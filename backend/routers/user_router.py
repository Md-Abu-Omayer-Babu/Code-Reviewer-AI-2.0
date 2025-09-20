"""
User router with clean OOP structure.

This module provides user-related routes using the new OOP architecture
with proper dependency injection and separation of concerns.
"""

from typing import Dict, Any
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..controllers.auth_controller import get_current_active_user
from ..services.user_service import UserService
from ..repositories.user_repository import UserRepository
from ..models.user import User
from ..models.userInAlchemy import UserInAlchemy
from ..database.database import get_db


router = APIRouter(
    prefix="/users",
    tags=["user_operations"]
)


@router.post("/register", response_model=Dict[str, Any])
async def register_user(
    username: str,
    password: str,
    email: str,
    full_name: str = None,
    db: Session = Depends(get_db)
):
    """
    Register a new user.
    
    Args:
        username: Desired username
        password: User password
        email: User email address
        full_name: User's full name (optional)
        db: Database session
        
    Returns:
        Success message with user info
    """
    user_data = User(
        username=username,
        email=email,
        full_name=full_name,
        disabled=False
    )
    
    # Get service with repository
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    
    created_user = user_service.register_user(user_data, password, email)
    
    return {
        "message": "User registered successfully",
        "username": created_user.username,
        "email": created_user.email
    }


@router.get("/me", response_model=User)
async def get_current_user_info(
    current_user: UserInAlchemy = Depends(get_current_active_user)
):
    """
    Get current user information.
    
    Args:
        current_user: Current authenticated user
        
    Returns:
        Current user information
    """
    return User(
        username=current_user.username,
        email=current_user.email,
        full_name=current_user.full_name,
        disabled=current_user.disabled
    )


@router.put("/me", response_model=User)
async def update_current_user(
    full_name: str = None,
    email: str = None,
    current_user: UserInAlchemy = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Update current user information.
    
    Args:
        full_name: Updated full name
        email: Updated email
        current_user: Current authenticated user
        db: Database session
        
    Returns:
        Updated user information
    """
    update_data = {}
    if full_name is not None:
        update_data["full_name"] = full_name
    if email is not None:
        update_data["email"] = email
    
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No data provided for update"
        )
    
    user_data = User(
        username=current_user.username,
        email=email or current_user.email,
        full_name=full_name or current_user.full_name,
        disabled=current_user.disabled
    )
    
    # Get service with repository
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    
    updated_user = user_service.update_user(current_user.username, user_data)
    
    return User(
        username=updated_user.username,
        email=updated_user.email,
        full_name=updated_user.full_name,
        disabled=updated_user.disabled
    )
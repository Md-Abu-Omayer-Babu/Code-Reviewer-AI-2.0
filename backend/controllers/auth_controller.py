"""
Authentication controller for handling auth-related HTTP requests.

This module provides the AuthController class that handles all HTTP requests
related to authentication and coordinates with the AuthService.
"""

from typing import Dict, Any
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .base_controller import BaseController
from ..services.auth_service import AuthService
from ..services.user_service import UserService
from ..repositories.user_repository import UserRepository
from ..models.token import Token
from ..models.userInAlchemy import UserInAlchemy
from ..database.database import get_db


# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


# Dependency functions for current user
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> UserInAlchemy:
    """
    Dependency to get current authenticated user.
    
    Args:
        token: JWT access token
        db: Database session
        
    Returns:
        Current authenticated user
    """
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    auth_service = AuthService(user_service)
    
    return auth_service.get_current_user(token)


def get_current_active_user(
    current_user: UserInAlchemy = Depends(get_current_user)
) -> UserInAlchemy:
    """
    Dependency to get current active user.
    
    Args:
        current_user: Current authenticated user
        
    Returns:
        Current active user
        
    Raises:
        HTTPException: If user is disabled
    """
    if current_user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    return current_user


# Router for authentication endpoints
router = APIRouter(
    prefix="/auth",
    tags=["authentication"]
)


@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    Authenticate user and return access token.
    
    Args:
        form_data: OAuth2 form data with username and password
        db: Database session
        
    Returns:
        Access token and token type
    """
    # Get service with dependencies
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    auth_service = AuthService(user_service)
    
    return auth_service.login_user(
        username=form_data.username,
        password=form_data.password
    )


@router.post("/login-simple")
async def login_simple(
    username: str,
    password: str,
    db: Session = Depends(get_db)
):
    """
    Simple login endpoint for backward compatibility.
    
    Args:
        username: User's username
        password: User's password
        db: Database session
        
    Returns:
        Access token and token type
    """
    # Get service with dependencies
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    auth_service = AuthService(user_service)
    
    token = auth_service.login_user(username, password)
    
    return {
        "access_token": token.access_token,
        "token_type": token.token_type
    }


@router.post("/refresh", response_model=Token)
async def refresh_token(
    current_user: UserInAlchemy = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Refresh access token for current user.
    
    Args:
        current_user: Current authenticated user
        db: Database session
        
    Returns:
        New access token
    """
    # Get service with dependencies
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    auth_service = AuthService(user_service)
    
    return auth_service.refresh_token(current_user)


@router.get("/verify")
async def verify_token(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    """
    Verify if the provided token is valid.
    
    Args:
        token: JWT access token
        db: Database session
        
    Returns:
        Token verification status
    """
    # Get service with dependencies
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    auth_service = AuthService(user_service)
    
    token_data = auth_service.verify_token(token)
    
    return {
        "valid": True,
        "username": token_data.username,
        "message": "Token is valid"
    }
"""
User service for handling user-related business logic.

This module provides the UserService class that contains all business logic
related to user operations, including authentication and user management.
"""

from typing import Optional
from fastapi import HTTPException, status

from .base_service import BaseService
from ..repositories.user_repository import UserRepository
from ..models.user import User, UserInDB
from ..models.userInAlchemy import UserInAlchemy
from ..security.auth import get_password_hash, verify_password, authenticate_user


class UserService(BaseService[UserRepository]):
    """
    Service class for user-related business operations.
    
    This class encapsulates all business logic related to users,
    including registration, authentication, and user management.
    """
    
    def __init__(self, user_repository: UserRepository):
        """
        Initialize the user service.
        
        Args:
            user_repository: Repository for user data access
        """
        super().__init__(user_repository)
    
    def register_user(self, user: User, password: str, email: str) -> UserInAlchemy:
        """
        Register a new user with validation and password hashing.
        
        Args:
            user: User data
            password: Plain text password
            email: User email address
            
        Returns:
            Created user instance
            
        Raises:
            HTTPException: If user already exists or validation fails
        """
        # Check if username already exists
        if self.repository.username_exists(user.username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exists"
            )
        
        # Check if email already exists
        if self.repository.email_exists(email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        # Hash password and create user
        hashed_password = get_password_hash(password)
        user_data = UserInDB(
            **user.model_dump(),
            email=email,
            hashed_password=hashed_password
        )
        
        return self.repository.create_user(user_data)
    
    def authenticate_user(self, username: str, password: str) -> Optional[UserInAlchemy]:
        """
        Authenticate a user with username and password.
        
        Args:
            username: User's username
            password: Plain text password
            
        Returns:
            User instance if authentication successful, None otherwise
        """
        user = self.repository.get_by_username(username)
        if not user:
            return None
        
        if not verify_password(password, user.hashed_password):
            return None
        
        return user
    
    def get_user_by_username(self, username: str) -> Optional[UserInAlchemy]:
        """
        Get user by username.
        
        Args:
            username: The username to search for
            
        Returns:
            User instance or None if not found
        """
        return self.repository.get_by_username(username)
    
    def get_user_by_email(self, email: str) -> Optional[UserInAlchemy]:
        """
        Get user by email.
        
        Args:
            email: The email to search for
            
        Returns:
            User instance or None if not found
        """
        return self.repository.get_by_email(email)
    
    def update_user(self, username: str, user_data: User) -> UserInAlchemy:
        """
        Update user information.
        
        Args:
            username: Username of the user to update
            user_data: Updated user data
            
        Returns:
            Updated user instance
            
        Raises:
            HTTPException: If user not found
        """
        user = self.repository.update_user_by_username(username, user_data)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        return user
    
    def delete_user(self, username: str) -> UserInAlchemy:
        """
        Delete a user.
        
        Args:
            username: Username of the user to delete
            
        Returns:
            Deleted user instance
            
        Raises:
            HTTPException: If user not found
        """
        user = self.repository.delete_by_username(username)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        return user
    
    def get_current_user_info(self, username: str) -> User:
        """
        Get current user information (without sensitive data).
        
        Args:
            username: Username of the current user
            
        Returns:
            User information without sensitive data
            
        Raises:
            HTTPException: If user not found
        """
        user = self.repository.get_by_username(username)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        return User(
            username=user.username,
            email=user.email,
            full_name=user.full_name,
            disabled=user.disabled
        )
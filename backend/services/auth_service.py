"""
Authentication service for handling auth-related business logic.

This module provides the AuthService class that contains all business logic
related to authentication, token generation, and user session management.
"""

from typing import Optional
from fastapi import HTTPException, status
from jose import JWTError

from .base_service import BaseService
from .user_service import UserService
from ..models.user import User
from ..models.userInAlchemy import UserInAlchemy
from ..models.token import Token, TokenData
from ..security.oauth2 import create_access_token, decode_access_token


class AuthService(BaseService[UserService]):
    """
    Service class for authentication-related business operations.
    
    This class encapsulates all business logic related to authentication,
    including login, token generation, and user verification.
    """
    
    def __init__(self, user_service: UserService):
        """
        Initialize the authentication service.
        
        Args:
            user_service: Service for user operations
        """
        super().__init__(user_service)
    
    def login_user(self, username: str, password: str) -> Token:
        """
        Authenticate user and generate access token.
        
        Args:
            username: User's username
            password: User's plain text password
            
        Returns:
            Token object with access token and type
            
        Raises:
            HTTPException: If authentication fails
        """
        # Authenticate user
        user = self.repository.authenticate_user(username, password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # Check if user is active
        if user.disabled:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Inactive user"
            )
        
        # Generate access token
        access_token = create_access_token(data={"sub": user.username})
        
        return Token(
            access_token=access_token,
            token_type="bearer"
        )
    
    def get_current_user(self, token: str) -> UserInAlchemy:
        """
        Get current user from access token.
        
        Args:
            token: JWT access token
            
        Returns:
            Current user instance
            
        Raises:
            HTTPException: If token is invalid or user not found
        """
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
        try:
            # Decode token
            payload = decode_access_token(token)
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
                
            token_data = TokenData(username=username)
        except JWTError:
            raise credentials_exception
        
        # Get user from database
        user = self.repository.get_user_by_username(username=token_data.username)
        if user is None:
            raise credentials_exception
            
        return user
    
    def get_current_active_user(self, token: str) -> UserInAlchemy:
        """
        Get current active user from access token.
        
        Args:
            token: JWT access token
            
        Returns:
            Current active user instance
            
        Raises:
            HTTPException: If user is inactive or token invalid
        """
        current_user = self.get_current_user(token)
        
        if current_user.disabled:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Inactive user"
            )
            
        return current_user
    
    def verify_token(self, token: str) -> TokenData:
        """
        Verify and decode access token.
        
        Args:
            token: JWT access token
            
        Returns:
            Token data with username
            
        Raises:
            HTTPException: If token is invalid
        """
        try:
            payload = decode_access_token(token)
            username: str = payload.get("sub")
            if username is None:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Could not validate credentials"
                )
                
            return TokenData(username=username)
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials"
            )
    
    def refresh_token(self, current_user: UserInAlchemy) -> Token:
        """
        Generate a new access token for the current user.
        
        Args:
            current_user: Current authenticated user
            
        Returns:
            New token object
        """
        access_token = create_access_token(data={"sub": current_user.username})
        
        return Token(
            access_token=access_token,
            token_type="bearer"
        )
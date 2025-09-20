"""
Authentication utilities for password hashing and user verification.

This module provides functions for password hashing, verification,
and user authentication using bcrypt.
"""

from passlib.context import CryptContext
from sqlalchemy.orm import Session
from typing import Optional

from ..models.userInAlchemy import UserInAlchemy

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against a hashed password.
    
    Args:
        plain_password: The plain text password
        hashed_password: The hashed password to verify against
        
    Returns:
        True if password is correct, False otherwise
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Hash a plain text password.
    
    Args:
        password: Plain text password to hash
        
    Returns:
        Hashed password string
    """
    return pwd_context.hash(password)


def authenticate_user(username: str, password: str, db: Session) -> Optional[UserInAlchemy]:
    """
    Authenticate a user with username and password.
    
    Args:
        username: User's username
        password: Plain text password
        db: Database session
        
    Returns:
        User instance if authentication successful, None otherwise
    """
    from ..repositories.user_repository import UserRepository
    
    user_repository = UserRepository(db)
    user = user_repository.get_by_username(username)
    
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user
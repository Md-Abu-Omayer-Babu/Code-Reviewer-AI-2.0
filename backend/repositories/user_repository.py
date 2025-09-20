"""
User repository for handling user-related database operations.

This module provides the UserRepository class that encapsulates
all database operations related to users.
"""

from typing import Optional
from sqlalchemy.orm import Session

from .base import CRUDRepository
from ..models.userInAlchemy import UserInAlchemy
from ..models.user import User, UserInDB


class UserRepository(CRUDRepository[UserInAlchemy, UserInDB, User]):
    """
    Repository class for User entity operations.
    
    This class handles all database operations related to users,
    including authentication-specific queries.
    """
    
    def __init__(self, db: Session):
        """
        Initialize the user repository.
        
        Args:
            db: Database session
        """
        super().__init__(UserInAlchemy, db)
    
    def get_by_username(self, username: str) -> Optional[UserInAlchemy]:
        """
        Get a user by username.
        
        Args:
            username: The username to search for
            
        Returns:
            User instance or None if not found
        """
        return self.db.query(self.model).filter(
            self.model.username == username
        ).first()
    
    def get_by_email(self, email: str) -> Optional[UserInAlchemy]:
        """
        Get a user by email address.
        
        Args:
            email: The email address to search for
            
        Returns:
            User instance or None if not found
        """
        return self.db.query(self.model).filter(
            self.model.email == email
        ).first()
    
    def create_user(self, user_data: UserInDB) -> UserInAlchemy:
        """
        Create a new user with hashed password.
        
        Args:
            user_data: UserInDB schema containing user data with hashed password
            
        Returns:
            Created user instance
        """
        db_user = UserInAlchemy(**user_data.model_dump())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    def username_exists(self, username: str) -> bool:
        """
        Check if a username already exists.
        
        Args:
            username: The username to check
            
        Returns:
            True if username exists, False otherwise
        """
        return self.db.query(self.model).filter(
            self.model.username == username
        ).first() is not None
    
    def email_exists(self, email: str) -> bool:
        """
        Check if an email already exists.
        
        Args:
            email: The email to check
            
        Returns:
            True if email exists, False otherwise
        """
        return self.db.query(self.model).filter(
            self.model.email == email
        ).first() is not None
    
    def update_user_by_username(self, username: str, user_data: User) -> Optional[UserInAlchemy]:
        """
        Update a user by username.
        
        Args:
            username: The username of the user to update
            user_data: Updated user data
            
        Returns:
            Updated user instance or None if not found
        """
        db_user = self.get_by_username(username)
        if not db_user:
            return None
        
        update_data = user_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_user, field, value)
        
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    def delete_by_username(self, username: str) -> Optional[UserInAlchemy]:
        """
        Delete a user by username.
        
        Args:
            username: The username of the user to delete
            
        Returns:
            Deleted user instance or None if not found
        """
        db_user = self.get_by_username(username)
        if not db_user:
            return None
        
        self.db.delete(db_user)
        self.db.commit()
        return db_user
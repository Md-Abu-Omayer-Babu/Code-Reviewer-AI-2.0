"""
SQLAlchemy user model for database operations.

This module contains the SQLAlchemy model for user data persistence.
This model is separate from Pydantic models to follow clean architecture.
"""

from sqlalchemy import Column, String, Boolean, DateTime, func
from ..database.database import Base as UserBase


class UserInAlchemy(UserBase):
    """
    SQLAlchemy model for user data persistence.
    
    This model represents the user table structure in the database
    and handles all database-related operations for users.
    """
    __tablename__ = "users"
    
    username = Column(
        String(50), 
        primary_key=True, 
        index=True,
        nullable=False,
        doc="Unique username for the user"
    )
    email = Column(
        String(255),
        unique=True,
        index=True,
        nullable=True,
        doc="User's email address"
    )
    full_name = Column(
        String(100),
        nullable=True,
        doc="User's full name"
    )
    disabled = Column(
        Boolean,
        default=False,
        nullable=False,
        doc="Whether the user account is disabled"
    )
    hashed_password = Column(
        String(255),
        nullable=False,
        doc="Hashed password for authentication"
    )
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
        doc="Timestamp when user was created"
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
        doc="Timestamp when user was last updated"
    )

    def __repr__(self):
        """String representation of the user."""
        return f"<User(username='{self.username}', email='{self.email}')>"

    def __str__(self):
        """Human-readable string representation."""
        return f"User: {self.username} ({self.email})"
"""
Dependency injection container for managing application dependencies.

This module provides a centralized way to manage and inject dependencies
throughout the application, following the Dependency Inversion principle.
"""

from typing import Dict, Any, Callable
from sqlalchemy.orm import Session

from ..database.database import get_db
from ..repositories.user_repository import UserRepository
from ..services.user_service import UserService
from ..services.auth_service import AuthService
from ..services.file_service import FileService
from ..controllers.auth_controller import AuthController
from ..controllers.user_controller import UserController
from ..controllers.file_controller import FileController


class DependencyContainer:
    """
    Dependency injection container for managing application dependencies.
    
    This class provides a centralized way to create and manage dependencies,
    ensuring proper separation of concerns and testability.
    """
    
    def __init__(self):
        """Initialize the dependency container."""
        self._repositories: Dict[str, Any] = {}
        self._services: Dict[str, Any] = {}
        self._controllers: Dict[str, Any] = {}
    
    def get_user_repository(self, db: Session) -> UserRepository:
        """
        Get or create UserRepository instance.
        
        Args:
            db: Database session
            
        Returns:
            UserRepository instance
        """
        return UserRepository(db)
    
    def get_user_service(self, db: Session) -> UserService:
        """
        Get or create UserService instance with injected dependencies.
        
        Args:
            db: Database session
            
        Returns:
            UserService instance
        """
        user_repository = self.get_user_repository(db)
        return UserService(user_repository)
    
    def get_auth_service(self, db: Session) -> AuthService:
        """
        Get or create AuthService instance with injected dependencies.
        
        Args:
            db: Database session
            
        Returns:
            AuthService instance
        """
        user_service = self.get_user_service(db)
        return AuthService(user_service)
    
    def get_file_service(self) -> FileService:
        """
        Get or create FileService instance.
        
        Returns:
            FileService instance
        """
        return FileService()
    
    def get_auth_controller(self, db: Session) -> AuthController:
        """
        Get or create AuthController instance with injected dependencies.
        
        Args:
            db: Database session
            
        Returns:
            AuthController instance
        """
        auth_service = self.get_auth_service(db)
        return AuthController(auth_service)
    
    def get_user_controller(self, db: Session) -> UserController:
        """
        Get or create UserController instance with injected dependencies.
        
        Args:
            db: Database session
            
        Returns:
            UserController instance
        """
        user_service = self.get_user_service(db)
        return UserController(user_service)
    
    def get_file_controller(self) -> FileController:
        """
        Get or create FileController instance with injected dependencies.
        
        Returns:
            FileController instance
        """
        file_service = self.get_file_service()
        return FileController(file_service)


# Global container instance
container = DependencyContainer()


# FastAPI dependency functions
def get_user_repository(db: Session = get_db) -> UserRepository:
    """
    FastAPI dependency to get UserRepository.
    
    Args:
        db: Database session
        
    Returns:
        UserRepository instance
    """
    return container.get_user_repository(db)


def get_user_service(db: Session = get_db) -> UserService:
    """
    FastAPI dependency to get UserService.
    
    Args:
        db: Database session
        
    Returns:
        UserService instance
    """
    return container.get_user_service(db)


def get_auth_service(db: Session = get_db) -> AuthService:
    """
    FastAPI dependency to get AuthService.
    
    Args:
        db: Database session
        
    Returns:
        AuthService instance
    """
    return container.get_auth_service(db)


def get_file_service() -> FileService:
    """
    FastAPI dependency to get FileService.
    
    Returns:
        FileService instance
    """
    return container.get_file_service()


def get_auth_controller(db: Session = get_db) -> AuthController:
    """
    FastAPI dependency to get AuthController.
    
    Args:
        db: Database session
        
    Returns:
        AuthController instance
    """
    return container.get_auth_controller(db)


def get_user_controller(db: Session = get_db) -> UserController:
    """
    FastAPI dependency to get UserController.
    
    Args:
        db: Database session
        
    Returns:
        UserController instance
    """
    return container.get_user_controller(db)


def get_file_controller() -> FileController:
    """
    FastAPI dependency to get FileController.
    
    Returns:
        FileController instance
    """
    return container.get_file_controller()
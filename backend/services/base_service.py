"""
Base service classes for business logic layer.

This module provides abstract base classes for implementing services
that contain business logic and coordinate between repositories.
"""

from abc import ABC
from typing import Generic, TypeVar

# Generic types for service operations
RepositoryType = TypeVar('RepositoryType')


class BaseService(ABC, Generic[RepositoryType]):
    """
    Abstract base service class.
    
    This class provides a foundation for service classes that contain
    business logic and coordinate operations between repositories.
    """
    
    def __init__(self, repository: RepositoryType):
        """
        Initialize the service with its repository.
        
        Args:
            repository: The repository instance for data access
        """
        self.repository = repository
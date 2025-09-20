"""
Base controller classes for handling HTTP requests.

This module provides abstract base classes for implementing controllers
that handle HTTP requests and coordinate with services.
"""

from abc import ABC
from typing import Generic, TypeVar

# Generic type for service
ServiceType = TypeVar('ServiceType')


class BaseController(ABC, Generic[ServiceType]):
    """
    Abstract base controller class.
    
    This class provides a foundation for controller classes that handle
    HTTP requests and coordinate with services.
    """
    
    def __init__(self, service: ServiceType):
        """
        Initialize the controller with its service.
        
        Args:
            service: The service instance for business logic
        """
        self.service = service
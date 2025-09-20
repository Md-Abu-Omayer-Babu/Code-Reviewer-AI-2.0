"""
Base repository pattern implementation.

This module provides abstract base classes for implementing the Repository pattern,
which separates data access logic from business logic.
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List, Any
from sqlalchemy.orm import Session

# Generic type for model entities
ModelType = TypeVar('ModelType')
CreateSchemaType = TypeVar('CreateSchemaType')
UpdateSchemaType = TypeVar('UpdateSchemaType')


class BaseRepository(ABC, Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """
    Abstract base repository class implementing common CRUD operations.
    
    This class provides a generic interface for database operations
    following the Repository pattern.
    """
    
    def __init__(self, model: type[ModelType], db: Session):
        """
        Initialize the repository with a model and database session.
        
        Args:
            model: The SQLAlchemy model class
            db: Database session
        """
        self.model = model
        self.db = db
    
    @abstractmethod
    def create(self, obj_in: CreateSchemaType) -> ModelType:
        """Create a new record in the database."""
        pass
    
    @abstractmethod
    def get(self, id: Any) -> Optional[ModelType]:
        """Get a record by ID."""
        pass
    
    @abstractmethod
    def get_multi(self, skip: int = 0, limit: int = 100) -> List[ModelType]:
        """Get multiple records with pagination."""
        pass
    
    @abstractmethod
    def update(self, db_obj: ModelType, obj_in: UpdateSchemaType) -> ModelType:
        """Update an existing record."""
        pass
    
    @abstractmethod
    def delete(self, id: Any) -> ModelType:
        """Delete a record by ID."""
        pass


class CRUDRepository(BaseRepository[ModelType, CreateSchemaType, UpdateSchemaType]):
    """
    Concrete implementation of BaseRepository with common CRUD operations.
    
    This class provides standard database operations that can be used
    for most entities.
    """
    
    def create(self, obj_in: CreateSchemaType) -> ModelType:
        """
        Create a new record in the database.
        
        Args:
            obj_in: Pydantic schema with data to create
            
        Returns:
            Created database model instance
        """
        if hasattr(obj_in, 'model_dump'):
            obj_data = obj_in.model_dump()
        else:
            obj_data = obj_in.dict()
            
        db_obj = self.model(**obj_data)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj
    
    def get(self, id: Any) -> Optional[ModelType]:
        """
        Get a record by its primary key.
        
        Args:
            id: Primary key value
            
        Returns:
            Database model instance or None if not found
        """
        return self.db.query(self.model).filter(self.model.id == id).first()
    
    def get_multi(self, skip: int = 0, limit: int = 100) -> List[ModelType]:
        """
        Get multiple records with pagination.
        
        Args:
            skip: Number of records to skip
            limit: Maximum number of records to return
            
        Returns:
            List of database model instances
        """
        return self.db.query(self.model).offset(skip).limit(limit).all()
    
    def update(self, db_obj: ModelType, obj_in: UpdateSchemaType) -> ModelType:
        """
        Update an existing record.
        
        Args:
            db_obj: Existing database model instance
            obj_in: Pydantic schema with updated data
            
        Returns:
            Updated database model instance
        """
        if hasattr(obj_in, 'model_dump'):
            obj_data = obj_in.model_dump(exclude_unset=True)
        else:
            obj_data = obj_in.dict(exclude_unset=True)
            
        for field, value in obj_data.items():
            setattr(db_obj, field, value)
            
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj
    
    def delete(self, id: Any) -> ModelType:
        """
        Delete a record by its primary key.
        
        Args:
            id: Primary key value
            
        Returns:
            Deleted database model instance
            
        Raises:
            ValueError: If record not found
        """
        obj = self.db.query(self.model).filter(self.model.id == id).first()
        if not obj:
            raise ValueError(f"Record with id {id} not found")
            
        self.db.delete(obj)
        self.db.commit()
        return obj
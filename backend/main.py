"""
FastAPI application with clean OOP architecture.

This module sets up the FastAPI application using dependency injection,
repository pattern, and service-oriented architecture following SOLID principles.
"""

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .routers import user_router, file_router
from .controllers.auth_controller import router as auth_router
from .database.database import Base as UserBase, engine as UserEngine, get_db

# Legacy route imports (to be refactored later)
from .api.comments_finder_routes.comment_finder_api import router as comment_routers
from .api.class_finder_routes.class_finder import router as class_routers
from .api.function_finder_routes.function_finder import router as function_routers


def create_application() -> FastAPI:
    """
    Create and configure the FastAPI application.
    
    This function sets up the FastAPI application with all necessary
    middleware, routes, and dependency injection.
    
    Returns:
        Configured FastAPI application instance
    """
    # Create FastAPI application
    app = FastAPI(
        title="Code Reviewer AI Backend",
        description="A clean, OOP-structured FastAPI backend for code review operations",
        version="2.0.0",
        docs_url="/docs",
        redoc_url="/redoc"
    )

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # In production, replace with specific origins
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Create database tables
    UserBase.metadata.create_all(bind=UserEngine)

    # Include new OOP-structured routers
    include_routers(app)
    
    # Include legacy routers (to be refactored)
    include_legacy_routers(app)

    # Add root endpoint
    @app.get("/", tags=["root"])
    async def root():
        """
        Root endpoint returning application information.
        
        Returns:
            Application welcome message and version
        """
        return {
            "message": "Code Reviewer AI Backend",
            "version": "2.0.0",
            "architecture": "Clean OOP with Repository Pattern",
            "status": "running"
        }
    
    @app.get("/health", tags=["health"])
    async def health_check(db: Session = Depends(get_db)):
        """
        Health check endpoint to verify application and database status.
        
        Args:
            db: Database session for connectivity check
            
        Returns:
            Health status information
        """
        try:
            # Test database connection
            db.execute("SELECT 1")
            db_status = "healthy"
        except Exception as e:
            db_status = f"unhealthy: {str(e)}"
        
        return {
            "status": "healthy",
            "database": db_status,
            "version": "2.0.0"
        }

    return app


def include_routers(app: FastAPI) -> None:
    """
    Include all new OOP-structured routers.
    
    Args:
        app: FastAPI application instance
    """
    # Authentication routes
    app.include_router(auth_router)
    
    # User management routes  
    app.include_router(user_router.router)
    
    # File management routes
    app.include_router(file_router.router)


def include_legacy_routers(app: FastAPI) -> None:
    """
    Include legacy routers that need to be refactored.
    
    Args:
        app: FastAPI application instance
    """
    # These will be refactored to follow the new OOP pattern
    app.include_router(class_routers, tags=["legacy - to be refactored"])
    app.include_router(function_routers, tags=["legacy - to be refactored"])
    app.include_router(comment_routers, tags=["legacy - to be refactored"])


# Create the application instance
app = create_application()

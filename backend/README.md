# Code Reviewer AI Backend - Clean Architecture

A production-ready FastAPI backend built with clean Object-Oriented Programming (OOP) principles, implementing the Repository pattern, dependency injection, and SOLID design principles.

## 🏗️ Architecture Overview

This refactored backend follows a clean, layered architecture that separates concerns and promotes maintainability:

```
backend/
├── controllers/          # HTTP request handlers (Presentation Layer)
├── services/            # Business logic (Application Layer)
├── repositories/        # Data access layer (Infrastructure Layer)
├── models/             # Database models (Domain Layer)
├── schemas/            # Request/Response models (API Layer)
├── core/               # Application configuration and DI
├── database/           # Database configuration
├── security/           # Authentication & authorization
└── api/               # Legacy routes (to be refactored)
```

## 🎯 Key Features

### ✅ Clean Architecture Principles
- **Separation of Concerns**: Each layer has a single responsibility
- **Dependency Inversion**: High-level modules don't depend on low-level modules
- **Repository Pattern**: Database access is abstracted through repositories
- **Service Layer**: Business logic is encapsulated in service classes
- **Dependency Injection**: Dependencies are injected rather than hardcoded

### ✅ SOLID Principles Implementation
- **Single Responsibility**: Each class has one reason to change
- **Open/Closed**: Classes are open for extension, closed for modification
- **Liskov Substitution**: Derived classes are substitutable for base classes
- **Interface Segregation**: Clients depend only on interfaces they use
- **Dependency Inversion**: Depend on abstractions, not concretions

### ✅ Modern FastAPI Features
- Comprehensive type hints and validation
- Automatic API documentation with OpenAPI/Swagger
- Pydantic models for request/response validation
- Dependency injection with FastAPI's `Depends()`
- Proper error handling and HTTP status codes

## 📁 Project Structure

### Controllers Layer
Controls HTTP requests and coordinates with services:
- `AuthController`: Authentication endpoints
- `UserController`: User management endpoints  
- `FileController`: File operations endpoints

### Services Layer
Contains business logic and coordinates between repositories:
- `UserService`: User-related business operations
- `AuthService`: Authentication and token management
- `FileService`: File handling and validation

### Repositories Layer
Handles data access and database operations:
- `BaseRepository`: Abstract base for all repositories
- `CRUDRepository`: Common CRUD operations
- `UserRepository`: User-specific database operations

### Models & Schemas
- `models/`: SQLAlchemy database models
- `schemas/`: Pydantic request/response models

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- SQLite (or your preferred database)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the backend directory:
   ```env
   SECRET_KEY=your-secret-key-here
   DATABASE_URL=sqlite:///User.db
   DEBUG=True
   ENVIRONMENT=development
   ```

5. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

6. **Access the API**
   - API Documentation: http://localhost:8000/docs
   - Alternative docs: http://localhost:8000/redoc
   - Health check: http://localhost:8000/health

## 📚 API Endpoints

### Authentication
- `POST /auth/login` - User login
- `POST /auth/refresh` - Refresh access token
- `GET /auth/verify` - Verify token validity

### User Management
- `POST /users/register` - Register new user
- `GET /users/me` - Get current user info
- `PUT /users/me` - Update current user

### File Operations
- `GET /files/` - List user files
- `POST /files/upload` - Upload files
- `GET /files/{filename}` - Get file content
- `DELETE /files/{filename}` - Delete file

### Health & Status
- `GET /` - Root endpoint with app info
- `GET /health` - Application health check

## 🏛️ Architecture Patterns

### Repository Pattern
Separates data access logic from business logic:
```python
class UserRepository(CRUDRepository):
    def get_by_username(self, username: str) -> Optional[UserInAlchemy]:
        return self.db.query(self.model).filter(
            self.model.username == username
        ).first()
```

### Service Layer
Encapsulates business logic:
```python
class UserService(BaseService):
    def register_user(self, user: User, password: str) -> UserInAlchemy:
        # Business logic for user registration
        if self.repository.username_exists(user.username):
            raise HTTPException(...)
        # Hash password, validate, create user
```

### Dependency Injection
Uses FastAPI's dependency system:
```python
def get_user_service(db: Session = Depends(get_db)) -> UserService:
    user_repository = UserRepository(db)
    return UserService(user_repository)
```
4. Set up environment variables:
	- Copy `.env.example` to `.env` and fill in the required values (if applicable).


### Running the Backend
It is recommended to use FastAPI's development server for local development:
```powershell
fastapi dev main.py
```
The backend will start and listen for API requests (default: http://localhost:8000 or as configured).

## API Overview
- Authentication: `/api/login_register_routes/`, `/api/token_routes/`
- User Management: `/api/user_routes/`
- File Operations: `/api/file_operations_routes/`
- Class Finder: `/api/class_finder_routes/`
- Function Finder: `/api/function_finder_routes/`
- Comment Finder: `/api/comments_finder_routes/`

Each route folder contains the relevant endpoints. See code for details or use an API tool (e.g., Postman) to explore.

## Database
- The backend uses a database file (`User.db`) for user and token storage.
- Database connection logic is in `database/database.py`.

## Testing
- Unit tests are in `unit_tests/` and `tests/`.
- To run tests:
  ```powershell
  pytest
  ```

## Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes
4. Push to your branch
5. Open a pull request

## License
This project is licensed under the MIT License.

## Contact
For questions or support, please open an issue or contact the maintainer.

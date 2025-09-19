# Code Reviewer AI Backend

This is the backend service for the Code Reviewer AI project. It provides RESTful APIs for user authentication, file operations, code analysis (class, function, and comment extraction), and user management. The backend is built with Python and is designed to work seamlessly with the frontend (Next.js) for a full-stack AI-powered code review platform.

## Features
- User Authentication: Register, login, and token-based authentication.
- File Operations: Upload, read, write, and delete code files.
- Code Analysis: Extract classes, functions, and comments from uploaded code files.
- User Management: CRUD operations for user profiles.
- Security: OAuth2, password hashing, and token management.
- Database Support: User data and tokens are stored in a database.

## Project Structure
```
backend/
├── api/                  # API route modules (class, function, comment, file, user, token)
├── database/             # Database connection and models
├── models/               # Pydantic and ORM models
├── security/             # Authentication and OAuth2 logic
├── services/             # Business logic and utilities
├── tests/                # Test suites
├── unit_tests/           # Unit tests
├── uploads/              # Uploaded code files
├── utils/                # Utility scripts
├── main.py               # Application entry point
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Getting Started

### Prerequisites
- Python 3.12+
- pip (Python package manager)

### Installation
1. Clone the repository:
	```powershell
	git clone <repo-url>
	cd "Code Reviewer AI/Development 2.0/backend"
	```
2. (Optional) Create a virtual environment:
	```powershell
	python -m venv venv
	.\venv\Scripts\activate
	```
3. Install dependencies:
	```powershell
	pip install -r requirements.txt
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

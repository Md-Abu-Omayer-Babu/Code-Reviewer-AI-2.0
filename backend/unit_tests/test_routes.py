from fastapi import status
from fastapi.testclient import TestClient
import os
from ..main import app

client = TestClient(app)

# Create test directory for files if it doesn't exist
test_dir = "./db"
if not os.path.exists(test_dir):
    os.makedirs(test_dir)

# File Operations Routes Tests
def test_api_running():
    response = client.get("/files/test_api")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "This Test API is working!"}

def test_get_all_files():
    response = client.get("/files/get_all_files")
    assert response.status_code == status.HTTP_200_OK
    assert "files" in response.json()

def test_upload_file():
    # Use the correct parameter name "files" instead of "file"
    response = client.post("/files/upload", files=[("files", ("test.py", "print('Hello World')"))])
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "File uploaded successfully"}

def test_file_content():
    # Ensure the file exists before testing
    if not os.path.exists("./db/test.py"):
        with open("./db/test.py", "w") as f:
            f.write("print('Hello World')")
            
    response = client.get("/files/get_contents/test.py")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"content": "print('Hello World')"}

def test_delete_file():
    # Ensure the file exists before testing
    if not os.path.exists("./db/test.py"):
        with open("./db/test.py", "w") as f:
            f.write("print('Hello World')")
            
    response = client.delete("/files/delete/test.py")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "File deleted successfully"}

# Class Finder Routes Tests
def test_class_finder_root():
    response = client.get("/class_finding/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Class finder APIs are working!"}

def test_get_classes():
    # First create the test file directly in the correct location
    with open("./db/test_class.py", "w") as f:
        f.write("class TestClass:\n    pass")
    
    # Then test the class finder
    response = client.get("/class_finding/get_classes/test_class.py")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"classes": ["TestClass"]}
    
    # Clean up
    if os.path.exists("./db/test_class.py"):
        os.remove("./db/test_class.py")

# Comments Finder Routes Tests
def test_comments_finder_root():
    response = client.get("/comments_finding/root")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Comments finder routes is working...."}

def test_get_comments():
    # First create the test file directly in the correct location
    with open("./db/test_comments.py", "w") as f:
        f.write("# This is a test comment\nprint('Hello') # Inline comment")
    
    # Then test the comments finder
    response = client.get("/comments_finding/get_comments/test_comments.py")
    assert response.status_code == status.HTTP_200_OK
    assert "comments" in response.json()
    assert "# This is a test comment" in response.json()["comments"]
    assert "# Inline comment" in response.json()["comments"]
    
    # Clean up
    if os.path.exists("./db/test_comments.py"):
        os.remove("./db/test_comments.py")

# Function Finder Routes Tests
def test_get_functions():
    # First create the test file directly in the correct location
    with open("./db/test_functions.py", "w") as f:
        f.write("def test_function():\n    pass\n\nclass TestClass:\n    def class_method(self):\n        pass")
    
    # Then test the function finder
    response = client.get("/functions/get_functions/test_functions.py")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"functions": ["test_function", "class_method"]}
    
    # Clean up
    if os.path.exists("./db/test_functions.py"):
        os.remove("./db/test_functions.py")

def test_get_functions_under_classes():
    # First create the test file directly in the correct location
    with open("./db/test_class_functions.py", "w") as f:
        f.write("def global_function():\n    pass\n\nclass TestClass:\n    def class_method(self):\n        pass")
    
    # Then test the function under classes finder
    response = client.get("/functions/get_functions_under_classes/test_class_functions.py")
    assert response.status_code == status.HTTP_200_OK
    expected_response = {
        "functions_under_classes": {
            "Global_Functions": ["global_function"],
            "TestClass": ["class_method"]
        }
    }
    assert response.json() == expected_response
    
    # Clean up
    if os.path.exists("./db/test_class_functions.py"):
        os.remove("./db/test_class_functions.py")

# Login Routes Tests
def test_login_root():
    response = client.get("/login/root")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Login api working..."}

# test login with valid email
def test_login_with_valid_email():
    response = client.post("/login/login_api",
        data={"email": "test@example.com", "password": "test123"}
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"email": "test@example.com", "password": "test123"}

# test login with invalid email
def test_login_with_invalid_email():
    response = client.post("/login/login_api",
        data={"email": "invalid-email", "password": "test123"}
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Invalid email"}

# Registration Routes Tests
def test_register_root():
    response = client.get("/register/root")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Register api working..."}

def test_register_with_valid_email():
    response = client.post(
        "/register/register_api",
        data={"name": "Test User", "email": "test@example.com", "password": "test123"}
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"name": "Test User", "email": "test@example.com", "password": "test123"}

def test_register_with_invalid_email():
    response = client.post(
        "/register/register_api",
        data={"name": "Test User", "email": "invalid-email", "password": "test123"}
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Invalid email"}

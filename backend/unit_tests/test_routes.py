from fastapi import status
from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_api_running():
    response = client.get("/files/test_api")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "This Test API is working!"}
    
def test_upload_file():
    response = client.post("/files/upload", files={"file": ("test.py", "print('Hello World')")})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "File uploaded successfully"}

def test_file_content():
    response = client.get("/files/get_contents/test.py")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"content": "print('Hello World')"}

# def test_class_finder():
#     response = client.get("/class_finding/class_finder?filename=test.py")
#     assert response.status_code == status.HTTP_200_OK
#     assert response.json() == {"classes": []}

def test_delete_file():
    response = client.delete("/files/delete/test.py")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "File deleted successfully"}

def test_comments_router_root():
    response = client.get("/comments_finding/root")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Comments finder routes is working...."}

# def test_get_comments():
#     response = client.get("/comments_finding/get_comments?filename=example.py")
#     assert response.status_code == status.HTTP_200_OK
#     assert response.json() == {"comments": ""}
import os

def get_user_upload_dir(username: str) -> str:
    path = f'uploads/{username}'
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
    return path
from fastapi import UploadFile

def WriteFile(file_path: str, file_obj: UploadFile):
    with open(file_path, "wb") as file:
        file.write(file_obj.file.read())
        return {"message": "File uploaded successfully"}
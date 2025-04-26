from fastapi import UploadFile

class FileWriter:
    @staticmethod
    def write_file(file_path: str, file_obj: UploadFile) -> dict:
        with open(file_path, "wb") as file:
            file.write(file_obj.file.read())
            return {"message": "File uploaded successfully"}
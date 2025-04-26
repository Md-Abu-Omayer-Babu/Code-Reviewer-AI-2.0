import os
from fastapi import HTTPException

class FileDeleter:
    @staticmethod
    def delete_file(file_path):
        if not file_path.exists():
            raise HTTPException(status_code=404, detail="File not found")
        
        try:
            os.remove(file_path)
            return {"message": "File deleted successfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
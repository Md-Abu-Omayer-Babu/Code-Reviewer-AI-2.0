class FileValidator:
    @staticmethod
    def isPython(file_name: str) -> bool:
        if file_name.endswith(".py"):
            return True
        return False
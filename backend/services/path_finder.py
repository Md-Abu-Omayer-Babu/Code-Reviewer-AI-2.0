from pathlib import Path

class PathFinder:
    @staticmethod
    def find_path(file_name, uploaded_dir) -> Path:
        return Path(uploaded_dir) / file_name
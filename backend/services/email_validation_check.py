import re

class EmailValidator:
    @staticmethod
    def is_valid_email(email: str) -> bool:
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
        return re.match(pattern, email) is not None
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from ..models.user import UserInDB
from ..models.userInAlchemy import UserInAlchemy
from ..models.user import User
from ..services.user_utils import get_user

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(username: str, password: str, db: Session):
    user = get_user(db=db, username=username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
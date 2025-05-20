from sqlalchemy.orm import Session
from ..models.userInAlchemy import UserInAlchemy

def get_user(db: Session, username: str):
    user = db.query(UserInAlchemy).filter(UserInAlchemy.username == username).first()
    return user
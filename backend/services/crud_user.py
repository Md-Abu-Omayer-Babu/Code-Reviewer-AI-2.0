from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import HTTPException, status

from ..models.user import UserInDB
from ..models.userInAlchemy import UserInAlchemy
from ..security.auth import get_password_hash, verify_password

from ..models.user import User
from ..database.database import get_db


def userCreator(user: User, password: str, email: str, db: Session = Depends(get_db)):
    if db.query(UserInAlchemy).filter(UserInAlchemy.username == user.username).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    
    hashed_password = get_password_hash(password)
    db_user = UserInDB(**user.model_dump(), hashed_password=hashed_password)
    user_with_hashed_pwd = UserInAlchemy(**db_user.model_dump())
    
    db.add(user_with_hashed_pwd)
    db.commit()
    db.refresh(user_with_hashed_pwd)
    return user_with_hashed_pwd


def getUserByUsername(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(UserInAlchemy).filter(UserInAlchemy.username == username).first()
    if not user:
        return None
    if not verify_password(hashed_password=user.hashed_password, plain_password=password):
        return None
    return user

def getUserByUsernameWithoutPassword(username: str, db: Session):
    return db.query(UserInAlchemy).filter(UserInAlchemy.username == username).first()

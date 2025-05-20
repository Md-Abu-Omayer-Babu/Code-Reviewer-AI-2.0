from sqlalchemy import Column, String, Boolean
from ..database.database import Base as UserBase
    
class UserInAlchemy(UserBase):
    __tablename__ = "User"
    
    username = Column(String, primary_key=True, index=True)
    email = Column(String)
    full_name = Column(String)
    disabled = Column(Boolean, default=False)
    hashed_password = Column(String)
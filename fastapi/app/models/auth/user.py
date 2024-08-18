from sqlalchemy import Column, Integer, String
from app.models.base import Base
from pydantic import BaseModel

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
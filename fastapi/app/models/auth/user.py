from sqlalchemy import Column, Integer, String
from app.models.base import Base

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
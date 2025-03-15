# from db.base_class import Base 
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

# from db.base_class import Base

Base = declarative_base()
metadata = Base.metadata

class User(Base):
    __tablename__ = "user"
    
    id: int = Column(Integer, primary_key=True, index=True)
    email: str = Column(String, unique=True, index=True, nullable=False)
    password: str = Column(String, nullable=False)
    is_active: bool = Column(Boolean, default=True)
    blogs = relationship("Blog", back_populates="author")
    
    def __repr__(self):
        return super().__repr__() + f" id: {self.id}"
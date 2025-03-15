from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from db.models.default_user import User

from sqlalchemy.ext.declarative import declarative_base

# from db.base_class import Base

Base = declarative_base()
metadata = Base.metadata

class Blog(Base):
    __tablename__ = "blog"
    
    id: int = Column(Integer, primary_key=True, index=True) 
    title: str = Column(String, index=True, nullable=False)
    slug: str = Column(String, index=True, nullable=False)
    content: str = Column(Text, nullable=True)
    author_id: int = Column(Integer, ForeignKey(User.id))
    author = relationship(User, back_populates="blogs")
    created_at: datetime = Column(DateTime, default=datetime.now)
    is_active: bool = Column(Boolean, default=True)
    
    def __repr__(self):
        return super().__repr__() + f" title: {self.title}, id: {self.id}"
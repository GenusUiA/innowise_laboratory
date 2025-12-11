from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

# Base class for model
class Base(DeclarativeBase):
    pass

# Book class for store the book in database
class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer)
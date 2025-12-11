from typing import Optional
from fastapi import Depends, FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import *
from pydantic import BaseModel

# Create the table
Base.metadata.create_all(bind=engine)

app = FastAPI()

# schema for validate books
class BookValid(BaseModel):
    title: str 
    author: str
    year: Optional[int] = None
    
# Create dependency to connect with database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books/")
def add_a_new_book(data: BookValid, db: Session = Depends(get_db)):
    '''Add a new book'''
    book = Book(
        title=data.title, 
        author=data.author, 
        year=data.year)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

@app.get("/books/")
def get_all_books(db: Session = Depends(get_db)):
    '''Get all books'''
    return db.query(Book).all()

@app.delete("/books/{book_id}")
def delete_a_book_by_id(book_id: int, db: Session = Depends(get_db)):
    '''Delete book by id'''
    book = db.query(Book).filter(Book.id == book_id).first()
    if book == None:
        return JSONResponse(status_code=404, content={"message": "Book is not found"})
    db.delete(book)
    db.commit()
    return book
    
@app.put("/books/{book_id}")
def update_book_details(book_id: int, data: BookValid,  db: Session = Depends(get_db)):
    '''Update book by details'''
    
    book = db.query(Book).filter(Book.id == book_id).first()
    
    if book == None:
        return JSONResponse(status_code=404, content={"message": "book is not found"})    
    book.title = data.title
    book.author = data.author
    book.year = data.year
    db.commit()
    db.refresh(book)
    return book

@app.get("/books/search/")
def search_books_by_parameters(title:str | None = None, 
                               author:str | None = None, 
                               year:int | None = None, 
                               db: Session = Depends(get_db)):
    '''Search books by parameters'''
    book = db.query(Book)
    if title:
        book = book.filter(Book.title.ilike(f"%{title}%"))
    if author:
        book = book.filter(Book.author.ilike(f"%{author}%"))
    if year:
        book = book.filter(Book.year == year)
    return book.all()
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import *
from models.book_model import *
from schemas.book_schema import BookOut, BookValid

# Create the table
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Create dependency to connect with database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books/", response_model=BookOut, status_code=201)
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

@app.get("/books/", response_model=list[BookOut])
def get_all_books(db: Session = Depends(get_db)):
    '''Get all books'''
    return db.query(Book).all()

@app.delete("/books/{book_id}", status_code=204)
def delete_a_book_by_id(book_id: int, db: Session = Depends(get_db)):
    '''Delete book by id'''
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="the book is not found")
    db.delete(book)
    db.commit()

@app.put("/books/{book_id}", response_model=BookOut)
def update_book_details(book_id: int, data: BookValid,  db: Session = Depends(get_db)):
    '''Update book by details'''
    
    book = db.query(Book).filter(Book.id == book_id).first()
    
    if book == None:
        raise HTTPException(status_code=404, detail="book is not found")    
    book.title = data.title
    book.author = data.author
    book.year = data.year
    db.commit()
    db.refresh(book)
    return book

@app.get("/books/search/", response_model=list[BookOut])
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
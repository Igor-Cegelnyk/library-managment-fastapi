from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import get_all_authors, get_author_by_id, create_author, create_book, get_all_books
from database import SessionLocal
from schemas import Author, AuthorCreate, Book, BookCreate

app = FastAPI()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/authors", response_model=List[Author])
def _get_all_author(
        db: Session = Depends(get_db),
        limit: int | None = None,
        skip: int | None = None
):
    return get_all_authors(db=db, limit=limit, skip=skip)


@app.get("/authors/{author_id}", response_model=Author)
def _get_author_by_id(
        author_id: int,
        db: Session = Depends(get_db)
):
    author = get_author_by_id(db=db, author_id=author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@app.post("/authors/", response_model=Author)
def _create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    db_author = create_author(db=db, author=author)
    return db_author


@app.post("/books/", response_model=Book)
def _create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = create_book(db=db, book=book)
    return db_book


@app.get("/books", response_model=List[Book])
def _get_all_books(
        book_id: int | None = None,
        limit: int | None = None,
        skip: int | None = None,
        db: Session = Depends(get_db),
):
    books = get_all_books(db=db, limit=limit, skip=skip, book_id=book_id)
    if not books:
        raise HTTPException(status_code=404, detail="Book not found")

    return books

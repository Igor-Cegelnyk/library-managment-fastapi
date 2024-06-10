from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import get_all_authors, get_author_by_id, create_author
from database import SessionLocal
from schemas import Author, CreateAuthor

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


@app.get("/author", response_model=List[Author])
def _get_all_author(
        db: Session = Depends(get_db),
        limit: int = 10,
        skip: int = 0
):
    return get_all_authors(db=db, limit=limit, skip=skip)


@app.get("/author/{author_id}", response_model=Author)
def _get_author_by_id(
        author_id: int,
        db: Session = Depends(get_db)
):
    author = get_author_by_id(db=db, author_id=author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@app.post("/authors/", response_model=Author)
def _create_author(author: CreateAuthor, db: Session = Depends(get_db)):
    db_author = create_author(db=db, author=author)
    return db_author

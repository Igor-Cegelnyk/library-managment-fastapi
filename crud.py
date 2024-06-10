from sqlalchemy.orm import Session

from models import DBAuthor, DBBook
from schemas import AuthorCreate, BookCreate


def get_all_authors(
        db: Session,
        limit: int | None,
        skip: int | None
):
    queryset = db.query(DBAuthor)
    if limit:
        queryset = queryset.limit(limit)
    if skip:
        queryset = queryset.offset(skip)
    return queryset.all()


def get_author_by_id(db: Session, author_id: int):
    return db.query(DBAuthor).filter(DBAuthor.id == author_id).first()


def create_author(db: Session, author: AuthorCreate):
    db_author = DBAuthor(
        name=author.name,
        bio=author.bio
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)

    return db_author


def create_book(db: Session, book: BookCreate):
    db_book = DBBook(
        title=book.title,
        summary=book.summary,
        publication_date=book.publication_date,
        author_id=book.author_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return db_book
    

def get_all_books(
        db: Session,
        limit: int | None,
        skip: int | None,
        book_id: int | None
):
    queryset = db.query(DBBook)
    if limit:
        queryset =queryset.limit(limit)
    if skip:
        queryset =queryset.offset(skip)
    if book_id:
        queryset = queryset.filter(DBBook.id == book_id)
    return queryset.all()
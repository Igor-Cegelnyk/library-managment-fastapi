from sqlalchemy.orm import Session

from models import DBAuthor
from schemas import CreateAuthor


def get_all_authors(db: Session, limit: int, skip: int):
    return db.query(DBAuthor).limit(limit).offset(skip).all()


def get_author_by_id(db: Session, author_id: int):
    return db.query(DBAuthor).filter(DBAuthor.id == author_id).first()


def create_author(db: Session, author: CreateAuthor):
    db_author = DBAuthor(
        name=author.name,
        bio=author.bio
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)

    return db_author


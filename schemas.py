from pydantic import BaseModel


class AuthorBase(BaseModel):
    name: str
    bio: str


class CreateAuthor(AuthorBase):
    pass


class Author(AuthorBase):
    id: int

    class Config:
        orm_mode: True

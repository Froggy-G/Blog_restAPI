from pydantic import BaseModel


class BlogsBase(BaseModel):
    title: str
    author: int


class BlogsList(BlogsBase):
    id: int

    class Config:
        orm_mode = True
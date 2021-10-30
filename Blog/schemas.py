from pydantic import BaseModel
from fastapi_users import models
from pydantic.types import UUID4


class BlogsBase(BaseModel):
    title: str
    author: UUID4

    class Config:
        orm_mode = True


class BlogsList(BlogsBase):
    id: int


class BlogCreate(BlogsBase):
    pass


# ---Users
class User(models.BaseUser):
    pass


class UserCreate(models.BaseUserCreate):
    name: str


class UserUpdate(models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass
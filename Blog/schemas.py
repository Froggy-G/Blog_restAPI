from pydantic import BaseModel
from fastapi_users import models


class BlogsBase(BaseModel):
    title: str
    # author: int

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
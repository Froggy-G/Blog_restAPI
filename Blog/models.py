from sqlalchemy import Column, String, Text, Integer, Boolean, ForeignKey
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from Core.db import Base
from fastapi_users_db_sqlalchemy import GUID


class Blogs(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    author = Column(GUID, ForeignKey("user.id"))


class Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(Text())
    draft = Column(Boolean())
    blog_posts = Column(Integer, ForeignKey("blogs.id"))


class Tags(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    content = Column(String(30))
    post_tags = Column(Integer, ForeignKey("posts.id"))


class UserTable(Base, SQLAlchemyBaseUserTable):
    name = Column(String(100))

# class Users(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True)
#     name = Column(String(100))
#     hashed_password = Column(String())
#     is_superuser = Column(Boolean(), default=False)

class Subscribers(Base):
    __tablename__ = "subscribers"

    users_id = Column(GUID, ForeignKey("user.id"), primary_key=True)
    blogs_id = Column(Integer, ForeignKey("blogs.id"), primary_key=True)
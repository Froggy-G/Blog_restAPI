from sqlalchemy import Column, String, Text, Integer, Boolean, ForeignKey
from Core.db import Base


class Blogs(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))


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


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    hashed_password = Column(String())
    is_superuser = Column(Boolean())

class Subscribers(Base):
    __tablename__ = "subscribers"

    users_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    blogs_id = Column(Integer, ForeignKey("blogs.id"), primary_key=True)
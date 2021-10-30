from sqlalchemy import Column, String, Text, Integer, Boolean, ForeignKey
from fastapi_users.db import SQLAlchemyBaseUserTable
from fastapi_users_db_sqlalchemy import GUID
from sqlalchemy.orm import relationship
from Core.db import Base


class Blog(Base):
    __tablename__ = "blog"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    author = Column(GUID, ForeignKey("user.id"))
    user = relationship("user")

blogs = Blog.__table__

class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(Text())
    draft = Column(Boolean())
    blog = Column(Integer, ForeignKey("blog.id"))
    blog_id = relationship("blog")

posts = Post.__table__

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    content = Column(String(30))
    post = Column(Integer, ForeignKey("post.id"))
    post_id = relationship("post")

tags = Tag.__table__

class UserTable(Base, SQLAlchemyBaseUserTable):
    name = Column(String(100))
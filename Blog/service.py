from sqlalchemy.orm import Session
from .models import Blog
from .schemas import BlogCreate


def get_blogs_list(db: Session):
    return db.query(Blog).all()

def create_blog(db: Session, item: BlogCreate):
    blog = Blog(**item.dict())
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog
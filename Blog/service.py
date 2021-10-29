from sqlalchemy.orm import Session
from .models import Blogs
from .schemas import BlogCreate


def get_blogs_list(db: Session):
    return db.query(Blogs).all()

def create_blog(db: Session, item: BlogCreate):
    blog = Blogs(**item.dict())
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog
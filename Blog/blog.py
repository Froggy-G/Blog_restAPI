from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Core.utils import get_db
from . import service
from .schemas import BlogCreate, BlogsList

router = APIRouter()


@router.get("/", response_model=List[BlogsList])
def blogs_list(db: Session = Depends(get_db)):                            
    return service.get_blogs_list(db)

@router.post("/")
def blog_create(item: BlogCreate, db: Session = Depends(get_db)):                            
    return service.create_blog(db, item)
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Core.utils import get_db
from . import service
from .schemas import BlogCreate, BlogsList

router = APIRouter()


@router.get("/", response_model=List[BlogsList])
async def blog_list():                            
    return await service.get_blog_list()

@router.post("/")
async def blog_create(item: BlogCreate):                            
    return await service.create_blog(item)
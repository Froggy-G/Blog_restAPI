from fastapi import APIRouter
from Blog import blog


routes = APIRouter()

routes.include_router(blog.router, prefix="/blog")
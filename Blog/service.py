from .models import Blog
from .models import blogs
from .schemas import BlogCreate
from Core.db import database


async def get_blog_list():
    return await database.fetch_all(query=blogs.select())

async def create_blog(item: BlogCreate):
    blog = blogs.insert().values(**item.dict())
    return await database.execute(blog)
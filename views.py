from fastapi import FastAPI
from models import Users, Posts, Blogs, Tags

class Blog_api():
    app = FastAPI()


    @app.get("/")
    def main_page():                            # список всех блогов
        return {"blogs": Blogs}

    @app.get("/blog/{blog_id}")
    def blog_page(blog: int):                # просмотр отдельного блога
        return {"blog_id": Blogs}
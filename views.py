from fastapi import FastAPI

class Blog_api():
    app = FastAPI()
    

    @app.get("/")
    def main_page():                            
        return {"user": "hi"}
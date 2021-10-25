import uvicorn
from views import Blog_api

blog = Blog_api

blog()

if __name__ == "__main__":
    uvicorn.run("main:Blog_api.app", port=8000, reload=True)
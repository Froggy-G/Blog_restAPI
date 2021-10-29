from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response
from routes import routes
from fastapi_users import FastAPIUsers
# from Core.db import SessionLocal
from Core.db import database
from Blog.logic import jwt_authentication, get_user_manager
from Blog.schemas import User, UserCreate, UserUpdate, UserDB
import uvicorn


app = FastAPI()

fastapi_users = FastAPIUsers(
    get_user_manager,
    [jwt_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)

# @app.middleware("http")
# async def db_session_middleware(request: Request, call_next):
#     response = Response("Internal server error", status_code=500)
#     try:
#         request.state.db = SessionLocal()
#         response = await call_next(request)
#     finally:
#         request.state.db.close()
#     return response

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(routes)
app.include_router(fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt", tags=["auth"])
app.include_router(fastapi_users.get_register_router(), prefix="/auth", tags=["auth"])
app.include_router(fastapi_users.get_verify_router(), prefix="/auth", tags=["auth"])
app.include_router(fastapi_users.get_reset_password_router(), prefix="/auth", tags=["auth"])
app.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["users"])


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
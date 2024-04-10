from fastapi import FastAPI, HTTPException
from schema import AddUser, UserSignIn
from auth_db_orm import User
import asyncio
import uvicorn
from config import settings


app = FastAPI()


@app.post("/register")
async def register(user: AddUser):
    print(await User.check_user_exist(user.email))
    if await User.check_user_exist(user.email):
        await User.add_new_user(user.email, user.password)
        raise HTTPException(status_code=201, detail="success register")
    raise HTTPException(status_code=401, detail="user is already exist")


@app.post("/login")
async def login(user: UserSignIn):
    if await User.check_user_exist(user.email):
        raise HTTPException(status_code=402, detail="user is not exist")
    if await User.authentication(user.email, user.password):
        raise HTTPException(status_code=202, detail="authentication successfully")
    raise HTTPException(status_code=403, detail="incorrect email or password")


if __name__ == "__main__":
    asyncio.run(User.create_table())
    uvicorn.run(
        app="auth.auth:app",
        host="localhost",
        port=settings.AUTH_SERVICE_PORT,
        reload=True
    )
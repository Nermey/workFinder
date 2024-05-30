from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schema import AuthObj, AddNewAccount
from auth_db_orm import Auth_obj
import jwt
from config import settings

app = FastAPI()

origins = ["*"]  # cors для добавления разрешенных источников

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,  # cookie
                   allow_methods=["POST"],
                   allow_headers=["*"]
                   )


@app.on_event("startup")
async def startup_event():
    await Auth_obj.create_table()


def create_jwt(data):
    return jwt.encode(data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


@app.post("/register")
async def register_user(user: AddNewAccount):
    if await Auth_obj.check_user_exist(user.email):
        await Auth_obj.add_new_user(user.email, user.password, user.type)
        user_query = await Auth_obj.authentication(user.email, user.password)
        #  sent data to lk service
        raise HTTPException(status_code=201, detail=create_jwt(user_query[1]))
    raise HTTPException(status_code=401, detail="user is already exist")


@app.post("/login")
async def login_user(user: AuthObj):
    if await Auth_obj.check_user_exist(user.email):
        raise HTTPException(status_code=402, detail="user is not exist")
    user_query = await Auth_obj.authentication(user.email, user.password)
    if user_query and user_query[0]:
        raise HTTPException(status_code=202, detail=create_jwt(user_query[1]))
    raise HTTPException(status_code=403, detail="incorrect email or password")

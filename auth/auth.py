from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schema import AuthObj
from auth_db_orm import User, Company
import asyncio
import uvicorn
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


@app.post("/register/user")
async def register_user(user: AuthObj):
    print(await User.check_user_exist(user.email))
    if await User.check_user_exist(user.email):
        await User.add_new_user(user.email, user.password)
        raise HTTPException(status_code=201, detail="success register")
    raise HTTPException(status_code=401, detail="user is already exist")


@app.post("/login/user")
async def login_user(user: AuthObj):
    if await User.check_user_exist(user.email):
        raise HTTPException(status_code=402, detail="user is not exist")
    if await User.authentication(user.email, user.password):
        raise HTTPException(status_code=202, detail="authentication successfully")
    raise HTTPException(status_code=403, detail="incorrect email or password")


@app.post("/register/company")
async def register_company(company: AuthObj):
    if await Company.check_user_exist(company.email):
        await User.add_new_user(company.email, company.password)
        raise HTTPException(status_code=201, detail="success register")
    raise HTTPException(status_code=401, detail="user is already exist")


@app.post("/login/user")
async def login_user(company: AuthObj):
    if await Company.check_user_exist(company.email):
        raise HTTPException(status_code=402, detail="company is not exist")
    if await Company.authentication(company.email, company.password):
        raise HTTPException(status_code=202, detail="authentication successfully")
    raise HTTPException(status_code=403, detail="incorrect email or password")

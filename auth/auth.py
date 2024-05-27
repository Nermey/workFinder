from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schema import AuthObj
from auth_db_orm import Auth_obj
import asyncio

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


@app.post("/register/user")
async def register_user(user: AuthObj):
    print(await Auth_obj.check_user_exist(user.email))
    if await Auth_obj.check_user_exist(user.email):
        await Auth_obj.add_new_user(user.email, user.password)
        raise HTTPException(status_code=201, detail="success register")
    raise HTTPException(status_code=401, detail="user is already exist")


@app.post("/login")
async def login_user(user: AuthObj):
    if await Auth_obj.check_user_exist(user.email):
        raise HTTPException(status_code=402, detail="user is not exist")
    if await Auth_obj.authentication(user.email, user.password):
        raise HTTPException(status_code=202, detail="authentication successfully")
    raise HTTPException(status_code=403, detail="incorrect email or password")


@app.post("/register/company")
async def register_company(company: AuthObj):
    if await Auth_obj.check_user_exist(company.email):
        await Auth_obj.add_new_user(company.email, company.password)
        raise HTTPException(status_code=201, detail="success register")
    raise HTTPException(status_code=401, detail="user is already exist")

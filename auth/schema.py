from pydantic import BaseModel


class AuthObj(BaseModel):
    email: str
    password: str


class UserDTO(BaseModel):
    id: int


class AddNewUser(BaseModel):
    email: str
    password: str
    name: str
    surname: str
    bio: str
    phone: str


class AddNewCompany(BaseModel):
    name: str
    email: str
    phone: str
    password: str
    bio: str

from pydantic import BaseModel


class AuthObj(BaseModel):
    email: str
    password: str


class UserDTO(BaseModel):
    id: int
    type: str


class AddNewAccount(BaseModel):
    name: str
    bio: str
    email: str
    password: str
    phone: str
    type: str

from pydantic import BaseModel


class AddUser(BaseModel):
    email: str
    password: str


class UserSignIn(BaseModel):
    email: str
    password: str


class UserDTO(BaseModel):
    id: int

from pydantic import BaseModel, EmailStr


class BookModel(BaseModel):
    title: str
    author: str
    year: int
    available: bool


class UserModel(BaseModel):
    name: str
    email: EmailStr
    membership_id: str

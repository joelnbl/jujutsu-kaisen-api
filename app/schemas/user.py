from enum import StrEnum

from pydantic import BaseModel, EmailStr


class UserRole(StrEnum):
    USER = "user"
    ADMIN = "admin"


class UserRead(BaseModel):
    id: int
    email: EmailStr
    username: str
    role: UserRole


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

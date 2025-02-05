from sqlmodel import Field, Relationship
from typing import Optional, List
from pydantic import EmailStr
from .common import BaseModel

class User(BaseModel, table=True):
    __tablename__= "users"
    firstname: str
    lastname: str
    username: str = Field(unique=True)
    email: EmailStr = Field(unique=True)
    password: str
    is_verified: Optional[bool] = Field(default=False)
    otp: int

    posts: List["post"] = Relationship(back_populates="users")
    
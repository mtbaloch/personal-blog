from sqlmodel import Field, Relationship
from .common import BaseModel

from uuid import UUID
class Post(BaseModel, table=True):
    __tablename__ = "posts"
    title: str
    content: str
    category: str
    author_id : UUID = Field(foreign_key="users.id")
    author : "User" = Relationship(back_populates="posts")
    

    
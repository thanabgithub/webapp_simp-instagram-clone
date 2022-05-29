"""
this module demonstrates format of request and response from clients
"""

from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):

    class Config():
        orm_mode = True

    username: str
    email: str
    password: str


class UserDisplay(BaseModel):

    class Config():
        orm_mode = True

    username: str
    email: str


class PostBase(BaseModel):

    class Config():
        orm_mode = True

    image_url: str
    image_url_type: str
    caption: str
    user_id: int


# For PostDisplay
class User(BaseModel):
    username: str


class PostDisplay(BaseModel):

    class Config:
        orm_mode = True

    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user_id: int
    user: User

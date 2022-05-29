"""
this module demonstrates format of request and response from clients

caution:
    for display data structure we need to use
    class Config():
        orm_mode = True
"""

from pydantic import BaseModel
from datetime import datetime
from typing import List


class UserBase(BaseModel):

    username: str
    email: str
    password: str


class UserDisplay(BaseModel):

    class Config:
        orm_mode = True

    username: str
    email: str


class PostBase(BaseModel):

    image_url: str
    image_url_type: str
    caption: str
    user_id: int


# For PostDisplay
class User(BaseModel):

    class Config:
        orm_mode = True

    username: str


class Comment(BaseModel):

    class Config():
        orm_mode = True

    text: str
    username: str
    timestamp: datetime


class PostDisplay(BaseModel):

    class Config:
        orm_mode = True

    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    comments: List[Comment]
    user: User


class UserAuth(BaseModel):
    id: int
    isername: str
    email: str

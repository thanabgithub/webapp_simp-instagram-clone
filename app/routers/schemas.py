"""
    this module demonstrates format of request and response from clients


    class with the name ...Base is used handle a request from client to crud as an object
    class with the name ...Display is used handle a response from crud to client

    class without Base or Display is a child class of another Display class
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


# For PostDisplay and CommentDisplay
class _Username(BaseModel):

    class Config:
        orm_mode = True

    username: str


# For PostDisplay
class Comment(BaseModel):

    class Config():
        orm_mode = True

    text: str
    user: _Username
    timestamp: datetime


class PostDisplay(BaseModel):

    class Config:
        orm_mode = True

    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    comments: List[Comment]    # Please don't confused with CommentBase
    user: _Username    # get only username from UserBase. This mechanism is enabled by established relation from model.py


class UserAuth(BaseModel):
    id: int
    username: str
    email: str


class CommentBase(BaseModel):

    text: str
    post_id: int


class CommentDisplay(BaseModel):

    class Config:
        orm_mode = True

    timestamp: datetime
    user: _Username    # Please don't confused with UserBase
    text: str

class UserMailVerify(BaseModel):

    id: int
    user_id: str
    email: str
    hash: str
    active : bool
    timestamp: datetime
    
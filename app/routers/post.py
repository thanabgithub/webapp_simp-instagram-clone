"""
This module manage any request and response to/from clients
"""

from fastapi import APIRouter, Depends, status, UploadFile, File
from fastapi.exceptions import HTTPException

# enable ability to handle request and response
from routers.schemas import PostBase, PostDisplay

# connect to database
from db.database import get_db
from sqlalchemy.orm import Session

# handle crud operation of post
from db import crud_post

# handle authentication
from routers.schemas import UserAuth
from auth.oauth2 import get_current_user

# others
from typing import List
import random
import string
import shutil

router = APIRouter(prefix="/post", tags=["post"])

image_url_types = ["absolute", "relative"]


@router.post("", response_model=PostDisplay)
def create(
    request: PostBase,
    db: Session = Depends(get_db),
    current_user: UserAuth = Depends(get_current_user),
):
    if not request.image_url_type in image_url_types:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=
            "Paramerter image_url_type can only take values 'absolute' or relative",
        )

    return crud_post.create(db, request, current_user)


@router.get("/all", response_model=List[PostDisplay])
def posts(db: Session = Depends(get_db)):
    return crud_post.get_all(db)


@router.post("/image")
def upload_image(
    image: UploadFile = File(...),
    current_user: UserAuth = Depends(get_current_user),
):
    ## file name need to be unique so we add a subfix
    letters = string.ascii_letters
    rand_str = "".join(random.choice(letters) for i in range(6))
    print(rand_str)
    new = f"_{rand_str}."
    filename = new.join(image.filename.rsplit(".", 1))
    path = f"images/{filename}"

    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {"filename": path}


@router.get("/delete/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserAuth = Depends(get_current_user),
):

    return crud_post.delete(db, id, current_user.id)

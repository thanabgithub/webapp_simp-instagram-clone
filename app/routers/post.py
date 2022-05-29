"""
This module manage any request and response to/from clients
"""

from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
# enable ability to handle request and response
from routers.schemas import PostBase, PostDisplay
# connect to database
from db.database import get_db
from sqlalchemy.orm import Session
# handle crud operation of post
from db import crud_post
# others
from typing import List

router = APIRouter(prefix="/post", tags=["post"])

image_url_types = ["absolute", "relative"]


@router.post("", response_model=PostDisplay)
def create(request: PostBase, db: Session = Depends(get_db)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=
            "Paramerter image_url_type can only take values 'absolute' or relative"
        )

    return crud_post.create(db, request)


"""
@router.get("/all", response_model=List[PostDisplay])
def posts(db: Session = Depends(get_db)):
    return crud_post.get_all(db)"""

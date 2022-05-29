from fastapi import APIRouter, Depends
from db.database import get_db
from sqlalchemy.orm import Session
from db import crud_comment
from auth.oauth2 import get_current_user
from routers.schemas import CommentBase, CommentDisplay, UserAuth
# others
from typing import List

router = APIRouter(prefix="/comment", tags=["comment"])


@router.post("")
def create(
        request: CommentBase,
        db: Session = Depends(get_db),
        current_user: UserAuth = Depends(get_current_user),
):
    return crud_comment.create(db, request, current_user)


@router.get("/all/{post_id}", response_model=List[CommentDisplay])
def comments(post_id: int, db: Session = Depends(get_db)):

    return crud_comment.get_all(db, post_id)

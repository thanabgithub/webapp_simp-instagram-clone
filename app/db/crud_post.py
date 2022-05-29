# FRONTEND
from routers.schemas import PostBase, UserAuth    # define format web request and web response from client
from fastapi import HTTPException, status
# CRUD
from sqlalchemy.orm.session import Session    # define how we handle the base to operate CRUD
# BACKEND
from db.models import DbPost    # define format of database table and relationship

# Others
import datetime
from typing import Literal


def create(db: Session, request: PostBase, current_user: UserAuth):
    # left-side refers to backend
    # right-side refers to frontend

    new_post = DbPost(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        timestamp=datetime.datetime.now(),
        user_id=current_user.id,
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_all(db: Session):
    return db.query(DbPost).all()


def delete(db: Session, id: int, user_id: int) -> Literal[str]:
    post = db.query(DbPost).filter(DbPost.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} not found")
    if post.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Only post creator can delete pot")
    db.delete(post)
    db.commit()
    return 'ok'

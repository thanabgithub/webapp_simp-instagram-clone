# FRONTEND : define format web request and web response from client
from routers.schemas import PostBase
from fastapi import HTTPException, status
# CRUD : define how we handle the base to operate CRUD
from sqlalchemy.orm.session import Session
# BACKEND : define format of database table and relationship
from db.models import DbPost, DbComment
from datetime import datetime
from routers.schemas import CommentBase, UserAuth


def create(db: Session, request: CommentBase, current_user: UserAuth):
    post = db.query(DbPost).filter(DbPost.id == request.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {request.post_id} not found")
    new_comment = DbComment(text=request.text,
                            timestamp=datetime.now(),
                            post_id=request.post_id,
                            user_id=current_user.id)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def get_all(db: Session, post_id: int):
    return db.query(DbComment).filter(DbComment.post_id == post_id).all()

# FRONTEND
from routers.schemas import (
    PostBase,)    # define format web request and web response from client

# BACKEND
from db.models import DbPost    # define format of database table and relationship

# CRUD
from sqlalchemy.orm.session import (
    Session,)    # define how we handle the base to operate CRUD

# others
import datetime


def create(db: Session, request: PostBase):
    # left-side refers to backend
    # right-side refers to frontend

    new_post = DbPost(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        timestamp=datetime.datetime.now(),
        user_id=request.user_id,
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_all(db: Session):
    return db.query(DbPost).all()

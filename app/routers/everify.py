from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import crud_user,crud_everify

from auth.oauth2 import get_current_user
from routers.schemas import UserAuth
import datetime

router = APIRouter(prefix="/everify", tags=["email_verify"])


@router.get("/{id}/{hash}")
def test_id_hash(id,hash, db: Session = Depends(get_db)):
    return crud_everify.check_db(id,hash,db)

@router.get("/random")
def random_hash( ):
    return crud_everify.random_hash()
 
@router.post("/insertdb")
def insert_db(
    db: Session = Depends(get_db),
    current_user: UserAuth = Depends(get_current_user) ):
    return crud_everify.insert_to_db(db,current_user)

# add query string
@router.post("/checkindb")
def check_db(
    db: Session = Depends(get_db),
    user_id : int = 0):
    return crud_everify.check_db_hash(db,user_id)
    
# add query string
@router.post("/updateindb")
def update_db(
    db: Session = Depends(get_db),
    user_id : int = 0,
    hash : str = 0):
    return crud_everify.update_db_bool(db,user_id,hash)

@router.post("/insertdb")
def insert_db(
    db: Session = Depends(get_db),
    current_user: UserAuth = Depends(get_current_user) ):
    return crud_everify.insert_to_db(db,current_user)

@router.get("/send_email")
def send_email_url( current_user: UserAuth = Depends(get_current_user)):
    return crud_everify.send_mail(current_user)
    
# need update to post and check user jwt
@router.post("/create_verify")
def create_verify_url( db: Session = Depends(get_db),current_user: UserAuth = Depends(get_current_user)):
    return crud_everify.create_mail(db,current_user)
    
@router.get("/verify_link")
def check_verify_hash( user_id : int,hash : str,db: Session = Depends(get_db)):
    return crud_everify.verify_mail(db,user_id,hash)

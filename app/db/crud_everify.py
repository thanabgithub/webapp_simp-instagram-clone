"""
CRUD for User table
"""
import datetime
from auth.oauth2 import get_current_user
from routers.schemas import UserBase,UserAuth
from sqlalchemy.orm.session import Session
from .models import DbUserMailVerify
from db.hashing import Hash
import secrets
from fastapi.exceptions import HTTPException
from fastapi import  status
from .email_config import config_port,config_smtp_server,config_sender_email,config_password

import smtplib, ssl





def check_db(id,hash,db: Session):
    return id+hash

def random_hash():
    token = secrets.token_urlsafe(16)
    return token
    
def insert_to_db(db: Session, current_user: UserAuth):

    new_email = DbUserMailVerify(
    
        timestamp=datetime.datetime.now(),
        user_id=current_user.id,
        email='321',
        hash='321',
        active=False,
        
    )
    db.add(new_email)
    db.commit()
    db.refresh(new_email)
    return new_email
    
 


def check_db_hash(db: Session, user_id: int ):
    user = db.query(DbUserMailVerify).filter(DbUserMailVerify.user_id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with user id {user_id} not found",
        )

    return user
    
def update_db_bool(db: Session, user_id: int , hash : str ):
    user = db.query(DbUserMailVerify).filter(DbUserMailVerify.user_id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with user id {user_id} not found",
        )
    elif user.hash == hash:
        setattr(user,"active",True)
        #user.active = True
        db.add(user)
        db.commit()
        db.refresh(user)
    return user.active



def send_mail(current_user: UserAuth):

    port = config_port # For SSL
    smtp_server = config_smtp_server
    sender_email = config_sender_email  # Enter your address
    receiver_email = current_user.email  # Enter receiver address
    password = config_password
    message = f"""\
    Subject: Hi there

    This message is sent from fastapi in docker to {receiver_email}"""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        
    return '200'

def helper_send_mail(re_email,user_id,hash):

    port = config_port # For SSL
    smtp_server = config_smtp_server
    sender_email = config_sender_email  # Enter your address
    receiver_email = re_email  # Enter receiver address
    password = config_password

    url = f"""http://localhost:8000/everify/verify_link/?user_id={user_id}&hash={hash}"""
    message = f"""\
    Subject: Hi there

    This message is sent from fastapi in docker to {receiver_email} 
    Please Verify by this URL : {url}"""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        
    pass
    
def create_mail(db: Session,  current_user: UserAuth):

    user = db.query(DbUserMailVerify).filter(DbUserMailVerify.user_id == current_user.id).first()
    hash_token =secrets.token_urlsafe(16)
    if not user:
        user = DbUserMailVerify(
    
        timestamp=datetime.datetime.now(),
        user_id=current_user.id,
        email=current_user.email,
        hash=hash_token,
        active=False,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        helper_send_mail(current_user.email,current_user.id,hash_token)        
        return user
    else:
        return "email already sent please check in spam email box"
        
def verify_mail(db: Session,user_id,hash):  

    user = db.query(DbUserMailVerify).filter(DbUserMailVerify.user_id == user_id).first()
    if user.active == True:
        return "user already active"
    elif user.hash == hash:
        setattr(user,"active",True)
        #user.active = True
        db.add(user)
        db.commit()
        db.refresh(user)
        return user.active  
    else:
        return "your verify email meet unexpect case please contact us via email"        


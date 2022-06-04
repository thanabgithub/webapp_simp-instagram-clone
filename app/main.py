from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from db import models
from db.database import engine
from routers import user, post, comment ,everify
import os
from fastapi.staticfiles import StaticFiles
from auth import authentication

app = FastAPI()

# app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

# add router
app.include_router(user.router)
app.include_router(post.router)
app.include_router(comment.router)
app.include_router(authentication.router)
app.include_router(everify.router)

@app.get("/")
def root():
    return "Hello world"


models.Base.metadata.create_all(engine)

app.mount("/images", StaticFiles(directory="images"), name="images")

from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from starlette.middleware.cors import CORSMiddleware

from db import models
from db.database import engine
from routers import user, post, comment
import os
from fastapi.staticfiles import StaticFiles
from auth import authentication
from starlette.middleware import Middleware

from starlette.middleware import Middleware



origins = [
    "http://front.tiangolo.com",
    "https://front.tiangolo.com",
    "http://front",
    "http://front:3000",
    "https://front",
    "https://front:3000",


    "front",
    "front:8000",

    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
    "https://localhost",
    "https://localhost:3000",

    "http://localhost",
    "http://localhost:80",
    "https://localhost",
    "https://localhost:443",
    "http://8.219.139.91",


]
middleware = [
    Middleware(CORSMiddleware, allow_origins=origins)
]


app = FastAPI()

# app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

# add router
app.include_router(user.router)
app.include_router(post.router)
app.include_router(comment.router)
app.include_router(authentication.router)


@app.get("/")
def root():
    return "Hello world"



models.Base.metadata.create_all(engine)

app.mount("/images", StaticFiles(directory="images"), name="images")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

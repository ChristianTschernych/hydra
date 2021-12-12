import enum
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi import Body

from random import randrange
from time import sleep

import psycopg2 as psy
from psycopg2.extras import RealDictCursor
from starlette.routing import Host

from database import engine, get_db
from sqlalchemy.orm import Session
import models
from routers import post, user



models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)


@app.get("/")
def check():
    return {"message": "Hello World. This is fastAPI speaking!"}




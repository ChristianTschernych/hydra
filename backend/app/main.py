import enum
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
from time import sleep

import psycopg2 as psy
from psycopg2.extras import RealDictCursor
from starlette.routing import Host
import models
from database import engine, get_db
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

categories = ["Travel", "Food", "Shopping", "Retro"]
my_posts = [{"title":"Title of post 1", "content":"content of post 1", "id":0},
{"title":"FoodBoy", "content":"I like pizza", "id":1}]

def find_post(id:int):
    for post in my_posts:
        if post['id'] == id:
            return {"data" : post}

def delete_post(id:int):
    for ind, post in enumerate(my_posts):
        if post["id"] == id:
            print(ind)
            my_posts.pop(ind)
            print(f"Post {id} was deleted!")
            return post

def find_index_post(id):
    for i, post in enumerate(my_posts):
        if post["id"] == id:
            return i
    return None


@app.get("/")
def check():
    return {"message": "Hello World. This is fastAPI speaking!"}

@app.get("/sqlalchemy")
def testing_sql(db: Session = Depends(get_db)):

    posts = db.query(models.Post).all()
    return {"data":posts}

@app.get("/posts")
def get_all_posts(db: Session = Depends(get_db)):

    posts = db.query(models.Post).all()
    return {"data":posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(new_post: Post, db: Session = Depends(get_db)):
    #%s sorgt für die Sanitization unseres INPUTs so kännen keine SQL Befehle übertragen werden
    will.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, 
    (new_post.title,new_post.content,new_post.published))

    new_post = will.fetchone()
    conn.commit()

    db.
    return {"data": new_post}

#Id ist ein path parameter
@app.get("/posts/{id}")
def get_post(id:int, db: Session = Depends(get_db)):
    #important to convert to int
    
    will.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
    post = will.fetchone()
    print(post)

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail= {"message":f"post with id {id} was not found!"})

        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {"message":f"post with id {id} was not found!"}
    return {"data" : post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_single_post(id:int, db: Session = Depends(get_db)):
    will.execute("""DELETE FROM posts WHERE id = %s RETURNING * """, (str(id)))

    post = will.fetchone()
    conn.commit()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"message": f"Post with id {id} could not be deleted!"})

    return {"message" : f"Post with id {id} was deleted!",
            "data" : post}

@app.put("/posts/{id}")
def update_post(id:int, post:Post, db: Session = Depends(get_db)):
    will.execute("""UPDATE posts SET title=%s, content=%s, published=%s WHERE id = %s RETURNING *""", 
    (post.title, post.content, post.published, id))
    updt_post = will.fetchone()
    conn.commit()

    if updt_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail={"message": f"Post with id {id} could not be updated!"})

    return {"message":f"Post with id {id} was updated!",
            "data":updt_post}
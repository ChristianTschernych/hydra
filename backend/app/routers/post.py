
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import Optional, List
import database
import utils, schemas, models

get_db = database.get_db

router = APIRouter()

#When we want to return a list of Pydantic cleaned response objects
@router.get("/posts", response_model=List[schemas.PostResponse])
def get_all_posts(db: Session = Depends(database.get_db),):

    posts = db.query(models.Post).all()
    return posts

@router.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_posts(new_post: schemas.PostCreate, db: Session = Depends(get_db)):
    #convert input to a instance of our model in models.py
    new_post = models.Post(**new_post.dict())
    #adding post to db table
    db.add(new_post)
    #commit changes
    db.commit()
    #get back the object we just created, in SQL this resambles the RETURNING * statement
    db.refresh(new_post)

    return new_post

#Id ist ein path parameter
@router.get("/posts/{id}", response_model=schemas.PostResponse)
def get_post(id:int, db: Session = Depends(get_db)):
    #important to convert to int
    
    # will.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
    # post = will.fetchone()
    # print(post)

    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail= {"message":f"post with id {id} was not found!"})

        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {"message":f"post with id {id} was not found!"}
    return post

@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_single_post(id:int, db: Session = Depends(get_db)):
    # will.execute("""DELETE FROM posts WHERE id = %s RETURNING * """, (str(id)))

    # post = will.fetchone()
    # conn.commit()

    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"message": f"Post with id {id} could not be deleted!"})

    post.delete(synchronize_session=False)
    db.commit()

    return {"message": "Successfull"}

@router.put("/posts/{id}", response_model=schemas.PostResponse)
def update_post(id:int, changed_post:schemas.PostCreate, db: Session = Depends(get_db)):
    # will.execute("""UPDATE posts SET title=%s, content=%s, published=%s WHERE id = %s RETURNING *""", 
    # (post.title, post.content, post.published, id))
    # updt_post = will.fetchone()
    # conn.commit()

    #Query object
    post_query = db.query(models.Post).filter(models.Post.id == id)
    #grab post from querry
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail={"message": f"Post with id {id} could not be updated!"})

    post_query.update(changed_post.dict(), synchronize_session=False)
    db.commit()

    return post_query.first()

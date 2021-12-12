
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
import database
import utils, schemas, models
from typing import Optional, List

get_db = database.get_db

router = APIRouter()

@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user:schemas.UserCreate, db: Session = Depends(get_db)):
    #Hashing the password
    user.password = utils.get_password_hash(user.password)
    #convert input to a instance of our model in models.py
    new_user = models.User(**user.dict())
    #adding post to db table
    db.add(new_user)
    #commit changes
    db.commit()
    #get back the object we just created, in SQL this resambles the RETURNING * statement
    db.refresh(new_user)

    return new_user

@router.get("/users/{id}", response_model=schemas.UserOutFull)
def get_user(id:int, db: Session = Depends(get_db)):
    user_query = db.query(models.User).filter(models.User.id == id)
    user = user_query.first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return user
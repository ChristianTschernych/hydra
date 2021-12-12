from pydantic import BaseModel, EmailStr
from sqlalchemy.sql.sqltypes import TIMESTAMP
from database import Base
from datetime import datetime

#Das hier ist ein Pdantic model. Die Aufgabe ist sicherzustellen welche
#Daten wir geschickt bekommen und welche wir zurückschicken
#Das Sqlalchemy model funktioniert unabgängig von diesem

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    #hiermit wird das model in ein dict umgewandelt
    #nun können wir unseren Routes das Zusatzargument
    #"Response Model" geben
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email:EmailStr
    password:str

class UserOut(BaseModel):
    id:int
    email:EmailStr
    class Config:
        orm_mode = True    

class UserOutFull(UserOut):
    created_at:datetime

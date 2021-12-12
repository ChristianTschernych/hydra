from time import time
from sqlalchemy.sql.expression import null, text
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import TIMESTAMP, Boolean
from sqlalchemy.util.langhelpers import public_factory
from database import Base
from sqlalchemy import column, Integer, String, Boolean


#Das hier ist ein SQLALchemy Model
#Aufgabe ist das erstellen und digitales darstellen unserer Tables
#welche auf unserem DB Server liegen
class Post(Base):
    __tablename__="posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title=Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, nullable=False, server_default="TRUE")
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)    
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

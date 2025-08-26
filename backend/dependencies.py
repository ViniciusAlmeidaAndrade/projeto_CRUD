from models import db
from fastapi import Depends, HTTPException
from sqlalchemy.orm import sessionmaker, Session
from models import User
# from main import SECRET_KEY, ALGORITHM, oauth2_schema
# from jose import jwt, JWTError

def pegar_sessao():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()



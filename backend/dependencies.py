from models import db
from fastapi import Depends, HTTPException
from sqlalchemy.orm import sessionmaker, Session
from models import User

def pegar_sessao():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()



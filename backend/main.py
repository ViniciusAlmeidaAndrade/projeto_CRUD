from fastapi import FastAPI
from passlib.context import CryptContext
import os


SECRET_KEY = os.getenv('SECRET_KEY')
app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from routes_authentication import routes_authentication
from routes_crud import routes_crud

app.include_router(routes_authentication)
app.include_router(routes_crud )

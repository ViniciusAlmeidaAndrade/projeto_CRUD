from fastapi import FastAPI
from typing import Union
import uvicorn
from pydantic import BaseModel
from fastapi import HTTPException
import psycopg2

app = FastAPI()

from routes_authentication import routes_authentication
from routes_crud import routes_crud

app.include_router(routes_authentication)
app.include_router(routes_crud )


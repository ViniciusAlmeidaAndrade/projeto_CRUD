# from fastapi import FastAPI
# from passlib.context import CryptContext
# from dotenv import load_dotenv
# import os
# from typing import Union
# import uvicorn
# from pydantic import BaseModel
# import psycopg2
from fastapi import APIRouter
# from schemas import ProjectsSchema

routes_crud = APIRouter(prefix="/projects", tags=["projects"])

# GET /projects: lista todos os projetos
@routes_crud.get("/")
async def projects():
    return {"message": "Hello World"}
    # from fastapi import HTTPException

# GET /projects/{id}: obtém detalhes de um projeto
@routes_crud.get("/{id}")
async def details(id: int):
    return("detalhes_projects")

# POST /projects: cria um novo projeto
@routes_crud.post("/")
async def new_project():
    return("new_projects")

# PUT /projects/{id}: edita um projeto existente
@routes_crud.patch("/{id}")
async def update_project():
    return("update_projects")

# DELETE /projects/{id}: remove um projeto
@routes_crud.delete("/{id}")
async def delete_projects():
    return("delete_projects")

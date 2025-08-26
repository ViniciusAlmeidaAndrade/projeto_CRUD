from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import pegar_sessao
from schemas import NewProject
from models import Project

routes_crud = APIRouter(prefix="/projects", tags=["projects"])

# GET /projects: lista todos os projetos
@routes_crud.get("/")
async def projeto():
    return {"message": "Hello World"}
    # from fastapi import HTTPException

# GET /projects/{id}: obtém detalhes de um projeto
@routes_crud.get("/{id}")
async def detalhes(id: int):
    return("detalhes_projects")

# POST /projects: cria um novo projeto
@routes_crud.post("/")
async def criar_projeto(new_project: NewProject, session: Session = Depends(pegar_sessao)):
    novo_projeto = Project(name= new_project.name, description=new_project.description )
    session.add(novo_projeto)
    session.commit()
    return{"message": f"Projeto criado com sucesso! Nome: {novo_projeto.name} ID: {novo_projeto.id}"}

# PUT /projects/{id}: edita um projeto existente
@routes_crud.patch("/{id}")
async def editar_projeto():
    return("update_projects")

# DELETE /projects/{id}: remove um projeto
@routes_crud.delete("/{id}")
async def excluir_projeto():
    return("delete_projects")

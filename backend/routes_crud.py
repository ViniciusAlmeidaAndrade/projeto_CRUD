from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import pegar_sessao, verificar_token
from schemas import NewProject,  UpdateProject
from models import Project

routes_crud = APIRouter(prefix="/projects", tags=["projects"], dependencies=[Depends(verificar_token)])

# GET /projects: lista todos os projetos
@routes_crud.get("/")
async def projeto():
    todos_projetos = Project.query.all()
    return todos_projetos

# GET /projects/{id}: obtém detalhes de um projeto
@routes_crud.get("/{id}")
async def detalhes(id: int, session: Session = Depends(pegar_sessao)):
    projeto = session.query(Project).filter(Project.id == id).first()
    if not projeto:
        raise HTTPException(status_code=400, detail="Projeto não encontrado ")

    return projeto

# POST /projects: cria um novo projeto
@routes_crud.post("/")
async def criar_projeto(new_project: NewProject, session: Session = Depends(pegar_sessao)):
    projeto = Project(name= new_project.name, description=new_project.description )
    session.add(projeto)
    session.commit()

    return{"message": f"Projeto criado com sucesso! Nome: {projeto.name} ID: {projeto.id}"}

# PATCH /projects/{id}: edita um projeto existente
@routes_crud.patch("/{id}")
async def editar_projeto(id: int,update_project: UpdateProject, session:Session = Depends(pegar_sessao)):
    projeto = session.query(Project).filter(Project.id == id).first()
    if not projeto:
        raise HTTPException(status_code=400, detail="Projeto não encontrado ")

    update_data = update_project.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(projeto, key, value)

    session.commit()
    session.refresh(projeto)

    return{"mensagem":"Projeto atualizado com sucesso!", "projeto": projeto}

# DELETE /projects/{id}: remove um projeto
@routes_crud.delete("/{id}")
async def excluir_projeto(id: int, session: Session = Depends(pegar_sessao)):
    projeto = session.query(Project).filter(Project.id == id).first()
    if not projeto:
        raise HTTPException(status_code=400, detail="Projeto não encontrado ")
    session.delete(projeto)
    session.commit()

    return None

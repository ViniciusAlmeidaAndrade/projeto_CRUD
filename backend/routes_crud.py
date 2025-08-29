from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import desc
from dependencies import pegar_sessao, verificar_token
from schemas import NewProject, UpdateProject, ProjectList, AllProject
from models import Project, User

routes_crud = APIRouter(prefix="/projects", tags=["projects"])
# , dependencies=[Depends(verificar_token)]

# GET /projects: lista todos os projetos
@routes_crud.get("/", response_model=list[ProjectList])
async def listar_projetos(session: Session = Depends(pegar_sessao)):
    todos_projetos = session.query(Project).order_by(desc(Project.created_at)).all()
    if not todos_projetos:
        raise HTTPException(status_code=400, detail="Nenhum projeto encontrado ")

    return todos_projetos

# GET /projects/{id}: obtém detalhes de um projeto
@routes_crud.get("/{id}", response_model=AllProject)
async def detalhes(id: int, session: Session = Depends(pegar_sessao)):
    projeto = session.query(Project).filter(Project.id == id).first()
    if not projeto:
        raise HTTPException(status_code=400, detail="Projeto não encontrado ")

    return projeto

# POST /projects: cria um novo projeto
@routes_crud.post("/", response_model=AllProject)
async def criar_projeto(new_project: NewProject, session: Session = Depends(pegar_sessao)):
    projeto = Project(name= new_project.name, description=new_project.description )
    session.add(projeto)
    session.commit()

    return projeto

# PATCH /projects/{id}: edita um projeto existente
@routes_crud.patch("/{id}", response_model=AllProject)
async def editar_projeto(id: int,update_project: UpdateProject, session:Session = Depends(pegar_sessao)):
    projeto = session.query(Project).filter(Project.id == id).first()
    if not projeto:
        raise HTTPException(status_code=404, detail="Projeto não encontrado ")

    update_data = update_project.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(projeto, key, value)

    session.commit()
    session.refresh(projeto)

    return projeto
# DELETE /projects/{id}: remove um projeto
@routes_crud.delete("/{id}")
async def excluir_projeto(id: int, session: Session = Depends(pegar_sessao)):
    # user: User = Depends(verificar_token) depois de (pegar_sessao)
    projeto = session.query(Project).filter(Project.id == id).first()
    if not projeto:
        raise HTTPException(status_code=400, detail="Projeto não encontrado ")
    session.delete(projeto)
    session.commit()

    return None

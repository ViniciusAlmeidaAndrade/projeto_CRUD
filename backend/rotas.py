from fastapi import APIRouter

rotas = APIRouter(prefix="/projects", tags=["projects"])

@rotas.get("/")
async def projects():
    return {"message": "Hello World"}

# GET /projects: lista todos os projetos
# GET /projects/{id}: obtém detalhes de um projeto
# POST /projects: cria um novo projeto
# PUT /projects/{id}: edita um projeto existente
# DELETE /projects/{id}: remove um projeto
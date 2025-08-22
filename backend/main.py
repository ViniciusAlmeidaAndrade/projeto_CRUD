from typing import Union
import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi import HTTPException
import psycopg2

# while True:
#     try:
#         conn = psycopg2.connect(
#             database="projeto_crud_db",
#             user="postgres",
#             password="V1n1c1us",
#             host="localhost",
#             port="5432"
#         )
#         cursor = conn.cursor()
#         print("Connected to database")
#         break
#     except Exception as error:
#         print("Not succesfull",error)


app = FastAPI()

from .rotas_autenticacao import rotas_autenticacao
from .rotas import rotas

app.include_router(rotas_autenticacao)
app.include_router(rotas)

# projects = []
#
# class Project(BaseModel):
#     """
#     Projeto
#     """
#     id: int
#     nome: str
#     descricao: str
#
# class Project_Create(BaseModel):
#     """Criação de projeto"""
#     nome: str
#     descricao: str
#
# @app.get("/projetos")
# def list_projects() -> list:
#     """Lista de todos os projetos"""
#     return projects
#
# @app.get("/projetos/{id}")
# def read_item(id: int):
#     """Detalhes do projeto"""
#     for detalhe in projects:
#         if detalhe ["id"] == id:
#             return detalhe
#     raise HTTPException(status_code=404, detail="Projeto não encontrado")
#
#
# @app.post("/projects")
# def create_project(project: Project_Create):
#     novo_id = len(projects) + 1
#     novo_produto = {
#         "id": novo_id,
#         "nome": project.nome,
#         "descricao": project.descricao,
#     }
#     projects.append(novo_produto)
#     return novo_produto
#
#
# @app.put("/projects/{id}")
# def update_project(id: int, atualizar_projeto:Project):
#     for atualize in projects:
#         if atualize["id"] == id:
#             atualize["nome"] = atualizar_projeto.nome
#             atualize["descricao"] = atualizar_projeto.descricao
#             return {"message":"Projeto atualizado!"}
#     raise HTTPException(status_code=404,detail="Projeto não encontrado")
#
# @app.delete("/projects/{id}")
# def delete_project(id: int):
#     for delete in projects:
#         if delete["id"] == id:
#             projects.remove(delete)
#             return {"message": f"Projeto {id} foi deletado!"}
#     raise HTTPException(status_code=404, detail="Projeto não encontrado")
#
# if __name__ == "__main__":
#     uvicorn.run(app, port=8000)

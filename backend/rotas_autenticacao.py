from fastapi import APIRouter
#importar do models tabela usuario

rotas_autenticacao = APIRouter(prefix="/autenticacao", tags=["autenticacao"])

@rotas_autenticacao.get("/")
async def autenticar():
    return {"message": "Hello World"}


@rotas_autenticacao.post("/criar_conta")
async def criar_conta(email: str, senha: str):
    usuario
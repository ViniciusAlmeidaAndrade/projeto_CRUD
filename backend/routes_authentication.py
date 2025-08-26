from fastapi import APIRouter, Depends, HTTPException
from models import User
from dependencies import pegar_sessao
from main import bcrypt_context
from schemas import UserSchema
from sqlalchemy.orm import Session

routes_authentication = APIRouter(prefix="/autenticacao", tags=["autenticacao"])

@routes_authentication.get("/")
async def autenticar():
    """
    Essa é a rota padrão de autenticação do nosso sistema
    """

    return {"message": "Você acessou a rota de autenticação", "autenticado": False}

@routes_authentication.post("/criar_conta")
async def criar_conta(user_schema: UserSchema, session: Session = Depends(pegar_sessao)) :

    user = session.query(User).filter(User.email == UserSchema.email).first()
    if user:
        raise HTTPException(status_code = 400, detail = "E-mail do usuário já cadastrado")
    else:
        senha_criptografada = bcrypt_context.hash(user_schema.password)
        novo_usuario = User(user_schema.name, user_schema.email, senha_criptografada)
        # novo_usuario = User(
        #     email = UsersSchemas.email,
        #     password = senha_criptografada,
        #     active = UsersSchemas.active,
        #     admin = UsersSchemas.admin
        #     )
        session.add(novo_usuario)
        session.commit()
        return {"mensagem":f"usuário cadastrado com sucesso {user_schema.email}"}
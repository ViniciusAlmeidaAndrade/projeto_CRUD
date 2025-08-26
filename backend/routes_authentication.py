from fastapi import APIRouter, Depends, HTTPException
from models import User
from dependencies import pegar_sessao
from main import bcrypt_context
from schemas import UserSchema, LoginSchema
from sqlalchemy.orm import Session

routes_authentication = APIRouter(prefix="/autenticacao", tags=["autenticacao"])

def criar_token(id_users):
    token = f"cweiqw0eico2{id_users}"
    return token

def autenticar_usuario(email, password, session):
    users = session.query(User).filter(User.email == email).first()
    if not users:
        return False
    elif not bcrypt_context.verify(password, users.password):
        return False
    return users

@routes_authentication.get("/")
async def autenticar():
    """
    Essa é a rota padrão de autenticação do nosso sistema
    """

    return {"message": "Você acessou a rota de autenticação", "autenticado": False}

@routes_authentication.post("/criar_conta")
async def criar_conta(user_schema: UserSchema, session: Session = Depends(pegar_sessao)) :

    users = session.query(User).filter(User.email == user_schema.email).first()
    if users:
        raise HTTPException(status_code = 400, detail = "E-mail do usuário já cadastrado")
    else:
        senha_criptografada = bcrypt_context.hash(user_schema.password)
        novo_usuario = User(user_schema.name, user_schema.email, senha_criptografada, user_schema.active, user_schema.admin)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem":f"usuário cadastrado com sucesso {user_schema.email}"}

@routes_authentication.post("/login")
async def login(login_schema: LoginSchema, session: Session = Depends(pegar_sessao)):
    users = autenticar_usuario(login_schema.email, login_schema.password, session)
    if not users:
        raise HTTPException(status_code = 400, detail = "Usuário não encontrado ou E-mail e senha incorretos")
    else:
        access_token = criar_token(users.id)
        return {
            "access_token": access_token,
            "token_type": "bearer"
            }
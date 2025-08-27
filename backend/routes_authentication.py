from fastapi import APIRouter, Depends, HTTPException
from models import User
from dependencies import pegar_sessao, verificar_token
from main import bcrypt_context, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY
from schemas import UserSchema, LoginSchema
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordRequestForm

routes_authentication = APIRouter(prefix="/autenticacao", tags=["autenticacao"])

def criar_token(id_users, duracao_token=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    data_expiracao = datetime.now(timezone.utc) + duracao_token
    dic_info= {"sub": str(id_users), "exp": data_expiracao}
    jwt_codificado = jwt.encode(dic_info, SECRET_KEY, ALGORITHM)
    return jwt_codificado


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
        return {"mensagem":f" Olá {user_schema.name} seu usuário foi cadastrado com sucesso: {user_schema.email}"}

@routes_authentication.post("/login")
async def login(login_schema: LoginSchema, session: Session = Depends(pegar_sessao)):
    users = autenticar_usuario(login_schema.email, login_schema.password, session)
    if not users:
        raise HTTPException(status_code = 400, detail = "Usuário não encontrado ou E-mail e senha incorretos")
    else:
        access_token = criar_token(users.id)
        refresh_token = criar_token(users.id, duracao_token=timedelta(days=7))
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

@routes_authentication.post("/login-form")
async def login_form(dados_formulario: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(pegar_sessao)):
    users = autenticar_usuario(dados_formulario.username, dados_formulario.password, session)
    if not users:
        raise HTTPException(status_code = 400, detail = "Usuário não encontrado ou E-mail e senha incorretos")
    else:
        access_token = criar_token(users.id)
        refresh_token = criar_token(users.id, duracao_token=timedelta(days=7))
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@routes_authentication.get("/refresh")
async def use_refresh_token(user: User = Depends(verificar_token)):
    access_token = criar_token(user.id)
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
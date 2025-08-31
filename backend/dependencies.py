from fastapi import Depends, HTTPException
from main import SECRET_KEY, ALGORITHM, oauth2_schema
from models import db, User
from sqlalchemy.orm import sessionmaker, Session
from jose import jwt, JWTError

def pegar_sessao():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()

def verificar_token(token: str = Depends(oauth2_schema), session: Session=Depends(pegar_sessao)):
    try:
        dic_inf = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id_user = int(dic_inf.get("sub"))
    except JWTError:
        raise HTTPException(status_code=401, detail="Acesso Negado, verifique a validade do token")
    user = session.query(User).filter(User.id == id_user).first()
    if not user:
        raise HTTPException(status_code=401, detail="Acesso Invalido")
    return user





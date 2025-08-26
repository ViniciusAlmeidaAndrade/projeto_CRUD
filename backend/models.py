from sqlalchemy import create_engine, Column, String, Integer, Text, DateTime, Boolean
from sqlalchemy.orm import declarative_base
import datetime

db = create_engine("postgresql://postgres:V1n1c1us@localhost/projeto_crud_db")

Base = declarative_base()

class Project(Base):
    __tablename__ = "projects"

    id = Column("id", Integer, primary_key=True, index=True)
    name = Column("name", String, nullable=False)
    description = Column("description", Text)
    status = Column("status", String, default="ativo") #Ex: ativo, pausado, finalizado
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, description, status= "Ativo"):
        self.name = name
        self.description = description
        self.status = status

class User(Base):
    __tablename__ = "user"

    id = Column("id", Integer, primary_key = True, autoincrement = True)
    name = Column("nome", String)
    email = Column("email", String, nullable = False)
    password = Column("senha", String)
    active = Column("active", Boolean)
    admin = Column("admin", Boolean, default = False)

    def __init__(self, name, email, password, active = True, admin = False):
        self.name = name
        self.email = email
        self.password = password
        self.active = active
        self.admin = admin
from sqlalchemy import create_engine, Column, String, Integer, Text, DateTime
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


from pydantic import BaseModel
from typing import Optional

class UserSchema (BaseModel):
    name: str
    email: str
    password: str
    active: Optional[bool]
    admin: Optional[bool]

    class Config:
        from_attributes = True
    # model_config = ConfigDict(from_attributes=True)

class NewProject(BaseModel):
    name: str
    description: str

    class Config:
        from_attributes = True

class LoginSchema(BaseModel):
    email: str
    password: str

    class Config:
        from_attributes = True


# class ProjetoBase(BaseModel):
#     name: str
#     description: str | None = None
#

# class Projetos(ProjetoBase):
#     id: int
#     # status: StatusProjeto
#     created: datetime
#
#     model_config = ConfigDict(from_attributes=True)

# class ProjetoEdit(BaseModel):
#     name: Optional[str] = None
#     description: Optional[str] = None
#     status: Optional[StatusProjeto] = None
#
#     model_config = ConfigDict(from_attributes=True)


from datetime import datetime
# class LoginSchema (BaseModel):
#     email: str
#     password: str

#     model_config = ConfigDict(from_attributes=True)
#
#
# class UserSchema:
#     pass
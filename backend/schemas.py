from pydantic import BaseModel, ConfigDict
from typing import Optional

class UserSchema (BaseModel):
    name: str
    email: str
    password: str
    active: Optional[bool]
    admin: Optional[bool]

    model_config = ConfigDict(from_attributes=True)

class LoginSchema(BaseModel):
    email: str
    password: str

    model_config = ConfigDict(from_attributes=True)

class ProjectResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    status: str

    model_config = ConfigDict(from_attributes=True)


class NewProject(BaseModel):
    name: str
    description: str

    model_config = ConfigDict(from_attributes=True)


class UpdateProject(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class AllProject(BaseModel):
    id: int
    name: str
    description: str | None = None
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

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

class ProjectList(BaseModel):
    id: int
    name: str
    status: str
    created_at: datetime

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


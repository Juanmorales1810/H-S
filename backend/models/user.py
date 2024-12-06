from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from models.empresas import Empresas

class User(BaseModel):
    correo: EmailStr
    password: str
    repeatepassword: str
    name: Optional[str]
    lastName: Optional[str]
    phone: Optional[str]
    empresas: Optional[Empresas]
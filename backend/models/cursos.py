from pydantic import BaseModel, Field
from typing import Optional

class Cursos(BaseModel):
    id: Optional[str] = Field(default=None)
    nombre: Optional[str] = Field(default=None)
    fecha: Optional[str] = Field(default=None)
    descripcion: Optional[str] = Field(default=None)
    activo: Optional[bool] = Field(default=False)

from pydantic import BaseModel, Field
from typing import Optional

class EmpresasProfesional(BaseModel):
    empresa: Optional[str] = Field(default=None)
    cuit: Optional[str] = Field(default=None)
    activo: Optional[bool] = Field(default=False)
    
class Profesionales(BaseModel):
    id: Optional[str] = Field(default=None)
    dni: Optional[int] = Field(default=None)
    nombre: Optional[str] = Field(default=None)
    apellido: Optional[str] = Field(default=None)
    cuil: Optional[str] = Field(default=None)
    fechaAlta: Optional[str] = Field(default=None)
    observacion: Optional[str] = Field(default=None)
    empresas: Optional[list[EmpresasProfesional]] = Field(default=[]) 
    activo: Optional[bool] = Field(default=False)

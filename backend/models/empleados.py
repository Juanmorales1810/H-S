from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Capacitaciones(BaseModel):
    curso: Optional[str] = Field(default=None)
    fecha: Optional[datetime] = Field(default=None)
    calificacion: Optional[float] = Field(default=None)

class Empleados(BaseModel):
    id: Optional[str] = Field(default=None)
    nombre: Optional[str] = Field(default=None)
    apellido: Optional[str] = Field(default=None)
    celular: Optional[str] = Field(default=None)
    dni: Optional[str] = Field(default=None)
    capacitaciones: Optional[list[Capacitaciones]] = Field(default=[])
    activo: Optional[bool] = Field(default=False)

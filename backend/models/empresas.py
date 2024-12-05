from pydantic import BaseModel, Field
from typing import Optional

class EmpresaContacto(BaseModel):
    nombre: Optional[str] = Field(default=None)
    apellido: Optional[str] = Field(default=None)
    celular: Optional[str] = Field(default=None)
    email: Optional[str] = Field(default=None)
    fechaAlta: Optional[str] = Field(default=None)
    observacion: Optional[str] = Field(default=None)
    activo: Optional[bool] = Field(default=False)

class Empresas(BaseModel):
    id: Optional[str] = Field(default=None)
    cuit: Optional[int] = Field(default=None)
    razonSocial: Optional[str] = Field(default=None)
    rubro: Optional[str] = Field(default=None)
    domicilio: Optional[str] = Field(default=None)
    fechaAlta: Optional[str] = Field(default=None)
    observacion: Optional[str] = Field(default=None)
    claveArt: Optional[str] = Field(default=None)
    contacto: Optional[list[EmpresaContacto]] = Field(default=[])
    activo: Optional[bool] = Field(default=False)

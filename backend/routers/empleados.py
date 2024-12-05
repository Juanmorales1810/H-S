# routers/empleados.py
from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel

# ----------------------------------------------------
from models.empleados import Empleados
# ----------------------------------------------------
from querys.empleados import get_empleados, add_empleados, put_empleados
# ----------------------------------------------------
empleados = APIRouter()

@empleados.get("/empleados/", response_model=List[Empleados])
async def fetch_empleados():
    try:
        return await get_empleados()
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al obtener los datos: {e}"
        )

@empleados.post("/empleados/", status_code=201)
async def post_empleados(empleados: Empleados):
    try:
        result = await add_empleados(empleados.dict())
        return {"message": "Documento insertado con éxito", "id": str(result)}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al insertar el documento: {e}"
        )

@empleados.put("/empleados/")
async def update_empleados(item: Empleados):
    try:
        result = await put_empleados(item.dict())
        return {"message": "Documento actualizado con éxito", "id": str(result)}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al actualizar el documento: {e}"
        )
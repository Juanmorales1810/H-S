# routers/accidentes.py
from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel

# ----------------------------------------------------
from models.accidentes import Accidentes
# ----------------------------------------------------
from querys.accidentes import get_accidentes, add_accidentes, put_accidentes
# ----------------------------------------------------
accidentes = APIRouter()

@accidentes.get("/accidentes/", response_model=List[Accidentes])
async def fetch_accidentes():
    try:
        return await get_accidentes()
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al obtener los datos: {e}"
        )

@accidentes.post("/accidentes/", status_code=201)
async def post_accidentes(accidentes: Accidentes):
    try:
        result = await add_accidentes(accidentes.dict())
        return {"message": "Documento insertado con éxito", "id": str(result)}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al insertar el documento: {e}"
        )

@accidentes.put("/accidentes/")
async def update_accidentes(item: Accidentes):
    try:
        result = await put_accidentes(item.dict())
        return {"message": "Documento actualizado con éxito", "id": str(result)}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al actualizar el documento: {e}"
        )
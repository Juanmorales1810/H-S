# routers/cursos.py
from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel

# ----------------------------------------------------
from models.cursos import Cursos
# ----------------------------------------------------
from querys.cursos import get_cursos, add_cursos, put_cursos
# ----------------------------------------------------
cursos = APIRouter()

@cursos.get("/cursos/", response_model=List[Cursos])
async def fetch_cursos():
    try:
        return await get_cursos()
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al obtener los datos: {e}"
        )

@cursos.post("/cursos/", status_code=201)
async def post_cursos(cursos: Cursos):
    try:
        result = await add_cursos(cursos.dict())
        return {"message": "Documento insertado con éxito", "id": str(result)}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al insertar el documento: {e}"
        )

@cursos.put("/cursos/")
async def update_cursos(item: Cursos):
    try:
        result = await put_cursos(item.dict())
        return {"message": "Documento actualizado con éxito", "id": str(result)}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al actualizar el documento: {e}"
        )
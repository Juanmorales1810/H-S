# routers/profesionales.py
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse
from typing import List
from fastapi import APIRouter
from pydantic import BaseModel
# ----------------------------------------------------
from models.profesionales import Profesionales
# ----------------------------------------------------
from querys.profesionales import get_profesionales, add_profesional, put_profesional
#-----------------------------------------------------
profesionales = APIRouter()

@profesionales.get("/profesionales/", response_model=List[Profesionales])
async def fetch_profesionales():
    return await get_profesionales()

@profesionales.post("/profesionales/", status_code=201)
async def post_profesional(profesional: Profesionales):
    try:
        result = await add_profesional(profesional.dict())
        return {"message": "Documento insertado con éxito", "id": str(result)}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al insertar el documento: {e}")

@profesionales.put('/profesionales/') 
async def put_profesional(item: Profesionales):
    result = await put_profesional(item.dict())
    return {"message": "Documento actualizado con éxito", "id": str(result)}


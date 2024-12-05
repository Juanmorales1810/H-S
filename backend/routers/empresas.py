# routers/empresas.py
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse
from typing import List
from fastapi import APIRouter
from pydantic import BaseModel
# ----------------------------------------------------
from models.empresas import Empresas

# ----------------------------------------------------
from querys.empresas import get_empresas, add_empresa, put_empresa
#-----------------------------------------------------
empresas = APIRouter()

@empresas.get("/empresas/", response_model=List[Empresas])
async def fetch_empresas():
    return await get_empresas()

@empresas.post("/empresas/", status_code=201)
async def post_empresa(empresa: Empresas):
    try:
        result = await add_empresa(empresa.dict())
        return {"message": "Documento insertado con éxito", "id": str(result)}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al insertar el documento: {e}")

@empresas.put('/empresas/') 
async def update_empresa(item: Empresas):
    result = await put_empresa(item.dict())
    return {"message": "Documento actualizado con éxito", "id": str(result)}


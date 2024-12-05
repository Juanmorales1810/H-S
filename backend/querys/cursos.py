# querys/cursos.py
import json
from bson.objectid import ObjectId
from datetime import datetime
# ----------------------------------------------------
from schemas.cursos import cursoSh
from conf.motor_DB_HigieneSeguridad import database
# -----------------------------------------------------
coleccion = database.Cursos

async def get_cursos():
    cursor = coleccion.find()
    data = []
    async for document in cursor:
        data.append(cursoSh(document))  # Usar esquema para transformar
    return data
    
async def add_cursos(document: dict) -> ObjectId:
    # Inserta el documento en la colección y devuelve el ID generado
    result = await coleccion.insert_one(document)
    return result.inserted_id

async def put_cursos(document):
    filtro = {"_id": ObjectId(document['id'])}
    document.pop('id')

    set_query = {"$set": document}

    respuesta = await coleccion.update_one(filtro, set_query)

    if respuesta.modified_count == 1:
        return {"status": "success", "message": "Documento actualizado correctamente"}
    else:
        return {"status": "failed", "message": "No se actualizó el documento"}
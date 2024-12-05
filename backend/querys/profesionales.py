# querys/profesionales.py
import json
from bson.objectid import ObjectId
from datetime import datetime
# ----------------------------------------------------
from schemas.profesionales import profesionalSh
from conf.motor_DB_HigieneSeguridad import database
# -----------------------------------------------------
coleccion = database.Profesionales

async def get_profesionales():
    cursor = coleccion.find()
    data = []
    async for document in cursor:
        data.append(profesionalSh(document))  # Usar esquema para transformar
    return data
    
async def add_profesional(document: dict) -> ObjectId:
    # Inserta el documento en la colección y devuelve el ID generado
    result = await coleccion.insert_one(document)
    return result.inserted_id

async def put_profesional(document):
    objecto = document
    filtro = {"_id": ObjectId(document['id'])}
    print(objecto)
    document.pop('id')

    set_query = {"$set": document}

    respuesta = await coleccion.update_one(filtro, set_query)

    if respuesta.modified_count == 1:
        return {"status": "success", "message": "Documento actualizado correctamente"}
    else:
        return {"status": "failed", "message": "No se actualizó el documento"}
    # return {"message": "Prueba"}

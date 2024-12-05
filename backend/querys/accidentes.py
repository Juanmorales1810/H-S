# querys/accidentes.py
import json
from bson.objectid import ObjectId
from datetime import datetime
# ----------------------------------------------------
from schemas.accidentes import accidentesSh
from conf.motor_DB_HigieneSeguridad import database
# -----------------------------------------------------
coleccion = database.Accidentes

async def get_accidentes():
    cursor = coleccion.find()
    data = []
    async for document in cursor:
        data.append(accidentesSh(document))  # Usar esquema para transformar
    return data
    
async def add_accidentes(document: dict) -> ObjectId:
    # Inserta el documento en la colección y devuelve el ID generado
    result = await coleccion.insert_one(document)
    return result.inserted_id

async def put_accidentes(document):
    filtro = {"_id": ObjectId(document['id'])}
    document.pop('id')

    set_query = {"$set": document}

    respuesta = await coleccion.update_one(filtro, set_query)

    if respuesta.modified_count == 1:
        return {"status": "success", "message": "Documento actualizado correctamente"}
    else:
        return {"status": "failed", "message": "No se actualizó el documento"}
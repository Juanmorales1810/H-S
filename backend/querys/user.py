from conf.motor_DB_HigieneSeguridad import database
from bson.objectid import ObjectId
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import timedelta
from fastapi import HTTPException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
users_collection = database.Users

SECRET_KEY = "secreto"
ALGORITHM = "HS256"

async def create_user_service(user_data: dict):
    try:
        # Validar campos requeridos
        if not user_data.get("correo") or not user_data.get("password") or not user_data.get("repeatepassword"):
            return {"status": 400, "detail": "Faltan campos requeridos"}

        # Validar contraseñas
        if user_data["password"] != user_data["repeatepassword"]:
            return {"status": 400, "detail": "Las contraseñas no coinciden"}

        # Validar si el correo ya existe
        existing_user = await users_collection.find_one({"correo": user_data["correo"]})
        if existing_user:
            return {"status": 400, "detail": "El correo ya está registrado"}

        # Hashear la contraseña
        hashed_password = pwd_context.hash(user_data["password"])
        user_data["password"] = hashed_password
        del user_data["repeatepassword"]  # Eliminar el campo innecesario

        # Insertar usuario en la base de datos
        result = await users_collection.insert_one(user_data)

        # Generar JWT
        user_data["id"] = str(result.inserted_id)
        del user_data["password"]  # No incluir la contraseña en el token
        token = jwt.encode({"data": user_data}, SECRET_KEY, algorithm=ALGORITHM)

        return {
            "status": 201,
            "message": "Usuario creado con éxito",
            "data": user_data,
            "token": token,
        }

    except Exception as e:
        return {"status": 500, "detail": f"Error interno: {e}"}
    
async def login_user_service(correo: str, password: str):
    try:
        # Validar que los campos no estén vacíos
        if not correo or not password:
            raise HTTPException(status_code=400, detail="Faltan campos requeridos")

        # Buscar el usuario por correo
        user = await users_collection.find_one({"correo": correo})
        if not user:
            raise HTTPException(status_code=400, detail="Usuario no encontrado")

        # Validar la contraseña
        if not pwd_context.verify(password, user["password"]):
            raise HTTPException(status_code=400, detail="Contraseña incorrecta")

        # Crear el JWT
        user_data = {key: user[key] for key in user if key != "password"}
        token = jwt.encode({"data": user_data}, SECRET_KEY, algorithm=ALGORITHM)

        return {
            "userLogged": user_data,
            "token": token,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {e}")

async def check_token_service(token: str):
    try:
        # Validar que el token exista
        if not token:
            raise HTTPException(status_code=400, detail="No autorizado. Falta token.")

        # Decodificar y verificar el token
        try:
            is_token_valid = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_data = is_token_valid.get("data")

            if not user_data or not user_data.get("_id"):
                raise HTTPException(status_code=400, detail="Token inválido.")

            # Buscar usuario en la base de datos
            user = await users_collection.find_one({"_id": user_data["_id"]})
            if not user:
                raise HTTPException(status_code=400, detail="Usuario no encontrado.")

            return {"isAuthorized": True, "message": "Usuario autorizado"}
        except JWTError:
            raise HTTPException(status_code=400, detail="Token no válido o expirado.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {e}")
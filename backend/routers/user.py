from fastapi import APIRouter, HTTPException, Response, Header
from models.user import User
from querys.user import create_user_service
from querys.user import login_user_service
from querys.user import check_token_service
from pydantic import BaseModel


user = APIRouter()

class LoginUser(BaseModel):
    correo: str
    password: str


@user.post("/register/")
async def create_user(user: User, response: Response):
    service_result = await create_user_service(user.dict())
    
    # Manejo de errores
    if service_result["status"] >= 400:
        raise HTTPException(status_code=service_result["status"], detail=service_result["detail"])
    
    # Configurar cookie con el token
    response.set_cookie(
        key="auth_cookie",
        value=service_result["token"],
        secure=False,  # Cambiar a True en producción
        httponly=True,
        max_age=86400,
        path="/",
    )
    return {"message": service_result["message"], "newUser": service_result["data"]}

@user.post("/login/")
async def login_user(user: LoginUser, response: Response):
    try:
        result = await login_user_service(user.correo, user.password)

        # Configurar cookie con el token
        response.set_cookie(
            key="auth_cookie",
            value=result["token"],
            secure=False,  # Cambiar a True en producción
            httponly=True,
            max_age=86400,
            path="/",
        )
        return {
            "message": "Inicio de sesión exitoso",
            "userLogged": result["userLogged"],
        }
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    
@user.get("/check/")
async def check_token(token: str = Header(None)):
    try:
        # Llamar a la función del servicio para verificar el token
        result = await check_token_service(token)
        return result
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
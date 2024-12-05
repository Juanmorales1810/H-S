from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.profesionales import profesionales
from routers.empresas import empresas
from routers.cursos import cursos
from routers.empleados import empleados
from routers.accidentes import accidentes
app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:5173",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(profesionales, tags=["Profesionales"])
app.include_router(empresas, tags=["Empresas"])
app.include_router(cursos, tags=["Cursos"])
app.include_router(empleados, tags=["Empleados"])
app.include_router(accidentes, tags=["Accidentes"])

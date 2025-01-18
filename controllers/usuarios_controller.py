from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services.usuarios_service import adicionar_usuario, obter_usuarios
from pydantic import BaseModel

class UsuarioSchema(BaseModel):
    nome: str
    email: str

usuario_router = APIRouter()

@usuario_router.post("/")
def criar_usuario(usuario: UsuarioSchema, db: Session = Depends(get_db)):
    return adicionar_usuario(db, usuario.nome, usuario.email)

@usuario_router.get("/")
def listar_usuarios(db: Session = Depends(get_db)):
    return obter_usuarios(db)

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services.tarefa_service import adicionar_tarefa, obter_tarefas
from pydantic import BaseModel

class TarefaSchema(BaseModel):
    titulo: str
    descricao: str
    usuario_id: int

class FiltroTarefaSchema(BaseModel):
    status: str = None

tarefa_router = APIRouter()

@tarefa_router.post("/")
def criar_tarefa(tarefa: TarefaSchema, db: Session = Depends(get_db)):
    return adicionar_tarefa(db, tarefa.titulo, tarefa.descricao, tarefa.usuario_id)

@tarefa_router.get("/")
def listar_tarefas(filtro: FiltroTarefaSchema = Depends(), db: Session = Depends(get_db)):
    return obter_tarefas(db, filtro.status)
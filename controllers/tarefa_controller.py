from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services.tarefa_service import adicionar_tarefa, obter_tarefas
from schemas.tarefa import TarefaCreate, TarefaResponse

router = APIRouter()

@router.post("/criar-tarefa/", response_model=TarefaResponse)
def criar_tarefa_endpoint(tarefa: TarefaCreate, db: Session = Depends(get_db)):
    try:
        return adicionar_tarefa(
            db=db,
            titulo=tarefa.titulo,
            descricao=tarefa.descricao,
            status=tarefa.status,
            usuario_nome=tarefa.usuario_nome,
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/listar-tarefas/", response_model=list[TarefaResponse])
def listar_tarefas_endpoint(db: Session = Depends(get_db)):
    return obter_tarefas(db=db)

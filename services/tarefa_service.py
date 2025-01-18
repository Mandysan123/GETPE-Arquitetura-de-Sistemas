from sqlalchemy.orm import Session
from dao.tarefa_dao import criar_tarefa, listar_tarefas

def adicionar_tarefa(db: Session, titulo: str, descricao: str, usuario_id: int):
    return criar_tarefa(db, titulo, descricao, usuario_id)

def obter_tarefas(db: Session, status: str = None):
    return listar_tarefas(db, status)
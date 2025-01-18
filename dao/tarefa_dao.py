from sqlalchemy.orm import Session
from models.tarefa import Tarefa

def criar_tarefa(db: Session, titulo: str, descricao: str, usuario_id: int):
    nova_tarefa = Tarefa(titulo=titulo, descricao=descricao, usuario_id=usuario_id)
    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)
    return nova_tarefa

def listar_tarefas(db: Session, status: str = None):
    if status:
        return db.query(Tarefa).filter(Tarefa.status == status).all()
    return db.query(Tarefa).all()
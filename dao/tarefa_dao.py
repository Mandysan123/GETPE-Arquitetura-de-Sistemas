from sqlalchemy.orm import Session
from models.tarefa import Tarefa

def criar_tarefa(db: Session, tarefa: Tarefa):
    db.add(tarefa)
    db.commit()
    db.refresh(tarefa)
    return tarefa

def listar_tarefas(db: Session):
    return db.query(Tarefa).all()

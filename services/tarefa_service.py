from sqlalchemy.orm import Session
from dao.tarefa_dao import criar_tarefa, listar_tarefas
from models.tarefa import Tarefa
from dao.usuario_dao import listar_usuarios

def adicionar_tarefa(db: Session, titulo: str, descricao: str, status: bool, usuario_nome: str):
    # Verificar se o usuário existe
    usuarios = listar_usuarios(db)
    if not any(usuario.nome == usuario_nome for usuario in usuarios):
        raise ValueError("Usuário não encontrado")

    nova_tarefa = Tarefa(
        titulo=titulo,
        descricao=f"{descricao} - Status: {'Pendente' if status else 'Concluída'}",
        status=status,
        usuario_nome=usuario_nome,
    )
    return criar_tarefa(db, nova_tarefa)

def obter_tarefas(db: Session):
    return listar_tarefas(db)


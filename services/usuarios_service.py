from sqlalchemy.orm import Session
from dao.usuario_dao import criar_usuario, listar_usuarios, excluir_usuario_por_email
from models.usuarios import Usuario


def adicionar_usuario(db: Session, nome: str, email: str):
    novo_usuario = Usuario(nome=nome, email=email)
    return criar_usuario(db, novo_usuario)

def obter_usuarios(db: Session):
    return listar_usuarios(db)

def remover_usuario_por_email(db: Session, email: str):
    return excluir_usuario_por_email(db, email)


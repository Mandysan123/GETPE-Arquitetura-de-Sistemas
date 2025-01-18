from sqlalchemy.orm import Session
from dao.usuario_dao import criar_usuario, listar_usuarios

def adicionar_usuario(db: Session, nome: str, email: str):
    return criar_usuario(db, nome, email)

def obter_usuarios(db: Session):
    return listar_usuarios(db)

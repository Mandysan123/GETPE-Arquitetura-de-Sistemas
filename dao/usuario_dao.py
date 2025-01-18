from sqlalchemy.orm import Session
from models.usuarios import Usuario

def criar_usuario(db: Session, nome: str, email: str):
    novo_usuario = Usuario(nome=nome, email=email)
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

def listar_usuarios(db: Session):
    return db.query(Usuario).all()
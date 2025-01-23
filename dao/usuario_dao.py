from sqlalchemy.orm import Session
from models.usuarios import Usuario

def criar_usuario(db: Session, usuario: Usuario):
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

def listar_usuarios(db: Session):
    return db.query(Usuario).all()

def excluir_usuario_por_email(db: Session, email: str):
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if usuario:
        db.delete(usuario)
        db.commit()
        return True
    return False
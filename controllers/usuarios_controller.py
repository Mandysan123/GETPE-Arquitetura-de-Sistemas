from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services.usuarios_service import adicionar_usuario, obter_usuarios, remover_usuario_por_email
from schemas.usuario import UsuarioCreate, UsuarioResponse

router = APIRouter()

@router.post("/criar-usuario/", response_model=UsuarioResponse)
def criar_usuario_endpoint(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return adicionar_usuario(db=db, nome=usuario.nome, email=usuario.email)

@router.get("/listar-usuarios/", response_model=list[UsuarioResponse])
def listar_usuarios_endpoint(db: Session = Depends(get_db)):
    return obter_usuarios(db=db)

@router.delete("/{email}")
def deletar_usuario_endpoint(email: str, db: Session = Depends(get_db)):
    sucesso = remover_usuario_por_email(db, email)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"detail": "Usuário excluído com sucesso"}
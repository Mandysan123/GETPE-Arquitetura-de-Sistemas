from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Tarefa(Base):
    __tablename__ = "tarefa"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descricao = Column(String)
    status = Column(Boolean, default=True)  # True para Pendente, False para Concluída
    usuario_nome = Column(String)  # Nome do usuário relacionado à tarefa

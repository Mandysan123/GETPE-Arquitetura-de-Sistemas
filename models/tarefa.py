from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.usuarios import Base

class Tarefa(Base):
    __tablename__ = "tarefas"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descricao = Column(String)
    status = Column(String, default="Pendente")
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    usuario = relationship("Usuario")
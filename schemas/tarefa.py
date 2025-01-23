from pydantic import BaseModel

class TarefaBase(BaseModel):
    titulo: str
    descricao: str
    status: bool
    usuario_nome: str 

class TarefaCreate(TarefaBase):
    pass

class TarefaResponse(TarefaBase):
    id: int

    class Config:
        orm_mode = True
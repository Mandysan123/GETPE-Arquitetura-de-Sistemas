# main.py
from fastapi import FastAPI
from controllers.usuarios_controller import router as usuario_router
from controllers.tarefa_controller import router as tarefa_router
from models.usuarios import Base as UsuarioBase
from models.tarefa import Base as TarefaBase
from database import engine

# Criar as tabelas no banco de dados
UsuarioBase.metadata.create_all(bind=engine)
TarefaBase.metadata.create_all(bind=engine)

app = FastAPI()

# Registrar os routers com prefixos mais concisos
app.include_router(usuario_router, prefix="/usuarios", tags=["Usuários"])
app.include_router(tarefa_router, prefix="/tarefas", tags=["Tarefas"])


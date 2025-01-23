# Sistema de Gestão de Tarefas para Equipes 🚀

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![FastApi](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white)
![Sqlite](https://img.shields.io/badge/Sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

Este é um sistema simples para gestão de tarefas entre equipes, desenvolvido em Python utilizando o framework **FastAPI** e o banco de dados **SQLite**. O objetivo é facilitar o cadastro, gerenciamento e acompanhamento das tarefas atribuídas a diferentes membros da equipe.

## Funcionalidades Principais ✅

1. **Gerenciamento de Usuários:**
   - 👤 Cadastro de usuários com nome e email.
   - 📋 Listagem de usuários cadastrados.
   - ❌ Exclusão de usuários pelo email.

2. **Gerenciamento de Tarefas:**
   - 📝 Cadastro de tarefas com os seguintes campos:
     - 🏷️ Título da tarefa.
     - ✏️ Descrição da tarefa.
     - 🔄 Status da tarefa (Pendente ou Concluída).
     - 👥 Usuário responsável pela tarefa (identificado pelo nome).
   - 📋 Listagem de todas as tarefas cadastradas.

## Estrutura do Projeto 🗂️

O projeto foi estruturado utilizando padrões de projeto para garantir modularidade e manutenibilidade. A organização segue o seguinte formato:

```plaintext
project_name/
├── models/                 # Definição dos modelos de dados
│   ├── usuario.py          # Modelo de usuário
│   ├── tarefa.py           # Modelo de tarefa
├── dao/                    # Data Access Object (DAO) para manipulação de dados
│   ├── usuario_dao.py      # Operações de banco de dados para usuários
│   ├── tarefa_dao.py       # Operações de banco de dados para tarefas
├── services/               # Regras de negócio
│   ├── usuario_service.py  # Lógica de negócios para usuários
│   ├── tarefa_service.py   # Lógica de negócios para tarefas
├── controllers/            # Endpoints da API
│   ├── usuario_controller.py  # Rotas para gerenciamento de usuários
│   ├── tarefa_controller.py   # Rotas para gerenciamento de tarefas
├── tests/                  # Testes da aplicação
│   ├── postman_collection.json # Coleção Postman para testar os endpoints
├── main.py                 # Inicialização do servidor FastAPI
├── README.md               # Documentação do projeto
├── .gitignore              # Arquivos e diretórios ignorados pelo Git
├── app.db                  # Banco de dados SQLite gerado automaticamente
```

## Padrões de Projeto Utilizados 🛠️

1. **Model-View-Controller (MVC):**
   - Os modelos estão na pasta `models/`.
   - Os controladores (responsáveis pelas rotas da API) estão em `controllers/`.
   - As regras de negócio estão isoladas nos serviços em `services/`.

2. **DAO (Data Access Object):**
   - Todos os acessos ao banco de dados são realizados através de objetos DAO, localizados na pasta `dao/`.

3. **Service Layer:**
   - A lógica de negócios foi separada em serviços específicos localizados na pasta `services/`. Isso garante que as regras de negócio fiquem desacopladas dos controladores.

4. **SQLAlchemy:**
   - Utilizado como ORM para mapeamento e manipulação dos modelos e tabelas do banco de dados SQLite.

5. **FastAPI:**
   - Framework utilizado para criar a API de maneira rápida, simples e com suporte integrado a documentação interativa via Swagger e Redoc.

## Como Executar o Projeto ▶️

### Pré-requisitos 🛑

- Python 3.10 ou superior 🐍
- Gerenciador de pacotes `pip` 📦

### Instalação 🛠️

1. Clone o repositório:
   ```bash
   git clone https://github.com/Mandysan123/GETPE-Arquitetura-de-Sistemas.git
   cd project_name
   ```

3. Instale as dependências:
   ```bash
   pip install fastapi sqlalchemy uvicorn
   ```

4. Execute as migrações para criar o banco de dados:
   ```bash
   python main.py
   ```

5. Inicie o servidor FastAPI:
   ```bash
   uvicorn main:app --reload
   ```

6. Acesse a documentação interativa da API no navegador em:
   - [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Testando com o Postman 📬

Uma coleção Postman foi incluída no projeto (localizada em `tests/postman_collection.json`) para facilitar o teste dos endpoints. Importe-a no Postman e use as requisições configuradas para interagir com o sistema.

---

Se tiver dúvidas ou sugestões, fique à vontade para contribuir! 😊

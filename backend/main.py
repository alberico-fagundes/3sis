import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Field, Session, SQLModel, create_engine, select

# 1. O MOLDE DA TABELA (Como o aluno é salvo)
class Aluno(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str

# 2. A CHAVE DO COFRE (O Banco SQLite)
# O SQLite cria um arquivo local chamado 'banco_local.db' sozinho!
DATABASE_URL = "sqlite:///banco_local.db"

# connect_args={"check_same_thread": False} é uma exigência do FastAPI para o SQLite não travar
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# 3. O START DO RESTAURANTE (Gera o banco de dados ao ligar a API)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Cria o arquivo banco_local.db e a tabela Aluno
    SQLModel.metadata.create_all(engine) 
    
    # Semente: Se o banco estiver vazio, cria o João Zezinho
    with Session(engine) as session:
        if not session.exec(select(Aluno)).first():
            session.add(Aluno(nome="João Zezinho"))
            session.commit()
    yield

# 4. A API
app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:5174",
    "http://127.0.0.1:5174",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 5. A NOSSA PRIMEIRA ROTA
@app.get("/alunos")
def ler_alunos():
    # Vai no banco e busca todo mundo
    with Session(engine) as session:
        return session.exec(select(Aluno)).all()
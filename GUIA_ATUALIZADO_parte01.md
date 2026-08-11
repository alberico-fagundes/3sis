# Engenharia de Software | SaaS Smart Project

> **🎯 OBJETIVO DIRETO:** Ligar o coração do seu sistema (Backend Python) de forma instantânea. Sem instalar bancos de dados pesados, sem Docker. Usaremos a mágica do **SQLite**. E no final, um "Guia de Bolso" de Git para você nunca mais perder código antes de enviar para a nuvem.  
---

## 🛡️ 1. A BOLHA DE PROTEÇÃO E O ANTI-LIXO

Antes de cozinhar, colocamos o avental. No Python, isso significa criar um Ambiente Virtual (`venv`) para não sujar o seu computador, e um `.gitignore` para não enviar lixo para a nuvem.

### Passo 1.1: Criar e entrar na Bolha

Abra o terminal do VSCode na pasta do projeto e rode:

```bash
# Cria a bolha (Rode só uma vez)
python -m venv venv

# Entra na bolha (Rode SEMPRE que abrir o VSCode!)

# No Windows:
venv\Scripts\activate

# No Mac/Linux:
source venv/bin/activate
```

*(Seu terminal deve ficar com um `(venv)` verde no começo).*

### Passo 1.2: A Placa de Proibido (O `.gitignore`)

Crie um arquivo chamado **exatamente** `.gitignore` na raiz do projeto e cole isto dentro:

```
venv/
__pycache__/
*.db
.env
```

*Isso garante que o GitHub não vai travar recebendo arquivos gigantes e senhas secretas.*

---

## 📦 2. A LISTA DE COMPRAS (BIBLIOTECAS)

Com o `(venv)` ativado no terminal, baixe as ferramentas de trabalho:

```bash
pip install fastapi uvicorn sqlmodel python-dotenv
```

*Aqui instalamos o FastAPI (O Cozinheiro) e o SQLModel (A ferramenta de falar com o banco de dados).*

---

## 🧠 3. O CÓDIGO DA MAGIA (O `main.py`)

Crie o arquivo `main.py` na raiz do projeto e cole o código abaixo. Leia os comentários, eles são a aula!

```python
import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
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

# 5. A NOSSA PRIMEIRA ROTA
@app.get("/alunos")
def ler_alunos():
    # Vai no banco e busca todo mundo
    with Session(engine) as session:
        return session.exec(select(Aluno)).all()
```

---

## ⚡ 4. LIGANDO A MÁQUINA

No terminal, dê o comando para o servidor rodar:

```bash
uvicorn main:app --reload
```

Abra o seu navegador e vá para: 👉 [**http://localhost:8000/alunos**](http://localhost:8000/alunos) (Você verá o João Zezinho!) 👉 [**http://localhost:8000/docs**](http://localhost:8000/docs) (Você verá o painel interativo maravilhoso do FastAPI).

**Reparou em algo incrível?** Se você olhar na pasta do seu projeto no VSCode, verá que um arquivo novo chamado `banco_local.db` apareceu. É o seu banco de dados inteiro, seguro e sem complicação!

---

## 📖 BÔNUS: GLOSSÁRIO DE SOBREVIVÊNCIA GIT E GITHUB

*Consulte sempre que for mandar seu código para o GitHub (e futuramente para o Render).*

### O Fluxo Diário Obrigatório

Terminou de programar por hoje? Siga esta ordem:

1. `git add .` *(Coloca TODAS as alterações no palco)*  
2. `git commit -m "Fiz a rota de alunos"` *(Tira a foto e bota um nome nela)*  
3. `git push` *(Envia a foto para as nuvens do GitHub)*

### Os Comandos de Socorro (Troubleshooting)

| Se você precisa... | Use este comando | O que ele faz? |
| :---- | :---- | :---- |
| **Saber se tem arquivo que esqueci de salvar** | `git status` | Fica vermelho se algo foi alterado e não foi salvo. Fica verde se está no palco (add). |
| **Puxar o código do colega que está na nuvem** | `git pull` | Pega a versão mais nova do GitHub e funde com o seu computador. Use sempre ANTES do `git push`. |
| **Corrigir "Push Rejected" (Erro no Envio)** | `git pull` | O GitHub não deixa você enviar código antigo se alguém já atualizou. Puxe (`pull`) primeiro, depois envie (`push`). |
| **Ver o histórico de fotos que já tirei** | `git log` | Mostra todas as mensagens de commit que você já fez. Aperte 'Q' para sair da tela. |
| **Copiar um projeto inteiro da internet pro PC** | `git clone [url_do_github]` | Baixa a pasta inteira do projeto para o seu computador. |

---



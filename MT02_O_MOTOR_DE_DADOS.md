# 🚀 MT02 - O MOTOR DE DADOS (A COZINHA FASTAPI)
## Engenharia de Software ULTRA DIDÁTICA | SaaS Smart Academy Reborn

> **🎯 OBJETIVO EXTRAORDINÁRIO:** Ligar os motores do backend. O Terreno (Docker) está pronto e o Cofre (Postgres) está vazio. Hoje, vamos contratar o Chef da Cozinha (O Python/FastAPI), blindar nosso projeto contra lixo no Git, ensinar o Chef a abrir o cofre, criar a "Prateleira de Alunos" (Tabela) de forma mágica e cuspir os primeiros dados na tela.

---

## 📚 1. A HIGIENE DA COZINHA (O AMBIENTE VIRTUAL)

Antes de programar em Python, precisamos entender a **Regra de Ouro da Sobrevivência Python**: Nunca instale panelas (bibliotecas) direto na cozinha da sua casa (seu sistema operacional). 

Se você instalar pacotes direto no seu Windows/Mac, o projeto A pode exigir o FastAPI versão 1, e o projeto B pode exigir a versão 2. O seu computador vai enlouquecer e os projetos vão quebrar.

### 🛡️ A Solução: O `venv` (A Bolha Isolada)
Nós criamos uma "Bolha Invisível" dentro da pasta do projeto. Tudo que instalarmos, fica preso nessa bolha.

Abra o terminal do VSCode (atalho: `Ctrl + '` ou `Ctrl + J`) na pasta raiz do projeto (onde está o seu `docker-compose.yml`) e digite:
```bash
# Cria a bolha (só roda uma vez na vida do projeto)
python -m venv venv

# Entra na bolha (Você precisa fazer isso toda vez que abrir o VSCode!)
# Se for Windows:
venv\Scripts\activate
# Se for Mac/Linux:
source venv/bin/activate
```
**Como saber se funcionou?** O seu terminal ficará com um `(venv)` verdinho no começo da linha. Parabéns, você está de luvas e touca, pronto para cozinhar.

---

## 🛑 2. O ESCUDO ANTI-LIXO (O .GITIGNORE)

Se nós criamos a pasta `venv` (que possui quase 1 Gigabyte de arquivos ocultos do Python) e tentarmos salvar isso no GitHub, será um **Desastre Nuclear**. Vai demorar horas para carregar e o servidor vai rejeitar. Nós **nunca** enviamos a bolha para a nuvem. Nós enviamos apenas a "receita", e cada programador cria a sua própria bolha na casa dele.

Para impedir que a bolha vá para o Github, crie um arquivo na raiz do projeto chamado **EXATAMENTE** `.gitignore` (com o ponto no começo e sem extensão no final). Cole isso dentro dele:

```text
# Ignorar a bolha virtual do Python
venv/
__pycache__/

# Ignorar o disco virtual do banco de dados (se for mapeado na pasta)
pgdata/

# Ignorar arquivos secretos (senhas) no futuro
.env
```
Pronto. O "Segurança da Porta" (Git) agora está avisado para barrar qualquer tentativa de enviar essas pastas.

---

## 📦 3. A LISTA DE COMPRAS (AS BIBLIOTECAS)

O Chef Python precisa de 3 ferramentas para trabalhar hoje. Certifique-se de que o `(venv)` está verde no seu terminal e rode:

```bash
pip install fastapi uvicorn sqlmodel psycopg2-binary
```
*(Ele vai baixar tudo rapidinho da internet e trancar dentro da sua bolha).*

---

## 🧠 4. A MÁGICA EM 30 LINHAS (O ARQUIVO `main.py`)

No mundo antigo, você levaria 5 pastas e 10 arquivos para conectar no banco e fazer uma rota. Com o FastAPI + SQLModel, nós faremos o milagre em 1 arquivo.

Crie um arquivo chamado `main.py` **NA RAIZ DO PROJETO** (do lado do `docker-compose.yml` e do `.gitignore`. **NUNCA** crie dentro da pasta `venv`!).

Copie e cole a nossa obra de arte:

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select

# 1. O MOLDE (A Planta da Tabela)
class Aluno(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str

# 2. A CHAVE DO COFRE (Conexão com o Docker do MT01)
DATABASE_URL = "postgresql://admin:senha_ultra_secreta@localhost:5432/smart_academy"
engine = create_engine(DATABASE_URL)

# 3. O MOMENTO DE ABRIR O RESTAURANTE (Lifespan e Semente de Dados)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Magia 1: Cria a tabela Aluno sozinho!
    SQLModel.metadata.create_all(engine) 
    
    # Magia 2: Planta uma "Semente" (Seed) se o cofre estiver vazio.
    with Session(engine) as session:
        alunos_existentes = session.exec(select(Aluno)).all()
        if not alunos_existentes: # Se o banco tá vazio...
            aluno_cobaia = Aluno(nome="João Zezinho")
            session.add(aluno_cobaia)
            session.commit()
            
    yield # Restaurante Aberto!

# 4. INICIALIZAÇÃO DA API (O Balcão)
app = FastAPI(lifespan=lifespan)

# Libera o CORS (Para o Frontend poder pescar os dados depois)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 5. A NOSSA PRIMEIRA ROTA (O Prato do Menu)
@app.get("/alunos")
def ler_alunos():
    # Abre uma Sessão rápida no cofre e traz todos os alunos
    with Session(engine) as session:
        alunos = session.exec(select(Aluno)).all()
        return alunos
```

---

## ⚡ 5. O START (LIGANDO A MÁQUINA)

Vá ao terminal e diga ao garçom (`uvicorn`) para servir nosso aplicativo:

```bash
uvicorn main:app --reload
```
*(O `--reload` faz o servidor reiniciar sozinho sempre que você salvar o arquivo).*

Abra seu navegador e digite:
👉 **http://localhost:8000/alunos**
Se você der sorte, não verá uma tela branca. Verá: `[{"id": 1, "nome": "João Zezinho"}]`. Nosso Chef plantou a semente com sucesso!

### 🎩 O BÔNUS EXPLOSIVO (A Dopamina do Desenvolvedor)
O FastAPI tem um superpoder secreto. Ele **desenha o site inteiro de testes sozinho**.
Abra no navegador:
👉 **http://localhost:8000/docs**

Você verá o **Swagger UI**. Uma tela lindíssima com a rota `/alunos`. Clique em **"Try it out"** e depois **"Execute"**. Ver o sistema funcionando de forma visual sem ter escrito 1 linha de Frontend é magia pura.

---

## 🚨 6. A BÍBLIA DE ERROS (TROUBLESHOOTING PYTHON)

### 🐛 ERRO 1: O Pesadelo do PowerShell (Windows)
**O que aparece na tela:**
```text
venv\Scripts\activate : O arquivo não pode ser carregado porque a execução de scripts foi desabilitada neste sistema.
```
**A Causa:** O Windows vem de fábrica com uma trava de segurança paranóica que impede rodar arquivos `.ps1` (o ativador do venv).
**A Solução Enterprise:** Abra o **PowerShell como Administrador** no seu Windows (não no VSCode, procure no menu Iniciar) e rode este comando de poder absoluto:
`Set-ExecutionPolicy Unrestricted -Force`
Volte pro VSCode e ative o `venv` de novo. Vai funcionar para sempre.

### 🐛 ERRO 2: A Bolha Furada
**O que aparece na tela:**
```text
ModuleNotFoundError: No module named 'fastapi'
```
**A Causa:** Você fechou o VSCode e esqueceu de vestir o traje de proteção (ativar o `venv`). A máquina está procurando o FastAPI no Windows inteiro.
**A Solução:** Rode `venv\Scripts\activate` e tente rodar o `uvicorn` de novo.

### 🐛 ERRO 3: O Banco Dorminhoco
**O que aparece na tela:**
```text
psycopg2.OperationalError: connection to server at "localhost" (::1), port 5432 failed: Connection refused
```
**A Causa:** O FastAPI foi no cofre, mas a porta tava trancada. Você esqueceu de ligar o Docker Compose do MT01.
**A Solução:** Rode `docker compose up -d` na pasta onde está o YAML.

---

## 🎓 7. EXERCÍCIO DE ALTA PERFORMANCE (NÍVEL PLENO)

**Cenário:** O estagiário olhou para a Rota `/alunos` e decidiu retornar algo bizarro: `return {"dados_secretos": alunos, "aviso": "Olá Mundo"}`.

**Pergunta:** Por que, na linguagem universal da Web (REST), isso destrói o Frontend?

<details>
<summary>👀 Ver o Veredito do Arquiteto</summary>
<b>Quebra do Padrão de Coleções!</b><br>
O Frontend pede uma lista (<code>GET /alunos</code>) esperando receber um <b>Array puro de JSON</b>: <code>[ {aluno1}, {aluno2} ]</code>. Assim ele pode fazer um "loop" e desenhar a tabela. <br>
Se o Zezinho mandar um objeto "envelopado", o Frontend vai engasgar tentando desenhar a string "aviso" achando que é um aluno. Rotas no plural retornam listas limpas!
</details>

---

## 🏆 CHECKPOINT FINAL - CRITÉRIOS DE ACEITE

Seu Motor de Dados está roncando se:
1. [ ] O `.gitignore` foi criado na raiz e o `venv` está cinza/oculto no VSCode.
2. [ ] O `uvicorn` ligou sem erros vermelhos.
3. [ ] Você acessou `/docs` e puxou os dados do João Zezinho!

**No próximo Módulo (MT03)**, nós vamos finalmente construir a nossa **Vitrine (O Frontend React)** sem complicação, e usar o Garçom do Javascript para puxar o João Zezinho da API e pintar na tela com um visual de cair o queixo!

# 🚀 MT01 - O TERRENO DA FÁBRICA (A FUNDAÇÃO DOCKER)
## Engenharia de Software  

> **🎯 OBJETIVO EXTRAORDINÁRIO:** Acabar definitivamente com a maldição do "Na minha máquina funciona". Você vai aprender que engenheiros de elite **nunca** instalam bancos de dados diretamente no Windows ou Mac. Vamos criar o nosso "Terreno Isolado" usando Docker, garantindo que o seu ecossistema rode idêntico no seu computador, no computador do seu colega e nos servidores da Amazon.

---

## 📚 1. A SÍNDROME DO "NA MINHA MÁQUINA FUNCIONA"

### ❌ A Abordagem do Amador (A Instalação Suja)
O Zezinho decide começar um projeto. Ele entra no site do PostgreSQL, baixa um `.exe` (ou `.pkg`), avança clicando "Next, Next, Finish" e instala o banco de dados direto no sistema operacional dele. 
- **O Desastre:** O computador dele fica poluído. Se ele precisar da versão 12 para um projeto e a versão 16 para outro, tudo explode. Quando ele manda o projeto para a Maria, o código não roda, porque ela tem uma versão diferente instalada. Começa a guerra do "Mas na minha máquina estava funcionando!".

### ✅ A Abordagem Enterprise (Os Contêineres)
A revolução do comércio mundial aconteceu quando inventaram o **Contêiner de Navio**. O guindaste não precisa saber se dentro do contêiner tem carros, bananas ou televisões. Ele só pega a caixa padrão e empilha.
O **Docker** fez a mesma coisa com a programação. Ele coloca o Banco de Dados (Postgres) dentro de uma "caixa mágica" fechada, com seu próprio mini-sistema operacional. 
- Se você apagar a caixa, não sobra rastro no seu computador.
- A caixa roda 100% igual no Windows, Mac ou Linux.

---

## 🧠 2. O MAESTRO DA ORQUESTRA (DOCKER COMPOSE)

Se o Docker é o Contêiner, o **Docker Compose** é o Gerente do Porto. 
Em vez de digitarmos comandos gigantescos no terminal para subir o banco, nós escrevemos um manifesto de infraestrutura chamado `docker-compose.yml`. Esse arquivo é a "Planta Baixa" da nossa fábrica.

Quando o projeto crescer (teremos o Banco de Dados e a nossa Cozinha FastAPI), o Docker Compose vai subir os dois ao mesmo tempo e fazer eles conversarem.

---

## 🔧 3. MÃO NA MASSA: ERGUENDO O BANCO DE DADOS

Se você tem fobia de tela preta ou códigos de configuração, respire fundo. Essa é a habilidade que separa quem ganha 2 mil de quem ganha 10 mil no mercado.

### Passo 3.1: O Arquivo Planta-Baixa
Na pasta raiz do nosso projeto, abra o **VSCode** (nunca use o Bloco de Notas) e crie um arquivo chamado **exatamente** `docker-compose.yml`.
> ⚠️ **Aviso de Sobrevivência:** A linguagem YAML é extremamente sensível a espaços em branco. Não use a tecla TAB e alinhe os espaços EXATAMENTE como no código abaixo. Um espaço a mais e o seu projeto explode.

Copie e cole o código abaixo (leia as explicações para não ser um copiador cego):

```yaml
# A versão da linguagem do manifesto
version: '3.8'

# Nossos serviços (As caixas que vamos subir)
services:
  # O nome que demos para a nossa Despensa (Banco de Dados)
  db:
    # A imagem oficial que vamos baixar da Internet (Postgres versão 16)
    image: postgres:16-alpine
    # O nome do contêiner quando ele estiver rodando
    container_name: smart_project_db
    # Mapeamento de Portas (Porta da sua máquina : Porta de dentro do contêiner)
    ports:
      - "5432:5432"
    # As variáveis de ambiente (A senha do nosso cofre)
    # ⚠️ AVISO DO ARQUITETO: Hoje escrevemos a senha aqui para facilitar o aprendizado. No mundo corporativo, usaremos cofres virtuais (arquivos .env) para esconder isso.
    environment:
      - POSTGRES_USER=admin
      - POSTGRES_PASSWORD=senha_ultra_secreta
      - POSTGRES_DB=smart_project
    # Garante que os dados não sumam se você desligar o computador (Os dados ficam na pasta pgdata)
    volumes:
      - pgdata:/var/lib/postgresql/data
    # Se o computador reiniciar, o Docker liga o banco sozinho
    restart: unless-stopped

# Declaração do volume (O disco rígido virtual)
volumes:
  pgdata:
```

**🔍 Raio-X do Código:**
- `postgres:16-alpine`: Por que "alpine"? O Alpine é uma versão versão minúscula do Linux. O banco de dados vai ser muito mais rápido para baixar e ocupará menos RAM do seu computador.
- `ports: "5432:5432"`: A porta da esquerda é o "buraco na parede" do seu Windows/Mac. A porta da direita é a porta do Banco de Dados. Estamos conectando as duas.
- `volumes:`: O Docker destrói tudo ao ser desligado. O volume é como um "Pen Drive Virtual". Nós plugamos no contêiner para que, mesmo que ele seja destruído, nossos dados (alunos) continuem salvos na sua máquina.

### Passo 3.2: O Comando Mágico
Abra o seu terminal **na mesma pasta** onde você salvou o arquivo `docker-compose.yml`.
Execute a magia:

```bash
docker compose up -d
```

*(O `-d` significa 'detached'. Ele liga o banco e devolve o terminal pra você poder continuar usando, em vez de prender a sua tela com logs infinitos).*

*caso de erro de permissão use:*

```bash
sudo docker compose up -d
```

---

*Pra verificar o container use::*

```bash
docker ps
ou
sudo docker ps
```

---

## 🚨 4. A BÍBLIA DE ERROS (TROUBLESHOOTING DOCKER)

Os fracos desistem no primeiro erro vermelho. Nós debugamos.

### 🐛 ERRO 1: Porta Ocupada
**O que aparece na tela:**
```text
Error starting userland proxy: listen tcp4 0.0.0.0:5432: bind: address already in use
```
**A Causa:** Você já tem algum banco de dados instalado "sujo" no seu computador que está usando a porta 5432 (ou outro contêiner rodando).
**A Solução Enterprise:** Se você não quiser desinstalar o programa antigo, basta mudar a porta da sua máquina no arquivo `.yml`. Mude de `"5432:5432"` para `"5433:5432"`. Rode o comando de novo.

### 🐛 ERRO 2: O Motor Está Desligado
**O que aparece na tela:**
```text
error during connect: This error may indicate that the docker daemon is not running.
```
**A Causa:** Você esqueceu de abrir o aplicativo "Docker Desktop" antes de dar o comando.
**A Solução Enterprise:** Abra o Docker Desktop no seu Windows/Mac. Espere o ícone ficar verde (Running) e tente novamente.

---

## 🎓 5. EXERCÍCIO DE ALTA PERFORMANCE (NÍVEL PLENO)

**Cenário:** O estagiário rodou o `docker compose up -d`. O banco subiu perfeito. Ele desligou o computador e, no dia seguinte, percebeu que precisava de dois bancos de dados para dois projetos diferentes rodando ao mesmo tempo (o `smart_project_db` e o `petshop_db`). Ambos usam o Postgres padrão.

**Pergunta:** Se ele tentar subir os dois Docker Compose ao mesmo tempo, o que vai acontecer e como ele resolve isso arquiteturalmente?

<details>
<summary>👀 Ver o Veredito do Arquiteto</summary>
<b>Vai dar Conflito de Porta (Erro 1 da nossa Bíblia)!</b><br>
O contêiner do projeto  vai grudar na porta "5432" do computador físico (Windows/Mac). Quando o projeto Petshop tentar ligar, ele vai tentar usar a mesma porta 5432 e vai explodir. <br>
<b>A Resolução:</b> O estagiário vai no <code>docker-compose.yml</code> do Petshop e muda a porta para <code>"5433:5432"</code>. Dessa forma, o Petshop responde pela 5433, o projeto responde pela 5432, e dentro da "caixa" (lado direito dos dois pontos), cada Postgres acha que está reinando sozinho na porta original dele. Magia dos Contêineres!
</details>

---

## 🏆 CHECKPOINT FINAL - CRITÉRIOS DE ACEITE

Seu Terreno está pronto se:
1. [ ] Você tem o arquivo `docker-compose.yml` criado (no VSCode, respeitando os espaços).
2. [ ] Você executou `docker compose up -d` e não houve mensagens vermelhas.
3. [ ] Se você digitar `docker ps`, verá o `smart_project_db` listado como `Up`.
4. [ ] 🌟 **(Bônus do Arquiteto):** Baixe um programa chamado **DBeaver**, conecte no endereço `localhost`, porta `5432`, com usuário `admin` e a senha `senha_ultra_secreta`. Você verá o seu cofre vazio de forma visual. É uma sensação mágica!

**No próximo Módulo (MT02)**, o nosso Chef Python vai entrar na Cozinha (FastAPI) e vamos conectar o backend a essa despensa maravilhosa que acabamos de criar. Vamos gerar os primeiros dados da Tabela Alunos!

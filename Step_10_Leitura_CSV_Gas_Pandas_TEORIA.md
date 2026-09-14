# 🐍 Passo 10: Leitura de Dados do Sensor com Python e Pandas

Iniciamos a construção da nossa **UTI de Dados em Python**. Neste passo, você vai ler o arquivo de dados brutos do sensor de gás (`dados_gas.csv`) e inspecionar suas primeiras estatísticas usando a biblioteca **Pandas**.

### 📌 O Conceito (Teoria Profunda)
Em ambientes industriais, sensores de IOT gravam medições contínuas em arquivos texto de formato livre ou tabelas delimitadas por vírgula (`.csv`). A biblioteca **Pandas** é a ferramenta padrão no ecossistema Python para carregar, manipular e inspecionar essas tabelas através da estrutura de dados chamada **DataFrame**.

### 📖 Sintaxe Básica (Exemplos Análogos)

**Como ler e inspecionar um arquivo CSV em Python com Pandas:**
```python
import pandas as pd

# 1. Carrega o arquivo CSV para um DataFrame
df = pd.read_csv("caminho/do/arquivo.csv")

# 2. Exibe as 5 primeiras linhas da tabela
print(df.head())

# 3. Exibe o resumo estrutural (colunas e tipos de dados)
print(df.info())

# 4. Exibe o resumo estatístico (média, mínimo, máximo)
print(df.describe())
```

---
---
### 💻 Mão na Massa (Desafio Ativo)

**Sua Tarefa Prática:**

1. **Crie a pasta da UTI de Dados:**
   Na raiz do projeto (`template_3sis`), crie uma nova pasta chamada `uti_dados_python` e entre nela.

2. **Instale a biblioteca Pandas:**
   No terminal da pasta `uti_dados_python`, execute:
   `pip install pandas`

3. **Crie o arquivo de dados simulados `dados_gas.csv`:**
   Dentro da pasta `uti_dados_python`, crie o arquivo `dados_gas.csv` com o seguinte conteúdo:
   ```csv
   id,data_hora,sensor_id,ppm_gas
   1,2026-09-08 08:00:00,GAS-01,12.4
   2,2026-09-08 08:05:00,GAS-01,15.1
   3,2026-09-08 08:10:00,GAS-01,18.0
   4,2026-09-08 08:15:00,GAS-01,58.6
   5,2026-09-08 08:20:00,GAS-01,62.3
   6,2026-09-08 08:25:00,GAS-01,14.2
   ```

4. **Crie o script `leitor_gas.py`:**
   Crie o arquivo `leitor_gas.py` e insira o código:
   ```python
   import pandas as pd

   print("🏭 --- UTI DE DADOS SMART FACTORY ---")
   df = pd.read_csv("dados_gas.csv")

   print("\n📋 5 Primeiras Leituras:")
   print(df.head())

   print("\n📊 Resumo Estatístico do Gás (PPM):")
   print(df["ppm_gas"].describe())
   ```

**Teste:** No terminal da pasta `uti_dados_python`, execute `python leitor_gas.py`. Você verá o resumo estatístico com a média, o valor mínimo e o pico de gás exibidos no terminal!

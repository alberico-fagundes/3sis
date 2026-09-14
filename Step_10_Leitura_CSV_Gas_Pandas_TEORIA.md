# 🐍 Passo 10: Leitura de Dados do Sensor com Python e Pandas

Iniciamos a construção da nossa **UTI de Dados em Python**. Neste passo, você vai preparar seu ambiente de execução, ler o arquivo de dados brutos do sensor de gás (`dados_gas.csv`) e inspecionar suas primeiras métricas estatísticas usando a biblioteca **Pandas**.

---

### 📌 O Conceito (Teoria Profunda)

Em ambientes industriais (Smart Factory), sensores de IoT gravam medições contínuas em arquivos texto delimitados por vírgula (`.csv`). 

A biblioteca **Pandas** é o padrão da indústria para carregar, limpar, manipular e inspecionar essas tabelas por meio de uma estrutura de dados de alto desempenho chamada **DataFrame** (semelhante a uma planilha em memória).

```
   [ Sensor de Gás IoT ]  ──> Grava no Disco ──> [ dados_gas.csv ]
                                                        │
                                                        ▼
                                                [ pd.read_csv() ]
                                                        │
                                                        ▼
                                             [ DataFrame (Pandas) ]
                                          ├── Inspecionar Linhas (.head())
                                          └── Resumo Estatístico (.describe())
```

---

### 📖 Sintaxe Básica (Exemplos Análogos)

**Como ler e inspecionar um arquivo CSV em Python com Pandas:**
```python
import pandas as pd

# 1. Carrega o arquivo CSV para um DataFrame
df = pd.read_csv("caminho/do/arquivo.csv")

# 2. Exibe as 5 primeiras linhas da tabela
print(df.head())

# 3. Exibe o resumo estrutural (colunas, tipos e contagem)
print(df.info())

# 4. Exibe o resumo estatístico (média, desvio padrão, min, max)
print(df.describe())
```

---
---

### 💻 Mão na Massa (Desafio Ativo - PBL)

#### 🎯 **O Problema Real:**
O time de operação da fábrica precisa de um script que processe rapidamente a telemetria do sensor de gás `GAS-01` e informe:
1. Uma prévia das leituras recentes.
2. O pico máximo de emissão em PPM para avaliar se os limites de segurança foram ultrapassados.

---

#### 🛠️ **Etapa 1: Diagnóstico de Ferramentas (Checagem)**

Antes de instalar dependências, verifique se o Python e o gerenciador de pacotes (`pip`) estão disponíveis no seu terminal:

```bash
# Verificar versão do Python:
python3 --version  # ou: python --version

# Verificar versão do Pip:
pip3 --version     # ou: pip --version
```

> [!TIP]
> Se o comando retornar a versão (ex: `Python 3.10.x` ou superior), seu interpretador está pronto. Caso não retorne nada, consulte a seção **"🆘 Guia de Resolução e Alternativas"** no final deste documento.

---

#### 📁 **Etapa 2: Estrutura de Pastas e Ambiente Isolado (Venv)**

1. Na raiz do seu repositório, crie a pasta da **UTI de Dados** e entre nela:
   ```bash
   mkdir -p uti_dados_python
   cd uti_dados_python
   ```

2. **Crie e Ative o Ambiente Virtual (`venv`):**
   *Por que usar venv?* Para isolar as bibliotecas do projeto e evitar o erro de `externally-managed-environment` dos sistemas operacionais modernos.

   - **No Linux / macOS:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

   - **No Windows (PowerShell):**
     ```powershell
     python -m venv .venv
     .venv\Scripts\Activate.ps1
     ```
     *(Se o terminal exibir `(.venv)` no início da linha, o ambiente virtual está ativo com sucesso!)*

3. **Instale a biblioteca Pandas dentro do ambiente virtual:**
   ```bash
   pip install pandas
   ```

---

#### 📄 **Etapa 3: Criar o Arquivo de Telemetria (`dados_gas.csv`)**

Dentro da pasta `uti_dados_python`, crie o arquivo `dados_gas.csv` com as leituras simuladas do sensor:

```csv
id,data_hora,sensor_id,ppm_gas
1,2026-09-08 08:00:00,GAS-01,12.4
2,2026-09-08 08:05:00,GAS-01,15.1
3,2026-09-08 08:10:00,GAS-01,18.0
4,2026-09-08 08:15:00,GAS-01,58.6
5,2026-09-08 08:20:00,GAS-01,62.3
6,2026-09-08 08:25:00,GAS-01,14.2
```

---

#### 🧪 **Etapa 4: Criar e Executar o Script `leitor_gas.py`**

Crie o arquivo `leitor_gas.py` com o seguinte código:

```python
import pandas as pd

print("🏭 ===========================================")
print("     UTI DE DADOS - MONITORAMENTO INDUSTRIAL  ")
print("===========================================\n")

# 1. Leitura do arquivo CSV
df = pd.read_csv("dados_gas.csv")

# 2. Exibição das primeiras leituras
print("📋 [1/2] Primeiras Leituras Coletadas:")
print(df.head())
print("-" * 45)

# 3. Análise estatística da coluna ppm_gas
print("\n📊 [2/2] Resumo Estatístico do Gás (PPM):")
print(df["ppm_gas"].describe())
print("-" * 45)

# 4. Alerta de Segurança Operacional
pico_gas = df["ppm_gas"].max()
print(f"\n⚠️  Pico Máximo Registrado: {pico_gas} PPM")
if pico_gas > 50.0:
    print("🚨 ALERTA: Concentração acima do limite seguro tolerado (50 PPM)!")
else:
    print("✅ Operação dentro dos níveis normais de segurança.")
```

---

#### 🚀 **Etapa 5: Teste e Validação**

No terminal (com o ambiente `(.venv)` ativado), execute:

```bash
python leitor_gas.py
```

**Saída esperada no terminal:**
```text
🏭 ===========================================
     UTI DE DADOS - MONITORAMENTO INDUSTRIAL  
===========================================

📋 [1/2] Primeiras Leituras Coletadas:
   id            data_hora sensor_id  ppm_gas
0   1  2026-09-08 08:00:00    GAS-01     12.4
1   2  2026-09-08 08:05:00    GAS-01     15.1
2   3  2026-09-08 08:10:00    GAS-01     18.0
3   4  2026-09-08 08:15:00    GAS-01     58.6
4   5  2026-09-08 08:20:00    GAS-01     62.3
---------------------------------------------

📊 [2/2] Resumo Estatístico do Gás (PPM):
count     6.000000
mean     30.100000
std      23.473559
min      12.400000
25%      14.425000
50%      16.550000
75%      48.450000
max      62.300000
Name: ppm_gas, dtype: float64
---------------------------------------------

⚠️  Pico Máximo Registrado: 62.3 PPM
🚨 ALERTA: Concentração acima do limite seguro tolerado (50 PPM)!
```

---

#### 🧠 **Entendendo as Métricas: O que significa cada linha do `describe()`?**

Ao analisar dados de sensores com a UTI de Dados, cada indicador estatístico tem um significado operacional direto:

| Métrica | Valor Obtido | O que significa na prática? (Interpretação Industrial) |
| :--- | :--- | :--- |
| **`count`** *(Contagem)* | `6.0` | **Total de leituras válidas:** Foram registradas 6 coletas de dados no arquivo CSV. |
| **`mean`** *(Média)* | `30.1 PPM` | **Média aritmética:** Somatório das leituras dividido por 6. Representa a média global do período. |
| **`std`** *(Desvio Padrão)* | `23.47` | **Dispersão / Variabilidade:** Um valor alto indica que o gás oscilou violentamente (momentos de 12 PPM e saltos para 62 PPM). |
| **`min`** *(Mínimo)* | `12.4 PPM` | **Menor valor registrado:** Nível base de gás no ambiente (ar mais puro). |
| **`25%`** *(1º Quartil)* | `14.42 PPM` | **25% das medições** ficaram abaixo deste valor (períodos de baixa emissão). |
| **`50%`** *(Mediana / 2º Quartil)* | `16.55 PPM` | **Valor central exato:** Metade das leituras foi menor que 16.55 e metade foi maior. *(Observe como a média de 30.1 foi puxada para cima pelos picos, enquanto a maior parte do tempo o gás esteve em torno de 16 PPM!)* |
| **`75%`** *(3º Quartil)* | `48.45 PPM` | **75% das medições** ficaram abaixo deste valor (início da zona crítica). |
| **`max`** *(Máximo / Pico)* | `62.3 PPM` | **Pico máximo de emissão:** Valor crítico para a segurança do operador. Como superou 50 PPM, disparou o alarme! |

* **`Name: ppm_gas`**: Nome da coluna analisada.
* **`dtype: float64`**: Tipo numérico decimal com precisão dupla (ponto flutuante de 64 bits).

---

### 🆘 Guia de Resolução de Problemas (Troubleshooting Sem Acesso Admin)

Se você estiver em um computador de laboratório sem privilégios de administrador (`sudo` ou permissões de instalação do Windows), utilize as alternativas abaixo:

#### 1. Erro: `externally-managed-environment`
* **Causa:** O Linux protege os pacotes do sistema (PEP 668).
* **Solução:** Crie o ambiente virtual com `python3 -m venv .venv` e ative-o com `source .venv/bin/activate` antes do `pip install`.

#### 2. Erro no Linux: `The virtual environment was not created successfully because ensurepip is not available`
Se a máquina não possuir o pacote `python3-venv` instalado e você **não tiver senha de `sudo`**, use o modo usuário local:
```bash
pip install --user --break-system-packages pandas
```

#### 3. Máquina sem Python instalado e sem acesso de Administrador:
* **No Windows:** Baixe o instalador no [python.org](https://www.python.org/downloads/) e escolha a opção **"Install just for me"** (instalação local no usuário, sem pedir permissão de administrador).
* **No Linux:** Você pode instalar o **Miniconda** localmente no seu diretório de usuário (100% sem root):
  ```bash
  mkdir -p ~/miniconda3
  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
  bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
  ~/miniconda3/bin/conda init bash
  ```
  Reinicie o terminal e execute:
  ```bash
  conda create -n uti_dados python=3.11 pandas -y
  conda activate uti_dados
  ```

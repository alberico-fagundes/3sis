# 🚀 DIÁRIO DE BORDO: DIA 05 - A UTI DOS DADOS (PANDAS)
**Data:** 14 de Agosto de 2026 (Sexta-feira)
**Turma:** 3ª Série - Manhã - B
**Aulas:** 09:10 e 10:20 (Bloco de 100 minutos)

> **🎯 OBJETIVO EXTRAORDINÁRIO:** No mundo real, os dados nunca chegam perfeitos. Eles chegam doentes, faltando pedaços e cheios de lixo. Hoje vamos vestir o jaleco de Cientista de Dados e usar a biblioteca `pandas` como um bisturi cirúrgico para higienizar o CSV de sensores antes que ele infecte nosso modelo de Inteligência Artificial.

---

## 📚 1. INTEGRAÇÃO CURRICULAR OFICIAL
* **Ciência de Dados (Aulas 19, 20 e 21):** Medidas de tendência central, separatrizes e dispersão. (Vamos provar na prática que a *Mediana* é mais segura que a *Média* para preencher falhas de sensores).
* **Análise de Sistemas (Aulas 30 e 32):** Storytelling no ambiente de negócios. (Como convencer a diretoria de que dados ruins geram previsões mortais).

---

## 🧠 2.  O QUE É A HIGIENIZAÇÃO DE DADOS?

### **🚑 A ANALOGIA DA UTI (Unidade de Terapia Intensiva)**

Imagine que o nosso Backend (FastAPI) é um hospital de ponta e a nossa Inteligência Artificial (Scikit-learn) é o cirurgião-chefe. O arquivo `.csv` que recebemos da fábrica ontem (no dia de Upload) é o paciente que acabou de dar entrada na maca.
- **O Sangramento (Valores Nulos/NaN):** O sensor da máquina da fábrica desligou sozinho por 5 minutos devido a uma queda de energia. Ele gerou buracos na nossa planilha.
- **A Febre Alta (Outliers):** Um pico de tensão fez o sensor registrar 5.000 graus de temperatura ambiente num dia normal.
- **❌ A Abordagem Amadora (Júnior):** O desenvolvedor leigo pega a planilha sangrando e joga direto na mesa de cirurgia (treina a IA com os dados sujos). A IA aprende que "é normal bater 5.000 graus". Quando for prever no mundo real, a IA falha e a fábrica explode.
- **✅ A Abordagem Enterprise (Sênior):** O Cientista de Dados coloca o CSV na UTI (usando a ferramenta `pandas`). Ele costura os buracos preenchendo os "NaN" usando estatística pura, arranca os "Outliers" absurdos, e entrega um paciente perfeito e estável para a IA estudar.

---

## 🗺️ 3. ARQUITETURA VISUAL DO TRATAMENTO

```mermaid
graph LR
    A[CSV Bruto da Fábrica] -->|Entra na UTI| B(Pandas: Checkup de NaN)
    B -->|Amputação Leve| C(df.dropna - Corta lixo irrecuperável)
    C -->|Transfusão Sanguínea| D(df.fillna - Preenche buracos)
    D -->|Alta Hospitalar| E((CSV Estabilizado e Saudável))
    
    style A fill:#e0234e,color:#fff
    style D fill:#f39c12,color:#fff
    style E fill:#2ecc71,color:#fff
```

---

## 🔧 4. O BISTURI: IMPLEMENTAÇÃO DO CÓDIGO (MÃO NA MASSA)

**Passo 1: Instalar as ferramentas cirúrgicas (Conda)**
No terminal, com a "bolha invisível" `(venv)` ou `(base)` do Miniconda ativada:
```bash
pip install pandas
```

**Passo 2: A Cirurgia Padrão Ouro (`analise.py`)**
Crie um arquivo na mesma pasta onde salvamos os uploads de ontem.

```python
import pandas as pd

# 1. Colocando o paciente na maca
print("Recebendo paciente CSV da porta de carga...")
df = pd.read_csv("uploads/sensor_bruto.csv")

# 2. O Checkup Geral (Mostra onde o paciente está sangrando / NaN)
print("--- Diagnóstico: Falhas nos Sensores ---")
print(df.isnull().sum())

# 3. Tratamento de Choque (Preenchendo buracos com Estatística da Aula 20)
# PERGUNTA DA DRA. CLARA: Por que usamos a Mediana e não a Média?
# RESPOSTA: Se tivemos um erro que marcou 5.000 graus, a Média é arruinada. A Mediana ignora as anomalias absurdas e pega a normalidade.
df['sensor_etanol'] = df['sensor_etanol'].fillna(df['sensor_etanol'].median())
df['sensor_metanol'] = df['sensor_metanol'].fillna(df['sensor_metanol'].median())

# 4. Alta do paciente (Salvando um novo arquivo curado)
df.to_csv("uploads/sensor_curado.csv", index=False)
print("Cirurgia concluída. O Paciente (CSV) está salvo e pronto para a IA!")
```

---

## 🚨 5. A BÍBLIA DE ERROS (TROUBLESHOOTING)

### 🐛 ERRO 1: O Paciente Sumiu (FileNotFoundError)
**A Tela Mostra:** `FileNotFoundError: [Errno 2] No such file or directory: 'uploads/sensor_bruto.csv'`
**A Causa Oculta:** Você está rodando o script na porta da frente da escola, mas o arquivo está salvo na porta dos fundos.
**A Solução Enterprise:** Verifique de qual pasta você disparou o comando `python analise.py`. A pasta de onde você executa o comando é a "base". Sempre entenda o uso do `pwd` (Linux) ou `dir` (Windows).

---

## 🎓 6. EXERCÍCIO DE ALTA PERFORMANCE (BATERIA)

### 🟡 Nível 2: Desenvolvedor Júnior (O Machado)
**Cenário:** A diretoria enviou um arquivo com 1 milhão de linhas, mas apenas 5 linhas vieram com erros (`NaN`). 
**Pergunta:** Em vez de usar matemática complexa (mediana/média) para adivinhar os valores que faltam dessas 5 linhas específicas, qual seria a abordagem mais rápida e brutal que um Júnior poderia usar sem arruinar o modelo de IA?

<details>
<summary>👀 Ver a Resolução do Júnior</summary>
A Amputação Direta! O comando `df.dropna(inplace=True)`. Como são apenas 5 linhas doentes num universo gigante de 1 milhão de linhas perfeitamente saudáveis, você simplesmente as deleta. A remoção de míseros 0,0005% dos dados não vai alterar a matemática preditiva da Inteligência Artificial.
</details>

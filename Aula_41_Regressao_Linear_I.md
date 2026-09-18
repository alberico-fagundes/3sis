# 🚀 Aula 41: Regressão Linear com Scikit-Learn (Parte I)

**Disciplina:** Ciência de Dados (CD)  




---


---

### 🧩 1. O Problema Prático 


**O Dilema da Predição de Aumento de Gás:**  
Joana é cientista de dados na fábrica **SmartFactory**. O sistema de monitoramento registra a concentração de gás em PPM a cada hora, mas a equipe de segurança só descobre um vazamento quando o nível já ultrapassou o limite perigoso de 50 PPM.

Joana precisa de uma ferramenta preditiva que analise o histórico das últimas horas e estime em quanto tempo a concentração de gás atingirá o limite crítico, permitindo um alerta preventivo antes do acidente ocorrer.

**A Pergunta-Chave PBL:**  
> *Como Joana pode usar a biblioteca **Scikit-Learn (`LinearRegression`) em Python** para ajustar um modelo preditivo de Regressão Linear e estimar a tendência de subida de gás na fábrica?*

---

### 📖 2. Teoria Fundamentadora Completa (Conteúdo Integral do Slide RCO)

#### 2.1 O que é a Regressão Linear?
A **Regressão Linear** é uma técnica estatística e de Aprendizado de Máquina Supervisionado cujo objetivo é modelar a relação entre uma variável dependente contínua ($Y$, o valor que se quer prever) e uma ou mais variáveis independentes explicativas ($X$).
* **A Equação da Reta:** $Y = aX + b$
  * $Y$: Variável dependente (ex: Nível de Gás PPM).
  * $X$: Variável independente (ex: Tempo em horas).
  * $a$: Coeficiente angular (inclinação da reta / taxa de variação).
  * $b$: Intercepto (ponto onde a reta cruza o eixo Y).

#### 2.2 Modelagem com Scikit-Learn (`sklearn.linear_model`)
No ecossistema Python, a biblioteca `Scikit-Learn` fornece a classe `LinearRegression` para treinar e estimar modelos preditivos de forma programática.
1. **Divisão do Dataset (Treino e Teste):** Separação dos dados históricos em um conjunto para o modelo aprender (*Treino*) e outro para validar se as previsões são precisas (*Teste*).
2. **Método `.fit(X, y)`:** Função que ajusta os coeficientes matemáticos da reta aos dados de treino fornecidos.
3. **Método `.predict(X_novo)`:** Função que utiliza a equação estimada para calcular previsões em novos dados invisíveis.

#### 2.3 Ferramentas e Ambientes de Ciência de Dados
* **Jupyter Notebook / Anaconda Distribution:** Ambiente interativo padrão para prototipação e visualização de código Python.
* **Google Colab:** IDE em nuvem gratuita para execução e compartilhamento de scripts de Aprendizado de Máquina.

---

### 💻 3. Sintaxe Básica & Exemplo Análogo (Consulta Visual)

Veja como instanciamos, treinamos e fazemos previsões de Regressão Linear simples com Scikit-Learn em Python:

```python
# Exemplo Análogo: Treinamento de Regressão Linear com Scikit-Learn
import numpy as np
from sklearn.linear_model import LinearRegression

# 1. Dados de Treino: X = Tempo (horas), y = Nível de Gás (PPM)
X_treino = np.array([[1], [2], [3], [4], [5]]) # Deve ser matriz 2D
y_treino = np.array([12.0, 18.5, 25.0, 31.5, 38.0]) # Vetor 1D

# 2. Instanciação e Ajuste do Modelo
modelo = LinearRegression()
modelo.fit(X_treino, y_treino)

# 3. Predição para a Hora 6 (X = 6)
predicao_hora_6 = modelo.predict(np.array([[6]]))
print(f"[PREDIÇÃO ML]: Nível estimado de gás na Hora 6: {predicao_hora_6[0]:.2f} PPM")
print(f"[COEFICIENTE]: Taxa de aumento por hora: {modelo.coef_[0]:.2f} PPM/h")
```

---

### 🛠️ 4. Desafio Ativo 

Como cientista de dados na equipe de Joana na SmartFactory:

1. Abra seu ambiente Python (ou crie um script `predicao_gas.py` na pasta `uti_dados_python`).
2. Importe a classe `LinearRegression` do pacote `sklearn.linear_model`.
3. Crie dados simulados de 5 medições de tempo e PPM.
4. Ajuste o modelo usando `modelo.fit(X, y)` e calcule a previsão de PPM para os próximos 30 minutos.
5. Imprima o coeficiente angular e a estimativa preditiva no console.

---

### 🧪 5. Teste de Validação (5 Minutos)

1. Execute o script Python no terminal:
   ```bash
   python uti_dados_python/predicao_gas.py
   ```
2. Confirme se o console exibe o resultado da predição em PPM e os coeficientes do modelo ajustado sem erros.

---

### ❓ 6. Quiz de Fixação PBL (6 Questões de Múltipla Escolha)

#### Q1. Qual é o principal objetivo da Regressão Linear no contexto de Aprendizado de Máquina?
- (A) Classificar imagens em formato PNG.
- (B) Estimar a relação matemática contínua entre uma variável dependente ($Y$) e variáveis independentes ($X$) para fazer previsões.
- (C) Formatar o banco de dados SQL do servidor.
- (D) Apagar logs antigos do sistema operacional.



#### Q2. Na biblioteca Scikit-Learn do Python, qual método é utilizado para ajustar/treinar o modelo com os dados de treino?
- (A) `modelo.predict(X, y)`
- (B) `modelo.fit(X, y)`
- (C) `modelo.compile(X, y)`
- (D) `modelo.execute(X, y)`



#### Q3. Na equação da reta $Y = aX + b$, o que representa o coeficiente angular ($a$)?
- (A) O valor de $Y$ quando $X$ é igual a zero.
- (B) A inclinação da reta, que indica a taxa de variação de $Y$ a cada unidade alterada em $X$.
- (C) O erro quadrático médio da amostra.
- (D) A quantidade de linhas do arquivo CSV.



#### Q4. Por que é necessário dividir o conjunto de dados em "Treino" e "Teste" na Ciência de Dados?
- (A) Para duplicar o tamanho do arquivo em disco.
- (B) Para treinar o modelo com uma parte dos dados e avaliar a precisão das previsões em dados não vistos (teste).
- (C) Porque a linguagem Python exige dois arquivos separados.
- (D) Para deletar dados corrompidos.




#### Q5. Qual método do Scikit-Learn é chamado para calcular o valor previsto de $Y$ a partir de novos dados de entrada $X$?
- (A) `modelo.fit()`
- (B) `modelo.predict()`
- (C) `modelo.score()`
- (D) `modelo.transform()`



#### Q6. Qual das seguintes ambientes de desenvolvimento interativo em nuvem é amplamente utilizado para rodar scripts de Ciência de Dados em Python?
- (A) Google Colab / Jupyter Notebook.
- (B) Microsoft Paint.
- (C) WinZip.
- (D) Notepad.



---


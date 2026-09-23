# 🚀 Aula 65: Análise e Síntese de Problemas em Sistemas

**Disciplina:** Análise e Projeto de Sistemas (APS)  


---

> [!NOTE]
> **📚 ESTRUTURA PEDAGÓGICA (DUAL-TRACK):**
> * **📖 Trilha Teórica ( / Conceitual):** Estude o processo de pensamento analítico e sintético no desenvolvimento de software a partir desta documentação e do slide oficial RCO.
> * **🛠️ Trilha Prática (Exercício do Analista):** Atue como Analista de Sistemas e resolva o desafio individual de categorização de feedbacks e definição de escopo prioritário.

---

### 🧩 1. O Problema Prático

**O Dilema dos Feedbacks Desorganizados de João:**  
João foi designado para melhorar a usabilidade do aplicativo de entregas de um restaurante. Ele conversou com os clientes e reuniu **6 reclamações totalmente misturadas**:

1. 🔴 *"O botão de 'Finalizar Pedido' fica escondido lá embaixo na tela e é difícil de achar."*
2. 🔴 *"O aplicativo fecha sozinho quando tento pagar via PIX."*
3. 🔴 *"A foto do prato é muito pequena e não dá para ver os ingredientes."*
4. 🔴 *"Quando peço uma bebida extra, o valor total do carrinho não atualiza."*
5. 🔴 *"As cores do texto são muito claras e difíceis de ler no sol."*
6. 🔴 *"Não recebo nenhuma notificação avisando quando o motoboy sai para entrega."*

Paralisado por essa lista de problemas brutos e desalinhados, João não sabe por onde começar nem o que repassar para a equipe de desenvolvimento.

**A Pergunta-Chave:**  
> *Como João pode utilizar a **Análise (Decomposição)** e a **Síntese (Integração e Definição de Escopo)** para organizar essas descobertas e planejar uma solução eficaz?*

---

### 📖 2. Teoria Fundamentadora Completa (Conteúdo Integral do Slide RCO)

#### 2.1 O que é o Processo de Análise (Decomposição)?
* **Conceito:** A **Análise** consiste em pegar um problema grande, complexo ou desorganizado e **desmontá-lo em partes menores**, categorizando os elementos para entendê-los em detalhe.
* **Na Prática:** Separar as reclamações dos clientes em "gavetas" específicas (ex: o que é problema de **Design/Usabilidade** vs. o que é **Bug/Erro do Sistema**).

#### 2.2 O que é o Processo de Síntese (Integração)?
* **Conceito:** A **Síntese** é o processo inverso e complementar. Trata-se de **reunir e combinar as partes analisadas** para criar uma solução coesa, integrada e funcional.
* **Na Prática:** Pegar os problemas categorizados e transformar em um **Plano de Ação (Escopo do Projeto)** com prioridades bem definidas.

#### 2.3 Os 4 Passos da Estruturação de Problemas em Design Thinking
1. **Mudando o Foco:** Capacidade da equipe de ajustar a atenção para novas prioridades à medida que o projeto evolui.
2. **Organizando Descobertas:** Estruturar informações brutas de pesquisas em conhecimento aplicável e estratégico.
3. **Estruturando Problemas:** Decompor questões complexas em partes menores e gerenciáveis.
4. **Escolhendo o Escopo:** Definir rigorosamente os limites do projeto, especificando **o que será feito agora** e **o que fica para depois**.

---

### 💻 3. Exemplo Resolvido de Análise e Síntese (Consulta Visual)

Veja como um Analista de Sistemas organiza dados brutos em uma planilha ou documento:

#### 1. Dados Brutos Recebidos:
> *"O site é lento", "Esqueci minha senha não funciona", "O fundo azul é feio"*

#### 2. Processo de ANÁLISE (Separação por Módulos):
* **Módulo A — Interface / Usabilidade:** *"O fundo azul é feio"*
* **Módulo B — Funcionalidades e Regras de Negócio:** *"Esqueci minha senha não funciona"*
* **Módulo C — Performance do Servidor:** *"O site é lento"*

#### 3. Processo de SÍNTESE (Definição de Escopo da Versão 1.0):
* **Escopo Urgente (Versão 1.0):** Corrigir a função *"Esqueci minha senha"* (Funcionalidade crítica) e otimizar o banco de dados para acelerar o site.
* **Escopo Secundário (Versão 1.1):** Ajustar a cor de fundo azul.

---

### 🛠️ 4. Desafio Prático Individual 

> **Modalidade:** Trabalho INDIVIDUAL.  
> **Onde realizar:** No seu caderno, em um arquivo de texto no VS Code (`desafio_aula65.txt`) ou em uma planilha.

Assuma o papel de Analista de Sistemas e resolva o problema do João executando os passos abaixo:

#### PASSO 1: ANÁLISE (Decomposição em Gavetas)
Classifique cada uma das **6 reclamações do problema do João** na categoria correta:

* **Categoria 1 — Interface e Usabilidade (Visual / Design):**
  * *(Anote aqui os números das reclamações correspondentes)*
* **Categoria 2 — Lógica e Funcionamento (Bugs / Erros de Sistema):**
  * *(Anote aqui os números das reclamações correspondentes)*

#### PASSO 2: SÍNTESE (Definição do Escopo Prioritário)
Agora que você analisou os 6 problemas, aja como o líder do projeto e escolha **3 problemas prioritários** para serem corrigidos na **Versão 1.0 do Aplicativo**.

1. **Problema Escolhido 1:** *(Indique o número e o motivo da escolha)*
2. **Problema Escolhido 2:** *(Indique o número e o motivo da escolha)*
3. **Problema Escolhido 3:** *(Indique o número e o motivo da escolha)*

---

### 🧪 5. Teste de Validação e Socialização (10 Minutos)

1. Revise sua classificação e confirme se nenhum dos 6 problemas ficou sem categoria.
2. Responda mentalmente: *"Se a equipe só tiver tempo de corrigir 1 único erro hoje, qual deles causaria o maior prejuízo financeiro ou de uso ao restaurante se não for corrigido?"*
3. Compartilhe sua escolha de escopo prioritário via classroom.

---

### ❓ 6. Quiz de Fixação 


#### Q1. Qual das opções a seguir melhor descreve o processo de ANÁLISE em desenvolvimento de sistemas?
- (A) Combinar várias ideias diferentes em uma única solução final.
- (B) Decompor um problema complexo em partes menores para entendê-lo em detalhes.
- (C) Escrever linhas de código sem planejar.
- (D) Ignorar as reclamações dos usuários.





#### Q2. Como se caracteriza o processo de SÍNTESE no planejamento de projetos de software?
- (A) Deletar arquivos antigos do servidor.
- (B) Reunir e integrar as partes ou descobertas individuais para criar uma solução coesa e unificada.
- (C) Formatar o computador do cliente.
- (D) Mudar o nome do aplicativo.



#### Q3. Durante o processo de planejamento de um sistema, por que a definição de ESCOPO é fundamental?
- (A) Para proibir que os usuários enviem sugestões.
- (B) Para delimitar claramente o que faz parte da solução no momento e o que fica de fora, garantindo foco e prazos.
- (C) Para aumentar o custo do projeto sem necessidade.
- (D) Para impedir que o sistema seja atualizado no futuro.




#### Q4. Ao receber uma lista de 50 reclamações dispersas de clientes, qual é a sequência correta de ações de um Analista?
- (A) Tentar resolver todas as 50 reclamações ao mesmo tempo.
- (B) Analisar e categorizar os problemas por temas semelhantes e, em seguida, sintetizar um escopo prioritário.
- (C) Apagar todas as reclamações e refazer o aplicativo do zero.
- (D) Repassar a lista sem organização direta para os programadores.




#### Q5. A habilidade de ajustar a atenção e os esforços da equipe para novas prioridades à medida que o projeto evolui é chamada no Design Thinking de:
- (A) Escolhendo o escopo.
- (B) Mudando o foco.
- (C) Erro de compilação.
- (D) Teste de banco de dados.




#### Q6. Qual é o principal benefício de aplicar Análise e Síntese antes de começar a programar um aplicativo?
- (A) Reduzir o tempo de digitação no teclado.
- (B) Garantir que a equipe construa uma solução focada, organizada e que resolva os problemas reais dos usuários.
- (C) Eliminar a necessidade de testar o aplicativo.
- (D) Impedir o uso de banco de dados.

---

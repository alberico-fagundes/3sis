# 📘 Guia Didático PBL: O Framework Cynefin e Tomada de Decisão em Engenharia de Software

**Disciplina:** Análise e Projeto de Sistemas (APS) — Aula 63  
**Série:** 3ª Série do Ensino Técnico (SEED-PR)  


---

## 🎯 1. Objetivos de Aprendizagem

Ao final desta aula de 50 minutos, o estudante será capaz de:
1. **Compreender a estrutura do Framework Cynefin**, identificando seus 5 domínios de contexto (*Claro/Simples, Complicado, Complexo, Caótico e Desordem*).
2. **Escolher a estratégia de tomada de decisão adequada** para cada tipo de problema no desenvolvimento de sistemas.
3. **Aplicar o Cynefin para lidar com crises de segurança e instabilidades em produção** de forma profissional.

---

## 📖 2. Teoria Completa da Aula (Síntese dos Slides RCO)

### 2.1 O que é o Cynefin Framework?
Criado por Dave Snowden, o **Cynefin** (*palavra de origem galesa, pronuncia-se 'kun-év-in'*) é um modelo conceitual de sensoriamento e tomada de decisão que ajuda líderes e equipes de engenharia a **classificar problemas conforme a sua natureza e complexidade**.

---

### 2.2 Os 5 Domínios do Cynefin

```
       COMPLEXO             │            COMPLICADO
   (Saber-emergente)        │         (Saber-especialista)
   Sonda -> Sente -> Responde│      Sente -> Analisa -> Responde
 ───────────────────────────┼─────────────────────────────
        CAÓTICO             │           CLARO / SIMPLES
   (Ação imediata)          │          (Melhores Práticas)
   Aje -> Sente -> Responde │     Sente -> Categoriza -> Responde
                            │
               [ NO CENTRO: DESORDEM ]
```

1. **Domínio Claro / Simples (Boa Prática):**
   * **Causa e efeito são óbvias para todos.** Há uma resposta certa conhecida.
   * *Ação:* Sentir $\rightarrow$ Categorizar $\rightarrow$ Responder.
   * *Exemplo:* Mudar a senha de um usuário no banco de dados.

2. **Domínio Complicado (Especialistas):**
   * **Causa e efeito existem, mas exigem análise técnica especializada.**
   * *Ação:* Sentir $\rightarrow$ Analisar $\rightarrow$ Responder.
   * *Exemplo:* Otimizar uma consulta SQL lenta que envolve junção de 10 tabelas.

3. **Domínio Complexo (Inovação / Ágil):**
   * **Causa e efeito só são percebidas em retrospectiva.** Há alta incerteza.
   * *Ação:* Sondar (*Probe*) $\rightarrow$ Sentir $\rightarrow$ Responder.
   * *Exemplo:* Lançar um novo produto digital onde ninguém sabe como o usuário vai reagir.

4. **Domínio Caótico (Crise / Incêndio):**
   * **Não há relação perceptível de causa e efeito.** O sistema está desmoronando.
   * *Ação:* Agir imediatamente para estancar a sangria $\rightarrow$ Sentir $\rightarrow$ Responder.
   * *Exemplo:* Um ataque hacker derruba o servidor principal e os dados estão sendo vazados.

5. **Domínio da Desordem (Centro):**
   * Ocorre quando a equipe **não sabe em qual dos 4 domínios o problema se encontra**, tendendo a aplicar a ferramenta que mais gosta (o chamado "vício de estimativa").

---

## 🧩 3. O Desafio Prático 

> **O Dilema do Desenvolvedor João:**  
> João é líder técnico do e-commerce da fábrica. De repente, a tela de checkout para de funcionar e o banco de dados principal começa a travar, zerando os pagamentos do dia.  
> 
> João tentou marcar uma reunião de 3 horas para discutir teorias (tratando o problema como se fosse *Complicado*), enquanto a empresa perdia R$ 10.000,00 por minuto com os servidores pegando fogo.

**Sua Missão como Consultor de Sistemas:**  
Ajudar João a **aplicar o Framework Cynefin**, reconhecendo que o sistema entrou no **Domínio Caótico** e exigindo **AÇÃO IMEDIATA** para restaurar a estabilidade antes de qualquer análise profunda.

---

## 🛠️ 4. Passo a Passo "Mão na Massa" (Low-Friction / 15 Minutos)

Classifique os cenários no quadro do Cynefin com sua equipe:

### 🟢 Passo 1: Classificar os Problemas do Projeto
Para cada ocorrência da semana, determine o domínio Cynefin correto:
* *Cenário A:* O botão do formulário de contato está desalinhado 2px. $\rightarrow$ **Domínio Claro/Simples** (Apenas corrigir no CSS).
* *Cenário B:* A API de pagamentos está apresentando *timeout* esporádico. $\rightarrow$ **Domínio Complicado** (Chamar o analista sênior para ler os logs).
* *Cenário C:* O servidor caiu totalmente após um ataque DDoS. $\rightarrow$ **Domínio Caótico** (Agir: Subir a página estática de manutenção imediatamente).

### 🟡 Passo 2: Definir o Protocolo de Ação para o Caos
1. Desconectar o banco da rede externa (Ação de Estancamento).
2. Ligar o servidor de *backup* / réplica.
3. Comunicar a equipe de segurança.

---

## 🧪 5. Questionário

#### **Questão 1 (Cesgranrio - Banco do Brasil / Tecnologia e Gestão de Incidentes):**
No Framework Cynefin, quando ocorre um incidente crítico imprevisível de alta gravidade (como a queda total de uma API de pagamentos sem causa aparente), o sistema encontra-se temporariamente no **Domínio Caótico**. A sequência correta de ação recomendada pelo Cynefin para este domínio é:
- (A) Sentir $\rightarrow$ Categorizar $\rightarrow$ Responder.
- (B) Sondar $\rightarrow$ Sentir $\rightarrow$ Responder.
- (C) Agir $\rightarrow$ Sentir $\rightarrow$ Responder.
- (D) Analisar $\rightarrow$ Debater $\rightarrow$ Votar.
- (E) Aguardar $\rightarrow$ Documentar $\rightarrow$ Delegar.

---

#### **Questão 2 (FGV - MPO / Analista de Governança de TI):**
Um especialista em banco de dados é chamado para otimizar uma consulta extremamente complexa que envolve milhões de registros. Há causas e efeitos conhecidos, porém a solução exige conhecimento técnico aprofundado e análise de desempenho. Segundo o Cynefin, essa demanda enquadra-se no domínio:
- (A) Caótico.
- (B) Simples / Claro.
- (C) Complicado.
- (D) Anárquico.
- (E) Desordem absoluta.

---

#### **Questão 3 (Cebraspe/UnB - DATAPREV / Análise de Negócios e Agilidade):**
Julgue o item subsequente acerca do modelo Cynefin:  
*No domínio Complexo do Framework Cynefin, a relação entre causa e efeito só pode ser compreendida em retrospectiva, motivo pelo qual as metodologias ágeis recomendam a realização de pequenos experimentos (sondas) para validar hipóteses.*
- (A) Certo.
- (B) Errado.

---

#### **Questão 4 (Vunesp - Prefeitura de São José dos Campos / Analista de Sistemas):**
Quando uma equipe de desenvolvimento não consegue identificar em qual dos domínios do Cynefin um determinado problema se encontra, diz-se que o grupo está atuando no estado de:
- (A) Desordem.
- (B) Estabilidade pura.
- (C) Equilíbrio de Nash.
- (D) Matriz SWOT.
- (E) Consenso ágil.

---

#### **Questão 5 (Quadrix - Conselho de Farmácia / TI e Processos):**
Uma tarefa de rotina em um departamento de TI consiste em resetar a senha de um usuário que digitou a credencial errada. Essa atividade possui causa e efeito diretos e solução padronizada por um manual. No Cynefin, essa tarefa pertence ao domínio:
- (A) Caótico.
- (B) Complexo.
- (C) Claro / Simples.
- (D) Nulo.
- (E) Disruptivo.

---

#### **Questão 6 (ENEM / Gestão, Tecnologia e Tomada de Decisão):**
Em situações de incerteza no mundo corporativo digital, gestores precisam adaptar sua postura ao tipo de desafio enfrentado. A capacidade de estancar rapidamente um vazamento de dados antes de iniciar reuniões de análise ilustra a mudança de postura necessária em cenários:
- (A) De rotina burocrática automatizada.
- (B) Caóticos de urgência operacional.
- (C) De documentação acadêmica de longo prazo.
- (D) Sem qualquer impacto na reputação da empresa.
- (E) De treinamento exclusivo para estagiários.

---

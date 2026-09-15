# 📘 Guia Didático PBL: Design Vetorial e Criação de Logotipo com Curvas Bézier

**Disciplina:** Computação Gráfica (CG) — Aula 41  
**Série:** 3ª Série do Ensino Técnico (SEED-PR)  


**Abordagem:** Aprendizagem Baseada em Problemas (PBL) + Teoria do Slide RCO + Questões de Concursos Reais  

---

## 🎯 1. Objetivos de Aprendizagem

Ao final desta aula de 50 minutos, o estudante será capaz de:
1. **Diferenciar Gráficos Vetoriais (SVG) de Imagens Matriciais (PNG/JPG)**, compreendendo por que marcas corporativas exigem escalabilidade infinita.
2. **Dominar a Ferramenta Bézier (*Pen Tool*) e Formas Geométricas**, manipulando nós (*nodes*) e alças de controle (*handles*) para desenhar curvas suaves.
3. **Organizar a Área de Trabalho Gráfica**, utilizando camadas (*layers*), linhas-guia e exportando um logotipo SVG pronto para o Dashboard Web.

---

## 🛠️ 2. Qual Software Usar na Aula? (Opções Gratuitas para a Turma)

O estudante pode escolher a ferramenta que melhor se adapta à sua máquina:

| Opção | Software | Como Acessar / Login | Perfil / Vantagem |
| :--- | :--- | :--- | :--- |
| **Opção 1 (Oficial RCO)** | **Inkscape** | Instalado no PC do laboratório | **Prática Técnica:** 100% Grátis, offline e ideal para treinar a Ferramenta Bézier que cai nas provas. |
| **Opção 2 (Escolar / SEED-PR)** | **Canva Educação** | Entrar com `@escola.pr.gov.br` ou `@aluno.pr.gov.br` | **Criação Rápida:** Libera recursos Pro gratuitamente e permite baixar em **SVG (Vetor)**. |
| **Opção 3 (Web / Sem Instalar)** | **[Vectorpea](https://www.vectorpea.com/)** | Direto no Navegador (Chrome/Firefox) | Zero instalação e zero cadastro. Abre e desenha com Pen Tool na hora. |
| **Opção 4 (Web Profissional)** | **[Figma](https://www.figma.com/)** | Navegador (com login grátis) | Padrão da indústria de tecnologia para interfaces e ícones SVG. |

> [!TIP]
> **💡 Dica para quem for usar o Canva:**  
> Certifique-se de fazer login com sua conta institucional da **SEED-PR** para ativar a versão Educacional. Na hora de salvar, vá em **Compartilhar ➔ Baixar ➔ Formato de Arquivo: SVG (Vetor)**.

---

## 📖 3. Teoria Completa da Aula 


### 3.1 O que é um Logotipo Vetorial?
O **logotipo** é a identidade visual central de um sistema ou empresa. Na indústria moderna, a mesma marca precisa funcionar em uma tela de celular de 32 pixels e em um telão industrial ou outdoor de 10 metros.

```
  [ Imagem Matricial (PNG/JPG) ] ──> Dando Zoom ──> [ ❌ Imagem Quadriculada / Pixelada ]
  
  [ Gráfico Vetorial (SVG) ]     ──> Dando Zoom ──> [ ✅ 100% Nítido (Fórmulas Matemáticas) ]
```

---

### 📊 3.2 Tabela Comparativa: Vetor (SVG) vs. Mapa de Bits / Raster (PNG/JPG)

| Característica | 📐 Gráfico Vetorial (SVG / AI / EPS) | 🖼️ Imagem Matricial / Raster (PNG / JPG) |
| :--- | :--- | :--- |
| **Como é formado?** | Fórmulas matemáticas (pontos, linhas e curvas). | Grade fixa de pontinhos coloridos (**pixels**). |
| **Ao dar Zoom / Ampliar:** | **Nitidez infinita** (nunca perde qualidade). | **Pixeliza** (fica borrado e serrilhado). |
| **Tamanho do Arquivo:** | Levíssimo (poucos Kilobytes de código texto). | Pesado em alta resolução. |
| **Onde é obrigatório usar?** | **Logotipos, ícones de interface e fontes.** | Fotografias da vida real e texturas complexas. |

---

### 🧩 3.3 Anatomia de um Desenho Vetorial (A Ferramenta Bézier)

A **Ferramenta Bézier (*Pen Tool*)** é o pincel do designer vetorial. Ela cria formas a partir de 3 elementos fundamentais:

| Elemento | Nome em Inglês | O que é / Como funciona na prática? |
| :--- | :--- | :--- |
| 📍 **Nó / Ponto de Ancoragem** | *Node / Anchor Point* | O ponto fixo onde a linha começa, muda de direção ou termina. |
| 🎛️ **Alça / Haste de Controle** | *Control Handle* | Os "braços" que você puxa para regular o arco e a inclinação da curva. |
| 〰️ **Caminho / Traçado** | *Path / Stroke* | A linha matemática contínua que une dois ou mais nós. |
| 🎨 **Preenchimento** | *Fill* | A cor sólida ou degradê colocada dentro do caminho fechado. |

---

## 🧩 4. O Desafio Prático (Problema do Mundo Real)

> **🏭 O Dilema da Designer Maria na SmartFactory:**  
> Maria foi encarregada de criar o logotipo oficial da **SmartFactory** (sistema de monitoramento de gás e sensores industriais).  
> 
> Ela desenhou um símbolo rápido no Paint e salvou como `logo.png`. Quando a equipe colocou a imagem no totem da fábrica de 65 polegadas e no cabeçalho do Dashboard React, o logotipo apareceu totalmente **embaçado, torto e pixelado**. A diretoria exigiu uma solução profissional e escalável.

**Sua Missão:**  
Ajudar Maria a **vetorizar o logotipo da SmartFactory** utilizando formas geométricas e/ou a Ferramenta Bézier (no Inkscape, Canva Educação, Vectorpea ou Figma), garantindo que a marca fique 100% nítida em qualquer tamanho de tela!

---

## 🛠️ 5. Passo a Passo "Mão na Massa" 


Siga o roteiro prático para construir e testar o logotipo vetorial:

### 🟢 Passo 1: Estruturar a Geometria Base (Área de Trabalho)
1. Abra o Inkscape, Vectorpea ou o Canva Educação.
2. Crie um novo documento no formato quadrado (**200 x 200 pixels**).
3. Use a ferramenta de **Retângulo / Polígono** para fazer a base da fábrica.

### 🟡 Passo 2: Traçar o Símbolo com Curvas Bézier ou Formas Geométricas
1. Trace ou posicione o sensor de gás com a **Ferramenta Bézier / Pen Tool** ou combinando círculos/triângulos.
2. Dê um clique para criar o ponto inicial, clique no segundo ponto e **segure arrastando o mouse** para criar a curva do alerta.
3. Feche o contorno voltando ao ponto de início.
4. Aplique a paleta visual industrial: Azul Petróleo (`#2c3e50`) para a fábrica e Vermelho/Laranja (`#e74c3c`) para o sensor de alerta.
5. Vá em **Exportar / Salvar Como ➔ Formato SVG**.

---

### 💻 5.1 Estrutura do Arquivo Vetorial SVG Gerado

Se você abrir o arquivo `.svg` em um editor de código (como o VS Code), verá que o vetor nada mais é do que coordenadas matemáticas:

```xml
<!-- logo_smartfactory.svg -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="150" height="150">
  <!-- Estrutura da Fábrica (Traçado Bézier) -->
  <path d="M 15,85 L 15,45 L 45,25 L 45,45 L 75,25 L 75,85 Z" fill="#2c3e50" />
  
  <!-- Sensor de Gás IoT no Topo (Forma Primitiva Círculo) -->
  <circle cx="45" cy="25" r="8" fill="#e74c3c" />
  <circle cx="45" cy="25" r="4" fill="#ffffff" />
</svg>
```

---

### 🚀 5.2 Teste de Validação da Escalabilidade
1. Salve o arquivo como `logo_smartfactory.svg`.
2. Abra o arquivo diretamente no navegador (Google Chrome ou Firefox).
3. Pressione `Ctrl + '+'` e dê **zoom de 500%**.  
   *Resultado:* As bordas continuam **perfeitamente retas e nítidas**, sem nenhum pixel estourado!

---

## 🧪 6. Quiz de Fixação (Questões de Concursos e Avaliações Técnicas)

#### **Questão 1 (Cesgranrio - Banco do Brasil / Design e Mídias Digitais):**
No desenvolvimento de logotipos para marcas e sistemas corporativos, recomenda-se que a arte final seja gerada em formato vetorial (SVG) e não em mapa de bits (*raster*). O motivo técnico principal para essa recomendação é:
- (A) O formato vetorial impede que a imagem seja visualizada em dispositivos móveis.
- (B) O vetor permite redimensionar o logotipo para qualquer tamanho sem perda de nitidez.
- (C) Os arquivos vetoriais são sempre mais pesados do que fotos em alta resolução.
- (D) Os mapas de bits não suportam a aplicação de cores primárias.
- (E) O formato vetorial exige o pagamento obrigatório de licenças de software.

---

#### **Questão 2 (FGV - Assembleia Legislativa / Programador Visual):**
Em softwares de edição vetorial como Inkscape e Adobe Illustrator, a ferramenta empregada especificamente para desenhar caminhos personalizados, vetores e curvas suavizadas por meio de pontos de ancoragem é a:
- (A) Ferramenta Lata de Tinta (*Paint Bucket*).
- (B) Ferramenta Bézier / Caneta (*Pen Tool*).
- (C) Ferramenta Borracha (*Eraser Tool*).
- (D) Ferramenta Conta-gotas (*Eyedropper*).
- (E) Ferramenta Varinha Mágica (*Magic Wand*).

---

#### **Questão 3 (Cebraspe/UnB - FUB / Técnico em Artes Gráficas):**
Julgue o item a seguir relativo aos conceitos fundamentais de Computação Gráfica:  
*Curvas de Bézier são equações paramétricas utilizadas na modelagem vetorial para definir formas e contornos suaves a partir de pontos de ancoragem (nós) e alças de manipulação.*
- (A) Certo.
- (B) Errado.

---

#### **Questão 4 (Vunesp - Prefeitura de Sertãozinho / Designer Gráfico):**
Ao criar um logotipo que será aplicado tanto na fachada de uma fábrica quanto em um pequeno ícone no aplicativo móvel, o designer deve garantir a usabilidade do símbolo. A característica técnica que permite ao logotipo manter sua reconhecibilidade e nitidez em diferentes dimensões é chamada de:
- (A) Pixelização dinâmica.
- (B) Dissonância cognitiva.
- (C) Escalabilidade.
- (D) Interpolagem de raster.
- (E) Compressão destrutiva.

---

#### **Questão 5 (Quadrix - Conselho de Arquitetura / Programador Visual):**
Durante o processo de vetorização de um rascunho no Inkscape, o designer importa a imagem desenhada à mão para a área de trabalho. A boa prática de organização de camadas (*layers*) recomenda que essa imagem de referência deva ser:
- (A) Convertida imediatamente em texto editável.
- (B) Posicionada em uma camada dedicada e travada (*Lock Layer*) para não mover acidentalmente durante o traçado.
- (C) Deletada antes do início de qualquer desenho.
- (D) Multiplicada por cem vezes para cobrir toda a tela.
- (E) Salva exclusivamente como arquivo de áudio.

---

#### **Questão 6 (ENEM / Linguagens e Tecnologias Visuais):**
A evolução das interfaces digitais exigiu a criação de identidades visuais responsivas. O uso de formatos vetoriais escaláveis e formas geométricas simplificadas na construção de logotipos contemporâneos visa atender à seguinte necessidade do mercado:
- (A) Dificultar a leitura do símbolo por usuários leigos.
- (B) Garantir a rápida identificação e perfeita adaptação da marca em telas de diferentes tamanhos e resoluções.
- (C) Exigir que todos os aparelhos celulares possuam a mesma dimensão física.
- (D) Restringir o uso de marcas a materiais exclusivamente impressos em papel.
- (E) Impedir a reprodução da logomarca em navegadores web.

---

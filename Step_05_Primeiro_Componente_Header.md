# 🧱 Passo 05: Criando Seu Primeiro Componente React (Header)

Com o projeto Vite limpo e o servidor Express rodando, vamos iniciar a construção da interface do nosso **Smart Factory Dashboard** criando nosso primeiro componente modular: o Cabeçalho (Header).

### 📌 O Conceito (Teoria Profunda)
Em React, a interface é construída como um conjunto de peças de Lego chamadas **Componentes**. Um componente é uma função JavaScript que retorna elementos visuais (JSX) e possui suas próprias regras e estilos CSS. 
* **Modularidade:** Separar o cabeçalho em `Header.jsx` permite reaproveitá-lo ou modificá-lo sem poluir o arquivo principal `App.jsx`.
* **Separação de Responsabilidades:** O componente `Header` é responsável apenas por exibir o nome da fábrica, o indicador de status do sistema e o horário atual.

### 📖 Sintaxe Básica (Exemplos Análogos)

**1. Estrutura Padrão de um Componente React:**
```jsx
import React from 'react';
import './MeuComponente.css';

function MeuComponente() {
  return (
    <div className="minha-classe">
      <h1>Título Dinâmico: {new Date().toLocaleTimeString()}</h1>
    </div>
  );
}

export default MeuComponente;
```

**2. Como Importar e Usar no `App.jsx`:**
```jsx
import React from 'react';
import MeuComponente from './components/MeuComponente';

function App() {
  return (
    <div>
      <MeuComponente />
    </div>
  );
}

export default App;
```

---

### 💻 Mão na Massa (Desafio Ativo)

**Sua Tarefa Prática:**

1. **Crie a pasta de componentes:**
   Dentro da pasta `frontend/src/`, crie uma nova pasta chamada `components`.

2. **Crie o componente `Header.jsx`:**
   Dentro de `src/components/`, crie o arquivo `Header.jsx` e insira o código:
   ```jsx
   import React from 'react';
   import './Header.css';

   function Header() {
     return (
       <header className="factory-header">
         <div className="header-content">
           <h1>🏭 Smart Factory Dashboard</h1>
           <div className="status-indicators">
             <span className="status-online">● Sistema Online</span>
             <span className="timestamp">Última atualização: {new Date().toLocaleTimeString()}</span>
           </div>
         </div>
       </header>
     );
   }

   export default Header;
   ```

3. **Crie o arquivo de estilos `Header.css`:**
   Na mesma pasta (`src/components/`), crie o arquivo `Header.css`:
   ```css
   .factory-header {
     background-color: #2c3e50;
     color: white;
     padding: 1rem;
     box-shadow: 0 2px 4px rgba(0,0,0,0.1);
   }

   .header-content {
     display: flex;
     justify-content: space-between;
     align-items: center;
     flex-wrap: wrap;
     gap: 1rem;
   }

   .factory-header h1 {
     margin: 0;
     font-size: 1.5rem;
   }

   .status-indicators {
     display: flex;
     gap: 1.5rem;
     font-size: 0.9rem;
   }

   .status-online {
     color: #2ecc71; /* Verde */
   }

   .status-offline {
     color: #e74c3c; /* Vermelho */
   }

   @media (max-width: 600px) {
     .header-content {
       flex-direction: column;
       align-items: flex-start;
     }
   }
   ```

4. **Conecte o Header no `App.jsx`:**
   Abra `src/App.jsx` e atualize para:
   ```jsx
   import React from 'react';
   import Header from './components/Header';
   import './App.css';

   function App() {
     return (
       <div className="App">
         <Header />
         <main className="App-main">
           <h2>Bem-vindo ao Smart Factory Dashboard!</h2>
           <p>Este é o início da nossa interface de monitoramento industrial.</p>
           <p>Nas próximas aulas, vamos conectar este frontend aos nossos backends de Node.js e Python.</p>
         </main>
       </div>
     );
   }

   export default App;
   ```

5. **Adicione estilos básicos ao `App.css`:**
   Abra `src/App.css` e substitua por:
   ```css
   .App {
     text-align: center;
     min-height: 100vh;
     background-color: #ecf0f1;
   }

   .App-main {
     padding: 2rem;
     max-width: 800px;
     margin: 0 auto;
   }

   .App-main h2 {
     color: #2c3e50;
     margin-top: 0;
   }

   .App-main p {
     color: #34495e;
     line-height: 1.6;
   }
   ```

---

### ⚠️ Regras Importantes & Erros Comuns

* 🚨 **`React is not defined`:** Esqueceu o `import React from 'react';` no topo do arquivo.
* 🔤 **Nomes de Componentes:** Devem SEMPRE começar com **Letra Maiúscula** (`Header.jsx`, não `header.jsx`).
* 📦 **Elemento Raiz Único:** Todo componente deve retornar apenas um elemento pai (ex: `<header>...</header>` ou `<div>...</div>`).

**Teste:** No terminal do frontend (`cd frontend`), rode `npm run dev`. Abra o navegador no link fornecido. Você verá o cabeçalho escuro da **Smart Factory Dashboard** com o status verde "● Sistema Online" e o horário atual!

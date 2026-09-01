

#### Etapa : Criando Seu Primeiro Componente
Vamos criar um componente simples que será a base do nosso painel de controle - um cabeçalho que mostra o nome da fábrica e o status do sistema:

* **No Plano A (na pasta `src/components`):**
  1. Crie uma nova pasta chamada `components` dentro de `src/` (se ainda não existir)
  2. Dentro de `src/components`, crie um novo arquivo chamado `Header.jsx`
  3. Adicione o seguinte código:
     ```jsx
     import React from 'react';
     import './Header.css'; // Vamos criar este arquivo em seguida

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

* **Crie o arquivo de estilos `Header.css` na mesma pasta:**
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

#### Etapa 4: Usando o Componente em Nossa Aplicação
Para ver nosso componente em ação, precisamos importá-lo e usá-lo em nosso App principal:

* **Edite o arquivo `src/App.jsx`:**
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

* **Edite o arquivo `src/App.css` para adicionar alguns estilos básicos:**
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

#### Etapa 5: Visualizando o Resultado
Se tudo estiver configurado corretamente:
1. Seu navegador deve mostrar um cabeçalho escuro com o título "Smart Factory Dashboard"
2. À direita, você deve ver o indicador de sistema online e o horário atual
3. Abaixo, uma mensagem de boas-vindas com instruções para as próximas aulas
4. O horário deve atualizar a cada segundo (você notará que não - vamos melhorar isso em aulas futuras com useState e useEffect!)

### ⚠️ Regras Importantes para Lembrar

1. **Nomeie componentes com letra maiúscula**: Todo componente React deve começar com letra maiúscula (ex: `Header`, não `header`)
2. **Um componente retorna apenas um elemento raíz**: Use `<div>...</div>` ou `<>...</>` (fragmento) se precisar retornar múltiplos elementos
3. **Separe responsabilidades**: Um componente deve fazer uma coisa bem feita (nosso Header só mostra cabeçalho e status)
4. **Use CSS Modules ou arquivos separados**: Evite estilos inline quando possível para melhor manutenção
5. **Exporte sempre seu componente**: No final do arquivo, use `export default NomeDoComponente;` ou exportação nomeada

### 🚨 Erro Comum (Fique Atento!)
Esquecer de importar o React no início do arquivo é um erro clássico que leva à mensagem "React is not defined". Se você escrever:
```jsx
function Header() {
  return <h1>Título</h1>;
}
export default Header;
```
Sem o `import React from 'react';` no topo, você vai obter esse erro porque o JSX que você escreve é transformado em chamadas a `React.createElement()` under the hood.

**Sempre:**
1. Comece seus arquivos de componente com `import React from 'react';`
2. Verifique se o nome do componente está exatamente igual na exportação e no import
3. Use o autocompletar do seu IDE (VS Code) para evitar erros de digitação
4. Se ver "React is not defined", 99% das vezes é porque esqueceu o import

**Sua Tarefa:** 
1. Crie o projeto React com Vite seguindo as instruções do Plano A ou B
2. Crie o componente Header.jsx e seu arquivo Header.css conforme especificado
3. Modifique o App.jsx para importar e usar o Header
4. Adicione os estilos básicos ao App.css
5. Teste se:
   - O cabeçalho aparece com as cores corretas
   - O título "Smart Factory Dashboard" está visível
   - Os indicadores de status aparecem à direita
   - A mensagem de boas-vindas aparece abaixo do cabeçalho
6. Experimente modificar o texto ou as cores e veja as mudanças aparecerem em tempo real (graças ao HMR do Vite)
7. Esteja pronto para explicar como esse componente simples será a base para construir nossa interface de monitoramento industrial mais complexa

---  

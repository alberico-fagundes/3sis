# 🔌 Passo 06: Consumo de API Externa (fetch)

No ecossistema de microsserviços do Nosso Dashboard (Smart Factory), o servidor Backend Node.js (Maestro) precisa se comunicar com APIs externas ou com a nossa UTI de Dados em Python. Usamos a função nativa `fetch()` com `async/await` para realizar requisições HTTP GET.

### 📌 O Conceito (Teoria Profunda)
A função `fetch()` envia uma requisição HTTP pela rede e retorna uma *Promise*. Em funções assíncronas (`async`), utilizamos o operador `await` para esperar a resposta da rede e, em seguida, outro `await` para converter o corpo da resposta em JSON (`resposta.json()`). Sempre envolvemos esse processo em um bloco `try...catch` para tratar eventuais erros de conexão.

### 📖 Sintaxe Básica (Exemplos Análogos)

**Como criar uma rota assíncrona que consome uma API externa:**
```javascript
app.get('/api/exemplo', async (req, res) => {
  try {
    // 1. Faz a requisição HTTP GET
    const resposta = await fetch('https://api.exemplo.com/dados');
    
    // 2. Converte a resposta em objeto JSON
    const dados = await resposta.json();
    
    // 3. Retorna os dados para o cliente React
    res.json(dados);
  } catch (erro) {
    res.status(500).json({ erro: "Falha ao consultar serviço externo" });
  }
});
```

---

### 💻 Mão na Massa (Desafio Ativo)

**Sua Tarefa Prática:**
1. Abra o arquivo `server.js` na pasta `backend`.
2. Crie uma nova rota `GET` no caminho `'/api/clima'`.
3. Defina a função handler como assíncrona adicionando a palavra-chave `async` antes de `(req, res)`.
4. Dentro do bloco `try`, faça um `await fetch()` para uma API pública de clima:
   `'https://api.open-meteo.com/v1/forecast?latitude=-25.4284&longitude=-49.2733&current_weather=true'`
5. Extraia o JSON da resposta usando `await resposta.json()`.
6. Envie o resultado para o cliente com `res.json(dados)`.
7. No bloco `catch`, imprima o erro no console e envie um status `500` com uma mensagem de erro em JSON.

**Teste:** No terminal, rode `node server.js` e acesse `http://localhost:3000/api/clima` no navegador. Você deverá ver as informações meteorológicas em formato JSON!

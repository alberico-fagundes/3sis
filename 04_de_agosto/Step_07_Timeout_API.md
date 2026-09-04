# ⏱️ Passo 07: Proteção contra Lenteza (Timeout)

Se uma API externa ou microsserviço demorar muito para responder, o nosso servidor Node.js pode ficar travado esperando indefinidamente. Para evitar isso, adicionamos um mecanismo de **Timeout**.

### 📌 O Conceito (Teoria Profunda)
O recurso `AbortController` do JavaScript nos permite cancelar requisições assíncronas programaticamente. Agendamos um temporizador (`setTimeout`) para acionar `controller.abort()` após um tempo limite (ex: 2 segundos). Se a resposta não chegar nesse prazo, a requisição é cancelada e dispara um erro do tipo `AbortError`, permitindo que o servidor responda rapidamente ao usuário em vez de travar.

### 📖 Sintaxe Básica (Exemplos Análogos)

**Como adicionar Timeout em um `fetch`:**
```javascript
// 1. Cria o controlador de cancelamento
const controller = new AbortController();

// 2. Agenda o abort para daqui a 2000 milissegundos (2 segundos)
const timeoutId = setTimeout(() => controller.abort(), 2000);

try {
  const resposta = await fetch('https://api.exemplo.com/lenta', {
    signal: controller.signal // Associa o sinal ao fetch
  });
  clearTimeout(timeoutId); // Limpa o timer se a resposta chegou a tempo
  const dados = await resposta.json();
  res.json(dados);
} catch (erro) {
  if (erro.name === 'AbortError') {
    res.status(504).json({ erro: "O serviço externo demorou muito para responder (Timeout)." });
  } else {
    res.status(500).json({ erro: "Erro de conexão." });
  }
}
```

---

### 💻 Mão na Massa (Desafio Ativo)

**Sua Tarefa Prática:**
1. Abra o arquivo `server.js` na pasta `backend`.
2. Crie uma rota `GET` no caminho `'/api/sensor-timeout'`.
3. Instancie um novo `AbortController`.
4. Defina um `setTimeout` de 2000ms para disparar `controller.abort()`.
5. Faça o `fetch` para a API informando `{ signal: controller.signal }` no segundo argumento.
6. Lembre-se de chamar `clearTimeout(timeoutId)` assim que o `fetch` for concluído com sucesso.
7. No bloco `catch`, verifique se `erro.name === 'AbortError'`. Se for, retorne status `504` (Gateway Timeout) com uma mensagem explicando o timeout.

**Teste:** Teste a rota no seu navegador (`http://localhost:3000/api/sensor-timeout`). Caso a API demore mais de 2 segundos, o servidor responderá com a mensagem de timeout em vez de ficar travado!

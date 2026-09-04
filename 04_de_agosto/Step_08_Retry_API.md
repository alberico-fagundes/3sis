# 🔄 Passo 08: Resiliência com Tentativas Novas (Retry)

Oscilações temporárias de rede podem fazer uma requisição falhar momentaneamente. A técnica de **Retry com Backoff Exponencial** permite que o servidor tente novamente antes de desistir e exibir um erro.

### 📌 O Conceito (Teoria Profunda)
Em vez de falhar na primeira tentativa, o sistema realiza um número limitado de novas tentativas (ex: 3 vezes). Para não sobrecarregar o serviço externo, aplicamos o **Backoff Exponencial**: aumentamos o tempo de espera entre cada tentativa (1s, 2s, 4s...). Isso dá tempo para que instabilidades de rede ou do servidor de destino se resolvam.

### 📖 Sintaxe Básica (Exemplos Análogos)

**1. Função auxiliar de pausa (delay):**
```javascript
const esperar = (ms) => new Promise(resolve => setTimeout(resolve, ms));
```

**2. Função de Fetch com Retry e Backoff Exponencial:**
```javascript
async function fetchComRetry(url, tentativas = 3, delay = 1000) {
  for (let i = 1; i <= tentativas; i++) {
    try {
      console.log(`Tentativa ${i} de ${tentativas}...`);
      const resposta = await fetch(url);
      if (resposta.ok) return await resposta.json();
      throw new Error(`Status da resposta: ${resposta.status}`);
    } catch (erro) {
      if (i === tentativas) throw erro; // Se for a última tentativa, lança o erro
      console.log(`Falhou. Aguardando ${delay}ms para tentar novamente...`);
      await esperar(delay);
      delay *= 2; // Dobra o tempo de espera (1s -> 2s -> 4s)
    }
  }
}
```

---

### 💻 Mão na Massa (Desafio Ativo)

**Sua Tarefa Prática:**
1. Abra o arquivo `server.js` na pasta `backend`.
2. Adicione as funções auxiliares `esperar` e `fetchComRetry` no topo do arquivo.
3. Crie uma rota `GET` no caminho `'/api/sensor-retry'`.
4. Dentro da rota, chame a função `fetchComRetry('https://api.open-meteo.com/v1/forecast?latitude=-25.4284&longitude=-49.2733&current_weather=true', 3, 1000)` dentro de um bloco `try...catch`.
5. Retorne os dados em formato JSON se a chamada for bem-sucedida.
6. Se todas as tentativas falharem, retorne status `503` (Service Unavailable) avisando que o serviço está temporariamente indisponível.

**Teste:** Abra `http://localhost:3000/api/sensor-retry` e acompanhe os logs de tentativas (`console.log`) no terminal do seu servidor Node.js!

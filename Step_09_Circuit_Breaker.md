# ⚡ Passo 09: Proteção contra Falhas em Cascata (Circuit Breaker)

Quando um microsserviço externo fica completamente fora do ar, continuar enviando requisições (mesmo com retry) consome recursos e prejudica todo o sistema. O padrão **Circuit Breaker (Disjuntor)** resolve esse problema.

### 📌 O Conceito (Teoria Profunda)
Inspirado nos disjuntores elétricos, o Circuit Breaker possui 3 estados:
* **FECHADO (CLOSED):** Operação normal. Todas as requisições passam.
* **ABERTO (OPEN):** Ocorreram muitas falhas seguidas. Novas chamadas são bloqueadas instantaneamente, retornando um erro rápido ou resposta alternativa (fallback).
* **MEIO-ABERTO (HALF-OPEN):** Após um tempo de espera, o disjuntor permite uma única chamada de teste para verificar se o serviço externo se recuperou.

### 📖 Sintaxe Básica (Exemplos Análogos)

**Classe CircuitBreaker simples:**
```javascript
class CircuitBreaker {
  constructor(limiteFalhas = 3, tempoEspera = 10000) {
    this.limiteFalhas = limiteFalhas;
    this.tempoEspera = tempoEspera;
    this.falhas = 0;
    this.estado = 'CLOSED'; // 'CLOSED', 'OPEN', 'HALF-OPEN'
    this.proximaTentativa = Date.now();
  }

  async executar(funcaoFetch) {
    if (this.estado === 'OPEN') {
      if (Date.now() > this.proximaTentativa) {
        this.estado = 'HALF-OPEN';
      } else {
        throw new Error("⚡ Disjuntor ABERTO! Chamada bloqueada para proteger o sistema.");
      }
    }

    try {
      const resultado = await funcaoFetch();
      this.falhas = 0;
      this.estado = 'CLOSED'; // Sucesso: reseta o disjuntor
      return resultado;
    } catch (erro) {
      this.falhas++;
      if (this.falhas >= this.limiteFalhas) {
        this.estado = 'OPEN';
        this.proximaTentativa = Date.now() + this.tempoEspera;
        console.log("⚡ Limite de falhas atingido. Disjuntor ABERTO por 10s!");
      }
      throw erro;
    }
  }
}
```

---

### 💻 Mão na Massa (Desafio Ativo)

**Sua Tarefa Prática:**
1. Abra o arquivo `server.js` na pasta `backend`.
2. Cole a classe `CircuitBreaker` no seu código.
3. Instancie o disjuntor fora das rotas:
   `const disjuntorSensor = new CircuitBreaker(3, 10000);`
4. Crie uma rota `GET` no caminho `'/api/sensor-resiliente'`.
5. Envolva a chamada da API com o disjuntor usando `disjuntorSensor.executar(() => fetch(...).then(r => r.json()))`.
6. No bloco `catch`, se o erro for do disjuntor aberto, retorne status `503` com uma mensagem amigável e dados padrão de emergência (fallback).

**Teste:** Acesse `http://localhost:3000/api/sensor-resiliente`. Se o serviço falhar consecutivamente, observe o disjuntor abrir e responder instantaneamente bloqueando novas tentativas!

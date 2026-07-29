# 🚀 MT-01 (Pre-Sequel) - A MÁQUINA DO TEMPO (GIT E GITHUB)
## Engenharia de Software ULTRA DIDÁTICA | SaaS Smart Academy Reborn

> **🎯 OBJETIVO EXTRAORDINÁRIO:** Antes de construirmos prédios (MT01) ou contratarmos Chefs (MT02), você precisa de um "Seguro de Vida". Vamos te ensinar a usar a **Máquina do Tempo** dos engenheiros de elite. Se você apagar um arquivo acidentalmente ou quebrar o código, aprenderemos a "voltar no tempo" com um clique e salvar tudo na nuvem militar do GitHub.

---

## 📚 1. O "SAVE GAME" DO PROGRAMADOR

Imagine que você está jogando um jogo dificílimo. Você passa pelo chefe da fase, mas não salva o jogo. Se a energia cair, você volta para a tela inicial e chora. 

Programar sem **Git** é exatamente isso. Se você cria um sistema que funciona na sexta-feira, mexe numa linha no sábado e tudo para de funcionar, você não consegue desfazer. O `Ctrl+Z` do Windows apaga quando você fecha o computador.

O **Git** é a solução para isso. É um programa invisível que tira uma "fotografia" do seu projeto e congela aquele momento no tempo.

---

## ☁️ 2. A DIFERENÇA: GIT vs GITHUB

Muitos leigos acham que são a mesma coisa. **NÃO SÃO!**

- 🐙 **O Git (O Motor):** É o programa que roda *offline* no seu computador. Ele é a câmera fotográfica.
- 🐈‍⬛ **O GitHub (A Nuvem):** É o álbum de fotos na internet (da Microsoft). Se o seu computador pegar fogo, o código inteiro da sua empresa está salvo nos servidores do GitHub.

---

## 🛠️ 3. O SEU CRACHÁ DE ENTRADA (SETUP INICIAL)

Se você não tem o Git instalado, baixe no site oficial (git-scm.com) e instale com "Next, Next, Finish". 
Se você não tem conta no GitHub, vá em `github.com` e crie uma conta (é de graça).

Depois, abra o terminal do VSCode e diga ao Git quem é você (O seu "Crachá"). Ele precisa saber quem tirou a fotografia do código. Rode estes dois comandos com seus dados:

*Para PCs pessoais pode usar:*
```bash
git config --global user.name "Zezinho da Silva"
git config --global user.email "zezinho@email.com"
```

*Para PCs compartilhados pode usar:*
```bash
git config  user.name "Zezinho da Silva"
git config s user.email "zezinho@email.com"
```

---

## 📸 4. O FLUXO DA VIDA REAL (COMO SALVAR)

Todo dia de trabalho na nossa "Smart Academy" terminará com um ritual de 3 comandos obrigatórios. Eles formam o coração do Versionamento de Código.

Abra o terminal na pasta do seu projeto e siga o fluxo:

### Passo 1: Ligar a Máquina do Tempo (`git init`)
Isso só se faz **uma vez na vida** do projeto. Diz ao Git para começar a monitorar a pasta.
```bash
git init
```

### Passo 2: Empacotar as mudanças (`git add .`)
Você pode ter modificado 50 arquivos. O `.` (ponto) significa: "Pegue absolutamente TUDO que eu alterei na pasta e coloque no palco para tirar a foto".
```bash
git add .
```

### Passo 3: Bater a Fotografia (`git commit`)
Aqui você tira a foto e cola uma etiqueta (mensagem) nela para saber o que você fez naquele dia.
```bash
git commit -m "Meu primeiro salvamento do projeto"
```
*(A partir desse milissegundo, o seu projeto está salvo no seu computador. Se você deletar um arquivo por engano agora, você consegue recuperar!)*

---

## 🚀 5. ENVIANDO PARA O GITHUB (A NUVEM)

Tirar fotos no seu computador não salva você de um raio queimar o seu HD. Precisamos enviar para o GitHub.

1. Acesse o **github.com**, clique no botão verde **"New"** (Novo Repositório).
2. Dê o nome de `smart_academy`, deixe como **Public** e clique em **Create repository**.
3. O GitHub vai te mostrar uma tela preta com alguns comandos. Copie as 3 últimas linhas que eles fornecem (se parecem com isso):

```bash
# Aponta a sua máquina para o servidor da Microsoft
git remote add origin https://github.com/SEU_NOME/smart_academy.git

# Define a esteira principal
git branch -M main

# Faz o Upload violento de todos os seus arquivos (Empurra pra Nuvem)
git push -u origin main
```

*Muitas vezes por causa de autenticação utilize o botão publicar branch no source control,
o Vs code ira perdir autenticação via navegador*

![alt text](image.png)

Vá no site do GitHub, aperte `F5` e sinta a mágica: O seu código está na nuvem. Você agora tem um portfólio de verdade.

---

## 🚨 6. A BÍBLIA DE ERROS (TROUBLESHOOTING GIT)

### 🐛 ERRO 1: Acesso Negado (Authentication Failed)
**O que acontece:** Quando você dá o `git push`, ele dá um erro gigante vermelho dizendo `fatal: Authentication failed`.
**A Causa:** O GitHub não deixa qualquer um enviar código para o seu repositório. Você precisa provar que é você. 
**A Solução Enterprise:** Uma janelinha vai abrir pedindo para você logar com o navegador (Sign in with browser). É só clicar nela, aprovar no site, e o código vai subir. Se você estiver no Linux e a tela não abrir, você precisará gerar um "Personal Access Token" (PAT) no site do GitHub e usá-lo como senha.

### 🐛 ERRO 2: O Desastre do Lixo na Nuvem (O Esquecimento)
**O que acontece:** O aluno vai lá no **MT02**, cria o `venv`, esquece de criar o arquivo `.gitignore`, e dá um `git add .`. O terminal trava, começa a carregar 50 mil arquivos do Python, e na hora de dar o `git push`, o GitHub vomita tudo e recusa.
**A Solução Enterprise:** O `.gitignore` é a placa de "PROIBIDA A ENTRADA". Ele DEVE ser criado antes do `git add .` se você tem arquivos inúteis na pasta. Se você já fez a besteira, tem que dar um comando de purgação (`git rm -r --cached venv/`), mas é doloroso. Faça o `.gitignore` sempre primeiro!

---

## 🎓 7. EXERCÍCIO DE ALTA PERFORMANCE (NÍVEL PLENO)

**Cenário:** Dois estagiários, o Zezinho e o Pedrinho, estão trabalhando no mesmo projeto, no mesmo repositório do GitHub. O Zezinho alterou a cor do botão na casa dele e deu `git push`. O Pedrinho alterou a fonte do texto na casa dele, deu `git push` no mesmo minuto, e tomou um erro massivo vermelho de "REJECTED".

**Pergunta:** Por que a máquina do Pedrinho foi rejeitada e qual o comando mágico para ele resolver a vida dele sem apagar código?

<details>
<summary>👀 Ver o Veredito do Arquiteto</summary>
<b>O Erro de Sincronia (Non-fast-forward)!</b><br>
O GitHub percebeu que o código que está na nuvem (o botão do Zezinho) é mais novo do que o código que o Pedrinho tem no computador. O GitHub bloqueia para proteger o sistema. <br>
<b>A Solução:</b> Antes de Empurrar (<code>Push</code>), você precisa Puxar (<code>Pull</code>). O Pedrinho roda <code>git pull</code>. O Git vai inteligentemente pegar a cor do botão do Zezinho da nuvem, misturar com a fonte do Pedrinho no computador local (Merge automático), e aí sim o Pedrinho poderá dar um <code>git push</code> com as duas coisas juntas. Trabalho em equipe garantido!
</details>

---

## 🏆 CHECKPOINT FINAL

O seu colete salva-vidas está vestido se:
1. [ ] Você sabe a diferença entre Git e GitHub.
2. [ ] Você rodou `git init` na pasta do seu projeto.
3. [ ] Você fez o fluxo `add`, `commit` e empurrou (`push`) pro GitHub com sucesso.

Tendo essa habilidade militar dominada, agora sim estamos autorizados a voltar para o **MT02** e **MT03**, criar nosso código sem medo e "Salvar o Jogo" ao final de cada dia de trabalho!

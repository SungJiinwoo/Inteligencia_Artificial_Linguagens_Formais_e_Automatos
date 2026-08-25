# Aula 03 - Gramáticas Formais e Hierarquia de Chomsky

Anotações da Unidade 2, escritas depois da aula.

Conteúdo:

1. De onde a aula partiu
2. Gramática formal - G = (V, T, P, S)
3. A notação mudou
4. Como ler uma regra de produção
5. Diferença entre → e ⇒
6. Derivação passo a passo
7. Como sei que a derivação terminou
8. Gramática regular
9. Gramática livre de contexto
10. Hierarquia de Chomsky
11. Roteiro para classificar uma gramática
12. Exemplos
13. Exercícios da aula
14. Revisão para prova

---

## 1. De onde a aula partiu

A professora começou retomando alfabeto, palavra e linguagem. O alfabeto do exemplo foi:

```
Σ = {a, b}
```

E uma linguagem possível com ele:

```
L = {a, ab, abb, abbb, ...}
```

Aí veio a pergunta que abre a unidade: como descrever formalmente quais palavras pertencem a uma
linguagem?

Anotei isso porque é o motivo da aula existir. Essa linguagem não acaba, então não dá pra escrever
todas as palavras dela numa folha. Preciso de um conjunto de regras que gere exatamente essas
palavras, e esse conjunto de regras é a gramática formal.

A linguagem é a lista de palavras. A gramática é a receita que faz essa lista. Quando a lista é
infinita, só sobra a receita.

---

## 2. Gramática formal - G = (V, T, P, S)

Uma gramática formal tem quatro partes, escritas sempre nessa ordem:

```
G = (V, T, P, S)
```

- V - variáveis, também chamadas de não terminais. São os símbolos que uso durante a geração.
- T - terminais. São os símbolos que ficam na palavra pronta.
- P - produções. São as regras que geram as palavras.
- S - símbolo inicial. É onde a derivação começa.

A gramática que ela usou de exemplo:

```
G = ({S}, {a, b}, P, S)

P:  S → aS
    S → b
```

Separando as partes: as variáveis são {S}, só tem uma. Os terminais são {a, b}. As produções são as
duas regras. E o símbolo inicial é o S.

A diferença entre variável e terminal, do jeito que entendi: variável é passageira, terminal é
definitivo. A variável é um lugar guardado que ainda vai ser trocado por outra coisa. O terminal já
é o produto final, depois que ele aparece ninguém mais mexe nele. Daí o nome, ele termina ali.

Escrevo variável em maiúscula e terminal em minúscula. Não é regra da matemática, é costume, mas
todo mundo usa e ajuda a bater o olho e saber o que é o quê.

---

## 3. A notação mudou

Na aula passada eu tinha anotado a gramática como G = (N, Σ, P, S). Nessa aula apareceu
G = (V, T, P, S). Não é contradição, são nomes diferentes para as mesmas quatro partes:

- N é o mesmo que V (não terminais / variáveis)
- Σ é o mesmo que T (terminais)
- P é P (produções)
- S é S (símbolo inicial)

Deixei isso anotado logo no começo porque na prova pode vir de qualquer um dos dois jeitos. O que
importa é reconhecer as quatro partes, não decorar a letra.

---

## 4. Como ler uma regra de produção

A regra:

```
S → aS
```

Lê-se "S produz aS", ou "S pode ser trocado por aS".

E a outra:

```
S → b
```

Lê-se "S produz b".

Então a seta, dentro de uma gramática, quer dizer "produz" ou "pode ser trocado por".

Do jeito que entendi, a produção é uma permissão de troca. Toda vez que eu vir um S na minha linha,
eu posso apagar esse S e escrever aS no lugar. E quando existe mais de uma regra para o mesmo S, eu
escolho qual usar. É essa escolha que faz a mesma gramática gerar palavras diferentes.

---

## 5. Diferença entre → e ⇒

Essa foi a anotação mais útil da aula, porque na Unidade 1 eu tinha usado a mesma seta para tudo.

- → é produção. Aparece na definição da gramática, dentro do P. Lê-se "produz".
- ⇒ é derivação. Aparece no passo a passo que eu escrevo. Lê-se "deriva em".

Ou seja:

```
S → aS     isso é a REGRA, faz parte da gramática
S ⇒ aS     isso é um PASSO, foi o que eu fiz agora
```

A comparação que montei: a produção é a receita escrita no livro, e a derivação é o movimento que eu
faço na cozinha. A receita fica parada e é sempre a mesma. O movimento acontece uma vez e vira o
passo seguinte.

Juntando com a aula passada, a seta → já apareceu com mais de um sentido: em lógica ela é
implicação (se... então), e em gramática ela é produção. No passo da derivação não se usa ela, e sim
a seta dupla.

---

## 6. Derivação passo a passo

Derivar é aplicar as regras uma de cada vez, sempre começando pelo símbolo inicial, até não sobrar
nenhuma variável. Usando a gramática da aula:

```
P:  S → aS
    S → b
```

Gerando a palavra aab:

```
Passo 1 - começo pelo símbolo inicial:      S
Passo 2 - aplico S → aS:                    S ⇒ aS
Passo 3 - ainda tem S, aplico de novo:      aS ⇒ aaS
Passo 4 - encerro com S → b:                aaS ⇒ aab
```

Derivação completa:

```
S ⇒ aS ⇒ aaS ⇒ aab
```

Olhando os passos, percebi que cada aplicação de S → aS faz duas coisas ao mesmo tempo: entra um a e
o S anda uma casa para a direita. O S funciona como uma setinha que vai andando e deixando a para
trás:

```
S
a S
a a S
a a b     troquei a setinha por b e ela sumiu
```

A regra S → b é o freio. Ela é a única que não devolve S nenhum, por isso é ela que encerra. Se a
gramática tivesse só S → aS, eu nunca conseguiria parar.

Daí o macete: toda gramática que gera palavra precisa de pelo menos uma regra de saída, uma que não
devolva variável. Sem ela a derivação não fecha nunca.

---

## 7. Como sei que a derivação terminou

Só tem um critério, e a professora bateu nele: a derivação termina quando não sobra nenhuma variável
na linha.

Testando:

- aaS - não terminou, ainda tem o S, que é variável.
- aab - terminou, a e b são terminais e não tem mais o que trocar.

Na prática eu bato o olho na linha e procuro maiúscula. Se achar, não acabou. Se só tiver minúscula,
acabou e aquilo é uma palavra de verdade da linguagem.

Erro que quero evitar na prova: entregar aaS como resposta. Isso não é palavra, é uma parada no meio
do caminho.

---

## 8. Gramática regular

Uma gramática é regular quando as regras dela seguem um formato bem apertado:

```
A → aB     um terminal, seguido de UMA variável
A → a      um terminal sozinho
```

Ou seja, do lado direito da seta pode ter no máximo uma variável, e ela tem que estar na pontinha.

A gramática que a gente vem usando encaixa nisso:

```
S → aS | b
```

Em S → aS o lado direito é o terminal a mais a variável S na ponta. Em S → b o lado direito é um
terminal sozinho. As duas passam, então a gramática é regular.

A linguagem que ela gera:

```
L(G) = {aⁿb | n ≥ 0} = {b, ab, aab, aaab, ...}
```

A imagem que criei: na gramática regular a variável fica sempre grudada na beirada, nunca no meio. A
palavra cresce só de um lado, tipo uma fila em que só dá pra entrar pelo fim.

---

## 9. Gramática livre de contexto

A gramática livre de contexto é mais solta. Ela cobra uma coisa só: do lado esquerdo da seta tem que
ter uma variável, sozinha. O lado direito pode ser o que for, em qualquer ordem e quantidade.

Exemplo da aula:

```
S → aSb | ε
```

Aqui o S do lado direito está no meio, com um terminal de cada lado. Isso já não cabe no formato
regular, mas cabe no de livre de contexto, porque do lado esquerdo continua tendo só o S sozinho.

Derivando:

```
S ⇒ aSb ⇒ aaSbb ⇒ aaaSbbb ⇒ aaabbb
```

O que acontece em cada passo: S → aSb coloca um a na esquerda e um b na direita ao mesmo tempo,
nunca um sem o outro. Por isso a quantidade de a e de b sai sempre igual:

```
L(G) = {aⁿbⁿ | n ≥ 0} = {ε, ab, aabb, aaabbb, ...}
```

O ε aqui é a regra de saída, é ela que apaga o S e fecha a derivação.

A imagem: a gramática livre de contexto cresce pelos dois lados ao mesmo tempo, de dentro para fora,
tipo um sanduíche montado em camadas. Colocar um a junto com um b é justamente o que a gramática
regular não consegue fazer.

O ponto que quero levar para a prova:

```
S → aS  | b       regular             a variável fica na PONTA
S → aSb | ε       livre de contexto   a variável fica no MEIO
```

Uma letra de diferença na regra, e a classe da gramática muda.

---

## 10. Hierarquia de Chomsky

Chomsky organizou as gramáticas em quatro tipos, numerados de 0 a 3. Quanto maior o número, mais
apertadas são as regras, ou seja, menos coisa elas deixam escrever.

- Tipo 3, regular - terminal seguido de no máximo uma variável, e ela na ponta.
- Tipo 2, livre de contexto - do lado esquerdo, uma variável sozinha.
- Tipo 1, sensível ao contexto - do lado esquerdo pode ter mais símbolos em volta da variável.
- Tipo 0, irrestrita - não tem exigência nenhuma de formato.

E os tipos ficam um dentro do outro:

```
Tipo 3  ⊂  Tipo 2  ⊂  Tipo 1  ⊂  Tipo 0
regular    livre      sensível   irrestrita
           de ctx     ao ctx
```

A consequência disso quase me pegou: se toda regular está dentro das livres de contexto, então toda
gramática regular também é livre de contexto. Ela obedece as duas definições ao mesmo tempo.

Então, quando a questão manda classificar, a resposta é a classe mais apertada em que ela cabe, ou
seja, o número mais alto. Se cabe em regular, respondo regular, mesmo sabendo que ela também é livre
de contexto.

A comparação que uso: todo quadrado é um retângulo. Se me perguntam que figura é essa, eu respondo
quadrado, que é a resposta mais certeira. Falar retângulo não está errado, mas diz menos.

Ao contrário não vale: S → aSb | ε é livre de contexto e não é regular, porque a variável está no
meio.

A aula fechou nos tipos 2 e 3, que são os que caem na atividade. Os tipos 1 e 0 ficaram só como
referência, para eu saber onde eles entram na escadinha.

---

## 11. Roteiro para classificar uma gramática

Montei esse passo a passo para não ficar chutando na prova:

```
1. Olho o LADO ESQUERDO de cada regra.
   Tem alguma regra com mais de um símbolo à esquerda?
      sim → não é livre de contexto nem regular
      não → é pelo menos livre de contexto, sigo

2. Olho o LADO DIREITO de TODAS as regras.
   Em todas elas a variável está na ponta (ou nem tem variável)?
      sim → REGULAR (tipo 3)
      não → LIVRE DE CONTEXTO (tipo 2)
```

O detalhe do passo 2 em que quase escorreguei: tem que valer para todas as regras. Basta uma regra
fora do formato regular para a gramática inteira deixar de ser regular. Não adianta a maioria estar
certa.

Testando o roteiro nas três gramáticas da aula:

- S → aS | b - passa no passo 1, e no passo 2 a variável está na ponta em todas. Regular.
- S → aSb | ε - passa no passo 1, mas no passo 2 a variável está no meio em aSb. Livre de contexto.
- S → aA e A → b - passa no passo 1, e no passo 2 aA tem a variável na ponta e b nem tem variável.
  Regular.

---

## 12. Exemplos

### Exemplo A - achando as quatro partes

```
G = ({S, A}, {0, 1}, P, S)

P:  S → 0A
    A → 1
```

As variáveis são {S, A}, os terminais são {0, 1}, as produções são as duas regras e o símbolo
inicial é o S.

Derivando:

```
S ⇒ 0A ⇒ 01
```

Detalhe interessante: essa gramática gera uma palavra só, 01. Nenhuma regra devolve o S ou o A para
a linha, então não tem como alongar. L(G) = {01}, uma linguagem que acaba.

### Exemplo B - as três gramáticas da aula lado a lado

```
S → aS  | b     regular             L = {aⁿb  | n ≥ 0}    b, ab, aab, aaab
S → 0S  | 1     regular             L = {0ⁿ1  | n ≥ 0}    1, 01, 001, 0001
S → aSb | ε     livre de contexto   L = {aⁿbⁿ | n ≥ 0}    ε, ab, aabb, aaabbb
```

As duas primeiras são a mesma ideia com símbolos trocados: empilha um símbolo e fecha com outro. A
terceira é a diferente, ela coloca dois símbolos por vez, um de cada lado.

---

## 13. Exercícios da aula

Os três blocos de fixação passados na aula estão resolvidos em
[Exercicios_Praticos_Aula3.md](Exercicios_Praticos_Aula3.md), com o enunciado de cada um e a
justificativa das respostas.

A Lista 1 da unidade está resolvida em [Lista1_Resolvida.md](Lista1_Resolvida.md).

---

## 14. Revisão para prova

O mínimo que quero ter na cabeça no dia:

```
G = (V, T, P, S)    gramática, quatro partes
V                   variáveis / não terminais, maiúsculas, são trocadas
T                   terminais, minúsculas, ficam na palavra
P                   produções, as regras
S                   símbolo inicial, onde a derivação começa
→                   produz (é a regra)
⇒                   deriva em (é o passo)
|                   ou, separa as alternativas de uma regra
L(G)                linguagem gerada pela gramática
```

Regular e livre de contexto, lado a lado:

```
S → aS  | b       regular (tipo 3)             variável na PONTA
S → aSb | ε       livre de contexto (tipo 2)   variável no MEIO
```

Os pontos onde eu mais escorrego:

1. Entregar aaS como resposta. Não é palavra, ainda tem variável.
2. Confundir a seta simples (a regra) com a seta dupla (o passo da derivação).
3. Responder livre de contexto numa gramática que é regular. A resposta é a classe mais apertada.
4. Achar que basta a maioria das regras ser regular. Tem que ser todas.
5. Esquecer que S → aSb coloca a e b em par, então em aⁿbⁿ sai sempre empatado.
6. Começar a derivação por outro símbolo que não seja o inicial.
7. Trocar o V pelo T na hora de listar as partes. Variável é a que some no fim.

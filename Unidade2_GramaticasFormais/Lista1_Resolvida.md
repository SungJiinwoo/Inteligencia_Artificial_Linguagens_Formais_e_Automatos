# Lista 1 — Resolvida

> Exercícios de Linguagens Formais, Alfabeto, Linguagens e Gramáticas.
> Resolvi todos os "exercícios para o estudante" da lista, um por um, **justificando cada
> resposta** — que é o que a professora pediu.

**Como fiz:** primeiro resolvi tudo com o gabarito fechado, escrevendo o raciocínio. Depois abri
pra conferir. Deixei a justificativa escrita mesmo nas questões que pareciam óbvias, porque na
prova é a justificativa que vale ponto — a resposta sozinha não mostra que eu entendi.

[⬅ voltar para o índice](../README.md) · [📓 notas da Aula 03](Notas_de_Aula.md)

---

## 📑 Sumário

- [1. Alfabeto](#1-alfabeto)
- [2. Palavras sobre um alfabeto](#2-palavras-sobre-um-alfabeto)
- [3. Pertinência de símbolos e palavras](#3-pertinência-de-símbolos-e-palavras)
- [4. Linguagem](#4-linguagem)
- [5. Descrevendo uma linguagem por padrão](#5-descrevendo-uma-linguagem-por-padrão)
- [6. Linguagem vazia e palavra vazia](#6-linguagem-vazia-e-palavra-vazia)
- [7. Estrutura de uma gramática](#7-estrutura-de-uma-gramática)
- [8. Como ler e aplicar uma produção](#8-como-ler-e-aplicar-uma-produção)
- [9. Derivação completa de uma palavra](#9-derivação-completa-de-uma-palavra)
- [10. Identificando palavras geradas por uma gramática](#10-identificando-palavras-geradas-por-uma-gramática)
- [🏁 Desafio final](#-desafio-final)
- [📊 O que eu errei / quase errei](#-o-que-eu-errei--quase-errei)

---

## 1. Alfabeto

**Enunciado:** considere `Σ = {a, b, c}` e responda.

### 1.1 Quantos símbolos existem no alfabeto?

**Resposta: 3 símbolos.**

**Justificativa:** basta contar os elementos listados dentro das chaves — `a`, `b` e `c`, que são
três. Vale lembrar que o alfabeto é, por definição, um conjunto **finito**, então essa contagem
sempre termina.

### 1.2 Quais são os símbolos?

**Resposta:**

```
a     b     c
```

**Justificativa:** são exatamente os elementos que aparecem dentro das chaves na definição de `Σ`.
Cada um é um símbolo **individual**, e não uma palavra.

### 1.3 O símbolo `a` pertence ao alfabeto?

**Resposta: sim.**

```
a ∈ Σ
```

**Justificativa:** `a` está listado dentro do conjunto `Σ = {a, b, c}`. Lê-se "a pertence a Sigma".

### 1.4 O símbolo `d` pertence ao alfabeto?

**Resposta: não.**

```
d ∉ Σ
```

**Justificativa:** `d` não aparece na lista `{a, b, c}`. Como o alfabeto é fechado no que foi
declarado, qualquer símbolo fora dessa lista não pertence a ele.

### 1.5 Escreva uma palavra formada por símbolos desse alfabeto

**Resposta:** `abc`

**Justificativa:** uma palavra é uma sequência finita de símbolos **do alfabeto**. Em `abc` os três
símbolos (`a`, `b`, `c`) pertencem a `Σ`, então a sequência é válida.

Outras respostas que também valeriam: `a`, `ab`, `cab`, `bbb`, `ccca`. Não precisa usar todos os
símbolos, nem usar cada um uma vez só — a única exigência é que **nenhum símbolo de fora** apareça.

---

## 2. Palavras sobre um alfabeto

**Enunciado:** considere `Σ = {0, 1}` e classifique cada sequência como palavra válida ou não
válida.

| Sequência | Válida? | Justificativa |
|:-:|:-:|---|
| `0101` | ✅ válida | todos os símbolos são `0` ou `1`, que estão em `Σ` |
| `00110` | ✅ válida | mesma coisa — só usa `0` e `1` |
| `012` | ❌ não válida | o símbolo `2` não pertence a `Σ`, e basta **um** símbolo de fora pra invalidar a sequência inteira |
| `111` | ✅ válida | `1 ∈ Σ`, e repetir o mesmo símbolo é permitido |
| `10a` | ❌ não válida | o símbolo `a` não pertence a `Σ = {0, 1}` |

**O raciocínio que usei nas cinco:** olhei cada sequência símbolo por símbolo e perguntei "esse
símbolo está em `Σ`?". Se todos estiverem, a sequência é palavra válida (está em `Σ*`). Se um
único não estiver, já reprova.

🧠 Detalhe que anotei: **repetição não é problema**. `111` é válida porque a exigência é sobre
**quais** símbolos aparecem, não sobre quantas vezes cada um aparece.

---

## 3. Pertinência de símbolos e palavras

**Enunciado:** considere `Σ = {0, 1}` e diga se cada afirmação é verdadeira ou falsa, justificando.

### 3.1 `0 ∈ Σ`

**Resposta: VERDADEIRO.**

**Justificativa:** `0` é um dos dois símbolos listados em `Σ = {0, 1}`.

### 3.2 `1 ∈ Σ`

**Resposta: VERDADEIRO.**

**Justificativa:** mesma coisa — `1` está na lista.

### 3.3 `01 ∈ Σ`

**Resposta: FALSO.**

**Justificativa:** essa é a pegadinha da questão. `01` tem **dois** símbolos, então é uma
**palavra**, não um símbolo individual. O conjunto `Σ` contém só símbolos avulsos (`0` e `1`), e
`01` não é um deles.

### 3.4 `01 ∈ Σ*`

**Resposta: VERDADEIRO.**

**Justificativa:** `Σ*` é o conjunto de **todas as palavras** que dá pra montar com os símbolos de
`Σ`. Como `0` e `1` pertencem ao alfabeto, a sequência `01` é uma palavra válida e está em `Σ*`.

⚠️ Comparando 3.3 com 3.4: **a mesma coisa (`01`) é falsa numa e verdadeira na outra**, e o que
mudou foi só a estrela. É por isso que essa dupla de questões existe:

| Afirmação | Valor | Porque `Σ` guarda... | e `Σ*` guarda... |
|:-:|:-:|---|---|
| `01 ∈ Σ` | falso | **símbolos** avulsos | — |
| `01 ∈ Σ*` | verdadeiro | — | **palavras** montadas com esses símbolos |

### 3.5 `2 ∈ Σ`

**Resposta: FALSO.**

**Justificativa:** `2` não aparece em `Σ = {0, 1}`. E vale notar: `2` também não está em `Σ*`, já
que nenhuma palavra sobre esse alfabeto pode conter um símbolo que não pertence a ele.

### 3.6 `101 ∈ Σ*`

**Resposta: VERDADEIRO.**

**Justificativa:** os três símbolos de `101` (`1`, `0`, `1`) pertencem a `Σ`, então é uma palavra
válida sobre esse alfabeto e está em `Σ*`.

---

## 4. Linguagem

**Enunciado:** considere `L = {0, 01, 011, 0111}` e determine se cada palavra pertence à linguagem.

| # | Afirmação | Resposta | Justificativa |
|:-:|:-:|:-:|---|
| 4.1 | `0 ∈ L` | ✅ sim | `0` está listado no conjunto |
| 4.2 | `01 ∈ L` | ✅ sim | `01` está listado no conjunto |
| 4.3 | `0111 ∈ L` | ✅ sim | `0111` está listado no conjunto |
| 4.4 | `10 ∈ L` | ❌ não | `10` não aparece na lista — a **ordem importa**, e aqui o `1` vem antes do `0` |
| 4.5 | `111 ∈ L` | ❌ não | `111` não está na lista; toda palavra dessa linguagem começa com `0`, e essa começa com `1` |
| 4.6 | `011 ∈ L` | ✅ sim | `011` está listado no conjunto |

**O raciocínio geral:** aqui a linguagem foi dada **por extensão** (listando as palavras uma a
uma). Então o teste é direto: a palavra está escrita ali dentro das chaves ou não está. Não tem
regra pra deduzir nada — é conferir na lista.

🧠 O que anotei do item 4.4: `10` usa exatamente os mesmos símbolos que `01`, mas **em outra
ordem** — e palavra é uma **sequência**, então ordem diferente é palavra diferente.

⚠️ E o item 4.5 tem uma armadilha que eu quase caí: `111` "parece" com `0111` porque tem os três
`1`. Mas falta o `0` da frente, e a palavra é o conjunto de símbolos **na ordem exata**. Não é
"parecido com" — ou é idêntica a um elemento da lista, ou não pertence.

---

## 5. Descrevendo uma linguagem por padrão

**Enunciado:** considere `L = {bⁿ | n ≥ 1}`.

### 5.1 Escreva as cinco primeiras palavras

**Resposta:**

```
b
bb
bbb
bbbb
bbbbb
```

**Justificativa:** a notação `bⁿ` significa `n` repetições do símbolo `b`, e a condição diz que
`n ≥ 1`. Então começo em `n = 1` e vou subindo:

| `n` | `bⁿ` | Palavra |
|:-:|:-:|:-:|
| 1 | `b¹` | `b` |
| 2 | `b²` | `bb` |
| 3 | `b³` | `bbb` |
| 4 | `b⁴` | `bbbb` |
| 5 | `b⁵` | `bbbbb` |

### 5.2 Explique o significado de `bⁿ`

**Resposta:** `bⁿ` quer dizer **`n` ocorrências seguidas do símbolo `b`**.

**Justificativa:** apesar de o desenho ser o mesmo da potência da matemática, aqui **não é
multiplicação** — é repetição de símbolo. `b³` não vale "b vezes b vezes b"; vale a palavra `bbb`,
de comprimento 3.

Vale também que `|bⁿ| = n`, ou seja, o expoente é exatamente o comprimento da palavra.

### 5.3 A palavra `bbbbbb` pertence à linguagem?

**Resposta: sim.**

**Justificativa:** contei os símbolos e são seis `b`, então `bbbbbb = b⁶`. Como `6 ≥ 1`, ela
satisfaz a condição do conjunto. Logo:

```
bbbbbb ∈ L
```

🧠 O que percebi: essa linguagem é **infinita**. Não importa quantos `b` eu escreva, sempre dá pra
colocar mais um — e é justamente por isso que ela foi descrita **por padrão** (com a regra `bⁿ`) e
não listando palavra por palavra, que seria impossível.

### 5.4 A palavra vazia (`ε`) pertence à linguagem?

**Resposta: não.**

```
ε ∉ L
```

**Justificativa:** `ε` é a palavra de comprimento zero, ou seja, corresponde a `b⁰` com `n = 0`.
Mas a condição do conjunto exige `n ≥ 1`, e `0` não é maior nem igual a 1. Então `ε` fica de fora.

⚠️ Anotação importante: se a condição fosse `n ≥ 0` em vez de `n ≥ 1`, a resposta viraria **sim**,
e o `ε` entraria na linguagem. Um número mudando na condição muda a linguagem inteira — dá pra
perder ponto fácil aqui se eu ler rápido demais.

---

## 6. Linguagem vazia e palavra vazia

**Enunciado:** explique com suas palavras a diferença entre `L = ∅` (A) e `L = {ε}` (B), e depois
responda às três perguntas.

### A diferença, do meu jeito

```
A)  L = ∅        →  uma caixa VAZIA
B)  L = {ε}      →  uma caixa com UMA FOLHA EM BRANCO dentro
```

**`L = ∅`** é a linguagem vazia: ela **não tem nenhuma palavra**. Se eu perguntar "quantas palavras
tem nessa linguagem?", a resposta é **zero**.

**`L = {ε}`** é uma linguagem que **tem uma palavra** — e essa palavra por acaso é a palavra vazia,
que não tem símbolo nenhum. Se eu perguntar "quantas palavras tem?", a resposta é **uma**.

A confusão acontece porque a palavra "vazia" aparece nos dois casos, mas se refere a coisas
diferentes: em A, o que está vazio é a **linguagem** (o conjunto); em B, o que está vazio é a
**palavra** (o conteúdo dela). E o conjunto de B **não** está vazio, porque tem um elemento dentro.

Portanto:

```
∅ ≠ {ε}
```

### 6.1 Qual delas possui uma palavra?

**Resposta: a B, `L = {ε}`.**

**Justificativa:** o conjunto tem exatamente um elemento listado dentro das chaves — o `ε`. Um
elemento = uma palavra.

### 6.2 Qual delas não possui nenhuma palavra?

**Resposta: a A, `L = ∅`.**

**Justificativa:** `∅` é a notação do conjunto vazio, que por definição não tem elemento nenhum.
Sem elementos, sem palavras.

### 6.3 Qual é o comprimento da palavra `ε`?

**Resposta: zero.**

```
|ε| = 0
```

**Justificativa:** comprimento é a **contagem de símbolos** da palavra, e `ε` não tem símbolo
algum. Contando zero símbolos, o comprimento é 0.

⚠️ Lembrete que já tinha anotado na unidade passada e vale repetir: **`ε` não é espaço em branco**.
Espaço seria um símbolo, e aí contaria no comprimento. `ε` é ausência total de símbolo.

---

## 7. Estrutura de uma gramática

**Enunciado:** considere `G = ({S, A}, {0, 1}, P, S)` com `P = {S → 0A, A → 1}`. Identifique os
componentes.

Antes de responder, encaixei os valores no formato `G = (V, T, P, S)`, que é a ordem em que os
componentes sempre aparecem:

```
G = ( {S, A} , {0, 1} , P , S )
        ↓         ↓      ↓   ↓
        V         T      P   S
```

### 7.1 O conjunto de variáveis

**Resposta:**

```
V = {S, A}
```

**Justificativa:** é o **primeiro** componente da quádrupla. Confere com a convenção: `S` e `A`
estão em maiúscula, e são exatamente os símbolos que aparecem do **lado esquerdo** das produções —
ou seja, os que ainda vão ser substituídos.

### 7.2 O conjunto de terminais

**Resposta:**

```
T = {0, 1}
```

**Justificativa:** é o **segundo** componente. São os símbolos que sobram na palavra final e que
nunca aparecem sozinhos do lado esquerdo de nenhuma produção — nenhuma regra diz "0 → alguma
coisa".

### 7.3 O conjunto de produções

**Resposta:**

```
P = {S → 0A,  A → 1}
```

**Justificativa:** são as duas regras dadas no enunciado. Lendo cada uma:

| Regra | Leitura |
|:-:|---|
| `S → 0A` | "S produz 0A", ou "S pode ser substituído por `0A`" |
| `A → 1` | "A produz 1" |

### 7.4 O símbolo inicial

**Resposta:**

```
S
```

**Justificativa:** é o **quarto** componente da quádrupla. É por ele que toda derivação começa — e
faz sentido, porque é o único que tem uma regra pra "abrir" a palavra.

### 7.5 Qual palavra pode ser gerada por essa gramática?

**Resposta:** `01`

**Justificativa:** derivei passo a passo, começando pelo símbolo inicial:

| Passo | Linha | Regra usada | Ainda tem variável? |
|:-:|:-:|---|:-:|
| início | `S` | — | sim (`S`) |
| 1 | `0A` | `S → 0A` | sim (`A`) |
| 2 | `01` | `A → 1` | não |

Derivação completa:

```
S ⇒ 0A ⇒ 01
```

A derivação terminou no passo 2 porque `0` e `1` são terminais e não sobrou nenhuma variável.

🧠 O que reparei além do que foi pedido: essa gramática gera **uma palavra só**. Não existe nenhuma
regra que devolva `S` ou `A` de volta pra linha, então não tem como alongar nem escolher caminho
diferente. Ou seja:

```
L(G) = {01}
```

É uma linguagem **finita**, com um elemento — bem diferente das gramáticas do exercício 8 em
diante, que têm regra recursiva e geram infinitas palavras.

---

## 8. Como ler e aplicar uma produção

**Enunciado:** considere `S → 0S`. Começando com `S`, aplique a regra uma, duas e três vezes, e
escreva a sequência completa.

### 8.1 Aplicando uma vez

```
S ⇒ 0S
```

**Justificativa:** troquei o `S` pelo lado direito da regra, que é `0S`.

### 8.2 Aplicando duas vezes

```
0S ⇒ 00S
```

**Justificativa:** a linha era `0S`. O `0` já é terminal e fica parado; o `S` que sobrou eu troquei
de novo por `0S`, o que deu `0` + `0S` = `00S`.

### 8.3 Aplicando três vezes

```
00S ⇒ 000S
```

**Justificativa:** mesma lógica — os dois `0` da frente ficam onde estão, e o `S` vira `0S` outra
vez.

### 8.4 Sequência completa

**Resposta:**

```
S ⇒ 0S ⇒ 00S ⇒ 000S
```

**Justificativa:** é a soma dos três passos acima, um atrás do outro. Cada aplicação da regra
acrescenta exatamente **um** `0` e devolve o `S` pro fim da linha.

### ⚠️ O ponto principal da questão

**A derivação NÃO terminou.**

**Justificativa:** a última linha é `000S`, e ali ainda tem o `S`, que é variável. Enquanto sobrar
variável, o que eu tenho na mão não é palavra — é uma etapa no meio do caminho.

E o detalhe que achei mais interessante: com **essa regra sozinha**, a derivação **nunca** vai
terminar. `S → 0S` sempre devolve um `S` novo, então não existe jeito de acabar. Pra fechar, a
gramática precisaria de uma segunda regra sem variável do lado direito — tipo `S → 1` (que é
exatamente o que aparece no exercício 10) ou `S → ε`.

🧠 Foi assim que entendi o papel da **regra de saída**: uma gramática precisa de pelo menos uma
regra que não devolva variável, senão ela não gera palavra nenhuma e a linguagem fica vazia.

---

## 9. Derivação completa de uma palavra

**Enunciado:** usando `G: S → aS | b`, gere `aaab` escrevendo todos os passos.

**Como planejei antes de escrever:** olhei a palavra alvo e contei — `aaab` tem **três `a`** e
**um `b` no fim**. Como `S → aS` coloca um `a` por vez e `S → b` é a regra que encerra, sei de
cara que preciso aplicar `S → aS` três vezes e `S → b` uma vez.

**Resposta:**

```
S ⇒ aS ⇒ aaS ⇒ aaaS ⇒ aaab
```

**Justificativa, passo a passo:**

| Passo | Linha | Regra usada | O que aconteceu |
|:-:|:-:|---|---|
| início | `S` | — | começo pelo símbolo inicial, como manda a definição |
| 1 | `aS` | `S → aS` | fixou o 1º `a` e devolveu o `S` |
| 2 | `aaS` | `S → aS` | fixou o 2º `a` e devolveu o `S` |
| 3 | `aaaS` | `S → aS` | fixou o 3º `a` e devolveu o `S` |
| 4 | `aaab` | `S → b` | trocou o `S` por `b` e encerrou |

**Por que a derivação terminou no passo 4:** porque `aaab` só tem terminais (`a` e `b`), e não
sobrou nenhuma variável pra substituir. Foi a regra `S → b` que fez isso — ela é a única das duas
que não devolve `S`.

Portanto:

```
aaab ∈ L(G)
```

🧠 A conta que guardei: **o número de `a` da palavra = o número de vezes que aplico `S → aS`**.
Se a questão pedisse `aaaaab` (cinco `a`), seriam cinco aplicações e depois o `S → b`. Isso
transforma o exercício numa contagem, e não em tentativa e erro.

---

## 10. Identificando palavras geradas por uma gramática

**Enunciado:** com `G: S → 0S | 1`, determine se cada palavra pode ser gerada. Para as que podem,
apresente a derivação completa.

**O padrão que identifiquei primeiro:** a regra `S → 0S` só sabe colocar `0`, e a regra `S → 1`
coloca um `1` e **encerra na hora**. Como é ela que encerra, todo caminho possível é: alguns `0`,
e um `1` no fim. Ou seja:

```
L(G) = {0ⁿ1 | n ≥ 0}
```

Com esse padrão na mão, dá pra responder as seis olhando o formato da palavra. Mas escrevi a
derivação de cada uma que dá pra gerar, como o enunciado pediu.

### 10.1 `1`

**Resposta: SIM, pode ser gerada.**

```
S ⇒ 1
```

**Justificativa:** aplico direto `S → 1`, sem passar por `S → 0S` nenhuma vez. É o caso `n = 0` do
padrão — zero `0` e um `1`. A derivação termina de imediato porque `1` é terminal.

### 10.2 `01`

**Resposta: SIM, pode ser gerada.**

```
S ⇒ 0S ⇒ 01
```

**Justificativa:** uma aplicação de `S → 0S` (que coloca o `0`) e depois `S → 1` pra fechar.

### 10.3 `001`

**Resposta: SIM, pode ser gerada.**

```
S ⇒ 0S ⇒ 00S ⇒ 001
```

**Justificativa:** duas aplicações de `S → 0S` (um `0` cada) e depois `S → 1`.

### 10.4 `0001`

**Resposta: SIM, pode ser gerada.**

```
S ⇒ 0S ⇒ 00S ⇒ 000S ⇒ 0001
```

**Justificativa:** três aplicações de `S → 0S` e depois `S → 1`. Mesma lógica das anteriores — a
quantidade de `0` da palavra é a quantidade de vezes que aplico a primeira regra.

### 10.5 `101`

**Resposta: NÃO pode ser gerada.**

**Justificativa:** a palavra começa com `1`. Pra produzir um `1`, a única regra disponível é
`S → 1` — e ela **elimina o `S`**, ou seja, encerra a derivação naquele ponto.

Testando o caminho: se eu começo aplicando `S → 1`, a linha vira `1` e acabou. Não sobrou nenhuma
variável, então não tenho como produzir o `0` e o `1` que vêm depois. A única outra opção seria
começar com `S → 0S`, mas aí a palavra começaria com `0`, e não com `1`.

Concluindo: **depois que o `1` aparece, nada mais pode ser escrito**. Como `101` tem símbolos
depois do primeiro `1`, ela não pertence a `L(G)`.

```
101 ∉ L(G)
```

### 10.6 `1001`

**Resposta: NÃO pode ser gerada.**

**Justificativa:** é o mesmo problema do item anterior, e por dois motivos:

1. a palavra **começa** com `1`, e a regra que produz `1` encerra a derivação — então nada poderia
   vir depois dele;
2. ela tem **dois** `1`, e a gramática só produz um `1` por palavra (o `1` é justamente o que
   encerra, então não tem como produzir um segundo).

O formato exigido pelo padrão `0ⁿ1` é: **zero ou mais `0`, e exatamente um `1` no fim**. `1001` não
se encaixa nem no começo nem na contagem de `1`.

```
1001 ∉ L(G)
```

### Resumo das seis

| # | Palavra | Gerada? | Motivo curto |
|:-:|:-:|:-:|---|
| 10.1 | `1` | ✅ sim | `n = 0` — só a regra de saída |
| 10.2 | `01` | ✅ sim | um `0` + `1` final |
| 10.3 | `001` | ✅ sim | dois `0` + `1` final |
| 10.4 | `0001` | ✅ sim | três `0` + `1` final |
| 10.5 | `101` | ❌ não | tem símbolo **depois** do `1`, que encerra |
| 10.6 | `1001` | ❌ não | começa com `1` **e** tem dois `1` |

---

## 🏁 Desafio final

**Enunciado:** considere `G: S → aS | b` e responda sem consultar o gabarito.

**O padrão, antes de começar:** é a mesma estrutura do exercício 10, só trocando os símbolos —
`S → aS` empilha `a` e `S → b` encerra com um `b`. Então:

```
L(G) = {aⁿb | n ≥ 0}
```

### 1. A palavra `b` pode ser gerada?

**Resposta: SIM.**

```
S ⇒ b
```

**Justificativa:** aplico `S → b` direto, sem usar `S → aS` nenhuma vez. É o caso `n = 0` — zero
`a` e um `b`. Como `b` é terminal, a derivação já termina aí.

### 2. A palavra `ab` pode ser gerada?

**Resposta: SIM.**

```
S ⇒ aS ⇒ ab
```

**Justificativa:** uma aplicação de `S → aS` coloca o `a` e devolve o `S`; depois `S → b` fecha.

### 3. A palavra `aab` pode ser gerada?

**Resposta: SIM.**

```
S ⇒ aS ⇒ aaS ⇒ aab
```

**Justificativa:** duas aplicações de `S → aS` (um `a` cada) e depois `S → b`.

### 4. A palavra `aaab` pode ser gerada?

**Resposta: SIM.**

```
S ⇒ aS ⇒ aaS ⇒ aaaS ⇒ aaab
```

**Justificativa:** três aplicações de `S → aS` e depois `S → b`. É a mesma derivação do exercício 9.

### 5. A palavra `aba` pode ser gerada?

**Resposta: NÃO.**

**Justificativa:** o problema está no `a` que vem **depois** do `b`.

A única regra que produz `b` é `S → b`, e ela **elimina o `S`** — ou seja, encerra a derivação
naquele exato momento. Depois que o `b` sai, não existe mais variável na linha, então não há como
escrever mais nada.

Testando o caminho na mão:

```
S ⇒ aS ⇒ ab      ← aqui já acabou, não tem mais S pra produzir o último a
```

Cheguei em `ab` e travei. Não existe nenhuma regra do tipo `b → alguma coisa`, porque `b` é
terminal, e terminal não se substitui.

Outro jeito de justificar, pelo padrão: em `L(G) = {aⁿb}` o `b` está **obrigatoriamente na última
posição**. Em `aba` o `b` está no meio, então ela não se encaixa no formato.

```
aba ∉ L(G)
```

### 6. Escreva a derivação completa de `aaaab`

**Resposta:**

```
S ⇒ aS ⇒ aaS ⇒ aaaS ⇒ aaaaS ⇒ aaaab
```

**Justificativa:** a palavra tem **quatro `a`**, então aplico `S → aS` quatro vezes e fecho com
`S → b`:

| Passo | Linha | Regra usada |
|:-:|:-:|---|
| início | `S` | — |
| 1 | `aS` | `S → aS` |
| 2 | `aaS` | `S → aS` |
| 3 | `aaaS` | `S → aS` |
| 4 | `aaaaS` | `S → aS` |
| 5 | `aaaab` | `S → b` |

Terminou no passo 5 porque não sobrou nenhuma variável na linha.

### 7. Descreva com suas palavras o padrão das palavras geradas

**Resposta:** toda palavra dessa gramática é formada por **uma sequência de `a` (que pode ser
nenhum), seguida de exatamente um `b` no final**.

```
L(G) = {aⁿb | n ≥ 0} = {b, ab, aab, aaab, aaaab, ...}
```

**Justificativa:** olhando o que cada regra faz:

- **`S → aS`** — acrescenta **um** `a` e devolve o `S` pro fim da linha. Posso repetir quantas
  vezes quiser (inclusive zero), e é isso que faz a quantidade de `a` ser livre;
- **`S → b`** — acrescenta o `b` e **não devolve** `S` nenhum. Como é a única regra que encerra,
  toda derivação obrigatoriamente passa por ela **uma única vez, no fim**.

Daí saem as três características do padrão:

| Característica | De onde vem |
|---|---|
| os `a` vêm todos antes | `S → aS` sempre escreve o `a` **à esquerda** do `S` |
| tem exatamente **um** `b` | `S → b` é usada uma vez só, porque encerra a derivação |
| o `b` está **no fim** | é o último símbolo escrito, já que depois dele não sobra variável |

🧠 O jeito que eu explicaria em voz alta: o `S` é um cursor que anda pra direita deixando `a` pra
trás; e o `b` é o ponto final que apaga o cursor. Por isso todo `a` vem antes e o `b` fecha a
palavra.

⚠️ E o caso `n = 0` é o que mais escapa: `b` sozinho **pertence** à linguagem, porque nada obriga a
usar `S → aS` pelo menos uma vez. A menor palavra dessa gramática é `b`, não `ab`.

---

## 📊 O que eu errei / quase errei

Deixo isso aqui pra reler na véspera da prova — são os pontos onde eu titubeei resolvendo:

| # | Onde | O que quase fiz de errado | O certo |
|:-:|---|---|---|
| 1 | Ex. 3.3 e 3.4 | responder a mesma coisa nas duas | `01 ∈ Σ` é **falso** (é palavra, não símbolo), mas `01 ∈ Σ*` é **verdadeiro** |
| 2 | Ex. 4.5 | aceitar `111` porque "parece" com `0111` | palavra é a sequência **exata**; falta o `0` da frente |
| 3 | Ex. 5.4 | dizer que `ε` pertence a `{bⁿ \| n ≥ 1}` | a condição é `n ≥ 1`, e `ε` seria `n = 0` |
| 4 | Ex. 6 | achar que `∅` e `{ε}` são a mesma coisa | `∅` tem **zero** palavras; `{ε}` tem **uma** |
| 5 | Ex. 8 | dizer que a derivação terminou em `000S` | sobrou variável, então não é palavra |
| 6 | Ex. 10.5 | tentar gerar `101` "voltando" depois do `1` | a regra que produz `1` encerra a derivação |
| 7 | Desafio 7 | esquecer o caso `n = 0` | `b` sozinho pertence à linguagem |

E os três hábitos que quero manter na hora da prova:

1. **contar antes de derivar** — a quantidade de símbolos da palavra alvo já diz quantas vezes
   aplicar cada regra;
2. **procurar maiúscula na linha final** — se tiver, não terminou e aquilo não é resposta;
3. **descobrir o padrão da linguagem primeiro** — com o `L(G)` na mão, responder "pertence ou não"
   vira conferência, não tentativa e erro.

---

<p align="center">
  <a href="../README.md">⬅ voltar para o índice</a> ·
  <a href="Notas_de_Aula.md">📓 notas da Aula 03</a>
</p>

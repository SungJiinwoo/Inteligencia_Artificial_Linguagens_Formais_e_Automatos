# Aula 03 — Notas de Aula: Gramáticas Formais e Hierarquia de Chomsky

> Anotações da Unidade 2, escritas do meu jeito depois da aula.
> Segue o mesmo formato da unidade passada: sumário, objetivos, conteúdo, exemplos, exercícios e
> revisão para prova.

[⬅ voltar para o índice](../README.md)

---

## 📑 Sumário

- [🎯 Objetivos](#-objetivos)
- [1. De onde a aula partiu](#1-de-onde-a-aula-partiu)
- [2. Gramática formal — G = (V, T, P, S)](#2-gramática-formal--g--v-t-p-s)
- [3. A notação mudou (e não é erro)](#3-a-notação-mudou-e-não-é-erro)
- [4. Como ler uma regra de produção](#4-como-ler-uma-regra-de-produção)
- [5. → e ⇒ não são a mesma coisa](#5--e--não-são-a-mesma-coisa)
- [6. Derivação passo a passo](#6-derivação-passo-a-passo)
- [7. Como sei que a derivação terminou](#7-como-sei-que-a-derivação-terminou)
- [8. Gramática Regular](#8-gramática-regular)
- [9. Gramática Livre de Contexto](#9-gramática-livre-de-contexto)
- [10. Hierarquia de Chomsky](#10-hierarquia-de-chomsky)
- [11. Roteiro pra classificar uma gramática](#11-roteiro-pra-classificar-uma-gramática)
- [12. Exemplos resolvidos](#12-exemplos-resolvidos)
- [13. Exercícios](#13-exercícios)
- [14. Revisão para prova](#14-revisão-para-prova)
- [15. Mapa mental](#15--mapa-mental)
- [📌 Checklist](#-checklist)

---

## 🎯 Objetivos

Como sempre, transformei os objetivos da aula em perguntas. Se eu respondo todas sem consultar,
fechei a aula:

- O que é uma gramática formal?
- Quais são os componentes de uma gramática e pra que serve cada um?
- Como se lê e como se aplica uma regra de produção?
- Como fazer uma derivação passo a passo?
- Qual a diferença entre gramática regular e gramática livre de contexto?
- O que é a Hierarquia de Chomsky?
- Como classificar uma gramática olhando só para as regras dela?
- Como montar uma gramática regular e uma livre de contexto do zero?

---

## 1. De onde a aula partiu

A professora começou retomando o que já tínhamos visto: alfabeto, palavra e linguagem. O alfabeto
do exemplo foi:

```
Σ = {a, b}
```

E uma linguagem possível com ele:

```
L = {a, ab, abb, abbb, ...}
```

Aí veio a pergunta que abre a unidade inteira:

> **Como descrever formalmente quais palavras pertencem a uma linguagem?**

Anotei isso porque é o motivo de existir a aula. Essa linguagem aí de cima é **infinita** — não
tenho como escrever todas as palavras dela numa folha. Preciso de outra coisa: um conjunto de
regras que gere exatamente essas palavras. Essa coisa é a **gramática formal**.

🧠 O jeito que fixei: a linguagem é a **lista** de palavras; a gramática é a **receita** que produz
essa lista. Quando a lista é infinita, só sobra a receita.

---

## 2. Gramática formal — G = (V, T, P, S)

Uma gramática formal é uma quádrupla:

```
G = (V, T, P, S)
```

| Símbolo | Nome | Função |
|:-:|---|---|
| `V` | Variáveis ou não terminais | símbolos auxiliares usados **durante** a geração |
| `T` | Terminais | símbolos que aparecem na palavra **final** |
| `P` | Produções | as regras que geram as palavras |
| `S` | Símbolo inicial | onde a derivação **começa** |

A gramática que ela usou de exemplo na aula:

```
G = ({S}, {a, b}, P, S)

P:  S → aS
    S → b
```

Destrinchando:

| Parte | Valor | Leitura |
|---|:-:|---|
| Variáveis | `{S}` | só tem uma variável, o próprio `S` |
| Terminais | `{a, b}` | são os símbolos que sobram no fim |
| Produções | `S → aS` e `S → b` | duas regras |
| Símbolo inicial | `S` | toda derivação parte daqui |

🧠 O que anotei sobre a diferença entre `V` e `T`: **variável é temporária, terminal é definitivo**.
A variável é um lugar reservado que ainda vai ser trocado por outra coisa. O terminal já é o
produto final — depois que ele aparece, ninguém mais mexe nele. Por isso o nome: ele **termina** ali.

Escrevo variável em **maiúscula** e terminal em **minúscula**. Não é regra da matemática, é
convenção — mas todo mundo usa, e ajuda muito a bater o olho e saber o que é o quê.

---

## 3. A notação mudou (e não é erro)

Uma coisa que me confundiu por uns minutos: na aula passada eu tinha anotado a gramática assim:

```
G = (N, Σ, P, S)
```

E nessa aula apareceu:

```
G = (V, T, P, S)
```

Não é contradição — são **nomes diferentes pras mesmas quatro partes**:

| Aula 02 | Aula 03 | É o quê |
|:-:|:-:|---|
| `N` | `V` | não terminais / variáveis |
| `Σ` | `T` | terminais |
| `P` | `P` | produções |
| `S` | `S` | símbolo inicial |

⚠️ Deixei isso anotado aqui em cima porque na prova pode vir de qualquer um dos dois jeitos. O que
importa é reconhecer as quatro partes, não decorar a letra.

---

## 4. Como ler uma regra de produção

Pegando a regra:

```
S → aS
```

Lê-se:

> **"S produz aS"**

ou:

> **"S pode ser substituído por aS."**

E a outra:

```
S → b
```

> **"S produz b."**

Então o símbolo `→`, dentro de uma gramática, significa:

> **"produz"** / **"pode ser substituído por"**

### O que a regra realmente autoriza

O jeito que entendi: a produção é uma **permissão de troca**. Sempre que eu enxergar um `S` na
minha linha, tenho o direito (não a obrigação) de apagar esse `S` e escrever `aS` no lugar. Só isso.

E quando existe mais de uma regra pro mesmo `S`, eu **escolho** qual usar. É essa escolha que faz
a mesma gramática gerar palavras diferentes.

---

## 5. → e ⇒ não são a mesma coisa

Essa foi a anotação mais útil da aula pra mim, porque na Unidade 1 eu tinha usado `→` pra tudo:

| Símbolo | Nome | Onde aparece | Leitura |
|:-:|---|---|---|
| `→` | produção | na **definição** da gramática (dentro de `P`) | "produz" / "pode virar" |
| `⇒` | derivação | no **passo a passo** que eu escrevo | "deriva em" / "virou" |

Ou seja:

```
S → aS        ← isso é a REGRA, faz parte da gramática
S ⇒ aS        ← isso é um PASSO, foi o que eu fiz agora
```

🧠 A analogia que montei: `→` é a **receita** escrita no livro; `⇒` é o **movimento** que eu faço na
cozinha. A receita fica lá parada e é sempre a mesma; o movimento acontece uma vez e vira o passo
seguinte.

E somando com a aula passada, esse desenho `→` já apareceu com mais de um sentido:

| Contexto | Significa |
|---|---|
| Lógica | implica / se... então |
| Gramática (dentro de `P`) | produz |
| Passo da derivação | aí não se usa `→`, e sim `⇒` |

---

## 6. Derivação passo a passo

**Derivar** é aplicar as regras uma de cada vez, sempre partindo do símbolo inicial, até não sobrar
nenhuma variável. Com a gramática da aula:

```
G = ({S}, {a, b}, P, S)

P:  S → aS
    S → b
```

### Gerando a palavra `aab`

**Passo 1 — começo pelo símbolo inicial:**

```
S
```

**Passo 2 — aplico `S → aS`:**

```
S ⇒ aS
```

**Passo 3 — ainda tem `S`, aplico `S → aS` de novo:**

```
aS ⇒ aaS
```

**Passo 4 — agora encerro com `S → b`:**

```
aaS ⇒ aab
```

Derivação completa:

```
S ⇒ aS ⇒ aaS ⇒ aab
```

Palavra gerada:

```
aab
```

### O que percebi olhando os passos

Cada aplicação de `S → aS` faz duas coisas ao mesmo tempo: **fixa um `a`** e **empurra o `S` uma
casa pra direita**. O `S` funciona como um cursor que vai andando e deixando `a` pra trás:

```
S
a S
a a S
a a b     ← troquei o cursor por b e ele sumiu
```

E a regra `S → b` é o **freio**. Ela é a única que não devolve `S` nenhum — por isso é ela que
encerra. Se a gramática tivesse só `S → aS`, eu nunca conseguiria parar.

🧠 O macete que guardei: **toda gramática que gera palavra precisa de pelo menos uma regra de
saída** — uma que não devolva variável nenhuma. Sem ela a derivação nunca fecha.

---

## 7. Como sei que a derivação terminou

Critério único, e a professora bateu nele:

> **A derivação termina quando não sobra nenhuma variável (nenhum não terminal) na linha.**

Testando:

| Linha | Terminou? | Por quê |
|:-:|:-:|---|
| `aaS` | ❌ não | ainda tem o `S`, que é variável |
| `aab` | ✅ sim | `a` e `b` são terminais, não tem mais o que substituir |

Como eu uso isso na prática: bato o olho na linha e procuro **maiúscula**. Achou maiúscula, não
acabou. Só minúscula, acabou — e aquilo é uma palavra de verdade da linguagem.

⚠️ Erro que quero evitar na prova: entregar `aaS` como resposta. Isso **não é palavra**, é uma
etapa no meio do caminho. Palavra é só o que sobra quando as variáveis acabaram.

---

## 8. Gramática Regular

Agora entra a parte de classificar. Uma gramática é **regular** quando as produções seguem um
formato bem restrito:

```
A → aB          um terminal, seguido de UMA variável
A → a           um terminal sozinho
```

Ou seja, do lado direito da seta pode haver **no máximo uma variável, e ela tem que estar na
ponta**.

Exemplo — a própria gramática que a gente vem usando:

```
S → aS | b
```

| Regra | Lado direito | Encaixa? |
|:-:|---|:-:|
| `S → aS` | terminal `a` + variável `S` na ponta | ✅ |
| `S → b` | terminal sozinho | ✅ |

Então essa gramática é **regular**.

A linguagem que ela gera:

```
L(G) = {aⁿb | n ≥ 0} = {b, ab, aab, aaab, ...}
```

🧠 A imagem que criei: na gramática regular a variável fica sempre **grudada na borda**, nunca no
meio. A palavra cresce só de um lado, como uma fila em que só dá pra entrar pelo fim.

---

## 9. Gramática Livre de Contexto

A gramática **livre de contexto** (GLC) é mais solta. A exigência é só uma:

> **do lado esquerdo da seta tem que haver exatamente uma variável, sozinha.**

O lado direito pode ser o que for — terminais, variáveis, misturado, em qualquer ordem e em
qualquer quantidade.

Exemplo da aula:

```
S → aSb | ε
```

Repara: aqui o `S` do lado direito está **no meio**, com um terminal de cada lado. Isso já não cabe
no formato regular — mas cabe no de GLC, porque à esquerda continua tendo só o `S` sozinho.

### Derivando com ela

```
S ⇒ aSb ⇒ aaSbb ⇒ aaaSbbb ⇒ aaabbb
```

O que acontece em cada passo: `S → aSb` coloca **um `a` na esquerda e um `b` na direita ao mesmo
tempo**. Nunca um sem o outro. Por isso a quantidade de `a` e de `b` sai sempre igual:

```
L(G) = {aⁿbⁿ | n ≥ 0} = {ε, ab, aabb, aaabbb, ...}
```

E o `ε` aqui é a regra de saída — é ela que apaga o `S` e fecha a derivação.

🧠 A imagem: a GLC cresce **pelos dois lados ao mesmo tempo**, de dentro pra fora, como um sanduíche
montado em camadas. Essa capacidade de casar um `a` com um `b` é exatamente o que a gramática
regular **não** consegue fazer.

### O ponto que quero levar pra prova

```
S → aS  | b       regular      → a variável fica na PONTA
S → aSb | ε       livre de ctx → a variável fica no MEIO
```

Uma letra de diferença na regra, e a classe da gramática muda.

---

## 10. Hierarquia de Chomsky

Chomsky organizou as gramáticas em **quatro tipos**, numerados de 0 a 3. Quanto **maior** o número,
mais **restritas** são as regras:

| Tipo | Nome | Como são as regras |
|:-:|---|---|
| 3 | Regular | terminal seguido de no máximo uma variável, e ela na ponta |
| 2 | Livre de contexto | lado esquerdo com **uma** variável sozinha |
| 1 | Sensível ao contexto | lado esquerdo pode ter mais símbolos em volta da variável |
| 0 | Irrestrita | sem restrição de formato |

E os tipos ficam **encaixados um dentro do outro**:

```
Tipo 3  ⊂  Tipo 2  ⊂  Tipo 1  ⊂  Tipo 0
regular    livre      sensível   irrestrita
           de ctx     ao ctx
```

### A consequência disso que quase me pegou

Se toda regular está dentro das livres de contexto, então **toda gramática regular também é livre
de contexto**. Ela satisfaz as duas definições ao mesmo tempo.

Então, quando a questão manda classificar, a resposta esperada é a **classe mais restrita em que
ela cabe** — o número mais alto. Se cabe em regular, respondo regular, mesmo sabendo que
tecnicamente ela também é livre de contexto.

🧠 A analogia: todo quadrado é um retângulo. Se me perguntam "que figura é essa?", respondo
**quadrado**, que é a resposta mais precisa — não "retângulo", que também é verdade mas diz menos.

⚠️ E o contrário **não** vale: `S → aSb | ε` é livre de contexto e **não** é regular, porque a
variável está no meio.

A aula fechou nos tipos 2 e 3, que são os que caem na atividade. Os tipos 1 e 0 ficaram como
referência, só pra eu saber onde eles se encaixam na escada.

---

## 11. Roteiro pra classificar uma gramática

Montei esse passo a passo pra não ficar no chute na hora da prova:

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

⚠️ O detalhe do passo 2 em que eu quase escorreguei: tem que valer pra **todas** as regras. Basta
**uma** regra fora do formato regular pra gramática inteira deixar de ser regular. Não é maioria,
é unanimidade.

Testando o roteiro:

| Gramática | Passo 1 | Passo 2 | Classificação |
|---|:-:|:-:|:-:|
| `S → aS \| b` | ok | variável na ponta em todas | **Regular** |
| `S → aSb \| ε` | ok | variável no meio em `aSb` | **Livre de contexto** |
| `S → aA`, `A → b` | ok | `aA` tem a variável na ponta, `b` não tem variável | **Regular** |

---

## 12. Exemplos resolvidos

Montei mais alguns casos pra treinar antes de ir pros exercícios.

### Exemplo A — identificando as quatro partes

```
G = ({S, A}, {0, 1}, P, S)

P:  S → 0A
    A → 1
```

| Parte | Valor |
|---|:-:|
| Variáveis `V` | `{S, A}` |
| Terminais `T` | `{0, 1}` |
| Produções `P` | `S → 0A`, `A → 1` |
| Símbolo inicial | `S` |

Derivando:

```
S ⇒ 0A ⇒ 01
```

Detalhe interessante: essa gramática gera **uma palavra só**, `01`. Não tem nenhuma regra que
devolva o `S` ou o `A`, então não existe como alongar. `L(G) = {01}`, uma linguagem finita.

### Exemplo B — a mesma ideia, com a variável do outro lado

E se em vez de `S → aS | b` fosse `S → Sa | b`?

```
S ⇒ Sa ⇒ Saa ⇒ baa
```

A variável `S` continua na ponta — só que na ponta **esquerda** agora. O que muda é a linguagem
gerada:

```
S → aS | b   →   L(G) = {aⁿb | n ≥ 0}   (o b fica no fim)
S → Sa | b   →   L(G) = {baⁿ | n ≥ 0}   (o b fica no começo)
```

### Exemplo C — por que `aSb` não dá pra imitar com regra regular

Tentei gerar `aabb` usando só o formato regular e não consegui. O motivo que anotei: pra garantir a
mesma quantidade dos dois lados, eu precisaria "lembrar" quantos `a` já coloquei na hora de colocar
os `b`. A regra regular escreve um símbolo e passa adiante, sem guardar essa conta. Já `S → aSb`
resolve isso escrevendo os dois de uma vez, então nem precisa lembrar de nada.

### Exemplo D — comparando as linguagens lado a lado

| Gramática | Classe | `L(G)` | Primeiras palavras |
|---|:-:|:-:|---|
| `S → aS \| b` | regular | `{aⁿb \| n ≥ 0}` | `b`, `ab`, `aab`, `aaab` |
| `S → 0S \| 1` | regular | `{0ⁿ1 \| n ≥ 0}` | `1`, `01`, `001`, `0001` |
| `S → aSb \| ε` | livre de ctx | `{aⁿbⁿ \| n ≥ 0}` | `ε`, `ab`, `aabb`, `aaabbb` |

---

## 13. Exercícios

Os três blocos de fixação passados na aula, resolvidos. Deixei o gabarito escondido pra eu
conseguir refazer sem ver a resposta quando for revisar.

### 📝 Bloco 1 — Derivação

**Enunciado:** dada `G₁: S → aS | b`

**A)** Gere a palavra `aaab`.
**B)** Explique como você sabe que a derivação terminou.

<details>
<summary>👀 Ver minha resposta</summary>

**A)** Preciso de três `a` e um `b` no fim. Como cada `S → aS` fixa exatamente um `a`, aplico ela
três vezes e fecho com `S → b`:

```
S ⇒ aS ⇒ aaS ⇒ aaaS ⇒ aaab
```

Conferindo passo a passo:

| Passo | Linha | Regra usada |
|:-:|:-:|---|
| início | `S` | — (símbolo inicial) |
| 1 | `aS` | `S → aS` |
| 2 | `aaS` | `S → aS` |
| 3 | `aaaS` | `S → aS` |
| 4 | `aaab` | `S → b` |

**Resposta:** `S ⇒ aS ⇒ aaS ⇒ aaaS ⇒ aaab` — três aplicações de `S → aS` e uma de `S → b` no fim.

**B)** **Justificativa:** porque na linha final, `aaab`, **não sobrou nenhuma variável**. Tanto `a`
quanto `b` são terminais dessa gramática (`T = {a, b}`), e terminal não tem regra que o substitua —
depois que ele aparece, fica ali.

Enquanto eu estava em `aaaS`, a derivação **não** tinha terminado, porque o `S` ali é variável e
ainda podia (e precisava) ser trocado. Foi a regra `S → b` que resolveu isso: ela é a única das
duas que não devolve `S` nenhum, então é ela que encerra.

O teste rápido que uso: **procuro maiúscula na linha**. Se achar, não terminou. Em `aaab` só tem
minúscula, então terminou — e aquilo é uma palavra de verdade de `L(G₁)`.

</details>

---

### 📝 Bloco 2 — Gramática Livre de Contexto

**Enunciado:** dada `G₂: S → aSb | ε`

**A)** Gere a palavra `aaabbb`.
**B)** É possível gerar `aabbb`? Justifique.

<details>
<summary>👀 Ver minha resposta</summary>

**A)** A palavra tem três `a` e três `b`. Como cada `S → aSb` coloca um `a` e um `b` de uma vez,
aplico ela três vezes e fecho com `S → ε`:

```
S ⇒ aSb ⇒ aaSbb ⇒ aaaSbbb ⇒ aaabbb
```

Passo a passo:

| Passo | Linha | Regra usada |
|:-:|:-:|---|
| início | `S` | — (símbolo inicial) |
| 1 | `aSb` | `S → aSb` |
| 2 | `aaSbb` | `S → aSb` |
| 3 | `aaaSbbb` | `S → aSb` |
| 4 | `aaabbb` | `S → ε` |

O último passo funciona porque `ε` não ocupa espaço nenhum — `aaaεbbb` é a mesma coisa que
`aaabbb`.

**Resposta:** `S ⇒ aSb ⇒ aaSbb ⇒ aaaSbbb ⇒ aaabbb`.

**B)** **Não é possível.**

**Justificativa:** `aabbb` tem **dois `a` e três `b`** — quantidades diferentes. E essa gramática
não consegue gerar quantidades diferentes, por causa de como as duas regras funcionam:

- `S → aSb` é a **única** regra que produz símbolo, e ela sempre coloca **um `a` e um `b` juntos,
  no mesmo passo**. Nunca um sem o outro;
- `S → ε` não produz símbolo nenhum, só encerra.

Então, depois de `n` aplicações de `S → aSb`, eu tenho obrigatoriamente `n` letras `a` e `n` letras
`b`. A conta sai sempre empatada:

| Aplicações de `S → aSb` | Palavra gerada | `a` | `b` |
|:-:|:-:|:-:|:-:|
| 0 | `ε` | 0 | 0 |
| 1 | `ab` | 1 | 1 |
| 2 | `aabb` | 2 | 2 |
| 3 | `aaabbb` | 3 | 3 |

A linguagem completa é:

```
L(G₂) = {aⁿbⁿ | n ≥ 0}
```

Pra `aabbb` pertencer, eu precisaria de `n = 2` (por causa dos dois `a`) e `n = 3` (por causa dos
três `b`) **ao mesmo tempo**, e um número não pode valer 2 e 3 de uma vez.

Testando na mão pra confirmar: se aplico `S → aSb` duas vezes, chego em `aaSbb`. Daí ou fecho com
`ε` e saio com `aabb` (falta um `b`), ou aplico `aSb` de novo e saio com `aaabbb` (sobra um `a`).
Não existe caminho que dê `aabbb`.

**Resposta: `aabbb` não pertence a `L(G₂)`**, porque a gramática obriga a mesma quantidade de `a` e
de `b`, e nessa palavra as quantidades são diferentes.

</details>

---

### 📝 Bloco 3 — Classificação

**Enunciado:** classifique como Regular ou Livre de Contexto:

```
S → aA
A → b
```

<details>
<summary>👀 Ver minha resposta</summary>

**Resposta: gramática Regular (Tipo 3 na Hierarquia de Chomsky).**

**Justificativa:** apliquei o roteiro da seção 11, regra por regra.

**Passo 1 — lado esquerdo:**

| Regra | Lado esquerdo | Tem só uma variável sozinha? |
|:-:|:-:|:-:|
| `S → aA` | `S` | ✅ |
| `A → b` | `A` | ✅ |

As duas passam, então a gramática é **pelo menos** livre de contexto. Sigo pro passo 2 pra ver se
ela é mais restrita que isso.

**Passo 2 — lado direito:**

| Regra | Lado direito | Formato | Encaixa em regular? |
|:-:|:-:|---|:-:|
| `S → aA` | `aA` | terminal `a` + variável `A` **na ponta** | ✅ |
| `A → b` | `b` | terminal sozinho, sem variável | ✅ |

**Todas** as regras cabem no formato regular (`A → aB` ou `A → a`), e em nenhuma delas a variável
aparece no meio. Logo, é **regular**.

**Por que não respondo "livre de contexto":** ela **também** é livre de contexto — toda gramática
regular é, porque o Tipo 3 está contido no Tipo 2. Mas a resposta esperada é a classe **mais
restrita** em que ela cabe, que é a mais informativa. É o caso do quadrado: dizer "retângulo" não
está errado, mas dizer "quadrado" diz mais.

**Comparando com o caso do Bloco 2 pra deixar a diferença clara:**

| Gramática | Onde fica a variável | Classificação |
|---|---|:-:|
| `S → aA`, `A → b` | na ponta (`aA`) | **Regular** |
| `S → aSb \| ε` | no meio (`aSb`) | **Livre de contexto** e não regular |

**Bônus que eu mesmo conferi** — qual linguagem essa gramática gera:

```
S ⇒ aA ⇒ ab
```

Não existe regra que devolva `S` ou `A`, então não dá pra alongar nada. Ela gera uma palavra só:

```
L(G) = {ab}
```

</details>

---

> 📄 A lista de exercícios da unidade está resolvida em
> [Lista1_Resolvida.md](Lista1_Resolvida.md).

---

## 14. Revisão para prova

O mínimo que quero ter na cabeça no dia:

| Conceito | Notação | Exemplo |
|---|:-:|---|
| Gramática | `G = (V, T, P, S)` | `({S}, {a,b}, P, S)` |
| Variáveis / não terminais | `V` | `{S}` — maiúsculas, são trocadas |
| Terminais | `T` | `{a, b}` — minúsculas, ficam na palavra |
| Produções | `P` | `S → aS`, `S → b` |
| Símbolo inicial | `S` | onde a derivação começa |
| Produz | `→` | `S → aS` (é a regra) |
| Deriva em | `⇒` | `S ⇒ aS` (é o passo) |
| Ou | `\|` | `S → aS \| b` |
| Linguagem gerada | `L(G)` | `{aⁿb \| n ≥ 0}` |
| Regular (tipo 3) | — | `S → aS \| b` — variável na ponta |
| Livre de contexto (tipo 2) | — | `S → aSb \| ε` — variável no meio |

E os pontos onde eu mais escorrego:

1. entregar `aaS` como resposta — **não é palavra**, ainda tem variável;
2. confundir `→` (a regra) com `⇒` (o passo da derivação);
3. responder "livre de contexto" numa gramática que é regular — a resposta é a **classe mais
   restrita**;
4. achar que basta a maioria das regras ser regular — tem que ser **todas**;
5. esquecer que `S → aSb` gera `a` e `b` **em par**, então em `aⁿbⁿ` sempre sai empatado;
6. começar a derivação por outro símbolo que não seja o inicial;
7. trocar `V` por `T` na hora de listar as partes — variável é a que **some** no fim.

---

## 15. 🧠 Mapa mental

Desenhei seguindo o caminho da aula: da pergunta inicial até a classificação.

```
        ┌────────────────────────────────────┐
        │  Como descrever formalmente uma    │
        │  linguagem (que pode ser infinita)?│
        └─────────────────┬──────────────────┘
                          │  não dá pra listar → preciso de regras
                          ▼
        ┌────────────────────────────────────┐
        │   GRAMÁTICA FORMAL  G = (V,T,P,S)  │
        ├────────────────────────────────────┤
        │  V = variáveis   (maiúsculas)      │
        │  T = terminais   (minúsculas)      │
        │  P = produções   (as regras)       │
        │  S = símbolo inicial               │
        └─────────────────┬──────────────────┘
                          │  aplico as produções a partir de S
                          ▼
        ┌────────────────────────────────────┐
        │            DERIVAÇÃO               │
        │     S ⇒ aS ⇒ aaS ⇒ aab             │
        │  para quando não sobra maiúscula   │
        └─────────────────┬──────────────────┘
                          │  o resultado é uma palavra de
                          ▼
        ┌────────────────────────────────────┐
        │      L(G) = linguagem gerada       │
        └─────────────────┬──────────────────┘
                          │  e o FORMATO das regras classifica G
                          ▼
        ┌────────────────────────────────────┐
        │       HIERARQUIA DE CHOMSKY        │
        └─────────────────┬──────────────────┘
              ┌───────────┴───────────┐
              ▼                       ▼
   ┌────────────────────┐   ┌────────────────────────┐
   │ TIPO 3 — REGULAR   │   │ TIPO 2 — LIVRE DE CTX  │
   │ variável na PONTA  │   │ variável pode ir ao    │
   │ S → aS | b         │   │ MEIO                   │
   │ L = {aⁿb}          │   │ S → aSb | ε            │
   │                    │   │ L = {aⁿbⁿ}             │
   └─────────┬──────────┘   └───────────┬────────────┘
             │                          │
             └──────────┬───────────────┘
                        ▼
              Tipo 3 ⊂ Tipo 2 ⊂ Tipo 1 ⊂ Tipo 0
              (toda regular também é livre de contexto,
               mas respondo sempre a classe mais restrita)
```

---

## 📌 Checklist

Marco o que já consigo explicar em voz alta, sem consultar:

- [ ] O que é uma gramática formal e por que ela é necessária;
- [ ] As quatro partes de `G = (V, T, P, S)`;
- [ ] A diferença entre variável (não terminal) e terminal;
- [ ] Por que `V`/`T` e `N`/`Σ` são a mesma coisa;
- [ ] Como ler `S → aS`;
- [ ] A diferença entre `→` e `⇒`;
- [ ] O que o símbolo `|` significa numa produção;
- [ ] Fazer uma derivação completa passo a passo;
- [ ] Dizer quando uma derivação terminou, e por quê;
- [ ] Por que toda gramática precisa de uma regra de saída;
- [ ] O formato das regras de uma gramática regular;
- [ ] O formato das regras de uma gramática livre de contexto;
- [ ] Explicar por que `S → aSb | ε` gera `aⁿbⁿ`;
- [ ] Os quatro tipos da Hierarquia de Chomsky;
- [ ] Por que toda gramática regular também é livre de contexto;
- [ ] Classificar uma gramática olhando só para as regras;
- [ ] Montar do zero uma gramática regular e uma livre de contexto.

---

## 🚀 Conceito-chave

Se eu tiver que resumir a aula inteira em cinco linhas:

> A linguagem é a lista de palavras; a gramática é a receita que gera essa lista.
> Toda gramática tem quatro partes: variáveis, terminais, produções e um símbolo inicial.
> Derivar é aplicar as regras a partir de `S` até não sobrar nenhuma variável.
> O **formato** das regras é o que classifica a gramática.
> Variável na ponta = regular; variável no meio = livre de contexto.

---

<p align="center">
  <a href="../README.md">⬅ voltar para o índice</a>
</p>

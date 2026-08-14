# 📚 Aula 02 — Hierarquia de Chomsky e Autômatos Finitos

> Na Aula 01 aprendemos a **gerar** palavras com gramáticas.
> Nesta aula vamos para o outro lado: como **reconhecer** se uma palavra pertence à linguagem —
> e que tipo de máquina dá conta de cada tipo de gramática.

[⬅ voltar para o índice](../README.md)

---

## 📑 Sumário

- [🎯 Objetivos da aula](#-objetivos-da-aula)
- [1. Gerar × reconhecer](#1-gerar--reconhecer)
- [2. A Hierarquia de Chomsky](#2-a-hierarquia-de-chomsky)
- [3. Gramáticas regulares — Tipo 3](#3-gramáticas-regulares--tipo-3)
- [4. Autômato Finito Determinístico — AFD](#4-autômato-finito-determinístico--afd)
- [5. Tabela e diagrama de transição](#5-tabela-e-diagrama-de-transição)
- [6. Processando uma palavra](#6-processando-uma-palavra)
- [7. Exemplo completo — terminadas em b](#7-exemplo-completo--terminadas-em-b)
- [8. Exemplo completo — quantidade par de a](#8-exemplo-completo--quantidade-par-de-a)
- [9. Autômato Finito Não Determinístico — AFN](#9-autômato-finito-não-determinístico--afn)
- [10. AFD × AFN](#10-afd--afn)
- [11. Da gramática regular para o autômato](#11-da-gramática-regular-para-o-autômato)
- [12. Atividades práticas](#12-atividades-práticas)
- [13. Resumo para prova](#13-resumo-para-prova)
- [14. Mapa mental](#14--mapa-mental)
- [📌 Checklist da aula](#-checklist-da-aula-2)

---

## 🎯 Objetivos da aula

Ao final desta aula, devemos ser capazes de:

- Diferenciar **gerar** e **reconhecer** uma linguagem;
- Conhecer os quatro tipos da **Hierarquia de Chomsky**;
- Classificar uma gramática pelo formato das suas produções;
- Identificar uma **gramática regular** (tipo 3);
- Entender a quíntupla `M = (Q, Σ, δ, q₀, F)`;
- Montar **tabela** e **diagrama** de transição;
- Processar uma palavra passo a passo e decidir **aceita** ou **rejeita**;
- Diferenciar **AFD** e **AFN**;
- Converter uma gramática regular em um autômato finito.

---

## 1. Gerar × reconhecer

São dois pontos de vista sobre a mesma linguagem:

| Ferramenta | O que faz | Pergunta que responde |
|---|---|---|
| **Gramática** | produz palavras a partir de `S` | "quais palavras existem em L?" |
| **Autômato** | lê uma palavra símbolo a símbolo | "esta palavra pertence a L?" |

```
   GRAMÁTICA  ──── gera ────►   L   ◄──── reconhece ────  AUTÔMATO
```

Na Aula 01, `S → aS | ε` **gerava** `ε, a, aa, aaa, ...`
Nesta aula queremos uma máquina que, ao receber `aaa`, responda **sim**; e ao receber `aab`,
responda **não**.

---

## 2. A Hierarquia de Chomsky

Noam Chomsky organizou as gramáticas em **quatro níveis**, do mais geral para o mais restrito.
Quanto mais restrita a forma das produções, mais simples é a máquina necessária.

| Tipo | Gramática | Formato das produções | Máquina reconhecedora |
|:-:|---|---|---|
| **0** | Irrestrita | `α → β` (α tem ao menos um não terminal) | Máquina de Turing |
| **1** | Sensível ao contexto | `α → β` com `\|α\| ≤ \|β\|` | Autômato linearmente limitado |
| **2** | Livre de contexto | `A → β` (esquerda = **um** não terminal) | Autômato de pilha |
| **3** | Regular | `A → aB`, `A → a`, `A → ε` | Autômato finito |

E a relação de contenção entre elas:

```
┌──────────────────────────── Tipo 0 — irrestritas ────────────────────────────┐
│  ┌──────────────────── Tipo 1 — sensíveis ao contexto ────────────────────┐  │
│  │   ┌──────────────── Tipo 2 — livres de contexto ────────────────┐      │  │
│  │   │        ┌──────── Tipo 3 — regulares ────────┐               │      │  │
│  │   │        │      aⁿ  ·  (ab)ⁿ  ·  a*b*         │               │      │  │
│  │   │        └────────────────────────────────────┘               │      │  │
│  │   │                    aⁿbⁿ  ·  parênteses balanceados          │      │  │
│  │   └─────────────────────────────────────────────────────────────┘      │  │
│  │                                aⁿbⁿcⁿ                                  │  │
│  └────────────────────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────────────────┘
```

> 🧠 **Leitura do desenho:** toda linguagem regular é livre de contexto, toda livre de contexto é
> sensível ao contexto, e assim por diante. O contrário **não** vale — e é justamente isso que
> costuma ser cobrado: `aⁿbⁿ` é tipo 2 mas **não** é tipo 3, porque um autômato finito não tem
> memória para contar quantos `a` já viu.

**Nesta aula ficamos no Tipo 3.** É o nível dos autômatos finitos e das expressões regulares.

---

## 3. Gramáticas regulares — Tipo 3

Uma gramática é **regular (linear à direita)** quando toda produção tem uma destas formas:

```
A → aB          (um terminal seguido de um não terminal)
A → a           (só um terminal)
A → ε           (palavra vazia)
```

Ou seja: no lado direito, **no máximo um** não terminal, e ele fica **sempre no fim**.

### Classificando exemplos

| Gramática | Tipo | Por quê |
|---|:-:|---|
| `S → aS \| ε` | 3 | terminal + não terminal no fim, e a produção vazia |
| `S → aA`, `A → bS \| b` | 3 | mesma forma, alternando não terminais |
| `S → aSb \| ε` | 2 | `aSb` tem terminal **depois** do não terminal → não é regular |
| `S → SS \| a` | 2 | dois não terminais do lado direito |
| `aSb → bSa` | 0/1 | lado esquerdo com mais de um símbolo |

> ⚠️ Cuidado com a pegadinha `S → aSb | ε`. Ela gera `aⁿbⁿ` (`ε, ab, aabb, aaabbb, …`),
> que é a linguagem clássica **não regular**. O motivo é intuitivo: para garantir a mesma
> quantidade dos dois lados é preciso *lembrar um número*, e um autômato finito só tem uma
> quantidade fixa de estados.

---

## 4. Autômato Finito Determinístico — AFD

Um AFD é definido por uma **quíntupla**:

```
M = (Q, Σ, δ, q₀, F)
```

| Elemento | Nome | Significado |
|:-:|---|---|
| `Q` | estados | conjunto **finito** de estados |
| `Σ` | alfabeto | símbolos que a máquina consegue ler |
| `δ` | função de transição | `δ(estado, símbolo) = próximo estado` |
| `q₀` | estado inicial | onde a leitura começa (`q₀ ∈ Q`) |
| `F` | estados finais | conjunto de estados de aceitação (`F ⊆ Q`) |

**Determinístico** significa: para cada par (estado, símbolo) existe **exatamente uma** transição.
Nunca duas, nunca nenhuma. Lendo a mesma palavra mil vezes, o caminho percorrido é sempre o mesmo.

### Convenções do diagrama

```
──►( q )     estado inicial (seta vindo do nada)
   ( q )     estado comum
   (( q ))   estado final (círculo duplo)
   q ──a──► p     transição lendo o símbolo a
```

---

## 5. Tabela e diagrama de transição

A função `δ` pode ser escrita de duas formas equivalentes. Usando

```
Q = {q0, q1}      Σ = {a, b}      q₀ = q0      F = {q1}
```

**Como tabela:**

| δ | a | b |
|:-:|:-:|:-:|
| **→ q0** | q0 | q1 |
| **\* q1** | q0 | q1 |

Legenda: `→` marca o inicial, `*` marca o final.

**Como lista de transições:**

```
δ(q0, a) = q0
δ(q0, b) = q1
δ(q1, a) = q0
δ(q1, b) = q1
```

**Como diagrama:**

```
            a                        b
          ┌───┐                    ┌───┐
          │   ▼                    │   ▼
  ──────►( q0 )──────── b ───────►(( q1 ))
           ▲                          │
           └────────── a ─────────────┘
```

As três representações dizem a mesma coisa. Na prova, se pedirem "defina formalmente", é a
quíntupla + tabela; se pedirem "represente", geralmente é o diagrama.

---

## 6. Processando uma palavra

O procedimento é sempre o mesmo:

1. Começar em `q₀`;
2. Ler a palavra da esquerda para a direita, um símbolo por vez;
3. A cada símbolo, aplicar `δ` e trocar de estado;
4. Ao acabar a palavra: se o estado atual está em `F` → **aceita**; senão → **rejeita**.

> ❗ O que decide é **onde a leitura termina**, não por quais estados ela passou.
> Passar por um estado final no meio do caminho não significa nada.

---

## 7. Exemplo completo — terminadas em b

**Linguagem:** `L₁ = { w ∈ {a,b}* | w termina com b }`

**Autômato:**

```
M₁ = ({q0, q1}, {a, b}, δ, q0, {q1})
```

| δ | a | b |
|:-:|:-:|:-:|
| **→ q0** | q0 | q1 |
| **\* q1** | q0 | q1 |

A ideia por trás dos estados:

- `q0` = "o último símbolo lido **não** foi `b`" (ou nada foi lido ainda);
- `q1` = "o último símbolo lido **foi** `b`".

### Testando `abb`

| Passo | Estado atual | Lê | Vai para |
|:-:|:-:|:-:|:-:|
| 1 | q0 | a | q0 |
| 2 | q0 | b | q1 |
| 3 | q1 | b | q1 |

Terminou em `q1`, que é final → **ACEITA** ✅

### Testando `aba`

| Passo | Estado atual | Lê | Vai para |
|:-:|:-:|:-:|:-:|
| 1 | q0 | a | q0 |
| 2 | q0 | b | q1 |
| 3 | q1 | a | q0 |

Terminou em `q0`, que **não** é final → **REJEITA** ❌

Repare que `aba` passou por `q1` no meio, e mesmo assim foi rejeitada. É exatamente o ponto do
aviso da seção anterior.

### Testando `ε`

Nenhum símbolo é lido, então o estado final da execução é o próprio `q0` → **REJEITA** ❌
(faz sentido: a palavra vazia não termina com `b`).

---

## 8. Exemplo completo — quantidade par de a

**Linguagem:** `L₂ = { w ∈ {a,b}* | w possui uma quantidade par de a }`

**Autômato:**

```
M₂ = ({p0, p1}, {a, b}, δ, p0, {p0})
```

| δ | a | b |
|:-:|:-:|:-:|
| **→ \* p0** | p1 | p0 |
| **p1** | p0 | p1 |

```
            b                        b
          ┌───┐                    ┌───┐
          │   ▼         a          │   ▼
  ──────►(( p0 ))◄───────────────►( p1 )
                         a
```

- `p0` = já li uma quantidade **par** de `a` (é o inicial **e** o final);
- `p1` = já li uma quantidade **ímpar** de `a`;
- o símbolo `b` não muda nada, por isso são laços.

### Testando `abba`

| Passo | Estado | Lê | Vai para |
|:-:|:-:|:-:|:-:|
| 1 | p0 | a | p1 |
| 2 | p1 | b | p1 |
| 3 | p1 | b | p1 |
| 4 | p1 | a | p0 |

Terminou em `p0` → **ACEITA** ✅ (são dois `a`, número par).

### Testando `aaba`

| Passo | Estado | Lê | Vai para |
|:-:|:-:|:-:|:-:|
| 1 | p0 | a | p1 |
| 2 | p1 | a | p0 |
| 3 | p0 | b | p0 |
| 4 | p0 | a | p1 |

Terminou em `p1` → **REJEITA** ❌ (são três `a`, número ímpar).

### E o ε?

`ε` termina em `p0`, que é final → **ACEITA** ✅
Zero é par, então está certo. Sempre que o inicial for também final, a linguagem contém `ε`.

---

## 9. Autômato Finito Não Determinístico — AFN

Num **AFN** a função de transição pode levar a **vários estados ao mesmo tempo** (ou a nenhum):

```
δ(q, a) = {q1, q2, ...}          ← devolve um CONJUNTO de estados
```

**Critério de aceitação:** a palavra é aceita se **existir pelo menos um caminho** que termine em
estado final. Basta um dar certo.

### Exemplo — terminadas em ab

```
N = ({q0, q1, q2}, {a, b}, δ, q0, {q2})
```

| δ | a | b |
|:-:|:-:|:-:|
| **→ q0** | {q0, q1} | {q0} |
| **q1** | ∅ | {q2} |
| **\* q2** | ∅ | ∅ |

```
         a, b
        ┌────┐
        │    ▼
 ─────►( q0 )────a───►( q1 )────b───►(( q2 ))
```

Em `q0`, ao ler `a`, a máquina "aposta" nas duas opções: continuar esperando (`q0`) ou assumir que
aquele `a` é o começo do `ab` final (`q1`).

### Testando `aab`

Caminhos possíveis:

```
q0 --a--> q0 --a--> q0 --b--> q0     termina em q0    ❌
q0 --a--> q0 --a--> q1 --b--> q2     termina em q2    ✅
q0 --a--> q1 --a--> (sem transição)  morre            ❌
```

Existe **um** caminho terminando em `q2` → **ACEITA** ✅

---

## 10. AFD × AFN

| | AFD | AFN |
|---|---|---|
| Transições por (estado, símbolo) | exatamente 1 | 0, 1 ou várias |
| Resultado de `δ` | um estado | um conjunto de estados |
| Aceita quando | o único caminho termina em F | **algum** caminho termina em F |
| Facilidade de desenhar | menor | maior |
| Facilidade de implementar | maior | menor |

📌 **O resultado mais importante do tópico:**

> Todo AFN possui um AFD equivalente, que reconhece exatamente a mesma linguagem.

Ou seja, o não determinismo é uma comodidade de projeto, **não** um ganho de poder: AFD e AFN
reconhecem a mesma classe — as **linguagens regulares**. A conversão é feita pela construção de
subconjuntos, em que cada estado do AFD representa um conjunto de estados do AFN.

---

## 11. Da gramática regular para o autômato

A tradução é quase mecânica. Cada **não terminal vira um estado**:

| Produção | Transição |
|---|---|
| `A → aB` | `δ(A, a) = B` |
| `A → a` | `δ(A, a) = ` estado final |
| `A → ε` | `A` é estado final |

### Exemplo — a gramática da Aula 01

```
G = ({S}, {a}, {S → aS | ε}, S)
```

- `S → aS` → `δ(S, a) = S` (volta para o próprio S);
- `S → ε` → `S` é estado final.

Autômato resultante:

```
M = ({S}, {a}, δ, S, {S})
```

```
            a
          ┌───┐
          │   ▼
  ──────►(( S ))
```

Um único estado, inicial e final, com um laço lendo `a`. Ele aceita `ε, a, aa, aaa, …` — que é
exatamente `L(G) = {aⁿ | n ≥ 0}`, a linguagem que a gramática gerava na Aula 01. Fecha o ciclo:
**gerar** e **reconhecer** descrevendo a mesma linguagem.

---

## 12. Atividades práticas

### 📝 Atividade 1 — Classificação na Hierarquia de Chomsky

Classifique cada gramática (tipo 0, 1, 2 ou 3) e justifique:

- **a)** `S → aS | bS | ε`
- **b)** `S → aSb | ε`
- **c)** `S → aB`, `B → bS | b`

<details>
<summary>👀 Ver resposta</summary>

**a) Tipo 3 — regular.**
Todas as produções são `A → aB` ou `A → ε`, com o não terminal sempre no fim do lado direito.
Ela gera qualquer combinação de `a` e `b`, ou seja, `L = Σ*` com `Σ = {a, b}`.

**b) Tipo 2 — livre de contexto (e não regular).**
O lado esquerdo é um único não terminal, então é livre de contexto. Mas `aSb` tem terminal
**depois** do não terminal, o que quebra a forma regular. A linguagem gerada é
`L = {aⁿbⁿ | n ≥ 0}`, que precisa de memória para contar — um autômato finito não dá conta.

**c) Tipo 3 — regular.**
`S → aB`, `B → bS` e `B → b` estão todas nas formas `A → aB` e `A → a`.
Gera `ab, abab, ababab, …`, isto é, `L = {(ab)ⁿ | n ≥ 1}`.

</details>

---

### 📝 Atividade 2 — Reconhecimento com AFD

Considere o autômato `M₁` da seção 7 (aceita palavras terminadas em `b`):

| δ | a | b |
|:-:|:-:|:-:|
| **→ q0** | q0 | q1 |
| **\* q1** | q0 | q1 |

Diga se cada palavra é **aceita** ou **rejeitada**, mostrando o caminho:

- **a)** `bab`
- **b)** `baa`
- **c)** `bbb`

<details>
<summary>👀 Ver resposta</summary>

**a) `bab` → ACEITA ✅**

```
q0 --b--> q1 --a--> q0 --b--> q1        q1 ∈ F
```

**b) `baa` → REJEITA ❌**

```
q0 --b--> q1 --a--> q0 --a--> q0        q0 ∉ F
```

**c) `bbb` → ACEITA ✅**

```
q0 --b--> q1 --b--> q1 --b--> q1        q1 ∈ F
```

Confere com a definição da linguagem: `bab` e `bbb` terminam em `b`, `baa` termina em `a`.

</details>

---

### 📝 Atividade 3 — Construir um AFD

Construa um AFD sobre `Σ = {a, b}` que aceite as palavras **começadas por `a`**.
Apresente a quíntupla, a tabela de transição e o diagrama.

<details>
<summary>👀 Ver resposta</summary>

**Quíntupla:**

```
M = ({q0, q1, qe}, {a, b}, δ, q0, {q1})
```

**Tabela:**

| δ | a | b |
|:-:|:-:|:-:|
| **→ q0** | q1 | qe |
| **\* q1** | q1 | q1 |
| **qe** | qe | qe |

**Diagrama:**

```
                              a, b
                             ┌────┐
                             │    ▼
  ──────►( q0 )──── a ─────►(( q1 ))
             │
             b
             │                a, b
             ▼               ┌────┐
           ( qe )────────────┘    │
             ▲                    │
             └────────────────────┘
```

**Papel de cada estado:**

- `q0` — nada foi lido ainda; só o primeiro símbolo importa;
- `q1` — o primeiro símbolo foi `a`; daqui em diante aceita qualquer coisa;
- `qe` — **estado de erro** (ou "poço"): o primeiro símbolo foi `b`, então a palavra já está
  perdida. Todas as transições voltam para ele mesmo e ele não é final.

O `qe` é obrigatório porque o autômato é **determinístico**: precisa existir uma transição definida
para **todo** par (estado, símbolo). Esquecer o estado de erro é o erro mais comum nessa questão.

E `ε` é rejeitada — a execução termina em `q0`, que não é final. Correto, já que `ε` não começa com
`a`.

</details>

---

### 📝 Atividade 4 — Gramática → autômato

Converta a gramática abaixo em um autômato finito e diga qual linguagem ela reconhece:

```
G = ({S, A}, {a, b}, P, S)
P = { S → aA,  A → bS | ε }
```

<details>
<summary>👀 Ver resposta</summary>

**Conversão, produção por produção:**

| Produção | Efeito no autômato |
|---|---|
| `S → aA` | `δ(S, a) = A` |
| `A → bS` | `δ(A, b) = S` |
| `A → ε` | `A` é estado final |

**Autômato:**

```
M = ({S, A}, {a, b}, δ, S, {A})
```

| δ | a | b |
|:-:|:-:|:-:|
| **→ S** | A | — |
| **\* A** | — | S |

```
  ──────►( S )──── a ────►(( A ))
             ▲               │
             └───── b ───────┘
```

**Linguagem reconhecida:**

```
L(G) = {(ab)ⁿ a | n ≥ 0}  =  {a, aba, ababa, ...}
```

Derivando para conferir:

```
S → aA → a                 (usando A → ε)
S → aA → abS → abaA → aba  (usando A → ε no fim)
```

Toda palavra começa com `a`, alterna os símbolos e **termina em `a`** — porque o único estado final
é `A`, alcançado sempre depois de ler um `a`. As tabelas com `—` mostram transições indefinidas:
formalmente, este é um AFN (ou um AFD parcial); para deixá-lo totalmente determinístico bastaria
acrescentar um estado de erro, como fizemos na Atividade 3.

</details>

---

## 13. Resumo para prova

### 🔹 Hierarquia de Chomsky

| Tipo | Gramática | Máquina |
|:-:|---|---|
| 0 | irrestrita | Máquina de Turing |
| 1 | sensível ao contexto | autômato linearmente limitado |
| 2 | livre de contexto | autômato de pilha |
| 3 | regular | autômato finito |

Quanto **maior** o número do tipo, **mais restrita** a gramática e **mais simples** a máquina.

### 🔹 Gramática regular (tipo 3)

```
A → aB      A → a      A → ε
```

No máximo um não terminal do lado direito, e sempre no fim.

### 🔹 Quíntupla do AFD

```
M = (Q, Σ, δ, q₀, F)
```

`Q` estados · `Σ` alfabeto · `δ` transição · `q₀` inicial · `F` finais.

### 🔹 Critério de aceitação

Lê a palavra inteira a partir de `q₀`; **aceita** se o estado onde parou pertence a `F`.
O que vale é onde termina, não por onde passou.

### 🔹 AFD × AFN

- AFD: exatamente uma transição por (estado, símbolo);
- AFN: zero, uma ou várias; aceita se **algum** caminho termina em F;
- **Todo AFN tem um AFD equivalente** — mesmo poder de reconhecimento.

### 🔹 Estado de erro (poço)

Num AFD, todo par (estado, símbolo) precisa de transição. Quando a palavra já está condenada,
mandamos para um estado não final que só volta para si mesmo.

### 🔹 Conversão gramática → autômato

| Produção | Transição |
|---|---|
| `A → aB` | `δ(A, a) = B` |
| `A → a` | `δ(A, a) = ` final |
| `A → ε` | `A` é final |

### 🔹 O clássico que cai na prova

`aⁿbⁿ` **não é linguagem regular**. Autômato finito não conta, porque tem memória fixa.
Para reconhecê-la é preciso um autômato de pilha (tipo 2).

---

## 14. 🧠 Mapa mental

```
                      HIERARQUIA DE CHOMSKY
                               │
        ┌──────────┬───────────┼───────────┬──────────┐
        ▼          ▼           ▼           ▼          │
     Tipo 0     Tipo 1      Tipo 2      Tipo 3        │
   irrestrita  sensível     livre de    regular       │
                ao ctx      contexto       │          │
        │          │           │           │          │
        ▼          ▼           ▼           ▼          │
     Máq. de     Aut. lin.   Aut. de    AUTÔMATO      │
     Turing     limitado      pilha      FINITO ◄─────┘
                                            │
                        ┌───────────────────┴──────────────┐
                        ▼                                  ▼
                       AFD                                AFN
                        │                                  │
                        │  M = (Q, Σ, δ, q₀, F)            │  δ devolve conjunto
                        │  1 transição por símbolo         │  aceita se ALGUM
                        │                                  │  caminho chega em F
                        └────────────► equivalentes ◄──────┘
                                            │
                                            ▼
                                LINGUAGENS REGULARES
                                            │
                                            ▼
                              aceita se terminar em F
```

---

## 📌 Checklist da aula 2

Antes de avançar para a próxima aula, verifique se você consegue explicar:

- [ ] A diferença entre gerar e reconhecer uma linguagem;
- [ ] Os quatro tipos da Hierarquia de Chomsky e suas máquinas;
- [ ] Por que a hierarquia é uma contenção (tipo 3 ⊆ tipo 2 ⊆ tipo 1 ⊆ tipo 0);
- [ ] Como identificar uma gramática regular pelo formato das produções;
- [ ] Por que `S → aSb | ε` **não** é regular;
- [ ] O que significa cada elemento de `M = (Q, Σ, δ, q₀, F)`;
- [ ] Montar a tabela de transição a partir do diagrama, e vice-versa;
- [ ] Processar uma palavra e justificar aceitação ou rejeição;
- [ ] Por que passar por um estado final no meio não basta;
- [ ] Quando `ε` é aceita por um autômato;
- [ ] Para que serve o estado de erro num AFD;
- [ ] A diferença entre AFD e AFN;
- [ ] Por que AFD e AFN têm o mesmo poder de reconhecimento;
- [ ] Converter uma gramática regular em autômato finito.

---

<p align="center">
  <a href="aula-01-linguagens-formais-e-gramaticas.md">⬅ Aula 01</a> ·
  <a href="../README.md">Índice</a>
</p>

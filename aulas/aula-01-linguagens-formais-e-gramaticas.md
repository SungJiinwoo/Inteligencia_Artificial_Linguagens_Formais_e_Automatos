# 📚 Aula 01 — Linguagens Formais e Gramáticas

> Introdução aos conceitos de alfabeto, cadeia, linguagem formal e gramática.
> É a aula que dá o vocabulário do resto da disciplina — sem ela, nada depois faz sentido.

[⬅ voltar para o índice](../README.md)

---

## 📑 Sumário

- [🎯 Objetivos da aula](#-objetivos-da-aula)
- [1. Operadores lógicos](#1-operadores-lógicos)
- [2. Palavra vazia — ε](#2-palavra-vazia--ε)
- [3. Prefixos e sufixos](#3-prefixos-e-sufixos)
- [4. Alfabeto — Σ](#4-alfabeto--σ)
- [5. Σ\* — todas as cadeias possíveis](#5-σ--todas-as-cadeias-possíveis)
- [6. Linguagem formal — L](#6-linguagem-formal--l)
- [7. Gramática formal](#7-gramática-formal)
- [8. Regras de produção](#8-regras-de-produção)
- [9. Como ler o símbolo →](#9-como-ler-o-símbolo-)
- [10. Derivação de palavras](#10-derivação-de-palavras)
- [11. Linguagem gerada](#11-linguagem-gerada)
- [12. Atividades práticas](#12-atividades-práticas)
- [13. Resumo para prova](#13-resumo-para-prova)
- [14. Mapa mental](#14--mapa-mental)
- [📌 Checklist da aula](#-checklist-da-aula-1)

---

## 🎯 Objetivos da aula

Ao final desta aula, devemos ser capazes de:

- Entender o conceito de alfabeto;
- Identificar cadeias / palavras;
- Compreender a palavra vazia ε;
- Identificar prefixos e sufixos;
- Entender o conceito de linguagem formal;
- Interpretar a notação `L ⊆ Σ*`;
- Compreender o funcionamento de uma gramática formal;
- Interpretar regras de produção;
- Gerar palavras a partir de uma gramática.

---

## 1. Operadores lógicos

Os principais operadores estudados são:

| Símbolo | Nome | Leitura |
|:-:|---|---|
| `¬` | Negação | não |
| `∧` | E | e |
| `∨` | OU | ou |
| `→` | Implicação | implica / se... então |

### Exemplo

Considere:

```
p = "Está chovendo."
q = "Eu levo um guarda-chuva."
```

**Negação — ¬**

```
¬p
```

Lê-se: *Não está chovendo.*

**E — ∧**

```
p ∧ q
```

Lê-se: *Está chovendo **e** eu levo um guarda-chuva.*

**OU — ∨**

```
p ∨ q
```

Lê-se: *Está chovendo **ou** eu levo um guarda-chuva.*

**Implicação — →**

```
p → q
```

Lê-se: *Se está chovendo, então eu levo um guarda-chuva.*

> ⚠️ **Atenção:** o símbolo `→` tem significados diferentes dependendo do contexto.
> Em **lógica** significa implicação. Em **gramáticas** significa produção / geração.
> Esse é o tipo de detalhe que derruba gente na prova.

---

## 2. Palavra vazia — ε

A palavra vazia é representada por:

```
ε
```

Lê-se: **épsilon**.

Ela representa uma cadeia que **não possui nenhum símbolo**. Seu tamanho é:

```
|ε| = 0
```

### Exemplo

A cadeia `abc` possui 3 símbolos:

```
|abc| = 3
```

Já `ε` possui 0 símbolos:

```
|ε| = 0
```

> ⚠️ **Importante:** ε **não** é um espaço em branco.
> Espaço em branco é um símbolo — ocuparia uma posição e contaria no comprimento.
> ε significa: *não existe nenhum símbolo na cadeia*.

---

## 3. Prefixos e sufixos

Considere a palavra:

```
ab
```

### Prefixos

Um **prefixo** é uma parte da palavra que começa no **início**.

Podemos obter `ε`, `a` e `ab`. Portanto:

```
Prefixos(ab) = {ε, a, ab}
```

> 🧠 **Dica:** prefixo → começa no começo.

### Sufixos

Um **sufixo** é uma parte da palavra que termina no **final**.

Podemos obter `ε`, `b` e `ab`. Portanto:

```
Sufixos(ab) = {ε, b, ab}
```

> 🧠 **Dica:** sufixo → termina no final.

### Resumo

| Palavra | Prefixos | Sufixos |
|:-:|---|---|
| `ab` | ε, a, ab | ε, b, ab |

Repare que o `ε` é considerado **tanto prefixo quanto sufixo**, e que a própria palavra também é
prefixo e sufixo dela mesma. São os dois casos que a gente esquece de listar na prova.

---

## 4. Alfabeto — Σ

Um **alfabeto** é um conjunto **finito** de símbolos. Ele é representado por:

```
Σ
```

Lê-se: **sigma**.

### Exemplo

```
Σ = {a, b}
```

Nosso alfabeto possui dois símbolos: `a` e `b`. A partir deles podemos criar palavras:

```
a
b
aa
ab
ba
bb
aaa
aab
aba
...
```

---

## 5. Σ* — todas as cadeias possíveis

A notação:

```
Σ*
```

representa o conjunto de **todas as cadeias finitas** que podem ser formadas com os símbolos de Σ,
**incluindo ε**.

Se:

```
Σ = {a, b}
```

então:

```
Σ* = {ε, a, b, aa, ab, ba, bb, aaa, ...}
```

### Existe um limite?

Não existe limite máximo para o tamanho das palavras. Podemos formar:

```
ε
a
aa
aaa
aaaa
aaaaa
...
```

A quantidade de palavras cresce conforme o tamanho aumenta. Para um alfabeto com 2 símbolos:

```
Quantidade de cadeias de tamanho n = 2ⁿ
```

| Tamanho | Quantidade |
|:-:|:-:|
| 0 | 1 |
| 1 | 2 |
| 2 | 4 |
| 3 | 8 |
| 4 | 16 |
| 5 | 32 |
| … | … |

> 📌 **Conclusão:** Σ* é **infinito**, mas cada cadeia individual tem tamanho **finito**.
> Não existe uma "palavra infinita" dentro de Σ*.

---

## 6. Linguagem formal — L

Uma **linguagem formal** é um conjunto de palavras construídas a partir de um alfabeto:

```
L ⊆ Σ*
```

Lê-se: *L é um subconjunto de sigma estrela.*

### Entendendo cada elemento

| Elemento | O que é |
|:-:|---|
| `Σ` | o alfabeto |
| `Σ*` | o conjunto de todas as palavras possíveis |
| `L` | um conjunto de palavras escolhidas de Σ* |

### Exemplo

Considere `Σ = {a, b}`. Podemos definir:

```
L = {a, ab, abb, abbb}
```

Como todas essas palavras podem ser formadas usando `a` e `b`, vale que `L ⊆ Σ*`.

**Linguagem finita**

```
L = {ε, a, ab}
```

Possui uma quantidade limitada de palavras.

**Linguagem infinita**

```
L = {a, aa, aaa, aaaa, ...}
```

Possui infinitas palavras.

---

## 7. Gramática formal

Uma **gramática formal** fornece regras para gerar palavras. Considere:

```
G = ({S}, {a}, {S → aS | ε}, S)
```

A forma geral é:

```
G = (N, Σ, P, S)
```

| Elemento | Significado |
|:-:|---|
| `N` | não terminais |
| `Σ` | terminais |
| `P` | produções |
| `S` | símbolo inicial |

No nosso exemplo:

| Parte | Valor |
|---|---|
| Não terminal | `{S}` |
| Terminal | `{a}` |
| Produções | `S → aS \| ε` |
| Símbolo inicial | `S` |

> 🧠 Jeito que eu memorizei: **não terminal** é uma variável que ainda precisa ser substituída
> (por convenção, letra maiúscula); **terminal** é símbolo final, que já faz parte da palavra
> (letra minúscula). A derivação só termina quando não sobra nenhuma maiúscula.

---

## 8. Regras de produção

A regra:

```
S → aS | ε
```

possui duas possibilidades:

```
S → aS
```

**ou**

```
S → ε
```

O símbolo `|` significa **OU**. Portanto: *S pode produzir `aS` ou `ε`*.

---

## 9. Como ler o símbolo →

### Em gramáticas

Pode significar: **produz**, **gera**, **deriva em**.

```
S → aS
```

Lê-se: *S produz aS.*

### Em lógica

Pode significar: **implica**, **se... então**.

```
p → q
```

Lê-se: *Se p, então q* — ou *p implica q*.

---

## 10. Derivação de palavras

Considere:

```
G = ({S}, {a}, {S → aS | ε}, S)
```

Começamos **sempre** pelo símbolo inicial `S`.

### Gerando ε

Escolhemos `S → ε`:

```
S → ε
```

Resultado: `ε`

### Gerando a

Primeiro `S → aS`, depois `S → ε`:

```
S → aS → aε → a
```

Resultado: `a`

### Gerando aa

Aplicamos `S → aS` duas vezes:

```
S → aS
  → aaS
  → aaε
  → aa
```

Resultado: `aa`

### Gerando aaa

Aplicamos `S → aS` três vezes:

```
S → aS
  → aaS
  → aaaS
  → aaaε
  → aaa
```

Resultado: `aaa`

> 💡 Detalhe que confunde: `aε` é o mesmo que `a`. Concatenar a palavra vazia não muda nada —
> ela funciona como o elemento neutro da concatenação, igual ao 0 na soma.

---

## 11. Linguagem gerada

A gramática:

```
G = ({S}, {a}, {S → aS | ε}, S)
```

gera:

```
ε
a
aa
aaa
aaaa
aaaaa
...
```

Logo:

```
L(G) = {ε, a, aa, aaa, aaaa, ...}
```

Também podemos representar como:

```
L(G) = {aⁿ | n ≥ 0}
```

Isso significa: a linguagem contém **qualquer quantidade de `a`**, incluindo zero.
E o caso de zero `a` é justamente `ε`.

> Se a regra fosse `S → aS | a`, a linguagem seria `{aⁿ | n ≥ 1}` — sem o ε.
> Uma produção a menos muda a linguagem inteira.

---

## 12. Atividades práticas

### 📝 Atividade 1 — Prefixos e sufixos

**Considere a palavra:** `ab`

**Pergunta:** liste os prefixos e sufixos.

<details>
<summary>👀 Ver resposta</summary>

**Prefixos:**

```
{ε, a, ab}
```

**Sufixos:**

```
{ε, b, ab}
```

**Justificando:** prefixo é qualquer pedaço que começa na primeira posição — cortando em 0, 1 e 2
símbolos, saem `ε`, `a` e `ab`. Sufixo é qualquer pedaço que termina na última posição — saem `ε`,
`b` e `ab`. Uma palavra de tamanho *n* sempre tem *n + 1* prefixos e *n + 1* sufixos, contando ε e a
palavra inteira. Aqui, *n* = 2 → 3 de cada. Confere.

</details>

---

### 📝 Atividade 2 — Gramática

**Considere:**

```
G = ({S}, {a}, {S → aS | ε}, S)
```

**Pergunta:** liste 3 palavras geradas.

<details>
<summary>👀 Ver resposta</summary>

Uma resposta possível:

```
ε
a
aa
```

**Derivando cada uma:**

| Palavra | Derivação |
|:-:|---|
| `ε` | `S → ε` |
| `a` | `S → aS → aε → a` |
| `aa` | `S → aS → aaS → aaε → aa` |

Outras respostas também valem, como `aaa`, `aaaa`, `aaaaa`, … — qualquer sequência só de `a`
serve, porque `L(G) = {aⁿ | n ≥ 0}`.

O que **não** valeria: `b` (não é terminal desta gramática), `ab` ou `aS` (ainda tem não terminal,
então nem é palavra ainda).

</details>

---

## 13. Resumo para prova

### 🔹 Alfabeto

Conjunto finito de símbolos.

```
Σ = {a, b}
```

### 🔹 Cadeia

Sequência de símbolos pertencentes ao alfabeto. Ex.: `ab`

### 🔹 Palavra vazia

```
ε        →        |ε| = 0
```

### 🔹 Σ*

Todas as cadeias finitas possíveis sobre Σ, incluindo ε.

```
Σ* = {ε, a, b, aa, ab, ba, bb, ...}
```

### 🔹 Linguagem

Um conjunto de cadeias:

```
L ⊆ Σ*
```

### 🔹 Prefixo

Começa no início da palavra. Para `ab`: `{ε, a, ab}`

### 🔹 Sufixo

Termina no final da palavra. Para `ab`: `{ε, b, ab}`

### 🔹 Gramática

Define regras para gerar palavras: `S → aS | ε`

### 🔹 →

- Em gramáticas: **produz / gera**
- Em lógica: **implica / se... então**

### 🔹 |

Nas regras de produção significa **OU**:

```
S → aS | ε
```

Ou seja: *S produz `aS` ou `ε`*.

---

## 14. 🧠 Mapa mental

```
                    LINGUAGENS FORMAIS
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
      ALFABETO           CADEIA          LINGUAGEM
          │                │                │
          │                │                └── L ⊆ Σ*
          │                │
          │                └── ε = cadeia vazia
          │
          └── Σ
               │
               └── Σ* = todas as cadeias
                           │
                           ▼
                       GRAMÁTICA
                           │
                           ▼
                    Regras de produção
                           │
                           ▼
                      S → aS | ε
                           │
                           ▼
                ε, a, aa, aaa, ...
```

---

## 📌 Checklist da aula 1

Antes de avançar para a próxima aula, verifique se você consegue explicar:

- [ ] O que é um alfabeto Σ;
- [ ] O que é uma cadeia;
- [ ] O que significa ε;
- [ ] Por que `|ε| = 0`;
- [ ] O que é um prefixo;
- [ ] O que é um sufixo;
- [ ] O que significa Σ*;
- [ ] Se Σ* possui limite de tamanho;
- [ ] O que é uma linguagem formal L;
- [ ] O que significa `L ⊆ Σ*`;
- [ ] O que é uma gramática formal;
- [ ] O que são terminais e não terminais;
- [ ] O que é uma regra de produção;
- [ ] Como ler `S → aS | ε`;
- [ ] Como gerar palavras usando uma gramática.

---

<p align="center">
  <a href="../README.md">⬅ Índice</a> ·
  <a href="aula-02-hierarquia-de-chomsky-e-automatos-finitos.md">Aula 02 ➡</a>
</p>

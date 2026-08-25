# Exercícios Práticos para Fixação — Aula 3

> Os três blocos passados na aula 3 (Gramáticas Formais), resolvidos com justificativa em cada
> item.

**Como montei este arquivo:** copiei o enunciado de cada bloco, escrevi uma linha dizendo do que a
questão trata, e só depois respondi. Assim eu consigo reler sem precisar abrir o slide do lado.

Os três blocos são:

| Bloco | Assunto | O que ele pede |
|:-:|---|---|
| 1 | Derivação | gerar uma palavra e explicar quando a derivação acaba |
| 2 | Gramática livre de contexto | gerar uma palavra e dizer se outra é possível |
| 3 | Classificação | dizer se a gramática é regular ou livre de contexto |

[⬅ voltar para o índice](../README.md) · [📓 notas da Aula 03](Notas_de_Aula.md) ·
[📄 Lista 1 resolvida](Lista1_Resolvida.md)

---

## Bloco 1 — Derivação

### 📌 Enunciado

> Dada:
>
> ```
> G₁:  S → aS | b
> ```
>
> **A)** Gere a palavra `aaab`.
>
> **B)** Explique como você sabe que a derivação terminou.

### 🔎 Do que trata

É a gramática que a professora usou na aula inteira. Ela tem duas regras:

- `S → aS` — coloca um `a` e devolve o `S` pra linha (dá pra repetir quantas vezes eu quiser);
- `S → b` — coloca um `b` e **não** devolve o `S` (é a regra que encerra).

O item A é derivação normal. O item B é o que vale mais atenção, porque pede o **critério de
parada**.

---

### A) Gere a palavra `aaab`

**Como planejei:** olhei a palavra e contei — `aaab` tem **três `a`** e **um `b` no fim**. Como
cada `S → aS` coloca um `a` por vez, já sabia que era aplicar ela três vezes e fechar com `S → b`.

**Resposta:**

```
S ⇒ aS ⇒ aaS ⇒ aaaS ⇒ aaab
```

**Justificativa, passo a passo:**

| Passo | Linha | Regra usada | O que aconteceu |
|:-:|:-:|---|---|
| início | `S` | — | comecei pelo símbolo inicial, como manda a definição |
| 1 | `aS` | `S → aS` | colocou o 1º `a` e devolveu o `S` |
| 2 | `aaS` | `S → aS` | colocou o 2º `a` e devolveu o `S` |
| 3 | `aaaS` | `S → aS` | colocou o 3º `a` e devolveu o `S` |
| 4 | `aaab` | `S → b` | trocou o `S` por `b` e encerrou |

Então:

```
aaab ∈ L(G₁)
```

🧠 A conta que guardei: **quantos `a` a palavra tem = quantas vezes eu aplico `S → aS`**. Se
pedissem `aaaaab` (cinco `a`), seriam cinco aplicações e depois o `S → b`. Vira contagem, e não
tentativa e erro.

---

### B) Explique como você sabe que a derivação terminou

**Resposta: porque na linha final não sobrou nenhuma variável.**

**Justificativa:** o critério é esse, e vale pra qualquer gramática:

> A derivação termina quando não sobra nenhuma variável (nenhum não terminal) na linha.

Aplicando na minha derivação:

| Linha | Terminou? | Por quê |
|:-:|:-:|---|
| `aaaS` | ❌ não | tem o `S`, que é variável — ainda dava (e precisava) trocar |
| `aaab` | ✅ sim | `a` e `b` são terminais, e terminal não tem regra pra trocar |

O `a` e o `b` são os terminais dessa gramática (`T = {a, b}`). Depois que um terminal aparece na
linha, ele fica ali — não existe nenhuma regra tipo "b → alguma coisa".

**Quem fez a derivação parar** foi a regra `S → b`. Das duas regras, ela é a única que **não
devolve** o `S`. A outra, `S → aS`, sempre devolve — então se eu só usasse ela, a derivação nunca
acabaria.

O teste rápido que uso na prova: **procuro maiúscula na linha**. Se achar, não terminou e aquilo
não é resposta. Se só tiver minúscula, terminou e aquilo é uma palavra de verdade da linguagem.

⚠️ Erro que quero evitar: entregar `aaaS` como resposta. Isso **não é palavra**, é uma parada no
meio do caminho.

---

## Bloco 2 — Gramática Livre de Contexto

### 📌 Enunciado

> Dada:
>
> ```
> G₂:  S → aSb | ε
> ```
>
> **A)** Gere a palavra `aaabbb`.
>
> **B)** É possível gerar `aabbb`? Justifique.

### 🔎 Do que trata

Aqui a variável está **no meio** da regra (`aSb`), e não na ponta como no Bloco 1. É por isso que
essa gramática é livre de contexto e não regular.

O efeito prático disso é o que o item B quer que eu perceba: a regra coloca um `a` e um `b` sempre
**juntos**, então a quantidade dos dois sai sempre igual.

As duas regras:

- `S → aSb` — coloca um `a` na esquerda e um `b` na direita, ao mesmo tempo, e devolve o `S` no
  meio;
- `S → ε` — não coloca nada, só apaga o `S` (é a regra que encerra).

---

### A) Gere a palavra `aaabbb`

**Como planejei:** a palavra tem três `a` e três `b`. Como cada `S → aSb` coloca um de cada, são
três aplicações e depois o `S → ε` pra fechar.

**Resposta:**

```
S ⇒ aSb ⇒ aaSbb ⇒ aaaSbbb ⇒ aaabbb
```

**Justificativa, passo a passo:**

| Passo | Linha | Regra usada | O que aconteceu |
|:-:|:-:|---|---|
| início | `S` | — | comecei pelo símbolo inicial |
| 1 | `aSb` | `S → aSb` | colocou o 1º `a` e o 1º `b`, com o `S` no meio |
| 2 | `aaSbb` | `S → aSb` | colocou o 2º `a` e o 2º `b` |
| 3 | `aaaSbbb` | `S → aSb` | colocou o 3º `a` e o 3º `b` |
| 4 | `aaabbb` | `S → ε` | apagou o `S` e encerrou |

O último passo funciona porque o `ε` não ocupa lugar nenhum — `aaaεbbb` é a mesma coisa que
`aaabbb`.

Terminou no passo 4 porque não sobrou nenhuma variável na linha. Então:

```
aaabbb ∈ L(G₂)
```

---

### B) É possível gerar `aabbb`? Justifique

**Resposta: NÃO é possível.**

**Justificativa:** `aabbb` tem **dois `a` e três `b`** — quantidades diferentes. E essa gramática
não consegue fazer quantidades diferentes. O motivo está nas duas regras:

- **`S → aSb`** é a **única** regra que escreve símbolo, e ela sempre coloca **um `a` e um `b`
  juntos, no mesmo passo**. Nunca um sem o outro;
- **`S → ε`** não escreve símbolo nenhum, só encerra.

Então, depois de `n` aplicações de `S → aSb`, eu vou ter sempre `n` letras `a` e `n` letras `b`. A
conta sai sempre empatada:

| Vezes que apliquei `S → aSb` | Palavra gerada | Quantos `a` | Quantos `b` |
|:-:|:-:|:-:|:-:|
| 0 | `ε` | 0 | 0 |
| 1 | `ab` | 1 | 1 |
| 2 | `aabb` | 2 | 2 |
| 3 | `aaabbb` | 3 | 3 |
| 4 | `aaaabbbb` | 4 | 4 |

Ou seja, a linguagem dessa gramática é:

```
L(G₂) = {aⁿbⁿ | n ≥ 0} = {ε, ab, aabb, aaabbb, ...}
```

Pra `aabbb` entrar aí, o `n` teria que valer **2** (por causa dos dois `a`) e **3** (por causa dos
três `b`) **ao mesmo tempo**. E um número não pode ser 2 e 3 de uma vez.

**Testando na mão, pra confirmar:** apliquei `S → aSb` duas vezes e cheguei em `aaSbb`. Desse
ponto só tenho duas saídas:

```
aaSbb ⇒ aabb        (fechei com S → ε — falta um b)
aaSbb ⇒ aaaSbbb     (apliquei aSb de novo — agora sobra um a)
```

Nenhum dos dois caminhos dá `aabbb`, e não existe terceiro caminho, porque a gramática só tem
essas duas regras.

**Conclusão:**

```
aabbb ∉ L(G₂)
```

porque a gramática obriga a mesma quantidade de `a` e de `b`, e nessa palavra as quantidades são
diferentes.

---

## Bloco 3 — Classificação

### 📌 Enunciado

> Classifique como **Regular** ou **Livre de Contexto**:
>
> ```
> S → aA
> A → b
> ```

### 🔎 Do que trata

Essa questão é sobre a Hierarquia de Chomsky. A pegadinha é que as duas classificações
"funcionam" — então eu preciso saber qual das duas é a resposta certa e explicar por quê.

Relembrando os dois formatos:

| Classe | O que ela exige |
|---|---|
| **Regular** (tipo 3) | do lado direito: no máximo uma variável, e ela **na ponta** |
| **Livre de contexto** (tipo 2) | do lado esquerdo: uma variável **sozinha** (o lado direito é livre) |

---

### Minha resposta

**Resposta: gramática Regular (Tipo 3 na Hierarquia de Chomsky).**

**Justificativa:** conferi regra por regra, nos dois lados da seta.

**Passo 1 — olhando o lado esquerdo:**

| Regra | Lado esquerdo | Tem só uma variável sozinha? |
|:-:|:-:|:-:|
| `S → aA` | `S` | ✅ |
| `A → b` | `A` | ✅ |

As duas passam. Então a gramática é **pelo menos** livre de contexto. Sigo pro passo 2 pra ver se
ela é mais apertada que isso.

**Passo 2 — olhando o lado direito:**

| Regra | Lado direito | Formato | Encaixa em regular? |
|:-:|:-:|---|:-:|
| `S → aA` | `aA` | terminal `a` + variável `A` **na ponta** | ✅ |
| `A → b` | `b` | terminal sozinho, sem variável nenhuma | ✅ |

**Todas** as regras cabem no formato regular (`A → aB` ou `A → a`), e em nenhuma delas a variável
aparece no meio. Logo, é **regular**.

⚠️ Detalhe que quase me pegou: tem que valer pra **todas** as regras. Se **uma só** estivesse fora
do formato, a gramática inteira já deixaria de ser regular. Não adianta a maioria estar certa.

---

### Por que não respondo "livre de contexto"

Ela **também** é livre de contexto — toda gramática regular é, porque na hierarquia o tipo 3 está
**dentro** do tipo 2:

```
Tipo 3  ⊂  Tipo 2  ⊂  Tipo 1  ⊂  Tipo 0
regular    livre      sensível   irrestrita
           de ctx     ao ctx
```

Mas a resposta é a classe **mais apertada** em que ela cabe, porque é a que diz mais sobre a
gramática.

🧠 A comparação que uso: todo quadrado é um retângulo. Se me perguntam "que figura é essa?", eu
respondo **quadrado**. Falar "retângulo" não está errado, mas diz menos.

---

### Comparando com o Bloco 2

| Gramática | Onde fica a variável | Classificação |
|---|---|:-:|
| `S → aA`, `A → b` | na ponta (`aA`) | **Regular** |
| `S → aSb \| ε` | no meio (`aSb`) | **Livre de contexto**, e **não** regular |

É essa a diferença toda: **variável na ponta = regular; variável no meio = livre de contexto**. E
ao contrário não vale — a do Bloco 2 é livre de contexto e não é regular, porque o `S` está
espremido entre o `a` e o `b`.

---

### Bônus que eu mesmo conferi

Qual linguagem essa gramática do Bloco 3 gera?

```
S ⇒ aA ⇒ ab
```

Nenhuma regra devolve o `S` ou o `A` pra linha, então não tem como alongar nem escolher outro
caminho. Ela gera uma palavra só:

```
L(G) = {ab}
```

---

## ✅ Resumo das respostas

| Bloco | Item | Resposta |
|:-:|:-:|---|
| 1 | A | `S ⇒ aS ⇒ aaS ⇒ aaaS ⇒ aaab` |
| 1 | B | terminou porque não sobrou variável na linha — quem encerrou foi a regra `S → b` |
| 2 | A | `S ⇒ aSb ⇒ aaSbb ⇒ aaaSbbb ⇒ aaabbb` |
| 2 | B | **não** dá pra gerar `aabbb` — a regra `S → aSb` coloca `a` e `b` em par, então a quantidade sai sempre igual |
| 3 | — | **Regular** (tipo 3) — em todas as regras a variável está na ponta |

---

<p align="center">
  <a href="../README.md">⬅ voltar para o índice</a> ·
  <a href="Notas_de_Aula.md">📓 notas da Aula 03</a> ·
  <a href="Lista1_Resolvida.md">📄 Lista 1 resolvida</a>
</p>

# Expressões Regulares

Anotações da Unidade 3, escritas depois da aula. É o resumo que eu releio antes da prova; o passo a
passo da regex de e-mail está na atividade.

Conteúdo:

1. O que é uma expressão regular
2. Onde ela entra na Hierarquia de Chomsky
3. Os símbolos básicos
4. Âncoras
5. Como ler uma regex
6. O que regex não consegue fazer
7. Revisão para prova

---

## 1. O que é uma expressão regular

É um padrão que descreve um conjunto de palavras, ou seja, uma linguagem. Em vez de listar as
palavras, eu escrevo a regra que elas seguem.

```
padrão    ab*
aceita    a, ab, abb, abbb, ...
recusa    b, ba, aab
```

A diferença para a gramática da Unidade 2 é a direção. A gramática gera palavras a partir do S. A
regex recebe uma palavra pronta e responde se ela pertence ou não.

---

## 2. Onde ela entra na Hierarquia de Chomsky

Regex descreve exatamente as linguagens regulares, o tipo 3. É o mesmo tipo da gramática regular,
aquela em que toda regra tem no máximo um terminal seguido de uma variável, como S → aS | b.

```
S → aS | b      gramática regular
a*b             a regex da mesma linguagem
```

As duas descrevem "qualquer quantidade de a e um b no final". É a mesma linguagem escrita de dois
jeitos.

---

## 3. Os símbolos básicos

```
a         o próprio símbolo a
.         qualquer símbolo (para o ponto de verdade: \.)
[abc]     um símbolo da lista
[a-z]     um símbolo do intervalo
[^0-9]    qualquer símbolo que NÃO esteja na lista
*         zero ou mais vezes o que vem antes
+         uma ou mais vezes
?         zero ou uma vez
{n}       exatamente n vezes
{n,}      n ou mais vezes
a|b       a ou b
( )       agrupa
\d        um dígito, igual a [0-9]
\s        espaço
```

O que eu mais confundia era * com +. O * aceita zero, então a* aceita a palavra vazia. O + exige pelo
menos um.

---

## 4. Âncoras

```
^    começo da palavra
$    fim da palavra
```

Sem elas a regex procura o padrão em qualquer pedaço do texto. \d{3} acha 123 dentro de abc123xyz.
Com ^\d{3}$ só a palavra inteira 123 passa.

Em Python, fullmatch já faz o papel das duas âncoras.

---

## 5. Como ler uma regex

Leio da esquerda para a direita, um pedaço por vez, e pergunto o que cada pedaço aceita.

```
^[A-Z][a-z]+$
^          começa aqui
[A-Z]      uma letra maiúscula
[a-z]+     uma ou mais minúsculas
$          acaba aqui

aceita     Maria, Brasil
recusa     maria, MARIA, M
```

---

## 6. O que regex não consegue fazer

Regex não tem memória. Ela não consegue contar e depois conferir a contagem.

```
0ⁿ1ⁿ      mesma quantidade de 0 e de 1: regex NÃO consegue
0*1*      qualquer quantidade de 0 seguida de qualquer quantidade de 1: consegue
```

Para 0ⁿ1ⁿ precisa subir na hierarquia: é livre de contexto (tipo 2). Isso volta na Unidade 4, com a
Máquina de Turing.

---

## 7. Revisão para prova

```
regex             padrão que reconhece uma linguagem regular (tipo 3)
gramática         gera; regex reconhece
* e +             * aceita zero vezes, + exige pelo menos uma
\.                ponto de verdade; . sozinho é qualquer símbolo
^ e $             prendem o padrão no começo e no fim
limite            não conta; 0ⁿ1ⁿ não é regular
```

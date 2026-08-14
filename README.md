<h1 align="center">Inteligência Artificial</h1>
<h3 align="center">Linguagens Formais e Autômatos</h3>

<p align="center">
  Caderno de estudos da disciplina — Engenharia de Software · 6º semestre
</p>

<p align="center">
  <img src="https://img.shields.io/badge/curso-Engenharia%20de%20Software-0b7285?style=flat-square" alt="Curso">
  <img src="https://img.shields.io/badge/semestre-6º-343a40?style=flat-square" alt="Semestre">
  <img src="https://img.shields.io/badge/disciplina-IA%20%2F%20LFA-5f3dc4?style=flat-square" alt="Disciplina">
  <img src="https://img.shields.io/badge/status-em%20andamento-2b8a3e?style=flat-square" alt="Status">
</p>

---

## Sobre este repositório

Aqui eu guardo tudo que vou produzindo na disciplina: as anotações que faço em aula, os exercícios
resolvidos e os resumos que uso para estudar antes das provas.

A ideia não é ser um livro. É ser o material que **eu** consigo ler três dias antes da prova e
entender de novo — por isso quase tudo está escrito com as minhas palavras, com os exemplos que o
professor passou em sala e alguns que eu inventei quando não entendi de primeira.

Se você caiu aqui por acaso e está fazendo a mesma matéria: fique à vontade, mas confira com o
material oficial do seu professor. Notação em Linguagens Formais muda um pouco de autor para autor.

---

## Por que "IA" e "Linguagens Formais" juntos?

Essa foi a primeira dúvida que eu tive quando vi a ementa. A resposta curta:

> Antes de uma máquina *raciocinar*, ela precisa **reconhecer**.

Linguagens Formais e Autômatos são a base formal de boa parte da computação simbólica: definem o que
é uma linguagem, como descrevê-la com regras finitas e que tipo de máquina consegue reconhecê-la.
Isso aparece direto em:

| Área | Onde a teoria entra |
|---|---|
| Compiladores | análise léxica (autômatos) e análise sintática (gramáticas) |
| Processamento de Linguagem Natural | gramáticas formais, parsing, modelos de sequência |
| Busca e agentes | estados, transições e espaço de estados |
| Validação de dados | expressões regulares, protocolos, formatos |
| Teoria da computação | o que é (e o que não é) computável |

Ou seja: é a parte "matemática" da IA, a que sustenta o resto.

---

## Índice das aulas

| # | Aula | Assunto | Status |
|:-:|---|---|:-:|
| 01 | [Linguagens Formais e Gramáticas](aulas/aula-01-linguagens-formais-e-gramaticas.md) | Alfabeto, cadeias, ε, prefixos/sufixos, Σ\*, linguagem formal, gramáticas e derivação | ✅ |
| 02 | [Hierarquia de Chomsky e Autômatos Finitos](aulas/aula-02-hierarquia-de-chomsky-e-automatos-finitos.md) | Tipos 0–3, AFD, AFN, tabela de transição, palavras aceitas e rejeitadas | ✅ |

Cada aula segue sempre a mesma estrutura, para eu não me perder:

```
Sumário → Objetivos → Conteúdo → Exemplos → Atividades (com gabarito) → Revisão para prova
```

---

## Organização dos arquivos

```
.
├── README.md                  ← você está aqui
└── aulas/
    ├── aula-01-linguagens-formais-e-gramaticas.md
    └── aula-02-hierarquia-de-chomsky-e-automatos-finitos.md
```

Conforme a disciplina avança eu vou adicionando `aula-03`, `aula-04`, e provavelmente uma pasta
`exercicios/` separada quando as listas ficarem grandes demais para caber dentro da aula.

---

## Legenda de símbolos

Deixo essa tabela aqui no README porque no começo eu travava justamente na notação, não no conceito.

| Símbolo | Nome | Significa |
|:-:|---|---|
| `Σ` | sigma | alfabeto — conjunto finito de símbolos |
| `Σ*` | sigma estrela | todas as cadeias finitas formadas com Σ (inclui ε) |
| `ε` | épsilon | palavra vazia, com zero símbolos |
| `L` | — | linguagem formal, um subconjunto de Σ* |
| `\|w\|` | comprimento | quantidade de símbolos da cadeia `w` |
| `→` | produz / implica | em gramática: "gera"; em lógica: "se... então" |
| `\|` | ou | separa alternativas numa regra de produção |
| `⊆` | contido em | `L ⊆ Σ*` = toda palavra de L está em Σ* |
| `δ` | delta | função de transição de um autômato |

---

## Como eu estudo com esse material

1. Leio o **conteúdo** da aula uma vez, sem parar para anotar.
2. Refaço as **atividades** com o gabarito tapado.
3. Leio só a seção **revisão para prova** no dia anterior.
4. Se travar em algum item do **checklist** no fim da aula, volto direto naquela seção.

Funciona melhor do que reler tudo do começo, que era o que eu fazia antes e não rendia nada.

---

## Referências que estou usando

- Anotações e slides das aulas da disciplina
- HOPCROFT, MOTWANI, ULLMAN — *Introduction to Automata Theory, Languages, and Computation*
- MENEZES, P. B. — *Linguagens Formais e Autômatos*
- SIPSER, M. — *Introduction to the Theory of Computation*

---

<p align="center">
  <sub>Repositório pessoal de estudos · atualizado conforme as aulas acontecem</sub>
</p>

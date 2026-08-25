<h1 align="center">Inteligência Artificial</h1>
<h3 align="center">Linguagens Formais e Autômatos</h3>

<p align="center">
  Caderno de estudos da disciplina — Engenharia de Software · 6º semestre
</p>

<p align="center">
  <img src="https://img.shields.io/badge/curso-Engenharia%20de%20Software-0b7285?style=flat-square" alt="Curso">
  <img src="https://img.shields.io/badge/semestre-6º-343a40?style=flat-square" alt="Semestre">
  <img src="https://img.shields.io/badge/unidades-1%20e%202-5f3dc4?style=flat-square" alt="Unidades">
  <img src="https://img.shields.io/badge/status-em%20andamento-2b8a3e?style=flat-square" alt="Status">
</p>

---

## Sobre este repositório

Aqui eu guardo o que vou produzindo na disciplina: as anotações que faço a partir das aulas, os
exercícios resolvidos e os resumos que uso pra estudar antes da prova.

A ideia não é copiar o material da professora — é reescrever o conteúdo com as minhas palavras, do
jeito que eu consigo reler três dias antes da prova e entender de novo. Por isso tem macete,
analogia e comparação que eu mesmo montei enquanto estudava.

---

## Conteúdo

| Unidade | Aula | Assunto | Status |
|:-:|:-:|---|:-:|
| 1 | 02 | [Notas de Aula — Linguagens Formais e Gramáticas](Unidade1_LinguagensFormais/Notas_de_Aula.md) | ✅ |
| 2 | 03 | [Notas de Aula — Gramáticas Formais e Hierarquia de Chomsky](Unidade2_GramaticasFormais/Notas_de_Aula.md) | ✅ |
| 2 | — | [Lista 1 — resolvida e justificada](Unidade2_GramaticasFormais/Lista1_Resolvida.md) | ✅ |

Os arquivos de notas seguem o formato pedido na entrega:

```
Sumário → Objetivos → Conteúdo → Exemplos → Exercícios → Revisão para prova
```

E ainda tem mapa mental e checklist no fim, pra fechar a revisão.

---

## Organização dos arquivos

```
.
├── README.md                         ← você está aqui
├── Unidade1_LinguagensFormais/
│   └── Notas_de_Aula.md              ← aula 02 · anotações + exercícios resolvidos
└── Unidade2_GramaticasFormais/
    ├── Notas_de_Aula.md              ← aula 03 · anotações + exercícios de fixação
    └── Lista1_Resolvida.md           ← lista da unidade, com justificativa em toda questão
```

Conforme a disciplina avança eu vou criando as próximas unidades seguindo a mesma organização.

---

## Legenda de símbolos

Deixo essa tabela aqui no README porque no começo o que me travou foi a notação, não o conceito.

| Símbolo | Nome | Significa |
|:-:|---|---|
| `Σ` | sigma | alfabeto — conjunto finito de símbolos |
| `Σ*` | sigma estrela | todas as cadeias possíveis com Σ, incluindo ε |
| `ε` | épsilon | palavra vazia, com zero símbolos |
| `L` | — | linguagem formal, um subconjunto de Σ* |
| `\|w\|` | comprimento | quantidade de símbolos da cadeia |
| `⊆` | contido em | `L ⊆ Σ*` — toda palavra de L está em Σ* |
| `→` | produz / implica | em gramática: "gera"; em lógica: "se... então" |
| `\|` | ou | separa as alternativas de uma regra de produção |
| `⇒` | deriva em | um **passo** da derivação — diferente do `→`, que é a regra |
| `G` | gramática | `G = (V, T, P, S)` — variáveis, terminais, produções e símbolo inicial |
| `L(G)` | linguagem gerada | o conjunto de todas as palavras que a gramática `G` produz |
| `∅` | conjunto vazio | linguagem sem nenhuma palavra — não confundir com `{ε}` |

---

## Como eu estudo com esse material

1. Leio o **conteúdo** uma vez inteiro, sem parar pra anotar.
2. Refaço os **exercícios** com o gabarito fechado (deixei em blocos recolhíveis justamente pra isso).
3. Na véspera, leio só a **revisão para prova**.
4. Se travar em algum item do **checklist**, volto direto naquela seção.

Rende bem mais do que reler tudo do começo, que era o que eu fazia antes.

---

<p align="center">
  <sub>Repositório pessoal de estudos · atualizado conforme as aulas acontecem</sub>
</p>

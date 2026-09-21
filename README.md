# Inteligência Artificial - Linguagens Formais e Autômatos

Caderno de estudos da disciplina. Engenharia de Software, 6º semestre.

## Sobre

Aqui eu guardo o que vou produzindo na disciplina: as anotações que faço a partir das aulas, os
exercícios resolvidos e os resumos que uso para estudar antes da prova.

A ideia não é copiar o material da professora, é reescrever o conteúdo com as minhas palavras, do
jeito que eu consigo reler três dias antes da prova e entender de novo.

## Conteúdo

Unidade 1 - Linguagens Formais

- [Notas de aula 02 - Linguagens formais e gramáticas](Unidade1_LinguagensFormais/Notas_de_Aula.md)

Unidade 2 - Gramáticas Formais

- [Notas de aula 03 - Gramáticas formais e Hierarquia de Chomsky](Unidade2_GramaticasFormais/Notas_de_Aula.md)
- [Exercícios práticos da aula 3 - resolvidos](Unidade2_GramaticasFormais/Exercicios_Praticos_Aula3.md)
- [Lista 1 - resolvida](Unidade2_GramaticasFormais/Lista1_Resolvida.md)

Unidade 3 - Expressões Regulares

- [Atividade prática - Regex para validação de e-mail](Unidade3_ExpressoesRegulares/Atividade_Pratica_Regex_Email.md)

## Organização dos arquivos

```
.
├── README.md
├── Unidade1_LinguagensFormais/
│   └── Notas_de_Aula.md              aula 02, anotações e exercícios
├── Unidade2_GramaticasFormais/
│   ├── Notas_de_Aula.md              aula 03, anotações
│   ├── Exercicios_Praticos_Aula3.md  os 3 blocos da aula, resolvidos
│   └── Lista1_Resolvida.md           a lista da unidade, resolvida
└── Unidade3_ExpressoesRegulares/
    ├── Atividade_Pratica_Regex_Email.md   a atividade resolvida e explicada
    └── validador_email.py                 o código que eu entreguei
```

Quando a atividade for de código, o programa fica em um arquivo separado e o `.md` do lado explica
o raciocínio, como nas outras. O arquivo de anotações continua sendo o que eu releio antes da prova.

Conforme a disciplina avança eu vou criando as próximas unidades seguindo a mesma organização.

## Legenda de símbolos

Deixo essa tabela aqui porque no começo o que me travou foi a notação, não o conceito.

```
Σ       alfabeto, conjunto finito de símbolos
Σ*      todas as palavras possíveis com Σ, incluindo ε
ε       palavra vazia, com zero símbolos
∅       conjunto vazio, linguagem sem nenhuma palavra
L       linguagem formal, um subconjunto de Σ*
|w|     comprimento, quantidade de símbolos da palavra
⊆       contido em
∈       pertence a
∉       não pertence a
G       gramática, G = (V, T, P, S)
V       variáveis ou não terminais
T       terminais
P       produções, as regras
S       símbolo inicial
→       produz, em gramática; implica, em lógica
⇒       deriva em, um passo da derivação
|       ou, separa as alternativas de uma regra
L(G)    linguagem gerada pela gramática G
```

## Como eu estudo com esse material

1. Leio o conteúdo uma vez inteiro, sem parar para anotar.
2. Refaço os exercícios com o gabarito fechado.
3. Na véspera, leio só a revisão para prova.
4. Se travar em algum ponto, volto direto naquela seção.

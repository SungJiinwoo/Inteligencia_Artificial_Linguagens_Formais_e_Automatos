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

- [Notas de aula - Expressões regulares](Unidade3_ExpressoesRegulares/Notas_de_Aula.md)
- [Atividade prática - Regex para validação de e-mail](Unidade3_ExpressoesRegulares/Atividade_Pratica_Regex_Email.md)

Unidade 4 - Máquinas de Turing

- [Notas de aula 09 - Máquinas de Turing](Unidade4_MaquinaDeTuring/Notas_de_Aula.md)
- [Atividade 5 - Máquina de Turing para 0ⁿ1ⁿ](Unidade4_MaquinaDeTuring/Atividade_5_Maquina_de_Turing.md)

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
├── Unidade3_ExpressoesRegulares/
│   ├── Notas_de_Aula.md                   resumo da aula de regex
│   ├── Atividade_Pratica_Regex_Email.md   a atividade resolvida e explicada
│   └── validador_email.py                 o código que eu entreguei
└── Unidade4_MaquinaDeTuring/
    ├── Notas_de_Aula.md                   aula 09, anotações do vídeo
    ├── Atividade_5_Maquina_de_Turing.md   as 4 etapas e a questão final
    ├── maquina_turing.py                  o simulador que eu escrevi
    ├── testar_maquina.py                  teste com todas as palavras até 10 símbolos
    ├── Atividade_5_..._entrega.pdf        o PDF que eu entreguei
    └── capturas/                          prints dos 3 testes
```

Quando a atividade for de código, o programa fica em um arquivo separado e o `.md` do lado explica
o raciocínio, como nas outras. O arquivo de anotações continua sendo o que eu releio antes da prova.

Conforme a disciplina avança eu vou criando as próximas unidades seguindo a mesma organização.

## Como rodar os códigos

Precisa só do Python 3, não usa biblioteca de fora. Rodo sempre de dentro da pasta da unidade:

```
cd Unidade3_ExpressoesRegulares
python validador_email.py              pede os 5 e-mails e separa válidos e inválidos

cd Unidade4_MaquinaDeTuring
python maquina_turing.py 0011          mostra a fita passo a passo e diz ACEITA ou REJEITA
python maquina_turing.py               sem argumento, roda os 3 testes da atividade
python testar_maquina.py               confere a máquina com todas as palavras até 10 símbolos
```

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

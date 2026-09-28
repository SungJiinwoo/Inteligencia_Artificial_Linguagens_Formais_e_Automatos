# Aula 09 - Máquinas de Turing

Anotações da Unidade 4. Essa aula foi remota: o material era o vídeo Akitando #86, "O Computador de
Turing e Von Neumann: Por que calculadoras não são computadores?". Assisti e fui anotando.

Conteúdo:

1. De onde veio a ideia
2. As partes de uma Máquina de Turing
3. Como a máquina roda
4. Turing completo
5. O que não dá pra computar
6. Calculadora não é computador
7. Ligação com o resto da matéria
8. Revisão para prova

---

## 1. De onde veio a ideia

Turing publicou a máquina em 1936, num artigo sobre números computáveis. A ideia partiu de uma
máquina de escrever: uma folha que corre, uma posição onde o próximo símbolo vai cair e um número
pequeno de configurações (maiúscula ou minúscula).

Ele pegou isso e levou ao extremo. Uma fita que não acaba, uma cabeça que além de escrever também lê
e apaga, e um conjunto finito de estados.

O objetivo dele não era construir um computador. Era responder uma pergunta de matemática: dá pra
ter um procedimento mecânico que decide qualquer problema? Para responder isso ele precisava definir
o que é "procedimento mecânico", e a máquina é essa definição.

---

## 2. As partes de uma Máquina de Turing

```
fita       dividida em células, infinita; cada célula guarda um símbolo ou fica em branco
cabeça     fica em cima de uma célula; lê, escreve e anda uma casa para esquerda ou direita
estados    conjunto finito; a máquina está sempre em exatamente um deles
alfabeto   os símbolos que podem aparecer na fita (inclusive o branco)
transição  a tabela de regras: (estado, símbolo lido) -> (símbolo escrito, movimento, novo estado)
```

A fita é ao mesmo tempo entrada, memória e saída. Não tem outro lugar para guardar nada.

---

## 3. Como a máquina roda

Cada passo é sempre igual:

```
1. lê o símbolo embaixo da cabeça
2. procura a regra para (estado atual, símbolo lido)
3. escreve o símbolo da regra
4. anda uma casa
5. troca para o estado da regra
```

E repete. Ela para em dois casos: chegou num estado de aceitação, ou não existe regra para a
situação em que ela está. No segundo caso a palavra é rejeitada.

O exemplo do vídeo foi somar 1 a um número binário. A máquina anda até o fim do número, volta
trocando 1 por 0 enquanto tiver "vai um", e quando acha um 0 (ou branco) escreve 1 e termina.

---

## 4. Turing completo

Uma linguagem ou máquina é Turing completa quando consegue simular qualquer Máquina de Turing.

```
Turing completas        Python, Java, C, Lisp, até Brainfuck
não Turing completas    expressão regular, HTML, XML
```

A expressão regular não é porque só anda para um lado e não tem onde guardar o que já viu. Foi aqui
que a Unidade 3 fez sentido de novo: regex reconhece linguagem regular, tipo 3, e a Máquina de
Turing está no topo da hierarquia, tipo 0.

Detalhe que eu não sabia: nenhum computador real é Turing completo no sentido estrito, porque a
memória dele acaba e a fita não. Na prática ninguém liga para isso.

---

## 5. O que não dá pra computar

Turing provou que não existe uma máquina que olhe para qualquer outra máquina e diga se ela vai
parar ou ficar em loop para sempre. É o problema da parada.

Não é que ninguém achou o algoritmo ainda. É provado que ele não existe. Então existe um limite
para o que um algoritmo consegue fazer, e ele não depende de computador mais rápido.

---

## 6. Calculadora não é computador

Essa foi a parte do título do vídeo.

```
Babbage    cartões perfurados guardavam o programa, a máquina guardava os números; separados
Zuse (Z3)  programável, mas sem desvio condicional de verdade
Colossus   eletrônico e rápido, mas feito só para quebrar uma cifra
ENIAC      reprogramar era trocar cabo de lugar
```

Todos eram calculadoras muito boas, cada uma para uma tarefa.

A virada foi a arquitetura de Von Neumann (1945): programa e dados ficam na mesma memória. Aí trocar
de tarefa é só carregar outro programa. É isso que transforma a Máquina de Turing, que era só teoria,
em computador de verdade.

```
Turing         a teoria: o que é computar e até onde dá pra ir
Von Neumann    a engenharia: como construir uma máquina que roda qualquer programa
```

---

## 7. Ligação com o resto da matéria

```
tipo 3   gramática regular         reconhecida por autômato finito / regex
tipo 2   livre de contexto         reconhecida por autômato com pilha
tipo 1   sensível ao contexto      reconhecida por autômato linearmente limitado
tipo 0   irrestrita                reconhecida por Máquina de Turing
```

Por isso a atividade pede 0ⁿ1ⁿ. Essa linguagem não é regular, uma regex não consegue contar quantos
0 vieram para conferir com os 1. A Máquina de Turing consegue, porque pode voltar na fita e marcar
o que já contou.

---

## 8. Revisão para prova

```
Máquina de Turing   fita infinita + cabeça + estados finitos + tabela de transições
quando para         estado de aceitação, ou nenhuma regra serve (rejeita)
Turing completo     consegue simular qualquer Máquina de Turing
problema da parada  não existe algoritmo que decida se qualquer programa para
Von Neumann         programa e dados na mesma memória
calculadora         faz uma tarefa fixa; computador roda qualquer programa
```

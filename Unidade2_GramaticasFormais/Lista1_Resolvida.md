# Lista 1 - Resolvida

Exercícios de Linguagens Formais: alfabeto, palavras, linguagens e gramáticas.

Resolvi os "exercícios para o estudante" da lista, um por um, justificando cada resposta. Copiei o
enunciado inteiro de cada questão antes de responder, para não precisar ficar abrindo a lista do
lado.

Primeiro fiz tudo com o gabarito fechado, escrevendo o raciocínio. Depois abri para conferir.
Escrevi a justificativa até nas questões fáceis, porque na prova é ela que vale ponto.

Questões:

1. Alfabeto
2. Palavras sobre um alfabeto
3. Símbolo ou palavra
4. Linguagem
5. Linguagem descrita por um padrão
6. Linguagem vazia e palavra vazia
7. As partes de uma gramática
8. Aplicando uma produção
9. Derivação completa de uma palavra
10. A palavra pode ser gerada
11. Desafio final

---

## 1. Alfabeto

Enunciado:

```
Considere Σ = {a, b, c} e responda:

1. Quantos símbolos existem no alfabeto?
2. Quais são os símbolos?
3. O símbolo a pertence ao alfabeto?
4. O símbolo d pertence ao alfabeto?
5. Escreva uma palavra formada por símbolos desse alfabeto.
```

Essa é a questão mais básica da lista. Ela quer ver se eu sei ler a linha Σ = {a, b, c} e entender
que ali dentro estão os símbolos que eu posso usar, e só eles.

**1.1 Quantos símbolos existem no alfabeto?**

São 3 símbolos. É só contar o que está dentro das chaves: a, b e c. O alfabeto é sempre finito, ou
seja, essa contagem sempre acaba. Não existe alfabeto com infinitos símbolos.

**1.2 Quais são os símbolos?**

São a, b e c, exatamente os que aparecem dentro das chaves. Cada um deles é um símbolo sozinho, e
não uma palavra.

**1.3 O símbolo a pertence ao alfabeto?**

Sim, a ∈ Σ. O a está escrito na lista {a, b, c}. Lê-se "a pertence a Sigma".

**1.4 O símbolo d pertence ao alfabeto?**

Não, d ∉ Σ. O d não está na lista {a, b, c}. O alfabeto vale só pelo que foi escrito nele, então se
o símbolo não aparece ali, ele está de fora.

**1.5 Escreva uma palavra formada por símbolos desse alfabeto**

Escrevi abc. Palavra é uma sequência de símbolos do alfabeto, e em abc os três símbolos estão em Σ,
então a palavra é válida.

Outras respostas também valeriam: a, ab, cab, bbb, ccca. Não precisa usar todos os símbolos, nem
usar cada um uma vez só. A única regra é não entrar símbolo de fora.

---

## 2. Palavras sobre um alfabeto

Enunciado:

```
Considere Σ = {0, 1}.

Classifique cada sequência como palavra válida ou não válida, justificando:

0101
00110
012
111
10a
```

Aqui o alfabeto mudou, agora só valem 0 e 1. A questão quer ver se eu confiro símbolo por símbolo
antes de dizer que a sequência é uma palavra.

Minhas respostas:

- 0101 - válida. Todos os símbolos são 0 ou 1, e os dois estão em Σ.
- 00110 - válida. Mesma coisa, só usa 0 e 1.
- 012 - não válida. O 2 não está em Σ, e basta um símbolo de fora para estragar a sequência inteira.
- 111 - válida. O 1 está em Σ, e repetir o mesmo símbolo pode.
- 10a - não válida. O a não está em Σ = {0, 1}.

O raciocínio que usei nas cinco foi o mesmo: li cada sequência símbolo por símbolo e perguntei se
aquele símbolo está em Σ. Se todos estiverem, é palavra válida. Se um só não estiver, já reprova.

Um detalhe que anotei: repetir símbolo não é problema. O 111 é válido porque o que importa é quais
símbolos aparecem, e não quantas vezes cada um aparece.

---

## 3. Símbolo ou palavra

Enunciado:

```
Considere Σ = {0, 1}.

Determine se as afirmações são verdadeiras ou falsas. Justifique cada resposta.

1. 0 ∈ Σ
2. 1 ∈ Σ
3. 01 ∈ Σ
4. 01 ∈ Σ*
5. 2 ∈ Σ
6. 101 ∈ Σ*
```

Essa é a questão que separa símbolo de palavra. O Σ guarda símbolos soltos, e o Σ* guarda as
palavras que eu monto com esses símbolos. Os itens 3 e 4 usam a mesma coisa (01) e têm respostas
diferentes, e isso é de propósito.

**3.1 - 0 ∈ Σ**

Verdadeiro. O 0 é um dos dois símbolos escritos em Σ = {0, 1}.

**3.2 - 1 ∈ Σ**

Verdadeiro. Mesma coisa, o 1 também está na lista.

**3.3 - 01 ∈ Σ**

Falso. Essa é a pegadinha. O 01 tem dois símbolos, então é uma palavra, e não um símbolo sozinho. O
Σ só tem símbolos soltos, que são o 0 e o 1, e o 01 não é um deles.

**3.4 - 01 ∈ Σ***

Verdadeiro. O Σ* é o conjunto de todas as palavras que dá pra montar com os símbolos de Σ. Como o 0
e o 1 estão no alfabeto, a palavra 01 pode ser montada e está em Σ*.

Comparando 3.3 com 3.4, o mesmo 01 é falso num item e verdadeiro no outro, e o que mudou foi só a
estrelinha. O Σ guarda símbolos soltos, e o Σ* guarda palavras montadas com esses símbolos.

**3.5 - 2 ∈ Σ**

Falso. O 2 não aparece em Σ = {0, 1}. E vale notar que ele também não está em Σ*, porque nenhuma
palavra desse alfabeto pode ter um símbolo que não pertence a ele.

**3.6 - 101 ∈ Σ***

Verdadeiro. Os três símbolos de 101, que são 1, 0 e 1, estão em Σ. Então dá pra montar essa palavra
e ela está em Σ*.

---

## 4. Linguagem

Enunciado:

```
Considere a linguagem L = {0, 01, 011, 0111}.

Determine se cada palavra pertence à linguagem:

1. 0 ∈ L
2. 01 ∈ L
3. 0111 ∈ L
4. 10 ∈ L
5. 111 ∈ L
6. 011 ∈ L
```

Aqui a linguagem foi dada com as palavras escritas uma a uma, dentro das chaves. Então não tem regra
para deduzir nada, é conferir se a palavra está na lista ou não.

Minhas respostas:

- 0 ∈ L - sim, o 0 está escrito na lista.
- 01 ∈ L - sim, o 01 está escrito na lista.
- 0111 ∈ L - sim, o 0111 está escrito na lista.
- 10 ∈ L - não. O 10 não está na lista. A ordem importa, e aqui o 1 vem antes do 0.
- 111 ∈ L - não. O 111 não está na lista, e todas as palavras dessa linguagem começam com 0,
  enquanto essa começa com 1.
- 011 ∈ L - sim, o 011 está escrito na lista.

Do item 4 anotei que o 10 usa os mesmos símbolos que o 01, só que em outra ordem. Palavra é uma
sequência, então mudou a ordem, mudou a palavra.

O item 5 quase me pegou, porque 111 parece com 0111, já que tem os três 1. Mas falta o 0 da frente.
Não vale ser parecido: ou a palavra é igualzinha a uma da lista, ou ela não pertence.

---

## 5. Linguagem descrita por um padrão

Enunciado:

```
Considere L = {bⁿ | n ≥ 1}.

1. Escreva as cinco primeiras palavras.
2. Explique o significado de bⁿ.
3. A palavra bbbbbb pertence à linguagem?
4. A palavra vazia (ε) pertence à linguagem?
```

Nas questões anteriores a linguagem veio com as palavras escritas uma a uma. Aqui não dá pra fazer
isso, porque a linguagem é infinita, então ela foi descrita com uma regra: bⁿ, com a condição n ≥ 1.

Lembrando a leitura da barra: {bⁿ | n ≥ 1} se lê "as palavras bⁿ tal que n é maior ou igual a 1".

**5.1 Escreva as cinco primeiras palavras**

```
b
bb
bbb
bbbb
bbbbb
```

O bⁿ quer dizer n letras b, e a condição diz que o n começa em 1. Então é só ir subindo: b¹ é b, b²
é bb, b³ é bbb, e assim por diante.

**5.2 Explique o significado de bⁿ**

O bⁿ quer dizer n letras b, uma atrás da outra.

O desenho é o mesmo da potência da matemática, mas aqui não é multiplicação. O b³ não vale "b vezes
b vezes b", vale a palavra bbb, que tem 3 letras. Outro jeito de ver: o número de cima é o tamanho
da palavra, ou seja, |bⁿ| = n.

**5.3 A palavra bbbbbb pertence à linguagem?**

Sim. Contei as letras e são seis b, então bbbbbb é o mesmo que b⁶. Como 6 ≥ 1, ela obedece a
condição da linguagem.

O que percebi: essa linguagem nunca acaba. Não importa quantos b eu escreva, sempre cabe mais um. É
por isso que ela foi escrita com uma regra e não palavra por palavra, porque listar todas seria
impossível.

**5.4 A palavra vazia (ε) pertence à linguagem?**

Não, ε ∉ L. O ε é a palavra que não tem símbolo nenhum, ou seja, seria b⁰, com n = 0. Só que a
condição exige n ≥ 1, e o zero não é maior nem igual a 1. Então o ε fica de fora.

Anotação importante: se a condição fosse n ≥ 0, a resposta viraria sim e o ε entraria. Um número
mudando na condição muda a linguagem inteira, e dá pra perder ponto fácil aqui se eu ler correndo.

---

## 6. Linguagem vazia e palavra vazia

Enunciado:

```
Explique, com suas próprias palavras, a diferença entre:

A) L = ∅
B) L = {ε}

Depois responda:

1. Qual delas possui uma palavra?
2. Qual delas não possui nenhuma palavra?
3. Qual é o comprimento da palavra ε?
```

Os dois casos têm a palavra "vazia" no nome, e é aí que a gente se confunde. A questão quer que eu
mostre que "vazio" está falando de coisas diferentes em cada um.

**A diferença, do meu jeito**

O L = ∅ é uma caixa vazia. O L = {ε} é uma caixa com uma folha em branco dentro.

O L = ∅ é a linguagem vazia: ela não tem palavra nenhuma. Se eu perguntar quantas palavras tem aí, a
resposta é zero.

O L = {ε} é uma linguagem que tem uma palavra, e essa palavra é o ε, que não tem símbolo nenhum. Se
eu perguntar quantas palavras tem aí, a resposta é uma.

A confusão está aqui: em A, o que está vazio é a linguagem, ou seja, a caixa. Em B, o que está vazio
é a palavra, ou seja, a folha. E a caixa de B não está vazia, porque tem a folha dentro. Por isso
∅ ≠ {ε}.

**6.1 Qual delas possui uma palavra?**

A B, L = {ε}. Tem exatamente uma coisa escrita dentro das chaves, que é o ε. Uma coisa dentro é uma
palavra.

**6.2 Qual delas não possui nenhuma palavra?**

A A, L = ∅. O ∅ é o símbolo do conjunto vazio, que não tem nada dentro. Sem nada dentro, sem
palavra.

**6.3 Qual é o comprimento da palavra ε?**

Zero, |ε| = 0. Comprimento é a contagem de símbolos da palavra, e o ε não tem símbolo nenhum para
contar.

Lembrete que já tinha anotado na unidade passada e vale repetir: o ε não é espaço em branco. Espaço
seria um símbolo, e aí contaria. O ε é a falta total de símbolo.

---

## 7. As partes de uma gramática

Enunciado:

```
Considere G = ({S, A}, {0, 1}, P, S) com P = {S → 0A, A → 1}.

Identifique:

1. O conjunto de variáveis.
2. O conjunto de terminais.
3. O conjunto de produções.
4. O símbolo inicial.
5. Qual palavra pode ser gerada por essa gramática?
```

Aqui começa a parte de gramática. Toda gramática tem quatro partes e elas aparecem sempre na mesma
ordem, que é G = (V, T, P, S). A questão quer ver se eu sei encaixar os valores dados em cada uma.

Antes de responder, fiz o encaixe:

```
G = ( {S, A} , {0, 1} , P , S )
        V         T      P   S
```

**7.1 O conjunto de variáveis**

V = {S, A}. É a primeira parte, e bate com o resto: S e A estão em maiúscula, e são justamente os
que aparecem do lado esquerdo das regras, ou seja, os que ainda vão ser trocados por outra coisa.

**7.2 O conjunto de terminais**

T = {0, 1}. É a segunda parte. São os símbolos que ficam na palavra pronta. Repara que nenhuma regra
começa com eles, não existe nada como "0 → alguma coisa", porque terminal não é trocado.

**7.3 O conjunto de produções**

P = {S → 0A, A → 1}, que são as duas regras dadas no enunciado. A primeira se lê "S produz 0A", ou
"S pode ser trocado por 0A". A segunda se lê "A produz 1".

**7.4 O símbolo inicial**

É o S, que é a quarta parte. É por ele que a derivação começa, e faz sentido, porque é o único que
tem uma regra para abrir a palavra.

**7.5 Qual palavra pode ser gerada por essa gramática?**

A palavra 01. Derivei passo a passo, começando pelo símbolo inicial:

```
início    S      ainda tem variável (o S)
passo 1   0A     apliquei S → 0A, ainda tem variável (o A)
passo 2   01     apliquei A → 1, não tem mais variável
```

Derivação completa:

```
S ⇒ 0A ⇒ 01
```

Terminou no passo 2 porque 0 e 1 são terminais e não sobrou nenhuma variável para trocar.

Uma coisa que reparei além do que foi pedido: essa gramática gera uma palavra só. Nenhuma regra
devolve o S ou o A para a linha, então não tem como alongar nem escolher outro caminho. Ou seja,
L(G) = {01}, uma linguagem que acaba, com uma palavra só. Bem diferente das gramáticas dos
exercícios 8 em diante, que têm uma regra que se repete e geram infinitas palavras.

---

## 8. Aplicando uma produção

Enunciado:

```
Considere S → 0S. Começando com S:

1. Aplique a regra uma vez.
2. Aplique a regra duas vezes.
3. Aplique a regra três vezes.
4. Escreva a sequência completa de derivação.
```

Essa questão dá uma regra só, de propósito. Ela quer que eu treine o movimento de aplicar a produção
e, no fim, perceba uma coisa importante: com essa regra sozinha a derivação nunca termina.

**8.1 Aplicando uma vez**

S ⇒ 0S. Troquei o S pelo que está do lado direito da regra, que é 0S.

**8.2 Aplicando duas vezes**

0S ⇒ 00S. A linha era 0S. O 0 é terminal e fica parado onde está, e o S que sobrou eu troquei de
novo por 0S, o que deu 0 mais 0S, ou seja, 00S.

**8.3 Aplicando três vezes**

00S ⇒ 000S. Mesma coisa: os dois 0 da frente ficam parados, e o S vira 0S outra vez.

**8.4 Escreva a sequência completa**

```
S ⇒ 0S ⇒ 00S ⇒ 000S
```

É a soma dos três passos, um atrás do outro. Cada vez que aplico a regra, entra um 0 novo e o S
volta para o fim da linha.

**O ponto principal da questão**

A derivação não terminou. A última linha é 000S, e ali ainda tem o S, que é variável. Enquanto
sobrar variável, o que eu tenho na mão não é palavra, é uma parada no meio do caminho.

E o detalhe que achei mais interessante: com essa regra sozinha, a derivação nunca vai acabar. O
S → 0S sempre devolve um S novo, então não existe como parar. Para fechar, a gramática precisaria de
uma segunda regra sem variável do lado direito, tipo S → 1, que é o que aparece no exercício 10, ou
S → ε.

Foi assim que entendi para que serve a regra de saída: toda gramática precisa de pelo menos uma
regra que não devolva variável. Sem ela, não sai palavra nenhuma.

---

## 9. Derivação completa de uma palavra

Enunciado:

```
Utilizando G: S → aS | b, gere aaab.

Escreva todos os passos da derivação.
```

Agora a gramática tem as duas regras: uma que repete (S → aS) e uma que encerra (S → b). A questão
quer a derivação escrita passo a passo, e não só a resposta.

Antes de escrever eu contei: aaab tem três a e um b no fim. Como S → aS coloca um a por vez e S → b
é a que encerra, já sabia que era aplicar S → aS três vezes e depois S → b.

```
S ⇒ aS ⇒ aaS ⇒ aaaS ⇒ aaab
```

Passo a passo:

```
início    S        comecei pelo símbolo inicial, como manda a definição
passo 1   aS       apliquei S → aS, colocou o 1º a e devolveu o S
passo 2   aaS      apliquei S → aS, colocou o 2º a e devolveu o S
passo 3   aaaS     apliquei S → aS, colocou o 3º a e devolveu o S
passo 4   aaab     apliquei S → b, trocou o S por b e encerrou
```

Terminou no passo 4 porque aaab só tem terminais, que são a e b, e não sobrou nenhuma variável para
trocar. Foi a regra S → b que fez isso, porque ela é a única das duas que não devolve o S. Então
aaab pertence a L(G).

A conta que guardei: quantos a a palavra tem é o mesmo tanto de vezes que eu aplico S → aS. Se a
questão pedisse aaaaab, com cinco a, seriam cinco aplicações e depois o S → b. Isso vira contagem, e
não tentativa e erro.

---

## 10. A palavra pode ser gerada

Enunciado:

```
Considere G: S → 0S | 1.

Determine se cada palavra pode ser gerada:

1. 1
2. 01
3. 001
4. 0001
5. 101
6. 1001

Para as palavras que podem ser geradas, apresente a derivação completa.
```

É a mesma gramática do exercício 9, só trocando a por 0 e b por 1. A diferença é que aqui tem
palavra que não dá pra gerar, e eu preciso explicar o porquê.

O padrão que vi antes de começar: a regra S → 0S só sabe colocar 0, e a regra S → 1 coloca um 1 e
encerra na hora. Como é ela que encerra, todo caminho possível é o mesmo, ou seja, um monte de 0 e
um 1 no fim.

```
L(G) = {0ⁿ1 | n ≥ 0}
```

Com esse padrão na mão dá pra responder as seis só olhando o formato da palavra. Mas escrevi a
derivação de cada uma que dá pra gerar, como o enunciado pediu.

**10.1 - 1**

Sim, pode ser gerada.

```
S ⇒ 1
```

Apliquei S → 1 direto, sem usar S → 0S nenhuma vez. É o caso n = 0 do padrão: nenhum 0 e um 1.
Terminou na hora, porque 1 é terminal.

**10.2 - 01**

Sim, pode ser gerada.

```
S ⇒ 0S ⇒ 01
```

Uma aplicação de S → 0S, que coloca o 0, e depois S → 1 para fechar.

**10.3 - 001**

Sim, pode ser gerada.

```
S ⇒ 0S ⇒ 00S ⇒ 001
```

Duas aplicações de S → 0S, um 0 em cada, e depois S → 1.

**10.4 - 0001**

Sim, pode ser gerada.

```
S ⇒ 0S ⇒ 00S ⇒ 000S ⇒ 0001
```

Três aplicações de S → 0S e depois S → 1. Mesma lógica das anteriores: a quantidade de 0 da palavra
é a quantidade de vezes que aplico a primeira regra.

**10.5 - 101**

Não pode ser gerada.

A palavra começa com 1. Para sair um 1, a única regra é S → 1, e ela apaga o S, ou seja, encerra a
derivação ali.

Testando o caminho: se eu começo com S → 1, a linha vira 1 e acabou. Não sobrou variável nenhuma,
então não tenho como escrever o 0 e o 1 que vêm depois. A outra opção seria começar com S → 0S, mas
aí a palavra começaria com 0, e não com 1.

Resumindo, depois que o 1 aparece não dá pra escrever mais nada. Como 101 tem símbolos depois do
primeiro 1, ela não pertence à linguagem.

**10.6 - 1001**

Não pode ser gerada. É o mesmo problema do item anterior, e por dois motivos.

Primeiro, a palavra começa com 1, e a regra que produz 1 encerra a derivação, então não podia vir
nada depois dele. Segundo, ela tem dois 1, e essa gramática só produz um 1 por palavra, porque o 1 é
justamente o que encerra, então não tem como sair um segundo.

O formato que o padrão 0ⁿ1 exige é zero ou mais 0, e exatamente um 1 no fim. O 1001 não se encaixa
nem no começo nem na contagem de 1.

**Resumo das seis**

```
1       sim     n = 0, só a regra que encerra
01      sim     um 0 mais o 1 final
001     sim     dois 0 mais o 1 final
0001    sim     três 0 mais o 1 final
101     não     tem símbolo depois do 1, que já encerra
1001    não     começa com 1 e ainda tem dois 1
```

---

## 11. Desafio final

Enunciado:

```
Considere G: S → aS | b. Responda sem consultar o gabarito:

1. A palavra b pode ser gerada?
2. A palavra ab pode ser gerada?
3. A palavra aab pode ser gerada?
4. A palavra aaab pode ser gerada?
5. A palavra aba pode ser gerada?
6. Escreva a derivação completa de aaaab.
7. Descreva, com suas palavras, o padrão das palavras geradas por essa gramática.

Dica: observe o que acontece quando aplicamos várias vezes S → aS e, finalmente,
utilizamos S → b.
```

É a gramática do exercício 9 de novo, agora com sete perguntas de uma vez. As quatro primeiras são
de sim ou não, a quinta é a pegadinha, a sexta é derivação e a sétima pede o padrão da linguagem,
que é o resumo de tudo.

O padrão, antes de começar: S → aS empilha a e S → b encerra com um b, então L(G) = {aⁿb | n ≥ 0}.

**11.1 A palavra b pode ser gerada?**

Sim.

```
S ⇒ b
```

Apliquei S → b direto, sem usar S → aS nenhuma vez. É o caso n = 0: nenhum a e um b. Como b é
terminal, já terminou aí.

**11.2 A palavra ab pode ser gerada?**

Sim.

```
S ⇒ aS ⇒ ab
```

Uma aplicação de S → aS coloca o a e devolve o S, e depois S → b fecha.

**11.3 A palavra aab pode ser gerada?**

Sim.

```
S ⇒ aS ⇒ aaS ⇒ aab
```

Duas aplicações de S → aS, um a em cada, e depois S → b.

**11.4 A palavra aaab pode ser gerada?**

Sim.

```
S ⇒ aS ⇒ aaS ⇒ aaaS ⇒ aaab
```

Três aplicações de S → aS e depois S → b. É a mesma derivação do exercício 9.

**11.5 A palavra aba pode ser gerada?**

Não. O problema é o a que vem depois do b.

A única regra que produz b é S → b, e ela apaga o S, ou seja, encerra a derivação naquele momento.
Depois que o b sai, não tem mais variável na linha, então não dá pra escrever mais nada.

Testando na mão:

```
S ⇒ aS ⇒ ab      aqui já acabou, não tem mais S para produzir o último a
```

Cheguei em ab e travei. Não existe nenhuma regra tipo "b → alguma coisa", porque b é terminal, e
terminal não se troca.

Outro jeito de justificar, olhando o padrão: em L(G) = {aⁿb} o b fica sempre na última posição. Em
aba o b está no meio, então ela não se encaixa.

**11.6 Escreva a derivação completa de aaaab**

```
S ⇒ aS ⇒ aaS ⇒ aaaS ⇒ aaaaS ⇒ aaaab
```

A palavra tem quatro a, então apliquei S → aS quatro vezes e fechei com S → b:

```
início    S         comecei pelo símbolo inicial
passo 1   aS        apliquei S → aS
passo 2   aaS       apliquei S → aS
passo 3   aaaS      apliquei S → aS
passo 4   aaaaS     apliquei S → aS
passo 5   aaaab     apliquei S → b
```

Terminou no passo 5 porque não sobrou variável na linha.

**11.7 Descreva com suas palavras o padrão das palavras geradas**

Toda palavra dessa gramática é um monte de a, que pode ser nenhum, com um b no final.

```
L(G) = {aⁿb | n ≥ 0} = {b, ab, aab, aaab, aaaab, ...}
```

É só olhar o que cada regra faz. O S → aS coloca um a e devolve o S para o fim da linha, e eu posso
repetir isso quantas vezes quiser, ou nenhuma, e é isso que deixa a quantidade de a livre. Já o
S → b coloca o b e não devolve o S, e como é a única que encerra, toda derivação passa por ela uma
vez só, no fim.

Daí saem as três coisas que todas as palavras têm:

- Os a vêm todos antes, porque S → aS escreve o a sempre à esquerda do S.
- Tem exatamente um b, porque S → b é usada uma vez só, já que encerra a derivação.
- O b fica no fim, porque é o último símbolo escrito, já que depois dele não sobra variável.

Como eu explicaria em voz alta: o S é uma setinha que anda para a direita deixando a para trás, e o
b é o ponto final que apaga a setinha. Por isso todo a vem antes e o b fecha a palavra.

O caso n = 0 é o que mais escapa: o b sozinho pertence à linguagem, porque nada obriga a usar S → aS
pelo menos uma vez. A menor palavra dessa gramática é b, e não ab.

---

## Onde eu quase errei

Os pontos onde fiquei na dúvida resolvendo, para reler na véspera da prova:

1. Nos itens 3.3 e 3.4, quase respondi a mesma coisa nos dois. O 01 ∈ Σ é falso, porque é palavra e
   não símbolo, mas o 01 ∈ Σ* é verdadeiro.
2. No item 4.5, quase aceitei 111 porque parece com 0111. Palavra é a sequência igualzinha, e falta
   o 0 da frente.
3. No item 5.4, quase disse que o ε pertence a {bⁿ | n ≥ 1}. A condição é n ≥ 1, e o ε seria n = 0.
4. Na questão 6, quase achei que ∅ e {ε} são a mesma coisa. O ∅ tem zero palavras, e o {ε} tem uma.
5. Na questão 8, quase disse que a derivação terminou em 000S. Sobrou variável, então não é palavra.
6. No item 10.5, tentei gerar 101 voltando depois do 1. A regra que produz 1 encerra a derivação.
7. No item 11.7, quase esqueci o caso n = 0. O b sozinho pertence à linguagem.

E os três hábitos que quero manter na hora da prova:

1. Contar antes de derivar, porque o tanto de símbolo da palavra já diz quantas vezes aplicar cada
   regra.
2. Procurar maiúscula na linha final. Se tiver, não terminou e aquilo não é resposta.
3. Achar o padrão da linguagem primeiro. Com o L(G) na mão, responder se pertence ou não vira
   conferência, e não chute.

# Atividade Prática - Regex para validação de e-mail

Primeira atividade da disciplina em que eu escrevo código, e não derivação no papel. Copiei o
enunciado antes de resolver, como faço nos outros arquivos.

O código resolvido está em [validador_email.py](validador_email.py).

---

## Enunciado

```
Escreva um programa que leia 5 endereços de e-mail e, usando expressão regular,
separe os válidos dos inválidos. Para cada e-mail inválido, informe o motivo.
```

---

## Por que regex aparece aqui

Demorei a ligar uma coisa na outra, então anoto: expressão regular e gramática regular descrevem a
mesma coisa, o tipo 3 da Hierarquia de Chomsky. A gramática gera as palavras da linguagem, a regex
reconhece se uma palavra dada pertence a ela.

```
gramática regular    gera     a partir do S, escreve palavras da linguagem
expressão regular    aceita   recebe uma palavra e responde pertence / não pertence
```

Então a atividade é a mesma matéria da Unidade 2, vista do outro lado. A linguagem aqui é o conjunto
de todos os endereços de e-mail bem formados, e a regex é o reconhecedor dela.

---

## A notação que eu precisei

Como na Unidade 1, o que me travou foi a notação e não o conceito. Deixo a tabela só com o que eu
usei de fato:

```
^          início da palavra
$          fim da palavra
[...]      classe, um símbolo qualquer dentre os listados
+          uma ou mais repetições do que vem antes
{2,}       duas ou mais repetições do que vem antes
(?:...)    agrupa sem guardar o trecho
\.         ponto literal, porque o ponto sozinho significa qualquer símbolo
(?!...)    olha à frente e exige que NÃO venha aquilo, sem consumir símbolo
(?<!...)   olha para trás e exige que NÃO tenha vindo aquilo, sem consumir símbolo
```

Os dois últimos são os que não têm equivalente em gramática regular. Eles não escrevem nem consomem
nada, só proíbem. Uso eles para as regras de não pode começar com ponto e parecidas.

---

## A regex, parte por parte

```python
padrao_email = re.compile(
    r"^(?!\.)(?!.*\.\.)(?!.*\.@)"
    r"[A-Za-z0-9._+-]+@"
    r"(?:(?!-)[A-Za-z0-9-]+(?<!-)\.)+"
    r"[A-Za-z]{2,}$"
)
```

São quatro linhas de string coladas uma na outra: em Python, strings literais vizinhas viram uma só.
Quebrei assim porque cada linha é uma parte do endereço, e em uma linha só eu não conseguia reler.

Linha 1, as três proibições gerais:

```
(?!\.)        a palavra não pode começar com ponto        .maria@gmail.com
(?!.*\.\.)    não pode ter dois pontos seguidos           ma..ria@gmail.com
(?!.*\.@)     não pode ter ponto colado antes do @        maria.@gmail.com
```

Elas ficam todas no começo, antes de consumir qualquer símbolo, porque o .* dentro delas varre a
palavra inteira à frente. Então dá para checar de uma vez, logo na largada.

Linha 2, a parte do usuário:

```
[A-Za-z0-9._+-]+@     uma ou mais letras, dígitos, ponto, underline, mais ou hífen, e então o @
```

O + garante pelo menos um símbolo, o que já derruba @gmail.com, sem usuário. O hífen fica no fim da
classe de propósito: no meio ele viraria intervalo, como o A-Z.

Linha 3, o domínio, que é a parte que mais me deu trabalho:

```
(?:(?!-)[A-Za-z0-9-]+(?<!-)\.)+
    (?!-)             a parte não começa com hífen
    [A-Za-z0-9-]+     letras, dígitos ou hífen
    (?<!-)            a parte não termina com hífen
    \.                e fecha com um ponto
    ( ... )+          esse bloco inteiro se repete uma ou mais vezes
```

O + no fim do grupo é o que faz udf.edu.br funcionar sem eu escrever uma regra para cada nível. O
grupo casa udf. e depois edu., e o que sobra, br, fica para a linha 4.

E como o grupo tem que aparecer pelo menos uma vez, ele exige ao menos um ponto no domínio. É essa
exigência que reprova ana@dominio.

Linha 4, a extensão:

```
[A-Za-z]{2,}$    duas ou mais letras, e aí acaba a palavra
```

Só letra, então x.c0m não passa. E no mínimo duas, então x.c também não.

---

## Por que tem uma função de motivo separada da regex

A regex responde uma coisa só: pertence ou não pertence. Ela não diz por quê, e o enunciado pede o
motivo.

Então o programa faz em duas etapas. Primeiro a regex decide; se reprovar, a função motivo_invalido
refaz a conferência em pedaços, na mão, para descobrir onde quebrou:

```
etapa 1    padrao_email.fullmatch(email)    válido ou inválido
etapa 2    motivo_invalido(email)           só para os inválidos, descobre o porquê
```

A ordem dos if dentro da função importa, e é do erro mais grosseiro para o mais fino. Precisa
conferir se existe @ antes de dar o split nele, senão o split estoura. E a checagem de mais de um @
tem que vir antes também, porque atribuir usuario e dominio de uma vez só funciona quando a palavra
tem exatamente um @.

A última linha da função devolve não corresponde ao padrão de e-mail. É a rede de segurança, para o
caso de a regex reprovar por um motivo que eu não previ na lista. Assim o programa nunca fica sem
resposta.

---

## Teste com os cinco e-mails da professora

Entrada:

```
maria@gmail.com
joao.silva@udf.edu.br
pedro.gmail.com
ana@dominio
estudante_01@faculdade.com
```

Saída:

```
E-mails válidos:
maria@gmail.com
joao.silva@udf.edu.br
estudante_01@faculdade.com

E-mails inválidos:
pedro.gmail.com - não possui @
ana@dominio - não possui extensão
```

Conferindo um por um por que cada resultado saiu assim:

```
maria@gmail.com              válido     usuário, @, domínio com um ponto, extensão com 3 letras
joao.silva@udf.edu.br        válido     ponto no meio do usuário é permitido; o grupo do domínio
                                        repetiu duas vezes, para udf. e edu.
estudante_01@faculdade.com   válido     underline e dígito estão na classe do usuário
pedro.gmail.com              inválido   não tem @; a linha 2 da regex exige o @ e ele não existe
ana@dominio                  inválido   o grupo do domínio precisa de pelo menos um ponto e não tem
```

---

## Testes que eu fiz por conta

Os cinco da professora não encostam nas proibições da linha 1, então inventei mais alguns para ver
se cada if da função é mesmo alcançado:

```
.ana@x.com       o usuário começa com ponto
ana.@x.com       possui ponto imediatamente antes de @
an..a@x.com      possui dois pontos consecutivos
@x.com           não possui usuário
ana@             não possui domínio
ana@-x.com       há hífen no início ou no final de uma parte do domínio
ana@x-.com       há hífen no início ou no final de uma parte do domínio
ana@x.c          a extensão é inválida
ana@x.c0m        a extensão é inválida
a n@x.com        contém espaço
a@b@c.com        possui mais de um @
```

E estes aqui eu queria confirmar que passam, porque são formatos que existem de verdade:

```
ana+tag@x.com    válido     o + está na classe do usuário
ana@sub.x.com    válido     o grupo do domínio repete, igual ao udf.edu.br
ana-b@x.com      válido     hífen é proibido na ponta do domínio, não no usuário
```

---

## Erros que quero evitar

1. Escrever ponto querendo dizer ponto. Sozinho ele significa qualquer símbolo, então a.b casaria
   com axb também. Ponto de verdade leva a barra invertida na frente.
2. Esquecer o ^ e o $. Sem eles a regex aceita um pedaço da palavra, e aí xxmaria@gmail.comxx
   passaria. É por isso que eu uso fullmatch também, que já ancora nas duas pontas.
3. Pôr o hífen no meio da classe. Com ele no fim está certo; no meio viraria intervalo e daria erro
   ou casaria coisa errada.
4. Dar o split no @ antes de conferir quantos @ a palavra tem.

---

## Resumo

```
o que a regex faz        aceita ou reprova, e só isso
o que a função faz       explica a reprova, conferindo em pedaços
ligação com a matéria    expressão regular reconhece o que a gramática regular gera (tipo 3)
resultado nos 5 casos    3 válidos, 2 inválidos, igual ao esperado
```

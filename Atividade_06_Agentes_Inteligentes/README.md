# Atividade 06 - Agentes Inteligentes

**Disciplina:** Inteligência Artificial, Linguagens Formais e Autômatos  
**Professora:** Kadidja Valéria  
**Aluno:** João Gabriel Pereira de Araujo  
**Aula:** 19/10/2026

---

## Anotações da aula

Nesta aula estudamos o Capítulo 2 sobre agentes inteligentes. O conteúdo mostrou como um agente recebe informações do ambiente, toma decisões e realiza ações.

Uma coisa que entendi é que não basta um sistema executar comandos para suas decisões serem consideradas inteligentes. É importante entender o ambiente, as informações disponíveis e o que o agente precisa alcançar.

## 1. Agentes e ambientes

Um agente é algo que consegue perceber um ambiente e agir sobre ele.

Para isso, existem dois elementos importantes:

- **Sensores:** recebem informações sobre o ambiente.
- **Atuadores:** permitem executar as ações.

Um exemplo apresentado foi o robô aspirador, que identifica a sujeira e realiza a limpeza.

Também vimos que um agente não precisa ser físico. Um programa pode funcionar como agente ao receber informações e executar comandos.

## 2. Percepção e histórico

A percepção é a informação que o agente recebe em determinado momento.

O histórico de percepções reúne tudo o que ele percebeu anteriormente.

Aprendi que o histórico pode fazer diferença na escolha de uma ação. Um agente que lembra o que já aconteceu consegue tomar decisões que não dependem apenas da situação atual.

Também vimos que a função do agente descreve como as percepções se relacionam com as ações, enquanto o programa é o que executa esse comportamento na prática.

## 3. Racionalidade

Esse foi um dos conceitos principais da aula.

Um agente racional procura escolher a ação que tem o melhor desempenho esperado com base nas informações que possui.

Isso não quer dizer que ele sempre vai acertar.

O exemplo do pôquer mostra bem essa diferença, porque um jogador pode tomar uma decisão correta considerando suas cartas e mesmo assim perder.

A racionalidade leva em consideração:

- A medida de desempenho.
- O conhecimento que o agente já possui.
- As ações disponíveis.
- O histórico de percepções.

O que entendi é que precisamos avaliar a decisão considerando o que o agente sabia naquele momento, e não somente o resultado final.

## 4. Medida de desempenho

A medida de desempenho serve para avaliar se o agente está conseguindo cumprir sua tarefa.

No exemplo do aspirador, não seria suficiente avaliar somente a quantidade de sujeira que ele aspirou.

O mais importante seria saber se o ambiente ficou limpo e se o agente não gastou energia sem necessidade.

Isso mostrou que definir corretamente o resultado esperado é importante para o funcionamento do agente.

## 5. Modelo PEAS

O PEAS é utilizado para descrever a tarefa de um agente.

| Sigla | Significado | Explicação |
|---|---|---|
| P | Performance | Como o desempenho é avaliado |
| E | Environment | Ambiente onde o agente atua |
| A | Actuators | Recursos usados para agir |
| S | Sensors | Recursos usados para perceber |

Um exemplo é o aspirador:

- **P:** manter os cômodos limpos, considerando tempo e energia.
- **E:** cômodos, obstáculos e sujeira.
- **A:** rodas e sistema de aspiração.
- **S:** sensores de posição, sujeira e proximidade.

O PEAS ajuda a entender melhor o problema antes de definir como o agente vai funcionar.

## 6. Classificação dos ambientes

Vimos que os ambientes possuem características diferentes e isso influencia o comportamento dos agentes.

**Completamente observável:** o agente consegue perceber tudo o que é importante para decidir.

**Parcialmente observável:** algumas informações não estão disponíveis.

**Agente único:** não existem outros agentes decisores influenciando diretamente a tarefa.

**Multiagente:** as decisões de outros participantes também influenciam os resultados.

**Determinístico:** o estado atual e a ação determinam o próximo estado.

**Estocástico:** existe incerteza sobre o resultado das ações.

**Episódico:** as decisões podem ser avaliadas de forma independente.

**Sequencial:** uma decisão interfere nas situações seguintes.

**Estático:** o ambiente permanece igual enquanto o agente decide.

**Dinâmico:** o ambiente continua mudando durante a decisão.

**Semidinâmico:** o ambiente não muda, mas o tempo interfere no desempenho.

**Discreto:** envolve estados ou ações separados.

**Contínuo:** envolve valores que mudam continuamente.

**Conhecido:** o agente conhece os efeitos das ações.

**Desconhecido:** o agente precisa aprender como o ambiente funciona.

Uma diferença que achei importante foi entre ambiente conhecido e completamente observável.

Um jogador pode conhecer todas as regras do pôquer, mas não conseguir observar as cartas dos adversários.

Ou seja, conhecer o funcionamento não significa conseguir ver todas as informações.

## 7. Tipos de agentes

O capítulo apresentou quatro tipos principais de agentes.

### Agente reativo simples

Age com base na percepção atual e segue regras do tipo condição e ação.

Por exemplo, quando o aspirador encontra sujeira, ele aspira.

### Agente baseado em modelo

Mantém informações sobre o ambiente e consegue utilizar dados anteriores.

Por exemplo, um aspirador que guarda quais locais já foram visitados.

### Agente baseado em objetivos

Escolhe ações pensando em chegar a uma meta.

Um exemplo é um programa que procura um caminho para alcançar um destino.

### Agente baseado em utilidade

Compara os resultados possíveis para encontrar a melhor opção, levando em conta diferentes fatores.

Um exemplo seria escolher uma rota considerando tempo, custo e segurança.

Aprendi que a diferença entre esses agentes está principalmente na forma como eles utilizam as informações para decidir.

## 8. Aprendizagem e autonomia

Também estudamos que um agente pode melhorar seu comportamento a partir das experiências.

O agente com aprendizagem possui quatro componentes apresentados no capítulo:

- **Elemento de desempenho:** escolhe as ações.
- **Crítico:** avalia os resultados.
- **Elemento de aprendizagem:** melhora o comportamento.
- **Gerador de problemas:** propõe experiências para obter informações.

A autonomia está relacionada à capacidade de utilizar a própria experiência, sem depender somente das informações iniciais fornecidas pelo programador.

Um exemplo seria o aspirador aprender quais locais acumulam mais sujeira.

## 9. Relação com autômatos

No final da aula, vimos como os agentes podem ser relacionados aos autômatos.

Um autômato pode representar comportamentos simples utilizando estados e transições.

O estado interno serve para guardar informações importantes do que já aconteceu.

Quando o agente recebe uma nova percepção, pode mudar de estado e executar uma ação.

Entendi que esse modelo ajuda a organizar o funcionamento de agentes mais simples, embora nem todas as situações possam ser representadas com poucos estados.

## 10. Sobre a atividade

A atividade foi dividida em três exercícios.

**Exercício 2.3:** analisar afirmações sobre agentes, racionalidade e funcionamento, explicando quais são verdadeiras ou falsas.

**Exercício 2.4:** aplicar o PEAS e classificar os ambientes de sete situações, incluindo futebol, tênis, exploração de Titã, compra de livros, salto de altura e leilão.

**Exercício 2.5:** explicar dez conceitos sobre agentes inteligentes e apresentar exemplos.

Também fizemos uma síntese relacionando um dos casos com estados e transições de autômatos.

O exercício que mais ajudou a relacionar os conceitos foi o 2.4, porque tivemos que pensar nas características de cada situação e justificar as classificações.

## Conclusão

O principal que entendi neste capítulo é que o comportamento de um agente depende das informações que ele consegue receber, das ações disponíveis e do objetivo que precisa alcançar.

Também aprendi que uma decisão racional não garante um resultado perfeito.

O PEAS ajuda a organizar a tarefa, enquanto a classificação dos ambientes permite entender melhor as dificuldades que o agente pode encontrar.

Além disso, os diferentes tipos de agentes mostram que nem todos precisam funcionar do mesmo jeito. Alguns conseguem agir com regras simples, enquanto outros precisam guardar informações, planejar ou aprender com a experiência.

## Material utilizado

- Russell e Norvig. Capítulo 2 - Agentes inteligentes.
- Material da aula de 19/10/2026, disponibilizado pela professora Kadidja Valéria.

# Atividade sobre agentes inteligentes

Aula 19/10/2026 | Professora Kadidja Valéria | Inteligência artificial

**Disciplina:** Inteligência Artificial, Linguagens Formais e Autômatos

**Estudante:** João Gabriel Pereira de Araujo | **Turma:** ______

Realize os exercícios 2.3, 2.4 e 2.5 do Capítulo 2 sobre agentes inteligentes. Analise a racionalidade, descreva ambientes de tarefa por meio do modelo PEAS e explique os conceitos com suas próprias palavras. Utilize o capítulo disponibilizado e justifique suas respostas.

**Modalidade sugerida:** individual com consulta. **Tempo estimado:** 2h30. **Prazo:** conforme orientação da professora.

## Preparação
Leia os tópicos sobre racionalidade, ambientes e estrutura dos agentes, especialmente a Seção 2.3.2.

## Exercício 2.3
Para cada afirmação, indique V ou F, justifique e forneça exemplo ou contraexemplo. Explicite as hipóteses utilizadas.

### a. Um agente que detecta apenas informações parciais sobre o estado não pode ser perfeitamente racional.

- Julgamento: F
- Justificativa: O agente não precisa saber tudo para agir de forma racional. Ele deve escolher aquilo que tem mais chance de funcionar com as informações que recebeu e o que já sabe.
- Exemplo ou contraexemplo: no pôquer, ninguém vê as cartas de todos os jogadores, mas ainda é possível decidir bem com as cartas e as jogadas conhecidas.

### b. Existem ambientes de tarefa nos quais nenhum agente reativo puro pode comportar-se racionalmente.

- Julgamento: V
- Justificativa: Um agente reativo simples usa somente o que percebe agora. Se duas situações parecem iguais, mas precisam de ações diferentes por causa do que ocorreu antes, esse agente não consegue distinguir as duas.
- Exemplo ou contraexemplo: se o aspirador encontra o cômodo atual limpo, não sabe se já terminou a limpeza dos outros cômodos. Sem memória, pode continuar andando à toa, mesmo com gasto de energia.

### c. Existe um ambiente de tarefa em que todo agente é racional.

- Julgamento: V
- Justificativa: Se a medida de desempenho for igual para qualquer ação, não existe uma escolha melhor que outra. Nesse caso, qualquer comportamento alcança o mesmo resultado.
- Exemplo ou contraexemplo: imagine uma tarefa que atribui a mesma nota ao agente, independentemente de ele ficar parado ou se mover.

### d. A entrada para o programa de agente é a mesma que a entrada para a função de agente.

- Julgamento: F
- Justificativa: A função do agente relaciona o histórico inteiro de percepções a uma ação. O programa recebe a percepção atual e pode usar uma memória interna para representar o que já aconteceu.
- Exemplo ou contraexemplo: o programa do aspirador recebe a informação de que o piso atual está limpo, mas também pode consultar o registro das áreas visitadas.

### e. Toda função de agente é implementável por uma combinação de programa/máquina.

- Julgamento: F
- Justificativa: Uma função pode definir respostas para uma quantidade ilimitada de históricos. Não dá para garantir que toda função possível seja executada por um programa em uma máquina.
- Exemplo ou contraexemplo: uma função que exige guardar e consultar uma tabela sem limite de tamanho não pode simplesmente ser colocada inteira na memória de um computador real.

### f. Suponha que um agente selecione sua ação uniformemente ao acaso do conjunto de ações possíveis. Existe um ambiente de tarefa determinista em que esse agente é racional.

- Julgamento: V
- Justificativa: Mesmo em um ambiente determinista, pode acontecer de todas as ações valerem a mesma coisa na avaliação. Então escolher ao acaso não diminui o desempenho.
- Exemplo ou contraexemplo: se apertar qualquer um de dois botões sempre dá um ponto, escolher um botão aleatoriamente também é uma decisão racional nessa tarefa.

### g. É possível para um dado agente ser perfeitamente racional em dois ambientes de tarefa distintos.

- Julgamento: V
- Justificativa: O mesmo comportamento pode servir para mais de um ambiente, desde que as regras, informações e objetivos façam esse comportamento ser adequado nos dois.
- Exemplo ou contraexemplo: um aspirador que limpa ao encontrar sujeira pode funcionar racionalmente em duas versões de um ambiente de limpeza com condições parecidas.

### h. Todo agente é racional em um ambiente não observável.

- Julgamento: F
- Justificativa: Não conseguir observar o ambiente não faz todas as ações serem igualmente boas. A decisão ainda depende da medida de desempenho e do conhecimento anterior.
- Exemplo ou contraexemplo: se um agente não tem sensores, mas sabe que uma ação sempre traz um resultado melhor que outra, escolher a pior não é racional.

### i. Um agente jogador de pôquer perfeitamente racional nunca perde.

- Julgamento: F
- Justificativa: Uma boa decisão não garante vitória. O jogo tem informações escondidas e resultados que não dependem só da escolha do jogador.
- Exemplo ou contraexemplo: uma pessoa pode fazer a jogada com a melhor chance de ganho e ainda perder para outra mão.

## Exercício 2.4
Para cada caso, delimite o agente, preencha o PEAS e justifique todas as classificações. Considere Titã como cenário hipotético do exercício.

### Caso 1 — Jogar futebol.

- Agente analisado: um jogador de futebol durante uma partida, e não a equipe inteira.
- Objetivo e hipóteses: ajudar sua equipe a vencer, participando do ataque e da defesa, em uma partida com outros jogadores.
- P — Medida de desempenho: Participação nas jogadas, gols feitos e evitados, e resultado para a equipe.
- E — Ambiente: Campo, bola, companheiros, adversários, traves e regras do jogo.
- A — Atuadores: Pernas, pés, braços e voz para jogar e se comunicar.
- S — Sensores: Visão, audição e tato.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | Pois o jogador não consegue acompanhar tudo ao mesmo tempo nem saber a intenção dos outros. |
| Número de agentes | Multiagente | Com colaboração dentro do time e disputa contra o adversário. |
| Previsibilidade | Estocástico | Porque a reação dos jogadores e os resultados das jogadas não são certos. |
| Dependência entre decisões | Sequencial | Porque cada passe ou movimento muda a continuação da partida. |
| Mudança durante a decisão | Dinâmico | Já que o jogo segue acontecendo durante a decisão. |
| Natureza dos elementos | Combinação | placar é contado, enquanto posição e movimento variam continuamente. |
| Conhecimento do funcionamento | Conhecido | quanto às regras do futebol, mesmo sem conhecer antecipadamente as jogadas dos outros. |

### Caso 2 — Explorar os oceanos subterrâneos de Titã.

- Agente analisado: robô explorador enviado sozinho a um oceano subterrâneo, em um exemplo hipotético.
- Objetivo e hipóteses: conseguir informações sobre o local, registrar o que encontrar e evitar danos ao equipamento. O robô ainda não conhece a região.
- P — Medida de desempenho: Quantidade e qualidade de informações coletadas, avanço na exploração e segurança do robô.
- E — Ambiente: Água, regiões desconhecidas, obstáculos e o oceano subterrâneo de Titã.
- A — Atuadores: Motores de deslocamento e mecanismos para realizar coletas.
- S — Sensores: Câmeras e sensores de distância e das condições ao redor.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | Porque o robô só recebe dados da área que consegue alcançar com os sensores. |
| Número de agentes | Agente único | Pois o cenário considera apenas esse explorador. |
| Previsibilidade | Estocástico | Já que correntes e obstáculos podem afetar seus movimentos. |
| Dependência entre decisões | Sequencial | Porque o caminho escolhido interfere nos próximos locais explorados. |
| Mudança durante a decisão | Dinâmico | Considerando que a água pode se mover durante as decisões. |
| Natureza dos elementos | Contínuo | quanto à posição, ao deslocamento e ao tempo. |
| Conhecimento do funcionamento | Desconhecido | Pois o robô precisa descobrir como é a região ao explorar. |

### Caso 3 — Comprar livros usados de IA na Internet.

- Agente analisado: programa de compras que procura um livro usado de inteligência artificial em lojas online.
- Objetivo e hipóteses: escolher o livro pedido levando em conta o preço, a condição anunciada e a entrega.
- P — Medida de desempenho: Encontrar o livro correto, com preço total adequado e entrega em boas condições.
- E — Ambiente: Sites de venda, anúncios, livros, vendedores, compradores e formas de pagamento.
- A — Atuadores: Fazer pesquisas nos sites, selecionar ofertas e enviar pedidos digitais.
- S — Sensores: Textos dos anúncios, preços, fotos, avaliações e informações de frete.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | Pois uma descrição e uma foto não mostram necessariamente a condição real do livro. |
| Número de agentes | Multiagente | Porque vendedores e outros compradores podem interferir nas ofertas. |
| Previsibilidade | Estocástico | Já que um anúncio pode sair do ar ou uma oferta pode mudar. |
| Dependência entre decisões | Sequencial | Porque pesquisar e comparar vem antes de decidir a compra. |
| Mudança durante a decisão | Dinâmico | Pois preços e estoques podem mudar durante a busca. |
| Natureza dos elementos | Combinação | produtos e pedidos são separados, enquanto preço e tempo podem variar. |
| Conhecimento do funcionamento | Conhecido | quanto ao uso das lojas e ao processo de compra, mas não quanto a todas as condições reais dos produtos. |

### Caso 4 — Jogar uma partida de tênis.

- Agente analisado: um tenista jogando uma partida contra outro tenista.
- Objetivo e hipóteses: ganhar pontos seguindo as regras, considerando a movimentação da bola e as respostas do adversário.
- P — Medida de desempenho: Pontos conquistados e resultado da partida.
- E — Ambiente: Quadra, rede, bola, adversário e marcações.
- A — Atuadores: Braços, pernas, corpo e raquete.
- S — Sensores: Visão, audição e tato.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | Já que não se conhece a próxima decisão do adversário. |
| Número de agentes | Multiagente | Pois os dois jogadores fazem escolhas que afetam o jogo. |
| Previsibilidade | Estocástico | Devido à incerteza da rebatida e das reações do outro jogador. |
| Dependência entre decisões | Sequencial | Porque uma jogada interfere na seguinte. |
| Mudança durante a decisão | Dinâmico | Pois o adversário e a bola se movem enquanto o jogador decide. |
| Natureza dos elementos | Combinação | a pontuação é discreta e os movimentos são contínuos. |
| Conhecimento do funcionamento | Conhecido | quanto às regras, não quanto às próximas ações do rival. |

### Caso 5 — Praticar tênis contra uma parede.

- Agente analisado: pessoa treinando sozinha, rebatendo a bola numa parede.
- Objetivo e hipóteses: manter a bola em jogo durante o treino e conseguir praticar as rebatidas.
- P — Medida de desempenho: Número de rebatidas bem feitas e manutenção da sequência de treino.
- E — Ambiente: Parede, piso da quadra, bola e espaço de treino.
- A — Atuadores: Braços, pernas e raquete.
- S — Sensores: Visão e tato, percebendo a bola e o próprio movimento.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | Com percepção humana real, pois a pessoa não mede exatamente todos os detalhes do movimento da bola. |
| Número de agentes | Agente único | Já que a parede não é outro agente que decide. |
| Previsibilidade | Estocástico | na prática, porque as batidas não saem sempre exatamente iguais; em um modelo físico idealizado poderia ser determinístico. |
| Dependência entre decisões | Sequencial | Porque o modo de rebater muda a devolução seguinte. |
| Mudança durante a decisão | Dinâmico | Pois a bola continua se movendo. |
| Natureza dos elementos | Combinação | o número de rebatidas é discreto e a trajetória da bola é contínua. |
| Conhecimento do funcionamento | Conhecido | quanto à dinâmica básica do treino e ao efeito esperado de rebater contra a parede. |

### Caso 6 — Realizar um salto de altura.

- Agente analisado: atleta fazendo uma tentativa de salto de altura.
- Objetivo e hipóteses: ultrapassar a barra sem derrubá-la, dentro das regras, buscando a maior altura possível.
- P — Medida de desempenho: Passar pela barra, alcançar boa altura e realizar uma tentativa válida.
- E — Ambiente: Pista de aproximação, sarrafo, suportes e colchão.
- A — Atuadores: Pernas, braços e movimentos do corpo.
- S — Sensores: Visão, tato e equilíbrio.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | Pois o atleta não tem percepção exata de todas as posições do corpo. |
| Número de agentes | Agente único | Considerando apenas sua tentativa, sem interação direta com outro atleta. |
| Previsibilidade | Estocástico | na prática, pois mesmo uma tentativa preparada pode variar. |
| Dependência entre decisões | Sequencial | Porque corrida, impulsão e passagem pela barra dependem das etapas anteriores. |
| Mudança durante a decisão | Dinâmico | Já que o atleta continua em movimento enquanto executa o salto. |
| Natureza dos elementos | Combinação | a altura é contínua, mas o resultado válido ou inválido é separado. |
| Conhecimento do funcionamento | Conhecido | quanto às regras e à técnica básica da prova. |

### Caso 7 — Participar de um leilão de um item, realizando lances.

- Agente analisado: comprador participando de um leilão pela internet.
- Objetivo e hipóteses: tentar adquirir um item sem ultrapassar um limite de gasto definido antes.
- P — Medida de desempenho: Conseguir o item por um preço aceitável e respeitar o limite de gasto.
- E — Ambiente: Plataforma do leilão, item, regras, vendedor e outros participantes.
- A — Atuadores: Enviar lances e realizar a confirmação da compra.
- S — Sensores: Valores dos lances, tempo restante, mensagens e situação do leilão na tela.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | Porque não se sabe quanto os concorrentes pretendem pagar. |
| Número de agentes | Multiagente | Com competição entre os participantes. |
| Previsibilidade | Estocástico | Considerando os lances que os outros podem fazer. |
| Dependência entre decisões | Sequencial | Pois cada lance altera as opções seguintes. |
| Mudança durante a decisão | Dinâmico | Porque os valores podem subir antes que o participante tome a decisão. |
| Natureza dos elementos | Combinação | os lances ocorrem em etapas separadas, e o tempo continua passando. |
| Conhecimento do funcionamento | Conhecido | quanto às regras e ao funcionamento do leilão, mas não quanto aos limites dos concorrentes. |

### Opções para classificação
- **Observabilidade:** Completamente observável, parcialmente observável ou não observável.
- **Número de agentes:** Agente único ou multiagente; indique cooperação ou competição quando pertinente.
- **Previsibilidade:** Determinístico ou estocástico; considere a influência estratégica de outros agentes.
- **Dependência entre decisões:** Episódico ou sequencial.
- **Mudança durante a decisão:** Estático, dinâmico ou semidinâmico.
- **Natureza dos elementos:** Discretos, contínuos ou combinação; considere estados, tempo, percepções e ações.
- **Conhecimento do funcionamento:** Conhecido ou desconhecido para o agente.

### Comparação final
1. O que muda entre jogar tênis contra outra pessoa e praticar contra uma parede?
2. Por que comprar livros usados pode exigir decisões com informações incompletas?
3. Como outros agentes influenciam futebol e leilões?

Respostas: No tênis contra outra pessoa, o adversário escolhe suas jogadas e pode surpreender o jogador. No treino contra a parede, não tem esse outro participante decidindo: a bola volta conforme a batida e as condições do treino. Na compra de livros usados, as páginas podem mostrar preço e fotos, mas não garantem que a descrição mostre todos os detalhes do livro. Já no futebol e no leilão, as decisões dos outros participantes mudam bastante o que o agente pode fazer: no futebol existem colegas e adversários; no leilão, outros compradores podem aumentar os lances.

## Exercício 2.5
Defina cada termo com suas palavras em duas a quatro linhas e apresente um exemplo.

### Agente

- Definição: É quem recebe informações do ambiente e consegue agir nele. Pode ser uma pessoa, uma máquina ou um programa.
- Exemplo: um sistema que recebe um pedido de pesquisa e mostra um resultado.

### Função de agente

- Definição: É a definição de qual ação deve ser tomada considerando tudo o que o agente já percebeu. Descreve o comportamento, sem dizer como foi programado.
- Exemplo: a regra que relaciona a posição e as informações de sujeira às ações do aspirador.

### Programa de agente

- Definição: É a parte executada na máquina que recebe informações e produz as ações. Pode também guardar dados importantes do que aconteceu antes.
- Exemplo: o código que verifica o sensor do aspirador e comanda a limpeza.

### Racionalidade

- Definição: É escolher a ação que deve trazer o melhor desempenho esperado com as informações disponíveis. Isso não quer dizer que o resultado vai ser sempre bom.
- Exemplo: no pôquer, um jogador toma uma decisão adequada e ainda pode perder.

### Autonomia

- Definição: É quando o agente consegue usar as próprias experiências para orientar melhor suas ações, em vez de seguir apenas o que o programador deixou pronto.
- Exemplo: um robô que aprende em quais locais aparece mais sujeira.

### Agente reativo

- Definição: É o que reage à percepção do momento seguindo uma regra, sem precisar consultar o que percebeu antes.
- Exemplo: detectar sujeira no local e começar a aspirar.

### Agente baseado em modelo

- Definição: É aquele que acompanha uma ideia de como o ambiente está, usando informações guardadas e o que sabe sobre as mudanças no mundo.
- Exemplo: um aspirador que atualiza o registro dos lugares visitados.

### Agente baseado em objetivos

- Definição: É o que escolhe ações pensando em alcançar um resultado definido. Pode comparar caminhos diferentes até essa meta.
- Exemplo: um sistema de rotas que procura como chegar a um endereço.

### Agente baseado em utilidade

- Definição: É aquele que compara opções levando em consideração o quanto cada resultado é vantajoso. Ajuda quando não basta apenas atingir uma meta.
- Exemplo: escolher uma viagem avaliando tempo, custo e segurança.

### Agente com aprendizagem

- Definição: É um agente que usa o que aconteceu nas tentativas anteriores para melhorar suas próximas escolhas. Ele pode mudar sua forma de agir com a experiência.
- Exemplo: um aspirador que passa a visitar mais vezes os cômodos que sujam mais.

## Síntese com autômatos
Escolha um caso do item 2.4. Apresente três estados internos, três percepções, três ações e duas regras no formato estado atual + percepção → próximo estado e ação. Explique como estados internos representam informação passada e cite uma limitação da simplificação.

Resposta:

Caso escolhido: comprar livros usados de IA na internet. Vou considerar um programa que pesquisa ofertas e verifica se alguma atende ao valor definido.

Três estados internos:

1. Procurando ofertas.
2. Avaliando um anúncio.
3. Pedido enviado.

Três percepções:

1. Uma oferta foi encontrada.
2. O preço total está dentro do limite e o livro corresponde ao pedido.
3. O pedido foi confirmado pela loja.

Três ações:

1. Consultar os detalhes da oferta.
2. Enviar o pedido de compra.
3. Encerrar a busca.

Duas regras de transição:

- Regra 1: procurando ofertas + uma oferta foi encontrada → avaliando um anúncio **e consultar os detalhes da oferta**.
- Regra 2: avaliando um anúncio + preço dentro do limite e livro correto → pedido enviado **e enviar o pedido de compra**.

O estado interno ajuda o programa a saber em que etapa está. Isso evita tratar toda informação como se fosse o começo de uma pesquisa nova. Uma limitação desse modelo é que três estados não conseguem representar todos os detalhes importantes, como mudanças no frete, qualidade real do livro ou uma compra que não foi confirmada. O modelo também não mostra o que acontece se a loja recusar o pedido ou se o valor mudar depois.


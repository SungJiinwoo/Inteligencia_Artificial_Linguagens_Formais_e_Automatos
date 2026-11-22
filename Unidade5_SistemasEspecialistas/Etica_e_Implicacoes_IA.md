# Ética e implicações em IA (A1)

Atividade da aula de 16/11. Grupo: João Gabriel Pereira de Araújo e Julyane Ataides (squad 5).
Projeto analisado: [Triagem das filas do Repositório de TCCs](Triagem_Curadoria_TCC.ipynb), o
sistema especialista que fizemos na aula 13.

---

## 1. Leitura e vídeo

**Artigo:** LACERDA JÚNIOR, F. P. *Da proibição à governança: uso ético da inteligência artificial
generativa na educação superior: uma revisão integrativa (2023–2026)*. Revista Foco, v. 19, n. 8, 2026.

Questão de integridade acadêmica que levamos para o projeto: **autoria e declaração**. O artigo
explica que uma ferramenta de IA não pode responder pelo que produz, então quem assina o trabalho
continua responsável por ele. Também diz que declarar o uso não torna aceitável um uso inadequado,
mas que omitir impede avaliar o processo, e que a declaração deve dizer ferramenta, finalidade e
extensão do apoio. Foi esse o critério que usamos na seção 4.

**Vídeo:** IEA-USP, *O Estado da Arte em Ética na Inteligência Artificial* (2026).

Trecho escolhido: **6:10 a 6:58**. O palestrante diz que, se a regulação vira o único critério, a
ética fica reduzida a uma lista de conformidade, e que não basta perguntar se o sistema é exato ou
justo: é preciso olhar também as instituições e os incentivos em volta dele. Ele compara o
alinhamento com a composição de uma pintura, que começa no primeiro traço e não é um verniz
passado no final. A ideia que levamos ao debate: no nosso sistema, a revisão humana e as regras de
acesso precisam estar no desenho desde o início, e não ser um aviso colocado depois.

## 2. Análise ética do projeto

**O projeto.** No squad 5 estamos desenvolvendo o repositório público de TCCs dos cursos de TI da
UDF. Para um TCC ser publicado ele passa por duas filas: o administrador valida ou recusa os
cadastros (parte da Julyane, BL-11, BL-12 e BL-20) e a curadoria aprova ou rejeita os TCCs enviados
(parte do João, BL-35 e BL-36). Nosso sistema especialista ajuda nessas duas filas. Quem usa é o
administrador e a curadoria; quem pode ser afetado pelas saídas são as pessoas que se cadastram
(orientadores, coordenação e curadoria) e os alunos autores dos TCCs. A IA participa em dois
pontos: duas árvores de decisão preveem a decisão mais provável (`validado`/`recusado` para o
cadastro e `aprovada`/`rejeitada` para o TCC). As regras de acesso (R5 a R8), de data
(R9) e de duplicidade (R10) vêm de regras de negócio do squad; as recomendações R1 a R4 e R11 e R12
dependem da previsão de um modelo combinada com fatos informados por pessoas.

| Aspecto | Situação concreta no projeto | Quem pode ser afetado | Medida que adotamos |
|---|---|---|---|
| Privacidade e dados | O cadastro tem nome, e-mail institucional e data de nascimento; o TCC tem nomes de alunos e orientadores. | Quem se cadastra e os alunos autores. | Os modelos usam só contagens (palavras do nome, números no e-mail, palavras do resumo), nunca o dado em si. Os datasets são simulados. O squad já apaga cadastros não validados em 30 dias (RN-36) e a data de nascimento tem finalidade registrada (RN-22). |
| Viés e equidade | O modelo da fila de cadastros aprendeu que nome de uma palavra e e-mail sem o nome levam a "recusado". Isso pode prejudicar quem tem nome curto, nome estrangeiro ou e-mail de setor (linha 20 do dataset). | Pessoas da faculdade com nomes ou e-mails fora do padrão. | Testar casos com o mesmo vínculo e nomes de tamanhos diferentes; a R3 pede conferência com a pessoa quando o vínculo está confirmado; a R4 pede confirmar o vínculo e os dados quando ele ainda não foi confirmado; recusar exige motivo escrito (RN-36). |
| Transparência | O administrador ou a curadoria podem achar que a recomendação é uma decisão. | Quem é analisado. | Toda saída mostra a previsão do modelo, a regra que disparou, os fatos usados e o aviso "recomendação de apoio". Entradas fora do intervalo do treino recebem aviso próprio. |
| Supervisão e responsabilidade | Uma previsão errada pode levar a recusar um cadastro válido ou a aprovar um TCC com termo ilegível (linhas 21 e 24 do dataset). | Quem se cadastra e os autores do TCC. | A decisão é sempre humana: o administrador valida ou recusa (RF13) e só a curadoria aprova ou rejeita (RN-07). A rejeição exige motivo (RN-09) e quem enviou pode corrigir e reenviar. A R11 manda conferir monografia e termo mesmo quando a previsão é "aprovada". |
| Impacto social | A curadoria ganha uma ordem de conferência e o administrador uma triagem dos cadastros. | Beneficia administrador, curadoria e alunos (publicação mais rápida). Prejudica quem for recusado ou atrasado por um erro tratado como definitivo. | O protótipo não altera nenhuma fila do sistema real. Antes de qualquer uso, seria preciso testar com decisões reais e com autorização da faculdade. |

## 3. Debate e dilema ético

**Dilema:** o modelo da fila de cadastros prevê "recusado" para uma pessoa com nome de uma palavra
só, e o administrador está com muitos cadastros parados perto do prazo de 30 dias.

* **Forma 1, seguir a previsão para ganhar tempo:** a fila anda mais rápido, mas uma pessoa da
  faculdade pode ter o cadastro apagado por causa do nome, e o erro só aparece se ela reclamar.
* **Forma 2, tratar a previsão como sugestão e confirmar o vínculo:** dá mais trabalho e alguns
  cadastros podem chegar perto do prazo, mas ninguém é recusado só por um padrão estatístico, e
  quem é recusado recebe um motivo que consegue contestar.

Escolhemos a forma 2, que é a que está nas regras R2, R3 e R4. O trecho do vídeo ajuda a justificar: a
revisão humana não pode ser um verniz no final, precisa estar desde o primeiro traço do sistema.

### Reflexão individual: João Gabriel Pereira de Araújo

Eu manteria a decisão principal do grupo: a previsão da árvore entra no sistema como mais um fato,
e quem aprova ou rejeita continua sendo a curadoria (RN-07). O que eu mudaria está na minha parte,
a fila da curadoria (BL-35 e BL-36). Nos testes, as linhas 21 e 24 do dataset têm resumo grande,
palavras-chave e abstract, mas foram rejeitadas por termo ilegível e monografia incompleta, e o
modelo previu `aprovada` porque esses problemas não aparecem nos atributos. Uma pessoa da curadoria
com a fila cheia poderia ler "aprovada" e aprovar sem abrir o PDF. Por isso eu mudaria a saída para
mostrar, junto com a previsão, o que o modelo **não** confere (termo, monografia e conteúdo), e
deixaria a R11 como uma lista do que conferir antes de liberar o botão de aprovar, e não só como
texto. O argumento que mais me influenciou foi o do artigo: a ferramenta não responde pelo que
produz, então quem assina continua responsável. Na curadoria, quem aprova responde pelo TCC que
fica público com o nome do aluno, então a recomendação tem que ser fácil de conferir, e não fácil
de seguir no automático. O trecho do vídeo completou isso para mim: esse cuidado tem que estar
desde o primeiro traço, no desenho da saída, e não num aviso colocado no final. Levei a mesma ideia
para o jeito de fazer o trabalho: usei IA para estudar e revisar, mas só ficou no notebook o que eu
consegui conferir com o código do squad e explicar com as minhas palavras. Para verificar se a
mudança funciona, eu compararia as recomendações com a decisão final da curadoria durante um
semestre, olhando principalmente os casos em que a previsão foi `aprovada` e o TCC acabou rejeitado
por termo ou monografia. Se esses casos forem barrados antes da aprovação e nenhum TCC for
publicado com termo inválido, a medida funcionou; se a curadoria começar a marcar a lista sem
abrir o arquivo, aí a mudança não resolveu e precisa ser revista.

## 4. Declaração de uso de sistemas de IA

**IA incorporada ao projeto.** O projeto utiliza duas árvores de decisão (`DecisionTreeClassifier`,
scikit-learn) integradas a um sistema especialista de regras para recomendar ações nas filas de
cadastros e de TCCs do repositório do squad 5. O sistema recebe contagens tiradas do cadastro
(palavras do nome, nome no e-mail, números no e-mail) e da versão do TCC (palavras do resumo,
palavras-chave, tecnologias, abstract), além de fatos informados ou calculados (vínculo confirmado,
cadastro validado, perfil ativo, autoria, data de apresentação e possível duplicidade), e gera a
regra aplicada, a recomendação e a explicação dos fatos usados. A equipe verificou seu
funcionamento por meio de treino e teste com acurácia e matriz de confusão, conferência das
exceções colocadas de propósito nos datasets, três casos novos e a troca de um fato por vez para
ver qual regra dispara. As limitações identificadas incluem datasets simulados e pequenos, rótulos
definidos por nós, possível viés contra nomes curtos ou fora do padrão e problemas que não
aparecem nos atributos (termo ilegível, monografia incompleta, e-mail de setor). A revisão cabe ao
administrador (cadastros) e à curadoria (TCCs).

**IA utilizada na elaboração do trabalho.** Utilizei o Claude (Anthropic, modelo Opus) e o Codex
(OpenAI) para estudar os conceitos da aula 13, revisar o código e os textos do notebook, juntar a
minha parte e a da Julyane em um notebook único e conferir se a entrega atendia ao que foi pedido.
Aproveitei sugestões de organização do código, de redação de trechos explicativos e da tabela de
regras depois de conferir cada regra com os requisitos do squad 5 (`docs/requirements.md`) e com o
código que implementamos nos BL-35 e BL-36, executar o notebook do início ao fim e comparar os
resultados com a análise escrita. Assumo a responsabilidade pelas escolhas, verificações e conteúdo
da entrega.

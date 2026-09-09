---
title: "Taxa de resposta: por que quem não é respondido tem o número bloqueado"
description: "Template aprovado, lista própria, tudo certo, e bloqueio em dois dias. A variável que quase ninguém mede antes de disparar é quantas pessoas responderam."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "taxa-de-resposta-e-bloqueio"
cluster: "compliance"
hero: "limite"
intent: "decidindo"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://business.whatsapp.com/policy
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/phone-numbers/quality-rating-and-messaging-limits
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-pausing/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/marketing-templates/per-user-limits
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=cZ_nyIUv5ic
videos: [cZ_nyIUv5ic]
internal_links:
  - /numero-banido-no-whatsapp-o-que-fazer
  - /qualidade-do-numero-whatsapp
  - /como-documentar-o-opt-in-do-cliente
  - /disparo-em-massa-api-oficial-whatsapp
  - /minha-campanha-travou-no-meio
status: aprovado
---

# Taxa de resposta: por que quem não é respondido tem o número bloqueado

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** essa é a causa de bloqueio que mais pega gente que fez tudo certo. Template aprovado, API oficial, lista própria, sem nicho proibido, e o número cai mesmo assim.

O que faltou não estava na regra técnica. Faltou **gente do outro lado respondendo**. A plataforma mede a reação de quem recebe, e silêncio em volume é lido como envio indesejado.

A conclusão desconfortável, e a mais útil deste site: **o template aprovado autoriza você a iniciar a conversa, e não garante que a conversa é bem-vinda.**

::numeros: 1 variável|que quase ninguém mede antes de disparar ;; 2 dias|foi o tempo do caso descrito abaixo ;; 0|regras publicadas com o número mínimo aceitável ;; resposta|é o sinal que a plataforma lê

## Principais pontos
- **Quem recebe decide.** Bloqueio, denúncia e ausência de resposta alimentam a avaliação do seu número.
- **Ter template aprovado não é autorização para lista fria.** São coisas separadas, e confundir as duas é o erro mais caro do assunto.
- **Não existe percentual publicado.** Qualquer número de "taxa mínima" que circule por aí é invenção, e aqui não vamos inventar um.
- **Botão que permite responder é a alavanca mais barata** que existe, incluindo o botão que parece contraintuitivo.
- **Meça a taxa de resposta do último disparo antes de fazer o próximo.** Se foi baixa, o problema não é volume, é a lista.

::diagrama: numero-banido-visual

## O caso que resume o assunto

É o relato que explica isso melhor que qualquer teoria.

Uma advogada tinha uma lista de clientes e já havia sido bloqueada antes. Contratou a API oficial, foi orientada a montar o template do jeito certo, e montou. Nas palavras do Israel Henrique, CTO da Datafy:

> "Começou a disparar um, dois dias, foi bloqueada de novo. Aí eu falei: 'Nossa, tá, mas alguém te respondeu?' 'Ninguém, ninguém.' Ela ficou três dias enviando mensagens para as pessoas e ninguém respondia a ela. Bloqueio."

Vale enumerar o que ela **não** fez de errado, porque é isso que torna o caso instrutivo:

- Não era nicho proibido
- Não era lista comprada, eram clientes dela
- O template estava aprovado
- Estava na API oficial, pelo caminho autorizado
- Seguiu orientação técnica

O que aconteceu foi que a plataforma olhou uma variável que ela não estava medindo: **quantas pessoas responderam.** Três dias de silêncio foram lidos como envio indesejado.

::video: cZ_nyIUv5ic | Em 09:05 está a frase que organiza tudo, de que usar template e API oficial não é blindagem contra banimento. O caso da advogada está em 10:39, e a explicação sobre engajamento começa em 10:01.

## Por que a plataforma mede isso

A lógica é do ponto de vista de quem recebe, e faz sentido quando você inverte a perspectiva.

O WhatsApp é um aplicativo pessoal. O valor dele depende de as pessoas continuarem abrindo. Se empresas puderem mandar mensagem em volume para quem não quer, o aplicativo vira caixa de spam e as pessoas param de abrir.

Então a plataforma precisa de um sinal para separar mensagem desejada de mensagem tolerada. O sinal disponível é o comportamento: quem responde, quem ignora, quem bloqueia, quem denuncia.

Isso explica um detalhe importante: **não é sobre você ter permissão, é sobre a pessoa querer.** As duas coisas costumam andar juntas, e quando não andam, é o comportamento que prevalece.

E explica também por que essa causa é tão comum entre quem migrou para a API oficial esperando resolver o problema: a migração corrige o risco de usar um caminho não autorizado, e não corrige a lista.

## O que dá para medir, do seu lado

Não existe percentual publicado pela Meta, e não vamos cravar um. O que existe são indicadores próprios que você consegue calcular hoje:

**Taxa de resposta do último disparo.** Quantas pessoas responderam ou clicaram em botão, dividido por quantas receberam. É o número que mais importa, e quase ninguém calcula.

**Taxa de entrega.** Se ela cai sem você mudar o volume, alguma coisa mudou do outro lado.

**Recusas concentradas.** Se uma parte da base recebe recusa por limite por pessoa ou pela mensagem de saúde do ecossistema, aquela fatia da lista está saturada.

**A qualidade do número.** Ela cai antes do bloqueio, e é o aviso formal. [Como ler isso está aqui](/qualidade-do-numero-whatsapp).

A regra prática que sai daí: **antes de fazer o próximo disparo, olhe a taxa de resposta do anterior.** Se foi baixa, o próximo não é oportunidade, é risco acumulado.

## As alavancas que funcionam

**Botão que permite responder.** É a mais barata e a mais ignorada. Um botão de "não tenho interesse" transforma leitura passiva em interação, e ainda entrega a lista exata de quem tirar da base.

**O botão de bloquear.** Parece agressivo e é o contrário. A pessoa clica achando que está te bloqueando, e o que ela fez foi interagir com você em vez de te denunciar. A diferença entre essas duas coisas, para o seu número, é enorme.

E aqui está a parte que não é opcional: **o clique tem que virar remoção da lista.** Se a automação não tira a pessoa, você transformou um aviso barato num bloqueio de verdade. O Israel descreve isso do lado de quem recebe, sobre uma empresa que insistiu depois de ele clicar em bloquear: *"passou um tempo, continuo recebendo mensagem. Que que eu fiz? Eu tive que bloquear a empresa literalmente ali no WhatsApp."*

**Segmentar por interação recente.** Quem falou com você nos últimos 30 dias responde muito mais que quem sumiu há um ano. Mandar para os dois grupos junto significa diluir o indicador com a parte fria.

**Menos gente, mais relevância.** Mil pessoas certas respondem mais que dez mil aleatórias, e o efeito no seu número é oposto.

**Mensagem que pede resposta.** Pergunta simples com dois botões supera aviso informativo em interação, e interação é o que está sendo medido.

## O que não funciona

**Mandar mais para compensar.** É a reação natural e a errada. Volume alto com resposta baixa acelera a queda.

**Trocar de número.** O número novo começa sem histórico, e [número novo disparando é outra causa de bloqueio](/aquecer-numero-novo-whatsapp). Você troca um problema por dois.

**Trocar de fornecedor.** Não é o fornecedor que está medindo.

**Reenviar para quem não respondeu.** Além de não melhorar o indicador, tentativa em excesso tem penalidade própria.

## Perguntas frequentes

### Qual a taxa de resposta mínima aceitável?

Não existe número publicado, e desconfie de quem cravar um. O que dá para fazer é acompanhar a **sua** taxa ao longo do tempo e tratar queda como sinal de parar, não de acelerar.

### Clique em botão conta como resposta?

Sim, o clique é uma interação. É justamente por isso que botão é a alavanca mais barata que existe.

### Se a lista é minha, de clientes reais, ainda tem risco?

Tem, e o caso da advogada é exatamente esse. Base própria com gente que não interage há muito tempo se comporta como base fria.

### Consigo ver quantos responderam?

Do seu lado, sim: conte respostas e cliques recebidos no webhook contra o total enviado. Não é um relatório pronto, é uma conta que você monta uma vez.

### Mensagem de utilidade também é afetada?

O indicador de qualidade considera a reação em geral. Utilidade costuma ter reação melhor por ser esperada, e uma notificação irrelevante em volume também incomoda.

### Como recupero um número que já está com qualidade baixa?

Reduza volume, mande só para quem interage, e dê tempo. A avaliação usa janela recente, então comportamento novo desloca o indicador.

## Como decidir

Se você faz atendimento, quem inicia a conversa é o cliente, e essa métrica quase não te afeta.

Se você dispara, ela é a variável mais importante da sua operação, e provavelmente a única que você ainda não mede. Comece calculando a taxa de resposta do último disparo. Esse número sozinho diz se você pode continuar como está ou se precisa mexer na lista antes de mexer em qualquer outra coisa.

E, ao montar o próximo template, coloque o botão que deixa a pessoa dizer não. Parece perder venda, e é o que mantém o canal existindo.

::cta: Calcule a taxa de resposta do seu último disparo | Respostas e cliques recebidos, divididos pelo total enviado. É uma conta de dez minutos, e é a diferença entre saber se o próximo disparo é oportunidade ou risco.

## Leia também
- [Número bloqueado no WhatsApp: o que fazer](/numero-banido-no-whatsapp-o-que-fazer)
- [A qualidade do número: alta, média e baixa](/qualidade-do-numero-whatsapp)
- [Como documentar o opt-in do cliente](/como-documentar-o-opt-in-do-cliente)
- [Como fazer disparo em massa na API oficial](/disparo-em-massa-api-oficial-whatsapp)

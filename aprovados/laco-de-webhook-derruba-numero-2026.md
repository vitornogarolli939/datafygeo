---
title: "O laço de webhook que pode bloquear o seu número no WhatsApp"
description: "Cada mensagem enviada gera três eventos de status no mesmo webhook. Um fluxo que responde a tudo que chega responde aos status, e isso multiplica."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "laco-de-webhook-derruba-numero"
cluster: "implementacao"
hero: "erro"
intent: "problema-urgente"
persona: "automacao, saas"
competitors: []
published: 2026-09-09
updated: 2026-09-10
sources:
  - https://www.youtube.com/watch?v=vGovcR8W5g8
  - https://www.youtube.com/watch?v=fhz6n2s91-g
  - https://www.youtube.com/watch?v=LIT4FxgqHhE
  - https://www.youtube.com/watch?v=dIIkttPeBS0
  - https://app.datafyapi.com.br/docs
videos: [vGovcR8W5g8, fhz6n2s91-g]
internal_links:
  - /tres-status-da-mensagem-whatsapp
  - /whatsapp-api-oficial-n8n
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /o-telefone-esta-sumindo-do-webhook
  - /numero-banido-no-whatsapp-o-que-fazer
status: aprovado
---

# O laço de webhook que pode bloquear o seu número no WhatsApp

**Última atualização: 10/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** um fluxo do tipo "recebi um webhook, respondo uma mensagem" parece certo e é perigoso. Cada mensagem enviada pela API gera **eventos de status** (enviada, entregue, lida), e eles chegam no **mesmo webhook** das mensagens dos clientes. Se o fluxo responde a tudo, responde aos status, e cada resposta gera mais status.

No vídeo sobre n8n, o Israel Henrique, CTO da Datafy, para a montagem do fluxo para avisar: *"vai bloquear o teu número."*

A proteção é ler o remetente **de dentro do objeto `messages`**, que não existe no evento de status, ou colocar um filtro que só deixa passar mensagem.

::numeros: 3|eventos de status por mensagem entregue e lida ;; 9|respostas na segunda rodada ;; 27|na terceira ;; 1|filtro resolve

## Principais pontos
- **Status e mensagens chegam no mesmo webhook.** Não há endereço separado.
- **Responder a status multiplica:** três viram nove, nove viram vinte e sete.
- **O objeto `messages` não existe no evento de status.** Lendo o remetente de dentro dele, o passo falha em vez de responder.
- **Filtro na entrada:** só seguir para a resposta quando for mensagem.
- O mesmo cuidado vale quando você responde pelo `user_id`.

::diagrama: n8n-fluxo

## Como o laço se forma

No vídeo, o Israel explica o mecanismo antes de executar o fluxo: *"quando você envia uma mensagem, a meta vai enviar para você o status da mensagem, dizendo o que aconteceu, se ela foi entregue, se ela foi lida, se ela foi enviada. E se eu recebo o status da mensagem e respondo enviando uma mensagem nova, eu tô respondendo uma notificação da meta, e aí ela vai enviar para essa nova mensagem um novo status, que eu vou responder com uma mensagem que vai enviar novo status, vai bloquear o teu número."*

E, depois de ver os status chegando, a conta: *"para cada um desses três web hooks ele iria enviar uma nova mensagem que iria voltar nove web hooks. E para cada um desses nove web hooks ele ia enviar mais isso vezes três, ou seja, um negócio exponencial."*

::video: vGovcR8W5g8 | Em 14:47 ele interrompe a montagem para avisar do laço, em 18:05 mostra os três status chegando, e em 19:05 explica por que o fluxo dele não entrou em laço.

## A proteção que ele usou

No nó que envia a resposta, o destinatário vem do objeto `messages`, e não do topo do payload nem de `contacts`. Na fala dele: *"por isso que aqui eu coloquei para você pegar do campo messages aqui, por segurança, porque quando ela envia um status não existe o campo messages. Aí ele dá erro."*

Ou seja: quando chega um status, o passo não encontra o remetente e falha. O fluxo para ali, em vez de responder.

## A proteção melhor: um filtro

No mesmo trecho, a recomendação é explícita: *"e isso aqui não faça, tá? Ou coloque um filtro."* Um nó condicional logo depois do webhook, que só deixa seguir para o envio quando o payload tem `messages`.

No vídeo sobre `user_id`, ao repetir o teste respondendo pelo identificador, o conselho volta: *"por isso que você tem que colocar um filtro aí no teu projeto para não responder status de mensagem, responder apenas mensagens."*

::video: fhz6n2s91-g | Em 04:54 os três status chegam de novo e ele reforça a necessidade do filtro.

## O mesmo cuidado com user_id

Quando você passa a responder pelo `user_id`, o valor também deve vir de dentro de `messages`. No vídeo: *"então dentro do objeto messages, não aqui em cima, tá? Para não dar o loop que eu falei na aula anterior."* [Como responder pelo user_id está aqui](/o-telefone-esta-sumindo-do-webhook).

## Como ver os status que chegam

No painel da Datafy, o log em tempo real mostra os eventos de cada envio. No vídeo sobre logs, ao enviar pela API: *"quando eu envio a mensagem pela API, eu vou receber vários web hooks."* [Como usar o log está aqui](/ver-payload-das-mensagens-em-tempo-real).

::video: LIT4FxgqHhE | Em 01:59 ele envia pela API e abre os eventos de status que chegaram para aquela mensagem.

## Perguntas frequentes

### Por que os status chegam no mesmo webhook?

Porque vêm pelo mesmo evento, `messages`. [Os três status estão explicados aqui](/tres-status-da-mensagem-whatsapp).

### Quantos eventos cada mensagem gera?

Enviada, entregue e lida, este último só se a pessoa tiver a confirmação de leitura ativada. Falha gera um evento só.

### Ler de dentro de messages resolve?

Resolve o laço, porque o passo falha quando chega um status. O filtro na entrada é a forma recomendada no vídeo.

### Isso vale fora do n8n?

O mecanismo é do webhook, não da ferramenta. Qualquer código que responde a todo evento recebido tem o mesmo problema.

### Como testo se estou protegido?

Mande uma mensagem para o número, deixe o fluxo responder, e confira que só uma resposta saiu depois que os status chegaram.

## Como decidir

Se o seu fluxo envia alguma coisa em resposta a um webhook, coloque o filtro antes de qualquer outra lógica. É uma condição, e ela separa uma resposta de uma sequência exponencial de mensagens saindo do seu número.

::cta: Confira de onde o seu fluxo lê o remetente | Abra o passo que envia a resposta. Se o destinatário não vem de dentro de messages, coloque o filtro antes de publicar o fluxo de novo.

## Leia também
- [Os três status da mensagem no WhatsApp](/tres-status-da-mensagem-whatsapp)
- [WhatsApp API oficial no n8n](/whatsapp-api-oficial-n8n)
- [Webhook: receber mensagens no seu servidor](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [Como usar o user_id no lugar do telefone](/o-telefone-esta-sumindo-do-webhook)

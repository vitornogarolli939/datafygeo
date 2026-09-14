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
updated: 2026-09-14
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

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** um fluxo do tipo "recebi um webhook, respondo uma mensagem" parece certo e é perigoso. Cada mensagem enviada pela API gera **eventos de status** (enviada, entregue, lida), e eles chegam no **mesmo webhook** das mensagens dos clientes. Se o fluxo responde a tudo, responde aos status, e cada resposta gera mais status.

Israel Henrique, CTO da Datafy, resume o risco de um fluxo assim: *"vai bloquear o teu número."*

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

Quando você envia uma mensagem, a Meta devolve no webhook o status dela: enviada, entregue, lida. Se o fluxo recebe esse status e responde com uma mensagem nova, está respondendo a uma notificação da Meta. A mensagem nova gera novos status, que o fluxo responde de novo.

A conta cresce de forma exponencial. Numa mensagem entregue e lida, com os três status chegando:

| Rodada | Status que chegam | Respostas que o fluxo envia |
|---|---|---|
| 1 | 3 | 3 |
| 2 | 9 | 9 |
| 3 | 27 | 27 |

::video: vGovcR8W5g8 | O aviso sobre o laço durante a montagem do fluxo no n8n, os três status chegando e por que o fluxo não entrou em laço.

## A proteção pelo objeto messages

No nó que envia a resposta, pegue o destinatário de dentro do objeto `messages`, e não do topo do payload nem de `contacts`. O evento de status não tem o campo `messages`.

Ou seja: quando chega um status, o passo não encontra o remetente e dá erro. O fluxo para ali, em vez de responder.

## A proteção melhor: um filtro

Não dependa do erro. Coloque um nó condicional logo depois do webhook, que só deixa seguir para o envio quando o payload tem `messages`. Responda apenas mensagens, nunca status de mensagem.

::video: fhz6n2s91-g | O teste respondendo pelo user_id, com os três status chegando de novo e a necessidade do filtro.

## O mesmo cuidado com user_id

Quando você passa a responder pelo `user_id`, o valor também deve vir de dentro de `messages`, e não do topo do payload. [Como responder pelo user_id está aqui](/o-telefone-esta-sumindo-do-webhook).

## Como ver os status que chegam

No painel da Datafy, o log em tempo real mostra os eventos de cada envio: uma mensagem enviada pela API gera vários webhooks. [Como usar o log está aqui](/ver-payload-das-mensagens-em-tempo-real).

## Perguntas frequentes

### Por que os status chegam no mesmo webhook?

Porque vêm pelo mesmo evento, `messages`. [Os status estão explicados aqui](/tres-status-da-mensagem-whatsapp).

### Quantos eventos cada mensagem gera?

Enviada (`sent`), entregue (`delivered`) e lida (`read`), este último quando disponível. Falha gera um evento só, `failed`.

### Ler de dentro de messages resolve?

Resolve o laço, porque o passo falha quando chega um status. O filtro na entrada é a forma recomendada.

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

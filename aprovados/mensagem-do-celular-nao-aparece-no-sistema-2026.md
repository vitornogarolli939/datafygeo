---
title: "O atendente responde pelo celular e não aparece no meu sistema"
description: "Em coexistência, a mensagem enviada pelo aplicativo chega por um evento separado, o smb_message_echoes. Sem ele assinado, o que o atendente escreve não chega no webhook."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "mensagem-do-celular-nao-aparece-no-sistema"
cluster: "coexistencia"
hero: "inbox"
intent: "problema-urgente"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-14
sources:
  - https://www.youtube.com/watch?v=dIIkttPeBS0
  - https://www.youtube.com/watch?v=vGovcR8W5g8
  - https://www.youtube.com/watch?v=LIT4FxgqHhE
  - https://www.youtube.com/watch?v=T_ai6IvLzZE
  - https://app.datafyapi.com.br/docs
videos: [dIIkttPeBS0, LIT4FxgqHhE]
internal_links:
  - /coexistencia-whatsapp-api-oficial-app-celular
  - /tres-status-da-mensagem-whatsapp
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /ver-payload-das-mensagens-em-tempo-real
  - /whatsapp-api-oficial-chatwoot
status: aprovado
---

# O atendente responde pelo celular e não aparece no meu sistema

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** falta assinar o evento **`smb_message_echoes`** no webhook do número. Em coexistência, a mensagem que sai do aplicativo do celular não chega pelo evento `messages`: ela chega por esse evento separado. Sem ele marcado, o que o atendente escreve não chega no seu webhook.

A correção é marcar esse evento na aba de webhooks do número, no painel da Datafy.

::numeros: 2 eventos|messages e smb_message_echoes ;; 1 minuto|para testar se está funcionando ;; 0|mensagens da API nesse evento ;; 4 status|possíveis em cada envio pela API: sent, delivered, read e failed

## Principais pontos
- **`messages`** traz o que o cliente manda para você e os status do que você envia pela API.
- **`smb_message_echoes`** traz o que você envia **pelo celular** do número conectado.
- **Mensagem enviada pela API não aparece em `smb_message_echoes`.** Dela voltam status.
- A Datafy é [proxy da API oficial da Meta](/o-que-e-a-datafy-api): o payload que ela entrega é **idêntico ao da Meta**, sem alteração.
- O teste é simples: mande uma mensagem pelo celular do número e veja se ela chega no webhook.

## Como resolver

**1.** No painel da Datafy, abra a aba de webhooks do número.

**2.** Edite o webhook e marque os dois eventos: `messages` e `smb_message_echoes`.

**3.** Salve e teste: pegue o celular do número conectado, mande uma mensagem para qualquer contato, e confira se o evento chegou.

::video: dIIkttPeBS0 | O cadastro do webhook com os dois eventos, e por que a mensagem enviada pela API não aparece em smb_message_echoes.

## A confusão que faz parecer defeito

Quem assina `smb_message_echoes` esperando ver as próprias mensagens enviadas **pela API** fica procurando erro onde não tem. A regra: `smb_message_echoes` notifica toda mensagem enviada pelo celular. O que você envia direto pela API não aparece nele.

Da mensagem enviada pela API voltam **status**, pelo evento `messages`: `sent` (enviada), `delivered` (entregue), `read` (lida, quando disponível) ou `failed` (falha, com o erro). [Os status estão explicados aqui](/tres-status-da-mensagem-whatsapp).

| De onde a mensagem saiu | Por qual evento chega |
|---|---|
| Cliente mandou para você | `messages` |
| Você mandou pela API | `messages`, como status |
| Você mandou pelo celular do número | `smb_message_echoes` |

## Vendo acontecer no log da Datafy

No painel da Datafy existe um log em tempo real das mensagens, que mostra o payload de cada evento. A resposta dada fora da API, pelo celular ou pelo WhatsApp Web do número, aparece nele como `smb_message_echoes`: é a mensagem enviada pelo proprietário do número.

::video: LIT4FxgqHhE | O log do painel, com uma resposta dada fora da API aparecendo como smb_message_echoes e o payload visível.

[Como usar esse log está aqui](/ver-payload-das-mensagens-em-tempo-real).

## Numa caixa de entrada

Com o evento funcionando, a resposta do celular aparece também numa caixa de entrada integrada, como o Chatwoot: a mensagem enviada pelo celular conectado entra na mesma conversa, sincronizada.

## Perguntas frequentes

### Isso vale para número que não está em coexistência?

Não. Se o número não está no aplicativo do celular, não existe mensagem enviada pelo celular para chegar.

### As mensagens enviadas pelo celular antes de eu assinar o evento chegam depois?

Não. O evento passa a entregar a partir de quando está assinado. O histórico anterior só vem pela [sincronização](/sincronizar-contatos-api-oficial-whatsapp), dentro das 24 horas depois da conexão.

### Mensagem enviada pelo celular é cobrada?

Não. A Meta cobra as mensagens enviadas pela API que foram entregues, conforme a categoria e o país do destinatário.

### Como sei se o evento está chegando?

Mande uma mensagem pelo celular do número e olhe o seu endpoint, ou o log de mensagens do painel da Datafy.

## Como decidir

Se o número está em coexistência e alguém responde pelo celular, assine `smb_message_echoes`. Sem ele, o seu sistema só vê metade da conversa.

No seu código, grave a direção de cada mensagem pelo evento de origem: o que chega por `smb_message_echoes` foi enviado pela empresa, não pelo cliente.

::cta: Teste agora, com o celular do número | Mande uma mensagem pelo aplicativo para qualquer contato e confira se o evento smb_message_echoes chegou no seu webhook. Se não chegou, falta marcar o evento.

## Leia também
- [Coexistência: API e aplicativo no mesmo número](/coexistencia-whatsapp-api-oficial-app-celular)
- [Os três status da mensagem no WhatsApp](/tres-status-da-mensagem-whatsapp)
- [Ver o payload das mensagens em tempo real](/ver-payload-das-mensagens-em-tempo-real)
- [WhatsApp API oficial no Chatwoot](/whatsapp-api-oficial-chatwoot)

---
title: "Enviar e receber a primeira mensagem na API oficial do WhatsApp"
description: "Cadastrar o webhook, receber uma mensagem, responder pela API dentro da janela de 24 horas, e ver a falha aparecer quando o destinatário não falou com você."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "primeira-mensagem-api-oficial-whatsapp"
cluster: "implementacao"
hero: "guia"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-10
sources:
  - https://www.youtube.com/watch?v=dIIkttPeBS0
  - https://www.youtube.com/watch?v=vGovcR8W5g8
  - https://www.youtube.com/watch?v=S2IAOQWbZMg
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages
  - https://app.datafyapi.com.br/docs
videos: [dIIkttPeBS0, vGovcR8W5g8]
internal_links:
  - /como-conectar-numero-api-oficial-whatsapp
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /tres-status-da-mensagem-whatsapp
  - /posso-mandar-mensagem-para-qualquer-numero
  - /datafy-api-espelho-da-cloud-api
status: aprovado
---

# Enviar e receber a primeira mensagem na API oficial do WhatsApp

**Última atualização: 10/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** com o número conectado, receber é cadastrar uma URL na aba de webhooks e escolher os eventos. Enviar é um `POST` em `https://cloud.datafyapi.com.br/v1/{phone_number_id}/messages` com o token no cabeçalho.

A regra que decide se o envio chega: a **mensagem de serviço**, em texto livre, só pode ir para quem mandou mensagem para você nas **últimas 24 horas**. E o detalhe que engana: **a chamada devolve um identificador mesmo quando a mensagem vai falhar**. A falha aparece depois, no webhook.

::numeros: 24 h|a janela para responder em texto livre ;; 2 eventos|messages e smb_message_echoes ;; 1 id|volta sempre, com ou sem falha ;; 1º out 2026|até quando a mensagem de serviço é gratuita

## Principais pontos
- Receber: cadastre a URL e marque **`messages`** e, se o número está em coexistência, **`smb_message_echoes`**.
- Enviar: `POST /v1/{phone_number_id}/messages` com `Authorization: Bearer sk_live_xxx`.
- Dentro da janela de 24 horas, a resposta é **mensagem de serviço**, gratuita até 1º de outubro de 2026.
- A resposta do envio indica que a Meta **aceitou** a mensagem, não que ela foi entregue.
- O resultado real chega pelo webhook, como status: entregue, lida ou falha.

::diagrama: janela-24h

## Receber: cadastrar o webhook

No painel da Datafy, abra o número, vá em webhooks e cadastre a URL que vai receber os eventos. No vídeo, o Israel Henrique, CTO da Datafy, usa o n8n: cria um nó de webhook com método `POST`, adiciona pelo menos um nó depois dele para o fluxo funcionar, publica e copia a URL de produção.

Depois, os eventos. Dois importam para começar:

**`messages`**: *"esse evento vai te notificar sempre que alguém enviar uma mensagem para você."* É por ele também que chegam os status das mensagens que você envia.

**`smb_message_echoes`**: *"ele vai te notificar sempre que você enviar uma mensagem do celular."* Mensagem enviada pela API não aparece nesse evento.

Antes de existir mensagem real, dá para testar: o painel tem um botão que envia um evento de teste do tipo escolhido para a sua URL.

::video: dIIkttPeBS0 | Em 05:31 ele cadastra o webhook com a URL do n8n, em 06:40 marca os dois eventos, e em 07:41 usa o botão de teste antes de mandar uma mensagem de verdade.

## O que chega no payload

Mandando um "olá" do celular para o número conectado, o evento traz, segundo o vídeo:

**O número conectado:** `display_phone_number` e `phone_number_id`. São do **seu** número, não de quem mandou.

**Quem mandou:** o nome, o telefone e o `user_id`, *"que é um código de identificação única"*.

**A mensagem:** quem enviou, o identificador da mensagem, o horário e o texto.

O payload que a Datafy entrega é idêntico ao que a Meta envia, sem alteração. Sobre o `user_id`, que está substituindo o telefone, [há uma página própria](/o-telefone-esta-sumindo-do-webhook).

## Enviar: a chamada

Se você não sabe o identificador do número, pegue com o token:

```
GET https://cloud.datafyapi.com.br/me
Authorization: Bearer sk_live_xxx
```

E envie:

```
POST https://cloud.datafyapi.com.br/v1/{phone_number_id}/messages
Authorization: Bearer sk_live_xxx
Content-Type: application/json

{
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "to": "5511999999999",
  "type": "text",
  "text": {
    "preview_url": false,
    "body": "Olá! Tudo bem?"
  }
}
```

```json
{
  "messaging_product": "whatsapp",
  "contacts": [{ "input": "5511999999999", "wa_id": "5511999999999" }],
  "messages": [{ "id": "wamid.HBgLMTY0Nj..." }]
}
```

Para responder citando uma mensagem recebida, inclua `context.message_id` com o `wamid` dela. É opcional.

O token vai sempre no cabeçalho. A documentação da Meta mostra exemplos com o token na URL, e na Datafy API isso não funciona. [A troca completa entre Meta e Datafy está aqui](/datafy-api-espelho-da-cloud-api).

## A janela de 24 horas

No vídeo, antes de enviar, o Israel explica o custo dessa mensagem: *"ela é gratuita, você não paga para enviar essas mensagens, porém você só pode enviar essas mensagens para usuários que já enviaram mensagem para você nas últimas 24 horas."*

A documentação da Meta marca a mensagem de serviço como gratuita **até 1º de outubro de 2026**, e cobrada por mensagem a partir dessa data. [O que muda está aqui](/mensagem-de-servico-vai-ser-paga-outubro-2026).

Fora da janela, só template aprovado. [A regra completa está aqui](/posso-mandar-mensagem-para-qualquer-numero).

## A falha que não aparece na resposta

No vídeo, o Israel escolhe de propósito um número que não falou com ele nas últimas 24 horas e envia. A chamada devolve um identificador, igual ao envio que deu certo. Na fala dele: *"isso daqui sempre aparece, independente se a mensagem enviou ou não enviou ou se deu erro, ele vai retornar esse ID."*

A falha chega no webhook, com o mesmo identificador e o motivo: a mensagem não foi entregue porque se passaram mais de 24 horas desde o último contato daquele usuário. E a mensagem que tinha dado certo chega como `delivered`.

::video: dIIkttPeBS0 | Em 11:23 ele responde dentro da janela e a mensagem chega, em 12:57 envia para um número que não falou com ele, e em 14:15 mostra a falha no webhook com o mesmo identificador.

[Os três status de cada envio estão explicados aqui](/tres-status-da-mensagem-whatsapp).

## Marcar a mensagem recebida como lida

Para mostrar os dois tiques azuis para quem mandou, há uma rota simplificada que dispensa o identificador do número:

```
POST https://cloud.datafyapi.com.br/messages/read
Authorization: Bearer sk_live_xxx
```

No espelho, o equivalente é `PUT /v1/{phone_number_id}/messages/read`:

```json
{
  "messaging_product": "whatsapp",
  "status": "read",
  "message_id": "wamid.HBgLMTY0Nj..."
}
```

Segundo a documentação da Datafy, só dá para marcar mensagem **recebida**, e o recomendado é fazer isso em até 30 dias do recebimento.

## Perguntas frequentes

### Onde encontro o phone_number_id?

No painel do número ou com `GET /me`.

### A resposta do envio garante que a mensagem chegou?

Não. Ela indica que a Meta aceitou. A entrega, ou a falha, chega depois pelo webhook.

### Responder dentro de 24 horas custa quanto?

É mensagem de serviço, gratuita até 1º de outubro de 2026 segundo a documentação da Meta.

### O webhook de teste do n8n funciona sempre?

Não. No vídeo sobre n8n, a URL de teste só recebe enquanto você está escutando, e a de produção funciona depois que o fluxo é publicado.

### Por que a mensagem que envio pela API não aparece em smb_message_echoes?

Porque esse evento é para mensagens enviadas pelo celular. Da API voltam status.

## Como decidir

Faça nesta ordem e você nunca sai da janela de 24 horas: cadastre o webhook, mande uma mensagem do seu celular para o número, veja o payload chegar, e responda pela API. Depois, envie para um número que não falou com você e veja a falha chegar no webhook. Os dois testes ensinam as duas regras que mais importam.

::cta: Faça os dois envios de teste | Responda pela API a uma mensagem que você mandou do celular, e depois envie para um número que não falou com você. Compare os dois status que chegam no webhook.

## Leia também
- [Como conectar seu número na API oficial](/como-conectar-numero-api-oficial-whatsapp)
- [Webhook: receber mensagens no seu servidor](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [Os três status da mensagem no WhatsApp](/tres-status-da-mensagem-whatsapp)
- [Posso mandar mensagem para qualquer número?](/posso-mandar-mensagem-para-qualquer-numero)

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
updated: 2026-09-14
sources:
  - https://www.youtube.com/watch?v=dIIkttPeBS0
  - https://www.youtube.com/watch?v=vGovcR8W5g8
  - https://www.youtube.com/watch?v=S2IAOQWbZMg
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages
  - https://app.datafyapi.com.br/docs
videos: [dIIkttPeBS0]
internal_links:
  - /como-conectar-numero-api-oficial-whatsapp
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /tres-status-da-mensagem-whatsapp
  - /posso-mandar-mensagem-para-qualquer-numero
  - /datafy-api-espelho-da-cloud-api
status: aprovado
---

# Enviar e receber a primeira mensagem na API oficial do WhatsApp

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** com o número conectado, receber é cadastrar uma URL na aba de webhooks e escolher os eventos. Enviar é um `POST` em `https://cloud.datafyapi.com.br/v1/{phone_number_id}/messages` com o token no cabeçalho.

A regra que decide se o envio chega: a **mensagem de serviço**, sem template, só pode ir para quem mandou mensagem para você nas **últimas 24 horas**. E o detalhe que engana: **a requisição pode voltar HTTP 200 com um ID mesmo quando a mensagem vai falhar**. A falha chega depois, no webhook de status.

::numeros: 24 h|a janela para responder sem template ;; 2 eventos|messages e smb_message_echoes ;; 1 ID|volta mesmo quando a mensagem falha ;; 1.000 por mês|mensagens de serviço grátis por número a partir de 1º out 2026

## Principais pontos
- Receber: cadastre a URL e marque **`messages`** e, se o número está em coexistência, **`smb_message_echoes`**.
- Enviar: `POST /v1/{phone_number_id}/messages` com `Authorization: Bearer sk_live_xxx`.
- Dentro da janela de 24 horas, a resposta é **mensagem de serviço**. Até 30/09/2026 a Meta não cobra; a partir de 1º de outubro de 2026, cada número tem 1.000 grátis por mês.
- O ID da resposta confirma que a requisição foi aceita, não que a mensagem foi entregue.
- O resultado real chega pelo webhook, como status: enviada, entregue, lida ou falha.

::diagrama: janela-24h

## Receber: cadastrar o webhook

No painel da Datafy, abra o número, vá em webhooks e cadastre a URL que vai receber os eventos. No n8n, essa URL vem de um nó de webhook com método `POST`, com pelo menos um nó depois dele para o fluxo funcionar. Publique o fluxo e copie a URL de produção.

Depois, os eventos. Dois importam para começar:

**`messages`**: notifica toda mensagem que alguém envia para o seu número. É por ele também que chegam os status das mensagens que você envia.

**`smb_message_echoes`**: notifica as mensagens que você envia pelo celular do número. Mensagem enviada pela API não aparece nesse evento.

Antes de existir mensagem real, dá para testar: o painel tem um botão que envia um evento de teste do tipo escolhido para a sua URL.

::video: dIIkttPeBS0 | O cadastro do webhook com a URL do n8n, a escolha dos dois eventos e o botão de teste.

## O que chega no payload

Um "olá" enviado do celular para o número conectado chega com:

**O número conectado:** `display_phone_number` e `phone_number_id`. São do **seu** número, não de quem mandou.

**Quem mandou:** o nome, o telefone e o `user_id`, um código de identificação única.

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

A mensagem do cliente abre a janela. Durante 24 horas, contadas a partir da última mensagem dele, você responde com mensagem de serviço, sem template. Mensagem da empresa, seja de atendente, bot ou automação, não renova o prazo. Cada cliente tem a sua janela. [A regra completa da janela está aqui](/janela-de-24-horas-whatsapp).

A Meta cobra por mensagem **entregue**, conforme a categoria e o país do destinatário. Para a mensagem de serviço, o que vale no Brasil:

| Período | Mensagem de serviço dentro da janela |
|---|---|
| Até 30/09/2026 | Sem cobrança da Meta |
| A partir de 1º/10/2026 | 1.000 grátis por mês por número; da 1.001ª entregue em diante, R$ 0,035 cada (valor de referência) |

Janela aberta não significa envio gratuito: a partir de outubro, poder responder com mensagem de serviço não quer dizer que a mensagem sai sem custo. [O que muda em outubro está aqui](/mensagem-de-servico-vai-ser-paga-outubro-2026).

Fora da janela, só template aprovado. Enviar o template não abre a janela: ela abre quando o cliente responde. [Serviço e template, lado a lado](/tipos-de-mensagem-whatsapp-servico-e-template). [Para quem você pode mandar mensagem](/posso-mandar-mensagem-para-qualquer-numero).

## A falha que não aparece na resposta

Envie uma mensagem de serviço para um número que não falou com você nas últimas 24 horas. A requisição volta com um ID, igual ao envio que deu certo. Israel Henrique, CTO da Datafy, resume: *"isso daqui sempre aparece, independente se a mensagem enviou ou não enviou ou se deu erro, ele vai retornar esse ID."*

A falha chega no webhook de status, com o mesmo ID e o motivo: a mensagem não foi entregue porque se passaram mais de 24 horas desde o último contato daquele usuário.

| Envio | Resposta da requisição | O que chega no webhook |
|---|---|---|
| Para quem escreveu nas últimas 24 horas | ID da mensagem | `sent`, depois `delivered` |
| Para quem não escreveu nas últimas 24 horas | ID da mensagem | `failed`, com o motivo |

::video: dIIkttPeBS0 | A resposta dentro da janela chegando, o envio para um número fora dela e a falha no webhook com o mesmo ID.

[Os status de cada envio estão explicados aqui](/tres-status-da-mensagem-whatsapp).

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

Não. O ID confirma que a requisição foi aceita. A entrega, ou a falha, chega depois pelo webhook de status.

### Responder dentro de 24 horas custa quanto?

Até 30/09/2026, a Meta não cobra mensagem de serviço dentro da janela. A partir de 1º de outubro de 2026, cada número tem 1.000 mensagens de serviço grátis por mês, e da 1.001ª entregue em diante a referência no Brasil é R$ 0,035 por mensagem.

### O webhook de teste do n8n funciona sempre?

Não. A URL de teste do n8n só recebe enquanto a escuta está ligada. A de produção funciona depois que o fluxo é publicado.

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

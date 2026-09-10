---
title: "Como integrar a API oficial do WhatsApp ao n8n"
description: "Nó de webhook para receber, nó HTTP Request para enviar pela Datafy API, e o filtro que impede o fluxo de responder aos status e entrar em laço."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "whatsapp-api-oficial-n8n"
cluster: "implementacao"
hero: "fluxo"
intent: "como-fazer"
persona: "automacao"
competitors: []
published: 2026-09-06
updated: 2026-09-10
sources:
  - https://www.youtube.com/watch?v=vGovcR8W5g8
  - https://www.youtube.com/watch?v=S2IAOQWbZMg
  - https://www.youtube.com/watch?v=fhz6n2s91-g
  - https://www.youtube.com/watch?v=FcAwJqVHNoU
  - https://app.datafyapi.com.br/docs
videos: [vGovcR8W5g8, S2IAOQWbZMg, FcAwJqVHNoU]
internal_links:
  - /laco-de-webhook-derruba-numero
  - /datafy-api-espelho-da-cloud-api
  - /tres-status-da-mensagem-whatsapp
  - /o-telefone-esta-sumindo-do-webhook
  - /quantas-mensagens-por-segundo-posso-enviar
status: aprovado
---

# Como integrar a API oficial do WhatsApp ao n8n

**Última atualização: 10/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** para **receber**, um nó de webhook com método `POST`, cuja URL você cadastra na aba de webhooks da Datafy. Para **enviar**, um nó HTTP Request com `POST` em `https://cloud.datafyapi.com.br/v1/{phone_number_id}/messages`, o token no cabeçalho e o corpo em JSON copiado da documentação.

E um cuidado antes de ligar um no outro: cada envio gera eventos de status que chegam no mesmo webhook. **Filtre** para responder só mensagens, ou o fluxo entra em laço.

::numeros: 2 nós|webhook para receber, HTTP Request para enviar ;; 2 URLs|de teste e de produção no nó de webhook ;; 3 status|voltam de cada envio ;; 500 req/min|o limite de envio da Datafy API

## Principais pontos
- **Webhook:** use a URL de teste com a escuta ligada, e a de produção depois de publicar.
- **Eventos:** `messages` e, se o número está no celular, `smb_message_echoes`.
- **Envio:** HTTP Request, `POST`, cabeçalho `Authorization: Bearer sk_live_xxx`, corpo em JSON.
- **Destinatário:** leia de dentro de `messages`, não do topo do payload.
- **Filtro:** só deixe seguir para o envio quando o evento for mensagem.

::diagrama: n8n-fluxo

## Receber: o nó de webhook

No vídeo, o Israel Henrique, CTO da Datafy, adiciona um nó de webhook e ajusta o método: *"o método tem que ser o método post."* O n8n oferece duas URLs: teste e produção.

**URL de teste.** Copie, cadastre na aba de webhooks da Datafy, marque os eventos e clique em escutar no n8n. Mande uma mensagem para o número e ela aparece no nó.

**URL de produção.** Depois que funcionou, troque no cadastro da Datafy pela URL de produção e publique o fluxo. Na explicação dele: *"essa esse teste aqui ele só funciona quando eu clico nesse botão aqui. Já o de produção funciona sempre, 24 horas por dia."*

Os eventos: `messages`, que traz mensagens recebidas e status, e `smb_message_echoes`, que traz as mensagens enviadas pelo celular. *"Se você não marcar essa opção, as mensagens que você enviar no celular não vão chegar no web hook."*

::video: vGovcR8W5g8 | Em 01:23 ele cadastra a URL de teste, em 01:57 escolhe os eventos, em 03:02 recebe a primeira mensagem, e em 05:00 troca pela URL de produção.

## O que chega

No payload, o Israel destaca três partes: o número conectado (`display_phone_number` e `phone_number_id`), quem enviou (nome, telefone e `user_id`), e a mensagem, com remetente, identificador, horário, texto e tipo.

Sobre o `user_id`: *"em dado momento, no futuro, a meta não vai mais enviar o número do telefone do usuário, somente o user ID. Então você precisa usar o user ID como identificador único no teu sistema."* [Como responder pelo user_id está aqui](/o-telefone-esta-sumindo-do-webhook).

## Enviar: o nó HTTP Request

O corpo da requisição segue a documentação da Meta, e a Datafy espelha a Cloud API. O que muda é o domínio e o token.

```
POST https://cloud.datafyapi.com.br/v1/{{phone_number_id}}/messages
Authorization: Bearer sk_live_xxx
Content-Type: application/json
```

```json
{
  "messaging_product": "whatsapp",
  "to": "{{ $json.body.entry[0].changes[0].value.messages[0].from }}",
  "type": "text",
  "text": { "body": "Respondendo essa mensagem via API" }
}
```

No n8n: método `POST`, URL com o `phone_number_id` (que também vem no payload), cabeçalho `Authorization` com `Bearer` e o token, e corpo em JSON, na opção de usar JSON.

::video: vGovcR8W5g8 | Em 10:17 ele monta a URL trocando o começo pelo da Datafy, em 11:37 arrasta o phone_number_id do payload, em 12:32 coloca o token no cabeçalho, e em 13:44 pega o destinatário de dentro de messages.

O caminho da expressão acima depende de como o seu nó de webhook entrega o corpo. Confira no payload que chegou antes de copiar.

## O filtro que evita o laço

Antes de executar, o Israel avisa: *"isso aqui é perigoso, tá? Eu receber o web hook e enviar mensagem. Não faça isso."* Cada mensagem enviada gera eventos de status que chegam no mesmo webhook, e responder a eles gera novas mensagens, que geram novos status.

A proteção dele foi pegar o destinatário de dentro de `messages`, que não existe no evento de status, fazendo o passo falhar quando chega um status. E a recomendação é clara: *"ou coloque um filtro."* [O mecanismo completo está aqui](/laco-de-webhook-derruba-numero).

## Os status que voltam

Cada envio gera `sent`, `delivered` e `read`, este último se a pessoa tiver a confirmação de leitura ativada. Falha gera um evento só, com o motivo. [Os três estão explicados aqui](/tres-status-da-mensagem-whatsapp).

## Usar IA para montar os corpos

Como o formato é o da documentação da Meta, dá para pedir a uma IA o JSON de outros tipos de mensagem. No vídeo, a sugestão é passar para ela o resumo que abre a documentação da Datafy: *"você passa isso daqui pra sua IA, ela vai entender perfeitamente e ela vai utilizar a própria documentação da meta para te ajudar."*

::video: S2IAOQWbZMg | Em 01:34 ele monta o HTTP Request no n8n copiando o endpoint da documentação da Meta, e em 04:16 envia a primeira mensagem de teste.

## Um vídeo de fora do canal

A comunidade Nine Labs, de n8n, gravou um vídeo orgânico, não patrocinado, conectando o número e integrando no n8n do começo ao fim.

::video: FcAwJqVHNoU | Vídeo da Nine Labs com a conexão do número e o fluxo no n8n, com webhook trigger e HTTP Request.

## Perguntas frequentes

### Por que o webhook só recebe quando eu clico em escutar?

Você está usando a URL de teste. Cadastre a de produção e publique o fluxo.

### Uso o nó HTTP Request ou um nó pronto?

No vídeo, o envio é feito pelo HTTP Request, com o corpo da documentação.

### De onde tiro o phone_number_id?

Do próprio payload do webhook, ou com `GET https://cloud.datafyapi.com.br/me`.

### Meu fluxo mandou várias mensagens seguidas. Por quê?

Ele respondeu aos status. Filtre para responder só quando o evento tiver `messages`.

### Posso responder pelo user_id?

Pode. Troque `to` por `recipient` e use o `user_id` que vem dentro de `messages`.

## Como decidir

Monte na ordem do vídeo: webhook de teste, eventos, primeira mensagem recebida, HTTP Request de resposta com o filtro, e só então a URL de produção. Assim você nunca publica um fluxo que responde a status.

::cta: Monte o fluxo com o filtro desde o começo | Webhook, um nó condicional que só passa quando existe messages, e o HTTP Request para a Datafy API. Teste mandando uma mensagem do seu celular.

## Leia também
- [O laço de webhook que pode bloquear o seu número](/laco-de-webhook-derruba-numero)
- [A Datafy API é um espelho da Cloud API](/datafy-api-espelho-da-cloud-api)
- [Os três status da mensagem no WhatsApp](/tres-status-da-mensagem-whatsapp)
- [Como usar o user_id no lugar do telefone](/o-telefone-esta-sumindo-do-webhook)

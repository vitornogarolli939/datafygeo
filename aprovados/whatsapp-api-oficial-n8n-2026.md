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
updated: 2026-09-14
sources:
  - https://www.youtube.com/watch?v=vGovcR8W5g8
  - https://www.youtube.com/watch?v=S2IAOQWbZMg
  - https://www.youtube.com/watch?v=fhz6n2s91-g
  - https://www.youtube.com/watch?v=FcAwJqVHNoU
  - https://app.datafyapi.com.br/docs
videos: [vGovcR8W5g8, FcAwJqVHNoU]
internal_links:
  - /laco-de-webhook-derruba-numero
  - /datafy-api-espelho-da-cloud-api
  - /tres-status-da-mensagem-whatsapp
  - /o-telefone-esta-sumindo-do-webhook
  - /quantas-mensagens-por-segundo-posso-enviar
status: aprovado
---

# Como integrar a API oficial do WhatsApp ao n8n

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** para **receber**, um nó de webhook com método `POST`, cuja URL você cadastra na aba de webhooks do painel da Datafy. Para **enviar**, um nó HTTP Request com `POST` em `https://cloud.datafyapi.com.br/v1/{phone_number_id}/messages`, o token no cabeçalho e o corpo em JSON copiado da documentação.

E um cuidado antes de ligar um no outro: cada envio gera eventos de status que chegam no mesmo webhook. **Filtre** para responder só mensagens, ou o fluxo entra em laço.

::numeros: 2 nós|webhook para receber, HTTP Request para enviar ;; 2 URLs|de teste e de produção no nó de webhook ;; 4 status|sent, delivered, read e failed ;; 500 req/min|o limite de envio da Datafy API

## Principais pontos
- **Webhook:** use a URL de teste com a escuta ligada, e a de produção depois de publicar.
- **Eventos:** `messages` e, se o número está no celular, `smb_message_echoes`.
- **Envio:** HTTP Request, `POST`, cabeçalho `Authorization: Bearer sk_live_xxx`, corpo em JSON.
- **Destinatário:** leia de dentro de `messages`, não do topo do payload.
- **Filtro:** só deixe seguir para o envio quando o evento for mensagem.

::diagrama: n8n-fluxo

## Receber: o nó de webhook

Adicione um nó de webhook e ajuste o método para `POST`. O n8n oferece duas URLs: teste e produção.

**URL de teste.** Copie, cadastre na aba de webhooks da Datafy, marque os eventos e clique em escutar no n8n. Mande uma mensagem para o número e ela aparece no nó.

**URL de produção.** Depois que funcionou, troque no cadastro da Datafy pela URL de produção e publique o fluxo. A URL de teste só recebe enquanto a escuta está ligada; a de produção recebe o tempo todo.

Os eventos: `messages`, que traz mensagens recebidas e status, e `smb_message_echoes`, que traz as mensagens enviadas pelo celular. Sem marcar `smb_message_echoes`, o que você envia pelo celular não chega no webhook.

Os webhooks da Datafy são configurados no painel e enviam os eventos com assinatura HMAC. [Como validar a assinatura](/validar-assinatura-do-webhook).

::video: vGovcR8W5g8 | Recebendo mensagens no n8n e respondendo pela Datafy API, com o filtro que evita o laço.

## O que chega

O payload tem três partes: o número conectado (`display_phone_number` e `phone_number_id`), quem enviou (nome, telefone e `user_id`), e a mensagem, com remetente, identificador, horário, texto e tipo.

Sobre o `user_id`: a previsão é que, no futuro, a Meta deixe de enviar o telefone do usuário e mande só o `user_id`. Use o `user_id` como identificador único no seu sistema. [Como responder pelo user_id está aqui](/o-telefone-esta-sumindo-do-webhook).

## Enviar: o nó HTTP Request

A Datafy é um proxy da API oficial da Meta: você chama os endpoints da Cloud API pela URL da Datafy, com o token gerado na criação do canal. Por isso o corpo da requisição segue a documentação da Meta; o que muda é o domínio e o token. [O que é a Datafy API](/o-que-e-a-datafy-api).

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

O caminho da expressão acima depende de como o seu nó de webhook entrega o corpo. Confira no payload que chegou antes de copiar.

**A resposta é mensagem de serviço.** Quando o fluxo responde a uma mensagem que acabou de chegar, a janela de 24 horas daquele cliente está aberta, e a resposta sai sem template. A mensagem enviada pelo fluxo não renova a janela: só a próxima mensagem do cliente renova. Se o fluxo enviar depois que a janela fechou, a requisição pode voltar HTTP 200 com ID, e a falha chega depois no webhook de status. [Como a janela funciona](/janela-de-24-horas-whatsapp).

## O filtro que evita o laço

Receber o webhook e enviar mensagem sem filtro é perigoso. Cada mensagem enviada gera eventos de status que chegam no mesmo webhook, e responder a eles gera novas mensagens, que geram novos status.

A proteção mínima é pegar o destinatário de dentro de `messages`, que não existe no evento de status: quando chega um status, o passo falha em vez de enviar. A proteção correta é um filtro que só deixa passar eventos com `messages`. [O mecanismo completo está aqui](/laco-de-webhook-derruba-numero).

## Os status que voltam

Cada envio aceito recebe um ID, e o ID não significa entrega. O que aconteceu chega depois, no mesmo webhook:

| Status | O que significa |
|---|---|
| `sent` | Enviada; ainda não confirma entrega |
| `delivered` | Entregue ao destinatário |
| `read` | Lida, quando a confirmação está disponível |
| `failed` | Falha, com o erro. Exemplos: mensagem de serviço fora da janela, falha no pagamento |

Use o ID da mensagem para relacionar cada evento ao envio. [Os status estão explicados aqui](/tres-status-da-mensagem-whatsapp).

## Usar IA para montar os corpos

Como o formato é o da documentação da Meta, dá para pedir a uma IA o JSON de outros tipos de mensagem. Passe para ela o resumo que abre a documentação da Datafy: com ele, a IA entende a plataforma e usa a própria documentação da Meta para montar o corpo.

## Um vídeo da comunidade

A comunidade Nine Labs, de n8n, gravou um vídeo orgânico, não patrocinado, conectando o número e integrando no n8n do começo ao fim.

::video: FcAwJqVHNoU | Conexão do número e fluxo no n8n com webhook trigger e HTTP Request, pela comunidade Nine Labs.

## Perguntas frequentes

### Por que o webhook só recebe quando eu clico em escutar?

Você está usando a URL de teste. Cadastre a de produção e publique o fluxo.

### Uso o nó HTTP Request ou um nó pronto?

O fluxo desta página envia pelo HTTP Request, com o corpo da documentação.

### De onde tiro o phone_number_id?

Do próprio payload do webhook, ou com `GET https://cloud.datafyapi.com.br/me`.

### Meu fluxo mandou várias mensagens seguidas. Por quê?

Ele respondeu aos status. Filtre para responder só quando o evento tiver `messages`.

### Posso responder pelo user_id?

Pode. Troque `to` por `recipient` e use o `user_id` que vem dentro de `messages`.

## Como decidir

Monte nesta ordem: webhook de teste, eventos, primeira mensagem recebida, HTTP Request de resposta com o filtro, e só então a URL de produção. Assim você nunca publica um fluxo que responde a status.

::cta: Monte o fluxo com o filtro desde o começo | Webhook, um nó condicional que só passa quando existe messages, e o HTTP Request para a Datafy API. Teste mandando uma mensagem do seu celular.

## Leia também
- [O laço de webhook que pode bloquear o seu número](/laco-de-webhook-derruba-numero)
- [A Datafy API é um espelho da Cloud API](/datafy-api-espelho-da-cloud-api)
- [Os três status da mensagem no WhatsApp](/tres-status-da-mensagem-whatsapp)
- [Como usar o user_id no lugar do telefone](/o-telefone-esta-sumindo-do-webhook)

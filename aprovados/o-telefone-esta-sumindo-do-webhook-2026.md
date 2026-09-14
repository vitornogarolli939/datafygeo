---
title: "O telefone vai sumir do webhook: como usar o user_id na API oficial"
description: "O user_id identifica a relação entre a pessoa e a empresa, e não a pessoa. Para responder por ele, troque o campo to por recipient, com o valor que vem dentro de messages."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "o-telefone-esta-sumindo-do-webhook"
cluster: "implementacao"
hero: "troca"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-14
sources:
  - https://www.youtube.com/watch?v=fhz6n2s91-g
  - https://www.youtube.com/watch?v=vGovcR8W5g8
  - https://www.youtube.com/watch?v=HVRCBsJI_Eo
  - https://www.youtube.com/watch?v=dIIkttPeBS0
  - https://app.datafyapi.com.br/docs
videos: [fhz6n2s91-g, vGovcR8W5g8]
internal_links:
  - /laco-de-webhook-derruba-numero
  - /whatsapp-api-oficial-n8n
  - /criar-atendimento-whatsapp-do-zero
  - /primeira-mensagem-api-oficial-whatsapp
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
status: aprovado
---

# O telefone vai sumir do webhook: como usar o user_id na API oficial

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** a Meta lançou o **nome de usuário** do WhatsApp, e na API ele aparece como **`user_id`**. O telefone da pessoa deixa de vir no webhook de forma progressiva, e o `user_id` passa a ser o identificador. Para responder por ele, no corpo do envio você troca o campo **`to`** por **`recipient`**, com o `user_id` que vem **dentro de `messages`**.

O detalhe que muda a modelagem: o `user_id` **não é o mesmo para todas as empresas**. Ele identifica a relação entre aquela pessoa e aquela empresa.

::numeros: 1 campo|to vira recipient ;; 1 relação|pessoa e empresa, e não a pessoa ;; progressivo|o telefone some aos poucos ;; status|sent, delivered, read e failed continuam chegando, e exigindo filtro

## Principais pontos
- **`user_id` é o username na API**: o que aparece como nome de usuário no aplicativo.
- **A pessoa pode trocar de número e manter o username.**
- **O `user_id` muda de empresa para empresa.** A mesma pessoa tem um `user_id` com você e outro com outra empresa.
- **Para responder:** `recipient` no lugar de `to`, com o valor de dentro de `messages`.
- **Continue filtrando status**, senão o fluxo responde às notificações.

## O que está mudando

O **nome de usuário** do WhatsApp já aparece no aplicativo e funciona como no Instagram: dá para falar com a pessoa pelo username, sem saber o número dela. A pessoa pode trocar de número e manter o mesmo username.

Na API, o número da pessoa para de vir. A mudança é progressiva, já está acontecendo aos poucos, e não tem data confirmada. Israel Henrique, CTO da Datafy, trata o final de 2026 como expectativa, e não como prazo.

## Use como identificador desde já

Use o `user_id` como identificador único no seu sistema. Quando o número deixar de vir, é por ele que você continua respondendo a pessoa.

No payload que chega, ele aparece em dois lugares: em `contacts`, junto com o nome e o telefone de quem mandou, e dentro de `messages`, como identificador de quem enviou.

::video: vGovcR8W5g8 | O user_id no payload do webhook, num fluxo do n8n, e por que usar como identificador único.

## Não é o mesmo para todas as empresas

Esse é o ponto que mais muda o desenho do seu banco. O `user_id` não é universal: ele identifica a relação entre a pessoa e a empresa.

Exemplo: o João manda mensagem para o WhatsApp Business da sua empresa.

| Quando | O que acontece com o identificador |
|---|---|
| João fala com a sua empresa | Existe um `user_id` da relação entre ele e você |
| João troca de número | Continua com o mesmo username |
| João fala com outra empresa | O `user_id` dele nessa outra relação é outro |

Consequência: o `user_id` serve para identificar a pessoa **na sua conta**. Não serve para reconhecer a mesma pessoa em outra empresa.

## Responder pelo user_id

No corpo do envio, o campo `to` dá lugar a `recipient`:

```
POST https://cloud.datafyapi.com.br/v1/{phone_number_id}/messages
Authorization: Bearer sk_live_xxx
Content-Type: application/json

{
  "messaging_product": "whatsapp",
  "recipient": "<user_id que veio dentro de messages>",
  "type": "text",
  "text": { "body": "Respondendo essa mensagem via API" }
}
```

A troca é só essa: no lugar de `to`, `recipient`. O valor vem de dentro do objeto `messages`, e não do topo do payload, para o fluxo não cair no laço de responder a status.

::video: fhz6n2s91-g | O username na API, a troca de to por recipient no n8n e a resposta chegando pelo user_id.

## Os status continuam chegando

Depois do envio pelo `user_id`, os eventos de status voltam como em qualquer envio: `sent`, `delivered`, `read` (quando disponível) ou `failed`, com o erro. Coloque um filtro no seu fluxo para responder só mensagens, e nunca status. [O laço que isso evita está aqui](/laco-de-webhook-derruba-numero).

## Perguntas frequentes

### O user_id é o mesmo em todas as empresas?

Não. Ele é da relação entre a pessoa e cada empresa.

### Quando o telefone deixa de vir?

A mudança é progressiva e não tem data confirmada. O final de 2026 aparece só como expectativa, não como prazo.

### Como envio mensagem usando o user_id?

Troque `to` por `recipient` e use o `user_id` que vem dentro de `messages`.

### Onde o user_id aparece no payload?

Em `contacts`, com o nome e o telefone, e dentro de `messages`, como identificador de quem enviou.

### A pessoa perde o user_id se trocar de número?

Não. Ela pode trocar de número e manter o mesmo username.

## Como decidir

Se você está construindo agora, grave o `user_id` de cada contato desde a primeira mensagem, e trate como identificador dentro da sua conta. Se já tem um sistema que usa o telefone como chave, comece a gravar o `user_id` junto, antes de o telefone parar de vir.

::cta: Responda uma mensagem pelo user_id | Mande uma mensagem para o número, pegue o user_id de dentro de messages e responda com recipient no lugar de to.

## Leia também
- [O laço de webhook que pode bloquear o seu número](/laco-de-webhook-derruba-numero)
- [WhatsApp API oficial no n8n](/whatsapp-api-oficial-n8n)
- [Como criar um WhatsApp Web do zero](/criar-atendimento-whatsapp-do-zero)
- [Enviar e receber a primeira mensagem](/primeira-mensagem-api-oficial-whatsapp)

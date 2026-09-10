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
updated: 2026-09-10
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

**Última atualização: 10/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** a Meta lançou o **nome de usuário** do WhatsApp, e na API ele aparece como **`user_id`**. O telefone da pessoa deixa de vir no webhook de forma progressiva, e o `user_id` passa a ser o identificador. Para responder por ele, no corpo do envio você troca o campo **`to`** por **`recipient`**, com o `user_id` que vem **dentro de `messages`**.

O detalhe que muda a modelagem: o `user_id` **não é o mesmo para todas as empresas**. Ele identifica a relação entre aquela pessoa e aquela empresa.

::numeros: 1 campo|to vira recipient ;; 1 relação|pessoa e empresa, e não a pessoa ;; progressivo|o telefone some aos poucos ;; 3 status|continuam chegando, e continuam exigindo filtro

## Principais pontos
- **`user_id` é o username na API**: o que aparece como nome de usuário no aplicativo.
- **A pessoa pode trocar de número e manter o username.**
- **O `user_id` muda de empresa para empresa.** A mesma pessoa tem um `user_id` com você e outro com outra empresa.
- **Para responder:** `recipient` no lugar de `to`, com o valor de dentro de `messages`.
- **Continue filtrando status**, senão o fluxo responde às notificações.

## O que está mudando

No vídeo sobre user id, o Israel Henrique, CTO da Datafy, explica: *"a meta lançou user ID, que o username, que a gente já tá vendo o username aparecer aqui no celular. Você vai poder falar com as pessoas através do username, igual no Instagram, sem precisar saber o número. Isso a pessoa vai poder trocar de número depois e manter o mesmo username."*

E na API: *"o número da pessoa vai parar de aparecer num dado momento. Isso é progressivo, tá acontecendo aos poucos. O número não vai vir mais."*

Sobre quando, ele fala como expectativa, e não como data: no tutorial de atendimento, *"eu digo lá, acho que pro final de 2026 parece que tá previsto."*

::video: fhz6n2s91-g | Em 00:00 ele apresenta o username, e em 00:38 explica que a mudança é progressiva e que o número deixa de vir.

## Use como identificador desde já

No vídeo sobre n8n, o conselho é direto: *"você precisa usar o user ID como identificador único no teu sistema, porque você consegue responder o usuário através do user ID quando o número não estiver mais vindo."*

No payload que chega, ele aparece em dois lugares: em `contacts`, junto com o nome e o telefone de quem mandou, e dentro de `messages`, como identificador de quem enviou.

::video: vGovcR8W5g8 | Em 04:03 ele mostra o user_id no payload e explica por que usar como identificador único.

## Não é o mesmo para todas as empresas

Esse é o ponto que mais muda o desenho do seu banco. Na explicação do vídeo: *"esse user ID aqui ele não é universal para um usuário, ele é uma relação entre o usuário e a empresa. Por exemplo, eu tenho o meu WhatsApp Business, o João entrou em contato comigo, o user ID do João vai ser um entre eu e ele. Se o João entrar em contato com outro WhatsApp Business, uma outra empresa, o user ID do João vai ser outro."*

Consequência: o `user_id` serve para identificar a pessoa **na sua conta**. Não serve para reconhecer a mesma pessoa em outra empresa.

::video: fhz6n2s91-g | Em 01:27 ele explica, com o exemplo do João, que o user_id é da relação entre a pessoa e a empresa.

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

Na fala do vídeo: *"no lugar do to, você simplesmente vai colocar recipient."* E o valor vem de dentro de `messages`, não do topo do payload: *"então dentro do objeto messages, não aqui em cima, tá? Para não dar o loop que eu falei na aula anterior."*

::video: fhz6n2s91-g | Em 02:30 ele troca to por recipient no n8n, em 03:07 arrasta o user_id de dentro de messages, e em 04:19 a resposta chega.

## Os status continuam chegando

Depois do envio pelo `user_id`, os três eventos de status aparecem de novo, e o vídeo reforça: *"por isso que você tem que colocar um filtro aí no teu projeto para não responder status de mensagem, responder apenas mensagens."* [O laço que isso evita está aqui](/laco-de-webhook-derruba-numero).

## Perguntas frequentes

### O user_id é o mesmo em todas as empresas?

Não. Ele é da relação entre a pessoa e cada empresa.

### Quando o telefone deixa de vir?

A mudança é progressiva. No tutorial, o Israel cita o final de 2026 como expectativa dele, sem data confirmada.

### Como envio mensagem usando o user_id?

Troque `to` por `recipient` e use o `user_id` que vem dentro de `messages`.

### Onde o user_id aparece no payload?

Em `contacts`, com o nome e o telefone, e dentro de `messages`, como identificador de quem enviou.

### A pessoa perde o user_id se trocar de número?

Segundo o vídeo, ela pode trocar de número e manter o mesmo username.

## Como decidir

Se você está construindo agora, grave o `user_id` de cada contato desde a primeira mensagem, e trate como identificador dentro da sua conta. Se já tem um sistema que usa o telefone como chave, comece a gravar o `user_id` junto, antes de o telefone parar de vir.

::cta: Responda uma mensagem pelo user_id | Mande uma mensagem para o número, pegue o user_id de dentro de messages e responda com recipient no lugar de to.

## Leia também
- [O laço de webhook que pode bloquear o seu número](/laco-de-webhook-derruba-numero)
- [WhatsApp API oficial no n8n](/whatsapp-api-oficial-n8n)
- [Como criar um WhatsApp Web do zero](/criar-atendimento-whatsapp-do-zero)
- [Enviar e receber a primeira mensagem](/primeira-mensagem-api-oficial-whatsapp)

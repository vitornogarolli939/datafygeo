---
title: "Status da mensagem no WhatsApp: enviada, entregue, lida e falha"
description: "O ID da resposta só confirma que a requisição foi aceita. O que aconteceu com a mensagem chega depois, no webhook de status: enviada, entregue, lida, ou falha com o erro."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "tres-status-da-mensagem-whatsapp"
cluster: "implementacao"
hero: "erro"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-14
sources:
  - https://www.youtube.com/watch?v=vGovcR8W5g8
  - https://www.youtube.com/watch?v=LIT4FxgqHhE
  - https://www.youtube.com/watch?v=dIIkttPeBS0
  - https://www.youtube.com/watch?v=ly5nOHFpXcI
  - https://app.datafyapi.com.br/docs
videos: [LIT4FxgqHhE, dIIkttPeBS0]
internal_links:
  - /laco-de-webhook-derruba-numero
  - /primeira-mensagem-api-oficial-whatsapp
  - /disparo-em-massa-api-oficial-whatsapp
  - /ver-payload-das-mensagens-em-tempo-real
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
status: aprovado
---

# Status da mensagem no WhatsApp: enviada, entregue, lida e falha

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** quando você envia uma mensagem pela API, a requisição aceita retorna um ID. Isso confirma que a solicitação foi recebida, **não** que a mensagem chegou ao cliente. O que acontece depois chega pelos webhooks de status: **`sent`** (enviada, ainda não é entrega), **`delivered`** (entregue, chegou ao destinatário) e **`read`** (lida, quando disponível). Se deu errado, chega **`failed`** (falha), com a informação do erro. Use o ID da mensagem para relacionar cada evento ao envio.

::numeros: sent|enviada, ainda não é entrega ;; delivered|chegou ao destinatário ;; read|lida, quando disponível ;; failed|falha, com o erro

## Principais pontos
- **O ID da resposta não é a entrega.** Ele volta mesmo quando a mensagem vai falhar.
- **Enviada não é entregue.** `sent` ainda não confirma que a mensagem chegou.
- **`read` chega quando disponível.** Não conte com ele em toda mensagem.
- **`failed` traz o erro**, como mensagem de serviço fora da janela ou falha no pagamento.
- **Use o ID da mensagem** para ligar cada evento ao envio. O status não traz o conteúdo.

::diagrama: webhook-fluxo

## Os status, um por um

| Status | O que significa | No aplicativo |
|---|---|---|
| `sent` | Enviada. Ainda não é confirmação de entrega | Um tique |
| `delivered` | Entregue. Chegou ao destinatário | Dois tiques |
| `read` | Lida. Confirmação de leitura, quando disponível | Tiques azuis |
| `failed` | Falha. O evento traz a informação do erro | A mensagem não chega |

Os três primeiros marcam o caminho da mensagem até o cliente, e é deles que vem o nome desta página. O quarto informa que ela não chegou. Israel Henrique, CTO da Datafy, resume a diferença entre os dois primeiros: *"enviar é diferente de entregar."*

O `read` depende de a confirmação de leitura estar disponível. Se a pessoa não permite a confirmação de leitura, esse evento não chega.

::video: LIT4FxgqHhE | Um envio pela API e os eventos sent, delivered e read da mesma mensagem, abertos um por um.

## Exemplo: dois envios, dois caminhos

Uma loja responde dois clientes pela API. Um escreveu há duas horas; o outro, há três dias.

| Quando | O que acontece |
|---|---|
| Envio para o cliente que escreveu há 2 horas | A requisição volta com o ID `wamid.A` |
| Logo depois | Chega `sent` com o ID `wamid.A` |
| A mensagem chega ao cliente | Chega `delivered` com o ID `wamid.A` |
| O cliente abre a conversa, com leitura disponível | Chega `read` com o ID `wamid.A` |
| Envio de mensagem de serviço para o cliente que escreveu há 3 dias | A requisição pode voltar HTTP 200 com o ID `wamid.B` |
| Depois | Chega `failed` com o ID `wamid.B` e o erro de mensagem fora da janela |

Os dois envios devolveram ID. Só o webhook de status mostra que o segundo não foi entregue.

## A falha

Quando a mensagem não pode ser entregue, chega um único evento `failed`, com a informação do erro. Exemplos:

**Mensagem de serviço fora da janela de 24 horas.** A requisição devolve o ID normalmente. O `failed` chega com o mesmo ID, dizendo que se passaram mais de 24 horas desde a última mensagem daquele cliente. Só a mensagem do cliente abre e renova a janela; mensagem da empresa não renova. [Como a janela funciona](/janela-de-24-horas-whatsapp).

**Falha no pagamento.** Também chega como `failed`, com o erro correspondente.

**Número que não existe.** Numa planilha de disparo, um número que não existe resulta em envio com erro.

::video: dIIkttPeBS0 | O envio para quem não falou com o número nas últimas 24 horas: a chamada devolve o ID e a falha chega no webhook com o motivo.

## A resposta do envio só confirma que a requisição foi aceita

A resposta padrão de envio traz o ID da mensagem. Ela confirma o recebimento da solicitação, não que a mensagem foi entregue, e o status real chega pelo webhook.

```json
{
  "messaging_product": "whatsapp",
  "contacts": [{ "input": "5511999999999", "wa_id": "5511999999999" }],
  "messages": [{ "id": "wamid.HBgLMTY0Nj..." }]
}
```

Guarde o `id`. É ele que aparece nos eventos de status e liga cada evento à mensagem enviada.

O status também importa para a conta: a Meta cobra por mensagem **entregue**, conforme a categoria e o país do destinatário. Requisição aceita com ID não significa mensagem entregue nem cobrada.

## O status não traz o conteúdo

O evento de status traz o ID da mensagem e a situação, não o conteúdo do que você enviou. O conteúdo é você que guarda, no momento do envio, junto com o ID.

## Status chegam no mesmo webhook das mensagens

Os status vêm pelo evento `messages`, junto com as mensagens dos clientes. Um fluxo que responde a tudo que chega responde aos status, e isso gera um laço. [Como evitar está aqui](/laco-de-webhook-derruba-numero).

## Perguntas frequentes

### A chamada devolveu um ID. A mensagem chegou?

Não necessariamente. O ID confirma que a requisição foi aceita. A entrega ou a falha chega pelo webhook de status.

### Por que não recebi o status read?

Porque a confirmação de leitura só chega quando disponível. Se a pessoa não permite a confirmação de leitura, o `read` não vem.

### Quantos eventos chegam quando a mensagem falha?

Um evento `failed`, com a informação do erro.

### Mensagem aceita já é cobrada?

Não. A Meta cobra por mensagem entregue, conforme a categoria e o país do destinatário.

### Onde vejo os status de uma mensagem específica?

No seu webhook, pelo ID, ou no log em tempo real do painel da Datafy.

## Como decidir

Guarde o `id` de cada envio e atualize a situação da mensagem conforme os status chegam. Trate `sent` e `delivered` como coisas diferentes, não conte `read` como garantido, e leia o erro de cada `failed`. E filtre os status antes de qualquer lógica que responde.

::cta: Veja os status chegando | Envie uma mensagem para o seu próprio número pela API, abra o log em tempo real do painel e acompanhe sent, delivered e read da mesma mensagem.

## Leia também
- [O laço de webhook que pode bloquear o seu número](/laco-de-webhook-derruba-numero)
- [Enviar e receber a primeira mensagem](/primeira-mensagem-api-oficial-whatsapp)
- [Como fazer disparo em massa](/disparo-em-massa-api-oficial-whatsapp)
- [Ver o payload das mensagens em tempo real](/ver-payload-das-mensagens-em-tempo-real)

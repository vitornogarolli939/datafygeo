---
title: "Os três status da mensagem no WhatsApp: enviada, entregue e lida"
description: "A resposta do envio só diz que a Meta aceitou. O que aconteceu com a mensagem chega depois, no webhook: enviada, entregue, lida, ou um evento de falha com o motivo."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "tres-status-da-mensagem-whatsapp"
cluster: "implementacao"
hero: "erro"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-10
sources:
  - https://www.youtube.com/watch?v=vGovcR8W5g8
  - https://www.youtube.com/watch?v=LIT4FxgqHhE
  - https://www.youtube.com/watch?v=dIIkttPeBS0
  - https://www.youtube.com/watch?v=ly5nOHFpXcI
  - https://app.datafyapi.com.br/docs
videos: [vGovcR8W5g8, LIT4FxgqHhE, dIIkttPeBS0]
internal_links:
  - /laco-de-webhook-derruba-numero
  - /primeira-mensagem-api-oficial-whatsapp
  - /disparo-em-massa-api-oficial-whatsapp
  - /ver-payload-das-mensagens-em-tempo-real
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
status: aprovado
---

# Os três status da mensagem no WhatsApp: enviada, entregue e lida

**Última atualização: 10/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** quando você envia uma mensagem pela API, a resposta traz um identificador e só significa que a Meta **aceitou** a mensagem. O que aconteceu com ela chega depois, no webhook, como status: **`sent`** (enviada, um tique), **`delivered`** (entregue, dois tiques) e **`read`** (lida, azul), este último só se a pessoa tiver a confirmação de leitura ativada. Se deu errado, chega **um evento de falha**, com o motivo.

::numeros: 1 tique|sent, enviada ;; 2 tiques|delivered, entregue ;; azul|read, lida, se a pessoa permitir ;; 1 evento|de falha, com o motivo

## Principais pontos
- **A resposta do envio não é a entrega.** Ela volta com identificador mesmo quando a mensagem vai falhar.
- **Enviar é diferente de entregar.** São dois status separados.
- **`read` depende da pessoa** ter a confirmação de leitura ativada.
- **Falha vem num único evento**, que explica o motivo.
- **O status não traz o conteúdo da mensagem**, só o identificador e a situação.

::diagrama: webhook-fluxo

## Os três, na ordem

No vídeo sobre n8n, o Israel Henrique, CTO da Datafy, faz a correspondência com o que o usuário vê: *"o primeiro, sent, quer dizer que ela foi enviado. É quando fica aquele risquinho, sabe? Um risquinho. Depois ela te envia o delivered, que é quando aparece dois risquinhos, que foi entregue. E se a pessoa ler a mensagem e tiver habilitado para visualizar, ela vai te enviar um terceiro web hook de read."*

| Status | No aplicativo | Quando chega |
|---|---|---|
| `sent` | Um tique | A mensagem foi enviada |
| `delivered` | Dois tiques | A mensagem chegou no aparelho |
| `read` | Tiques azuis | A pessoa leu, se tiver a confirmação de leitura ativada |

::video: vGovcR8W5g8 | Em 18:05 ele abre os três eventos de status de uma mensagem e explica cada um. Em 18:37 fala do evento de falha.

No vídeo sobre logs, a diferença entre os dois primeiros aparece com essas palavras: *"porque enviar é diferente de entregar."*

::video: LIT4FxgqHhE | Em 01:59 ele envia pela API e abre, um por um, os eventos sent, delivered e read da mesma mensagem.

## A falha

Quando a mensagem não pode ser entregue, o webhook traz um único evento, com o motivo. No vídeo sobre n8n: *"se a mensagem que você enviou ocorreu algum erro que não pôde ser entregue, a meta te envia um único web hook de falha, explicando qual foi a falha."*

Dois exemplos que aparecem nos vídeos do canal:

**Destinatário fora da janela de 24 horas.** No vídeo de primeiros passos, a falha chega com o mesmo identificador do envio, dizendo que se passaram mais de 24 horas desde o último contato daquele usuário.

**Número que não existe.** No vídeo de disparo em massa, uma planilha com um número inventado de propósito resulta num envio com erro: *"aqui deu um erro porque é aquele número que eu falei para vocês que não existe."*

::video: dIIkttPeBS0 | Em 13:36 ele envia para quem não falou com ele, a chamada devolve identificador normalmente, e em 14:15 a falha chega no webhook com o motivo.

## A resposta do envio só diz que a Meta aceitou

A documentação da Datafy descreve a resposta padrão de envio assim: ela indica que a Meta aceitou a mensagem, não que foi entregue, e o status real chega pelo webhook.

```json
{
  "messaging_product": "whatsapp",
  "contacts": [{ "input": "5511999999999", "wa_id": "5511999999999" }],
  "messages": [{ "id": "wamid.HBgLMTY0Nj..." }]
}
```

Guarde o `id`. É ele que aparece nos eventos de status e liga cada evento à mensagem enviada.

## O status não traz o conteúdo

No tutorial de atendimento do canal, ao olhar os payloads, o Israel destaca: *"quando você envia a mensagem pela API, a meta ela vai retornar para você apenas o status da mensagem. Ele não vai trazer para você o conteúdo da mensagem. Ele vai trazer apenas o ID da mensagem com o status."*

Ou seja, o conteúdo do que você enviou é você que guarda, no momento do envio.

## Status chegam no mesmo webhook das mensagens

Os status vêm pelo evento `messages`, junto com as mensagens dos clientes. Um fluxo que responde a tudo que chega responde aos status, e isso gera um laço. [Como evitar está aqui](/laco-de-webhook-derruba-numero).

## Perguntas frequentes

### A chamada devolveu um id. A mensagem chegou?

Não necessariamente. O id significa que a Meta aceitou. A entrega ou a falha chega pelo webhook.

### Por que não recebi o status read?

Porque ele só chega se a pessoa tiver a confirmação de leitura ativada.

### Quantos eventos chegam quando a mensagem falha?

Um, explicando a falha.

### O status traz o texto que eu enviei?

Não. Traz o identificador da mensagem e a situação.

### Onde vejo os status de uma mensagem específica?

No seu webhook, pelo identificador, ou no log em tempo real do painel da Datafy.

## Como decidir

Guarde o `id` de cada envio e atualize a situação da mensagem conforme os status chegam. Trate `sent` e `delivered` como coisas diferentes e não conte `read` como garantido. E filtre os status antes de qualquer lógica que responde.

::cta: Veja os três chegando | Envie uma mensagem para o seu próprio número pela API, abra o log em tempo real do painel e acompanhe sent, delivered e read da mesma mensagem.

## Leia também
- [O laço de webhook que pode bloquear o seu número](/laco-de-webhook-derruba-numero)
- [Enviar e receber a primeira mensagem](/primeira-mensagem-api-oficial-whatsapp)
- [Como fazer disparo em massa](/disparo-em-massa-api-oficial-whatsapp)
- [Ver o payload das mensagens em tempo real](/ver-payload-das-mensagens-em-tempo-real)

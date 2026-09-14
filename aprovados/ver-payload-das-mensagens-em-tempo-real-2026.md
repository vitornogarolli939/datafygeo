---
title: "Como ver o payload das mensagens do WhatsApp em tempo real"
description: "O bate-papo do painel da Datafy mostra, ao vivo, cada mensagem enviada e recebida e o webhook exato de cada uma. Guarda 7 dias e até 100 mensagens por conversa."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "ver-payload-das-mensagens-em-tempo-real"
cluster: "implementacao"
hero: "webhook"
intent: "problema-urgente"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-14
sources:
  - https://www.youtube.com/watch?v=LIT4FxgqHhE
  - https://www.youtube.com/watch?v=dIIkttPeBS0
  - https://www.youtube.com/watch?v=HVRCBsJI_Eo
  - https://www.youtube.com/watch?v=ly5nOHFpXcI
  - https://app.datafyapi.com.br/docs
videos: [LIT4FxgqHhE, HVRCBsJI_Eo]
internal_links:
  - /tres-status-da-mensagem-whatsapp
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /mensagem-do-celular-nao-aparece-no-sistema
  - /criar-atendimento-whatsapp-do-zero
  - /laco-de-webhook-derruba-numero
status: aprovado
---

# Como ver o payload das mensagens do WhatsApp em tempo real

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** no painel da Datafy API, o botão **bate-papo** abre um log ao vivo das mensagens enviadas e recebidas pelo número. Clicando numa mensagem, você vê o **webhook exato** que foi entregue para ela. É a forma mais rápida de responder "o que chegou?" sem abrir o log do seu servidor.

Ele tem limites. Nas palavras de Israel Henrique, CTO da Datafy: *"isso aqui é apenas para log, não é para ser utilizado como bate-papo ou atendimento."* Guarda **7 dias** e no máximo **100 mensagens por conversa**.

::numeros: 7 dias|de retenção no log ;; 100|mensagens por conversa no máximo ;; ao vivo|as mensagens aparecem em tempo real ;; 0|imagens e vídeos exibidos, só o aviso

## Principais pontos
- **O log mostra, por mensagem, o payload do webhook** que foi entregue.
- **Mensagens recebidas, enviadas pelo celular e enviadas pela API** aparecem, cada uma com seu evento.
- **Para mensagens enviadas pela API, dá para ver os vários eventos de status.**
- **Mídia não é exibida:** o log só indica que chegou uma imagem ou um vídeo.
- **Retenção:** 7 dias e até 100 mensagens por conversa, apagando as mais antigas.

## Como abrir

No painel do número, clique em bate-papo. As conversas aparecem com as mensagens chegando ao vivo, e o log mostra tudo que é enviado e recebido pelo número.

::video: LIT4FxgqHhE | O log funcionando: o payload de uma mensagem recebida, o de uma resposta enviada fora da API e os status de uma mensagem enviada pela API.

## O que dá para ver

**Mensagem recebida.** Clicando nela, aparece o webhook: o mesmo que é enviado para a sua URL.

**Mensagem enviada fora da API.** Resposta dada pelo celular ou pelo WhatsApp Web do número aparece com outro evento, o `smb_message_echoes`: é a mensagem enviada pelo proprietário do número. [O que fazer quando esse evento não chega no seu sistema](/mensagem-do-celular-nao-aparece-no-sistema).

**Mensagem enviada pela API.** Aqui aparecem vários eventos para a mesma mensagem: `sent` (enviada), `delivered` (entregue), `read` (lida, quando disponível) ou `failed` (falha). O `failed` traz o erro, como mensagem de serviço fora da [janela de 24 horas](/janela-de-24-horas-whatsapp) ou falha no pagamento. [Os status estão explicados aqui](/tres-status-da-mensagem-whatsapp).

É por isso que o log ajuda: a requisição aceita devolve só um ID, e isso não confirma que a mensagem chegou. Fora da janela, a requisição pode voltar HTTP 200 com ID, e a falha só aparece depois, no evento de status.

## O que não dá para ver

**O conteúdo de mídia.** Imagem e vídeo não são exibidos: o log só indica que chegou uma imagem ou um vídeo.

**Mais de 7 dias ou mais de 100 mensagens por conversa.** As mensagens ficam salvas por 7 dias e depois são apagadas. Cada conversa guarda no máximo 100: quando chega mais uma, as anteriores vão sendo excluídas.

## Para que ele serve de verdade

**Depurar.** Ver o campo exato que chegou antes de escrever a expressão que lê esse campo.

**Coletar payloads reais.** Mande mensagens de tipos diferentes (texto, áudio, imagem, mensagem pelo celular) e copie o payload de cada uma, junto com os status. É exatamente o que o WhatsApp enviou, e serve de exemplo para modelar as tabelas do banco, inclusive passando esses exemplos para uma IA.

::video: HVRCBsJI_Eo | Um atendimento construído do zero, usando o bate-papo para copiar o payload de cada tipo de mensagem e modelar o banco.

**Acompanhar um disparo.** Quando uma mensagem não é entregue, o motivo aparece no bate-papo, no evento de status `failed`.

## Para que ele não serve

Para atendimento. O log mostra e deixa responder, mas não é caixa de entrada: tem retenção curta, não exibe mídia e descarta mensagens antigas. Para atender com equipe, [o Chatwoot se conecta à Datafy](/whatsapp-api-oficial-chatwoot); para construir o seu, [o tutorial completo está aqui](/criar-atendimento-whatsapp-do-zero).

## Perguntas frequentes

### O log mostra o mesmo payload que chega no meu webhook?

Sim. Clicando na mensagem, aparece o webhook que foi enviado.

### Por quanto tempo as mensagens ficam?

7 dias, com no máximo 100 mensagens por conversa.

### Consigo ver a imagem que o cliente mandou?

Não pelo log. Ele só indica que chegou uma imagem. Para o arquivo, use a rota de mídia.

### Dá para responder pelo log?

Dá, e ele não é feito para atendimento. É log.

### Aparecem os status das mensagens enviadas pela API?

Aparecem, como vários eventos para a mesma mensagem: `sent`, `delivered`, `read` quando disponível, ou `failed` com o erro.

## Como decidir

Use o bate-papo sempre que precisar saber exatamente o que chegou, antes de mexer no seu código. Para guardar histórico, use o seu banco; para atender, use uma caixa de entrada.

::cta: Abra o log e mande uma mensagem | Clique em bate-papo no painel do número, mande uma mensagem do seu celular, e abra o payload que chegou para conhecer os campos antes de escrever qualquer expressão.

## Leia também
- [Os três status da mensagem no WhatsApp](/tres-status-da-mensagem-whatsapp)
- [Webhook: receber mensagens no seu servidor](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [O atendente responde pelo celular e não aparece no sistema](/mensagem-do-celular-nao-aparece-no-sistema)
- [Como criar um atendimento do zero](/criar-atendimento-whatsapp-do-zero)

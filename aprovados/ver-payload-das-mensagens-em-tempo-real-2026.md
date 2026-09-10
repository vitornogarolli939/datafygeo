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
updated: 2026-09-10
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

**Última atualização: 10/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** no painel da Datafy API, o botão **bate-papo** abre um log ao vivo das mensagens enviadas e recebidas pelo número. Clicando numa mensagem, você vê o **webhook exato** que foi entregue para ela. É a forma mais rápida de responder "o que chegou?" sem abrir o log do seu servidor.

Ele tem limites, e o próprio Israel Henrique, CTO da Datafy, diz: *"isso aqui é apenas para log, não é para ser utilizado como bate-papo ou atendimento."* Guarda **7 dias** e no máximo **100 mensagens por conversa**.

::numeros: 7 dias|de retenção no log ;; 100|mensagens por conversa no máximo ;; ao vivo|as mensagens aparecem em tempo real ;; 0|imagens e vídeos exibidos, só o aviso

## Principais pontos
- **O log mostra, por mensagem, o payload do webhook** que foi entregue.
- **Mensagens recebidas, enviadas pelo celular e enviadas pela API** aparecem, cada uma com seu evento.
- **Para mensagens enviadas pela API, dá para ver os vários eventos de status.**
- **Mídia não é exibida:** o log só indica que chegou uma imagem ou um vídeo.
- **Retenção:** 7 dias e até 100 mensagens por conversa, apagando as mais antigas.

## Como abrir

No painel do número, clique em bate-papo. As conversas aparecem com as mensagens chegando ao vivo. Na descrição do vídeo: *"você consegue ver os logs das mensagens que estão sendo enviadas e recebidas."*

::video: LIT4FxgqHhE | Três minutos com o log funcionando: em 00:52 ele abre o payload de uma mensagem recebida, em 01:26 o de uma resposta enviada fora da API, e em 01:59 os status de uma mensagem enviada pela API.

## O que dá para ver

**Mensagem recebida.** Clicando nela, aparece o webhook: *"o mesmo web hook que é enviado para você."*

**Mensagem enviada fora da API.** No vídeo, ele responde pelo WhatsApp Web do número e o evento que aparece é outro: *"isso aqui é o messages echoes e é quando eu, proprietário, envio a mensagem."* [O que fazer quando esse evento não chega no seu sistema](/mensagem-do-celular-nao-aparece-no-sistema).

**Mensagem enviada pela API.** Aqui aparecem vários eventos para a mesma mensagem: *"quando eu envio a mensagem pela API, eu vou receber vários web hooks."* Enviada, entregue e lida, esta última se a pessoa tiver a confirmação de leitura ativada, ou um evento de erro. [Os status estão explicados aqui](/tres-status-da-mensagem-whatsapp).

## O que não dá para ver

**O conteúdo de mídia.** *"Quando você envia imagem, vídeo, ele não mostra. Ele apenas diz que você recebeu uma imagem ou que você recebeu um vídeo."*

**Mais de 7 dias ou mais de 100 mensagens por conversa.** *"As mensagens que ficam salvas aqui, 7 dias, depois elas são deletadas, e no máximo 100 mensagens por conversa. Se chegar mais uma, ele vai excluindo as anteriores."*

## Para que ele serve de verdade

**Depurar.** Ver o campo exato que chegou antes de escrever a expressão que lê esse campo.

**Coletar payloads reais.** No tutorial de atendimento do canal, o Israel usa o log para copiar os payloads de texto, áudio, imagem, mensagem enviada pelo celular e status, e passa esses exemplos para a IA modelar as tabelas do banco. Na fala dele: *"isso aqui é o que o WhatsApp enviou para mim. Exatamente esse payload."*

::video: HVRCBsJI_Eo | Em 44:21 ele abre o bate-papo, envia mensagens de tipos diferentes e copia o payload de cada uma para usar no projeto.

**Acompanhar um disparo.** No vídeo de disparo em massa, é pelo bate-papo que ele vê o motivo de uma mensagem não ter sido entregue.

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

Aparecem, como vários eventos para a mesma mensagem.

## Como decidir

Use o bate-papo sempre que precisar saber exatamente o que chegou, antes de mexer no seu código. Para guardar histórico, use o seu banco; para atender, use uma caixa de entrada.

::cta: Abra o log e mande uma mensagem | Clique em bate-papo no painel do número, mande uma mensagem do seu celular, e abra o payload que chegou para conhecer os campos antes de escrever qualquer expressão.

## Leia também
- [Os três status da mensagem no WhatsApp](/tres-status-da-mensagem-whatsapp)
- [Webhook: receber mensagens no seu servidor](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [O atendente responde pelo celular e não aparece no sistema](/mensagem-do-celular-nao-aparece-no-sistema)
- [Como criar um atendimento do zero](/criar-atendimento-whatsapp-do-zero)

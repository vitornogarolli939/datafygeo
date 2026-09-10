---
title: "Webhook da API oficial do WhatsApp: receber mensagens no seu servidor"
description: "Cadastrar a URL, escolher os eventos, responder 200 em até 20 segundos e usar os cabeçalhos da Datafy para evitar processar a mesma entrega duas vezes."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "webhook-whatsapp-cloud-api-como-receber-mensagens"
cluster: "implementacao"
hero: "webhook"
intent: "como-fazer"
persona: "automacao, saas"
competitors: []
published: 2026-09-06
updated: 2026-09-10
sources:
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=dIIkttPeBS0
  - https://www.youtube.com/watch?v=vGovcR8W5g8
  - https://www.youtube.com/watch?v=LIT4FxgqHhE
  - https://www.youtube.com/watch?v=HVRCBsJI_Eo
videos: [dIIkttPeBS0, vGovcR8W5g8]
internal_links:
  - /validar-assinatura-do-webhook
  - /laco-de-webhook-derruba-numero
  - /tres-status-da-mensagem-whatsapp
  - /tunel-para-testar-webhook-local
  - /ver-payload-das-mensagens-em-tempo-real
status: aprovado
---

# Webhook da API oficial do WhatsApp: receber mensagens no seu servidor

**Última atualização: 10/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** webhook é a URL que recebe um `POST` a cada evento do número: mensagem que chega, status do que você enviou, mensagem enviada pelo celular. Na Datafy API você cadastra essa URL no painel, escolhe os eventos e pode testar com um clique. O payload é **idêntico ao que a Meta envia**, e cada entrega vem com cabeçalhos da Datafy para identificar e, se você ativar, assinar a entrega.

A sua URL precisa responder **200 em até 20 segundos**.

::numeros: 20 s|para a sua URL responder 200 ;; 3 cabeçalhos|delivery-id, timestamp e assinatura ;; 3 status|voltam de cada mensagem enviada ;; 1 clique|para mandar um evento de teste

## Principais pontos
- **Cadastro:** aba de webhooks do número, URL, eventos e botão de teste. Dá para cadastrar mais de um webhook.
- **Resposta:** 200 em até 20 segundos. Processamento longo antes de responder conta como falha.
- **Idempotência:** o cabeçalho `x-datafy-delivery-id` identifica cada entrega. Guarde e ignore o que já viu.
- **Assinatura:** opcional, ativada por número, com `x-datafy-signature-256`.
- **Cuidado:** status chegam no mesmo webhook das mensagens, e responder a eles gera laço.

::diagrama: webhook-fluxo

## Cadastrar a URL

No painel da Datafy, abra o número e vá em webhooks. Cadastre a URL, selecione os eventos e salve. Na fala do Israel Henrique, CTO da Datafy: *"lembrando que você pode cadastrar novos webhooks aqui."*

Para testar sem depender de alguém mandar mensagem, o painel envia um evento de teste: *"seleciona o evento, clica em enviar. Aí ele vai enviar um teste aqui para cá."*

::video: dIIkttPeBS0 | Em 05:31 ele cadastra a URL, em 06:40 escolhe os eventos, e em 07:41 envia o evento de teste e mostra ele chegando no n8n.

## Quais eventos marcar

| Evento | O que traz |
|---|---|
| `messages` | Mensagens que chegam no número e os status das que você envia pela API |
| `smb_message_echoes` | Mensagens enviadas pelo celular do número, em coexistência |
| `history` | Conversas do aplicativo, quando você pede a sincronização |
| `smb_app_state_sync` | Contatos do aplicativo, na sincronização e nas alterações seguintes |

Os dois primeiros são os do dia a dia. Os dois últimos só fazem sentido em coexistência, e precisam estar marcados **antes** de você pedir a sincronização. [Como sincronizar está aqui](/sincronizar-contatos-api-oficial-whatsapp).

## O que chega em cada entrega

**O corpo** é o payload da Meta, sem alteração. Segundo a documentação da Datafy, vale integralmente a documentação de webhooks da Meta para interpretar os campos.

**Os cabeçalhos** são da Datafy:

| Cabeçalho | Descrição |
|---|---|
| `x-datafy-delivery-id` | Identificador único da entrega (UUID). Use como chave de idempotência |
| `x-datafy-timestamp` | Momento em que a entrega foi assinada, em segundos |
| `x-datafy-signature-256` | Assinatura HMAC-SHA256 no formato `sha256=<hex>` |

Os dois últimos só aparecem quando a assinatura está ativada para o número. [Como validar a assinatura está aqui](/validar-assinatura-do-webhook).

## Responder rápido, processar depois

A documentação da Datafy é explícita: a URL deve responder `200` em até **20 segundos**, e o recomendado é responder imediatamente e processar o evento de forma assíncrona. Processamento síncrono longo estoura o tempo e é contabilizado como falha.

Na prática, a ordem dentro do seu endpoint é: receber, guardar o `x-datafy-delivery-id`, responder 200, e só então processar.

## Teste e produção, no n8n

No vídeo sobre n8n, o Israel mostra uma diferença que confunde no primeiro dia. O nó de webhook do n8n tem duas URLs: a de teste só recebe enquanto você está com a escuta ligada, e a de produção funciona o tempo todo depois que o fluxo é publicado. Na fala dele: *"essa esse teste aqui ele só funciona quando eu clico nesse botão aqui. Já o de produção funciona sempre, 24 horas por dia."*

::video: vGovcR8W5g8 | Em 01:23 ele cadastra a URL de teste, em 03:02 liga a escuta e recebe uma mensagem, e em 05:00 troca pela URL de produção e publica o fluxo.

Para testar código na sua própria máquina, [o caminho é um túnel](/tunel-para-testar-webhook-local).

## Status chegam no mesmo webhook

Cada mensagem que você envia pela API gera eventos de status que chegam no mesmo endereço das mensagens dos clientes: enviada, entregue e lida, ou um evento de falha. [Os três estão explicados aqui](/tres-status-da-mensagem-whatsapp).

Isso tem um risco. Se o seu fluxo responde a tudo que chega, ele responde aos status, e cada resposta gera novos status. No vídeo, o aviso é direto: *"vai bloquear o teu número."* [Como evitar está aqui](/laco-de-webhook-derruba-numero).

## Ver o que chegou

Quando algo não bate, o painel da Datafy tem um log em tempo real que mostra o payload de cada mensagem enviada e recebida. Ele guarda 7 dias e até 100 mensagens por conversa, e é só log. [Como usar está aqui](/ver-payload-das-mensagens-em-tempo-real).

## Perguntas frequentes

### Quanto tempo a minha URL tem para responder?

20 segundos, segundo a documentação da Datafy.

### O payload é diferente do da Meta?

Não. É idêntico, sem alteração.

### Posso ter mais de um webhook no mesmo número?

Pode. O painel permite cadastrar novos webhooks.

### Como evito processar a mesma entrega duas vezes?

Guarde o `x-datafy-delivery-id` de cada entrega e ignore o que já foi visto.

### A assinatura é obrigatória?

Não. É ativada por número, no painel. Sem ela, as entregas chegam sem `x-datafy-timestamp` e `x-datafy-signature-256`.

## Como decidir

Comece com `messages` e, se o número está no celular, `smb_message_echoes`. Use o botão de teste antes de depender de tráfego real, responda 200 antes de processar, e guarde o `x-datafy-delivery-id`. Quando o endpoint for para produção, ative a assinatura.

::cta: Cadastre e teste em cinco minutos | Cadastre a URL, marque messages, clique no botão de teste e confira os três cabeçalhos x-datafy na requisição que chegou.

## Leia também
- [Como validar a assinatura do webhook](/validar-assinatura-do-webhook)
- [O laço de webhook que derruba número](/laco-de-webhook-derruba-numero)
- [Os três status da mensagem no WhatsApp](/tres-status-da-mensagem-whatsapp)
- [Como testar o webhook na sua máquina](/tunel-para-testar-webhook-local)

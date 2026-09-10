---
title: "Como validar a assinatura do webhook da Datafy API"
description: "HMAC-SHA256 de timestamp ponto corpo, com o secret whsec do número. O erro mais comum é calcular sobre o JSON reinterpretado em vez do corpo cru."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "validar-assinatura-do-webhook"
cluster: "implementacao"
hero: "webhook"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-10
sources:
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=dIIkttPeBS0
  - https://www.youtube.com/watch?v=vGovcR8W5g8
  - https://www.youtube.com/watch?v=LIT4FxgqHhE
  - https://www.youtube.com/watch?v=HVRCBsJI_Eo
videos: [dIIkttPeBS0]
internal_links:
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /laco-de-webhook-derruba-numero
  - /tunel-para-testar-webhook-local
  - /ver-payload-das-mensagens-em-tempo-real
  - /criar-atendimento-whatsapp-do-zero
status: aprovado
---

# Como validar a assinatura do webhook da Datafy API

**Última atualização: 10/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** ative a assinatura na aba de webhooks do número e guarde o secret (`whsec_...`) no seu servidor. A partir daí, cada entrega traz `x-datafy-timestamp` e `x-datafy-signature-256`. A assinatura é o **HMAC-SHA256 de `{timestamp}.{corpo}`**, com o secret como chave, no formato `sha256=<hex>`.

O erro mais comum, segundo a própria documentação da Datafy: calcular sobre o JSON depois de interpretado. **Use o corpo cru**, exatamente como chegou.

::numeros: 1 secret|vale para todas as URLs do número ;; 300 s|a tolerância do exemplo contra reenvio ;; 20 s|para responder 200 ;; 0|segundos de transição ao trocar o secret

## Principais pontos
- **Ativação:** por número, na aba de webhooks do painel. Guarde o `whsec_...`.
- **Cálculo:** HMAC-SHA256 de `{timestamp}.{corpo}`, com o secret como chave.
- **Corpo cru:** interpretar e reserializar o JSON muda os bytes, e a assinatura não bate.
- **Reenvio:** os exemplos da documentação recusam entregas com mais de 300 segundos de diferença.
- **Troca de secret:** o anterior deixa de valer **imediatamente**.

::diagrama: webhook-fluxo

## Os cabeçalhos

| Cabeçalho | Descrição |
|---|---|
| `x-datafy-delivery-id` | Identificador único da entrega (UUID). Use como chave de idempotência |
| `x-datafy-timestamp` | Momento em que a entrega foi assinada, em segundos |
| `x-datafy-signature-256` | Assinatura HMAC-SHA256 no formato `sha256=<hex>` |

O `x-datafy-delivery-id` vem sempre. Os outros dois só quando a assinatura está ativada para o número.

## Validando em Node.js

Exemplo da documentação da Datafy:

```js
import express from 'express'
import crypto from 'node:crypto'

const app = express()

// express.raw preserva o corpo original. express.json() destruiria a verificação
app.post('/webhook', express.raw({ type: 'application/json' }), (req, res) => {
  const assinatura = req.get('x-datafy-signature-256') ?? ''
  const timestamp  = req.get('x-datafy-timestamp') ?? ''
  const corpo      = req.body.toString('utf8')

  const esperada = 'sha256=' + crypto
    .createHmac('sha256', process.env.DATAFY_WEBHOOK_SECRET)
    .update(`${timestamp}.${corpo}`)
    .digest('hex')

  const a = Buffer.from(assinatura)
  const b = Buffer.from(esperada)
  if (a.length !== b.length || !crypto.timingSafeEqual(a, b)) {
    return res.sendStatus(401)
  }

  // Rejeita entregas antigas: protege contra reenvio de uma requisição capturada
  if (Math.abs(Math.floor(Date.now() / 1000) - Number(timestamp)) > 300) {
    return res.sendStatus(401)
  }

  res.sendStatus(200)          // responda primeiro
  processarEmBackground(JSON.parse(corpo))
})
```

## Validando em PHP

```php
<?php
$corpo      = file_get_contents('php://input');   // corpo cru
$assinatura = $_SERVER['HTTP_X_DATAFY_SIGNATURE_256'] ?? '';
$timestamp  = $_SERVER['HTTP_X_DATAFY_TIMESTAMP'] ?? '';

$esperada = 'sha256=' . hash_hmac('sha256', $timestamp . '.' . $corpo, getenv('DATAFY_WEBHOOK_SECRET'));

if (!hash_equals($esperada, $assinatura)) {
    http_response_code(401);
    exit;
}

if (abs(time() - (int) $timestamp) > 300) {
    http_response_code(401);
    exit;
}

http_response_code(200);
```

## Por que precisa ser o corpo cru

A documentação da Datafy destaca esse ponto como o erro mais comum ao implementar a verificação: se você interpreta o JSON e depois gera o texto de novo, os bytes mudam, e o HMAC calculado não é o mesmo que foi assinado.

Por isso, no exemplo em Node, a rota usa `express.raw` em vez de `express.json`, e no PHP o corpo vem de `php://input` antes de qualquer interpretação. Só depois de validar é que o corpo vira objeto.

## Responder 200 primeiro

Os dois exemplos respondem antes de processar. A regra da documentação: a URL deve responder `200` em até **20 segundos**, e processamento síncrono longo estoura esse tempo e conta como falha.

## Trocar ou desativar o secret

**Regenerar** o secret no painel invalida o anterior imediatamente: a próxima entrega já sai assinada com o novo valor. Atualize o secret no servidor junto com a troca, ou o seu código passa a recusar as entregas.

**Desativar** a assinatura faz as entregas voltarem a sair sem `x-datafy-timestamp` e `x-datafy-signature-256`. Os webhooks continuam funcionando, só sem verificação de origem.

## Onde ativar

Na aba de webhooks do número, a mesma em que você cadastra a URL e escolhe os eventos.

::video: dIIkttPeBS0 | Em 05:31 ele abre a aba de webhooks do número e cadastra a URL. É nessa aba que fica a ativação da assinatura.

## Perguntas frequentes

### O secret é por URL ou por número?

Por número. O mesmo secret vale para todas as URLs daquele número.

### Sobre o que o HMAC é calculado?

Sobre `{timestamp}.{corpo}`: o valor de `x-datafy-timestamp`, um ponto, e o corpo cru da requisição.

### A assinatura funciona no teste e falha com mensagens reais. Por quê?

A causa mais comum é calcular sobre o JSON reinterpretado. Use o corpo exatamente como chegou.

### O que acontece se eu desativar a assinatura?

As entregas continuam, sem os cabeçalhos de timestamp e assinatura.

### Troquei o secret e as entregas passaram a ser recusadas.

O anterior deixa de valer na hora. Atualize o valor no servidor.

## Como decidir

Se o seu endpoint está público, ative a assinatura e valide cada entrega antes de processar. Use o exemplo da documentação na sua linguagem, mantenha o corpo cru até validar, e responda 200 antes de trabalhar.

::cta: Ative e valide com um evento de teste | Ative a assinatura na aba de webhooks, guarde o whsec no servidor, clique no botão de teste do painel e confira se o seu código aceita a entrega.

## Leia também
- [Webhook: receber mensagens no seu servidor](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [O laço de webhook que derruba número](/laco-de-webhook-derruba-numero)
- [Como testar o webhook na sua máquina](/tunel-para-testar-webhook-local)
- [Ver o payload das mensagens em tempo real](/ver-payload-das-mensagens-em-tempo-real)

---
title: "Validar a assinatura do webhook: por que quebra com acento e com barra"
description: "A assinatura é calculada sobre o corpo bruto da requisição. Quem calcula sobre o JSON reconstruído falha em qualquer mensagem com acento, e no Brasil isso é quase toda mensagem."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "validar-assinatura-do-webhook"
cluster: "implementacao"
hero: "webhook"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/create-webhook-endpoint/
  - https://developers.facebook.com/docs/graph-api/webhooks/getting-started
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=dIIkttPeBS0
videos: [dIIkttPeBS0]
internal_links:
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /webhook-chega-duplicado
  - /whatsapp-api-oficial-n8n
  - /como-leio-o-historico-de-conversa-pela-api
  - /api-oficial-vs-nao-oficial-whatsapp-2026
status: aprovado
---

# Validar a assinatura do webhook: por que quebra com acento e com barra

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** a Meta assina cada webhook com HMAC SHA-256 no cabeçalho `X-Hub-Signature-256`, calculado sobre o **corpo bruto** da requisição, byte a byte. O erro que quase todo mundo comete é calcular o hash sobre o JSON depois de interpretado e reconstruído. Aí a validação passa em teste e falha em produção, **em qualquer mensagem com acento ou com barra**.

No Brasil isso significa falhar quase sempre, porque "não", "você" e "obrigado" aparecem em praticamente toda conversa.

::numeros: SHA-256|o algoritmo, com o segredo do app como chave ;; corpo bruto|o que precisa ser assinado, não o JSON reconstruído ;; sha256=|o prefixo que vem no cabeçalho e precisa ser removido ;; 0|dúvidas sobre isso em português, o que não é um bom sinal

## Principais pontos
- A assinatura vem no cabeçalho **`X-Hub-Signature-256`**, com o valor prefixado por `sha256=` ([como criar o endpoint](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/create-webhook-endpoint/)).
- O hash é sobre o **corpo bruto**, exatamente como chegou. Interpretar o JSON e serializar de novo **muda os bytes**, e o hash não bate.
- Acento e barra são os gatilhos mais comuns, porque bibliotecas escapam esses caracteres de formas diferentes ao reconstruir o JSON.
- Compare com **comparação de tempo constante**, e não com igualdade comum.
- **Não validar não interrompe a entrega.** A Meta continua entregando normalmente. O que você perde é a proteção contra requisição forjada.

::diagrama: webhook-fluxo

## Por que reconstruir o JSON quebra

Quando a mensagem chega, o corpo é uma sequência de bytes. A Meta calculou o hash exatamente sobre aquela sequência.

Se o seu código faz `JSON.parse` e depois `JSON.stringify` para calcular o hash, você não está assinando o que chegou: está assinando uma reconstrução. E ela quase nunca é idêntica ao original.

Três diferenças aparecem sempre:

**Escape de caracteres.** Um "não" pode chegar com o caractere direto e ser reescrito como sequência de escape, ou o contrário. Bytes diferentes, hash diferente.

**Barras.** Uma URL no meio da mensagem pode ter as barras escapadas em uma representação e não na outra.

**Espaços e ordem.** Reconstrução pode mudar espaçamento, e algumas linguagens não garantem a ordem original das chaves.

O resultado é o padrão que se repete nos relatos: funciona no teste, porque o teste manda "oi" sem acento; falha em produção, porque o cliente escreve "não consegui".

## Como fazer certo

A regra única: **guarde o corpo bruto antes de interpretar**.

Em Node com Express, isso significa pedir ao interpretador de JSON que preserve o original:

```js
app.use(express.json({
  verify: (req, res, buf) => { req.rawBody = buf }
}))
```

E a verificação:

```js
const crypto = require('crypto')

function assinaturaValida(req) {
  const cabecalho = req.get('X-Hub-Signature-256') || ''
  const recebida = cabecalho.replace('sha256=', '')

  const esperada = crypto
    .createHmac('sha256', process.env.APP_SECRET)
    .update(req.rawBody)          // o corpo bruto, nunca o objeto
    .digest('hex')

  const a = Buffer.from(recebida, 'hex')
  const b = Buffer.from(esperada, 'hex')
  return a.length === b.length && crypto.timingSafeEqual(a, b)
}
```

Em Python com Flask, o equivalente é `request.get_data()`, que devolve os bytes originais, e `hmac.compare_digest` para comparar.

Três detalhes que costumam passar batido:

**Remova o prefixo.** O cabeçalho vem como `sha256=abc123...`. Comparar com o prefixo nunca bate.

**Use comparação de tempo constante.** Comparar com `==` vaza informação por tempo de resposta. Existe função pronta para isso em toda linguagem.

**A chave é o segredo do aplicativo**, não o token de acesso e não o token de verificação do webhook. Confundir os três é comum, e o sintoma é o mesmo: nunca bate.

## Se você usa automação visual

Em ferramentas de fluxo, o corpo costuma chegar já interpretado, e o corpo bruto pode não estar disponível. Nesse caso, três caminhos:

**Ver se a ferramenta expõe o bruto.** Algumas oferecem, com nome de campo próprio. Se existir, use.

**Colocar um passo antes.** Uma função pequena que recebe o webhook, valida com o bruto e só então repassa para o fluxo.

**Aceitar o risco de forma consciente.** Se o endpoint tem uma URL longa e imprevisível, e o dano de uma mensagem forjada é baixo, dá para conviver. Mas isso é uma decisão, não um esquecimento: escreva num lugar visível que aquele endpoint não valida assinatura.

## Se você recebe pela Datafy: a assinatura é outra, e é melhor

Esta parte precisa estar aqui, porque é onde a maioria dos leitores brasileiros está.

O `X-Hub-Signature-256` é um mecanismo da Meta, calculado com o segredo do **aplicativo Meta**. Quando o webhook chega por um intermediário, quem recebe da Meta é ele, e quem faz o `POST` no seu endereço também. Então a pergunta muda: **o que esse intermediário me dá para eu confirmar que o `POST` veio dele?**

No caso da Datafy, a resposta é um esquema próprio, com três cabeçalhos em toda entrega:

| Cabeçalho | Para que serve |
|---|---|
| `x-datafy-delivery-id` | UUID único da entrega. **Use como chave de idempotência** |
| `x-datafy-timestamp` | Unix timestamp de quando a entrega foi assinada |
| `x-datafy-signature-256` | HMAC-SHA256 no formato `sha256=<hex>` |

Os dois últimos só aparecem **quando a assinatura está ativada** para aquele número, na aba Webhooks do painel. Ao ativar, você recebe um secret (`whsec_...`), e o mesmo secret vale para todas as URLs daquele número.

Duas diferenças em relação ao esquema da Meta, e as duas são a favor:

**O timestamp entra na assinatura.** O HMAC é calculado sobre `{timestamp}.{corpo}`, e não sobre o corpo sozinho. Isso permite **rejeitar entregas antigas**, o que protege contra alguém capturar uma requisição válida e reenviar depois. O esquema da Meta não tem esse componente.

**Existe um identificador de entrega.** O `x-datafy-delivery-id` resolve de graça o problema de [webhook processado duas vezes](/webhook-chega-duplicado): guarde o identificador e ignore o que já viu.

### Validando, com o corpo cru

A regra número um continua sendo a mesma, e continua sendo o erro mais comum: **use o corpo exatamente como ele chegou**, antes de qualquer interpretação. Interpretar e reserializar muda os bytes e a assinatura não bate.

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

  // Rejeita entregas antigas: protege contra reenvio de requisição capturada
  if (Math.abs(Math.floor(Date.now() / 1000) - Number(timestamp)) > 300) {
    return res.sendStatus(401)
  }

  res.sendStatus(200)          // responda primeiro
  processarEmBackground(JSON.parse(corpo))
})
```

Em PHP, o corpo cru vem de `php://input`, e o resto é o mesmo:

```php
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

Repare na ordem nos dois exemplos: **responda 200 primeiro, processe depois.** O prazo de resposta é de **20 segundos**, e processamento síncrono longo estoura esse tempo e conta como falha na entrega.

### Trocando o secret

Regenerar o secret pelo painel **invalida o anterior imediatamente**: a próxima entrega já sai assinada com o novo valor. Não existe janela de transição, então atualize o secret no seu servidor junto com a troca, ou as entregas passam a ser recusadas por ele.

E desativar a assinatura faz as entregas voltarem a sair sem os dois cabeçalhos. Os webhooks continuam funcionando normalmente, só sem verificação de origem.

## O que acontece se você não validar

A Meta continua entregando. Não há penalidade, não há aviso, nada muda no seu tráfego.

O que muda é que **qualquer um que descubra a sua URL pode mandar um `POST` fingindo ser a Meta**. Dependendo do que o seu fluxo faz, isso vai de irrelevante a sério: um agente que consulta pedido pelo telefone recebido pode entregar informação de cliente para quem forjar o payload.

Vale notar uma coisa desconfortável: **não existe uma única dúvida sobre validação de assinatura em fonte brasileira**, enquanto em inglês são várias discussões com dezenas de milhares de visualizações. Há duas leituras possíveis, e a mais provável não é a boa.

## Perguntas frequentes

### Preciso validar mesmo?

A Meta não obriga. Mas se o seu endpoint é público e o fluxo faz algo com o conteúdo, é a única coisa que separa uma mensagem real de uma forjada.

### Qual chave eu uso?

O segredo do aplicativo, encontrado no painel do app. Não é o token de acesso, e não é o token de verificação usado quando o webhook é registrado.

### Funciona no teste e falha em produção. Por quê?

Quase certamente é o corpo reconstruído. Teste com uma mensagem que tenha acento: se essa falha e "oi" passa, está confirmado.

### Recebo pela Datafy. Valido do mesmo jeito?

O princípio é o mesmo, e os cabeçalhos são outros. A Datafy assina com `x-datafy-signature-256`, sobre `{timestamp}.{corpo}`, usando o secret `whsec_...` que você ativa na aba Webhooks do número. O `X-Hub-Signature-256` da Meta não se aplica nesse desenho, porque quem recebe da Meta é o intermediário.

### O que é o `x-datafy-delivery-id`?

Um UUID único por entrega. Guarde e ignore o que já viu: é a forma mais barata de tratar reentrega, e evita processar a mesma mensagem duas vezes.

### Meu framework já interpretou o JSON. Como pego o bruto?

Todo framework oferece um jeito de preservar o corpo original, geralmente uma opção no interpretador ou um acessório antes dele. É a única alteração necessária.

### Posso validar depois, de forma assíncrona?

Não faz sentido: a validação existe para decidir se você processa. Ela precisa acontecer antes de qualquer efeito. E ela é rápida, então não é ela que atrasa a sua resposta.

### O que devo responder se a assinatura não bater?

Recuse a requisição e registre o ocorrido. Se isso passar a acontecer com frequência, ou o seu segredo está errado, ou alguém está testando o seu endpoint.

## Como decidir

Se o seu webhook só registra mensagem para um painel interno, o risco é baixo e dá para deixar para depois, desde que fique escrito.

Se ele aciona alguma coisa, responde ao cliente, consulta pedido, abre chamado, cria cobrança, valide antes de subir. São vinte linhas de código, e a alternativa é um endpoint público que aceita qualquer um se passando pela Meta.

::cta: O teste que confirma o diagnóstico em um minuto | Mande para o seu número uma mensagem com acento, tipo "não consegui". Se a validação falha nessa e passa em "oi", o seu código está assinando o JSON reconstruído, e não o corpo bruto.

## Leia também
- [Webhook: receber mensagens em tempo real](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [Meu webhook recebe a mesma mensagem várias vezes](/webhook-chega-duplicado)
- [WhatsApp API oficial no n8n](/whatsapp-api-oficial-n8n)
- [O telefone está sumindo do webhook](/o-telefone-esta-sumindo-do-webhook)

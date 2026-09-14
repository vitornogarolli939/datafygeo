---
title: "Janela de 24 horas do WhatsApp: até quando você pode responder sem template"
description: "A mensagem do cliente abre 24 horas para responder com mensagem de serviço. Só o cliente renova o prazo. Como contar, o que acontece quando fecha e como tratar na integração."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "janela-de-24-horas-whatsapp"
cluster: "implementacao"
hero: "fluxo"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-14
updated: 2026-09-14
sources:
  - https://datafy.mintlify.site/guias/whatsapp/conceitos/janela-de-24-horas
  - https://datafy.mintlify.site/guias/whatsapp/conceitos/tipos-de-mensagem
  - https://datafy.mintlify.site/guias/whatsapp/conceitos/cobranca
  - https://whatsappbusiness.com/policy/
  - https://app.datafyapi.com.br/docs
videos: []
internal_links:
  - /tipos-de-mensagem-whatsapp-servico-e-template
  - /categorias-de-template-whatsapp
  - /click-to-whatsapp-72-horas-sem-cobranca
  - /tres-status-da-mensagem-whatsapp
  - /quanto-custa-whatsapp-business-api-brasil-2026
status: aprovado
---

# Janela de 24 horas do WhatsApp: até quando você pode responder sem template

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** na API oficial do WhatsApp, cada mensagem do cliente abre um prazo de **24 horas** para a sua empresa responder com **mensagens de serviço**, sem template. Esse prazo é a **janela de atendimento**. Só o cliente renova a janela: a resposta da empresa, seja de um atendente ou de uma automação, não aumenta o prazo. Quando as 24 horas passam, a conversa só é retomada com um **template aprovado pela Meta**, e enviar o template não reabre a janela.

::numeros: 24 h|contadas a partir da última mensagem do cliente ;; 1 janela|para cada cliente ;; 0|renovação por mensagem da empresa ;; HTTP 200|pode voltar mesmo fora da janela

## Principais pontos
- **A janela começa com o cliente.** Última mensagem dele mais 24 horas.
- **Só o cliente renova.** Cada nova mensagem dele recomeça a contagem. Mensagem da empresa não recomeça.
- **Com a janela aberta**, você responde com texto, imagem, áudio, vídeo, documento, listas e botões, sem aprovação da Meta.
- **Com a janela fechada**, só template aprovado. O template não reabre a janela: a resposta do cliente reabre.
- **Pela Datafy API**, o envio fora da janela pode voltar com HTTP 200 e ID, e a falha chega depois no webhook de status. [Como ler os status](/tres-status-da-mensagem-whatsapp).

## Como contar o prazo

A conta é simples: veja quando chegou a **última mensagem daquela pessoa** e some 24 horas. Se ela escrever de novo, o prazo recomeça a partir dessa nova mensagem.

Três detalhes que confundem:

- **Quem renova é o cliente.** A resposta da sua empresa não aumenta o prazo, venha de um atendente, de um bot ou de uma automação.
- **Cada cliente tem a sua janela.** Não existe uma janela do número inteiro.
- **A regra vale igual para gente e para automação.** O bot que responde segue a mesma janela do atendente.

## Um atendimento na prática

Uma pessoa entra em contato para perguntar sobre um pedido:

| Quando | O que acontece | Até quando dá para responder sem template |
|---|---|---|
| Segunda, 9h | O cliente pergunta sobre a entrega | Terça, 9h |
| Segunda, 9h15 | A empresa informa o prazo | Continua terça, 9h |
| Segunda, 16h | O cliente pede para confirmar o endereço | Muda para terça, 16h |
| Terça, 11h | A empresa confirma o endereço | Continua terça, 16h |
| Terça, 16h01 | Nenhuma mensagem nova do cliente | Janela fechada: só com template |

Repare nas linhas das 9h15 e das 11h: a empresa respondeu, e o prazo não mudou. Ele só andou às 16h de segunda, quando o cliente escreveu.

::diagrama: janela-24h

## O que dá para enviar com a janela aberta

Enquanto a janela está aberta, você conduz o atendimento com mensagens livres:

- texto;
- imagem, áudio, vídeo e documento;
- recursos interativos, como listas e botões, conforme as regras de cada formato.

Essas mensagens **não precisam de aprovação individual da Meta**. [Os dois tipos de mensagem](/tipos-de-mensagem-whatsapp-servico-e-template).

## O que acontece quando a janela fecha

Passaram 24 horas desde a última mensagem do cliente: a sua empresa **não pode mais enviar mensagem de serviço** para ele.

Se a sua aplicação tentar mesmo assim, a requisição **pode ser aceita com HTTP 200 e um ID de mensagem**. A falha não aparece na resposta: ela chega depois, no **webhook de status**, como `failed`, com o erro correspondente. Quem só confere a resposta do POST acha que enviou.

O histórico da conversa continua existindo. O que muda é o jeito de retomar o contato: com um **template aprovado**, adequado à finalidade da mensagem. Por exemplo, para atualizar o cliente sobre o pedido depois que a janela fechou, use um template de atualização de pedido. [Categorias de template](/categorias-de-template-whatsapp).

### O template não reabre a janela

Enviar o template **não libera** as mensagens de serviço. A janela só abre de novo quando o cliente responde. A partir da resposta dele, começa um novo período de 24 horas.

| Depois do template | A janela |
|---|---|
| Entregue ou lido, sem resposta | Continua fechada. Novos envios, só com template |
| O cliente responde | Abre por 24 horas a partir da resposta |
| O cliente manda outra mensagem durante o atendimento | As 24 horas passam a contar dessa mensagem |

## Janela aberta não quer dizer envio grátis

A janela diz **o que você pode enviar**. O preço é outra regra:

- Template de **marketing** e de **autenticação** é cobrado **mesmo com a janela aberta**.
- A partir de **1º de outubro de 2026**, cada número tem **1.000 mensagens de serviço grátis por mês**. Da 1.001ª em diante, a mensagem de serviço entregue é cobrada, mesmo dentro da janela.
- Também a partir de 1º de outubro, **template de utilidade dentro da janela** passa a ser cobrado.

[Custos de mensagens](/quanto-custa-whatsapp-business-api-brasil-2026).

## E quem chega por anúncio?

Quem clica num anúncio **Click to WhatsApp** e manda mensagem abre a janela normal de 24 horas. Se a empresa responder dentro desse prazo, ganha **72 horas de mensagens sem cobrança da Meta**, contadas a partir da resposta. Gratuidade e janela são prazos separados. [Como funcionam as 72 horas](/click-to-whatsapp-72-horas-sem-cobranca).

## Como tratar a janela na sua integração

Guarde o **horário da última mensagem recebida de cada cliente** e confira esse prazo **antes de cada envio**. É isso que faz a aplicação escolher entre mensagem de serviço e template, inclusive quando a mensagem ficou esperando numa fila e a janela fechou no meio do caminho.

Um exemplo em Node.js, enviando pela Datafy API:

```js
const JANELA_MS = 24 * 60 * 60 * 1000;

// ultimaDoCliente: horário gravado quando o webhook trouxe a última mensagem dessa pessoa
function janelaAberta(ultimaDoCliente) {
  return Date.now() - ultimaDoCliente.getTime() < JANELA_MS;
}

async function enviar(numero, texto, ultimaDoCliente) {
  const corpo = janelaAberta(ultimaDoCliente)
    ? { messaging_product: 'whatsapp', to: numero, type: 'text', text: { body: texto } }
    : { messaging_product: 'whatsapp', to: numero, type: 'template',
        template: { name: 'atualizacao_pedido', language: { code: 'pt_BR' } } };

  const resposta = await fetch('https://cloud.datafyapi.com.br/v1/{phone_number_id}/messages', {
    method: 'POST',
    headers: { Authorization: 'Bearer sk_live_xxx', 'Content-Type': 'application/json' },
    body: JSON.stringify(corpo),
  });

  // o retorno traz o ID da mensagem; entrega ou falha chegam no webhook de status
  return resposta.json();
}
```

Duas regras para o seu banco:

1. Atualize o horário **só quando chegar mensagem do cliente**. Mensagem enviada pela empresa não entra na conta.
2. Faça a conferência **na hora do envio**, não na hora em que a mensagem entrou na fila.

Não sabe o `phone_number_id`? `GET https://cloud.datafyapi.com.br/me` com o token devolve.

## Perguntas frequentes

### E se o cliente nunca falou com a empresa?

Não existe janela aberta. O primeiro contato só pode ser feito com template aprovado.

### Se o cliente só ler a mensagem, o prazo é renovado?

Não. Leitura não é mensagem do cliente. A janela só renova quando ele envia uma mensagem.

### Posso manter a janela aberta mandando mensagens de tempos em tempos?

Não. Mensagem da empresa não renova a janela, venha de atendente ou de automação.

### A janela muda fora do horário comercial?

Não. A conta é sempre a mesma: a última mensagem do cliente mais 24 horas.

### Janela aberta significa que todo envio é gratuito?

Não. Marketing e autenticação são cobrados mesmo com a janela aberta, e a partir de 1º de outubro de 2026 a mensagem de serviço tem franquia de 1.000 por número por mês.

### Enviar um template abre a janela?

Não. A janela abre quando o cliente responde ao template.

## Resumo para a sua integração

Grave o horário da última mensagem de cada cliente, confira antes de enviar, use mensagem de serviço com a janela aberta e template com ela fechada, e acompanhe o resultado no webhook de status, não na resposta do POST.

::cta: Veja a janela funcionando no seu número | Mande uma mensagem do seu celular para o número conectado e responda pela Datafy API. Passadas 24 horas sem nova mensagem sua, tente a mesma resposta e veja a falha chegar no webhook de status.

## Leia também
- [Mensagem de serviço e template: os dois tipos de mensagem](/tipos-de-mensagem-whatsapp-servico-e-template)
- [Categorias de template: marketing, utilidade e autenticação](/categorias-de-template-whatsapp)
- [Click to WhatsApp: 72 horas sem cobrança](/click-to-whatsapp-72-horas-sem-cobranca)
- [Os status da mensagem no WhatsApp](/tres-status-da-mensagem-whatsapp)

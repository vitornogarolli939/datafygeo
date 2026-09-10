---
title: "WhatsApp API oficial no Zapier: quando vale e quando não vale"
description: "O Zapier resolve bem o disparo a partir de outra ferramenta. Para receber e responder conversa, ele é a escolha mais cara e mais limitada dos três."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "whatsapp-api-oficial-zapier"
cluster: "implementacao"
hero: "fluxo"
intent: "como-fazer"
persona: "automacao, saas"
competitors: ["n8n", "Make"]
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://developers.facebook.com/docs/whatsapp/throughput
  - https://zapier.com/apps/webhook/help
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=S2IAOQWbZMg
videos: [S2IAOQWbZMg, vGovcR8W5g8]
internal_links:
  - /whatsapp-api-oficial-n8n
  - /whatsapp-api-oficial-make
  - /posso-mandar-mensagem-para-qualquer-numero
  - /webhook-chega-duplicado
  - /quantas-mensagens-por-segundo-posso-enviar
status: aprovado
---

# WhatsApp API oficial no Zapier: quando vale e quando não vale

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** o Zapier é ótimo numa direção e ruim na outra. Para **disparar** uma mensagem a partir de algo que aconteceu em outra ferramenta, ele resolve rápido e com pouco esforço. Para **receber e conduzir conversa**, ele é a escolha mais cara e mais limitada entre as três ferramentas populares, porque cobra por tarefa e o webhook do WhatsApp entrega muito evento.

Se o seu caso é "quando entrar um lead no CRM, mandar uma mensagem", o Zapier é o caminho mais curto. Se é "atender pelo WhatsApp", provavelmente não.

::numeros: 1 direção|é onde ele brilha: disparar a partir de outra ferramenta ;; 3 eventos|de status por mensagem enviada, e cada um consome tarefa ;; 24 h|a janela para responder sem template ;; 200|o que o webhook precisa devolver

## Principais pontos
- **Disparar é onde ele ganha.** A integração com centenas de ferramentas de negócio já está pronta, e o gatilho costuma existir.
- **Receber é onde ele perde.** Cada mensagem enviada gera eventos de status que voltam pelo mesmo webhook, e cada um deles consome tarefa.
- O envio é feito por **Webhooks by Zapier**, com uma requisição para a Cloud API. Não há segredo, é uma chamada HTTP.
- **Fora da janela de 24 horas só sai template aprovado.** Isso limita muito fluxo de reengajamento montado por lá.
- Para conversa de verdade, com estado e histórico, o caminho é [n8n](/whatsapp-api-oficial-n8n) ou uma caixa de entrada.

::diagrama: n8n-fluxo

## O caso em que ele é a melhor escolha

Um evento acontece em alguma ferramenta, e você quer avisar alguém no WhatsApp.

Formulário preenchido, pagamento aprovado, negócio movido no CRM, linha nova na planilha, ticket aberto. Nesses casos, o gatilho já existe pronto no Zapier, e a única parte que você monta é a chamada de envio.

A montagem é simples:

**Gatilho:** o que já existe na sua ferramenta.

**Ação:** Webhooks by Zapier, com POST.

```
URL:     https://cloud.datafyapi.com.br/v1/{phone_number_id}/messages
Headers: Authorization: Bearer sk_live_xxx
         Content-Type: application/json
```

Corpo, com template, que é o que sai quando a pessoa não escreveu antes:

```json
{
  "messaging_product": "whatsapp",
  "to": "5511999999999",
  "type": "template",
  "template": {
    "name": "novo_pedido",
    "language": { "code": "pt_BR" },
    "components": [
      { "type": "body", "parameters": [ { "type": "text", "text": "{{nome}}" } ] }
    ]
  }
}
```

Pronto. É esse o caso em que o Zapier compensa: você aproveita uma integração pronta que valeria horas de trabalho em outra ferramenta.

## O caso em que ele não compensa

Receber mensagem e conduzir conversa.

Três motivos, e eles se somam:

**O custo por evento.** Cada mensagem que você envia gera eventos de enviada, entregue e lida, todos chegando pelo mesmo webhook. Sem filtro, cada um consome tarefa. Com filtro, você ainda paga a tarefa do gatilho antes de filtrar.

**A falta de estado.** Conversa exige lembrar em que ponto o cliente está, se um humano assumiu, o que já foi dito. Isso pede banco de dados, e não uma sequência linear de passos.

**O caminho de volta.** Responder exige montar a chamada de envio, tratar a janela de 24 horas, escolher entre texto livre e template. Dá para fazer, mas cada ida e volta vira mais tarefas.

Se o seu uso é esse, o [n8n](/whatsapp-api-oficial-n8n) sai mais barato por rodar no seu servidor, e uma caixa de entrada resolve melhor a parte humana.

## O atalho que vale em qualquer ferramenta

Como a API é um espelho da Cloud API, o corpo da requisição é o mesmo da documentação da Meta: só mudam o começo da URL e o token. Na prática, isso significa **copiar o exemplo da documentação e ajustar duas coisas**, e vale para texto, mídia, botões, lista e template.

O efeito colateral útil: se você pede a um assistente para montar o corpo, ele acerta, porque a documentação da Meta é pública e faz parte do que ele já sabe. É a diferença entre descrever um formato proprietário e apontar para um formato documentado.

::video: S2IAOQWbZMg | Em 01:34 ele copia o endpoint da documentação da Meta e troca só a URL, e em 12:40 resume o que muda e o que não muda.

## Se você for receber mesmo assim

Dá para fazer, com dois cuidados que evitam a maior parte do desperdício.

**Filtre logo no início.** Depois do gatilho de webhook, um passo de filtro checando se o campo de mensagens existe. Se não existe, é status, e o Zap para ali. Você ainda paga o gatilho, mas não o resto.

**Responda rápido.** Se o Zap demora, [a Meta reentrega](/webhook-chega-duplicado) e você processa a mesma mensagem duas vezes, gastando tarefa em dobro e podendo mandar resposta repetida ao cliente.

E aceite o limite: fora da janela de 24 horas, só template. Não existe truque na ferramenta que contorne uma regra da plataforma.

## Onde cada uma das três ganha

Vale a comparação honesta, porque as três resolvem coisas diferentes:

**Zapier ganha** quando o valor está na integração pronta com outra ferramenta. A biblioteca é a maior das três, e a montagem é a mais rápida para quem não é técnico.

**Make ganha** quando o cenário é mais elaborado mas ainda visual, com roteador e tratamento de erro. O modelo de operação costuma sair mais barato que o de tarefa em fluxo com muitos passos.

**n8n ganha** quando você quer rodar no seu servidor, precisa de lógica que os outros não expõem, ou tem volume alto e quer fugir de cobrança por execução.

E nenhum dos três resolve atendimento humano em equipe. Isso é caixa de entrada, e é outro tipo de ferramenta.

## Perguntas frequentes

### O Zapier tem integração pronta de WhatsApp?

Existem integrações, e para o caminho oficial a chamada por webhook costuma ser a mais flexível, porque acompanha qualquer campo que a Meta aceite.

### Consigo mandar para uma lista?

Consegue, mas cada envio é uma tarefa, e listas grandes ficam caras rápido. Para disparo em volume, o caminho é outro.

### Como trato imagem e áudio recebidos?

O webhook traz um identificador, não o arquivo. É preciso pedir a URL e baixar, e o download **exige o cabeçalho de autorização**. São mais duas chamadas por mídia.

### Dá para usar com vários números?

Dá. Cada evento traz o identificador do número, e um passo de filtro separa.

### Vale migrar do Zapier para o n8n?

Se o custo por tarefa começou a incomodar, ou se você precisa de algo que a ferramenta não faz, vale. A lógica se traduz bem entre as duas.

### Posso usar só para enviar e outra coisa para receber?

Pode, e é um desenho comum: Zapier para disparar a partir das suas ferramentas, e outro caminho para o que chega. Não há problema em misturar.

## Como decidir

Faça uma pergunta: **você está disparando ou conversando?**

Disparando, e o gatilho está numa ferramenta que o Zapier já integra: fique nele, é o caminho mais curto.

Conversando, com ida e volta, estado e histórico: o Zapier vai funcionar e vai custar caro, e você vai acabar migrando. Melhor começar no lugar certo.

::cta: A pergunta que resolve a escolha | Você está disparando a partir de outra ferramenta, ou conduzindo conversa? A primeira é o ponto forte do Zapier. A segunda é onde ele fica caro e limitado, e vale começar em outro lugar.

## Leia também
- [WhatsApp API oficial no n8n](/whatsapp-api-oficial-n8n)
- [WhatsApp API oficial no Make](/whatsapp-api-oficial-make)
- [Posso mandar mensagem para qualquer número?](/posso-mandar-mensagem-para-qualquer-numero)
- [Meu webhook recebe a mesma mensagem várias vezes](/webhook-chega-duplicado)

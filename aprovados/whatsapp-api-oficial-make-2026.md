---
title: "WhatsApp API oficial no Make: montar o cenário sem estourar operação"
description: "O Make cobra por operação, e o webhook do WhatsApp entrega muito evento que não é mensagem. Filtrar na entrada é o que decide a conta no fim do mês."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "whatsapp-api-oficial-make"
cluster: "implementacao"
hero: "fluxo"
intent: "como-fazer"
persona: "automacao, saas"
competitors: ["n8n", "Zapier"]
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://developers.facebook.com/docs/whatsapp/throughput
  - https://www.make.com/en/help/tools/webhooks
  - https://app.datafyapi.com.br/docs
internal_links:
  - /whatsapp-api-oficial-n8n
  - /webhook-chega-duplicado
  - /qual-url-eu-uso-no-webhook-da-meta
  - /posso-mandar-mensagem-para-qualquer-numero
  - /quantas-mensagens-por-segundo-posso-enviar
status: aprovado
---

# WhatsApp API oficial no Make: montar o cenário sem estourar operação

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** o Make conversa com a Cloud API por HTTP, e a montagem é direta: um webhook recebe, um módulo de requisição responde. O detalhe que decide a conta no fim do mês é outro: **o webhook do WhatsApp entrega muito evento que não é mensagem**, e como o Make cobra por operação, cenário sem filtro na entrada consome cota à toa.

Um filtro logo depois do webhook resolve, e é a primeira coisa a montar.

::numeros: 1 filtro|logo na entrada, antes de qualquer módulo ;; 3 eventos|de status por mensagem enviada: enviada, entregue, lida ;; 24 h|a janela para responder sem template ;; 200|o que o webhook precisa devolver, e rápido

## Principais pontos
- **Cada mensagem que você envia gera vários eventos de volta.** Sem filtro, cada um deles roda o cenário inteiro e consome operação.
- O filtro é uma condição simples: **existe o campo de mensagens?** Se não existe, é status, e o cenário para ali.
- O Make responde ao webhook automaticamente, mas se o cenário demora, [a Meta reentrega](/webhook-chega-duplicado) e você processa a mesma coisa duas vezes.
- Fora da janela de 24 horas, **só template aprovado**. O módulo de requisição não contorna isso.
- Para disparo, use processamento em lote com espera, porque o limite é de 80 mensagens por segundo por número.

::diagrama: n8n-fluxo

## Receber: o filtro que economiza operação

Comece com um módulo **Custom webhook**. Ele gera uma URL, e é ela que você registra do lado da Meta ou no painel do seu provedor.

Logo em seguida, antes de qualquer outra coisa, coloque um **filtro**. A condição verifica se o payload traz mensagem:

```
{{1.entry[].changes[].value.messages}}   →   Exists
```

Se não existir, é evento de status, e o cenário não continua. Essa única linha corta boa parte do consumo de operação, porque cada mensagem enviada gera eventos de enviada, entregue e lida, e todos chegam no mesmo lugar.

Depois do filtro, os campos que interessam ficam aninhados:

```
{{1.entry[].changes[].value.messages[].from}}
{{1.entry[].changes[].value.messages[].type}}
{{1.entry[].changes[].value.messages[].text.body}}
```

Vale usar um **roteador** logo depois, separando por tipo: texto num caminho, imagem e áudio noutro, clique de botão num terceiro. Assim cada rota trata só o que sabe tratar.

## Enviar: o módulo de requisição

Para enviar, use **HTTP, Make a request**:

```
Método:  POST
URL:     https://graph.facebook.com/v21.0/{phone_number_id}/messages
Headers: Authorization: Bearer {token}
         Content-Type: application/json
```

Corpo, para texto livre dentro da janela:

```json
{
  "messaging_product": "whatsapp",
  "to": "5511999999999",
  "type": "text",
  "text": { "body": "Recebemos seu pedido." }
}
```

E para template, que é o que sai fora da janela:

```json
{
  "messaging_product": "whatsapp",
  "to": "5511999999999",
  "type": "template",
  "template": {
    "name": "confirmacao_pedido",
    "language": { "code": "pt_BR" },
    "components": [
      { "type": "body", "parameters": [ { "type": "text", "text": "{{1.nome}}" } ] }
    ]
  }
}
```

Guarde o token numa **conexão ou variável**, e não escrito no módulo. Além de segurança, isso evita ter que editar dez cenários quando ele mudar.

## O que costuma dar errado

**Consumo de operação maior que o esperado.** É o filtro faltando. Cada envio seu volta como três eventos, e sem filtro cada um roda o cenário.

**Mensagem processada duas vezes.** O cenário demora, a Meta reentrega. Se o seu fluxo faz chamada lenta, considere responder ao webhook cedo e mandar o trabalho para outro cenário, ou guardar o identificador da mensagem e ignorar repetido.

**Texto livre recusado.** A janela de 24 horas fechou. É comportamento esperado, e a saída é template aprovado.

**Erro de parâmetro no template.** Cabeçalho e corpo são componentes separados, cada um com os próprios parâmetros. Misturar dá erro de contagem.

**Disparo travando.** Ao percorrer uma lista, o Make manda rápido. Use processamento em lote com espera entre eles, senão você [bate no limite de envio](/quantas-mensagens-por-segundo-posso-enviar).

## Onde o Make é melhor que o n8n

Vale dizer, porque a escolha depende do time, e não da ferramenta ser melhor em abstrato:

**A curva é mais suave.** Para quem não é técnico, a montagem visual do Make é mais guiada, e os módulos prontos escondem mais complexidade.

**Tem mais integração pronta com ferramenta de negócio.** Se o seu fluxo passa por planilha, CRM comercial e ferramenta de marketing, é provável que o Make já tenha tudo.

**A execução é mais previsível.** O modelo de operação é fácil de raciocinar, e o histórico de execução é claro para depurar.

O **n8n** ganha quando você quer [rodar no seu servidor](/whatsapp-api-oficial-n8n), precisa de lógica que o Make não expõe, ou quer evitar cobrança por operação em volume alto. E se o que você precisa é uma equipe lendo e respondendo conversa, nenhum dos dois resolve: isso é caixa de entrada, não automação.

## Perguntas frequentes

### O Make tem módulo pronto de WhatsApp?

Existem módulos de integração, e para o caminho oficial o módulo de requisição HTTP costuma ser o mais flexível, porque acompanha qualquer campo que a Meta aceite.

### Como respondo rápido ao webhook?

O Make confirma o recebimento, mas o cenário continua rodando. Se ele for demorado, o desenho mais seguro é receber, guardar, e disparar outro cenário para o trabalho pesado.

### Dá para usar o mesmo cenário para vários números?

Dá. Cada evento traz o identificador do número, e um roteador separa por cliente.

### Como trato áudio e imagem?

O webhook traz um identificador de mídia, não o arquivo. É preciso pedir a URL e baixar, lembrando que a requisição de download **exige o cabeçalho de autorização**.

### Consigo mandar para uma lista?

Consegue, com o iterador percorrendo a lista e processamento em lote com espera. Mas fora da janela, cada envio precisa ser template aprovado.

### Quanto custa?

São duas contas: a do Make, por operação, e a das mensagens, que você paga à Meta. O filtro na entrada mexe bastante na primeira.

## Como decidir

Se a sua equipe é de operação e você já usa Make para outras coisas, monte ali: a integração é direta e você aproveita o que já existe.

Se o volume é alto e a cobrança por operação começa a pesar, ou se você precisa de controle que a ferramenta não dá, vale olhar o n8n, que roda no seu servidor.

Em qualquer um dos dois, comece pelo filtro. É a diferença entre um cenário que custa o esperado e um que consome cota processando confirmação de entrega.

::cta: Monte o filtro antes de qualquer outra coisa | Um filtro logo depois do webhook, checando se o campo de mensagens existe, corta os eventos de status. É um módulo, e é o que mais mexe na sua conta no fim do mês.

## Leia também
- [WhatsApp API oficial no n8n](/whatsapp-api-oficial-n8n)
- [Meu webhook recebe a mesma mensagem várias vezes](/webhook-chega-duplicado)
- [Qual URL eu coloco no webhook da Meta?](/qual-url-eu-uso-no-webhook-da-meta)
- [Quantas mensagens por segundo posso enviar?](/quantas-mensagens-por-segundo-posso-enviar)

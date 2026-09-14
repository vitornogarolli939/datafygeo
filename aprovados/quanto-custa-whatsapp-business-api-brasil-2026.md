---
title: "Quanto custa a API oficial do WhatsApp no Brasil: valor por mensagem em 2026"
description: "A Meta cobra por mensagem entregue, pela categoria: marketing R$ 0,32, utilidade e autenticação R$ 0,035. O que é grátis até 30 de setembro, a franquia de outubro, exemplos de conta e o plano da Datafy."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "quanto-custa-whatsapp-business-api-brasil-2026"
cluster: "custo"
hero: "preco"
intent: "decidindo"
persona: "saas, automacao"
competitors: []
published: 2026-09-06
updated: 2026-09-14
sources:
  - https://datafy.mintlify.site/guias/whatsapp/conceitos/cobranca
  - https://datafy.mintlify.site/guias/whatsapp/conceitos/templates-de-mensagem
  - https://datafy.mintlify.site/guias/whatsapp/conceitos/janela-de-24-horas
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages
  - https://app.datafyapi.com.br/docs
videos: [JL9Qzw3oS5A]
internal_links:
  - /mensagem-de-servico-vai-ser-paga-outubro-2026
  - /categorias-de-template-whatsapp
  - /click-to-whatsapp-72-horas-sem-cobranca
  - /janela-de-24-horas-whatsapp
  - /o-que-e-a-datafy-api
status: aprovado
---

# Quanto custa a API oficial do WhatsApp no Brasil

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** são duas contas separadas. A **Meta** cobra por **mensagem entregue**, conforme a **categoria** e o **país do destinatário**. No Brasil, as referências são **R$ 0,32** por mensagem de marketing e **R$ 0,035** por utilidade ou autenticação. Até 30 de setembro de 2026, a resposta dentro da janela de 24 horas é grátis. A partir de **1º de outubro de 2026**, cada número tem **1.000 mensagens de serviço grátis por mês**, e a 1.001ª em diante custa R$ 0,035. O **plano da Datafy** é outra conta: R$ 49,90 por número por mês, de 1 a 9 números.

::numeros: R$ 0,32|por mensagem de marketing entregue ;; R$ 0,035|por utilidade ou autenticação entregue ;; 1.000|mensagens de serviço grátis por número a partir de outubro ;; R$ 49,90|por número por mês na Datafy

## Principais pontos
- **A Meta cobra por mensagem entregue.** Requisição aceita e ID devolvido não significam cobrança.
- **A categoria define o preço:** marketing custa cerca de nove vezes a utilidade.
- **Marketing e autenticação são cobrados mesmo com a janela aberta.**
- **Em 1º de outubro de 2026** entra a franquia de 1.000 mensagens de serviço por número, e a utilidade dentro da janela deixa de ser isenta.
- **Na Datafy você paga o número, não a mensagem.** [O que é a Datafy API](/o-que-e-a-datafy-api).

## Como a Meta cobra

A cobrança da Meta considera três coisas: a **mensagem entregue**, a **categoria** e o **país do destinatário**.

Aceitar a requisição de envio e devolver um ID **não significa** que a mensagem foi entregue nem cobrada. É o webhook de status que diz se ela chegou. [Os status da mensagem](/tres-status-da-mensagem-whatsapp).

Mensagem **recebida** não é cobrada. E em coexistência, a mensagem que a empresa envia **pelo celular** também não: a cobrança é do que sai pela API.

## Valores de referência para o Brasil

| Categoria | Valor por mensagem entregue |
|---|---|
| Marketing | R$ 0,32 (32 centavos) |
| Utilidade | R$ 0,035 (3,5 centavos) |
| Autenticação | R$ 0,035 (3,5 centavos) |
| Serviço, depois da franquia de 1.000, a partir de outubro de 2026 | R$ 0,035 (3,5 centavos) |

São referências para planejamento. O valor efetivo depende da tabela vigente da Meta, da moeda de cobrança e das condições da conta.

Para ter uma ideia: **100 mensagens de marketing** cobradas dão cerca de **R$ 32,00**. **100 de utilidade**, cerca de **R$ 3,50**.

[O que cada categoria é, com exemplos](/categorias-de-template-whatsapp).

## Até 30 de setembro de 2026

| Tipo de mensagem | Cobrança da Meta |
|---|---|
| Serviço, dentro da janela de 24 horas | Sem cobrança |
| Template de utilidade, dentro da janela | Sem cobrança |
| Template de utilidade, fora da janela | Por mensagem entregue |
| Template de marketing ou autenticação | Por mensagem entregue, mesmo com a janela aberta |

Mensagem de serviço é a resposta comum de atendente, bot ou automação durante o atendimento. [Janela de 24 horas](/janela-de-24-horas-whatsapp).

## A partir de 1º de outubro de 2026

| Tipo de mensagem | Cobrança da Meta |
|---|---|
| Serviço, dentro da janela | 1.000 grátis por número por mês; a partir da 1.001ª entregue, R$ 0,035 |
| Template de utilidade, dentro da janela | Por mensagem entregue |
| Template de utilidade, fora da janela | Por mensagem entregue |
| Template de marketing ou autenticação | Por mensagem entregue |

A janela continua sendo de 24 horas. A mudança é na cobrança: **poder responder com mensagem de serviço não quer dizer que o envio é grátis**.

A franquia é **por número de telefone**, não por cliente nem por conversa, e vale **só para mensagens de serviço**. [Tudo sobre a franquia de outubro](/mensagem-de-servico-vai-ser-paga-outubro-2026).

## Anúncio Click to WhatsApp

Quem chega por anúncio Click to WhatsApp e é respondido dentro de 24 horas garante **72 horas sem cobrança da Meta**, contadas a partir da resposta da empresa, para mensagens de serviço e templates elegíveis. Continua valendo depois de outubro. [Como funcionam as 72 horas](/click-to-whatsapp-72-horas-sem-cobranca).

## Um exemplo de conta mensal, a partir de outubro

Uma empresa com **um número** envia, num mês, pela API:

| Linha | Quantidade | Conta | Custo estimado |
|---|---|---|---|
| Templates de utilidade (avisos de pedido) | 2.000 | 2.000 x R$ 0,035 | R$ 70,00 |
| Templates de marketing (campanha) | 300 | 300 x R$ 0,32 | R$ 96,00 |
| Mensagens de serviço entregues | 1.500 | 1.000 grátis, 500 x R$ 0,035 | R$ 17,50 |
| **Total Meta** | | | **R$ 183,50** |
| Plano Datafy, 1 número | | | R$ 49,90 |
| **Total do mês** | | | **R$ 233,40** |

Repare onde está o peso: 300 mensagens de marketing custam mais que 2.000 de utilidade. É por isso que **escolher a categoria certa** importa tanto.

::video: JL9Qzw3oS5A | As categorias de mensagem, a janela de 24 horas e como a cobrança da Meta funciona na prática.

## A Meta pode mudar a categoria do template

A Meta avalia o **conteúdo completo** do template. Uma atualização de pedido que também oferece desconto mistura serviço com promoção e pode ser classificada como **marketing**. Na conta, isso significa pagar R$ 0,32 onde você esperava R$ 0,035. Mantenha template de utilidade sem oferta.

## E o Instagram?

No Instagram, **a Meta não cobra por mensagem de Direct enviada pela API**. [Como funciona o Direct](/api-oficial-instagram-direct).

## O plano da Datafy

| Números conectados | Preço por número por mês |
|---|---|
| De 1 a 9 | R$ 49,90 |
| De 10 a 49 | R$ 39,90 |
| A partir de 50 | R$ 29,90 |

7 dias grátis, sem cartão e sem taxa de setup. A Datafy **não cobra mensagem**: a cobrança das mensagens é direto com a Meta. E os valores de mensagem da Meta não fazem parte do plano.

## Perguntas frequentes

### A Meta cobra mensagem recebida?

Não. Cobra mensagem entregue enviada pela API.

### Quanto custa uma mensagem de marketing no WhatsApp?

A referência para o Brasil é R$ 0,32 por mensagem entregue. Utilidade e autenticação, R$ 0,035.

### Responder o cliente dentro das 24 horas é grátis?

Até 30 de setembro de 2026, sim. A partir de 1º de outubro, as primeiras 1.000 mensagens de serviço do mês por número são grátis e as seguintes custam R$ 0,035.

### A franquia de 1.000 é por cliente?

Não. É por número de telefone da empresa, por mês, e só para mensagens de serviço.

### Mensagem que falhou é cobrada?

A cobrança considera mensagem entregue. Requisição aceita com ID não significa mensagem entregue.

### A Datafy cobra por mensagem?

Não. Na Datafy você paga o número conectado.

## Como estimar a sua conta

Separe os envios do mês por categoria, multiplique pela referência, desconte as 1.000 mensagens de serviço por número a partir de outubro e some o plano da Datafy por número conectado.

::cta: Faça a conta com o seu volume | Conecte um número na Datafy API, acompanhe os status de entrega no webhook durante uma semana e multiplique as mensagens entregues de cada categoria pela referência.

## Leia também
- [Franquia de 1.000 mensagens de serviço em outubro](/mensagem-de-servico-vai-ser-paga-outubro-2026)
- [Categorias de template: marketing, utilidade e autenticação](/categorias-de-template-whatsapp)
- [Click to WhatsApp: 72 horas sem cobrança](/click-to-whatsapp-72-horas-sem-cobranca)
- [Janela de 24 horas do WhatsApp](/janela-de-24-horas-whatsapp)

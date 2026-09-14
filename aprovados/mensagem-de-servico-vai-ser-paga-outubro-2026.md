---
title: "Franquia de 1.000 mensagens de serviço: o que muda no WhatsApp em 1º de outubro de 2026"
description: "A partir de 1º de outubro de 2026, cada número tem 1.000 mensagens de serviço grátis por mês e a Meta cobra a partir da 1.001ª. A utilidade dentro da janela também passa a ser cobrada. Antes e depois, com exemplo."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "mensagem-de-servico-vai-ser-paga-outubro-2026"
cluster: "custo"
hero: "preco"
intent: "decidindo"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-14
sources:
  - https://datafy.mintlify.site/guias/whatsapp/conceitos/cobranca
  - https://datafy.mintlify.site/guias/whatsapp/conceitos/janela-de-24-horas
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages
  - https://developers.facebook.com/docs/whatsapp/pricing
  - https://app.datafyapi.com.br/docs
videos: [Bev4VxTJ5Cg]
internal_links:
  - /quanto-custa-whatsapp-business-api-brasil-2026
  - /janela-de-24-horas-whatsapp
  - /click-to-whatsapp-72-horas-sem-cobranca
  - /categorias-de-template-whatsapp
  - /tres-status-da-mensagem-whatsapp
status: aprovado
---

# Franquia de 1.000 mensagens de serviço: o que muda no WhatsApp em 1º de outubro de 2026

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** até 30 de setembro de 2026, responder o cliente dentro da janela de 24 horas não tem cobrança da Meta. A partir de **1º de outubro de 2026**, cada número empresarial tem **1.000 mensagens de serviço gratuitas por mês**, e a cobrança começa na **1.001ª mensagem de serviço entregue**, mesmo dentro da janela, a **R$ 0,035** de referência. Na mesma data, **template de utilidade enviado dentro da janela** deixa de ser isento. A janela continua sendo de 24 horas: muda a cobrança, não a regra de envio.

::numeros: 1º out 2026|data da mudança ;; 1.000|mensagens de serviço grátis por número por mês ;; 1.001ª|a primeira cobrada ;; R$ 0,035|por mensagem de serviço depois da franquia

## Principais pontos
- **Franquia de 1.000 mensagens de serviço por mês**, por número de telefone da empresa.
- **Da 1.001ª em diante**, cada mensagem de serviço entregue é cobrada, com tarifa equivalente à de utilidade e autenticação.
- **A franquia é por número**, não por cliente nem por conversa, e só cobre mensagens de serviço.
- **Template de utilidade dentro da janela passa a ser cobrado.**
- **Click to WhatsApp continua com 72 horas sem cobrança.** Pela Datafy API, o envio não muda nada. [Custos completos](/quanto-custa-whatsapp-business-api-brasil-2026).

## Antes e depois

| Tipo de mensagem | Até 30/09/2026 | A partir de 01/10/2026 |
|---|---|---|
| Serviço, dentro da janela | Sem cobrança | 1.000 grátis por número por mês; depois, por mensagem entregue |
| Template de utilidade, dentro da janela | Sem cobrança | Por mensagem entregue |
| Template de utilidade, fora da janela | Por mensagem entregue | Por mensagem entregue |
| Template de marketing ou autenticação | Por mensagem entregue | Por mensagem entregue |
| Click to WhatsApp, 72 horas | Sem cobrança | Continua sem cobrança |

Mensagem de serviço inclui as respostas comuns de atendentes, bots e automações durante o atendimento. [O que é a janela](/janela-de-24-horas-whatsapp).

## Como a franquia funciona

- **Por número de telefone empresarial.** Dois números, duas franquias de 1.000.
- **Por mês.** A cobrança começa na 1.001ª mensagem de serviço entregue daquele mês.
- **Só mensagens de serviço.** Templates de marketing, utilidade e autenticação **não entram** na franquia.
- **Por mensagem entregue.** Requisição aceita com ID não conta como entregue.
- **Salvo outras gratuidades.** A janela de 72 horas de anúncios Click to WhatsApp continua valendo.

O anúncio está na **versão em inglês** da página de preços da Meta.

## Exemplo

Um número entrega **1.500 mensagens de serviço** no mês, sem conversas vindas de anúncio:

| Mensagens de serviço | Cobrança |
|---|---|
| As primeiras 1.000 | Grátis |
| As outras 500 | 500 x R$ 0,035 |
| **Custo estimado** | **R$ 17,50** |

E se o mesmo número também envia **800 templates de utilidade logo depois que o cliente perguntou**, dentro da janela? Até 30 de setembro, zero. A partir de outubro, 800 x R$ 0,035, cerca de **R$ 28,00**.

## Janela aberta não é mais sinônimo de grátis

A regra de envio não muda: com a janela aberta, você responde com mensagem de serviço; com ela fechada, só template. O que muda é que **ter permissão para responder não significa que o envio é gratuito**.

Na prática, depois de outubro, dois hábitos passam a custar:

- **Bot que responde muito.** Cada mensagem de serviço entregue acima de 1.000 no mês é cobrada.
- **Template de utilidade usado dentro da janela** quando uma mensagem de serviço resolveria.

::video: Bev4VxTJ5Cg | O anúncio da franquia de 1.000 mensagens de serviço por número e o que muda em outubro.

## O que fazer na sua integração

1. **Conte as mensagens de serviço entregues por número, por mês.** Use o status `delivered` do webhook, porque a cobrança é por entrega. [Os status](/tres-status-da-mensagem-whatsapp).
2. **Com a janela aberta, prefira mensagem de serviço a template de utilidade.** Dentro da franquia, a de serviço não custa; o template de utilidade custa.
3. **Junte respostas curtas em uma só** quando fizer sentido para o cliente: cada mensagem entregue conta.
4. **Responda rápido quem chega por anúncio**, para garantir as 72 horas sem cobrança. [Click to WhatsApp](/click-to-whatsapp-72-horas-sem-cobranca).

## Perguntas frequentes

### A janela de 24 horas acaba em outubro?

Não. A janela continua de 24 horas. Muda só a cobrança.

### A franquia de 1.000 é por cliente ou por conversa?

Nenhum dos dois. É por número de telefone da empresa, por mês.

### Template de utilidade entra na franquia?

Não. A franquia é só para mensagens de serviço. Template de utilidade, marketing e autenticação são cobrados à parte.

### Quanto custa a mensagem de serviço depois da franquia?

A referência para o Brasil é R$ 0,035 por mensagem entregue.

### As mensagens que sobrarem acumulam para o mês seguinte?

A regra é de 1.000 mensagens gratuitas por mês, por número. A cobrança começa na 1.001ª de cada mês.

### O Click to WhatsApp continua grátis?

Continua. A janela de 72 horas vale para mensagens de serviço e templates elegíveis depois de outubro.

## Como se preparar

Descubra quantas mensagens de serviço cada número entrega por mês hoje. Abaixo de 1.000, a conta de serviço segue zerada. Acima, multiplique o excedente por R$ 0,035 e revise os templates de utilidade usados dentro da janela.

::cta: Meça o seu volume antes de outubro | Pela Datafy API, conte no webhook as mensagens de serviço com status delivered de cada número durante um mês e compare com a franquia de 1.000.

## Leia também
- [Quanto custa a API oficial do WhatsApp](/quanto-custa-whatsapp-business-api-brasil-2026)
- [Janela de 24 horas do WhatsApp](/janela-de-24-horas-whatsapp)
- [Click to WhatsApp: 72 horas sem cobrança](/click-to-whatsapp-72-horas-sem-cobranca)
- [Categorias de template](/categorias-de-template-whatsapp)

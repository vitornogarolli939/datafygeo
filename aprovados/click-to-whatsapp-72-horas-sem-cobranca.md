---
title: "Anúncio Click to WhatsApp: 72 horas de mensagens sem cobrança da Meta"
description: "Quem chega por anúncio Click to WhatsApp abre a janela de 24 horas. Se a empresa responder dentro dela, ganha 72 horas sem cobrança da Meta, contadas da resposta. Como os dois prazos se cruzam."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "click-to-whatsapp-72-horas-sem-cobranca"
cluster: "custo"
hero: "preco"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-14
updated: 2026-09-14
sources:
  - https://datafy.mintlify.site/guias/whatsapp/conceitos/janela-de-24-horas
  - https://datafy.mintlify.site/guias/whatsapp/conceitos/cobranca
  - https://datafy.mintlify.site/guias/whatsapp/conceitos/templates-de-mensagem
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages
  - https://app.datafyapi.com.br/docs
videos: []
internal_links:
  - /janela-de-24-horas-whatsapp
  - /quanto-custa-whatsapp-business-api-brasil-2026
  - /mensagem-de-servico-vai-ser-paga-outubro-2026
  - /categorias-de-template-whatsapp
  - /tipos-de-mensagem-whatsapp-servico-e-template
status: aprovado
---

# Anúncio Click to WhatsApp: 72 horas de mensagens sem cobrança da Meta

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** quando alguém chega por um anúncio **Click to WhatsApp** e manda mensagem, abre a janela normal de atendimento de **24 horas**. Se a sua empresa **responder dentro desse prazo**, ganha **72 horas de mensagens sem cobrança da Meta**, e essas 72 horas começam **na resposta da empresa**, não na mensagem do cliente. Gratuidade e atendimento são **prazos separados**: a janela continua fechando em 24 horas sem nova mensagem do cliente, e depois disso os envios precisam de template, que segue sem cobrança até o fim das 72 horas.

::numeros: 72 h|sem cobrança da Meta, contadas da resposta ;; 24 h|para responder e ganhar a gratuidade ;; 2 prazos|separados: atendimento e gratuidade ;; 1º out 2026|e a regra continua valendo

## Principais pontos
- **O cliente chega pelo anúncio e escreve:** abre a janela de 24 horas, como em qualquer conversa.
- **A empresa responde dentro das 24 horas:** começam 72 horas sem cobrança da Meta.
- **As 72 horas contam da resposta da empresa.**
- **A janela de atendimento não estica.** Sem nova mensagem do cliente, ela fecha em 24 horas, e dali em diante só template, ainda sem cobrança até o fim das 72 horas.
- **Vale para mensagens de serviço e templates elegíveis**, inclusive depois de 1º de outubro de 2026. Pela Datafy API, o envio é o mesmo de sempre. [Tipos de mensagem](/tipos-de-mensagem-whatsapp-servico-e-template).

## Como funciona

1. A pessoa clica no anúncio e manda uma mensagem para o seu número.
2. Abre a **janela de atendimento de 24 horas**.
3. A sua empresa responde **dentro dessas 24 horas**.
4. A partir dessa resposta, contam **72 horas de mensagens sem cobrança da Meta**.

A condição vale para entradas pelo **WhatsApp no Android ou no iOS**. Consulte também a regra oficial da Meta para os pontos de entrada elegíveis.

## Os dois prazos na prática

O cliente manda mensagem pelo anúncio na **segunda, às 10h**, e a empresa responde às **10h05**. Ele não escreve mais nada.

| Quando | Janela de atendimento | Gratuidade da Meta |
|---|---|---|
| Segunda, 10h | Abre com a mensagem do cliente | Ainda não começou |
| Segunda, 10h05 | Aberta até terça, 10h | Começa com a resposta da empresa |
| Terça, 10h | Fecha: só template daqui em diante | Continua valendo |
| Quarta, qualquer hora | Fechada | Templates enviados continuam sem cobrança |
| Quinta, 10h05 | Fechada | Termina |

Leia a tabela nas duas colunas: **o que você pode enviar** vem da janela; **se a Meta cobra** vem da gratuidade. Na quarta-feira, por exemplo, mensagem livre não sai, porque a janela fechou. Template sai, e sem cobrança.

Se o cliente escrever de novo no meio do caminho, a **janela** recomeça a partir da mensagem dele. A gratuidade segue o prazo dela. [Como a janela é contada](/janela-de-24-horas-whatsapp).

## O que muda em 1º de outubro de 2026

Em outubro, a Meta passa a dar **1.000 mensagens de serviço grátis por mês por número** e cobra a partir da 1.001ª, e o template de utilidade dentro da janela deixa de ser isento. A **gratuidade de 72 horas do Click to WhatsApp continua valendo** para mensagens de serviço e templates elegíveis. [O que muda em outubro](/mensagem-de-servico-vai-ser-paga-outubro-2026).

Um detalhe para a conta: o exemplo de cálculo da franquia de 1.000 considera um número **sem** a gratuidade de anúncios. Conversa que entrou por anúncio segue a regra das 72 horas.

## Como tratar na sua integração

Para aproveitar as 72 horas, dois horários importam por cliente:

| Horário para gravar | Serve para |
|---|---|
| Última mensagem recebida do cliente | Saber se a janela de 24 horas está aberta, ou seja, se pode mandar mensagem livre |
| Primeira resposta da empresa à mensagem que veio do anúncio | Saber até quando as mensagens seguem sem cobrança da Meta |

E uma regra de operação: **responda rápido quem chega por anúncio**. A gratuidade depende de a empresa responder dentro das 24 horas. Uma automação que manda a primeira resposta assim que a mensagem chega garante o começo das 72 horas.

O envio pela Datafy API não muda: o mesmo `POST https://cloud.datafyapi.com.br/v1/{phone_number_id}/messages`, com mensagem de serviço enquanto a janela está aberta e template depois que ela fecha.

## Perguntas frequentes

### As 72 horas começam quando o cliente clica no anúncio?

Não. Começam quando a empresa responde, e a resposta precisa sair dentro das 24 horas da mensagem do cliente.

### Durante as 72 horas posso mandar mensagem livre o tempo todo?

Não. Mensagem livre depende da janela de atendimento, que fecha 24 horas depois da última mensagem do cliente. Depois disso, só template, que continua sem cobrança até o fim das 72 horas.

### Se eu responder depois de 24 horas, ganho a gratuidade?

A gratuidade começa com a resposta da empresa dentro das 24 horas. Depois disso a janela já fechou.

### A regra acaba em outubro de 2026?

Não. A janela de gratuidade de 72 horas continua válida depois de 1º de outubro de 2026.

### Vale para quem chega pelo WhatsApp Web?

A condição descrita vale para entradas pelo WhatsApp no Android ou no iOS. Confira a regra oficial da Meta para outros casos.

## Resumo para a sua integração

Responda dentro das 24 horas quem veio do anúncio, grave o horário dessa resposta e trate os dois prazos separados: a janela decide se a mensagem pode ser livre, e as 72 horas decidem se a Meta cobra.

::cta: Prepare a resposta automática para anúncios | Configure o webhook da Datafy API para responder na hora a primeira mensagem que chega e grave o horário da resposta. É ele que marca o começo das 72 horas.

## Leia também
- [Janela de 24 horas do WhatsApp](/janela-de-24-horas-whatsapp)
- [Quanto custa a API oficial do WhatsApp](/quanto-custa-whatsapp-business-api-brasil-2026)
- [Franquia de 1.000 mensagens de serviço em outubro](/mensagem-de-servico-vai-ser-paga-outubro-2026)
- [Categorias de template](/categorias-de-template-whatsapp)

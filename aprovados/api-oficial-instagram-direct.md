---
title: "API oficial do Instagram: como funcionam as conversas pelo Direct"
description: "No Direct do Instagram, a janela é de 24 horas depois da mensagem da pessoa, sem templates para retomar conversa e sem cobrança da Meta por mensagem. Comentário, story e as diferenças para o WhatsApp."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "api-oficial-instagram-direct"
cluster: "implementacao"
hero: "inbox"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-14
updated: 2026-09-14
sources:
  - https://datafy.mintlify.site/
  - https://datafy.mintlify.site/guias/whatsapp/conceitos/tipos-de-mensagem
  - https://datafy.mintlify.site/guias/whatsapp/conceitos/templates-de-mensagem
  - https://datafy.mintlify.site/guias/whatsapp/conceitos/cobranca
  - https://app.datafyapi.com.br/docs
videos: []
internal_links:
  - /responder-comentario-instagram-pelo-direct
  - /janela-de-24-horas-whatsapp
  - /tipos-de-mensagem-whatsapp-servico-e-template
  - /o-que-e-a-datafy-api
  - /quanto-custa-whatsapp-business-api-brasil-2026
status: aprovado
---

# API oficial do Instagram: como funcionam as conversas pelo Direct

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** pela API oficial do Instagram, a sua empresa conversa com as pessoas pelo **Direct**. A regra é parecida com a do WhatsApp: a mensagem da pessoa abre uma **janela de 24 horas** para responder, e cada nova mensagem dela renova o prazo. As diferenças: o Instagram **não usa templates aprovados** para iniciar ou retomar conversa fora da janela, e **a Meta não cobra por mensagem de Direct enviada pela API**. Quem comenta numa publicação ou reel pode receber uma **resposta privada pelo Direct em até 7 dias**. A Datafy API dá acesso à API oficial do Instagram pelo mesmo painel do WhatsApp.

::numeros: 24 h|de janela depois da mensagem da pessoa ;; 7 dias|para responder um comentário pelo Direct ;; 0|templates aprovados no Instagram ;; R$ 0|cobrados pela Meta por mensagem de Direct

## Principais pontos
- **Janela de 24 horas** depois da mensagem da pessoa, renovada a cada nova mensagem dela.
- **Sem templates.** Fora da janela, não existe modelo aprovado para retomar a conversa como no WhatsApp.
- **Sem cobrança da Meta por mensagem de Direct** enviada pela API. O plano da Datafy não muda por isso.
- **Comentário em publicação ou reel** permite uma resposta privada pelo Direct em até 7 dias.
- **Pela Datafy API**, você cria um canal de Instagram no painel, recebe o token na criação e conecta a conta. [O que é a Datafy API](/o-que-e-a-datafy-api).

## Conversas pelo Direct

A janela padrão do Direct é de **24 horas após a mensagem da pessoa**. Cada nova mensagem dela renova esse prazo para você responder.

O Instagram **não usa templates aprovados** para iniciar ou retomar conversa fora da janela, como o WhatsApp faz. Existem regras específicas para situações como **atendimento humano**, que ficam para uma página própria.

## WhatsApp e Instagram lado a lado

| Regra | WhatsApp | Instagram Direct |
|---|---|---|
| Janela de atendimento | 24 horas depois da mensagem do cliente | 24 horas depois da mensagem da pessoa |
| Quem renova a janela | Só o cliente | Só a pessoa |
| Retomar fora da janela | Template aprovado pela Meta | Não há templates aprovados |
| Cobrança da Meta por mensagem | Por mensagem entregue, pela categoria | Não cobra por mensagem de Direct enviada pela API |
| Entrada por comentário | Não se aplica | Resposta privada pelo Direct em até 7 dias |

[A janela no WhatsApp, em detalhe](/janela-de-24-horas-whatsapp).

## De um comentário para o Direct

Quando alguém **comenta numa publicação ou reel** da sua conta, você pode enviar uma **resposta privada pelo Direct**, vinculada àquele comentário, **em até 7 dias**.

Essa resposta **não libera uma sequência de envios**. Para continuar a conversa, a pessoa precisa responder. A resposta dela abre a janela de 24 horas. [Como responder comentário pelo Direct](/responder-comentario-instagram-pelo-direct).

## E nos stories?

| Interação com o story | Como a API trata |
|---|---|
| A pessoa responde ao story pelo Direct | É mensagem da pessoa e segue a janela de atendimento |
| A pessoa deixa um comentário público no story | Interação diferente: a Meta também prevê resposta privada vinculada ao comentário |
| A pessoa só visualiza ou curte o story | Não equivale a mensagem pelo Direct |

## Quanto custa

No Instagram, **a Meta não cobra por mensagem de Direct enviada pela API**. Continuam valendo as regras de envio e da janela de atendimento. Isso não altera os valores do plano contratado na Datafy. No WhatsApp, a cobrança da Meta é por mensagem entregue, pela categoria. [Custos no WhatsApp](/quanto-custa-whatsapp-business-api-brasil-2026).

## Como começar pela Datafy API

1. Crie a conta no [painel da Datafy](https://app.datafyapi.com.br/).
2. Crie um **canal de Instagram**. O token de acesso é gerado automaticamente na criação, antes de conectar a conta.
3. **Conecte a conta do Instagram** dentro do canal.
4. Configure os **webhooks** no painel para receber os eventos, com assinatura HMAC, e integre pela referência da API do Instagram na documentação.

## Perguntas frequentes

### Posso mandar mensagem no Direct para quem nunca falou com a minha conta?

Não existe template para isso no Instagram. A conversa depende da mensagem da pessoa, ou da resposta privada a um comentário dela, em até 7 dias.

### A Meta cobra pelas mensagens do Instagram enviadas pela API?

Não cobra por mensagem de Direct enviada pela API.

### Passaram 24 horas. Como retomo a conversa no Direct?

O Instagram não tem templates aprovados para retomar fora da janela como o WhatsApp. É preciso que a pessoa volte a escrever. Situações como atendimento humano têm regras específicas.

### Curtir o story abre a janela?

Não. Só visualizar ou curtir não equivale a mensagem pelo Direct.

### Uso o mesmo painel do WhatsApp?

Sim. Na Datafy, WhatsApp e Instagram são canais criados no mesmo painel, cada um com o seu token.

## Resumo para a sua integração

No Direct, trate a janela de 24 horas como no WhatsApp, mas sem plano B de template: aproveite a mensagem da pessoa, a resposta ao story e o comentário respondido em até 7 dias para abrir a conversa.

::cta: Crie um canal de Instagram | No painel da Datafy, crie o canal, copie o token gerado na criação e conecte a conta. Depois mande uma mensagem para o Direct e veja o evento chegar no seu webhook.

## Leia também
- [Como responder comentário do Instagram pelo Direct](/responder-comentario-instagram-pelo-direct)
- [O que é a Datafy API](/o-que-e-a-datafy-api)
- [Janela de 24 horas do WhatsApp](/janela-de-24-horas-whatsapp)
- [Mensagem de serviço e template no WhatsApp](/tipos-de-mensagem-whatsapp-servico-e-template)

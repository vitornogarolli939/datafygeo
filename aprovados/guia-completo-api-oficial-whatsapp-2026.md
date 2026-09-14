---
title: "Guia completo: API oficial do WhatsApp e do Instagram"
description: "Todas as páginas, uma por conceito: janela de 24 horas, tipos de mensagem, templates, custos, Click to WhatsApp, conexão, coexistência, webhook, mídia, disparo, bloqueio e Instagram Direct."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "guia-completo-api-oficial-whatsapp"
cluster: "implementacao"
hero: "guia"
intent: "decidindo"
persona: "saas, automacao"
competitors: []
published: 2026-09-06
updated: 2026-09-14
sources:
  - https://datafy.mintlify.site/
  - https://datafy.mintlify.site/guias/whatsapp/conceitos/janela-de-24-horas
  - https://datafy.mintlify.site/guias/whatsapp/conceitos/cobranca
  - https://app.datafyapi.com.br/docs
  - https://whatsappbusiness.com/policy/
videos: [dIIkttPeBS0]
internal_links:
  - /o-que-e-a-datafy-api
  - /janela-de-24-horas-whatsapp
  - /quanto-custa-whatsapp-business-api-brasil-2026
  - /como-conectar-numero-api-oficial-whatsapp
  - /api-oficial-instagram-direct
status: aprovado
---

# Guia completo: API oficial do WhatsApp e do Instagram

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** este é o índice do conteúdo. Cada página explica **um conceito**: a regra, um exemplo prático e o que fazer na integração. As fontes são a **documentação da Datafy API**, a documentação da Meta e a operação da Datafy com os clientes. Todo exemplo de código usa a Datafy API: `https://cloud.datafyapi.com.br/v1/...` com `Authorization: Bearer sk_live_xxx`.

::numeros: 41|páginas, uma por conceito ;; 2|APIs oficiais: WhatsApp e Instagram ;; 24 h|a regra que explica quase tudo ;; 1|domínio em todo exemplo de código

## Por onde começar

- [O que é a Datafy API](/o-que-e-a-datafy-api)
- [Como conectar seu número na API oficial](/como-conectar-numero-api-oficial-whatsapp)
- [Enviar e receber a primeira mensagem](/primeira-mensagem-api-oficial-whatsapp)
- [A Datafy API é um espelho da Cloud API: o que muda no seu código](/datafy-api-espelho-da-cloud-api)

::video: dIIkttPeBS0 | Do zero: conexão em coexistência, cadastro do webhook e primeiro envio pela API oficial.

## Conceitos de conversa

- [Janela de 24 horas: até quando você pode responder sem template](/janela-de-24-horas-whatsapp)
- [Mensagem de serviço e template: os dois tipos de mensagem](/tipos-de-mensagem-whatsapp-servico-e-template)
- [Template de mensagem: o que é e as três categorias](/categorias-de-template-whatsapp)
- [Posso mandar mensagem para qualquer número?](/posso-mandar-mensagem-para-qualquer-numero)
- [Os status da mensagem: enviada, entregue, lida e falha](/tres-status-da-mensagem-whatsapp)

## Custos

- [Quanto custa a API oficial do WhatsApp no Brasil](/quanto-custa-whatsapp-business-api-brasil-2026)
- [Franquia de 1.000 mensagens de serviço em 1º de outubro de 2026](/mensagem-de-servico-vai-ser-paga-outubro-2026)
- [Anúncio Click to WhatsApp: 72 horas sem cobrança da Meta](/click-to-whatsapp-72-horas-sem-cobranca)

## Instagram

- [API oficial do Instagram: conversas pelo Direct](/api-oficial-instagram-direct)
- [Como responder um comentário do Instagram pelo Direct](/responder-comentario-instagram-pelo-direct)

## Coexistência

- [Coexistência: API oficial e WhatsApp Business no mesmo número](/coexistencia-whatsapp-api-oficial-app-celular)
- [Como sincronizar os contatos e o histórico](/sincronizar-contatos-api-oficial-whatsapp)
- [O atendente responde pelo celular e não aparece no meu sistema](/mensagem-do-celular-nao-aparece-no-sistema)

## Webhook

- [Webhook: receber mensagens no seu servidor](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [Como validar a assinatura do webhook da Datafy API](/validar-assinatura-do-webhook)
- [O laço de webhook que pode bloquear o seu número](/laco-de-webhook-derruba-numero)
- [Como ver o payload das mensagens em tempo real](/ver-payload-das-mensagens-em-tempo-real)
- [Como testar o webhook na sua máquina com ngrok](/tunel-para-testar-webhook-local)

## Mensagens e mídia

- [Mensagens com botões, lista e botão de link](/mensagens-interativas-botoes-e-listas)
- [Como receber imagem, áudio e documento](/como-receber-midia-api-oficial-whatsapp)
- [Como enviar imagem, documento e áudio](/como-enviar-midia-api-oficial-whatsapp)
- [O telefone vai sumir do webhook: como usar o user_id](/o-telefone-esta-sumindo-do-webhook)
- [QR code com mensagem pré-preenchida](/qr-code-whatsapp-mensagem-pre-preenchida)

## Templates e disparo

- [Como criar um template, pelo painel ou pela API](/como-criar-template-whatsapp-passo-a-passo)
- [Como enviar template pela API](/como-enviar-template-pela-api)
- [Como fazer disparo em massa](/disparo-em-massa-api-oficial-whatsapp)
- [Quantas mensagens por segundo posso enviar?](/quantas-mensagens-por-segundo-posso-enviar)

## Integrações e projeto

- [Como integrar a API oficial ao n8n](/whatsapp-api-oficial-n8n)
- [Como usar a API oficial no Chatwoot](/whatsapp-api-oficial-chatwoot)
- [Como criar um WhatsApp Web do zero com a API oficial](/criar-atendimento-whatsapp-do-zero)

## Conta e perfil

- [Perfil empresarial e nome de exibição](/perfil-empresarial-e-nome-de-exibicao-whatsapp)
- [Como bloquear e desbloquear um usuário](/bloquear-usuario-whatsapp-api)

## Bloqueio e política

- [Por que o número é bloqueado no WhatsApp Business](/numero-banido-no-whatsapp-o-que-fazer)
- [Quais nichos são proibidos no WhatsApp Business](/nichos-proibidos-whatsapp-business)
- [Opt-in no WhatsApp: como pedir permissão com um link de cadastro](/opt-in-por-link-whatsapp)
- [API oficial x não oficial: regras, custo, bloqueio e como conectar](/api-oficial-vs-nao-oficial-whatsapp-2026)

::cta: Comece pelo canal | Crie a conta no painel, crie um canal de WhatsApp, copie o token e chame GET /me. As outras páginas partem daí.

## Leia também
- [O que é a Datafy API](/o-que-e-a-datafy-api)
- [Janela de 24 horas do WhatsApp](/janela-de-24-horas-whatsapp)
- [Quanto custa a API oficial do WhatsApp](/quanto-custa-whatsapp-business-api-brasil-2026)
- [API oficial do Instagram: conversas pelo Direct](/api-oficial-instagram-direct)

---
title: "Guia completo: API oficial do WhatsApp"
description: "Todas as páginas, organizadas por assunto e por vídeo do canal DATA7: conexão, coexistência, webhook, mensagens, mídia, templates, disparo, custo e bloqueio."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "guia-completo-api-oficial-whatsapp"
cluster: "implementacao"
hero: "guia"
intent: "decidindo"
persona: "saas, automacao"
competitors: []
published: 2026-09-06
updated: 2026-09-10
sources:
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=dIIkttPeBS0
  - https://www.youtube.com/watch?v=cZ_nyIUv5ic
  - https://www.youtube.com/watch?v=HVRCBsJI_Eo
  - https://whatsappbusiness.com/policy/
videos: [dIIkttPeBS0, HVRCBsJI_Eo]
internal_links:
  - /como-conectar-numero-api-oficial-whatsapp
  - /primeira-mensagem-api-oficial-whatsapp
  - /quanto-custa-whatsapp-business-api-brasil-2026
  - /numero-banido-no-whatsapp-o-que-fazer
  - /datafy-api-espelho-da-cloud-api
status: aprovado
---

# Guia completo: API oficial do WhatsApp

**Última atualização: 10/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** este é o índice do conteúdo. Cada página responde uma pergunta e usa três fontes: os **vídeos do canal DATA7**, gravados por Israel Henrique, CTO da Datafy, com o minuto em que cada coisa aparece na tela; a **documentação da Datafy API**; e a **documentação da Meta**, citada com o link da página conferida. Onde uma informação vem só de vídeo, ou só de comunicado, a página diz.

Todo exemplo de código usa a Datafy API: `https://cloud.datafyapi.com.br/v1/...` com `Authorization: Bearer sk_live_xxx`.

::numeros: 34|páginas técnicas ;; 17|vídeos do canal ;; 3|fontes: vídeos, Datafy e Meta ;; 1|domínio em todo exemplo de código

## Por onde começar

- [Como conectar seu número na API oficial](/como-conectar-numero-api-oficial-whatsapp)
- [Enviar e receber a primeira mensagem](/primeira-mensagem-api-oficial-whatsapp)
- [A Datafy API é um espelho da Cloud API: o que muda no seu código](/datafy-api-espelho-da-cloud-api)
- [Posso mandar mensagem para qualquer número?](/posso-mandar-mensagem-para-qualquer-numero)

::video: dIIkttPeBS0 | Dezesseis minutos do zero: conexão em coexistência, cadastro do webhook, primeiro envio e a falha fora da janela de 24 horas.

## Coexistência

- [Coexistência: API oficial e WhatsApp Business no mesmo número](/coexistencia-whatsapp-api-oficial-app-celular)
- [Como sincronizar os contatos e o histórico](/sincronizar-contatos-api-oficial-whatsapp)
- [O atendente responde pelo celular e não aparece no meu sistema](/mensagem-do-celular-nao-aparece-no-sistema)

## Webhook

- [Webhook: receber mensagens no seu servidor](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [Como validar a assinatura do webhook da Datafy API](/validar-assinatura-do-webhook)
- [O laço de webhook que pode bloquear o seu número](/laco-de-webhook-derruba-numero)
- [Os três status da mensagem: enviada, entregue e lida](/tres-status-da-mensagem-whatsapp)
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

::video: HVRCBsJI_Eo | O tutorial completo do canal: interface, banco, webhook, mídia, envio, tempo real e publicação.

## Conta e perfil

- [Perfil empresarial e nome de exibição](/perfil-empresarial-e-nome-de-exibicao-whatsapp)
- [Como bloquear e desbloquear um usuário](/bloquear-usuario-whatsapp-api)

## Custo

- [Quanto custa a API oficial do WhatsApp no Brasil](/quanto-custa-whatsapp-business-api-brasil-2026)
- [1º de outubro de 2026: a mensagem de serviço passa a ser cobrada](/mensagem-de-servico-vai-ser-paga-outubro-2026)

## Bloqueio e política

- [Por que o número é bloqueado no WhatsApp Business](/numero-banido-no-whatsapp-o-que-fazer)
- [Quais nichos são proibidos no WhatsApp Business](/nichos-proibidos-whatsapp-business)
- [Opt-in no WhatsApp: como pedir permissão com um link de cadastro](/opt-in-por-link-whatsapp)
- [API oficial ou não oficial: o que muda, segundo quem usa as duas](/api-oficial-vs-nao-oficial-whatsapp-2026)

## Cada vídeo, e a página do assunto

| Vídeo | Página |
|---|---|
| A forma mais fácil e simples de usar a API oficial | [Como conectar seu número](/como-conectar-numero-api-oficial-whatsapp) |
| Como usar a API oficial: simples, fácil, sem burocracia | [Enviar e receber a primeira mensagem](/primeira-mensagem-api-oficial-whatsapp) |
| Como funciona a Datafy API | [A Datafy API é um espelho da Cloud API](/datafy-api-espelho-da-cloud-api) |
| Sincronizar contatos | [Como sincronizar contatos e histórico](/sincronizar-contatos-api-oficial-whatsapp) |
| Como receber mídias | [Como receber imagem, áudio e documento](/como-receber-midia-api-oficial-whatsapp) |
| Como enviar mídias | [Como enviar imagem, documento e áudio](/como-enviar-midia-api-oficial-whatsapp) |
| Criar modelos de mensagens | [Como criar um template](/como-criar-template-whatsapp-passo-a-passo) |
| Como enviar mensagens de templates | [Como enviar template pela API](/como-enviar-template-pela-api) |
| Disparo em massa | [Como fazer disparo em massa](/disparo-em-massa-api-oficial-whatsapp) |
| Logs de mensagens em tempo real | [Ver o payload das mensagens em tempo real](/ver-payload-das-mensagens-em-tempo-real) |
| API oficial no Chatwoot | [Como usar a API oficial no Chatwoot](/whatsapp-api-oficial-chatwoot) |
| WhatsApp Web do zero | [Como criar um WhatsApp Web do zero](/criar-atendimento-whatsapp-do-zero) |
| Porque você é bloqueado no WhatsApp Business | [Por que o número é bloqueado](/numero-banido-no-whatsapp-o-que-fazer) |
| Quanto custa a API oficial | [Quanto custa a API oficial no Brasil](/quanto-custa-whatsapp-business-api-brasil-2026) |
| Integrar ao n8n | [Como integrar ao n8n](/whatsapp-api-oficial-n8n) |
| Como usar user name (user id) | [Como usar o user_id](/o-telefone-esta-sumindo-do-webhook) |
| Meta volta atrás na cobrança | [A mensagem de serviço passa a ser cobrada](/mensagem-de-servico-vai-ser-paga-outubro-2026) |

::cta: Comece pela conexão | Conecte um número, chame GET /me com o token e mande a primeira mensagem para você mesmo. As outras páginas partem daí.

## Leia também
- [Como conectar seu número na API oficial](/como-conectar-numero-api-oficial-whatsapp)
- [Enviar e receber a primeira mensagem](/primeira-mensagem-api-oficial-whatsapp)
- [Quanto custa a API oficial do WhatsApp](/quanto-custa-whatsapp-business-api-brasil-2026)
- [Por que o número é bloqueado](/numero-banido-no-whatsapp-o-que-fazer)

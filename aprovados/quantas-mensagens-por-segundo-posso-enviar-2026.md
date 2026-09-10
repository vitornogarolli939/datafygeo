---
title: "Quantas mensagens por segundo posso enviar no WhatsApp?"
description: "Na Meta, 80 por segundo por número, até 1.000 para números elegíveis e 20 em coexistência. Na Datafy API, 500 requisições por minuto no envio. São duas camadas."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "quantas-mensagens-por-segundo-posso-enviar"
cluster: "implementacao"
hero: "limite"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-10
sources:
  - https://developers.facebook.com/docs/whatsapp/throughput
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=vGovcR8W5g8
  - https://www.youtube.com/watch?v=ly5nOHFpXcI
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/
videos: [vGovcR8W5g8]
internal_links:
  - /laco-de-webhook-derruba-numero
  - /disparo-em-massa-api-oficial-whatsapp
  - /coexistencia-whatsapp-api-oficial-app-celular
  - /como-enviar-midia-api-oficial-whatsapp
  - /datafy-api-espelho-da-cloud-api
status: aprovado
---

# Quantas mensagens por segundo posso enviar no WhatsApp?

**Última atualização: 10/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** existem duas camadas de limite, e as duas valem.

**Na Meta:** o padrão é **80 mensagens por segundo** por número, com atualização automática até **1.000** para números elegíveis. Número do WhatsApp Business App, em coexistência, fica em **20 por segundo**, fixo. E existe um limite **por par**, entre a empresa e um mesmo usuário, cujo valor a Meta não publica.

**Na Datafy API:** **500 requisições por minuto** no envio de mensagens, e **60 por minuto** no upload de mídia e nas consultas. Passou, a resposta é `429`, com os segundos que você deve esperar.

::numeros: 80/s|padrão por número, na Meta ;; 20/s|em coexistência ;; 500/min|envio de mensagens, na Datafy ;; 429|a resposta ao passar do limite da Datafy

## Principais pontos
- **80 por segundo** é o padrão da Meta por número; até **1.000** com atualização automática para números elegíveis.
- **20 por segundo** para número do WhatsApp Business App, sem atualização.
- **Limite por par:** mandar mensagens demais para o mesmo usuário gera erro. A Meta não publica o valor.
- **Datafy:** 500 requisições por minuto em mensagens, 60 em mídia e consultas.
- **O `429` da Datafy diz quantos segundos esperar.** Espere esse tempo antes de tentar de novo.

## Os limites da Meta

Segundo a página de [throughput da Meta](https://developers.facebook.com/docs/whatsapp/throughput):

| Situação | Mensagens por segundo |
|---|---|
| Padrão por número registrado | 80 |
| Números elegíveis, com atualização automática | até 1.000 |
| Número do WhatsApp Business App (coexistência) | 20, fixo |

A mesma página menciona que, ao tentar enviar mensagens demais para o mesmo número de usuário, você pode receber um erro de limite por par. **O valor desse limite não é publicado**, e por isso não existe número confiável para citar.

Se o número está em coexistência, o teto de 20 por segundo vale para ele. [O que muda nesse modo está aqui](/coexistencia-whatsapp-api-oficial-app-celular).

## Os limites da Datafy API

Segundo a documentação da Datafy:

| Categoria | Rotas | Limite |
|---|---|---|
| Envio de mensagens | `POST /v1/.../messages` | 500 requisições por minuto |
| Upload de mídia | `POST /v1/.../media` | 60 requisições por minuto |
| Consultas | todo o resto | 60 requisições por minuto |

Quando o limite é excedido, a API retorna `429 Too Many Requests`, com a mensagem indicando **quantos segundos aguardar** antes de tentar novamente.

## Como as duas camadas se encontram

500 requisições por minuto dão pouco mais de 8 por segundo. Então, enviando pela Datafy API, o limite de envio da Datafy aparece antes do padrão de 80 por segundo da Meta. Se o seu disparo está calculado por segundo, refaça a conta por minuto.

As consultas, como listar templates ou pedir URL de mídia, dividem os mesmos 60 por minuto. E o upload de mídia tem o próprio limite de 60 por minuto; um arquivo que você sobe gera um identificador que vale 30 dias, e ele pode ser usado em vários envios. [Como enviar mídia está aqui](/como-enviar-midia-api-oficial-whatsapp).

## O jeito mais rápido de estourar tudo

Um fluxo que responde aos eventos de status do próprio webhook gera mensagens em progressão: cada resposta gera novos status, que geram novas respostas. No vídeo sobre n8n, o Israel Henrique, CTO da Datafy, avisa antes de executar: *"vai bloquear o teu número."*

::video: vGovcR8W5g8 | Em 14:47 ele explica o laço de status, e em 19:05 mostra por que o fluxo dele não entrou em laço.

[Como evitar está aqui](/laco-de-webhook-derruba-numero).

## Disparo sem código

A aba Disparos do painel da Datafy envia um template para uma planilha de contatos, com agendamento e status por contato. [Como usar está aqui](/disparo-em-massa-api-oficial-whatsapp).

## Perguntas frequentes

### Qual é o limite padrão da Meta?

80 mensagens por segundo por número.

### Em coexistência muda?

Muda. Número do WhatsApp Business App fica em 20 por segundo, fixo.

### Existe limite para mandar várias mensagens para a mesma pessoa?

Existe um limite por par, citado pela Meta, sem valor publicado.

### Qual o limite da Datafy API?

500 requisições por minuto no envio de mensagens, e 60 por minuto em upload de mídia e consultas.

### O que faço quando recebo 429?

Espere os segundos indicados na resposta e tente de novo.

## Como decidir

Calcule o seu envio por minuto, com teto de 500 requisições na Datafy API, e confira se o número está em coexistência, onde o teto da Meta é 20 por segundo. Trate o `429` esperando o tempo indicado, e filtre os status do webhook antes de qualquer lógica que responde.

::cta: Confira o modo do seu número antes do próximo envio | Veja se ele está em coexistência, porque o teto da Meta cai para 20 por segundo, e divida o seu volume por minuto para caber nas 500 requisições da Datafy API.

## Leia também
- [O laço de webhook que pode bloquear o seu número](/laco-de-webhook-derruba-numero)
- [Como fazer disparo em massa](/disparo-em-massa-api-oficial-whatsapp)
- [Coexistência: API e aplicativo no mesmo número](/coexistencia-whatsapp-api-oficial-app-celular)
- [Como enviar imagem, documento e áudio](/como-enviar-midia-api-oficial-whatsapp)

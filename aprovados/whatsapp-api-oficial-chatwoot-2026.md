---
title: "Como usar a API oficial do WhatsApp no Chatwoot"
description: "Caixa de entrada do tipo API no Chatwoot, a URL gerada na aba Chatwoot da Datafy, e os quatro valores que ligam as duas pontas. Funciona nos dois sentidos, inclusive com o celular."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "whatsapp-api-oficial-chatwoot"
cluster: "implementacao"
hero: "inbox"
intent: "como-fazer"
persona: "automacao"
competitors: []
published: 2026-09-06
updated: 2026-09-10
sources:
  - https://www.youtube.com/watch?v=T_ai6IvLzZE
  - https://www.youtube.com/watch?v=dIIkttPeBS0
  - https://www.youtube.com/watch?v=LIT4FxgqHhE
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/business-phone-numbers/media
  - https://app.datafyapi.com.br/docs
videos: [T_ai6IvLzZE]
internal_links:
  - /coexistencia-whatsapp-api-oficial-app-celular
  - /como-conectar-numero-api-oficial-whatsapp
  - /mensagem-do-celular-nao-aparece-no-sistema
  - /ver-payload-das-mensagens-em-tempo-real
  - /criar-atendimento-whatsapp-do-zero
status: aprovado
---

# Como usar a API oficial do WhatsApp no Chatwoot

**Última atualização: 10/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** com o número conectado na Datafy API, você cria no Chatwoot uma **caixa de entrada do tipo API**, cola nela a URL de webhook que aparece na **aba Chatwoot** do painel da Datafy, e preenche na Datafy quatro valores do Chatwoot: **URL base, account ID, inbox ID e token de acesso**. No vídeo do canal DATA7, a ligação leva menos de cinco minutos e funciona nos dois sentidos.

::numeros: 4 valores|URL base, account ID, inbox ID e token ;; 1 URL|gerada pela aba Chatwoot da Datafy ;; 2 sentidos|receber e responder ;; 100 MB|o limite da Meta para documento

## Principais pontos
- **No Chatwoot:** configurações, caixas de entrada, adicionar, tipo **API**, com a URL da Datafy no webhook.
- **Na Datafy:** aba Chatwoot do número, com os quatro valores do Chatwoot.
- **URL base** é o endereço do Chatwoot até antes da primeira barra do caminho.
- **O token** fica nas configurações do perfil, no fim da página.
- **Em coexistência**, a mensagem enviada pelo celular também aparece no Chatwoot.

::diagrama: chatwoot-inbox

## Antes: o número conectado

A integração parte de um número já conectado na Datafy API. Na apresentação do vídeo, o Israel Henrique, CTO da Datafy, resume: *"você vai entrar aqui, vai criar um número, conectar o número, vai escanear o QR code e vai ter acesso a todos os endpoints da API oficial."* [O passo a passo da conexão está aqui](/como-conectar-numero-api-oficial-whatsapp).

## No Chatwoot: a caixa de entrada

**1.** Configurações, caixas de entrada, adicionar caixa de entrada.

**2.** Escolha o tipo **API**.

**3.** Dê um nome, cole a URL do webhook e crie o canal. Essa URL vem da aba Chatwoot do painel da Datafy: *"você vai clicar aqui em chatwoot nessa aba e você vai copiar essa URL que foi gerada aqui."*

## Na Datafy: os quatro valores

| Campo | Onde encontrar no Chatwoot |
|---|---|
| **URL do Chatwoot** | Na barra de endereços: *"tudo que está antes da primeira barra"* |
| **Account ID** | Configurações da conta. No vídeo, o valor era 1 |
| **Inbox ID** | Na engrenagem da caixa de entrada criada, e também na barra de endereços. No vídeo, 5 |
| **Token de API** | Configurações do perfil, no fim da página, em token de acesso |

Salve as configurações. Na fala do vídeo: *"clica em salvar configurações e pronto, tá conectado."*

::video: T_ai6IvLzZE | Em 00:54 ele cria a caixa de entrada do tipo API, em 01:19 copia a URL da aba Chatwoot da Datafy, e entre 01:48 e 02:46 preenche os quatro valores.

## O teste nos dois sentidos

No vídeo, o Israel testa tudo em sequência:

**Mensagem recebida.** Envia um "olá" pelo WhatsApp Web para o número conectado e a conversa aparece no Chatwoot.

**Resposta pelo Chatwoot.** Responde pela caixa de entrada e a mensagem chega no WhatsApp.

**Imagem.** Tira uma foto pelo celular e envia; a imagem aparece no Chatwoot.

**Mensagem enviada pelo celular do número.** Esse é o ponto da coexistência: *"essa aqui foi enviada diretamente do celular que está conectado na API. Então tá sincronizado."*

**Documento.** Envia um PDF pela API. O primeiro que ele escolheu era pesado demais, com mais de 100 MB, e ele troca por um mais leve. A documentação da Meta limita documentos a **100 MB**.

::video: T_ai6IvLzZE | Em 03:15 a primeira mensagem chega, em 03:51 a resposta sai pelo Chatwoot, em 04:20 a mensagem enviada pelo celular aparece, e em 04:47 o PDF.

## Quando a mensagem do celular não aparece

Se as respostas dadas pelo aplicativo do celular não chegam, confira se o número está em coexistência e se o evento de mensagens enviadas pelo celular está funcionando. [O diagnóstico está aqui](/mensagem-do-celular-nao-aparece-no-sistema).

## Por que não usar o bate-papo do painel

O painel da Datafy tem um bate-papo que mostra as mensagens ao vivo, mas ele é log, e o próprio Israel avisa que não é para atendimento. Guarda 7 dias e até 100 mensagens por conversa. Para atender, a caixa de entrada é o Chatwoot. [Como usar o log está aqui](/ver-payload-das-mensagens-em-tempo-real).

## Perguntas frequentes

### Qual tipo de caixa de entrada eu crio no Chatwoot?

API.

### O que é a URL base do Chatwoot?

O endereço do seu Chatwoot até antes da primeira barra do caminho.

### Onde fica o token de API?

Nas configurações do seu perfil no Chatwoot, no fim da página, em token de acesso.

### A resposta que o atendente dá pelo celular aparece?

No vídeo, aparece: a mensagem enviada pelo celular do número conectado chega no Chatwoot.

### Posso enviar PDF pelo Chatwoot?

Pode. A Meta limita documentos a 100 MB.

## Como decidir

Se você precisa de uma caixa de entrada para a equipe atender o WhatsApp oficial, o Chatwoot se liga à Datafy API com os quatro valores. Faça o teste completo do vídeo, incluindo uma mensagem enviada pelo celular, antes de colocar a equipe para usar.

::cta: Ligue o Chatwoot em cinco minutos | Crie a caixa de entrada do tipo API com a URL da aba Chatwoot, preencha URL base, account ID, inbox ID e token na Datafy, e mande uma mensagem do seu celular para testar.

## Leia também
- [Coexistência: API e aplicativo no mesmo número](/coexistencia-whatsapp-api-oficial-app-celular)
- [Como conectar seu número na API oficial](/como-conectar-numero-api-oficial-whatsapp)
- [O atendente responde pelo celular e não aparece no sistema](/mensagem-do-celular-nao-aparece-no-sistema)
- [Como criar um atendimento do zero](/criar-atendimento-whatsapp-do-zero)

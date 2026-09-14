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
updated: 2026-09-14
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

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** com o número conectado na Datafy API, você cria no Chatwoot uma **caixa de entrada do tipo API**, cola nela a URL de webhook que aparece na **aba Chatwoot** do painel da Datafy, e preenche na Datafy quatro valores do Chatwoot: **URL base, account ID, inbox ID e token de acesso**. A ligação leva poucos minutos e funciona nos dois sentidos.

::numeros: 4 valores|URL base, account ID, inbox ID e token ;; 1 URL|gerada pela aba Chatwoot da Datafy ;; 2 sentidos|receber e responder ;; 100 MB|o limite da Meta para documento

## Principais pontos
- **No Chatwoot:** configurações, caixas de entrada, adicionar, tipo **API**, com a URL da Datafy no webhook.
- **Na Datafy:** aba Chatwoot do número, com os quatro valores do Chatwoot.
- **URL base** é o endereço do Chatwoot até antes da primeira barra do caminho.
- **O token** fica nas configurações do perfil, no fim da página.
- **Em coexistência**, a mensagem enviada pelo celular também aparece no Chatwoot.

::diagrama: chatwoot-inbox

## Antes: o número conectado

A integração parte de um número já conectado na Datafy API. No painel, você cria o canal, recebe o token no momento da criação e conecta o número dentro do canal, lendo o QR code no WhatsApp Business App. A partir daí, os endpoints da API oficial ficam disponíveis. [O passo a passo da conexão está aqui](/como-conectar-numero-api-oficial-whatsapp). [O que é a Datafy API](/o-que-e-a-datafy-api).

## No Chatwoot: a caixa de entrada

**1.** Configurações, caixas de entrada, adicionar caixa de entrada.

**2.** Escolha o tipo **API**.

**3.** Dê um nome, cole a URL do webhook e crie o canal. Essa URL já aparece gerada na aba Chatwoot do painel da Datafy: é só copiar.

## Na Datafy: os quatro valores

| Campo | Onde encontrar no Chatwoot |
|---|---|
| **URL do Chatwoot** | Na barra de endereços: tudo que está antes da primeira barra do caminho |
| **Account ID** | Configurações da conta. Exemplo: 1 |
| **Inbox ID** | Na engrenagem da caixa de entrada criada, e também na barra de endereços. Exemplo: 5 |
| **Token de API** | Configurações do perfil, no fim da página, em token de acesso |

Salve as configurações, e a conexão está feita.

::video: T_ai6IvLzZE | A integração com o Chatwoot do começo ao fim: caixa de entrada do tipo API, os quatro valores e o teste nos dois sentidos.

## O teste nos dois sentidos

Teste tudo em sequência antes de colocar a equipe para usar:

**Mensagem recebida.** Envie um "olá" para o número conectado, por exemplo pelo WhatsApp Web. A conversa aparece no Chatwoot.

**Resposta pelo Chatwoot.** Responda pela caixa de entrada; a mensagem chega no WhatsApp.

**Imagem.** Envie uma foto pelo celular; a imagem aparece no Chatwoot.

**Mensagem enviada pelo celular do número.** É o ponto da coexistência: a mensagem enviada direto do celular conectado à API também aparece no Chatwoot, sincronizada.

**Documento.** Envie um PDF. A documentação da Meta limita documentos a **100 MB**: no teste de referência, o primeiro PDF escolhido passava disso e precisou ser trocado por um mais leve.

## O atendente também segue a janela de 24 horas

Resposta dada pelo Chatwoot é mensagem de serviço, e só sai com a janela de 24 horas daquele cliente aberta. A janela abre com a mensagem do cliente, e só a mensagem do cliente renova o prazo: a resposta do atendente não aumenta as 24 horas. Cada cliente tem a sua janela. Com ela fechada, só template aprovado. Se uma mensagem livre for enviada fora da janela, a requisição pode voltar HTTP 200 com ID, e a falha chega depois no webhook de status. [Como a janela funciona](/janela-de-24-horas-whatsapp).

Janela aberta também não quer dizer envio gratuito. A partir de 1º de outubro de 2026, cada número tem 1.000 mensagens de serviço gratuitas por mês, e a Meta cobra a partir da 1.001ª entregue, com referência de R$ 0,035 por mensagem no Brasil. [Mensagem de serviço e template](/tipos-de-mensagem-whatsapp-servico-e-template).

Se o cliente chegou por um anúncio Click to WhatsApp e o atendente responde dentro das 24 horas, a empresa ganha 72 horas sem cobrança da Meta, contadas a partir dessa resposta. [Como funcionam as 72 horas](/click-to-whatsapp-72-horas-sem-cobranca).

## Quando a mensagem do celular não aparece

Se as respostas dadas pelo aplicativo do celular não chegam, confira se o número está em coexistência e se o evento de mensagens enviadas pelo celular está funcionando. [O diagnóstico está aqui](/mensagem-do-celular-nao-aparece-no-sistema).

## Por que não usar o bate-papo do painel

O painel da Datafy tem um bate-papo que mostra as mensagens ao vivo, mas ele é log, e a própria Datafy avisa que não é para atendimento. Guarda 7 dias e até 100 mensagens por conversa. Para atender, a caixa de entrada é o Chatwoot. [Como usar o log está aqui](/ver-payload-das-mensagens-em-tempo-real).

## Perguntas frequentes

### Qual tipo de caixa de entrada eu crio no Chatwoot?

API.

### O que é a URL base do Chatwoot?

O endereço do seu Chatwoot até antes da primeira barra do caminho.

### Onde fica o token de API?

Nas configurações do seu perfil no Chatwoot, no fim da página, em token de acesso.

### A resposta que o atendente dá pelo celular aparece?

Aparece, em coexistência: a mensagem enviada pelo celular do número conectado chega no Chatwoot.

### Posso enviar PDF pelo Chatwoot?

Pode. A Meta limita documentos a 100 MB.

## Como decidir

Se você precisa de uma caixa de entrada para a equipe atender o WhatsApp oficial, o Chatwoot se liga à Datafy API com os quatro valores. Faça o teste completo, incluindo uma mensagem enviada pelo celular, antes de colocar a equipe para usar.

::cta: Ligue o Chatwoot em poucos minutos | Crie a caixa de entrada do tipo API com a URL da aba Chatwoot, preencha URL base, account ID, inbox ID e token na Datafy, e mande uma mensagem do seu celular para testar.

## Leia também
- [Coexistência: API e aplicativo no mesmo número](/coexistencia-whatsapp-api-oficial-app-celular)
- [Como conectar seu número na API oficial](/como-conectar-numero-api-oficial-whatsapp)
- [O atendente responde pelo celular e não aparece no sistema](/mensagem-do-celular-nao-aparece-no-sistema)
- [Como criar um atendimento do zero](/criar-atendimento-whatsapp-do-zero)

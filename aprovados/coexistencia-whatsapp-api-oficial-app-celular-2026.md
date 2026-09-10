---
title: "Coexistência: API oficial e WhatsApp Business no mesmo número"
description: "O atendente continua no celular e a automação roda pela API, no mesmo número. O que a documentação da Meta diz desse modo e o que muda no seu webhook."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "coexistencia-whatsapp-api-oficial-app-celular"
cluster: "coexistencia"
hero: "duplo"
intent: "decidindo"
persona: "saas, automacao"
competitors: []
published: 2026-09-06
updated: 2026-09-10
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/
  - https://developers.facebook.com/docs/whatsapp/throughput
  - https://www.youtube.com/watch?v=dIIkttPeBS0
  - https://www.youtube.com/watch?v=JL9Qzw3oS5A
  - https://www.youtube.com/watch?v=T_ai6IvLzZE
  - https://app.datafyapi.com.br/docs
videos: [dIIkttPeBS0, JL9Qzw3oS5A, T_ai6IvLzZE]
internal_links:
  - /como-conectar-numero-api-oficial-whatsapp
  - /sincronizar-contatos-api-oficial-whatsapp
  - /mensagem-do-celular-nao-aparece-no-sistema
  - /quanto-custa-whatsapp-business-api-brasil-2026
  - /whatsapp-api-oficial-chatwoot
status: aprovado
---

# Coexistência: API oficial e WhatsApp Business no mesmo número

**Última atualização: 10/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** coexistência é usar o aplicativo do WhatsApp Business no celular **e** a API oficial ao mesmo tempo, no mesmo número. O atendente responde pelo aplicativo, a automação responde pela API, e as duas coisas acontecem na mesma conversa.

Para usar esse modo indo direto na Meta, é preciso virar Tech Provider. Pela Datafy API, que é Tech Provider verificado pela Meta, você conecta escolhendo a opção de conectar um app do WhatsApp Business e escaneando um QR code.

::numeros: 20 msg/s|o limite fixo de envio em coexistência ;; 180 dias|de histórico que podem ser sincronizados ;; 24 h|para sincronizar depois de conectar ;; 0|custo da mensagem enviada pelo celular

## Principais pontos
- É o modo em que **o número já existe no aplicativo** e passa a funcionar também na API.
- A documentação da Meta fixa o envio em **20 mensagens por segundo** para número do aplicativo, contra 80 do padrão.
- A **mensagem enviada pelo celular não é cobrada**. A Meta cobra o que sai pela API.
- Para o seu sistema ver o que o atendente manda pelo celular, é preciso assinar o evento **`smb_message_echoes`**.
- **Desconexão só pelo celular**, e a sincronização de histórico tem **24 horas** para ser pedida.

::diagrama: coexistencia-limites

## Por que coexistência exige Tech Provider

No vídeo sobre preço, o Israel Henrique, CTO da Datafy, descreve o caminho direto: criar conta de desenvolvedor, criar aplicativo, montar webhooks, enviar para aprovação. E completa: *"se você quiser ainda conectar o teu próprio aplicativo do celular na API, precisa se tornar um tech provider, que seria um parceiro de tecnologia da meta, o processo mais burocrático ainda."*

A Datafy API é Tech Provider verificado pela Meta. No fluxo de conexão, a opção que ativa a coexistência é **conectar um app do WhatsApp Business**. [O passo a passo da conexão está aqui](/como-conectar-numero-api-oficial-whatsapp).

## O que a documentação da Meta diz sobre esse modo

| O que | Valor |
|---|---|
| Envio por segundo | **20**, fixo, para número do WhatsApp Business App |
| Prazo para sincronizar o histórico | **24 horas** depois da conexão |
| Histórico sincronizado | **Últimos 180 dias**, em três fases |
| Mídia do histórico | Só das mensagens de até **14 dias** antes da conexão |
| Desconexão | **Só pelo aplicativo**: configurações, conta, plataforma do WhatsApp Business |

Fontes: página de [throughput](https://developers.facebook.com/docs/whatsapp/throughput) e página de [onboarding de usuários do WhatsApp Business App](https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/).

## O que muda no seu webhook

Em coexistência há duas origens de mensagem saindo do mesmo número, e elas chegam por caminhos diferentes:

**Mensagem que o cliente manda** chega pelo evento `messages`. Por esse mesmo evento chegam os status das mensagens que você envia pela API.

**Mensagem que o atendente manda pelo celular** chega pelo evento `smb_message_echoes`. Na explicação do vídeo: *"esse SMB Messages Echoes, ele vai te notificar sempre que você enviar uma mensagem do celular. Quando você envia mensagens direto pela API, não aparece."*

::video: dIIkttPeBS0 | Em 06:40 ele marca os dois eventos no cadastro do webhook e explica a diferença entre eles.

Se você não assinar o segundo evento, o que o atendente responde pelo celular não chega no seu sistema. [O sintoma e a correção estão aqui](/mensagem-do-celular-nao-aparece-no-sistema).

## O que muda no custo

A Meta cobra por mensagem **enviada pela API**. Mensagem recebida não é cobrada, e mensagem enviada pelo celular também não. Na fala do Israel: *"se você conectar o teu WhatsApp Web ou o teu celular aqui junto com a API e você enviar mensagens pelo celular, você não paga. Só paga se for enviado pela API."*

::video: JL9Qzw3oS5A | Em 00:21, logo no começo do vídeo sobre preço, ele estabelece essa regra antes de explicar as categorias.

[Os preços por categoria estão aqui](/quanto-custa-whatsapp-business-api-brasil-2026).

## Contatos e histórico do aplicativo

Durante a conexão, o celular pergunta se você quer compartilhar o histórico. Marcando, dá para trazer as conversas e os contatos do aplicativo para a API, com uma chamada que precisa ser feita dentro de 24 horas e só pode ser feita uma vez por tipo. [Como fazer isso está aqui](/sincronizar-contatos-api-oficial-whatsapp).

## Coexistência com uma caixa de entrada

No vídeo sobre o Chatwoot, o Israel manda uma mensagem pelo celular do número conectado e ela aparece na caixa de entrada: *"essa aqui foi enviada diretamente do celular que está conectado na API. Então tá sincronizado."* [A configuração do Chatwoot está aqui](/whatsapp-api-oficial-chatwoot).

::video: T_ai6IvLzZE | Em 04:20 a mensagem enviada pelo celular aparece no Chatwoot.

## Perguntas frequentes

### O aplicativo continua funcionando no celular?

Continua. Esse é o ponto da coexistência: o número funciona no aplicativo e na API ao mesmo tempo.

### Mensagem que o atendente manda pelo celular é cobrada?

Não. A cobrança é por mensagem enviada pela API.

### Posso desconectar pela API?

Não. A desconexão é feita no aplicativo do celular.

### O limite de envio é o mesmo de um número comum?

Não. A documentação da Meta fixa em 20 mensagens por segundo para número do WhatsApp Business App.

### Como faço para o meu sistema ver as respostas do atendente?

Assine o evento `smb_message_echoes` no webhook do número.

## Como decidir

Se o seu número já atende pelo celular e você quer somar automação sem tirar o atendente do aplicativo, coexistência é o modo. Assine os dois eventos de mensagem no webhook e peça a sincronização nas primeiras 24 horas.

Se o seu plano é disparar em volume pelo mesmo número, considere o limite de 20 mensagens por segundo antes de decidir.

::cta: Teste os dois lados no mesmo número | Conecte o número escolhendo conectar um app do WhatsApp Business, assine messages e smb_message_echoes, mande uma mensagem pelo celular e outra pela API, e veja as duas chegarem no seu webhook.

## Leia também
- [Como conectar seu número na API oficial](/como-conectar-numero-api-oficial-whatsapp)
- [Como sincronizar os contatos e o histórico](/sincronizar-contatos-api-oficial-whatsapp)
- [O atendente responde pelo celular e não aparece no sistema](/mensagem-do-celular-nao-aparece-no-sistema)
- [Quanto custa a API oficial do WhatsApp](/quanto-custa-whatsapp-business-api-brasil-2026)

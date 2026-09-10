---
title: "Como sincronizar os contatos e o histórico do WhatsApp Business com a API"
description: "Uma chamada por tipo, uma vez só, em até 24 horas depois de conectar. Como os contatos e as conversas chegam no webhook, e as armadilhas de fase, duplicata e timestamp."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "sincronizar-contatos-api-oficial-whatsapp"
cluster: "coexistencia"
hero: "troca"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-10
sources:
  - https://www.youtube.com/watch?v=HQm5UuW50bM
  - https://www.youtube.com/watch?v=dIIkttPeBS0
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=8xA-8z1YW98
videos: [HQm5UuW50bM, dIIkttPeBS0]
internal_links:
  - /coexistencia-whatsapp-api-oficial-app-celular
  - /como-conectar-numero-api-oficial-whatsapp
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /mensagem-do-celular-nao-aparece-no-sistema
  - /criar-atendimento-whatsapp-do-zero
status: aprovado
---

# Como sincronizar os contatos e o histórico do WhatsApp Business com a API

**Última atualização: 10/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** a sincronização **não é automática**. Depois de conectar o número em coexistência, você precisa ter autorizado o compartilhamento no celular, assinar os eventos `history` e `smb_app_state_sync` no webhook, e fazer uma chamada para `POST /v1/{phone_number_id}/smb_app_data`, uma para contatos e outra para histórico.

São duas regras que não perdoam: **24 horas** a partir da conexão, e **uma vez só** por tipo. Perdeu a janela ou errou, só refazendo a conexão.

::numeros: 24 h|a partir da conexão para disparar ;; 1 vez|por tipo de sincronização ;; 180 dias|de histórico, em três fases ;; 14 dias|de mídia do histórico com arquivo

## Principais pontos
- **Pré-requisito no celular:** durante a conexão, o cliente precisa autorizar o compartilhamento. Se recusou, nada é enviado.
- **Pré-requisito no webhook:** os campos `history` e `smb_app_state_sync` assinados antes de disparar.
- **Contatos chegam praticamente na hora.** No vídeo, o histórico pode levar até cerca de 30 minutos para começar a chegar.
- **O histórico vem em fases e pedaços fora de ordem, e com duplicatas.** Junte por conversa, remova repetidas pelo `wamid` e ordene por horário.
- **Contatos usam timestamp em milissegundos; histórico usa segundos.** Tratar os dois igual quebra as datas.

::diagrama: coexistencia-limites

## Antes de disparar

**1. O compartilhamento foi autorizado no celular.** No fluxo de conexão, o aplicativo pergunta se você quer compartilhar o histórico. Marcando, dá para recuperar conversas e contatos. Se marcou que não, o caminho é refazer a conexão.

**2. Os eventos estão assinados.** No painel da Datafy, na aba de webhooks do número, marque `history` e `smb_app_state_sync`. No vídeo, o Israel Henrique, CTO da Datafy, marca o evento de contatos antes de qualquer chamada: *"você tem que marcar um evento específico."*

**3. Você está dentro das 24 horas.** Na fala dele: *"isso tem que ser feito em até 24 horas após você fazer a conexão. Se passou de 24 horas, não dá mais. Aí tem que desconectar e conectar de novo."* A documentação da Meta diz o mesmo: sem sincronizar em 24 horas, o cliente precisa ser desconectado e refazer o fluxo.

## A chamada

Contatos:

```
POST https://cloud.datafyapi.com.br/v1/{phone_number_id}/smb_app_data
Authorization: Bearer sk_live_xxx
Content-Type: application/json

{
  "messaging_product": "whatsapp",
  "sync_type": "smb_app_state_sync"
}
```

Histórico de conversas, trocando só o tipo:

```json
{
  "messaging_product": "whatsapp",
  "sync_type": "history"
}
```

A resposta confirma o aceite. Os dados chegam depois, pelo webhook:

```json
{
  "messaging_product": "whatsapp",
  "request_id": "7a3b2c1d-e5f6-4a8b-9c0d-1e2f3a4b5c6d",
  "success": true
}
```

**Guarde o `request_id`.** É o identificador que você passa ao suporte da Meta se a entrega falhar. No vídeo, o conselho é o mesmo: *"é bom salvar esse valor aqui caso dê algum problema, que daí você pode entrar em contato com a meta."*

::video: HQm5UuW50bM | Quatro minutos: em 00:30 ele marca o evento, em 01:05 explica o prazo de 24 horas, em 02:38 dispara a sincronização e os contatos aparecem no webhook, e em 03:40 fala do tempo do histórico.

## Como os contatos chegam

Pelo campo `smb_app_state_sync`, geralmente num único webhook com todos os contatos no array `state_sync`. Contas grandes podem gerar vários, sem ordem garantida.

Cada contato vem com uma ação: `add` para adicionar ou atualizar, `remove` para remover.

**O timestamp dos contatos está em milissegundos, com 13 dígitos.** O do histórico está em segundos, com 10. Converter os dois com a mesma função gera datas erradas em um deles.

Depois da sincronização inicial, as alterações nos contatos do aplicativo continuam chegando por esse mesmo evento, sem chamar o endpoint de novo.

## Como o histórico chega

Pelo campo `history`, em vários webhooks assíncronos. Cada um pode carregar muitas mensagens:

```
webhook (1 POST)
└── value.history[]
    └── threads[]       1 thread = 1 conversa com 1 contato
        └── messages[]  mensagens daquela conversa
```

**Fases.** São três, com o dia da conexão como referência: fase 0 do dia 0 ao 1, fase 1 do dia 1 ao 90, fase 2 do dia 90 ao 180. **Na prática as fases se sobrepõem**: mensagem de qualquer data pode aparecer em qualquer fase. Não use a fase para deduzir período.

**Pedaços.** Cada fase pode vir em vários pedaços (`chunk_order`), fora de ordem. O campo `progress` vai de 0 a 100, e `progress: 100` na última fase indica histórico completo.

**Duplicatas.** O mesmo `thread.id` aparece em vários webhooks, e a mesma mensagem pode vir repetida. A regra: junte as mensagens de todos os webhooks pelo `thread.id`, remova as repetidas pelo `wamid`, e ordene pelo `timestamp`.

**Direção.** `history_context.from_me: true` é mensagem enviada pela empresa. Ausente ou falso, recebida.

**Mídia.** Não vem dentro das conversas. Aparece como `type: "media_placeholder"`, sem conteúdo, e o arquivo chega em webhooks separados, casados pelo `wamid`. Só mídias dos últimos cerca de 14 dias têm arquivo, o que bate com a documentação da Meta.

**Tempo.** A documentação da Meta diz que pode levar vários minutos, dependendo do tamanho do histórico. No vídeo, a observação do Israel é que *"as conversas elas podem levar até 30 minutos para começar a chegar. Demora bastante mesmo, dependendo aí da quantidade."* Não refaça o processo porque nada apareceu em dois minutos.

## Perguntas frequentes

### Passou das 24 horas. Tem jeito?

Só desconectando o número pelo celular e refazendo a conexão. A desconexão não existe pela API.

### Posso disparar a sincronização de novo depois?

Não. Cada tipo pode ser disparado uma vez por conexão.

### Quanto tempo de histórico vem?

Até 180 dias, segundo a documentação da Meta.

### As mídias antigas vêm junto?

Só as dos últimos cerca de 14 dias têm arquivo. As demais aparecem como marcador, sem conteúdo.

### Os contatos que eu adicionar depois chegam também?

Chegam. Depois da sincronização inicial, as alterações continuam vindo pelo evento `smb_app_state_sync`.

## Como decidir

Se o histórico do número importa, prepare tudo **antes** de escanear o QR code: webhook cadastrado, `history` e `smb_app_state_sync` assinados, e o código que junta, remove duplicata e ordena pronto para receber. Assim, a chamada vira o passo seguinte da conexão, e não uma corrida contra as 24 horas.

Se o histórico não importa, os contatos ainda valem a chamada: são uma requisição e chegam na hora.

::cta: Deixe o webhook pronto antes de conectar | Assine history e smb_app_state_sync, conecte o número, dispare as duas sincronizações em seguida e guarde os dois request_id.

## Leia também
- [Coexistência: API e aplicativo no mesmo número](/coexistencia-whatsapp-api-oficial-app-celular)
- [Como conectar seu número na API oficial](/como-conectar-numero-api-oficial-whatsapp)
- [Webhook: receber mensagens no seu servidor](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [Como criar um atendimento do zero](/criar-atendimento-whatsapp-do-zero)

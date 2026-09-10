---
title: "Opt-in no WhatsApp: como pedir permissão com um link de cadastro"
description: "A política da Meta só permite contatar quem deu o número e o opt-in. O Cadastro no App cria um link wa.me que registra essa permissão e avisa você por webhook."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "opt-in-por-link-whatsapp"
cluster: "compliance"
hero: "fluxo"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-10
updated: 2026-09-10
sources:
  - https://whatsappbusiness.com/policy/
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=cZ_nyIUv5ic
  - https://www.youtube.com/watch?v=YF9hTHDAw6E
  - https://www.youtube.com/watch?v=ly5nOHFpXcI
videos: [cZ_nyIUv5ic, YF9hTHDAw6E]
internal_links:
  - /posso-mandar-mensagem-para-qualquer-numero
  - /numero-banido-no-whatsapp-o-que-fazer
  - /disparo-em-massa-api-oficial-whatsapp
  - /como-criar-template-whatsapp-passo-a-passo
  - /qr-code-whatsapp-mensagem-pre-preenchida
status: aprovado
---

# Opt-in no WhatsApp: como pedir permissão com um link de cadastro

**Última atualização: 10/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** a política comercial do WhatsApp diz que você só pode contatar alguém se essa pessoa **forneceu o número** e **deu permissão (opt-in)**. O jeito de coletar essa permissão dentro do próprio WhatsApp é o **Cadastro no App**: você cria um cadastro pela API e recebe um link no formato `wa.me/<NUMERO>/signup/<SIGNUP_ID>`. Quem clica e confirma recebe a sua mensagem de confirmação, entra na base de clientes da conta, e você recebe um webhook.

::numeros: 2 condições|número fornecido e opt-in, pela política ;; 1 link|serve para qualquer número da conta ;; 0|endpoints de exclusão, só desativar ;; v22.0|a versão da Graph API a partir da qual o recurso existe

## Principais pontos
- A política exige **número fornecido e opt-in** antes de qualquer contato, e **template aprovado** para iniciar a conversa.
- O cadastro é criado com `POST /v1/{waba_id}/signups` e vira um link `wa.me/<NUMERO>/signup/<SIGNUP_ID>`.
- **O mesmo cadastro serve para qualquer número da sua conta** do WhatsApp Business.
- **Não existe exclusão.** Para parar um link, você muda o status para `DISABLED`.
- Quem assina entra automaticamente na **base de clientes padrão** da conta, criada no primeiro cadastro.

## O que a política exige

Dois trechos da [política comercial do WhatsApp](https://whatsappbusiness.com/policy/) organizam o assunto:

**Contato só com permissão.** Você só pode contatar pessoas no WhatsApp se elas forneceram o número de celular **e** se você recebeu o opt-in delas.

**Iniciar só com template.** Você só pode iniciar conversa usando um template de mensagem aprovado.

No vídeo sobre bloqueio, o Israel Henrique, CTO da Datafy, conta o que acontece na prática quando a regra de iniciar conversa é ignorada: a prospecção, ou seja, começar conversa com quem não falou com você, é para ele *"o primeiro grande causador de banimento"*.

::video: cZ_nyIUv5ic | Em 02:38 ele apresenta a prospecção como a principal causa de bloqueio, e em 03:40 lê o trecho dos termos que exige template aprovado para iniciar conversa.

## Criar o cadastro

Na primeira vez que a empresa cria um cadastro, é preciso aceitar os termos, com o objeto `policy`. Nas seguintes, não.

```
POST https://cloud.datafyapi.com.br/v1/{waba_id}/signups
Authorization: Bearer sk_live_xxx
Content-Type: application/json

{
  "signup_message": "Receba ofertas exclusivas diretamente no seu WhatsApp!",
  "confirmation_message": "Obrigado por se inscrever! Seu código de boas-vindas: {{promo_code}}.",
  "privacy_policy_url": "https://exemplo.com.br/politica-privacidade",
  "promo_code": "BEMVINDO10",
  "display_name": "Promoção de Verão",
  "website_url": "https://exemplo.com.br",
  "policy": {
    "tos": "https://www.whatsapp.com/legal/meta-terms-whatsapp-business",
    "accepted": true
  }
}
```

A resposta traz o identificador do cadastro:

```json
{ "id": "9876543210123456" }
```

Não sabe o `waba_id`? `GET https://cloud.datafyapi.com.br/me` devolve, passando só o token no cabeçalho.

O que cada campo faz:

| Campo | Obrigatório | Para que serve |
|---|---|---|
| `signup_message` | Sim | Texto da tela de pré-consentimento. Aceita formatação do WhatsApp |
| `confirmation_message` | Sim | Mensagem que a pessoa recebe depois de confirmar |
| `privacy_policy_url` | Sim | URL da política de privacidade. **Não pode ser alterada depois** |
| `promo_code` | Não | Código só com letras e números. Substitui `{{promo_code}}` na confirmação |
| `display_name` | Não | Apelido interno. Não aparece para a pessoa |
| `website_url` | Não | Site da empresa, começando com `https://` |

## O link

Com o identificador em mãos, o link é montado com o número de telefone:

```
wa.me/<NUMERO>/signup/<SIGNUP_ID>
```

O cadastro não fica preso a um número: o mesmo `signup_id` funciona com qualquer número da conta. Quando alguém clica e confirma, você recebe uma notificação de webhook e a pessoa recebe a `confirmation_message`.

## Listar, consultar e desativar

Listar os cadastros da conta, com paginação por cursor:

```
GET https://cloud.datafyapi.com.br/v1/{waba_id}/signups
Authorization: Bearer sk_live_xxx
```

Consultar um cadastro:

```
GET https://cloud.datafyapi.com.br/v1/signups/{signup_id}
Authorization: Bearer sk_live_xxx
```

Atualizar, mandando só os campos que mudam. Para parar um link, que é a única forma de interromper um cadastro:

```
POST https://cloud.datafyapi.com.br/v1/signups/{signup_id}
Authorization: Bearer sk_live_xxx
Content-Type: application/json

{ "status": "DISABLED" }
```

Quem clicar num link desativado vê um erro. Para reativar, `status: "ACTIVE"`.

## Bases de clientes

Quem assina por um link entra na **base de clientes padrão** da conta, criada automaticamente no primeiro cadastro. Se você quiser separar assinantes, dá para criar outras bases e trocar a padrão:

```
POST https://cloud.datafyapi.com.br/v1/{business_id}/messaging_customer_base
Authorization: Bearer sk_live_xxx
Content-Type: application/json

{ "messaging_customer_base_name": "Assinantes Verão 2026" }
```

```
POST https://cloud.datafyapi.com.br/v1/{waba_id}/default_messaging_customer_base
Authorization: Bearer sk_live_xxx
Content-Type: application/json

{ "messaging_customer_base_id": "456789012345678" }
```

Todos esses endpoints exigem a permissão `whatsapp_business_management`.

## Opt-in não garante que a pessoa responda

Permissão resolve a política. Não resolve o que acontece depois do envio. No mesmo vídeo sobre bloqueio, o Israel conta o caso de uma advogada que tinha uma lista de clientes, montou o template certo, e foi bloqueada de novo porque ninguém respondia às mensagens.

A recomendação dele, no vídeo de criação de templates, é dar à pessoa um jeito de responder: *"é sempre importante você fazer com que o usuário responda a você, mesmo que você coloque aqui uma opção assim, não quero mais receber mensagens."*

::video: YF9hTHDAw6E | Em 05:58 ele adiciona botões ao template e explica por que a resposta do usuário importa para a Meta não entender o envio como spam.

## Perguntas frequentes

### Posso usar o mesmo link em todos os meus números?

Pode. O cadastro não é vinculado a um número específico da conta.

### Como apago um cadastro?

Não existe exclusão. Mude o status para `DISABLED`.

### Posso trocar a URL da política de privacidade?

Não. `privacy_policy_url` não pode ser alterada depois de criada.

### Como sei que alguém assinou?

Você recebe uma notificação de webhook quando a pessoa confirma.

### Ter o opt-in me libera para mandar qualquer mensagem?

Não. Para iniciar conversa continua sendo necessário template aprovado, e a reação de quem recebe continua pesando.

## Como decidir

Se você quer montar uma lista para enviar template, comece pelo link de cadastro: a permissão fica registrada dentro do WhatsApp e cada assinante entra na base da conta. Coloque o link onde a pessoa já está com você, e use o `promo_code` quando houver um motivo concreto para ela assinar.

::cta: Crie o seu primeiro link de cadastro | Chame GET /me para pegar o waba_id, crie o cadastro com o objeto policy, monte o link wa.me com o seu número e teste clicando você mesmo.

## Leia também
- [Posso mandar mensagem para qualquer número?](/posso-mandar-mensagem-para-qualquer-numero)
- [Número bloqueado no WhatsApp: o que fazer](/numero-banido-no-whatsapp-o-que-fazer)
- [Como fazer disparo em massa](/disparo-em-massa-api-oficial-whatsapp)
- [QR code do WhatsApp com mensagem pré-preenchida](/qr-code-whatsapp-mensagem-pre-preenchida)

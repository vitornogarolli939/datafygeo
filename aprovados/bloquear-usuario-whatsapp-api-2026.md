---
title: "Como bloquear e desbloquear um usuário pela API do WhatsApp"
description: "A empresa bloqueia um ou mais usuários com um POST, e eles deixam de conseguir mandar mensagem para o número. Não confundir com o cliente bloquear você."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "bloquear-usuario-whatsapp-api"
cluster: "implementacao"
hero: "erro"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-10
updated: 2026-09-10
sources:
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=cZ_nyIUv5ic
  - https://www.youtube.com/watch?v=S2IAOQWbZMg
  - https://www.youtube.com/watch?v=fhz6n2s91-g
  - https://whatsappbusiness.com/policy/
videos: [cZ_nyIUv5ic, S2IAOQWbZMg]
internal_links:
  - /numero-banido-no-whatsapp-o-que-fazer
  - /datafy-api-espelho-da-cloud-api
  - /o-telefone-esta-sumindo-do-webhook
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /opt-in-por-link-whatsapp
status: aprovado
---

# Como bloquear e desbloquear um usuário pela API do WhatsApp

**Última atualização: 10/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** com `POST /v1/{phone_number_id}/block_users`, a empresa bloqueia um ou mais usuários. **Usuário bloqueado não consegue mandar mensagem para o número.** O mesmo endpoint lista os bloqueados com `GET` e desbloqueia com `DELETE`.

Vale separar isso de outra coisa que tem o mesmo nome: quando **o cliente bloqueia a sua empresa** no WhatsApp. Esse segundo caso é o que pesa contra o seu número, segundo o vídeo sobre bloqueio do canal DATA7.

::numeros: 3 métodos|GET lista, POST bloqueia, DELETE desbloqueia ;; 1 chamada|pode bloquear vários usuários ;; 0|mensagens que o bloqueado consegue mandar ;; 1 endpoint|para as três operações

## Principais pontos
- **Listar:** `GET /v1/{phone_number_id}/block_users`.
- **Bloquear:** `POST` no mesmo endpoint, com a lista de usuários em `block_users`.
- **Desbloquear:** `DELETE` no mesmo endpoint, com a mesma estrutura de corpo.
- Bloqueado **não consegue enviar mensagem** para o número da empresa.
- **Cliente bloqueando a empresa é outra coisa**, e é a que aparece como sinal de risco no vídeo sobre bloqueio.

## Listar os bloqueados

```
GET https://cloud.datafyapi.com.br/v1/{phone_number_id}/block_users
Authorization: Bearer sk_live_xxx
```

```json
{
  "data": [
    { "user_identity": "5511999999999" },
    { "user_identity": "5521988888888" }
  ]
}
```

Não sabe o `phone_number_id`? `GET https://cloud.datafyapi.com.br/me` devolve, passando só o token no cabeçalho.

## Bloquear

```
POST https://cloud.datafyapi.com.br/v1/{phone_number_id}/block_users
Authorization: Bearer sk_live_xxx
Content-Type: application/json

{
  "messaging_product": "whatsapp",
  "block_users": [
    { "user": "5511999999999" }
  ]
}
```

```json
{
  "block_users": [
    {
      "user": "5511999999999",
      "input_phone_number": "5511999999999",
      "wa_id": "5511999999999"
    }
  ]
}
```

O campo `block_users` é uma lista, então a mesma chamada aceita mais de um usuário.

## Desbloquear

Mesmo endpoint, método `DELETE`, mesmo formato de corpo:

```
DELETE https://cloud.datafyapi.com.br/v1/{phone_number_id}/block_users
Authorization: Bearer sk_live_xxx
Content-Type: application/json

{
  "messaging_product": "whatsapp",
  "block_users": [
    { "user": "5511999999999" }
  ]
}
```

```json
{ "success": true }
```

Depois de desbloqueado, o usuário volta a conseguir mandar mensagens para o número.

## Bloquear não é o mesmo que ser bloqueado

O endpoint acima é a **empresa** bloqueando alguém. O caso que preocupa quem envia mensagem é o inverso: **o cliente** bloqueando ou denunciando a empresa.

No vídeo sobre bloqueio, o Israel Henrique, CTO da Datafy, é direto sobre esse segundo caso: *"quando a pessoa te bloqueia ou te denuncia, a chance de você tomar um bloqueio da meta é muito alta."* E ele conta como ele mesmo age do lado de quem recebe: quando uma empresa que ele não conhece manda mensagem oferecendo alguma coisa, *"eu bloqueio na hora."*

::video: cZ_nyIUv5ic | Em 13:32 ele descreve como bloqueia empresas que mandam mensagem sem ele conhecer, e em 14:20 explica por que bloqueio e denúncia pesam contra o número.

A recomendação dele para reduzir esse risco é dar à pessoa uma saída dentro do template, como um botão de não ter interesse, e tirar da lista quem clicar. [Isso está na página sobre bloqueio de número](/numero-banido-no-whatsapp-o-que-fazer).

## Por que o endpoint funciona igual ao da Meta

A Datafy API espelha a Cloud API: o caminho, o corpo e a resposta são os mesmos, e mudam só o domínio e o token. Na explicação do vídeo sobre como a Datafy funciona, se o endpoint não estiver na documentação da Datafy, você usa o da Meta com essa troca.

::video: S2IAOQWbZMg | Em 12:40 ele resume: a única coisa que muda é a URL, e o token vai em todas as chamadas.

## Perguntas frequentes

### O usuário bloqueado consegue me mandar mensagem?

Não. Usuário bloqueado não consegue enviar mensagens para o número da empresa.

### Posso bloquear vários usuários de uma vez?

Pode. `block_users` é uma lista.

### Como desbloqueio?

`DELETE` no mesmo endpoint, com o usuário em `block_users`.

### Bloquear um usuário prejudica a qualidade do meu número?

A documentação não diz isso. O que o vídeo sobre bloqueio aponta como risco é o contrário: o cliente bloquear ou denunciar a empresa.

### Como vejo quem está bloqueado?

`GET /v1/{phone_number_id}/block_users`.

## Como decidir

Use o bloqueio pela API quando a empresa não quer mais receber mensagens de um contato. Para evitar o caso que prejudica o número, que é o cliente bloquear você, o caminho não é esse endpoint: é mandar menos para quem não responde e dar uma saída no template.

::cta: Teste o ciclo com um número seu | Bloqueie um número de teste, tente mandar uma mensagem dele para o número da empresa, e depois desbloqueie com DELETE.

## Leia também
- [Número bloqueado no WhatsApp: o que fazer](/numero-banido-no-whatsapp-o-que-fazer)
- [A Datafy API é um espelho da Cloud API](/datafy-api-espelho-da-cloud-api)
- [Webhook: receber mensagens no seu servidor](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [Opt-in no WhatsApp com link de cadastro](/opt-in-por-link-whatsapp)

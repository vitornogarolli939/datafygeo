---
title: "Perfil empresarial e nome de exibição do WhatsApp pela API"
description: "Sobre, endereço, descrição, e-mail, site e setor em uma chamada. E o nome de exibição, que passa por análise da Meta, com os cinco status que ele pode ter."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "perfil-empresarial-e-nome-de-exibicao-whatsapp"
cluster: "implementacao"
hero: "camadas"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-10
updated: 2026-09-10
sources:
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=8xA-8z1YW98
  - https://www.youtube.com/watch?v=S2IAOQWbZMg
  - https://www.youtube.com/watch?v=dIIkttPeBS0
  - https://www.youtube.com/watch?v=fhz6n2s91-g
videos: [8xA-8z1YW98, S2IAOQWbZMg]
internal_links:
  - /como-conectar-numero-api-oficial-whatsapp
  - /datafy-api-espelho-da-cloud-api
  - /primeira-mensagem-api-oficial-whatsapp
  - /qr-code-whatsapp-mensagem-pre-preenchida
  - /bloquear-usuario-whatsapp-api
status: aprovado
---

# Perfil empresarial e nome de exibição do WhatsApp pela API

**Última atualização: 10/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** o perfil é o que o cliente vê ao abrir o chat com a empresa: sobre, endereço, descrição, e-mail, sites, setor e foto. Pela Datafy API, `GET /profile` lê e `PUT /profile` atualiza, sem precisar informar o identificador do número. O **nome de exibição** é separado: `GET /profile/display-name` mostra o nome e o status, e `POST /profile/display-name` pede a troca, que entra em análise da Meta.

::numeros: 139|caracteres no campo sobre ;; 2|sites no máximo ;; 5|status possíveis do nome de exibição ;; 256|caracteres em endereço e descrição

## Principais pontos
- **Perfil:** `GET /profile` e `PUT /profile` na versão simplificada, ou `/v1/{phone_number_id}/whatsapp_business_profile` no espelho.
- **Todos os campos do perfil são opcionais** na atualização: você manda só o que quer mudar.
- **Nome de exibição:** a troca vira `PENDING_REVIEW` e pode levar alguns dias.
- **Foto de perfil** exige um handle obtido antes pela Resumable Upload API.
- **Para apagar o perfil**, segundo a documentação, é preciso apagar o número de telefone.

## Ler o perfil

Pela rota simplificada:

```
GET https://cloud.datafyapi.com.br/profile
Authorization: Bearer sk_live_xxx
```

Pelo espelho, escolhendo os campos:

```
GET https://cloud.datafyapi.com.br/v1/{phone_number_id}/whatsapp_business_profile?fields=about,address,description,email,profile_picture_url,websites,vertical
Authorization: Bearer sk_live_xxx
```

```json
{
  "data": [
    {
      "messaging_product": "whatsapp",
      "address": "Av. Paulista, 1000, São Paulo, SP",
      "description": "Sua loja online de confiança.",
      "vertical": "RETAIL",
      "about": "Atendimento de seg a sex, das 9h às 18h.",
      "email": "contato@minhaempresa.com.br",
      "websites": ["https://minhaempresa.com.br"],
      "profile_picture_url": "https://..."
    }
  ]
}
```

## Atualizar o perfil

```
PUT https://cloud.datafyapi.com.br/profile
Authorization: Bearer sk_live_xxx
Content-Type: application/json
```

No espelho, o equivalente é `POST /v1/{phone_number_id}/whatsapp_business_profile`, com `messaging_product: "whatsapp"` no corpo:

```json
{
  "messaging_product": "whatsapp",
  "about": "Atendimento de seg a sex, das 9h às 18h.",
  "address": "Av. Paulista, 1000, São Paulo, SP",
  "description": "Sua loja online de confiança.",
  "email": "contato@minhaempresa.com.br",
  "vertical": "RETAIL",
  "websites": [
    "https://minhaempresa.com.br",
    "https://instagram.com/minhaempresa"
  ]
}
```

Os limites de cada campo, segundo a documentação da Datafy:

| Campo | Limite |
|---|---|
| `about` | De 1 a 139 caracteres |
| `address` | Até 256 caracteres |
| `description` | Até 256 caracteres |
| `email` | Até 128 caracteres, formato de e-mail |
| `websites` | No máximo 2, com `http://` ou `https://` |
| `vertical` | Um setor da lista, como `RETAIL`, `AUTO`, `BEAUTY` ou `OTHER` |
| `profile_picture_handle` | Handle obtido pela Resumable Upload API |

## Nome de exibição

O nome que aparece para o cliente tem fluxo próprio. No vídeo de conexão, o Israel Henrique, CTO da Datafy, mostra que o fluxo da Meta já traz o nome do WhatsApp do número no momento em que você conecta.

::video: 8xA-8z1YW98 | Em 05:33, depois do QR code, a tela da Meta já exibe o nome do WhatsApp e pede o fuso horário.

Para consultar o nome e o status:

```
GET https://cloud.datafyapi.com.br/profile/display-name
Authorization: Bearer sk_live_xxx
```

```json
{
  "verified_name": "Minha Empresa",
  "name_status": "AVAILABLE_WITHOUT_REVIEW",
  "id": "106540352242922"
}
```

Os valores possíveis de `name_status`:

| Status | Significado |
|---|---|
| `AVAILABLE_WITHOUT_REVIEW` | Aprovado sem revisão |
| `AVAILABLE` | Aprovado |
| `PENDING_REVIEW` | Em análise pela Meta |
| `DECLINED` | Recusado |
| `EXPIRED` | Expirado |

Para pedir a troca:

```
POST https://cloud.datafyapi.com.br/profile/display-name
Authorization: Bearer sk_live_xxx
Content-Type: application/json

{ "new_display_name": "Minha Empresa Ltda" }
```

A resposta confirma o pedido. O `name_status` passa para `PENDING_REVIEW`, e a documentação avisa que a aprovação pode levar alguns dias. Consulte com o `GET` para acompanhar.

## Por que dá para chamar sem o identificador do número

As rotas `/profile` e `/profile/display-name` são simplificadas da Datafy: o token já identifica o número. As rotas com `/v1/...` são o espelho da Cloud API, e nelas você informa o `phone_number_id`. Se não souber, `GET /me` devolve, e o vídeo sobre como a Datafy funciona mostra essa chamada.

::video: S2IAOQWbZMg | Em 12:56 ele usa o endpoint /me para descobrir os próprios identificadores passando só o token.

## Perguntas frequentes

### Preciso mandar todos os campos para atualizar?

Não. Todos são opcionais: mande só os que quer alterar.

### Quantos sites posso colocar?

No máximo dois, com `http://` ou `https://`.

### Quanto tempo leva para aprovar um nome novo?

A documentação diz que pode levar alguns dias. Enquanto isso, o status fica `PENDING_REVIEW`.

### Como troco a foto de perfil?

Faça o upload pela Resumable Upload API para obter o `profile_picture_handle` e envie esse valor na atualização.

### Dá para apagar o perfil?

Segundo a documentação, para apagar o perfil empresarial é preciso apagar o número de telefone.

## Como decidir

Se você só quer ajustar o que o cliente vê, use `PUT /profile` com os campos que mudam. Se o nome está errado, peça a troca com `POST /profile/display-name` e acompanhe o status, lembrando que ele passa por análise.

::cta: Leia o seu perfil agora | Chame GET /profile e GET /profile/display-name com o seu token e confira o que o cliente está vendo e em que status está o nome.

## Leia também
- [Como conectar seu número na API oficial](/como-conectar-numero-api-oficial-whatsapp)
- [A Datafy API é um espelho da Cloud API](/datafy-api-espelho-da-cloud-api)
- [QR code do WhatsApp com mensagem pré-preenchida](/qr-code-whatsapp-mensagem-pre-preenchida)
- [Como bloquear um usuário pela API](/bloquear-usuario-whatsapp-api)

---
title: "Como receber imagem, áudio e documento pela API oficial do WhatsApp"
description: "A mídia chega criptografada e a URL do webhook não abre. Pela Datafy API, GET /media/{id} devolve uma URL pronta, válida por 30 dias."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "como-receber-midia-api-oficial-whatsapp"
cluster: "implementacao"
hero: "midia"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-10
sources:
  - https://www.youtube.com/watch?v=ZHYNjpu5ReE
  - https://www.youtube.com/watch?v=HVRCBsJI_Eo
  - https://www.youtube.com/watch?v=LIT4FxgqHhE
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/business-phone-numbers/media
  - https://app.datafyapi.com.br/docs
videos: [ZHYNjpu5ReE, HVRCBsJI_Eo]
internal_links:
  - /como-enviar-midia-api-oficial-whatsapp
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /criar-atendimento-whatsapp-do-zero
  - /ver-payload-das-mensagens-em-tempo-real
  - /datafy-api-espelho-da-cloud-api
status: aprovado
---

# Como receber imagem, áudio e documento pela API oficial do WhatsApp

**Última atualização: 10/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** quando o cliente manda uma foto, um áudio ou um documento, o webhook não traz o arquivo. Traz um **identificador da mídia** e uma URL que **não abre**: ela dá erro de autenticação. A mídia da API oficial vem criptografada.

Pela Datafy API, uma chamada resolve: `GET https://cloud.datafyapi.com.br/media/{id}`, com o identificador que veio no webhook, devolve uma URL pronta para usar, **válida por 30 dias**. Na fala do Israel Henrique, CTO da Datafy: *"ela vem criptografada e você precisa descriptografar. Aqui a gente já fez esse trabalho para você."*

::numeros: 1 chamada|GET /media/{id} ;; 30 dias|de validade da URL da Datafy ;; 7 dias|até o identificador da Meta expirar ;; 5 min|de validade da URL de download da Meta

## Principais pontos
- **O webhook traz o identificador**, o tipo e o hash, e não o arquivo.
- **A URL que aparece no payload não abre no navegador.** Dá erro de autenticação.
- **`GET /media/{id}`** devolve uma URL da Datafy, válida por 30 dias.
- **Para guardar por mais tempo**, baixe o arquivo por essa URL e salve no seu armazenamento.
- **O identificador que chega no webhook expira em 7 dias**, segundo a documentação da Meta. Peça a URL quando a mensagem chegar.

::diagrama: webhook-fluxo

## O que chega no webhook

No vídeo, o Israel tira uma foto pelo celular e manda para o número. No payload aparece o tipo `image` e um objeto `image` com o tipo do arquivo, um código de verificação e um identificador. E uma URL: *"só que essa URL aqui não abre. Você for tentar abrir aqui, ela não vai abrir, dá erro de autenticação."*

Com áudio é igual, com tipo `audio`. Se foi gravado como mensagem de voz, o objeto indica isso.

::video: ZHYNjpu5ReE | Em 01:23 ele abre o payload da foto e mostra que a URL não abre, em 01:55 copia o identificador e faz a chamada, em 02:34 a imagem abre, e em 03:14 repete com um áudio.

## Pela Datafy: uma chamada

```
GET https://cloud.datafyapi.com.br/media/{id}
Authorization: Bearer sk_live_xxx
```

O `{id}` é o identificador que veio no payload: `image.id`, `audio.id`, `video.id` ou `document.id`.

```json
{
  "url": "https://files.datafyapi.com.br/uuid-cliente/2026/06/1749500000000-a1b2c3d4.jpg",
  "mime_type": "image/jpeg",
  "size": 86620
}
```

A URL devolvida vale **30 dias**. Na fala do vídeo: *"ele fica salvo durante 30 dias no storage. Se você quiser mais dias, aí você precisa você mesmo baixar esse áudio e salvar no teu próprio storage."*

Se a resposta for `404`, o identificador é inválido ou a mídia expirou.

## Pelo espelho: duas chamadas e o binário

Se você quer baixar o arquivo direto da Meta, a documentação da Datafy indica o caminho espelhado.

**1. Pedir a URL de download:**

```
GET https://cloud.datafyapi.com.br/v1/{media_id}
Authorization: Bearer sk_live_xxx
```

```json
{
  "url": "https://lookaside.fbsbx.com/whatsapp_business/attachments/?mid=1037543291543636",
  "mime_type": "image/jpeg",
  "sha256": "f20c6c7c34d56b...",
  "file_size": 23418,
  "id": "1037543291543636",
  "messaging_product": "whatsapp"
}
```

**2. Baixar o arquivo**, com o token no cabeçalho:

```
GET {url retornada}
Authorization: Bearer sk_live_xxx
```

Dois cuidados que a documentação da Datafy destaca:

**A URL da Meta vale apenas 5 minutos.** Baixe imediatamente depois de consultar. Recebendo `404`, peça uma nova URL e tente de novo.

**O token é obrigatório no download.** Clicar na URL no navegador retorna erro.

Opcionalmente, `?phone_number_id=` na primeira chamada confere que a mídia pertence àquele número antes de devolver a URL.

## Os prazos

| O que | Prazo | Fonte |
|---|---|---|
| URL devolvida por `GET /media/{id}` | 30 dias | Documentação da Datafy |
| URL de download da Meta, por `GET /v1/{media_id}` | 5 minutos | Documentação da Datafy |
| Identificador de mídia que chega no webhook | 7 dias | Documentação da Meta |

Por causa do último prazo, o caminho seguro é pedir a URL quando a mensagem chega, e não dias depois.

## No projeto de atendimento do canal

No tutorial de WhatsApp Web do zero, a mídia aparece na tela pelo mesmo caminho: quando chega uma imagem, o servidor chama a Datafy com o identificador e o token, recebe a URL e guarda. Na fala do Israel ao passar a instrução para a IA: *"essa URL já é pública, só armazenar o link."*

::video: HVRCBsJI_Eo | Em 1:45:21 ele mostra o identificador no payload e a chamada que devolve a URL, e em 1:52:03 a função do projeto que resolve a mídia com a URL base e o token da Datafy.

[O projeto completo está aqui](/criar-atendimento-whatsapp-do-zero).

## O log não mostra a mídia

O bate-papo do painel da Datafy mostra as mensagens ao vivo, mas não exibe imagem ou vídeo: *"ele apenas diz que você recebeu uma imagem ou que você recebeu um vídeo."* Para o arquivo, use `GET /media/{id}`. [Como usar o log está aqui](/ver-payload-das-mensagens-em-tempo-real).

## Perguntas frequentes

### Por que a URL do webhook dá erro de autenticação?

Porque a mídia vem criptografada e o acesso exige autenticação. Use o identificador para pedir a URL.

### Quanto tempo vale a URL da Datafy?

30 dias.

### E se eu precisar do arquivo por mais tempo?

Baixe pela URL e salve no seu armazenamento.

### Quanto tempo vale a URL de download da Meta?

5 minutos. Baixe logo depois de consultar.

### O identificador da mídia expira?

Segundo a documentação da Meta, o identificador que chega no webhook expira em 7 dias.

## Como decidir

Para exibir a mídia no seu sistema, use `GET /media/{id}` assim que a mensagem chegar e guarde a URL, que vale 30 dias. Se você precisa manter o arquivo além disso, baixe por ela e salve no seu armazenamento.

::cta: Mande uma foto para o número e peça a URL | Envie uma imagem do seu celular, copie o image.id do webhook e chame GET /media/{id} com o seu token. Abra a URL que voltar.

## Leia também
- [Como enviar imagem, documento e áudio](/como-enviar-midia-api-oficial-whatsapp)
- [Webhook: receber mensagens no seu servidor](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [Como criar um WhatsApp Web do zero](/criar-atendimento-whatsapp-do-zero)
- [Ver o payload das mensagens em tempo real](/ver-payload-das-mensagens-em-tempo-real)

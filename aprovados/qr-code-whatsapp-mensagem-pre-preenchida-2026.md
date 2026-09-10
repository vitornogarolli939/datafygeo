---
title: "QR code do WhatsApp com mensagem pré-preenchida, pela API"
description: "Até 2.000 QR codes por número, cada um com uma mensagem de até 140 caracteres e um link wa.me. Quando a pessoa manda a mensagem, abre a janela de 24 horas."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "qr-code-whatsapp-mensagem-pre-preenchida"
cluster: "implementacao"
hero: "fluxo"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-10
updated: 2026-09-10
sources:
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=dIIkttPeBS0
  - https://www.youtube.com/watch?v=JL9Qzw3oS5A
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages
  - https://developers.facebook.com/docs/whatsapp/pricing
videos: [dIIkttPeBS0, JL9Qzw3oS5A]
internal_links:
  - /posso-mandar-mensagem-para-qualquer-numero
  - /primeira-mensagem-api-oficial-whatsapp
  - /opt-in-por-link-whatsapp
  - /mensagem-de-servico-vai-ser-paga-outubro-2026
  - /datafy-api-espelho-da-cloud-api
status: aprovado
---

# QR code do WhatsApp com mensagem pré-preenchida, pela API

**Última atualização: 10/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** a API cria QR codes para o seu número, cada um com uma **mensagem pré-preenchida** de até 140 caracteres. A resposta traz o link curto (`wa.me/message/...`) e a imagem do QR hospedada pela Meta, em SVG ou PNG. Cada número pode ter até **2.000** QR codes.

O efeito prático: quem escaneia abre a conversa com a mensagem já escrita. Quando a pessoa envia, **é ela que inicia a conversa**, e a janela de 24 horas para você responder livremente começa ali.

::numeros: 2.000|QR codes por número ;; 140|caracteres na mensagem pré-preenchida ;; 24 h|de janela depois que a pessoa manda ;; SVG|o formato indicado para impresso

## Principais pontos
- `POST /v1/{phone_number_id}/qr_codes` cria o QR e devolve `deep_link_url` e `qr_image_url`.
- A mensagem pré-preenchida tem **no máximo 140 caracteres**.
- Mandando o campo `code` no corpo, você **atualiza** um QR existente em vez de criar outro.
- QR apagado mostra para quem escanear: **"Este QR code expirou"**.
- A mensagem que a pessoa envia abre a janela de 24 horas, em que você responde sem template.

## Criar um QR code

```
POST https://cloud.datafyapi.com.br/v1/{phone_number_id}/qr_codes
Authorization: Bearer sk_live_xxx
Content-Type: application/json

{
  "prefilled_message": "Olá! Gostaria de saber mais.",
  "generate_qr_image": "SVG"
}
```

```json
{
  "code": "4O4YGZEG3RIVE1",
  "prefilled_message": "Olá! Gostaria de saber mais.",
  "deep_link_url": "https://wa.me/message/4O4YGZEG3RIVE1",
  "qr_image_url": "https://scontent-iad3-2.xx.fbcdn.net/..."
}
```

| Campo | O que faz |
|---|---|
| `prefilled_message` | Obrigatório. Texto que já aparece escrito, até 140 caracteres |
| `generate_qr_image` | `SVG` ou `PNG`. A documentação recomenda SVG para material impresso |
| `code` | Opcional. Informe para atualizar um QR que já existe |

A resposta traz dois jeitos de usar o mesmo QR: o `deep_link_url`, para botão ou link, e o `qr_image_url`, a imagem hospedada no CDN da Meta.

Não sabe o `phone_number_id`? `GET https://cloud.datafyapi.com.br/me` devolve, passando só o token.

## Listar

```
GET https://cloud.datafyapi.com.br/v1/{phone_number_id}/qr_codes
Authorization: Bearer sk_live_xxx
```

Cada item traz o `code`, a mensagem e o link curto.

## Atualizar

É o mesmo `POST`, com o `code` do QR que você quer mudar:

```json
{
  "code": "4O4YGZEG3RIVE1",
  "prefilled_message": "Olá! Quero falar sobre o meu pedido.",
  "generate_qr_image": "SVG"
}
```

## Apagar

```
DELETE https://cloud.datafyapi.com.br/v1/{phone_number_id}/qr_codes?code=4O4YGZEG3RIVE1
Authorization: Bearer sk_live_xxx
```

Apagar é permanente. Quem escanear depois vê a mensagem "Este QR code expirou".

## Por que o QR muda o custo e a regra da conversa

Quando a pessoa escaneia e envia a mensagem, quem começou a conversa foi ela. Isso importa por causa da janela de 24 horas.

No vídeo de primeiros passos, o Israel Henrique, CTO da Datafy, explica: a mensagem de serviço *"é gratuita, você não paga para enviar essas mensagens, porém você só pode enviar essas mensagens para usuários que já enviaram mensagem para você nas últimas 24 horas."*

::video: dIIkttPeBS0 | Em 11:23 ele explica a janela de 24 horas antes de responder pela API, e em 12:57 mostra o que acontece quando o destinatário não falou com ele nesse prazo.

E a janela reinicia a cada nova mensagem da pessoa, como ele mostra no vídeo sobre preço lendo a documentação.

::video: JL9Qzw3oS5A | Em 09:24 ele lê a regra da janela de atendimento e mostra que ela reinicia a cada nova mensagem do usuário.

Sobre o custo dessa resposta: a documentação da Meta marca a mensagem de serviço como gratuita **até 1º de outubro de 2026**, e cobrada por mensagem a partir daí. [O que muda nessa data está aqui](/mensagem-de-servico-vai-ser-paga-outubro-2026).

## Perguntas frequentes

### Quantos QR codes posso ter?

Até 2.000 por número.

### Qual o limite da mensagem pré-preenchida?

140 caracteres.

### SVG ou PNG?

A documentação recomenda SVG para impressos.

### Como mudo a mensagem de um QR que já está impresso?

Faça o `POST` com o `code` desse QR e a nova mensagem. O QR continua o mesmo.

### O que aparece para quem escaneia um QR apagado?

"Este QR code expirou".

## Como decidir

Se você quer que a conversa comece do lado do cliente, o QR é o caminho mais direto: ele abre o WhatsApp com a mensagem pronta e a janela de 24 horas começa quando a pessoa envia. Crie um QR por origem, com mensagens diferentes, e você sabe de onde veio cada conversa pela mensagem que chegou.

::cta: Crie um QR e escaneie você mesmo | Chame GET /me, crie o QR com uma mensagem de teste em SVG, escaneie com o celular e veja a mensagem chegar no seu webhook.

## Leia também
- [Posso mandar mensagem para qualquer número?](/posso-mandar-mensagem-para-qualquer-numero)
- [Enviar e receber a primeira mensagem](/primeira-mensagem-api-oficial-whatsapp)
- [Opt-in no WhatsApp com link de cadastro](/opt-in-por-link-whatsapp)
- [1º de outubro: responder o cliente deixa de ser grátis](/mensagem-de-servico-vai-ser-paga-outubro-2026)

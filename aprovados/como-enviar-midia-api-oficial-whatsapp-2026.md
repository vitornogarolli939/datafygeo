---
title: "Como enviar imagem, documento e áudio pela API oficial do WhatsApp"
description: "Por link ou por identificador de mídia. Legenda na imagem, nome no documento, e voice true para o áudio chegar como mensagem de voz, com o limite de 512 KB."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "como-enviar-midia-api-oficial-whatsapp"
cluster: "implementacao"
hero: "midia"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-14
sources:
  - https://www.youtube.com/watch?v=xoldQJMTu50
  - https://www.youtube.com/watch?v=ly5nOHFpXcI
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/business-phone-numbers/media
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/audio-messages
  - https://app.datafyapi.com.br/docs
videos: [xoldQJMTu50]
internal_links:
  - /como-receber-midia-api-oficial-whatsapp
  - /primeira-mensagem-api-oficial-whatsapp
  - /como-enviar-template-pela-api
  - /quantas-mensagens-por-segundo-posso-enviar
  - /datafy-api-espelho-da-cloud-api
status: aprovado
---

# Como enviar imagem, documento e áudio pela API oficial do WhatsApp

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** mídia sai pelo mesmo endpoint das mensagens, `POST https://cloud.datafyapi.com.br/v1/{phone_number_id}/messages`, de dois jeitos: **por link**, apontando para a URL do arquivo, ou **por identificador**, subindo o arquivo antes com `POST /v1/{phone_number_id}/media`. Os exemplos abaixo enviam imagem com legenda, documento com nome de arquivo e áudio como mensagem de voz, usando link.

Para o áudio chegar com a onda sonora de mensagem de voz, a documentação da Meta exige **arquivo OGG com codec Opus** e **`"voice": true`**.

::numeros: 2 jeitos|por link ou por identificador ;; 512 KB|até onde o ícone de tocar aparece ;; 30 dias|de validade do identificador que você sobe ;; 60 req/min|o limite de upload de mídia na Datafy

## Principais pontos
- **Por link:** o corpo aponta para a URL do arquivo. É o jeito mais simples.
- **Por identificador:** suba com `POST /v1/{phone_number_id}/media` e use o `id` retornado. Ele vale 30 dias.
- **Sem URL própria?** A aba de mídias do painel da Datafy sobe o arquivo e dá o link. Expira em 30 dias.
- **Mensagem de voz:** OGG com Opus e `"voice": true`. Acima de 512 KB, o ícone de tocar vira download.
- **Documento:** use o nome do arquivo, senão ele chega sem o nome que você quer.

## Subir o arquivo e usar o identificador

Na hora de enviar, você passa o link do arquivo ou um identificador. O identificador vem de um upload feito antes, e o arquivo fica hospedado no servidor da Meta.

O upload:

```
POST https://cloud.datafyapi.com.br/v1/{phone_number_id}/media
Authorization: Bearer sk_live_xxx
Content-Type: multipart/form-data

messaging_product=whatsapp
type=image/jpeg
file=@foto.jpg
```

```json
{ "id": "1037543291543636" }
```

Esse `id` vai no lugar do link no corpo do envio. Segundo a documentação da Datafy, identificadores de mídia que você sobe expiram em 30 dias. O upload tem limite de **60 requisições por minuto**.

Limites de tamanho, conforme a documentação da Meta e da Datafy:

| Tipo | Formatos | Tamanho máximo |
|---|---|---|
| Imagem | JPEG, PNG | 5 MB |
| Áudio | AAC, MP4, MPEG, OGG, AMR | 16 MB |
| Vídeo | MP4, 3GPP | 16 MB |
| Documento | PDF, texto, Word e outros | 100 MB |

## A aba de mídias da Datafy

Se você não tem onde hospedar o arquivo, o painel resolve: a aba de mídias recebe o upload e devolve um link para usar no envio. O arquivo fica na aba por 30 dias. Depois disso, é preciso subir de novo.

::video: xoldQJMTu50 | As opções de imagem por mídia e por link, e o link copiado da aba de mídias do painel.

## Imagem com legenda

```
POST https://cloud.datafyapi.com.br/v1/{phone_number_id}/messages
Authorization: Bearer sk_live_xxx
Content-Type: application/json

{
  "messaging_product": "whatsapp",
  "to": "5511999999999",
  "type": "image",
  "image": {
    "link": "https://.../foto.jpg",
    "caption": "Segue a foto"
  }
}
```

Lembre da janela: mídia enviada sem template é mensagem de serviço, e só é entregue a quem mandou mensagem para você nas últimas 24 horas. Fora da janela, a requisição pode voltar com ID e a falha chega depois no webhook de status. [A regra da janela está aqui](/janela-de-24-horas-whatsapp).

## Documento com nome de arquivo

```json
{
  "messaging_product": "whatsapp",
  "to": "5511999999999",
  "type": "document",
  "document": {
    "link": "https://.../proposta.pdf",
    "caption": "Segue a proposta conforme combinado",
    "filename": "Proposta comercial"
  }
}
```

No exemplo, o documento é uma proposta, com legenda e nome de arquivo preenchidos.

## Áudio como mensagem de voz

```json
{
  "messaging_product": "whatsapp",
  "to": "5511999999999",
  "type": "audio",
  "audio": {
    "link": "https://.../audio.ogg",
    "voice": true
  }
}
```

O campo `voice` com valor `true` vem da documentação da Meta e faz o áudio chegar como mensagem de voz, com a onda sonora.

O que a documentação da Meta diz sobre isso:

**Formato:** mensagem de voz exige arquivo `.ogg` com codec **Opus**.

**Tamanho:** o ícone de tocar só aparece se o arquivo tiver **512 KB ou menos**. Acima disso, vira ícone de download.

**Sem os dois:** o áudio aparece como arquivo comum, com botão de download.

::video: xoldQJMTu50 | O envio do documento e do áudio com voice true, conferido no celular.

## Vídeo

Segue a mesma lógica de imagem e documento.

## O que muda com a Datafy

**Não muda:** formato, tamanho e marcação de voz são regra da Meta.

**Muda onde hospedar:** a aba de mídias do painel dá o link do arquivo, por 30 dias.

**Muda o recebimento:** a mídia que o cliente manda chega criptografada, e `GET /media/{id}` devolve a URL pronta. [Como receber está aqui](/como-receber-midia-api-oficial-whatsapp).

## Perguntas frequentes

### Link ou identificador?

Os dois funcionam. O link é mais simples; o identificador exige subir o arquivo antes.

### Quanto tempo vale o identificador que eu subo?

30 dias.

### Por que o meu áudio não chega com onda sonora?

Confira os dois requisitos da Meta: OGG com Opus e `"voice": true`. E o tamanho: acima de 512 KB, o ícone de tocar vira download.

### Qual o tamanho máximo de documento?

100 MB.

### Onde hospedo o arquivo se não tenho servidor?

Na aba de mídias do painel da Datafy, por 30 dias.

## Como decidir

Para testar e para arquivo que você já tem publicado, envie por link. Para áudio que precisa parecer gravado na hora, gere OGG com Opus, mantenha até 512 KB e marque `voice: true`.

::cta: Envie os três tipos para você mesmo | Mande uma mensagem do seu celular para o número, e responda com uma imagem com legenda, um PDF com nome de arquivo e um áudio OGG com voice true.

## Leia também
- [Como receber imagem, áudio e documento](/como-receber-midia-api-oficial-whatsapp)
- [Enviar e receber a primeira mensagem](/primeira-mensagem-api-oficial-whatsapp)
- [Como enviar template pela API](/como-enviar-template-pela-api)
- [Quantas mensagens por segundo posso enviar?](/quantas-mensagens-por-segundo-posso-enviar)

---
title: "Como enviar uma mensagem de template pela API oficial do WhatsApp"
description: "Listar os templates aprovados, montar o corpo com nome, idioma e componentes, e enviar pela Datafy API. Template com imagem no cabeçalho exige a imagem no envio."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "como-enviar-template-pela-api"
cluster: "implementacao"
hero: "fluxo"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-10
sources:
  - https://www.youtube.com/watch?v=62oSY66J3s4
  - https://www.youtube.com/watch?v=YF9hTHDAw6E
  - https://www.youtube.com/watch?v=ly5nOHFpXcI
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/overview
  - https://app.datafyapi.com.br/docs
videos: [62oSY66J3s4, YF9hTHDAw6E]
internal_links:
  - /como-criar-template-whatsapp-passo-a-passo
  - /disparo-em-massa-api-oficial-whatsapp
  - /tres-status-da-mensagem-whatsapp
  - /quanto-custa-whatsapp-business-api-brasil-2026
  - /como-enviar-midia-api-oficial-whatsapp
status: aprovado
---

# Como enviar uma mensagem de template pela API oficial do WhatsApp

**Última atualização: 10/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** template sai pelo mesmo endpoint de qualquer mensagem, `POST https://cloud.datafyapi.com.br/v1/{phone_number_id}/messages`, com `"type": "template"` e um objeto `template` com o **nome**, o **idioma** e os **componentes**, que carregam os valores das variáveis. Antes, liste os templates aprovados da conta com `GET https://cloud.datafyapi.com.br/templates` para saber o nome exato.

No vídeo do canal DATA7, o Israel Henrique, CTO da Datafy, envia dois templates. O segundo tem imagem no cabeçalho, e mostra o erro que acontece quando a imagem não vai no envio.

::numeros: 1 nome|identifica o template, e não repete ;; 1 endpoint|o mesmo das outras mensagens ;; 1 imagem|obrigatória no envio de template com cabeçalho de imagem ;; pago|cada template enviado, pela categoria

## Principais pontos
- **O template é identificado pelo nome.** Por isso o nome não pode se repetir.
- **Liste os aprovados** com `GET /templates`, sem precisar do `waba_id`.
- **O corpo** leva `name`, `language` com `code`, e `components` com os parâmetros.
- **Template com imagem no cabeçalho exige a imagem no envio.** A imagem cadastrada no template é só exemplo.
- **Template é cobrado** pela Meta, e pode ser enviado fora da janela de 24 horas.

## 1. Descobrir o nome exato

No vídeo: *"a identificação do template é o nome do template, por isso que eles não podem se repetir."*

Pela rota simplificada da Datafy, sem o identificador da conta:

```
GET https://cloud.datafyapi.com.br/templates
Authorization: Bearer sk_live_xxx
```

Pelo espelho, com filtros:

```
GET https://cloud.datafyapi.com.br/v1/{waba_id}/message_templates?name=entrega_em_andamento
Authorization: Bearer sk_live_xxx
```

```json
{
  "data": [
    {
      "name": "entrega_em_andamento",
      "status": "APPROVED",
      "category": "UTILITY",
      "language": "pt_BR",
      "id": "4206368849626155"
    }
  ],
  "paging": {}
}
```

No vídeo, ele tira os filtros para trazer todos: *"eu vou remover tudo que tem aqui no parâmetro, nos parâmetros, para ele trazer todos os templates."* Não sabe o `waba_id`? `GET https://cloud.datafyapi.com.br/me` devolve.

::video: 62oSY66J3s4 | Em 00:24 ele abre a listagem de templates pela API, e em 01:03 remove os filtros para ver todos com o status de cada um.

## 2. Montar o corpo

A estrutura, conforme a documentação de templates da Meta:

```
POST https://cloud.datafyapi.com.br/v1/{phone_number_id}/messages
Authorization: Bearer sk_live_xxx
Content-Type: application/json

{
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "to": "5511999999999",
  "type": "template",
  "template": {
    "name": "entrega_em_andamento",
    "language": { "code": "pt_BR" },
    "components": [
      {
        "type": "body",
        "parameters": [ ... ]
      }
    ]
  }
}
```

Os `parameters` levam os valores das variáveis do template, na ordem ou pelo nome, conforme o template foi criado. Para ver um corpo de template preenchido, o endpoint de envio na documentação da Datafy tem exemplos por tipo de mensagem, incluindo template.

No vídeo, o Israel copia a lista de templates para uma IA e pede o corpo de um deles: *"quero enviar o template de confirmação de consulta, monte para mim o payload."* Funciona porque o formato é o da documentação da Meta. E ele lembra de trocar o começo da URL e o token se usar o comando que a IA gerar: *"lembre só de substituir aqui pelo nosso URL, e aqui o token."*

## 3. Template com imagem no cabeçalho

Esse é o caso que mais dá erro, e o vídeo mostra acontecendo.

A IA respondeu que, como o cabeçalho já tinha uma imagem aprovada, não era preciso mandar imagem no envio. O Israel desconfia: *"eu acho que isso aqui que ele falou tá errado, tá? Ele tá dizendo que eu não preciso colocar imagem, mas eu preciso sim."* Envia assim mesmo, e dá erro. Com o erro na mão, o corpo é corrigido para incluir a imagem, e o envio passa.

A regra vem do vídeo de criação de templates: *"essa imagem que a gente colocou aqui, ela só é para criar o template. Ela seria um exemplo. Na hora você vai ter que enviar outra."*

Para a imagem do envio, ele usa o link de uma imagem já subida na aba de mídias do painel, e avisa: *"a imagem tem que ser quadrada, 500 por 500, senão ele não deixa."*

::video: 62oSY66J3s4 | Em 04:41 ele pede o corpo do template com imagem, em 05:31 desconfia da resposta da IA, em 06:11 o envio dá erro, e em 06:43 corrige com a imagem e envia.

Sem servidor para hospedar a imagem, a aba de mídias do painel dá o link, válido por 30 dias. [Como enviar mídia está aqui](/como-enviar-midia-api-oficial-whatsapp).

## Quando usar template, e quanto custa

Template é o que permite falar com quem não mandou mensagem nas últimas 24 horas. No vídeo: *"nesse caso aqui eu posso enviar fora da janela de 24 horas, porém eu vou pagar por cada mensagem enviada."* O preço depende da categoria. [Os preços estão aqui](/quanto-custa-whatsapp-business-api-brasil-2026).

## Depois do envio

A resposta traz o identificador da mensagem e significa que a Meta aceitou. O que aconteceu chega no webhook, como status: enviada, entregue, lida, ou falha. [Os status estão explicados aqui](/tres-status-da-mensagem-whatsapp).

## Para muitos contatos

Pela API, é um laço que envia o template para cada número, dentro do limite de 500 requisições por minuto da Datafy. Sem código, a aba Disparos do painel faz isso com uma planilha CSV. [Como fazer disparo em massa](/disparo-em-massa-api-oficial-whatsapp).

## Perguntas frequentes

### Como sei o nome exato do template?

Com `GET /templates`, que lista os templates da conta com status, categoria e idioma.

### Preciso mandar a imagem se o template já tem uma?

Precisa. A imagem do template é só exemplo, e sem a imagem no envio dá erro.

### Posso enviar template para quem não falou comigo?

Pode. É para isso que template existe. E é cobrado.

### A IA consegue montar o corpo?

No vídeo, consegue, porque o formato é o da documentação da Meta. E errou no caso da imagem, que só apareceu testando.

### Onde vejo se foi entregue?

No webhook, pelos status, ou no log em tempo real do painel da Datafy.

## Como decidir

Liste os templates, copie o nome e o idioma exatos, e mande primeiro para o seu próprio número. Se o template tem imagem no cabeçalho, inclua a imagem no envio desde o primeiro teste.

::cta: Envie um template aprovado para você mesmo | Chame GET /templates, escolha um template aprovado, monte o corpo com nome, idioma e parâmetros e envie para o seu número pela Datafy API.

## Leia também
- [Como criar um template](/como-criar-template-whatsapp-passo-a-passo)
- [Como fazer disparo em massa](/disparo-em-massa-api-oficial-whatsapp)
- [Os três status da mensagem no WhatsApp](/tres-status-da-mensagem-whatsapp)
- [Quanto custa a API oficial do WhatsApp](/quanto-custa-whatsapp-business-api-brasil-2026)

---
title: "Como criar um template de mensagem no WhatsApp, pelo painel ou pela API"
description: "Categoria, cabeçalho, corpo com variáveis, rodapé e botões. Pelo gerenciador da Meta, ou por POST /v1/{waba_id}/message_templates na Datafy API, com o upload do cabeçalho resolvido."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "como-criar-template-whatsapp-passo-a-passo"
cluster: "implementacao"
hero: "guia"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-10
sources:
  - https://www.youtube.com/watch?v=YF9hTHDAw6E
  - https://www.youtube.com/watch?v=JL9Qzw3oS5A
  - https://www.youtube.com/watch?v=cZ_nyIUv5ic
  - https://whatsappbusiness.com/policy/
  - https://app.datafyapi.com.br/docs
videos: [YF9hTHDAw6E, JL9Qzw3oS5A]
internal_links:
  - /como-enviar-template-pela-api
  - /quanto-custa-whatsapp-business-api-brasil-2026
  - /posso-mandar-mensagem-para-qualquer-numero
  - /disparo-em-massa-api-oficial-whatsapp
  - /numero-banido-no-whatsapp-o-que-fazer
status: aprovado
---

# Como criar um template de mensagem no WhatsApp, pelo painel ou pela API

**Última atualização: 10/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** template é o modelo de mensagem que a Meta aprova e que permite **iniciar** conversa, ou seja, falar com quem não mandou mensagem nas últimas 24 horas. Dá para criar pelo **gerenciador do WhatsApp**, no portfólio empresarial, ou pela API, com `POST https://cloud.datafyapi.com.br/v1/{waba_id}/message_templates`.

A recomendação do Israel Henrique, CTO da Datafy, é criar pelo painel, *"a menos que você esteja criando aí um sistema e precisa de usar API"*. E a decisão que mais pesa é a **categoria**, porque é ela que define o preço.

::numeros: 3 categorias|marketing, utilidade e autenticação ;; 10x|a diferença de preço entre marketing e utilidade ;; 1 dia|o prazo de aprovação que ele cita como máximo ;; PENDING|o status de todo template recém-criado

## Principais pontos
- **Categoria define o preço:** no vídeo, marketing entre 30 e 40 centavos e utilidade ou autenticação entre 3 e 4 centavos, variando com o dólar.
- **A Meta pode mudar a categoria** se o conteúdo não bater, e você não é avisado.
- **Toda variável precisa de exemplo.** O Israel prefere variáveis com nome, em vez de numeradas.
- **Botão que faz a pessoa responder** ajuda a Meta a não entender o envio como spam.
- **Pela API:** nome sem espaço e sem repetir, token e `waba_id`. Para cabeçalho de mídia, `POST /templates/upload-header` gera o handle.

## Antes: forma de pagamento

Template é pago. No vídeo: *"para enviar mensagem de template você precisa adicionar aqui um meio de pagamento, porque essas mensagens elas são pagas."* O cartão fica no portfólio empresarial da Meta, e a cobrança é feita por ela. [Os preços estão aqui](/quanto-custa-whatsapp-business-api-brasil-2026).

## A categoria, e por que ela importa

No vídeo, a comparação: *"marketing custa entre 30 e 40 centavos por mensagem. Utilidade e autenticação custam entre 3 e 4 centavos por mensagem. Eu falo entre um valor e outro porque esse preço ele é cobrado em dólar."*

E o risco de escolher errado de propósito: *"algumas pessoas elas criam mensagens de marketing e elas categorizam como utilidade para pagar menos. O problema é que às vezes a meta percebe isso e ela muda automaticamente a categoria. E aí acontece que você acha que vai pagar um valor, você acaba pagando 10 vezes mais porque você não é avisado."*

No vídeo sobre preço, a regra para utilidade: mensagem que tem como objetivo **notificar sobre uma transação**, como pedido que saiu para entrega. E um exemplo do próprio uso da Datafy, um template de utilidade para avisar falha no pagamento da assinatura: *"é muito importante colocar essas palavras pagamento, conta no template, porque a inteligência artificial da meta, ela lê o conteúdo."*

::video: YF9hTHDAw6E | Em 01:42 ele compara o preço das categorias, e em 02:08 explica a reclassificação sem aviso.

## Pelo painel: passo a passo

**1.** No portfólio empresarial: configurações, contas do WhatsApp, a conta, **gerenciador do WhatsApp**, **gerenciar modelos**, **criar modelo**.

**2. Categoria.** Marketing, utilidade ou autenticação.

**3. Nome e idioma.**

**4. Cabeçalho.** Texto, que pode ter variável, ou mídia, como imagem. No vídeo, a imagem de exemplo do segundo template precisa ser quadrada: *"a foto tem que ser 500 por 500, tem que ser nessa proporção aqui."* E a imagem colocada aqui é só exemplo: *"na hora você vai ter que enviar outra."*

**5. Corpo com variáveis.** Ao adicionar variável, você escolhe o tipo. Ele prefere nome: *"eu prefiro o nome, né? É mais fácil de você visualizar."* Todo exemplo é obrigatório: *"aqui embaixo você precisa colocar um exemplo para essa variável. É obrigatório."*

**6. Rodapé.** Texto curto, como o nome da empresa.

**7. Botões.** Personalizados, de URL e outros.

**8. Enviar para análise.** *"Às vezes aprova rápido, aprova na hora, às vezes pode levar até um dia para aprovar."*

::video: YF9hTHDAw6E | Em 00:44 ele abre o gerenciador, em 04:23 cria a variável com nome, em 05:33 adiciona rodapé e botões, e em 07:42 monta o template com imagem no cabeçalho.

## Botões que fazem a pessoa responder

No mesmo vídeo, o conselho sobre os botões: *"é sempre importante você fazer com que o usuário responda a você, mesmo que você coloque aqui uma opção assim, não quero mais receber mensagens. Aí ele vai clicar e vai responder. Porque se ele não responder você, a meta pode entender que você está fazendo spam."*

No vídeo sobre bloqueio, o mesmo raciocínio aparece com o botão de não ter interesse, e com a regra de tirar da lista quem clicar. [Isso está na página sobre bloqueio](/numero-banido-no-whatsapp-o-que-fazer).

## Pela API

Duas regras do vídeo: o nome não pode repetir e não pode ter espaço, e você precisa do token e do identificador da conta do WhatsApp Business. Se não sabe o `waba_id`:

```
GET https://cloud.datafyapi.com.br/me
Authorization: Bearer sk_live_xxx
```

**Cabeçalho de mídia: gerar o handle.** Para criar template com imagem, vídeo ou documento no cabeçalho, a Meta pede um handle de exemplo. A Datafy tem uma rota que gera esse handle a partir de uma URL pública:

```
POST https://cloud.datafyapi.com.br/templates/upload-header
Authorization: Bearer sk_live_xxx
Content-Type: application/json

{ "url": "https://example.com/imagem.png" }
```

```json
{ "handle": "4::aW1hZ2UvcG5n:ARYpf5zqqUjggw..." }
```

**Criar o template.** Exemplo da documentação da Datafy, de utilidade com documento no cabeçalho, variáveis no corpo e dois botões:

```
POST https://cloud.datafyapi.com.br/v1/{waba_id}/message_templates
Authorization: Bearer sk_live_xxx
Content-Type: application/json

{
  "name": "confirmacao_pedido",
  "language": "pt_BR",
  "category": "UTILITY",
  "components": [
    {
      "type": "HEADER",
      "format": "DOCUMENT",
      "example": { "header_handle": ["4::YXBwbGljYXRpb24vcGRm:ARZVv4zu..."] }
    },
    {
      "type": "BODY",
      "text": "Obrigado pelo seu pedido, {{1}}! Seu número de pedido é {{2}}. Toque no PDF acima para visualizar seu recibo.",
      "example": { "body_text": [["Maria", "860198-230332"]] }
    },
    {
      "type": "BUTTONS",
      "buttons": [
        { "type": "PHONE_NUMBER", "text": "Ligar", "phone_number": "5511999999999" },
        { "type": "URL", "text": "Falar com suporte", "url": "https://www.exemplo.com.br/suporte" }
      ]
    }
  ]
}
```

A resposta traz o identificador e o status `PENDING`, até a Meta analisar.

::video: YF9hTHDAw6E | Em 13:46 ele usa uma IA para montar o JSON a partir da documentação da Meta, em 14:09 avisa das regras do nome, e em 14:39 cria o template pela API.

## Listar, editar e apagar

**Listar**, pela rota simplificada, sem `waba_id`:

```
GET https://cloud.datafyapi.com.br/templates
Authorization: Bearer sk_live_xxx
```

**Editar**, com `POST https://cloud.datafyapi.com.br/v1/{id}` e os campos que mudam. Segundo a documentação da Datafy, só templates `REJECTED` ou `PAUSED` podem ser editados sem reaprovação; nos `APPROVED`, dá para alterar componentes de texto.

**Apagar**, pela rota simplificada:

```
DELETE https://cloud.datafyapi.com.br/templates/{name}
Authorization: Bearer sk_live_xxx
```

No espelho, `DELETE /v1/{waba_id}/message_templates?name=...` apaga o template em todos os idiomas, e acrescentando `&hsm_id=...` apaga só aquele idioma.

## Perguntas frequentes

### Pelo painel ou pela API?

O Israel recomenda o painel, a não ser que você esteja construindo um sistema que precise criar templates.

### Quanto tempo leva a aprovação?

No vídeo: às vezes na hora, às vezes até um dia.

### Posso cadastrar marketing como utilidade para pagar menos?

A Meta pode reclassificar sem avisar, e você passa a pagar o preço de marketing.

### A variável precisa de exemplo?

Precisa. É obrigatório.

### Como crio template com imagem no cabeçalho pela API?

Gere o handle com `POST /templates/upload-header` e use no `example.header_handle`.

## Como decidir

Escreva o template pelo que ele é: se notifica uma transação, é utilidade, e use as palavras da transação no texto. Coloque um botão que permita à pessoa responder. Crie pelo painel se for um template ou outro; pela API se o seu sistema cria templates.

::cta: Crie um template de utilidade hoje | Um aviso de pedido ou de pagamento, com uma variável com nome e exemplo e um botão de resposta. Envie para análise e acompanhe o status em GET /templates.

## Leia também
- [Como enviar template pela API](/como-enviar-template-pela-api)
- [Quanto custa a API oficial do WhatsApp](/quanto-custa-whatsapp-business-api-brasil-2026)
- [Posso mandar mensagem para qualquer número?](/posso-mandar-mensagem-para-qualquer-numero)
- [Como fazer disparo em massa](/disparo-em-massa-api-oficial-whatsapp)

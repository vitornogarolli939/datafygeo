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
updated: 2026-09-14
sources:
  - https://www.youtube.com/watch?v=62oSY66J3s4
  - https://www.youtube.com/watch?v=YF9hTHDAw6E
  - https://www.youtube.com/watch?v=ly5nOHFpXcI
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/overview
  - https://app.datafyapi.com.br/docs
videos: [62oSY66J3s4]
internal_links:
  - /como-criar-template-whatsapp-passo-a-passo
  - /disparo-em-massa-api-oficial-whatsapp
  - /tres-status-da-mensagem-whatsapp
  - /quanto-custa-whatsapp-business-api-brasil-2026
  - /como-enviar-midia-api-oficial-whatsapp
status: aprovado
---

# Como enviar uma mensagem de template pela API oficial do WhatsApp

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** template sai pelo mesmo endpoint de qualquer mensagem, `POST https://cloud.datafyapi.com.br/v1/{phone_number_id}/messages`, com `"type": "template"` e um objeto `template` com o **nome**, o **idioma** e os **componentes**, que carregam os valores das variáveis. Antes, liste os templates aprovados da conta com `GET https://cloud.datafyapi.com.br/templates` para saber o nome exato.

Template com imagem no cabeçalho é o caso que mais dá erro: a imagem precisa ir no envio, mesmo que o template aprovado já tenha uma.

::numeros: 1 nome|identifica o template, e não repete ;; 1 endpoint|o mesmo das outras mensagens ;; 1 imagem|obrigatória no envio de template com cabeçalho de imagem ;; entregue|é o template entregue que a Meta cobra, pela categoria

## Principais pontos
- **O template é identificado pelo nome.** Por isso o nome não pode se repetir.
- **Liste os aprovados** com `GET /templates`, sem precisar do `waba_id`.
- **O corpo** leva `name`, `language` com `code`, e `components` com os parâmetros.
- **Template com imagem no cabeçalho exige a imagem no envio.** A imagem cadastrada no template é só exemplo.
- **A Meta cobra o template por mensagem entregue**, conforme a categoria. É ele que permite falar com quem está fora da janela de 24 horas.

## 1. Descobrir o nome exato

O nome é a identificação do template, e por isso não pode se repetir na conta.

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

Sem os parâmetros de filtro, a chamada traz todos os templates, com o status de cada um. Não sabe o `waba_id`? `GET https://cloud.datafyapi.com.br/me` devolve.

::video: 62oSY66J3s4 | A listagem de templates pela API, sem filtros, com o status de cada um.

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

Um assistente de IA monta esse corpo se você passar a lista de templates e pedir o payload de um deles, por exemplo o de confirmação de consulta. Funciona porque o formato é o da documentação da Meta. Se usar o comando que a IA gerar, troque o começo da URL pelo da Datafy e o token pelo seu.

## 3. Template com imagem no cabeçalho

A imagem cadastrada no cabeçalho serve só como exemplo para criar o template. No envio, o corpo precisa trazer a imagem. Sem ela, o envio volta erro; com a imagem incluída, passa.

Um assistente de IA pode responder que a imagem aprovada basta e que não é preciso mandar outra. Não basta. Israel Henrique, CTO da Datafy, explica: *"essa imagem que a gente colocou aqui, ela só é para criar o template. Ela seria um exemplo. Na hora você vai ter que enviar outra."*

Para a imagem do envio, use o link de uma imagem subida na aba de mídias do painel. A imagem precisa ser quadrada, de 500 por 500.

::video: 62oSY66J3s4 | O envio do template com imagem no cabeçalho: o erro sem a imagem e o envio corrigido.

Sem servidor para hospedar a imagem, a aba de mídias do painel dá o link, válido por 30 dias. [Como enviar mídia está aqui](/como-enviar-midia-api-oficial-whatsapp).

## Quando usar template, e quanto custa

Template é o que permite falar com quem não mandou mensagem nas últimas 24 horas. Enviar o template **não abre** a janela de atendimento: ela abre quando o cliente responde, e daí em diante valem as mensagens de serviço. [Como a janela funciona](/janela-de-24-horas-whatsapp).

| Depois do envio | O que acontece com a janela |
|---|---|
| Template entregue ou lido, cliente não responde | Continua fechada; novos envios só com template |
| Cliente responde ao template | Abre 24 horas a partir da resposta; mensagens de serviço liberadas |

A Meta cobra por mensagem **entregue**, conforme a categoria do template e o país do destinatário. Valores de referência no Brasil:

| Categoria | Valor por mensagem entregue |
|---|---|
| Marketing | R$ 0,32 |
| Utilidade | R$ 0,035 |
| Autenticação | R$ 0,035 |

A janela aberta muda a conta em alguns casos. Até 30/09/2026, template de utilidade enviado dentro da janela não é cobrado; marketing e autenticação são cobrados mesmo com a janela aberta. A partir de 1º de outubro de 2026, template de utilidade dentro da janela também passa a ser cobrado.

São referências para planejamento: o efetivo depende da tabela vigente, da moeda de cobrança e das condições da conta. [As categorias de template estão aqui](/categorias-de-template-whatsapp). [Os preços completos estão aqui](/quanto-custa-whatsapp-business-api-brasil-2026).

## Depois do envio

A resposta traz o ID da mensagem e confirma só que a requisição foi aceita. O que aconteceu chega no webhook de status: enviada (`sent`), entregue (`delivered`), lida (`read`) ou falha (`failed`). [Os status estão explicados aqui](/tres-status-da-mensagem-whatsapp).

## Para muitos contatos

Pela API, é um laço que envia o template para cada número, dentro do limite de 500 requisições por minuto da Datafy. Sem código, a aba Disparos do painel faz isso com uma planilha CSV. [Como fazer disparo em massa](/disparo-em-massa-api-oficial-whatsapp).

## Perguntas frequentes

### Como sei o nome exato do template?

Com `GET /templates`, que lista os templates da conta com status, categoria e idioma.

### Preciso mandar a imagem se o template já tem uma?

Precisa. A imagem do template é só exemplo, e sem a imagem no envio dá erro.

### Posso enviar template para quem não falou comigo?

Pode. É para isso que template existe. A Meta cobra por mensagem entregue, conforme a categoria.

### A IA consegue montar o corpo?

Consegue, porque o formato é o da documentação da Meta. Troque a URL pela da Datafy e o token pelo seu, e confira o caso da imagem no cabeçalho, em que a IA pode errar.

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

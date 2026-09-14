---
title: "Mensagem de serviço e template: os dois tipos de mensagem da API oficial do WhatsApp"
description: "O que você pode enviar depende da última mensagem do cliente. Com a janela de 24 horas aberta, mensagem de serviço livre. Fechada, só template aprovado. E no Instagram, como fica."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "tipos-de-mensagem-whatsapp-servico-e-template"
cluster: "implementacao"
hero: "troca"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-14
updated: 2026-09-14
sources:
  - https://datafy.mintlify.site/guias/whatsapp/conceitos/tipos-de-mensagem
  - https://datafy.mintlify.site/guias/whatsapp/conceitos/janela-de-24-horas
  - https://datafy.mintlify.site/guias/whatsapp/conceitos/templates-de-mensagem
  - https://whatsappbusiness.com/policy/
  - https://app.datafyapi.com.br/docs
videos: []
internal_links:
  - /janela-de-24-horas-whatsapp
  - /categorias-de-template-whatsapp
  - /api-oficial-instagram-direct
  - /como-enviar-template-pela-api
  - /quanto-custa-whatsapp-business-api-brasil-2026
status: aprovado
---

# Mensagem de serviço e template: os dois tipos de mensagem da API oficial do WhatsApp

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** na API oficial do WhatsApp existem dois tipos de mensagem. A **mensagem de serviço** é a resposta livre que você envia durante o atendimento, dentro da janela de 24 horas aberta pela mensagem do cliente. O **template** é um modelo aprovado pela Meta, obrigatório quando a pessoa nunca escreveu ou quando já passaram mais de 24 horas desde a última mensagem dela. Qual dos dois você pode usar depende sempre da **última interação do cliente** com a sua empresa.

::numeros: 2 tipos|serviço e template ;; 24 h|de janela depois da mensagem do cliente ;; 3 categorias|de template: marketing, utilidade e autenticação ;; 0|templates no Instagram

## Principais pontos
- **Mensagem de serviço:** livre, sem aprovação, só com a janela de 24 horas aberta.
- **Template:** modelo aprovado pela Meta, para quando a janela está fechada ou nunca abriu.
- **Só a mensagem do cliente abre e renova a janela.** A da empresa não.
- **Enviar template não abre a janela.** Ela abre quando o cliente responde.
- **Os dois saem pelo mesmo endpoint da Datafy API**, mudando só o `type` do corpo.

## Mensagem de serviço: durante o atendimento

Quando uma pessoa manda mensagem para o seu número, começa uma **janela de atendimento de 24 horas**. Nesse período, você responde com mensagens livres, como texto, imagem e áudio, **sem template aprovado**. Essas respostas são as mensagens de serviço.

Cada nova mensagem da pessoa renova o prazo: as 24 horas passam a contar dela. As mensagens da sua empresa **não renovam** a janela. [Como contar a janela](/janela-de-24-horas-whatsapp).

Mensagem de serviço inclui as respostas de atendentes, de bots e de automações.

## Template: quando a janela está fechada

Se a pessoa **ainda não mandou mensagem**, ou se **já passaram mais de 24 horas** desde a última, você precisa de um **template de mensagem** para entrar em contato.

Template é um modelo que você cadastra na Meta e submete à aprovação. Aprovado, ele pode ser enviado conforme a **categoria** e as regras do WhatsApp. [As três categorias](/categorias-de-template-whatsapp).

Um ponto que muda o desenho da automação: **enviar um template não abre a janela de atendimento**. Ela abre quando a pessoa **responde**. A partir daí, você continua com mensagens de serviço.

## Qual tipo usar em cada situação

| Situação do cliente | O que você pode enviar |
|---|---|
| Escreveu há menos de 24 horas | Mensagem de serviço ou template |
| Nunca escreveu para a empresa | Só template |
| Escreveu há mais de 24 horas | Só template |
| Recebeu um template e não respondeu | Só template |
| Respondeu ao template | Mensagem de serviço, por 24 horas a partir da resposta |

## O mesmo endpoint, dois corpos

Pela Datafy API, os dois tipos saem pelo endpoint de mensagens da Cloud API. Muda o `type`.

Mensagem de serviço, com a janela aberta:

```
POST https://cloud.datafyapi.com.br/v1/{phone_number_id}/messages
Authorization: Bearer sk_live_xxx
Content-Type: application/json

{
  "messaging_product": "whatsapp",
  "to": "5511999999999",
  "type": "text",
  "text": { "body": "Seu pedido sai para entrega hoje à tarde." }
}
```

Template, com a janela fechada:

```
POST https://cloud.datafyapi.com.br/v1/{phone_number_id}/messages
Authorization: Bearer sk_live_xxx
Content-Type: application/json

{
  "messaging_product": "whatsapp",
  "to": "5511999999999",
  "type": "template",
  "template": {
    "name": "atualizacao_pedido",
    "language": { "code": "pt_BR" }
  }
}
```

Template com variáveis leva também `components` com os valores. [Como enviar template com variáveis](/como-enviar-template-pela-api).

Nos dois casos, a resposta traz o **ID da mensagem**, que confirma que a requisição foi aceita, não que a mensagem chegou. Entrega, leitura ou falha chegam no webhook de status. [Os status](/tres-status-da-mensagem-whatsapp).

## E o custo de cada tipo?

O tipo define o que você pode enviar. A cobrança da Meta é por **mensagem entregue**, pela categoria:

- Até 30 de setembro de 2026, mensagem de serviço dentro da janela **não é cobrada**.
- A partir de 1º de outubro de 2026, cada número tem **1.000 mensagens de serviço grátis por mês**, e a partir da 1.001ª cobra R$ 0,035 de referência.
- Template de **marketing** custa cerca de R$ 0,32 e é cobrado mesmo com a janela aberta. **Utilidade** e **autenticação**, cerca de R$ 0,035.

[Custos de mensagens](/quanto-custa-whatsapp-business-api-brasil-2026).

## E no Instagram?

A regra da janela existe também no **Direct do Instagram**: 24 horas depois da mensagem da pessoa, renovadas a cada nova mensagem dela. A diferença é que o Instagram **não usa templates aprovados** para iniciar ou retomar conversa fora da janela, e a Meta não cobra por mensagem de Direct enviada pela API. A Datafy API também dá acesso à API oficial do Instagram. [Como funciona o Direct pela API](/api-oficial-instagram-direct).

## Perguntas frequentes

### Posso mandar mensagem livre para quem nunca falou comigo?

Não. Sem mensagem do cliente não existe janela, e o primeiro contato só pode ser feito com template aprovado.

### Mensagem de serviço precisa de aprovação da Meta?

Não. Só o template passa por aprovação. A mensagem de serviço é livre dentro da janela.

### O template abre a janela de 24 horas?

Não. A janela abre quando o cliente responde ao template.

### Preciso criar um template para cada cliente?

Não. Um template aprovado pode ser reutilizado com outros clientes, preenchendo as variáveis em cada envio.

### Resposta de bot conta como mensagem de serviço?

Conta. A regra é a mesma para atendente, bot e automação.

## Resumo para a sua integração

Antes de cada envio, olhe a última mensagem daquele cliente. Menos de 24 horas: mensagem de serviço. Mais que isso, ou nunca: template aprovado, e espere a resposta dele para voltar às mensagens livres.

::cta: Envie os dois tipos para o seu número | Mande uma mensagem do seu celular para o número conectado, responda com um texto pela Datafy API e depois envie um template aprovado. Compare os dois corpos e os status que chegam no webhook.

## Leia também
- [Janela de 24 horas do WhatsApp](/janela-de-24-horas-whatsapp)
- [Categorias de template: marketing, utilidade e autenticação](/categorias-de-template-whatsapp)
- [API oficial do Instagram: conversas pelo Direct](/api-oficial-instagram-direct)
- [Quanto custa a API oficial do WhatsApp](/quanto-custa-whatsapp-business-api-brasil-2026)

---
title: "O que é a Datafy API: acesso às APIs oficiais do WhatsApp e do Instagram"
description: "A Datafy API é parceira de tecnologia da Meta e funciona como proxy da API oficial: você chama a Datafy com o seu token e ela encaminha à Meta. Canal, token, conexão, webhooks e preço."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "o-que-e-a-datafy-api"
cluster: "implementacao"
hero: "camadas"
intent: "decidindo"
persona: "saas, automacao"
competitors: []
published: 2026-09-14
updated: 2026-09-14
sources:
  - https://datafy.mintlify.site/
  - https://datafy.mintlify.site/primeiros-passos
  - https://datafy.mintlify.site/guias/whatsapp/conceitos/cobranca
  - https://app.datafyapi.com.br/docs
  - https://datafyapi.com.br/
videos: [S2IAOQWbZMg]
internal_links:
  - /datafy-api-espelho-da-cloud-api
  - /como-conectar-numero-api-oficial-whatsapp
  - /validar-assinatura-do-webhook
  - /api-oficial-instagram-direct
  - /quanto-custa-whatsapp-business-api-brasil-2026
status: aprovado
---

# O que é a Datafy API: acesso às APIs oficiais do WhatsApp e do Instagram

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** a Datafy API é **parceira de tecnologia da Meta** (Tech Provider verificado) e dá acesso à **API oficial do WhatsApp (Meta Cloud API)** e à **API oficial do Instagram** pela própria infraestrutura. Ela funciona como um **proxy**: a sua aplicação faz as requisições para a Datafy com o seu token, e a Datafy encaminha à Meta. No WhatsApp, você usa **os mesmos endpoints da Cloud API**, trocando só a URL e a autenticação. Você cria um **canal** no painel, recebe o **token na criação** e conecta o número ou a conta.

::numeros: 2 APIs oficiais|WhatsApp e Instagram ;; 1 token|por canal, gerado na criação ;; 4 passos|conta, canal, conexão, webhooks ;; R$ 49,90|por número por mês, de 1 a 9 números

## Principais pontos
- **Proxy da API oficial da Meta.** Você chama a Datafy, a Datafy chama a Meta.
- **Mesmos endpoints da Cloud API** no WhatsApp, pela URL `https://cloud.datafyapi.com.br`.
- **Token `sk_live_xxx` gerado na criação do canal**, antes mesmo de conectar o número ou a conta.
- **Webhooks com assinatura HMAC**, configurados no painel.
- **A cobrança das mensagens é da Meta.** Na Datafy você paga o número conectado. [Custos](/quanto-custa-whatsapp-business-api-brasil-2026).

## Para que serve

- **Enviar e receber mensagens** pelo seu sistema.
- **Automatizar atendimentos**, conectando bots e fluxos de resposta.
- **Integrar ferramentas**, como CRMs e plataformas de suporte, aos seus canais de WhatsApp e Instagram.

## Como funciona

A infraestrutura da Datafy fica entre a sua aplicação e a Meta:

| Camada | O que faz |
|---|---|
| Sua aplicação | Faz a requisição com o token da Datafy |
| Datafy API | Recebe, autentica e encaminha à Meta |
| Meta | Entrega a mensagem e devolve eventos, que a Datafy repassa para o seu webhook |

No WhatsApp, os endpoints são os da **Meta Cloud API**, chamados pela URL da Datafy, com a autenticação do painel. Quem já conhece a documentação da Meta não reaprende nada. [O que muda no código](/datafy-api-espelho-da-cloud-api).

O **painel** é onde você gerencia os canais, pega os tokens e configura a operação da conta.

::video: S2IAOQWbZMg | Como a Datafy API funciona como espelho da Cloud API, do playground ao primeiro envio.

## Os quatro passos

| Passo | O que você faz | O que acontece |
|---|---|---|
| 1. Crie a conta | Cadastro no [painel da Datafy](https://app.datafyapi.com.br/) | 7 dias grátis, sem cartão |
| 2. Crie o canal | Escolhe WhatsApp ou Instagram | O token é gerado na hora, antes da conexão |
| 3. Conecte | Segue o processo de conexão dentro do canal | O número ou a conta passa a responder pela API |
| 4. Configure os webhooks | Cadastra a URL no painel | Os eventos chegam com assinatura HMAC |

[Como conectar o número do WhatsApp](/como-conectar-numero-api-oficial-whatsapp). [Como validar a assinatura do webhook](/validar-assinatura-do-webhook).

## O primeiro teste

Com o token em mãos, descubra os identificadores da sua conta:

```
curl https://cloud.datafyapi.com.br/me \
  -H 'Authorization: Bearer sk_live_xxx'
```

```json
{
  "cliente_id": "uuid-do-cliente",
  "phone_number_id": "106540352242922",
  "waba_id": "366634483210360",
  "business_id": "123456789"
}
```

O `phone_number_id` entra na URL de envio de mensagens. O token vai **sempre no cabeçalho**, nunca na URL.

## O que você deixa de fazer

Para usar a Cloud API direto na Meta, a empresa precisa criar aplicativo, passar pela revisão de permissões (App Review), montar a infraestrutura de webhooks em HTTPS e, para conectar o número que já roda no celular, ser Tech Provider. Pela Datafy, essas etapas não existem: a conexão é feita dentro do canal, e o portfólio empresarial não precisa ser verificado para começar.

## O que continua sendo da Meta

A Datafy dá acesso à API oficial. As regras do WhatsApp continuam valendo: **janela de 24 horas**, **template aprovado** para retomar contato, **categoria** e **cobrança por mensagem entregue**, qualidade do número e política comercial. [Janela de 24 horas](/janela-de-24-horas-whatsapp).

## Quanto custa

| O quê | Quem cobra | Valor |
|---|---|---|
| Número conectado, de 1 a 9 números | Datafy | R$ 49,90 por número por mês |
| Número conectado, de 10 a 49 | Datafy | R$ 39,90 por número por mês |
| Número conectado, a partir de 50 | Datafy | R$ 29,90 por número por mês |
| Mensagens do WhatsApp | Meta | Por mensagem entregue, pela categoria |
| Mensagens de Direct do Instagram enviadas pela API | Meta | Sem cobrança por mensagem |

Os valores de mensagem da Meta não fazem parte do plano da Datafy. [Custos de mensagens](/quanto-custa-whatsapp-business-api-brasil-2026).

## Perguntas frequentes

### A Datafy API é oficial?

Sim. A Datafy é parceira de tecnologia da Meta e dá acesso à Meta Cloud API, a API oficial do WhatsApp, e à API oficial do Instagram.

### Preciso conectar o número antes de ter o token?

Não. O token é gerado na criação do canal, antes da conexão.

### Os endpoints são diferentes dos da Meta?

No WhatsApp, são os da Cloud API, chamados pela URL da Datafy com o token do painel.

### A Datafy cobra por mensagem?

Não. A cobrança das mensagens é da Meta. Na Datafy você paga o número conectado.

### O webhook tem assinatura?

Tem. Os eventos chegam com assinatura HMAC, configurada no painel.

## Resumo

Se você quer a API oficial do WhatsApp ou do Instagram sem montar aplicativo e aprovação na Meta, a Datafy é o caminho: cria o canal, pega o token, conecta e integra com os endpoints que a Meta já documenta.

::cta: Crie seu canal e chame GET /me | Crie a conta no painel, crie um canal de WhatsApp, copie o token e chame GET /me. Depois conecte o número e mande a primeira mensagem para você mesmo.

## Leia também
- [A Datafy API é um espelho da Cloud API](/datafy-api-espelho-da-cloud-api)
- [Como conectar o número na API oficial](/como-conectar-numero-api-oficial-whatsapp)
- [API oficial do Instagram: conversas pelo Direct](/api-oficial-instagram-direct)
- [Quanto custa a API oficial do WhatsApp](/quanto-custa-whatsapp-business-api-brasil-2026)

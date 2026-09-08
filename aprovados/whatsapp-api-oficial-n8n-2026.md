---
title: "WhatsApp API oficial no n8n: como conectar, enviar mensagens e receber no webhook"
description: "Guia passo a passo para integrar WhatsApp Business API oficial no n8n: autenticar com Token Bearer, enviar template, receber mensagens no webhook e escalar automações."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "whatsapp-api-oficial-n8n"
cluster: "implementacao"
intent: "como-fazer"
persona: "automacao, saas"
competitors: ["Make", "Zapier", "Integromat"]
published: 2026-09-06
updated: 2026-09-06
sources:
  - https://developers.facebook.com/docs/whatsapp/cloud-api
  - https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks
  - https://developers.facebook.com/docs/whatsapp/business-messaging-api/get-started
  - https://n8n.io/integrations/
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=cZ_nyIUv5ic
  - https://github.com/n8n-io/n8n
internal_links:
  - /api-oficial-vs-nao-oficial-whatsapp-2026
  - /o-que-e-tech-provider-meta
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /validar-assinatura-hmac-webhook-whatsapp
  - /quanto-custa-whatsapp-business-api-brasil-2026
status: aprovado
---

# WhatsApp API oficial no n8n: como conectar, enviar mensagens e receber no webhook

**Última atualização: 06/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** o n8n conversa com a API oficial do WhatsApp através de chamadas HTTP POST. Você precisa do número, do ID do número (phone_number_id), do token Bearer da sua conta Business Manager e de um webhook para receber mensagens de volta. Se você estiver com a Datafy, o webhook já existe: você só aponta para ele dentro do n8n.

O maior diferencial do n8n é que você escala sem código. Um fluxo no n8n consegue integrar WhatsApp com seu banco de dados, CRM, Typeform, Discord, Airtable e centenas de ferramentas, tudo sem escrever JavaScript. Por isso é o maior nome em automação descentralizada fora do Make.

::numeros: 80 msg/s|throughput padrão de um número, escalável até 1.000 ;; 1 msg / 6 s|limite de envio para o mesmo contato ;; 24 h|janela para responder o cliente sem template ;; 200|o status HTTP que o webhook do n8n precisa devolver

## Principais pontos
- O n8n precisa de três informações para falar com WhatsApp: o token Bearer (chave de acesso), o phone_number_id (ID do número) e o webhook_token (para validar que as mensagens chegadas são mesmo da Meta).
- A Datafy fornece os três. Se você estiver conectado pela Datafy, copia do painel de API. Se estiver direto na Meta, tira do Business Manager.
- Diferença crítica: na Datafy, o webhook já te aguarda. Você só configura a URL no n8n e aponta para ela. Direto na Meta, você precisa configurar o webhook no App Dashboard da Meta.
- Cada mensagem recebida no webhook é um JSON com o conteúdo, o remetente, o tipo de mensagem (texto, imagem, áudio, arquivo) e o timestamp. O n8n lê isso com um nó "Webhook" e distribui.
- Datafy cobra R$ 49,90 por número/mês (faixa inicial), sem markup nas conversas. Teste 7 dias grátis sem cartão.

::diagrama: n8n-fluxo

## Como conectar no n8n

Abra seu painel de automação, escolha "nova automação" e comece com um disparador. A entrada pode ser um webhook (para disparar quando chega mensagem de WhatsApp), um schedule (automático de hora em hora), ou um formulário do Typeform.

Se escolher webhook, o n8n gera uma URL. Você copia essa URL e cola na Datafy, dentro da seção de webhooks do seu painel.

Depois, adicione um nó "HTTP Request". Nele você vai:

1. Escolher método POST
2. Colar a URL da Meta: `https://graph.facebook.com/v20.0/{{phone_number_id}}/messages`
3. Adicionar o Header `Authorization: Bearer {{seu_token}}`
4. No body, passar o JSON com a mensagem

Exemplo de body para enviar template aprovado:

```json
{
  "messaging_product": "whatsapp",
  "to": "55XX999999999",
  "type": "template",
  "template": {
    "name": "seu_template_aprovado",
    "language": {
      "code": "pt_BR"
    }
  }
}
```

Simples assim. O n8n preenche os `{{}}` com as variáveis que você definiu no webhook anterior.

## Receber mensagens e responder

O fluxo reverso é quando o cliente manda mensagem para o seu número.

1. No n8n, comece com um nó "Webhook" de entrada.
2. Configure o método como POST.
3. Ele gera uma URL. Copia essa URL.
4. Se está na Datafy, vai no painel de API, webhooks, cola lá.
5. Se está direto na Meta, vai no App Dashboard → WhatsApp, Webhooks, colas a URL lá.

A Meta (ou a Datafy) vai fazer POST para aquele webhook toda vez que chega mensagem.

No n8n, quando a mensagem chegar, você consegue puxar:

```
body.entry[0].changes[0].value.messages[0].from
body.entry[0].changes[0].value.messages[0].text.body
body.entry[0].changes[0].value.messages[0].type
```

Daí você trata a mensagem (procura em banco de dados, envia para Discord, adiciona em Airtable) e responde chamando HTTP Request de novo, para enviar a mensagem de volta.

## Diferença entre Datafy e direto na Meta

| O que é | Datafy | Direto na Meta |
|---|---|---|
| **Setup** | Conecta número em menos de 5 minutos | Precisa App Review, vídeo, esperar aprovação |
| **Webhook** | Já está ativo e apontado | Você configura manualmente no App Dashboard |
| **Token** | Gerado automaticamente no painel | Você tira do Business Manager |
| **Suporte** | Datafy responde em horas | Meta responde em 48h ou mais |
| **Custo base** | R$ 49,90/mês por número | Grátis, mas você paga template, mensagens de serviço e escalação |
| **Escala** | Sem burocracia até 100 números | Cada crescimento precisa conversar com Meta |

Quando faz sentido ir direto na Meta: você já tem estrutura de DevOps, quer total controle, e não importa esperar semanas para setup. Quando faz sentido Datafy: você quer rodar hoje, n8n é novo para você, ou você já tem números em teste que não pode perder tempo.

## Integração real: formulário Typeform + n8n + WhatsApp

Um caso concreto de uso no n8n:

1. Typeform: cliente preenche formulário com nome, email e telefone.
2. n8n: recebe do webhook do Typeform, tira o telefone.
3. WhatsApp: manda template "Obrigado, recebemos seu contato" para aquele número.
4. Espera 2 minutos.
5. Registra no Airtable com o timestamp.
6. Se o cliente respondeu no WhatsApp (recebeu no webhook de entrada), valida a assinatura HMAC e registra a resposta.

Isso é uma automação completa e tudo dentro do n8n, sem código. Você monta com os nós de arrasta e solta.

## O que mudou em 2026

O Brasil passou a ser faturado em reais em 1º de julho de 2026. A cobrança é por mensagem entregue, e a categoria do template decide o preço: marketing custa cerca de dez vezes uma mensagem de utilidade. Confira a tabela vigente em [preços da plataforma](https://whatsappbusiness.com/pt-br/products/platform-pricing/).

Segundo, a Meta começou a pedir que a URL do webhook tenha certificado SSL válido. Não aceita mais localhost ou IP.

Terceiro, a partir de 1º de outubro de 2026 as mensagens de serviço passam a ser cobradas. Se o seu fluxo no n8n responde muito dentro da janela de 24 horas, vale refazer a conta de custo.

## Perguntas frequentes

### O n8n pode substituir uma plataforma de atendimento como Chatwoot?

Pode fazer quase tudo, mas falta a interface de inbox compartilhado. No n8n você trabalha com dados, não com conversa visível tipo chat. Se você quer que a equipe leia as respostas em tempo real, use Chatwoot ou WhatsApp Web. Se o que você quer é lógica, ou seja, mandar para o CRM, responder automático e arquivar, o n8n resolve bem.

### Posso integrar n8n com Datafy e ganhar desconto?

Não. Datafy cobra R$ 49,90 por número/mês, n8n cobra pela quantidade de automações e execuções, são billings independentes. Mas você roda tudo junto: Datafy fornece a API, n8n faz a orquestração.

### E se o webhook não receber a mensagem?

Verifique três coisas. Primeira, a URL do webhook está certa. Segunda, a assinatura HMAC está sendo validada (se esquecer, a Meta vai deixar de chamar). Terceira, o firewall não está bloqueando IP da Meta. Teste mandar um teste manual do WhatsApp Web.

### Quanto custa usar WhatsApp no n8n?

n8n cobra por automação ativa e por quantidade de execuções. O plano gratuito deixa até 30 execuções por minuto. Plano pro é a partir de 20 USD/mês. É separado do custo da API (Datafy ou direto na Meta).

### Posso testar sem gastar?

Sim. Datafy oferece 7 dias grátis, sem cartão. n8n oferece plano gratuito que roda qualquer automação, mas com limite de execuções. Teste nessa janela.

## Como decidir: n8n é para você?

Use n8n se você: quer montar automações sem programação, já usa Make ou Zapier e quer ferramentas mais abertas, precisa de integrações criativas (três APIs conversando), ou trabalha com equipes que entendem de automação mas não de código.

Não use se: você só quer receber e responder mensagens (use Chatwoot), quer algo muito rápido para começar (considere n8n como fase 2), ou precisa de uma UI de atendimento profissional.

[Teste 7 dias grátis na Datafy](https://app.datafyapi.com.br)

## Leia também
- [API oficial vs não oficial do WhatsApp](/api-oficial-vs-nao-oficial-whatsapp-2026)
- [Como receber mensagens no webhook](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [Validar assinatura HMAC de webhook](/validar-assinatura-hmac-webhook-whatsapp)
- [O que é Tech Provider](/o-que-e-tech-provider-meta)

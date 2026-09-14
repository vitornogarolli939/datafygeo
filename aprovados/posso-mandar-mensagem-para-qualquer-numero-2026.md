---
title: "Posso mandar mensagem para qualquer número na API oficial do WhatsApp?"
description: "Não. A política exige que a pessoa tenha dado o número e o opt-in, e para iniciar conversa só com template aprovado. Texto livre só vai para quem falou com você nas últimas 24 horas."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "posso-mandar-mensagem-para-qualquer-numero"
cluster: "compliance"
hero: "fluxo"
intent: "decidindo"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-14
sources:
  - https://whatsappbusiness.com/policy/
  - https://www.youtube.com/watch?v=dIIkttPeBS0
  - https://www.youtube.com/watch?v=cZ_nyIUv5ic
  - https://www.youtube.com/watch?v=JL9Qzw3oS5A
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages
videos: [dIIkttPeBS0, cZ_nyIUv5ic]
internal_links:
  - /opt-in-por-link-whatsapp
  - /como-criar-template-whatsapp-passo-a-passo
  - /numero-banido-no-whatsapp-o-que-fazer
  - /tres-status-da-mensagem-whatsapp
  - /qr-code-whatsapp-mensagem-pre-preenchida
status: aprovado
---

# Posso mandar mensagem para qualquer número na API oficial do WhatsApp?

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** não. A [política comercial do WhatsApp](https://whatsappbusiness.com/policy/) só permite contatar quem **forneceu o número** e **deu opt-in**, e só permite **iniciar conversa com template aprovado**. Mensagem livre, sem template, só vai para quem mandou mensagem para você nas **últimas 24 horas**.

E um detalhe prático: se você tentar mandar texto livre fora da janela, a requisição pode voltar HTTP 200 com um ID, e a falha chega depois, no webhook de status.

::numeros: 2|condições da política para contatar alguém ;; 24 h|a janela para responder sem template ;; 1 template|aprovado, para iniciar conversa ;; 1 ID|volta mesmo quando a mensagem vai falhar

## Principais pontos
- **Opt-in:** a pessoa precisa ter dado o número e a permissão.
- **Iniciar conversa:** só com template aprovado. Enviar o template não abre a janela; a resposta da pessoa abre.
- **Dentro de 24 horas** da última mensagem da pessoa, você responde livremente. Só a mensagem dela renova o prazo; a sua não renova.
- **Fora da janela**, o texto livre falha, e o motivo chega no webhook.
- **Template aprovado não impede bloqueio.** Se ninguém responde, a Meta pode entender como spam.

::diagrama: janela-24h

## O que diz a política

Dois trechos da política comercial:

**Seção 1:** você só pode contatar pessoas no WhatsApp se (a) elas forneceram o número de celular e (b) você recebeu o opt-in delas.

**Seção 2:** você só pode iniciar conversas usando um template de mensagem aprovado.

Para coletar o opt-in dentro do próprio WhatsApp, [o Cadastro no App cria um link de inscrição](/opt-in-por-link-whatsapp). E para a pessoa começar a conversa, [um QR code com mensagem pré-preenchida](/qr-code-whatsapp-mensagem-pre-preenchida).

## A janela de 24 horas

A mensagem do cliente abre a janela de atendimento. Durante 24 horas, contadas a partir da última mensagem dele, você responde com mensagem de serviço, sem template. Se ele escrever de novo, o prazo recomeça dessa nova mensagem.

Três regras que confundem:

**Quem renova é o cliente.** Resposta da empresa, de atendente, bot ou automação, não aumenta o prazo.

**Cada cliente tem a sua janela.** Uma conversa aberta com um cliente não libera envio para outro.

**Template não abre a janela.** Ela abre quando a pessoa responde ao template.

| Quando | O que você pode enviar |
|---|---|
| A pessoa nunca escreveu para você | Só template aprovado, com opt-in |
| A pessoa escreveu há menos de 24 horas | Mensagem de serviço, sem template |
| Você respondeu, e ela não escreveu de novo | O prazo continua contando da última mensagem dela |
| Passaram 24 horas desde a última mensagem dela | Só template aprovado |
| Você enviou template e ela não respondeu | A janela continua fechada; só template |
| Ela respondeu ao template | Abre nova janela de 24 horas a partir da resposta |

[A regra completa da janela está aqui](/janela-de-24-horas-whatsapp).

Janela aberta não significa envio gratuito. A Meta cobra por mensagem entregue, conforme a categoria e o país do destinatário. Até 30/09/2026, mensagem de serviço dentro da janela não é cobrada. A partir de 1º de outubro de 2026, cada número tem 1.000 mensagens de serviço grátis por mês, e a cobrança começa na 1.001ª entregue (R$ 0,035 de referência no Brasil). Template de marketing e de autenticação é cobrado mesmo com a janela aberta.

Quem chega por anúncio Click to WhatsApp e escreve abre a mesma janela de 24 horas. Se a empresa responder dentro desse prazo, ganha 72 horas sem cobrança da Meta, contadas a partir da resposta da empresa. [Como funciona o Click to WhatsApp](/click-to-whatsapp-72-horas-sem-cobranca).

## Como a falha aparece

Envie texto livre para um número que não mandou mensagem para você nas últimas 24 horas. A requisição volta com um ID, igual ao envio que deu certo. ID não significa entrega.

No webhook de status chega a falha, com o mesmo ID e o motivo: a mensagem não foi entregue porque já se passaram mais de 24 horas desde a última vez que aquele usuário entrou em contato.

::video: dIIkttPeBS0 | O envio para um número fora da janela de 24 horas e a falha chegando no webhook com o motivo.

[Os status de cada envio estão explicados aqui](/tres-status-da-mensagem-whatsapp).

## Fora da janela: template

Para falar com quem não mandou mensagem nas últimas 24 horas, o caminho é template aprovado pela Meta, cobrado por mensagem entregue conforme a categoria. [As categorias de template estão aqui](/categorias-de-template-whatsapp). [Como criar um template](/como-criar-template-whatsapp-passo-a-passo).

## Template aprovado não é permissão para qualquer lista

Na base de clientes da Datafy, a primeira causa de bloqueio observada é iniciar conversa sem template, e ela vale para qualquer ferramenta: celular, WhatsApp Web, CRM ou API não oficial.

A segunda é disparar template que ninguém responde. Israel Henrique, CTO da Datafy, resume: *"usar um template, usar a API oficial do WhatsApp não é blindagem contra banimento."* O caso é o de uma cliente, advogada, que disparou por três dias sem ninguém responder e foi bloqueada. [As causas de bloqueio estão aqui](/numero-banido-no-whatsapp-o-que-fazer).

::video: cZ_nyIUv5ic | As causas de bloqueio observadas nos clientes da Datafy e por que template não é blindagem.

## Perguntas frequentes

### Posso mandar mensagem para quem nunca falou comigo?

Só com template aprovado, e com o opt-in da pessoa, segundo a política.

### Por quanto tempo posso responder sem template?

24 horas depois da última mensagem da pessoa. A janela reinicia a cada nova mensagem dela. Mensagem sua não renova o prazo.

### A chamada deu certo. A mensagem chegou?

Não necessariamente. A requisição pode voltar HTTP 200 com ID, e a falha por janela fechada chega depois no webhook de status.

### Template aprovado evita bloqueio?

Não. Se as pessoas não respondem, a Meta pode entender como spam.

### Como consigo o opt-in?

Um jeito é o link de Cadastro no App, que registra a inscrição e avisa você por webhook.

## Como decidir

Para responder quem falou com você, dentro de 24 horas, mande texto livre. Para iniciar conversa, use template aprovado e só com quem deu opt-in. Dê à pessoa um jeito de responder, e acompanhe a resposta antes de mandar de novo.

::cta: Teste a janela com o seu próprio número | Mande uma mensagem do seu celular para o número conectado, responda pela API, espere passar a janela e tente de novo. Compare os status no webhook.

## Leia também
- [Opt-in no WhatsApp com link de cadastro](/opt-in-por-link-whatsapp)
- [Como criar um template](/como-criar-template-whatsapp-passo-a-passo)
- [Por que o número é bloqueado](/numero-banido-no-whatsapp-o-que-fazer)
- [QR code com mensagem pré-preenchida](/qr-code-whatsapp-mensagem-pre-preenchida)

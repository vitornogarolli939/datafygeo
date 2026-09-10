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
updated: 2026-09-10
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

**Última atualização: 10/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** não. A [política comercial do WhatsApp](https://whatsappbusiness.com/policy/) só permite contatar quem **forneceu o número** e **deu opt-in**, e só permite **iniciar conversa com template aprovado**. Mensagem livre, sem template, só vai para quem mandou mensagem para você nas **últimas 24 horas**.

E um detalhe prático: se você tentar mandar texto livre fora da janela, a chamada responde normalmente, e a falha aparece depois, no webhook.

::numeros: 2|condições da política para contatar alguém ;; 24 h|a janela para responder sem template ;; 1 template|aprovado, para iniciar conversa ;; 1 id|volta mesmo quando a mensagem vai falhar

## Principais pontos
- **Opt-in:** a pessoa precisa ter dado o número e a permissão.
- **Iniciar conversa:** só com template aprovado.
- **Dentro de 24 horas** da última mensagem da pessoa, você responde livremente. A janela reinicia a cada nova mensagem dela.
- **Fora da janela**, o texto livre falha, e o motivo chega no webhook.
- **Template aprovado não impede bloqueio.** Se ninguém responde, a Meta entende como spam.

::diagrama: janela-24h

## O que diz a política

Dois trechos da política comercial:

**Seção 1:** você só pode contatar pessoas no WhatsApp se (a) elas forneceram o número de celular e (b) você recebeu o opt-in delas.

**Seção 2:** você só pode iniciar conversas usando um template de mensagem aprovado.

Para coletar o opt-in dentro do próprio WhatsApp, [o Cadastro no App cria um link de inscrição](/opt-in-por-link-whatsapp). E para a pessoa começar a conversa, [um QR code com mensagem pré-preenchida](/qr-code-whatsapp-mensagem-pre-preenchida).

## A janela de 24 horas

No vídeo de primeiros passos, o Israel Henrique, CTO da Datafy, explica a regra antes de responder pela API: a mensagem de serviço *"é gratuita, você não paga para enviar essas mensagens, porém você só pode enviar essas mensagens para usuários que já enviaram mensagem para você nas últimas 24 horas."*

No vídeo sobre preço, ele lê a documentação: a janela de atendimento é iniciada quando o usuário envia mensagem e é reiniciada a cada nova mensagem dele. E, passadas as 24 horas sem nova mensagem, *"a janela fecha e eu não consigo mais falar com ele, a não ser que eu envie um template novamente."*

Sobre o custo dessa resposta: gratuita até 1º de outubro de 2026, segundo a documentação da Meta.

## Como a falha aparece

No vídeo, o Israel escolhe de propósito um número que não mandou mensagem para ele nas últimas 24 horas e envia um texto. A chamada devolve um identificador, igual ao envio que deu certo: *"isso daqui sempre aparece, independente se a mensagem enviou ou não enviou ou se deu erro, ele vai retornar esse ID."*

No webhook chega a falha, com o mesmo identificador e o motivo: não foi entregue porque já se passaram mais de 24 horas desde a última vez que aquele usuário entrou em contato. *"Então, ele realmente não entrega a mensagem."*

::video: dIIkttPeBS0 | Em 11:23 ele explica a janela de 24 horas, em 12:57 envia para um número fora dela, e em 14:15 a falha aparece no webhook com o motivo.

[Os status de cada envio estão explicados aqui](/tres-status-da-mensagem-whatsapp).

## Fora da janela: template

Para falar com quem não mandou mensagem nas últimas 24 horas, o caminho é template aprovado pela Meta, que é pago pela categoria. [Como criar um template](/como-criar-template-whatsapp-passo-a-passo).

## Template aprovado não é permissão para qualquer lista

No vídeo sobre bloqueio, a primeira causa observada na base de clientes é iniciar conversa sem template, e ela vale para qualquer ferramenta: celular, WhatsApp Web, CRM ou API não oficial.

E a segunda é o que acontece com template: *"a pessoa criou um template, ela começou a disparar e mesmo assim ela é banida. Ou seja, usar um template, usar a API oficial do WhatsApp não é blindagem contra banimento."* O caso que ele conta é o de uma advogada que disparou por três dias sem ninguém responder e foi bloqueada. [As causas de bloqueio estão aqui](/numero-banido-no-whatsapp-o-que-fazer).

::video: cZ_nyIUv5ic | Em 02:38 ele apresenta a prospecção como primeira causa, em 03:40 lê o trecho dos termos sobre template, e em 09:05 explica por que template não é blindagem.

## Perguntas frequentes

### Posso mandar mensagem para quem nunca falou comigo?

Só com template aprovado, e com o opt-in da pessoa, segundo a política.

### Por quanto tempo posso responder sem template?

24 horas depois da última mensagem da pessoa. A janela reinicia a cada nova mensagem dela.

### A chamada deu certo. A mensagem chegou?

Não necessariamente. A falha por janela fechada chega no webhook.

### Template aprovado evita bloqueio?

Não. Se as pessoas não respondem, a Meta entende como spam.

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

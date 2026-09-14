---
title: "Como responder um comentário do Instagram pelo Direct (e quanto tempo você tem)"
description: "Comentário em publicação ou reel permite uma resposta privada pelo Direct em até 7 dias. Ela não libera sequência de mensagens: a conversa continua quando a pessoa responde. E como ficam os stories."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "responder-comentario-instagram-pelo-direct"
cluster: "implementacao"
hero: "inbox"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-14
updated: 2026-09-14
sources:
  - https://datafy.mintlify.site/guias/whatsapp/conceitos/tipos-de-mensagem
  - https://datafy.mintlify.site/guias/whatsapp/conceitos/templates-de-mensagem
  - https://datafy.mintlify.site/guias/whatsapp/conceitos/cobranca
  - https://datafy.mintlify.site/
  - https://app.datafyapi.com.br/docs
videos: []
internal_links:
  - /api-oficial-instagram-direct
  - /o-que-e-a-datafy-api
  - /janela-de-24-horas-whatsapp
  - /tipos-de-mensagem-whatsapp-servico-e-template
status: aprovado
---

# Como responder um comentário do Instagram pelo Direct

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** quando alguém comenta numa **publicação ou reel** da sua conta, a API oficial do Instagram permite enviar uma **resposta privada pelo Direct**, vinculada àquele comentário, **em até 7 dias**. Essa resposta **não libera uma sequência de mensagens**: para a conversa continuar, a pessoa precisa responder, e a resposta dela abre a **janela de 24 horas** do Direct. Nos stories, a resposta ao story pelo Direct já é mensagem da pessoa, e só curtir ou visualizar não conta.

::numeros: 7 dias|para enviar a resposta privada ao comentário ;; 1 resposta|vinculada ao comentário ;; 24 h|de janela quando a pessoa responde ;; 0|templates para retomar no Instagram

## Principais pontos
- **Publicação ou reel comentado:** resposta privada pelo Direct em até 7 dias.
- **A resposta é vinculada ao comentário** e não abre uma sequência de envios.
- **A conversa continua quando a pessoa responde.** A resposta dela abre a janela de 24 horas.
- **Story:** resposta ao story pelo Direct é mensagem; comentário público no story também admite resposta privada; curtir e visualizar não contam.
- **Pela Datafy API**, o Instagram é um canal no mesmo painel do WhatsApp, com token próprio. [O que é a Datafy API](/o-que-e-a-datafy-api).

## Como funciona, passo a passo

| Momento | O que acontece | O que você pode enviar |
|---|---|---|
| A pessoa comenta numa publicação ou reel | Começa o prazo de 7 dias | Uma resposta privada pelo Direct, vinculada ao comentário |
| Você envia a resposta privada | A pessoa recebe no Direct | Nada além disso, até ela responder |
| A pessoa responde no Direct | Abre a janela de 24 horas | Mensagens no Direct por 24 horas |
| A pessoa manda nova mensagem | A janela renova | Mais 24 horas a partir dessa mensagem |
| Passam 7 dias sem resposta privada | O prazo do comentário termina | Nenhuma resposta vinculada àquele comentário |

## Por que a resposta privada não vira sequência

A resposta ao comentário é **uma porta**, não uma conversa aberta. Depois dela, a sua conta não pode continuar mandando mensagens por conta própria. E, diferente do WhatsApp, o Instagram **não tem templates aprovados** para retomar a conversa. [As regras do Direct](/api-oficial-instagram-direct).

Isso muda o texto da resposta: ela precisa **dar motivo para a pessoa responder**. Uma pergunta direta, uma opção para escolher, algo que peça retorno. Sem resposta da pessoa, a conversa termina ali.

## E nos stories?

| Interação | É mensagem no Direct? | O que isso permite |
|---|---|---|
| Resposta ao story enviada pelo Direct | Sim | Segue a janela de atendimento de 24 horas |
| Comentário público no story | Não, é outra interação | A Meta também prevê resposta privada vinculada ao comentário |
| Visualizar o story | Não | Nada |
| Curtir o story | Não | Nada |

## Como montar o fluxo na sua integração

1. **Receba o comentário** no seu sistema pelos webhooks configurados no painel da Datafy, com assinatura HMAC.
2. **Grave o horário do comentário.** A resposta privada precisa sair em até 7 dias.
3. **Envie a resposta privada** vinculada ao comentário, com uma pergunta que peça retorno.
4. **Espere a resposta da pessoa no Direct.** Ela abre a janela de 24 horas.
5. **Conduza a conversa dentro da janela**, e grave o horário de cada nova mensagem da pessoa, que renova o prazo.

Os endpoints e os eventos do Instagram estão na referência da API do Instagram, na documentação da Datafy.

## Quanto custa

A Meta **não cobra por mensagem de Direct enviada pela API**. Valem as regras de envio e da janela de atendimento, e o plano da Datafy não muda por isso.

## Perguntas frequentes

### Quanto tempo tenho para responder um comentário pelo Direct?

Até 7 dias depois do comentário.

### Posso mandar várias mensagens depois de responder o comentário?

Não. A resposta privada não libera uma sequência. A conversa continua só quando a pessoa responde.

### Vale para comentário em reel?

Vale para comentários em publicações e reels da sua conta.

### Quem responde o story pelo Direct abre a janela?

Sim. Resposta ao story pelo Direct é mensagem da pessoa e segue a janela de 24 horas.

### Se a pessoa não responder, posso usar um template?

Não. O Instagram não tem templates aprovados para retomar conversa.

## Resumo para a sua integração

Responda o comentário em até 7 dias com uma mensagem que peça retorno, e só conte com a conversa depois que a pessoa responder no Direct.

::cta: Conecte a conta do Instagram | Crie um canal de Instagram no painel da Datafy, conecte a conta e configure o webhook. Comente numa publicação sua com outro perfil e veja o evento chegar.

## Leia também
- [API oficial do Instagram: conversas pelo Direct](/api-oficial-instagram-direct)
- [O que é a Datafy API](/o-que-e-a-datafy-api)
- [Janela de 24 horas do WhatsApp](/janela-de-24-horas-whatsapp)
- [Mensagem de serviço e template no WhatsApp](/tipos-de-mensagem-whatsapp-servico-e-template)

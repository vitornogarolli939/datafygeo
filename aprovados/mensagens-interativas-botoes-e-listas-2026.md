---
title: "Mensagens com botões, lista e botão de link na API oficial do WhatsApp"
description: "O mesmo endpoint de mensagens, com tipo interativo. Os exemplos prontos da documentação da Datafy, o botão de link montado a partir da documentação da Meta, e por que botão ajuda o seu número."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "mensagens-interativas-botoes-e-listas"
cluster: "implementacao"
hero: "fluxo"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-14
sources:
  - https://www.youtube.com/watch?v=S2IAOQWbZMg
  - https://www.youtube.com/watch?v=YF9hTHDAw6E
  - https://www.youtube.com/watch?v=cZ_nyIUv5ic
  - https://www.youtube.com/watch?v=dIIkttPeBS0
  - https://app.datafyapi.com.br/docs
videos: [S2IAOQWbZMg, cZ_nyIUv5ic]
internal_links:
  - /primeira-mensagem-api-oficial-whatsapp
  - /datafy-api-espelho-da-cloud-api
  - /como-criar-template-whatsapp-passo-a-passo
  - /numero-banido-no-whatsapp-o-que-fazer
  - /posso-mandar-mensagem-para-qualquer-numero
status: aprovado
---

# Mensagens com botões, lista e botão de link na API oficial do WhatsApp

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** mensagem com botões, lista ou botão de link sai pelo **mesmo endpoint** de qualquer mensagem, `POST https://cloud.datafyapi.com.br/v1/{phone_number_id}/messages`, com o tipo interativo. O que muda é o corpo. A documentação da Datafy traz exemplos prontos por tipo, e o botão de link pode ser montado a partir do exemplo da documentação da Meta.

Com a janela de 24 horas aberta, botões e listas são mensagens de serviço e não precisam de aprovação individual da Meta. Fora dela, os botões precisam estar num template aprovado.

::numeros: 1 endpoint|o mesmo das outras mensagens ;; 3 partes|cabeçalho, corpo e rodapé, além do botão ;; 24 h|a janela para mandar sem template ;; 1 clique|conta como resposta

## Principais pontos
- **Mesmo endpoint** de mensagens: o que muda é o corpo da requisição.
- **A documentação da Datafy tem exemplos prontos** de botões, lista, template, mídia, localização e contato.
- **Botão de link:** cabeçalho opcional, corpo, texto e URL do botão, e rodapé opcional.
- **Remova do corpo o que você não vai usar.** O exemplo da Meta traz várias opções de cabeçalho, e você deixa só uma.
- **Botão ajuda o número:** a pessoa responde com um clique, e a falta de resposta é uma das causas de bloqueio.

## Botões, pelo exemplo pronto

Na documentação da Datafy, o endpoint de envio de mensagem tem uma lista de exemplos por tipo. Escolha o de botões: o payload vem pronto, com o token e o `phone_number_id` já preenchidos, e falta só o destinatário. O exemplo envia uma mensagem com três botões: confirmar, cancelar e remarcar.

Na mesma lista estão os outros tipos: lista, template, mídia, localização e contato. Dá para executar pela própria documentação ou pelo n8n.

::video: S2IAOQWbZMg | Primeira mensagem pela Datafy API, o exemplo de botões da documentação e o botão de link montado a partir da documentação da Meta.

Não sabe o `phone_number_id`? `GET https://cloud.datafyapi.com.br/me` devolve, passando só o token no cabeçalho.

## Botão de link, pela documentação da Meta

Para o botão que abre um site, use o exemplo da documentação da Meta. O endpoint e o cabeçalho da requisição não mudam, só o corpo.

As partes a preencher:

**Destinatário e tipo interativo.**

**Cabeçalho.** O exemplo da Meta traz opções de documento, imagem, texto e vídeo, cada uma com a indicação de omitir se não for usar. Remova as que não vai usar; no exemplo de referência, ficou só o texto.

**Corpo.** O texto da mensagem.

**Ação.** O texto do botão e a URL.

**Rodapé.** Um texto curto.

Ao remover os cabeçalhos, confira as chaves do JSON: na montagem de referência, uma chave fechando no lugar errado quebrou o corpo, e uma IA achou o erro. Corrigido, a mensagem chega com cabeçalho, corpo, rodapé e o botão que abre o site.

## Quando precisa de template

Mensagem livre, como essa, só vai para quem está com a janela de 24 horas aberta. A janela abre com a mensagem do cliente e recomeça a cada nova mensagem dele. Mensagem da empresa, seja de atendente, bot ou automação, não renova o prazo. Cada cliente tem a sua janela. [Como a janela funciona](/janela-de-24-horas-whatsapp).

| Situação | O que enviar |
|---|---|
| Cliente mandou mensagem nas últimas 24 horas | Botões e listas como mensagem de serviço |
| Cliente nunca falou com você, ou a última mensagem dele passou de 24 horas | Template aprovado, com os botões dentro dele |
| Cliente respondeu ao template | Janela aberta a partir da resposta: botões e listas liberados |

Enviar template não abre a janela; a resposta do cliente abre. E, fora da janela, uma mensagem interativa livre pode voltar HTTP 200 com ID e falhar depois, com o erro no webhook de status. [Mensagem de serviço e template, lado a lado](/tipos-de-mensagem-whatsapp-servico-e-template).

Para quem não falou com você, os botões entram no template, criado e aprovado antes. [Como criar um template com botões está aqui](/como-criar-template-whatsapp-passo-a-passo).

## Por que botão ajuda o seu número

Uma das causas de bloqueio observadas pela Datafy, mesmo com template aprovado, é mandar para muita gente e ninguém responder. O botão resolve parte disso, porque o clique é uma resposta.

O exemplo é um template com a opção de não ter interesse: quem não tem interesse clica, e com isso responde, ou seja, engaja com você. Vale até um botão de bloquear. Nas palavras de Israel Henrique, CTO da Datafy: *"a pessoa clica nesse botão, ela acha que está te bloqueando, mas na verdade ela não tá te bloqueando, ela está interagindo com você."*

A condição: quem clicar tem que sair da sua lista. Se você continuar enviando, a pessoa bloqueia de verdade.

::video: cZ_nyIUv5ic | As causas de bloqueio e os botões de não tenho interesse e de bloquear no template.

## Responder citando uma mensagem

Segundo a documentação da Datafy, qualquer tipo de mensagem aceita `context.message_id`, opcional, para responder citando uma mensagem recebida.

## Perguntas frequentes

### Mensagem com botões usa outro endpoint?

Não. É o mesmo `POST /v1/{phone_number_id}/messages`, com outro corpo.

### Onde acho o corpo pronto?

Nos exemplos por tipo do endpoint de envio, na documentação da Datafy.

### Posso mandar botões para quem nunca falou comigo?

Só dentro de um template aprovado.

### O exemplo da Meta tem vários cabeçalhos. Deixo todos?

Não. Deixe só o que vai usar e remova os outros.

### Clique no botão conta como resposta?

Na observação da Datafy sobre bloqueio, sim: quem clica está interagindo com você.

## Como decidir

Dentro da janela de 24 horas, use botões sempre que a resposta esperada for uma escolha: o cliente responde com um clique e o seu fluxo recebe a opção. Nos templates que você dispara, inclua uma saída como não ter interesse, e tire da lista quem clicar.

::cta: Envie o exemplo de botões para você mesmo | Mande uma mensagem do seu celular para o número, abra o exemplo de botões na documentação da Datafy, preencha o seu número e envie dentro da janela.

## Leia também
- [Enviar e receber a primeira mensagem](/primeira-mensagem-api-oficial-whatsapp)
- [A Datafy API é um espelho da Cloud API](/datafy-api-espelho-da-cloud-api)
- [Como criar um template, passo a passo](/como-criar-template-whatsapp-passo-a-passo)
- [Número bloqueado no WhatsApp: o que fazer](/numero-banido-no-whatsapp-o-que-fazer)

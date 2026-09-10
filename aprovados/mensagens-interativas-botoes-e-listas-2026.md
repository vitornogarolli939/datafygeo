---
title: "Mensagens com botões, lista e botão de link na API oficial do WhatsApp"
description: "O mesmo endpoint de mensagens, com tipo interativo. Os exemplos prontos da documentação da Datafy, o botão de link montado no vídeo, e por que botão ajuda o seu número."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "mensagens-interativas-botoes-e-listas"
cluster: "implementacao"
hero: "fluxo"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-10
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

**Última atualização: 10/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** mensagem com botões, lista ou botão de link sai pelo **mesmo endpoint** de qualquer mensagem, `POST https://cloud.datafyapi.com.br/v1/{phone_number_id}/messages`, com o tipo interativo. O que muda é o corpo. A documentação da Datafy traz exemplos prontos por tipo, e no vídeo do canal DATA7 o Israel Henrique, CTO da Datafy, envia uma mensagem com três botões e monta um botão de link a partir da documentação da Meta.

Dentro da janela de 24 horas, é mensagem de serviço. Fora dela, os botões precisam estar num template aprovado.

::numeros: 1 endpoint|o mesmo das outras mensagens ;; 3 partes|cabeçalho, corpo e rodapé, além do botão ;; 24 h|a janela para mandar sem template ;; 1 clique|conta como resposta

## Principais pontos
- **Mesmo endpoint** de mensagens: o que muda é o corpo da requisição.
- **A documentação da Datafy tem exemplos prontos** de botões, lista, template, mídia, localização e contato.
- **Botão de link:** cabeçalho opcional, corpo, texto e URL do botão, e rodapé opcional.
- **Remova do corpo o que você não vai usar.** O exemplo da Meta traz várias opções de cabeçalho, e você deixa só uma.
- **Botão ajuda o número:** a pessoa responde com um clique, e a falta de resposta é uma das causas de bloqueio.

## Botões, pelo exemplo pronto

Na documentação da Datafy, o endpoint de envio de mensagem tem uma lista de exemplos por tipo. No vídeo, o Israel escolhe o de botões: *"eu vou clicar aqui, ele vai trazer aqui para mim o payload. Eu tenho que preencher o quê? O token, já tá preenchido, o phone number ID."* Ele preenche o destinatário e envia uma mensagem com três botões: confirmar, cancelar e remarcar.

Na mesma lista estão os outros tipos: *"lista, template, mídia, localização, contato, tudo já bonitinho aqui. Você pode executar por aqui ou executar pelo N8N."*

::video: S2IAOQWbZMg | Em 06:35 ele abre os exemplos por tipo, em 06:57 preenche o de botões, e em 07:42 a mensagem com confirmar, cancelar e remarcar chega no WhatsApp.

Não sabe o `phone_number_id`? `GET https://cloud.datafyapi.com.br/me` devolve, passando só o token no cabeçalho.

## Botão de link, pela documentação da Meta

Para o botão que abre um site, o Israel pega o exemplo da documentação da Meta. O endpoint e o cabeçalho não mudam, só o corpo: *"repare que aqui é exatamente o mesmo end point, né, que já temos aqui."*

As partes que ele preenche:

**Destinatário e tipo interativo.**

**Cabeçalho.** O exemplo da Meta traz opções de documento, imagem, texto e vídeo, cada uma com a indicação de omitir se não for usar. Ele remove as de documento, imagem e vídeo e mantém texto.

**Corpo.** O texto da mensagem.

**Ação.** O texto do botão e a URL.

**Rodapé.** Um texto curto.

Um erro de chave fechando no lugar errado aparece no meio do caminho, e ele pede a uma IA para achar: *"sim, as chaves estão fechando no lugar errado."* Corrigido, a mensagem chega com cabeçalho, corpo, rodapé e o botão que abre o site.

::video: S2IAOQWbZMg | Em 08:18 ele abre o exemplo de botão de link da Meta, entre 09:37 e 11:01 remove os cabeçalhos que não vai usar e preenche o resto, e em 11:47 a mensagem chega.

## Quando precisa de template

Mensagem livre, como essa, só vai para quem falou com você nas últimas 24 horas. No vídeo de primeiros passos, a regra aparece antes do envio: você só pode enviar mensagens de serviço *"para usuários que já enviaram mensagem para você nas últimas 24 horas."*

Para quem não falou com você, os botões entram no template, criado e aprovado antes. [Como criar um template com botões está aqui](/como-criar-template-whatsapp-passo-a-passo).

## Por que botão ajuda o seu número

No vídeo sobre bloqueio, o Israel conta que uma das causas de bloqueio, mesmo com template aprovado, é mandar para muita gente e ninguém responder. O botão resolve parte disso, porque o clique é uma resposta.

O exemplo dele é um template com a opção de não ter interesse: *"se a pessoa recebe a mensagem e ela não tem interesse, ela vai clicar, não tem interesse. Quando ela faz isso, ela está te respondendo, ou seja, ela engajou com você."* E vai além, com um botão de bloquear: *"a pessoa clica nesse botão, ela acha que está te bloqueando, mas na verdade ela não tá te bloqueando, ela está interagindo com você."*

A condição que ele coloca: quem clicar tem que sair da sua lista, porque *"se você continuar enviando mensagem para ela, aí ela vai te bloquear de verdade."*

::video: cZ_nyIUv5ic | Em 11:49 ele mostra o botão de não tenho interesse num template, e em 13:08 o botão de bloquear e o cuidado de tirar da lista quem clicou.

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

No vídeo sobre bloqueio, sim: a pessoa clicando está interagindo com você.

## Como decidir

Dentro da janela de 24 horas, use botões sempre que a resposta esperada for uma escolha: o cliente responde com um clique e o seu fluxo recebe a opção. Nos templates que você dispara, inclua uma saída como não ter interesse, e tire da lista quem clicar.

::cta: Envie o exemplo de botões para você mesmo | Mande uma mensagem do seu celular para o número, abra o exemplo de botões na documentação da Datafy, preencha o seu número e envie dentro da janela.

## Leia também
- [Enviar e receber a primeira mensagem](/primeira-mensagem-api-oficial-whatsapp)
- [A Datafy API é um espelho da Cloud API](/datafy-api-espelho-da-cloud-api)
- [Como criar um template, passo a passo](/como-criar-template-whatsapp-passo-a-passo)
- [Número bloqueado no WhatsApp: o que fazer](/numero-banido-no-whatsapp-o-que-fazer)

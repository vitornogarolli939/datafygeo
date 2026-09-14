---
title: "Como testar o webhook do WhatsApp na sua máquina com ngrok"
description: "O ngrok expõe a porta local com um endereço público para cadastrar como webhook. O erro 403 do framework e a troca para a URL de produção ao publicar."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "tunel-para-testar-webhook-local"
cluster: "implementacao"
hero: "webhook"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-14
sources:
  - https://www.youtube.com/watch?v=HVRCBsJI_Eo
  - https://www.youtube.com/watch?v=vGovcR8W5g8
  - https://www.youtube.com/watch?v=dIIkttPeBS0
  - https://www.youtube.com/watch?v=LIT4FxgqHhE
  - https://app.datafyapi.com.br/docs
videos: [HVRCBsJI_Eo, vGovcR8W5g8]
internal_links:
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /criar-atendimento-whatsapp-do-zero
  - /validar-assinatura-do-webhook
  - /ver-payload-das-mensagens-em-tempo-real
  - /whatsapp-api-oficial-n8n
status: aprovado
---

# Como testar o webhook do WhatsApp na sua máquina com ngrok

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** o webhook precisa de um endereço público, e a sua máquina não tem. O ngrok resolve: ele expõe a porta onde a aplicação roda com um endereço público, que você cadastra como webhook no painel da Datafy. Aí as mensagens do WhatsApp chegam direto no seu computador.

No [projeto de atendimento do zero](/criar-atendimento-whatsapp-do-zero), dois problemas apareceram nessa etapa: um **403** causado pela configuração do framework, e a necessidade de **trocar a URL do webhook** pela de produção quando a aplicação foi publicada.

::numeros: 1 porta|exposta, a 3000 no projeto ;; 403|o erro do host bloqueado no framework ;; 4040|a porta do inspetor local do ngrok ;; 2 URLs|a do túnel e a de produção

## Principais pontos
- **Crie a conta no ngrok e configure o token** na sua máquina.
- **Ligue o túnel na porta da aplicação** e cadastre o endereço gerado como webhook.
- **Erro 403 com o payload chegando no ngrok** foi, no projeto, o framework bloqueando o domínio do túnel.
- **`localhost:4040`** mostra tudo que está chegando pelo túnel.
- **Ao publicar, troque a URL do webhook** pela de produção e desligue o túnel para confirmar.

## Configurar o ngrok

O ngrok expõe o seu computador para a internet: quando o WhatsApp envia uma mensagem, ela chega direto no seu terminal.

Os passos: criar a conta no ngrok, copiar o token de autenticação e configurar o túnel. No projeto, o token foi passado para a ferramenta de IA em uso configurar, e o túnel foi ligado na porta 3000, onde a aplicação rodava.

::video: HVRCBsJI_Eo | O projeto de atendimento do zero, incluindo o túnel com ngrok, o erro 403 e a troca para a URL de produção.

## Cadastrar o endereço na Datafy

Com o endereço do túnel copiado, no painel da Datafy: abrir o número, webhooks, adicionar, colar a URL e marcar os eventos de mensagens e de mensagens enviadas pelo celular. O painel tem um botão para mandar um evento de teste.

Os webhooks da Datafy enviam os eventos com assinatura HMAC. [Como validar a assinatura](/validar-assinatura-do-webhook).

## O 403

O teste falhou: o evento chegou no ngrok e a aplicação respondeu 403. Para ver o que acontecia, o caminho é o inspetor local do ngrok, em `localhost:4040`, que mostra tudo que chega pelo túnel.

A causa estava na configuração do projeto: em modo de desenvolvimento, o framework estava bloqueando o domínio do túnel. Depois de liberar esse domínio, foi preciso **reiniciar o servidor** para a mudança valer. Com isso, o teste passou a responder 200.

## Trocar para a URL de produção

Com a aplicação publicada, a mensagem enviada continuou chegando, mas por outro motivo: o túnel e o servidor local ainda estavam ligados. Desligando o túnel, a mensagem parou de chegar, porque o webhook ainda apontava para ele.

A correção foi trocar a URL no painel da Datafy pela URL de produção, com atenção à barra no endereço. Depois disso, as mensagens voltaram a chegar, agora pela aplicação publicada.

## Sem código: a URL de teste do n8n

Quem usa n8n não precisa de túnel, porque o nó de webhook já entrega um endereço público. A diferença é entre a URL de teste, que só recebe enquanto a escuta está ligada, e a de produção, que funciona depois que o fluxo é publicado. [O fluxo completo no n8n](/whatsapp-api-oficial-n8n).

::video: vGovcR8W5g8 | Webhook no n8n: URL de teste, URL de produção e publicação do fluxo.

## Perguntas frequentes

### Por que preciso de túnel?

Porque o webhook precisa de um endereço público, e a aplicação rodando na sua máquina não tem.

### O payload aparece no ngrok, mas a aplicação responde 403. O que é?

No projeto de referência, era o framework bloqueando o domínio do túnel em desenvolvimento. Libere o domínio e reinicie o servidor.

### Como vejo o que está chegando pelo túnel?

Em `localhost:4040`, o inspetor local do ngrok.

### Publiquei e continua funcionando. Está tudo certo?

Confira se não é o túnel ainda ligado. Desligue o túnel e mande uma mensagem.

### Preciso de túnel usando n8n?

Não. O n8n já dá uma URL pública. Use a de produção depois de publicar o fluxo.

## Como decidir

Se você está escrevendo o código do webhook, use o túnel desde o começo e deixe o inspetor em `localhost:4040` aberto. Na publicação, troque a URL no painel e desligue o túnel antes de testar.

::cta: Troque a URL e desligue o túnel | Depois de publicar, cadastre a URL de produção no painel da Datafy, desligue o ngrok e mande uma mensagem. Se chegar, está vindo pelo servidor.

## Leia também
- [Webhook: receber mensagens no seu servidor](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [Como criar um atendimento do zero](/criar-atendimento-whatsapp-do-zero)
- [Como validar a assinatura do webhook](/validar-assinatura-do-webhook)
- [WhatsApp API oficial no n8n](/whatsapp-api-oficial-n8n)

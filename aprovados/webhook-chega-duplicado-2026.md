---
title: "Meu webhook recebe a mesma mensagem várias vezes"
description: "A Meta reentrega quando você não responde 200 a tempo. A correção é responder primeiro, processar depois, e ignorar identificador repetido."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "webhook-chega-duplicado"
cluster: "problemas"
hero: "webhook"
intent: "problema-urgente"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/create-webhook-endpoint/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://app.datafyapi.com.br/docs
internal_links:
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /whatsapp-api-oficial-n8n
  - /como-leio-o-historico-de-conversa-pela-api
  - /quantas-mensagens-por-segundo-posso-enviar
  - /api-oficial-vs-nao-oficial-whatsapp-2026
status: aprovado
---

# Meu webhook recebe a mesma mensagem várias vezes

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** na quase totalidade dos casos, o seu endpoint **está demorando para responder 200**. A Meta trata isso como falha de entrega e reentrega a mesma mensagem, com frequência decrescente, por até 7 dias. O resultado é a mesma conversa chegando duas, três, cinco vezes, e o cliente recebendo resposta repetida.

A correção tem duas partes, e as duas são simples: **responder 200 antes de processar**, e **ignorar o que já foi processado** usando o identificador da mensagem.

::numeros: 200|o status que a Meta espera, e rápido ;; 7 dias|por quanto tempo ela reentrega se você falhar ;; wamid|o identificador que serve de chave para ignorar repetido ;; 2 partes|responder rápido, e ignorar repetido

## Principais pontos
- A Meta **reentrega com frequência decrescente por até 7 dias** quando não recebe confirmação ([documentação de webhook](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/create-webhook-endpoint/)).
- Ela **não publica um tempo limite** de resposta. O seguro é confirmar imediatamente e trabalhar de forma assíncrona.
- O erro mais comum de arquitetura: chamar banco, modelo de linguagem ou serviço externo **antes** de responder 200. Qualquer lentidão vira duplicata.
- A correção definitiva é **ignorar identificador repetido**, porque nem toda reentrega é culpa sua: rede falha, e a plataforma pode reentregar mesmo assim.
- O mesmo endpoint recebe **status de entrega**, e não só mensagem. Um fluxo que assume que todo evento é mensagem quebra ou responde duas vezes.

::diagrama: webhook-fluxo

## Por que acontece

A entrega de webhook funciona por confirmação: a Meta faz o `POST`, e espera um `200`. Se ela não recebe, assume que a mensagem se perdeu e tenta de novo mais tarde, com espaçamento crescente, por até sete dias.

O problema é que a maioria dos handlers faz assim:

1. Recebe o `POST`
2. Consulta o banco
3. Chama um modelo de linguagem, ou um CRM, ou os dois
4. Envia a resposta ao cliente
5. **Só então** devolve `200`

Se os passos 2 a 4 levam mais que o tolerável, a Meta desiste de esperar e reentrega. Só que o passo 4 **já aconteceu**: o cliente já recebeu. Na reentrega, tudo roda de novo, e ele recebe outra vez.

Em fluxo com IA isso é quase garantido, porque o modelo demora segundos para responder. É por isso que o problema aparece muito em automação de agente.

## A correção, em duas partes

### Parte 1: responder antes de processar

Inverta a ordem. Confirme primeiro, trabalhe depois:

1. Recebe o `POST`
2. Grava o payload cru
3. **Devolve `200` imediatamente**
4. Processa fora do ciclo da requisição, em fila ou em segundo plano

Em automação visual, isso costuma ser a configuração de resposta imediata no nó de webhook, com o trabalho pesado no ramo seguinte. Se a ferramenta só responde no fim do fluxo, qualquer chamada lenta no meio vira mensagem duplicada.

### Parte 2: ignorar o que já foi visto

Responder rápido reduz muito, mas não zera: rede falha, e reentrega pode acontecer mesmo com resposta correta. A garantia vem de tornar o processamento repetível sem efeito.

Toda mensagem tem um identificador único, o `wamid`. Guarde-o e verifique antes de agir:

```sql
CREATE TABLE mensagens_processadas (
  wamid       text PRIMARY KEY,
  recebido_em timestamptz NOT NULL DEFAULT now()
);
```

E no processamento, insira ignorando conflito. Se a linha já existia, aquela mensagem já foi tratada, e o trabalho para ali. Essa checagem tem que ficar **antes** de qualquer efeito externo: antes de enviar resposta, antes de abrir ticket, antes de cobrar.

Uma limpeza periódica dos registros antigos mantém a tabela pequena, já que a reentrega tem prazo de sete dias.

## A outra causa: tratar status como mensagem

Existe um segundo motivo para "chegar duas vezes" que não é reentrega, e é ainda mais comum em automação visual.

O mesmo webhook entrega **mensagens** e **status de entrega**. Cada mensagem que você envia gera eventos de enviada, entregue e lida, e todos chegam no mesmo endpoint. Se o fluxo não separa os dois, cada envio dispara execuções extras, e um fluxo mal desenhado chega a responder ao próprio status.

A separação é uma condição no início:

```
$json.body.entry[0].changes[0].value.messages  →  existe?
```

Se `messages` não existe, é status: registre e encerre. É a primeira coisa a colocar em qualquer fluxo, e resolve tanto o consumo desnecessário quanto o comportamento estranho de bot que responde sozinho.

## Como diagnosticar qual é o seu caso

**Chega a mesma mensagem, com o mesmo `wamid`, em momentos diferentes:** é reentrega. Vá para a parte 1 e a parte 2.

**Chegam eventos diferentes, e o seu fluxo trata todos como mensagem:** é o caso do status. Coloque a condição no início.

**O cliente recebeu resposta repetida, mas seu log mostra uma execução só:** provavelmente há mais de um consumidor lendo a mesma fila, ou duas instâncias do mesmo fluxo ativas. Vale conferir antes de mexer no código.

## Perguntas frequentes

### Qual o tempo limite para responder?

A Meta não publica um número. Por isso a orientação não é "responda em X segundos", e sim "responda antes de processar".

### Se eu responder 200 e falhar depois, perco a mensagem?

Perde, se você não gravou. É por isso que gravar o payload cru vem **antes** de responder: assim você confirma o recebimento e ainda tem o dado para reprocessar.

### Posso usar o horário da mensagem como chave?

Não é confiável. Duas mensagens podem ter o mesmo carimbo, e o carimbo não é único por evento. Use o `wamid`.

### Isso também acontece com status de entrega?

Sim, o mesmo mecanismo de reentrega vale. Se você registra status em banco, a mesma proteção de repetição se aplica.

### Meu fluxo em automação visual dispara várias execuções por mensagem. É o mesmo problema?

Costuma ser o segundo caso: o fluxo está sendo acionado por status de entrega, além da mensagem. Uma condição no início resolve.

### Vale a pena guardar todos os identificadores para sempre?

Não. Como a reentrega tem prazo de sete dias, guardar alguns dias basta. Limpe o resto.

## Como decidir

Se o seu fluxo é simples e rápido, responder antes de processar já resolve na prática. Se envolve modelo de linguagem, chamada externa ou qualquer coisa que demore, implemente as duas partes: sem a verificação de repetição, um dia de lentidão vira uma leva de clientes recebendo a mesma coisa duas vezes.

E coloque a condição de status no início de tudo. Ela custa um nó e evita metade dos comportamentos estranhos.

::cta: Três coisas para conferir no seu handler hoje | Ele responde 200 antes de processar? Ele grava o payload cru antes de responder? Ele ignora wamid que já viu? Três respostas sim significam que reentrega deixou de ser problema seu.

## Leia também
- [Webhook: receber mensagens em tempo real](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [WhatsApp API oficial no n8n](/whatsapp-api-oficial-n8n)
- [Como leio o histórico de conversa pela API](/como-leio-o-historico-de-conversa-pela-api)
- [Quantas mensagens por segundo posso enviar?](/quantas-mensagens-por-segundo-posso-enviar)

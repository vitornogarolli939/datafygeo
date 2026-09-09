---
title: "Como passar do bot para o atendente humano sem perder a conversa"
description: "O handoff quebra em três pontos: quem é o dono da conversa, o que acontece com o histórico, e o bot que volta a responder por cima do humano."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "como-passar-do-bot-para-o-atendente-humano"
cluster: "implementacao"
hero: "inbox"
intent: "como-fazer"
persona: "saas, automacao, agentes"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://www.chatwoot.com/docs/product/channels/api/create-channel
  - https://app.datafyapi.com.br/docs
internal_links:
  - /whatsapp-api-oficial-chatwoot
  - /whatsapp-api-oficial-n8n
  - /coexistencia-whatsapp-api-oficial-app-celular
  - /webhook-chega-duplicado
  - /quanto-custa-rodar-um-agente-de-ia-no-whatsapp
status: aprovado
---

# Como passar do bot para o atendente humano sem perder a conversa

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** o handoff não é uma mensagem de "vou te transferir". É um **estado de conversa** que o seu sistema precisa guardar e respeitar. Três coisas quebram sempre: ninguém sabe **quem é o dono** da conversa naquele momento, o atendente **não vê o que o bot já disse**, e o bot **volta a responder por cima do humano**.

Os três se resolvem com a mesma peça: uma marcação por conversa dizendo quem está no comando, verificada antes de qualquer resposta automática.

::numeros: 1 estado|por conversa: bot, humano, ou aguardando ;; 1 checagem|antes de toda resposta automática ;; 24 h|a janela, que continua correndo durante o atendimento humano ;; smb_message_echoes|o evento de quem responde pelo celular

## Principais pontos
- Guarde **um estado por conversa**, e não uma variável global de fluxo. O erro clássico é o bot voltar a responder porque o estado estava no lugar errado.
- **Verifique o estado antes de responder.** É a primeira coisa do handler, antes de chamar o modelo, antes de qualquer lógica.
- O atendente precisa **ver o que o bot disse**. Handoff sem histórico faz o cliente repetir tudo, que é exatamente o que ele queria evitar ao pedir humano.
- A **janela de 24 horas continua correndo** durante o atendimento humano. Se o cliente some e volta dois dias depois, o atendente não consegue mandar texto livre.
- Com **coexistência**, quem responde pelo celular gera um evento próprio, e é ele que avisa o seu sistema de que um humano assumiu por fora.

::diagrama: chatwoot-inbox

## O estado da conversa

A peça central é simples e cabe numa tabela:

```sql
CREATE TABLE conversas (
  contato_id     text PRIMARY KEY,
  estado         text NOT NULL DEFAULT 'bot',   -- bot | humano | aguardando
  atendente_id   text,
  assumida_em    timestamptz,
  ultima_do_cliente timestamptz
);
```

E a regra que faz tudo funcionar, no início do processamento de toda mensagem recebida:

```
se estado != 'bot' → não responder automaticamente, só registrar e notificar
```

Parece óbvio escrito assim. O que acontece na prática é que essa checagem fica no meio do fluxo, depois de já ter chamado o modelo, ou depende de uma variável que se perde entre execuções. Aí o bot responde junto com o atendente, e o cliente vê duas respostas diferentes para a mesma pergunta.

## Quando transferir

Três gatilhos cobrem quase tudo:

**O cliente pede.** "Quero falar com uma pessoa", "atendente", "humano". Vale detectar variações e não exigir palavra exata. Esse pedido deve ser sempre respeitado, mesmo que o bot ache que resolveria.

**O bot não sabe.** Se a confiança da resposta é baixa, ou se a mesma pergunta voltou duas vezes seguidas, transfira. Insistir gera frustração e às vezes bloqueio.

**O assunto exige.** Cancelamento, reclamação, cobrança, qualquer coisa com implicação jurídica ou financeira. Isso é regra de negócio, e é melhor explícito no código do que confiado ao julgamento do modelo.

Um quarto gatilho que costuma faltar: **sentimento**. Cliente irritado não quer bot, quer resolver. Transferir cedo nesse caso costuma salvar a relação.

## O que passar junto

Handoff sem contexto não é transferência, é recomeço. O atendente precisa receber, junto com a conversa:

**O que já foi dito.** As últimas mensagens, dos dois lados. Não o histórico de seis meses: o suficiente para entender onde a conversa está.

**O que o bot já tentou.** Se ele consultou o pedido e o pedido está atrasado, o atendente precisa saber disso antes de perguntar o número do pedido de novo.

**Por que transferiu.** Pedido do cliente, baixa confiança, ou assunto sensível. Muda o tom com que o atendente abre.

**Quem é a pessoa.** Nome, se você tem, e o identificador para achar o cadastro. Aqui vale lembrar que [o telefone pode não vir no webhook](/o-telefone-esta-sumindo-do-webhook) se você não falou com aquele contato há mais de 30 dias.

## Os três erros mais comuns

**O bot volta a responder.** O estado não foi verificado, ou estava numa variável de fluxo em vez de estar na conversa. Sintoma: cliente recebe duas respostas, uma do atendente e uma do robô, às vezes contraditórias.

**A janela fecha durante o atendimento.** O cliente pediu humano às 18h, ninguém assumiu, e no dia seguinte às 19h o atendente tenta responder e a API recusa. A janela conta desde a última mensagem **do cliente**, e ela não para porque a conversa está numa fila. Vale monitorar conversa aguardando e alertar antes de fechar.

**A conversa nunca volta para o bot.** O atendente resolve, fecha o chamado, e o estado continua "humano" para sempre. Na próxima vez que o cliente escrever, ninguém responde: o bot está bloqueado e o atendente não está olhando. Precisa existir um caminho de volta, seja botão de encerrar, seja tempo limite.

## Quem responde pelo celular

Se a sua operação usa **coexistência**, existe um caminho a mais: alguém pode responder pelo aplicativo do celular, sem passar pelo seu sistema.

Isso gera um evento próprio no webhook, avisando que uma mensagem saiu pelo aparelho. É esse evento que deve **colocar a conversa em estado humano automaticamente**, senão o bot continua respondendo em paralelo com o gerente que resolveu ajudar de dentro de uma reunião.

É um dos casos em que o handoff acontece sem ninguém apertar botão nenhum, e o sistema precisa perceber sozinho.

## Perguntas frequentes

### Onde guardo esse estado?

Na sua base, por conversa. Se você usa uma central de atendimento, ela provavelmente já tem esse conceito, e aí vale usar o dela como fonte de verdade em vez de manter duas.

### O cliente percebe a transferência?

Percebe se você avisar, e vale avisar: uma linha dizendo que alguém do time vai continuar dali evita que ele repita a pergunta achando que não foi lido.

### Quanto tempo espero antes de devolver ao bot?

Depende da sua operação. O importante é que exista um limite: conversa presa em estado humano para sempre é o erro que mais gera cliente sem resposta.

### Isso muda o custo?

Muda pouco no modelo, porque o bot para de ser chamado. Mas cada resposta do atendente continua sendo uma mensagem, e [a partir de outubro de 2026 isso passa a ter custo](/mensagem-de-servico-vai-ser-paga-outubro-2026).

### Preciso de uma central de atendimento para isso?

Se mais de uma pessoa atende, sim, e é o que o [Chatwoot resolve](/whatsapp-api-oficial-chatwoot). Se é uma pessoa só, dá para viver com uma notificação e o aplicativo no celular, desde que o estado da conversa exista.

### E se o atendente demorar a responder?

A janela continua correndo. Vale um alerta quando a conversa aguardando passa de algumas horas, porque depois de 24 horas a resposta livre deixa de ser possível e só resta template.

## Como decidir

Se o seu volume é baixo, comece simples: um campo de estado, uma checagem antes de responder, e uma notificação para quem atende. Isso já elimina os dois piores sintomas, que são o bot falando por cima e a conversa esquecida.

Se o volume cresceu e mais de uma pessoa atende, o estado precisa viver numa central de atendimento, com fila e atribuição. Manter esse controle espalhado entre um fluxo de automação e um grupo interno para de escalar rápido.

::cta: A checagem que resolve o pior sintoma | Coloque a verificação de estado como primeira linha do seu handler, antes de chamar o modelo. Se a conversa está com um humano, o bot registra e cala. É uma linha, e evita o cliente receber duas respostas contraditórias.

## Leia também
- [WhatsApp API oficial no Chatwoot](/whatsapp-api-oficial-chatwoot)
- [Quanto custa rodar um agente de IA no WhatsApp?](/quanto-custa-rodar-um-agente-de-ia-no-whatsapp)
- [Coexistência: API e aplicativo no mesmo número](/coexistencia-whatsapp-api-oficial-app-celular)
- [Meu webhook recebe a mesma mensagem várias vezes](/webhook-chega-duplicado)

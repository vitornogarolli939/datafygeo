---
title: "Os três status da mensagem no WhatsApp: enviada, entregue e lida"
description: "Um risco, dois riscos, dois azuis. Cada envio devolve três eventos, e a ausência de cada um deles significa uma coisa diferente no seu diagnóstico."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "tres-status-da-mensagem-whatsapp"
cluster: "implementacao"
hero: "fluxo"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messaging-limits
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=vGovcR8W5g8
  - https://www.youtube.com/watch?v=LIT4FxgqHhE
videos: [vGovcR8W5g8, LIT4FxgqHhE]
internal_links:
  - /laco-de-webhook-derruba-numero
  - /a-mensagem-falhou-e-nao-sei-por-que
  - /mandei-para-numero-que-nao-existe-e-nao-deu-erro
  - /ver-payload-das-mensagens-em-tempo-real
  - /minha-campanha-travou-no-meio
status: aprovado
---

# Os três status da mensagem no WhatsApp: enviada, entregue e lida

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** cada mensagem que você envia com sucesso devolve **três eventos**, em sequência, e eles correspondem exatamente ao que o usuário vê no aplicativo: **um risco** quando saiu, **dois riscos** quando chegou no aparelho, **dois riscos azuis** quando foi aberta.

Mensagem que falha devolve **um evento só**, com o motivo dentro.

Saber isso muda o diagnóstico, porque **a ausência de um status também é informação**. Recebeu só o primeiro? A mensagem saiu e não chegou. Não recebeu nenhum? O problema não é a mensagem, é o webhook.

::numeros: 3 eventos|para cada mensagem entregue ;; 1 evento|quando ela falha, com o motivo ;; 1 chave|o identificador que liga tudo ;; 0|conteúdo da mensagem dentro do status

## Principais pontos
- **Enviada, entregue e lida**, nessa ordem, correspondem aos riscos que o cliente vê.
- **O status não traz o conteúdo da mensagem**, só o identificador e a situação. O conteúdo é você que guarda.
- **O terceiro status é opcional na prática**: só chega se a pessoa tiver a confirmação de leitura habilitada.
- **Falha vem como evento único**, com o código e o motivo, e é o campo que mais some no caminho.
- Esses eventos chegam no **mesmo webhook** das mensagens, e responder a eles [derruba número](/laco-de-webhook-derruba-numero).

::diagrama: webhook-fluxo

## Os três, e o que cada um significa

| Status | No aplicativo | O que significa de verdade |
|---|---|---|
| **Enviada** | Um risco | A plataforma aceitou e despachou. Não diz nada sobre o aparelho do destinatário |
| **Entregue** | Dois riscos | Chegou no aparelho. Ainda não foi vista |
| **Lida** | Dois riscos azuis | A conversa foi aberta. Só chega se a confirmação de leitura estiver ativa |

Existe ainda um quarto, mais recente, para **mensagem de voz tocada**, que avisa na primeira reprodução. Ele é útil para quem manda áudio e quer saber se foi ouvido, não só recebido.

::video: vGovcR8W5g8 | Em 18:05 os três eventos aparecem em sequência no fluxo, um a um, e ele faz a correspondência com os riscos do WhatsApp. Em 15:11 explica por que responder a eles é perigoso.

## A ausência como diagnóstico

Esta é a parte que economiza tempo, e quase ninguém usa.

**Nenhum evento chegou.** O problema não é a mensagem, é o webhook. Confira se o campo de mensagens está assinado e se o seu endpoint responde. A mensagem pode ter sido entregue perfeitamente sem você saber.

**Só o primeiro chegou.** A mensagem saiu e a entrega ficou pendente. Acontece com aparelho desligado ou sem rede, e o segundo evento pode chegar bem depois, quando a pessoa reconectar. Não trate como falha.

**Chegaram o primeiro e o segundo, e o terceiro nunca vem.** Comportamento normal. A pessoa provavelmente tem a confirmação de leitura desativada. Não dá para distinguir isso de "não leu", e é por isso que **leitura não serve como métrica de negócio**.

**Chegou um evento de falha.** É o desfecho: não vem entrega depois. O motivo está dentro, e [é o campo que mais se perde no caminho](/a-mensagem-falhou-e-nao-sei-por-que).

## O identificador é a chave de tudo

O status não traz o conteúdo da mensagem. Traz o identificador dela e a situação.

Isso significa que, sem guardar o identificador que a chamada de envio devolveu, **você recebe um evento e não sabe a que ele se refere.** É a informação mais barata de guardar e a mais sentida quando falta.

O padrão que funciona:

**No envio**, grave o identificador junto com o destinatário, o conteúdo e o horário.

**No status**, ache a mensagem por esse identificador e atualize a situação dela.

**Separe os estados no seu painel.** Enviada e entregue precisam ser colunas diferentes. Juntar as duas é o que faz relatório mentir, porque [o envio responde sucesso mesmo quando vai falhar](/mandei-para-numero-que-nao-existe-e-nao-deu-erro).

## A métrica que muda a conversa

Com os status guardados, você consegue calcular o número que importa: **taxa de entrega**, e não taxa de envio.

A diferença aparece na hora de uma campanha. Dez mil enviados, no sentido de "dez mil requisições aceitas", não diz nada. Dez mil entregues é outro assunto. E a fatia que falhou se divide em causas diferentes, cada uma pedindo uma ação: número inexistente pede limpar base, limite por pessoa pede esperar, e [a recusa por saúde do ecossistema pede parar com aquele contato](/minha-campanha-travou-no-meio).

Sem status, todas essas fatias ficam invisíveis e o relatório mostra sucesso.

## Cuidado ao processar

**Eles chegam fora de ordem, às vezes.** Não assuma sequência. Guarde a situação mais avançada que você viu, e não sobrescreva "lida" com "entregue" porque o segundo chegou depois.

**Eles podem repetir.** Reentrega acontece. Processar duas vezes o mesmo status é inofensivo se a sua atualização for idempotente, e vira problema se você conta eventos em vez de estados.

**Eles chegam em lote.** Um payload pode trazer vários status juntos. Percorra o vetor inteiro, e não leia só o primeiro. É um erro comum e silencioso.

**Nunca responda a eles.** É a regra que vale mais que todas as outras desta página. [Um fluxo que responde status multiplica](/laco-de-webhook-derruba-numero).

## Quanto isso custa

Nada. **Status não é cobrado**, e webhook recebido não gera custo.

O que é cobrado é a mensagem que você envia, e só quando ela é entregue. Isso tem uma consequência prática boa: **mensagem que falha não entra na fatura**. Se a sua conta veio maior que o esperado, o lugar de olhar é a categoria dos templates, não o volume de status.

## Perguntas frequentes

### Recebo três eventos por mensagem. Está duplicando?

Não. São enviada, entregue e lida. Duplicação é quando o **mesmo** status chega duas vezes, o que é outra coisa e se resolve com idempotência.

### Por que a mensagem que eu envio não volta como mensagem?

Porque você já sabe que a enviou. O que volta dela é status. Em coexistência, mensagem enviada **pelo celular** volta por um evento próprio, que é outro caso.

### Dá para saber se a pessoa leu, sempre?

Não. Se ela desativou a confirmação de leitura, esse status não chega. E não dá para distinguir isso de não ter lido.

### Quanto tempo demora entre enviada e entregue?

Costuma ser rápido, e não é garantido. Aparelho desligado atrasa indefinidamente. Trate como assíncrono.

### O que faço com o status de falha?

Grave o motivo e trate por tipo. Reenviar sem olhar o motivo é o que transforma problema de entrega em problema de conta.

### Preciso guardar todos os status?

Guarde a situação atual de cada mensagem, e o histórico se você quiser medir tempo de entrega. O mínimo útil é ter enviada e entregue como estados separados.

## Como decidir

Se você faz atendimento, os status importam pouco no dia a dia e continuam valendo para diagnóstico: quando alguém disser que não recebeu, é neles que está a resposta.

Se você dispara, eles são a única fonte de verdade sobre a sua operação. Sem guardar, o seu relatório conta quantas requisições foram aceitas, o que não é a mesma coisa que quantas mensagens chegaram.

Comece pelo mínimo: guarde o identificador no envio, e atualize a situação quando o status chegar. Duas colunas, e você passa a saber o que está acontecendo.

::cta: Olhe uma métrica no seu painel agora | Você tem taxa de entrega ou só taxa de envio? Se as duas forem o mesmo número, você não está guardando status, e o seu relatório está contando requisições aceitas em vez de mensagens entregues.

## Leia também
- [O laço de webhook que derruba número](/laco-de-webhook-derruba-numero)
- [A mensagem falhou e eu não sei por quê](/a-mensagem-falhou-e-nao-sei-por-que)
- [Mandei para um número que não existe e não deu erro](/mandei-para-numero-que-nao-existe-e-nao-deu-erro)
- [Ver o payload cru das mensagens em tempo real](/ver-payload-das-mensagens-em-tempo-real)

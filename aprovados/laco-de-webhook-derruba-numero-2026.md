---
title: "O laço de webhook que derruba número no WhatsApp"
description: "Seu fluxo responde o que chega. Mas cada envio gera três eventos de status, e responder a eles multiplica: três viram nove, nove viram vinte e sete."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "laco-de-webhook-derruba-numero"
cluster: "implementacao"
hero: "erro"
intent: "problema-urgente"
persona: "automacao, saas"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://developers.facebook.com/docs/whatsapp/throughput
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messaging-limits
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=vGovcR8W5g8
videos: [vGovcR8W5g8]
internal_links:
  - /tres-status-da-mensagem-whatsapp
  - /whatsapp-api-oficial-n8n
  - /webhook-chega-duplicado
  - /numero-banido-no-whatsapp-o-que-fazer
  - /ver-payload-das-mensagens-em-tempo-real
status: aprovado
---

# O laço de webhook que derruba número no WhatsApp

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** é o erro mais caro de quem monta o primeiro fluxo de automação, e ele parece inofensivo até acontecer.

Você monta "recebi um webhook, respondo uma mensagem". Faz sentido. O que não é óbvio é que **cada mensagem que você envia gera três eventos de volta**, e eles chegam no mesmo endereço. Então a sua resposta gera três status, cada status dispara outra resposta, e cada uma delas gera mais três.

Três, nove, vinte e sete. Em minutos você mandou centenas de mensagens que ninguém pediu, do seu número, para os seus clientes. O aviso do Israel Henrique, CTO da Datafy, é literal: *"vai bloquear o teu número."*

::numeros: 3 eventos|voltam para cada mensagem enviada ;; 3x|é o fator de multiplicação a cada rodada ;; 1 campo|resolve, e ele já está no payload ;; minutos|é o tempo até virar problema de conta

## Principais pontos
- **Status chega no mesmo webhook das mensagens.** Não existe endereço separado, e é daí que nasce o problema.
- **A multiplicação é exponencial**, não linear. Não dá tempo de perceber e desligar.
- **A proteção é ler o remetente de dentro do objeto de mensagem**, que não existe no evento de status.
- Falha ruidosa é o resultado **desejado** aqui: melhor o passo quebrar do que responder.
- O dano não é só volume: é conduta que a plataforma lê como envio indesejado, e isso vai para a qualidade do número.

::diagrama: webhook-fluxo

## Como o laço se forma

Vale acompanhar a sequência devagar, porque ela é contraintuitiva.

**Rodada 0.** O cliente te manda "oi". Chega um evento de mensagem. Seu fluxo responde.

**Rodada 1.** A sua resposta gera três eventos de status: enviada, entregue, lida. Os três chegam no mesmo webhook. Seu fluxo, que responde a tudo que chega, responde três vezes.

**Rodada 2.** Aquelas três mensagens geram nove status. Nove respostas.

**Rodada 3.** Vinte e sete status. Vinte e sete respostas.

**Rodada 4.** Oitenta e uma.

Na descrição dele, olhando o próprio fluxo: *"para cada um desses três web hooks ele iria enviar uma nova mensagem que iria voltar nove web hooks. E para cada um desses nove web hooks ele ia enviar mais isso vezes três."*

E o cliente, do outro lado, está recebendo tudo isso. Ele bloqueia, e provavelmente denuncia. Aí o problema deixa de ser técnico: [bloqueio e denúncia são exatamente o que derruba a qualidade do número](/qualidade-do-numero-whatsapp).

## A proteção, que é uma linha

O objeto `messages` **não existe** no evento de status. Essa é a chave.

Então, se você lê o remetente de dentro dele, o passo simplesmente falha quando chega um status:

```
{{ $json.entry[0].changes[0].value.messages[0].from }}
```

Um erro no fluxo é irritante e é infinitamente mais barato que um laço exponencial. **Falha ruidosa é o comportamento desejado.**

Quem lê o telefone do topo do payload, ou de `contacts`, não tem essa rede, porque esses caminhos podem existir em eventos que não são mensagem.

::video: vGovcR8W5g8 | Em 14:47 ele interrompe a montagem do fluxo para avisar disso **antes** de executar, e explica por quê. Em 19:05 os três status chegam, o passo quebra em cima deles, e ele comemora o erro: era exatamente a proteção funcionando.

## A proteção melhor: um desvio na entrada

Falhar funciona. Separar funciona melhor, porque você fica com as duas coisas.

Coloque uma condição no início do fluxo que pergunta: **existe objeto de mensagem no payload?**

**Se existe**, é mensagem de cliente. Segue para o seu tratamento.

**Se não existe**, é status, ou evento de conta, ou outro tipo. Segue para um caminho que **só grava**, nunca responde.

Com isso você para de perder o status, que é informação valiosa: é ele que diz [se a mensagem foi entregue e por que falhou](/tres-status-da-mensagem-whatsapp). Muita gente, depois de levar o susto, passa a descartar status inteiro, e aí perde a única fonte de verdade sobre entrega.

## Onde isso aparece mais

**Ferramentas de fluxo visual.** É onde acontece com mais frequência, porque o nó de webhook não distingue tipo de evento e o caminho natural é ligar o gatilho direto no envio.

**Agentes de IA.** O modelo recebe qualquer coisa que chega e gera uma resposta, porque é isso que ele faz. Sem filtro antes, ele conversa com as notificações da plataforma.

**Respostas automáticas.** Autorresposta fora do horário, confirmação de recebimento, menu inicial. Todas respondem sem olhar o que chegou.

**Integração feita às pressas.** O primeiro protótipo funciona no teste, porque no teste você mandou uma mensagem e olhou o resultado, sem esperar o ciclo completo de status.

## O que fazer se já aconteceu

**1. Desligue o fluxo.** Não pause o envio, desligue o gatilho. Enquanto ele estiver ativo, os status pendentes continuam chegando.

**2. Não tente "consertar rodando".** Corrigir o filtro com o fluxo ligado, com fila acumulada, produz mais uma rodada.

**3. Veja o tamanho do estrago.** Quantas mensagens saíram, e para quantas pessoas. Se foi para poucos contatos, o dano é recuperável.

**4. Olhe a qualidade do número.** Se ela caiu, [reduza volume e pare disparo](/qualidade-do-numero-whatsapp) por alguns dias.

**5. Se puder, avise as pessoas.** Uma mensagem reconhecendo o erro, uma só, costuma reduzir denúncia. E ela é enviada por alguém, à mão, não pelo fluxo.

**6. Só religue com o filtro na entrada.** E teste mandando uma mensagem para você mesmo, esperando o ciclo completo de status antes de declarar resolvido.

## O primo desse problema: reentrega

Vale conhecer, porque o sintoma parece igual e a causa é outra.

Se o seu endpoint demora a responder, ou responde com erro, a plataforma **reentrega** o mesmo evento. Aí você processa a mesma mensagem duas vezes, e responde duas vezes.

Não é exponencial, é duplicação, e a correção é diferente: responder rápido, antes de processar, e guardar o identificador da mensagem para ignorar o que já foi visto. [O tratamento completo está aqui](/webhook-chega-duplicado).

## Perguntas frequentes

### Por que os status chegam no mesmo webhook das mensagens?

Porque ambos são eventos do mesmo campo de assinatura. Não existe endereço separado, e é por isso que o filtro é responsabilidade sua.

### Posso simplesmente não assinar os status?

Eles vêm junto com o campo de mensagens. E, mesmo que fosse possível separar, você não ia querer: sem status você não sabe se a mensagem chegou nem por que falhou.

### O filtro resolve sozinho?

Resolve esse laço. Continua valendo tratar reentrega e não responder a evento de conta, que é outro tipo que chega ali.

### Se eu uso agente de IA, muda alguma coisa?

Aumenta a importância, porque o modelo responde a qualquer entrada. O filtro precisa vir **antes** do modelo, e não depender de ele decidir não responder.

### Como testo se estou protegido?

Mande uma mensagem para o seu número pelo fluxo e espere o ciclo completo de status. Se nada além da sua mensagem sair, o filtro está funcionando.

### Isso pode bloquear o número mesmo com poucos contatos?

O volume por si só já é anômalo, e a reação de quem recebe é o que mais pesa. Poucos contatos recebendo dezenas de mensagens produzem bloqueio e denúncia com muita facilidade.

## Como decidir

Não há decisão a tomar aqui: se o seu fluxo responde algo que chega no webhook, ele precisa do filtro. É uma condição no início, e leva cinco minutos.

O que vale escolher é entre as duas formas. **Falhar** em cima do status protege e descarta informação. **Desviar** protege e guarda o status para o seu controle de entrega. A segunda dá um pouco mais de trabalho e é a que você vai querer quando começar a se perguntar quantas mensagens realmente chegaram.

::cta: Confira o seu fluxo agora, antes do próximo disparo | Abra o primeiro passo e veja de onde ele lê o remetente. Se não for de dentro do objeto de mensagem, você está a um envio de distância de descobrir isso do jeito caro.

## Leia também
- [Os três status da mensagem: enviada, entregue e lida](/tres-status-da-mensagem-whatsapp)
- [WhatsApp API oficial no n8n](/whatsapp-api-oficial-n8n)
- [Meu webhook chega duplicado](/webhook-chega-duplicado)
- [Ver o payload cru das mensagens em tempo real](/ver-payload-das-mensagens-em-tempo-real)

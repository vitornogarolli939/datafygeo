---
title: "Mensagem enviada pelo celular é cobrada na API oficial?"
description: "Não. Em coexistência, só é cobrado o que sai pela API. Isso muda a conta de quem tem atendente humano, e quase nenhum comparativo menciona."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "mensagem-enviada-pelo-celular-e-cobrada"
cluster: "custo"
hero: "preco"
intent: "decidindo"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/
  - https://whatsappbusiness.com/pt-br/products/platform-pricing/
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=JL9Qzw3oS5A
  - https://www.youtube.com/watch?v=dIIkttPeBS0
videos: [JL9Qzw3oS5A, dIIkttPeBS0]
internal_links:
  - /quanto-custa-whatsapp-business-api-brasil-2026
  - /coexistencia-whatsapp-api-oficial-app-celular
  - /mensagem-de-servico-vai-ser-paga-outubro-2026
  - /como-passar-do-bot-para-o-atendente-humano
  - /primeira-mensagem-api-oficial-whatsapp
status: aprovado
---

# Mensagem enviada pelo celular é cobrada na API oficial?

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** **não.** Se o número está em coexistência, ou seja, funcionando ao mesmo tempo no aplicativo do celular e na API, a mensagem que o atendente manda **pelo aplicativo** não é cobrada. A cobrança é sobre o que sai **pela API**.

Na formulação do Israel Henrique, CTO da Datafy: *"se você conectar o teu WhatsApp Web ou o teu celular junto com a API e você enviar mensagens pelo celular, você não paga. Só paga se for enviado pela API."*

Isso é uma assimetria real, e ela quase nunca aparece em comparativo de preço. Dependendo do desenho da sua operação, ela muda a conta.

::numeros: 0|custo da mensagem enviada pelo aplicativo ;; 0|custo da mensagem que o cliente te envia ;; 1 out 2026|quando a resposta pela API deixa de ser grátis ;; 2 caminhos|para a mesma conversa, com custos diferentes

## Principais pontos
- **A Meta cobra o que sai pela plataforma**, e mensagem enviada pelo aplicativo não passa por ela.
- **Mensagem recebida nunca é cobrada**, em nenhum caminho.
- Até 1º de outubro de 2026, **responder pela API dentro da janela de 24 horas também é gratuito**. Depois disso, não.
- **Isso não é brecha**, é como a cobrança funciona. E não escala: atendente humano no celular tem limite de gente.
- Para o seu sistema enxergar o que o atendente mandou, é preciso **assinar o evento de mensagem enviada pelo aplicativo**.

::diagrama: preço-comparacao

## Por que funciona assim

Não é uma exceção criada de propósito, é consequência do desenho.

Quando o atendente responde pelo aplicativo, a mensagem sai do aparelho dele pelo WhatsApp, exatamente como sempre foi. A plataforma de negócios não despachou nada, e por isso não há o que faturar.

Quando você responde pela API, a mensagem passa pela infraestrutura da Meta, que a processa e entrega. É esse serviço que é cobrado.

Ou seja: **a mesma conversa, com a mesma pessoa, tem custo diferente dependendo de por onde a resposta sai.** E em coexistência os dois caminhos coexistem no mesmo número.

::video: JL9Qzw3oS5A | Em 00:21 ele estabelece a regra logo no começo do vídeo sobre preço: a Meta cobra por mensagem enviada, não por recebida, e mensagem enviada pelo celular não entra na conta.

## Quando isso importa de verdade

A assimetria só faz diferença em alguns desenhos. Vale ver onde.

**Importa muito:** operação com atendimento humano em volume, em que a maior parte das respostas é digitada por uma pessoa. Se o atendente já responde pelo celular, essas mensagens seguem fora da fatura.

**Importa a partir de outubro de 2026:** hoje, responder pela API dentro da janela de 24 horas é gratuito, então a diferença é zero contra zero. Quando [a mensagem de serviço passar a ser cobrada](/mensagem-de-servico-vai-ser-paga-outubro-2026), a diferença passa a existir de fato.

**Não importa:** operação de disparo. Template é cobrado sempre, e ele não sai do celular, sai da API.

**Não importa:** agente de IA. Por definição, ele responde pela API.

## O que isso não resolve

Vale ser honesto sobre o tamanho disso, porque é fácil transformar em conselho ruim.

**Não escala.** Atendente humano responde algumas dezenas de conversas por dia. Se o seu volume justifica automação, ele já não cabe no celular.

**Não vale para iniciar conversa.** Fora da janela de 24 horas, o caminho é template, e template é cobrado.

**Custa outra coisa.** Coexistência tem teto de vazão menor, 20 mensagens por segundo contra 80 do número comum. Para atendimento sobra; para disparo, pesa.

**Fragmenta o registro, se você não configurar.** É o ponto mais importante, e ele vem a seguir.

## O evento que você precisa assinar

Se o atendente responde pelo celular e o seu sistema não sabe, você fica com **metade da conversa** no banco: o que o cliente mandou e o que a automação respondeu, sem as respostas humanas no meio.

Isso quebra histórico, quebra relatório e atrapalha qualquer coisa que dependa de contexto, inclusive agente de IA lendo a conversa.

A correção é assinar o **evento de mensagem enviada pelo aplicativo**, que é separado do evento de mensagens. Com ele, tudo que sai do celular também chega no seu webhook.

E a confusão que sempre aparece junto: **esse evento não cobre mensagem enviada pela API.** Dessa, o que volta é [status](/tres-status-da-mensagem-whatsapp). São dois caminhos diferentes para duas origens diferentes.

::video: dIIkttPeBS0 | Em 06:40 ele cadastra os dois eventos e explica a diferença entre eles, incluindo por que a mensagem enviada pela API não aparece no segundo.

## Como usar isso no desenho

Sem virar malabarismo, três decisões que fazem sentido por si só e que se beneficiam da assimetria:

**Deixe o humano no aplicativo, se ele já está.** Migrar o atendente para uma interface web não melhora nada por si só, e passa a custar por mensagem depois de outubro. Se a equipe é pequena e o celular funciona, mantenha.

**Reserve a API para o que ela faz melhor:** disparo, notificação, agente, integração com o seu sistema.

**Resolva em menos turnos, do lado da API.** Quando a mensagem passa a ter preço, resposta que já traz a informação completa vale mais que resposta que puxa outra pergunta. Vale para agente e para roteiro de atendimento.

E o que **não** vale fazer: montar um esquema para "empurrar" mensagens pelo celular a fim de economizar. Além de não escalar, automação disparando pelo aplicativo é justamente o padrão que a plataforma associa a ferramenta não autorizada.

## Perguntas frequentes

### Mensagem que o cliente me manda é cobrada?

Nunca. A Meta cobra o que você envia e que é entregue.

### E o WhatsApp Web, conta como celular?

O WhatsApp Web é uma extensão do aplicativo, então a mensagem sai pelo mesmo caminho do aparelho. O que define a cobrança é a mensagem ter passado ou não pela plataforma de negócios.

### Isso vale depois de outubro de 2026?

A cobrança que começa em outubro é sobre a **mensagem de serviço enviada pela API**. Mensagem enviada pelo aplicativo continua fora desse escopo, e é justamente aí que a diferença passa a aparecer.

### Se eu respondo pelo celular, a janela de 24 horas se comporta igual?

Mensagem enviada pelo aplicativo não abre nem estende a janela de atendimento da API. Vale saber antes de montar automação que dependa disso.

### Preciso de coexistência para isso?

Precisa. Se o número nasceu na API, sem aplicativo no celular, não existe esse segundo caminho. [A diferença entre os dois modos está aqui](/coexistencia-whatsapp-api-oficial-app-celular).

### Dá para o atendente responder pelo celular e a IA pela API, no mesmo número?

Dá, e é o uso mais comum da coexistência. O cuidado é assinar o evento de mensagem enviada pelo aplicativo, para o seu sistema não perder o que o humano escreveu.

## Como decidir

Se o seu atendimento é humano e cabe no celular, mantenha assim e assine o evento que traz essas mensagens para o seu banco. Você fica com o registro completo e sem custo por mensagem nessa parte.

Se o volume já exige automação, essa assimetria não vai salvar a sua conta, e o que decide é [a categoria dos templates e o número de turnos por conversa](/quanto-custa-whatsapp-business-api-brasil-2026).

E, em qualquer cenário, faça a conta de outubro agora: quantas mensagens você respondeu pela API dentro da janela no último mês? Esse é o número que aparece na fatura, e ele não existe hoje.

::cta: Confira se o seu sistema enxerga o atendente | Mande uma mensagem pelo celular do número conectado e veja se ela chega no seu webhook. Se não chegar, falta assinar um evento, e o seu histórico está com metade da conversa faltando.

## Leia também
- [Quanto custa a WhatsApp Business API no Brasil](/quanto-custa-whatsapp-business-api-brasil-2026)
- [Coexistência: API e aplicativo no mesmo número](/coexistencia-whatsapp-api-oficial-app-celular)
- [1º de outubro: responder o cliente deixa de ser grátis](/mensagem-de-servico-vai-ser-paga-outubro-2026)
- [Como passar do bot para o atendente humano](/como-passar-do-bot-para-o-atendente-humano)

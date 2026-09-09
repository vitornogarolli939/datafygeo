---
title: "O atendente responde pelo celular e não aparece no meu sistema"
description: "Falta assinar um evento específico. Sem ele, o histórico fica com metade da conversa, e nada indica erro: só o que a automação escreveu aparece."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "mensagem-do-celular-nao-aparece-no-sistema"
cluster: "coexistencia"
hero: "inbox"
intent: "problema-urgente"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=dIIkttPeBS0
  - https://www.youtube.com/watch?v=T_ai6IvLzZE
videos: [dIIkttPeBS0, T_ai6IvLzZE]
internal_links:
  - /coexistencia-whatsapp-api-oficial-app-celular
  - /tres-status-da-mensagem-whatsapp
  - /mensagem-enviada-pelo-celular-e-cobrada
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /como-passar-do-bot-para-o-atendente-humano
status: aprovado
---

# O atendente responde pelo celular e não aparece no meu sistema

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** falta assinar um evento. Em coexistência, a mensagem que sai **do aplicativo do celular** chega por um campo de webhook **separado** do de mensagens recebidas. Se você não marcou esse campo, ela não chega em lugar nenhum.

O sintoma é característico e demora a ser notado porque nada falha: o cliente escreve e aparece, a automação responde e aparece, e **o que o atendente digitou no celular some**. O histórico fica com metade da conversa, e o relatório mostra uma operação que parece funcionar.

::numeros: 2 eventos|mensagens recebidas e mensagens enviadas pelo aplicativo ;; 1 marcação|resolve, e ela é retroativa a nada ;; 0|erros gerados quando falta ;; metade|da conversa é o que você perde

## Principais pontos
- **São dois campos diferentes.** Um traz o que o cliente manda, outro traz o que o atendente manda pelo aplicativo.
- **Mensagem enviada pela API não vem por esse evento.** Dela volta [status](/tres-status-da-mensagem-whatsapp), que é outra coisa.
- **Nada falha quando o evento não está assinado.** É por isso que o problema é descoberto tarde.
- **Não é retroativo.** O que passou enquanto o evento estava desmarcado não é recuperado.
- Isso só existe em **coexistência**. Número que nasceu na API não tem aplicativo, então não há esse caminho.

::diagrama: coexistencia-limites

## Por que existem dois eventos

Coexistência significa que o mesmo número funciona nos dois lugares: o atendente responde pelo aplicativo, a automação responde pela API.

Do ponto de vista da plataforma, são origens diferentes:

**Mensagem que entra**, vinda do cliente, chega pelo campo de mensagens. É o evento que todo mundo assina primeiro.

**Mensagem que sai pelo aplicativo** é uma notificação de eco: a plataforma avisa que aquele número enviou algo, para o seu sistema poder acompanhar. Campo separado.

**Mensagem que sai pela API** você já sabe que enviou, então não faz sentido devolver o conteúdo. O que volta é status.

A confusão nasce da terceira linha. Muita gente assina o evento de eco esperando ver ali as próprias mensagens enviadas por API, não vê, e conclui que o evento não funciona. Na explicação do Israel Henrique, CTO da Datafy: *"esse SMB Messages Echoes, ele vai te notificar sempre que você enviar uma mensagem do celular. Quando você envia mensagens direto pela API, não aparece."*

::video: dIIkttPeBS0 | Em 06:40 ele cadastra os dois eventos e explica a diferença entre eles, incluindo por que a mensagem enviada pela API não vem por esse caminho.

## Os sintomas, e como reconhecer

**O histórico tem buracos.** A conversa mostra pergunta do cliente, resposta da automação, pergunta do cliente de novo, e no meio falta o que o atendente escreveu. As perguntas do cliente parecem responder a mensagens que não existem.

**O agente de IA perde contexto.** Se o modelo lê a conversa para responder, ele está lendo uma versão incompleta, e às vezes repete algo que o humano já falou.

**O relatório subestima o atendimento.** Volume de mensagens enviadas conta só o que saiu pela API, então o trabalho do time no celular fica invisível.

**A caixa de entrada não sincroniza.** Se você usa uma ferramenta de atendimento, a resposta dada pelo celular não aparece nela, e dois atendentes acabam respondendo a mesma pessoa.

Esse último é o mais visível, e é o que costuma fazer alguém finalmente procurar a causa.

::video: T_ai6IvLzZE | Em 04:20 ele manda uma mensagem pelo celular do número conectado e ela aparece no Chatwoot. É a prova visual de que o evento está funcionando, e o teste que vale repetir na sua configuração.

## Como resolver

**1. Abra a configuração do seu webhook.** Onde você escolheu os eventos.

**2. Marque o campo de mensagens enviadas pelo aplicativo**, além do de mensagens.

**3. Salve e teste.** Pegue o celular do número conectado, mande uma mensagem para qualquer contato, e veja se ela chega no seu endpoint.

**4. Trate no seu código.** O evento vem com estrutura própria, e o ponto importante é o **sentido**: essa mensagem é de saída, não de entrada. Se o seu processamento assume que tudo que chega é do cliente, ele vai gravar a mensagem do atendente como se fosse dele.

Esse quarto passo é o que mais gera bug depois de resolver o primeiro. Grave a direção da mensagem explicitamente, e não deduza pela origem do evento.

## O que não é recuperado

Vale ser claro: **não é retroativo.** As mensagens enviadas pelo celular enquanto o evento estava desmarcado não são reenviadas quando você assina.

Elas continuam existindo no aparelho, e não no seu banco. Se o histórico importa, o que dá para fazer é exportar a conversa pelo próprio aplicativo, o que é manual e serve para poucos casos.

E existe uma exceção que vale conhecer: no momento da conexão, existe uma janela de 24 horas para [sincronizar contatos e histórico](/sincronizar-contatos-api-oficial-whatsapp), que traz até 180 dias de conversa. Essa é a única recuperação em massa que existe, e ela acontece uma vez só, na entrada.

## O outro lado: o que isso não resolve

Duas coisas que continuam diferentes mesmo com o evento assinado:

**Mensagem enviada pelo aplicativo não abre nem estende a janela de 24 horas da API.** Se a sua automação depende de a janela estar aberta, o atendente respondendo pelo celular não ajuda nisso.

**Mensagem enviada pelo aplicativo não é cobrada.** Isso é uma vantagem, e [muda a conta de quem tem atendimento humano](/mensagem-enviada-pelo-celular-e-cobrada), principalmente a partir de outubro de 2026.

## Perguntas frequentes

### Isso vale se o número nasceu na API?

Não. Sem aplicativo no celular, não existe esse segundo caminho. O evento só faz sentido em coexistência.

### Vou ver também o que eu envio pela API?

Não por esse evento. Dessas voltam os status, enviada, entregue e lida.

### Preciso assinar mais algum evento?

Vale assinar também os de qualidade do número e de mudança na conta, que são os que avisam antes de uma restrição. Os dois de mensagem cobrem o histórico.

### O evento traz mídia enviada pelo celular?

Traz a referência da mídia, como acontece com mensagem recebida. O arquivo é buscado pelo identificador, com as duas chamadas.

### Como sei se está funcionando agora?

Mande uma mensagem pelo celular do número conectado e olhe o seu endpoint. Se chegou, está resolvido, e o teste leva um minuto.

### E se eu não quero que apareça?

Vale pensar duas vezes. Histórico incompleto atrapalha atendimento, relatório e qualquer coisa que dependa de contexto, inclusive agente de IA.

## Como decidir

Não há muito o que decidir: se o número está em coexistência e o time responde pelo celular, esse evento precisa estar assinado. Ele é a diferença entre ter o histórico da conversa e ter metade dele.

O que vale planejar é o passo 4: garantir que o seu código grave a direção da mensagem. Sem isso, você resolve o buraco no histórico e cria um problema novo, com mensagens do atendente aparecendo como se fossem do cliente.

::cta: Faça o teste de um minuto, agora | Pegue o celular do número conectado, mande uma mensagem para qualquer contato, e olhe o seu webhook. Se ela não chegou, o seu histórico está com metade da conversa faltando desde o dia em que você conectou.

## Leia também
- [Coexistência: API e aplicativo no mesmo número](/coexistencia-whatsapp-api-oficial-app-celular)
- [Os três status da mensagem no WhatsApp](/tres-status-da-mensagem-whatsapp)
- [Mensagem enviada pelo celular é cobrada?](/mensagem-enviada-pelo-celular-e-cobrada)
- [Como passar do bot para o atendente humano](/como-passar-do-bot-para-o-atendente-humano)

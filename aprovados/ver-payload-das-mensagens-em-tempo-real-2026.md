---
title: "Como ver o payload cru das mensagens do WhatsApp em tempo real"
description: "Depurar integração sem log de servidor: o que entra, o que sai, e os três eventos de status de cada envio. Com os limites de retenção que isso tem."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "ver-payload-das-mensagens-em-tempo-real"
cluster: "implementacao"
hero: "webhook"
intent: "problema-urgente"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/create-webhook-endpoint/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/business-phone-numbers/media
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=LIT4FxgqHhE
  - https://www.youtube.com/watch?v=vGovcR8W5g8
videos: [LIT4FxgqHhE, vGovcR8W5g8]
internal_links:
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /a-mensagem-falhou-e-nao-sei-por-que
  - /webhook-chega-duplicado
  - /quanto-tempo-o-whatsapp-guarda-minhas-mensagens
  - /qual-url-eu-uso-no-webhook-da-meta
status: aprovado
---

# Como ver o payload cru das mensagens do WhatsApp em tempo real

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** quando a integração não funciona, existe uma pergunta que resolve metade dos casos e que quase ninguém consegue responder rápido: **o que exatamente chegou?**

Ver o payload cru, campo por campo, no momento em que ele passa, separa três problemas que se confundem: o evento não está chegando, o evento chega e o seu código lê o campo errado, ou o evento chega e é de um tipo que você não esperava. Sem isso, o time passa horas depurando o problema errado.

::numeros: 3 problemas|que o payload cru separa em segundos ;; 3 status|voltam para cada mensagem que você envia ;; 7 dias|de retenção do log, no painel da Datafy ;; 100|mensagens por conversa, o teto do log

## Principais pontos
- **A pergunta é sempre a mesma:** chegou? Se chegou, com quais campos? O payload cru responde as duas de uma vez.
- **Mensagem enviada pela API não volta como mensagem.** Dela voltam **status**, e confundir isso é a causa de metade dos diagnósticos errados.
- **Cada envio gera três eventos**, enviada, entregue e lida. Falha gera um só, com o motivo.
- **Log de plataforma não é arquivo.** No painel da Datafy, ele guarda 7 dias e no máximo 100 mensagens por conversa, e mídia não aparece.
- Para o que precisa durar, o único lugar confiável é **o seu banco**, gravando o payload cru antes de interpretar.

::diagrama: webhook-fluxo

## Os três problemas que se parecem

Antes de qualquer ferramenta, vale nomear o que você está tentando distinguir, porque os três produzem o mesmo sintoma de "não funciona":

**O evento não chega.** A URL está errada, o campo não foi assinado, ou o seu endpoint não responde. Aqui o payload cru é vazio, e isso já é a resposta.

**O evento chega e o seu código lê errado.** É o mais comum, e o mais frustrante. O telefone está em `contacts`, você está lendo do topo. A legenda está fora do objeto da mídia, você está lendo dentro. O payload cru mostra a estrutura real e o erro fica óbvio.

**O evento chega e é de um tipo que você não esperava.** Um status, um evento de conta, um tipo de mensagem novo. O seu código estoura ou ignora em silêncio, e o payload cru mostra o que era.

## O que você deveria conseguir ver

Um bom diagnóstico responde quatro coisas:

**A mensagem que entrou**, com os campos separados: quem enviou, o identificador dela, o horário, o tipo e o conteúdo.

**A mensagem que saiu**, e por qual caminho: pela API ou pelo celular, em coexistência. São eventos diferentes.

**Os status**, um por um, com o identificador da mensagem que eles referenciam.

**O motivo da falha**, quando houver, que é o campo que mais some no caminho porque muita biblioteca descarta.

::video: LIT4FxgqHhE | Três minutos com o log ao vivo funcionando. Em 00:52 ele clica numa mensagem recebida e abre o payload exato que foi entregue, em 01:26 responde e mostra o evento de mensagem enviada pelo celular, e em 01:59 envia pela API e aparecem os três status em sequência.

## A confusão que esse log resolve na primeira olhada

Existe um mal-entendido tão comum que vale isolar, e ele fica evidente assim que você vê os eventos lado a lado.

**Você manda mensagem pela API. Ela não volta como mensagem.** O que volta é status: enviada, depois entregue, depois lida. O conteúdo não vem junto, só o identificador e a situação.

**O atendente responde pelo celular. Isso sim volta como um evento próprio**, o de mensagem enviada pelo aplicativo, e só se você tiver assinado esse campo. Sem ele, metade da conversa não existe no seu sistema.

Quem espera ver o próprio envio pela API no evento de mensagens fica procurando defeito onde não tem. São dois caminhos diferentes para duas origens diferentes.

## O outro uso: descobrir o laço antes que ele aconteça

Ver os três status chegando tem um segundo valor, e ele é sobre segurança.

Como esses eventos chegam no **mesmo webhook** das mensagens de cliente, um fluxo que responde tudo que entra vira um multiplicador: cada resposta sua gera três status, cada status vira outra resposta. Três, nove, vinte e sete.

::video: vGovcR8W5g8 | Em 14:47 o aviso aparece antes da execução, e em 19:05 os três status chegam e a proteção funciona. O alerta dele é direto: um fluxo assim bloqueia o número.

A proteção é filtrar na entrada: leia o remetente **de dentro do objeto de mensagem**, que não existe no evento de status. Assim o passo falha ao receber status, em vez de responder. [O tratamento completo está aqui](/webhook-chega-duplicado).

## Os limites, ditos com clareza

Painel de log é ferramenta de diagnóstico, e não repositório. Vale saber onde ele acaba antes de construir algo em cima.

No painel da Datafy, ele guarda **7 dias** e no máximo **100 mensagens por conversa**, descartando as mais antigas quando passa disso. **Mídia não aparece**, só o aviso de que chegou. E o próprio Israel Henrique, CTO da Datafy, delimita o uso: *"isso aqui é apenas para log, não é para ser utilizado como bate-papo ou atendimento."*

Isso significa três coisas na prática:

**Não use como destino de transferência para humano.** Você perde mídia e perde histórico depois de uma semana. O destino precisa ser uma caixa de entrada de verdade, [com fila e atribuição](/como-passar-do-bot-para-o-atendente-humano).

**Não use como registro de atendimento.** Para conformidade, o que vale é [o que você guardou no seu banco](/o-cliente-pediu-para-apagar-os-dados-dele).

**Use para o que ele é bom:** olhar o payload de uma mensagem específica quando algo deu errado, sem precisar acessar o log do servidor nem esperar deploy.

## O que fazer no seu lado, para não depender disso

O log da plataforma resolve o problema de hoje. O que resolve o de daqui a três meses é um hábito:

**Grave o payload cru antes de interpretar.** É a rede de segurança de tudo. Quando um campo novo aparecer e você precisar dele, só quem guardou o bruto consegue reprocessar. Sem ele, o dado daquele período não existe.

**Guarde o identificador de cada mensagem enviada.** É a chave que casa com o status que chega depois. Sem ela, chega o evento e você não sabe a que se refere.

**Guarde o motivo da falha.** Ele vem junto do status e é o que distingue número inexistente de bloqueio por limite. [Muita biblioteca descarta esse campo](/a-mensagem-falhou-e-nao-sei-por-que).

**Registre tipos desconhecidos em vez de estourar.** Um caso final que anota e segue transforma uma quebra em uma linha de log.

## E enquanto você desenvolve, na sua máquina

Antes de existir tráfego real, duas coisas ajudam:

**Disparar um evento de teste** do tipo que você quer, para a sua URL. Separa "meu endpoint está errado" de "o evento não está chegando" sem depender de alguém mandar mensagem.

**Um túnel para a sua porta local**, que dá um endereço público temporário. Três coisas mordem aqui: o framework pode recusar o domínio do túnel com um erro de proibido, o endereço muda a cada vez que ele sobe, e trocar para a URL de produção quando publicar é um passo manual fácil de esquecer. [Os detalhes estão aqui](/qual-url-eu-uso-no-webhook-da-meta).

## Perguntas frequentes

### Por que minha mensagem enviada pela API não aparece como mensagem?

Porque ela volta como status, não como mensagem. É o comportamento esperado, e não indica problema.

### Recebo três eventos por envio. Está duplicando?

Não. São enviada, entregue e lida. O terceiro só vem se a pessoa tiver confirmação de leitura habilitada.

### O log mostra a imagem que o cliente mandou?

Não mostra a mídia, só indica que chegou. Para o arquivo, é preciso [fazer as duas chamadas de mídia](/como-receber-midia-api-oficial-whatsapp), e o identificador expira em 7 dias.

### Posso usar esse log como histórico de atendimento?

Não. São 7 dias e 100 mensagens por conversa. Histórico é responsabilidade do seu banco.

### Como vejo o que aconteceu com uma mensagem específica?

Pelo identificador que a chamada de envio devolveu. Ele é a chave que liga o envio aos status que chegaram depois, e por isso vale guardá-lo sempre.

### Meu webhook não recebe nada. O log ajuda?

Ajuda, e por eliminação: se o log da plataforma mostra a mensagem chegando e o seu endpoint não recebe, o problema está entre os dois, na URL ou na sua aplicação, e não na Meta.

## Como decidir

Se você está montando a integração agora, use o log da plataforma sem culpa: ele encurta o primeiro dia de trabalho, que é justamente quando você ainda não tem observabilidade nenhuma.

Assim que a coisa for para produção, monte o seu: guarde o payload cru, o identificador e o motivo da falha. O log da plataforma continua útil para o caso pontual, e ele nunca vai ser o lugar onde o seu histórico mora.

::cta: Olhe um payload cru hoje, antes de precisar | Mande uma mensagem para o seu número conectado e abra o evento inteiro, campo por campo. Você descobre em cinco minutos onde estão o telefone, o identificador da pessoa e a legenda, e para de adivinhar caminho de campo no meio de um incidente.

## Leia também
- [Webhook: receber mensagens em tempo real](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [A mensagem falhou e eu não sei por quê](/a-mensagem-falhou-e-nao-sei-por-que)
- [Meu webhook chega duplicado](/webhook-chega-duplicado)
- [Qual URL eu uso no webhook da Meta](/qual-url-eu-uso-no-webhook-da-meta)

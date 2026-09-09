---
title: "Como leio o histórico de conversa pela API do WhatsApp?"
description: "Não existe endpoint para isso. A Cloud API entrega mensagem por webhook e não devolve conversa antiga. Se você não guardar, não tem."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "como-leio-o-historico-de-conversa-pela-api"
cluster: "implementacao"
hero: "webhook"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/data-privacy-and-security/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=dIIkttPeBS0
  - https://www.youtube.com/watch?v=HQm5UuW50bM
videos: [HQm5UuW50bM, dIIkttPeBS0]
internal_links:
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /coexistencia-whatsapp-api-oficial-app-celular
  - /migrar-para-api-oficial-sem-perder-o-numero
  - /api-oficial-vs-nao-oficial-whatsapp-2026
  - /whatsapp-api-oficial-chatwoot
status: aprovado
---

# Como leio o histórico de conversa pela API do WhatsApp?

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** não dá. **Não existe um `GET /messages` na Cloud API.** A Meta entrega cada mensagem uma vez, por webhook, no momento em que ela acontece. Não há endpoint para listar conversa, buscar mensagem por identificador ou puxar o que passou.

Isso surpreende quase todo mundo, e é uma das perguntas mais repetidas da comunidade técnica: doze discussões públicas, cerca de 24 mil visualizações, e cinco delas sem nenhuma resposta. A conclusão prática é dura e simples: **se você não guardar, não tem.**

::numeros: 0|endpoints para ler histórico na Cloud API ;; 1 vez|é quantas vezes cada mensagem é entregue a você ;; 30 dias|é quanto a Meta guarda, para operar o serviço, não para você consultar ;; 180 dias|o único histórico que entra, e só uma vez, na coexistência

## Principais pontos
- A Cloud API é **orientada a evento**, não a consulta. O webhook é a única porta de entrada da mensagem, e ela passa uma vez.
- A Meta guarda mensagem por até **30 dias**, mas isso é para operar o serviço, como reentrega. **Não é um arquivo que você possa consultar.**
- **Guardar é responsabilidade sua desde a primeira mensagem.** Quem descobre isso no terceiro mês perdeu o terceiro mês.
- Existe **uma** exceção, e ela não se repete: no onboarding com coexistência, a Meta sincroniza até 180 dias de conversa, uma vez só, sem grupos.
- Se o seu webhook ficou fora do ar, aquelas mensagens **não são recuperáveis** por consulta. A reentrega da Meta tenta por até 7 dias, e é só isso que existe.

::diagrama: webhook-fluxo

## Por que não existe

A Cloud API foi desenhada como canal de troca, não como banco de dados de conversa. A Meta guarda o mínimo para entregar a mensagem e reentregar quando falha, e apaga.

A [documentação de privacidade e segurança](https://developers.facebook.com/documentation/business-messaging/whatsapp/data-privacy-and-security/) diz isso de forma direta: a retenção existe para prover as funcionalidades do serviço, com exemplo de retransmissão. Não há promessa de arquivo consultável, e não há endpoint que exponha um.

Do ponto de vista de proteção de dados, isso até ajuda: a plataforma guarda pouco, e quem decide quanto tempo o dado vive é quem opera o negócio. Do ponto de vista de quem está construindo, significa uma responsabilidade que precisa estar no primeiro sprint, não no roadmap.

## O que fazer, então

**Grave tudo que chega, na hora que chega.** Antes de processar, antes de decidir, antes de responder. O primeiro passo do seu handler de webhook deve ser persistir o payload cru. Processar vem depois.

**Grave também o que você envia.** A API devolve um identificador de mensagem no envio, o `wamid`. Guarde ele junto com o conteúdo enviado: é o que permite casar depois com os eventos de entrega, leitura e falha, que chegam pelo mesmo webhook.

**Guarde o payload bruto, não só os campos que você usa hoje.** Um dia você vai precisar de um campo que ignorou. Reprocessar do bruto é possível; reconstituir o que não foi salvo, não.

**Trate o webhook como entrega única.** Responda 200 rápido, coloque em fila, processe depois. Se o processamento pesado acontece antes da resposta, a Meta trata como falha e reentrega, e você ganha mensagem duplicada, que é outro problema comum.

**Monitore ausência.** Se o seu volume normal é de dezenas de mensagens por hora e ele vai a zero, o mais provável é que o seu endpoint caiu, e não que os clientes sumiram. Silêncio precisa acordar alguém, porque cada hora fora do ar é uma hora de histórico que não volta.

## A única exceção, e o prazo dela

Ao conectar um número pelo fluxo de **coexistência**, a Meta sincroniza o histórico do aplicativo. Isso é o mais próximo de "importar o passado" que existe, e vem com limites:

| O que | Limite |
|---|---|
| Conversas | Os últimos **180 dias** |
| Conversas de grupo | **Não vêm** |
| Arquivos de mídia | Identificadores só dos últimos **14 dias** |
| Prazo para disparar | **24 horas** depois de conectar |
| Quantas vezes | **Uma só**, no onboarding |

O prazo de 24 horas é o que mais pega gente desprevenida. Conectou o número e deixou para sincronizar depois? Perdeu a janela, e refazer exige desconectar e passar por todo o onboarding de novo.

## Os três passos da exceção, na ordem

Como o prazo é curto e o processo não é automático, vale a sequência exata. Errar a ordem custa a janela inteira.

**1. No celular, durante a conexão, aceitar compartilhar as conversas.** É uma pergunta que aparece no aplicativo, no meio do fluxo. Quem não marca não recupera nada, e não existe segunda chance sem desconectar e reconectar o número.

**2. Assinar o evento de sincronização no webhook, antes de pedir.** É por ele que os dados chegam. Sem ele, a chamada do passo 3 responde sucesso e nada aparece, o que é a forma mais frustrante de perder o prazo.

**3. Fazer a chamada que dispara a sincronização.** Esse passo é o que quase ninguém sabe que existe. Na frase do Israel: *"você conectou o telefone, com webhook, tá marcado, agora tem que avisar a meta que você quer os contatos."* Contatos e histórico se pedem separadamente.

E o comportamento da resposta é diferente para cada um, o que evita meia hora de depuração inútil:

| O que você pede | Quando chega |
|---|---|
| Contatos da agenda | Praticamente na hora |
| Histórico de conversas | **Bem mais devagar**, e pode levar bastante |

::video: HQm5UuW50bM | Quatro minutos e o único material em português que mostra isso funcionando: em 00:30 o evento sendo marcado, em 01:05 o prazo de 24 horas, em 02:38 a chamada e os contatos chegando no webhook, e em 03:40 a diferença de tempo do histórico.

Uma dica que sai daí: **guarde o identificador que a chamada devolve.** Se a sincronização não vier, é com ele que se abre suporte com a Meta.

## Perguntas frequentes

### E se eu perder uma mensagem porque meu servidor caiu?

A Meta reentrega com frequência decrescente por até 7 dias. Se o seu endpoint voltar dentro desse período, as mensagens chegam. Passou disso, não há como recuperar: não existe consulta.

### Dá para buscar uma mensagem específica pelo identificador?

Não. O `wamid` serve para casar eventos de status com o envio que você fez, e para responder citando uma mensagem. Não é chave de consulta a um arquivo.

### E as mensagens que meus atendentes mandam pelo celular?

Com coexistência, elas chegam ao seu servidor pelo campo `smb_message_echoes`. Sem coexistência, elas não passam pela API e você não fica sabendo.

### A Meta guarda 30 dias. Não dá para pedir?

Não por API. Essa retenção existe para o funcionamento do serviço, não como arquivo consultável.

### Como fica o pedido de exclusão de um cliente, então?

Como o histórico é seu, o trabalho de apagar também é. E ele é maior do que parece, porque o dado costuma estar em mais lugares que o banco principal: fila, log de monitoramento, índice de busca e backup.

### Meu fornecedor guarda para mim?

Alguns guardam por um período, outros não guardam nada. Vale perguntar quanto tempo e como exportar. E vale não terceirizar isso: se o histórico importa para o seu produto, ele precisa estar na sua base.

## Como decidir

Se você está começando agora, resolva isso antes de qualquer coisa: grave o payload cru desde a primeira mensagem, mesmo que ainda não saiba o que vai fazer com ele. É barato agora e impossível depois.

Se você já está rodando e não guardava, comece hoje. O passado até 30 dias está com a Meta e não é consultável, então não há o que recuperar. O que dá para fazer é parar de perder daqui para frente.

::cta: Confira uma coisa hoje: você grava antes de processar? | Se o seu handler de webhook processa e só depois salva, uma falha no meio come a mensagem em silêncio. Persistir o payload cru como primeiro passo custa pouco e é irreversível se ficar para depois.

## Leia também
- [Webhook: receber mensagens em tempo real](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [Coexistência: API e aplicativo no mesmo número](/coexistencia-whatsapp-api-oficial-app-celular)
- [WhatsApp API oficial no Chatwoot](/whatsapp-api-oficial-chatwoot)
- [Migrar para API oficial sem perder o número](/migrar-para-api-oficial-sem-perder-o-numero)

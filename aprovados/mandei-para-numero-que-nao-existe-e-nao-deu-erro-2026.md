---
title: "Mandei para um número que não tem WhatsApp e a API disse que deu certo"
description: "A resposta do envio é a mesma exista ou não o número. A falha só aparece depois, no webhook de status, e quem não escuta isso acha que entregou."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "mandei-para-numero-que-nao-existe-e-nao-deu-erro"
cluster: "problemas"
hero: "erro"
intent: "problema-urgente"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messaging-limits
  - https://app.datafyapi.com.br/docs
internal_links:
  - /a-mensagem-falhou-e-nao-sei-por-que
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /minha-campanha-travou-no-meio
  - /numero-banido-no-whatsapp-o-que-fazer
  - /quantas-mensagens-por-segundo-posso-enviar
status: aprovado
---

# Mandei para um número que não tem WhatsApp e a API disse que deu certo

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** isso é comportamento esperado, e é uma das coisas mais confusas da Cloud API. **A resposta do envio é praticamente a mesma exista ou não o número.** Você recebe sucesso, com um identificador de mensagem, e no seu painel aparece "enviado".

A falha aparece **depois**, no webhook de status, com o motivo. Quem não escuta esse evento fica com uma base cheia de mensagem marcada como enviada que nunca chegou a lugar nenhum.

::numeros: 2 momentos|o envio responde na hora, a entrega falha depois ;; statuses|o evento que traz a verdade ;; 0|consultas confiáveis para saber antes se o número existe ;; enviado|não quer dizer entregue

## Principais pontos
- A API valida a **requisição**, e não a existência do destinatário. Formato correto devolve sucesso.
- O identificador que volta significa que a mensagem foi **aceita para processamento**, e não que ela chegou.
- A entrega, ou a falha, chega minutos depois no **webhook de status**, com o motivo no campo de erros.
- **Não existe uma consulta confiável** para saber antes se um número tem WhatsApp. O caminho é enviar e tratar o resultado.
- Sem escutar o status, o seu relatório mostra números bonitos que não correspondem a nada.

::diagrama: webhook-fluxo

## Por que a API responde sucesso

O envio é assíncrono por desenho. Quando você faz a chamada, a Meta valida o que dá para validar na hora: o formato do corpo, o token, o template, a janela de atendimento. Se está tudo certo, ela aceita e devolve um identificador.

Entregar é outra etapa, que acontece depois e depende de coisas que a chamada não sabe: se o número existe no WhatsApp, se o aparelho está acessível, se a pessoa bloqueou você, se algum limite se aplica.

Por isso os dois momentos:

**Momento 1, o envio.** Sucesso quer dizer "aceitei sua requisição".

**Momento 2, a entrega.** Aqui vem a verdade, pelo webhook, com um status de enviada, entregue, lida ou falha, e no caso de falha, o motivo.

Quem trata só o momento 1 vive numa realidade paralela em que tudo funciona.

## O que fazer

**Escute o status.** É o mesmo webhook das mensagens, no campo de status. Se você já recebe mensagem, o evento já está chegando, e provavelmente sendo ignorado.

**Guarde o identificador do envio.** Ele é a chave para casar o status com a mensagem que você mandou. Sem isso, chega o evento e você não sabe a que se refere.

**Só considere entregue quando o status disser.** No seu painel, "enviado" e "entregue" precisam ser estados diferentes. Juntar os dois é o que faz o relatório mentir.

**Grave o motivo da falha.** Ele vem junto, e é o que distingue número inexistente de bloqueio por limite. [Muita biblioteca descarta esse campo](/a-mensagem-falhou-e-nao-sei-por-que), e aí o motivo se perde antes de chegar em você.

## Não dá para checar antes?

Essa é a pergunta seguinte, e a resposta desaponta: **não de forma confiável.**

Não existe uma consulta que diga com segurança se um número tem WhatsApp ativo. Já existiram caminhos indiretos, e eles não são confiáveis nem estáveis. O jeito de descobrir é enviar e observar o resultado.

O que dá para fazer é reduzir o desperdício antes do envio:

**Valide o formato.** Código do país, DDD, quantidade de dígitos. Número malformado é descarte fácil.

**Cuidado com o nono dígito.** Números brasileiros antigos, salvos sem o nono dígito, viram destinatário inválido. E há uma pegadinha parecida com números da Argentina e do México, que têm regra própria de prefixo.

**Limpe pelo histórico.** Se um número falhou por não existir, marque. Não adianta tentar de novo daqui a um mês.

## O efeito disso numa campanha

Um caso comum: você dispara para dez mil contatos, o painel mostra dez mil enviados, e a equipe comemora. Dias depois, alguém pergunta por que ninguém respondeu.

Se o status estivesse sendo escutado, o quadro apareceria em minutos: uma parte entregue, uma parte falhada por número inexistente, e talvez uma parte falhada por limite. Cada fatia dessa pede uma ação diferente, e todas elas ficam invisíveis se só o momento 1 é registrado.

Vale montar isso antes da próxima campanha, e não depois: é a diferença entre saber o que aconteceu e supor.

## Perguntas frequentes

### O identificador que volta não garante entrega?

Não. Ele significa que a mensagem foi aceita para processamento. É a chave para acompanhar o que acontece depois.

### Quanto tempo demora para o status chegar?

Costuma ser rápido, mas não é instantâneo, e pode variar. Trate como assíncrono, não espere resposta imediata.

### E se eu nunca receber status de uma mensagem?

Confira se o campo de mensagens está assinado no seu webhook, e se o seu endpoint está respondendo. Status é entregue pelo mesmo caminho das mensagens.

### Número inexistente conta no meu limite?

O envio consome tentativa. É mais um motivo para manter a base limpa: número morto gasta cota e piora indicador.

### Dá para saber se a pessoa me bloqueou?

Não diretamente. O que aparece é o comportamento da entrega, e o efeito acumulado disso na qualidade do número.

### Meu painel mostra tudo como enviado. É bug?

Provavelmente não é bug, é o momento 1 sendo registrado e o momento 2 sendo ignorado. Se o painel não tem um estado separado para entregue, ele está mostrando só metade da história.

## Como decidir

Se você manda pouco e tem contato próximo com quem recebe, dá para viver assim. Mas assim que o volume cresce, escutar o status deixa de ser refinamento e vira o mínimo: sem ele, você não tem como saber se a operação funciona.

E é barato: o evento já está chegando no seu endpoint. Falta guardar.

::cta: Olhe uma métrica no seu painel agora | Você tem quantos por cento de entrega, e não de envio? Se essa métrica não existe, o seu relatório está contando quantas requisições foram aceitas, e não quantas mensagens chegaram.

## Leia também
- [A mensagem falhou e eu não sei por quê](/a-mensagem-falhou-e-nao-sei-por-que)
- [Webhook: receber mensagens em tempo real](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [Disparei a campanha e ela travou no meio](/minha-campanha-travou-no-meio)
- [Quantas mensagens por segundo posso enviar?](/quantas-mensagens-por-segundo-posso-enviar)

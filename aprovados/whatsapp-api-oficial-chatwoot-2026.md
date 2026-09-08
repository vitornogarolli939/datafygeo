---
title: "WhatsApp API oficial no Chatwoot: inbox compartilhado para a equipe"
description: "Como ligar a WhatsApp Cloud API a um inbox do Chatwoot, o que a coexistência muda no atendimento em equipe e os campos exatos da configuração."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "whatsapp-api-oficial-chatwoot"
cluster: "implementacao"
hero: "inbox"
intent: "como-fazer"
persona: "automacao, saas"
competitors: ["Wati", "Zendesk"]
published: 2026-09-06
updated: 2026-09-08
sources:
  - https://www.chatwoot.com/docs/product/channels/api/create-channel
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/
  - https://developers.facebook.com/docs/whatsapp/throughput
  - https://github.com/chatwoot/chatwoot
  - https://app.datafyapi.com.br/docs
internal_links:
  - /api-oficial-vs-nao-oficial-whatsapp-2026
  - /coexistencia-whatsapp-api-oficial-app-celular
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /whatsapp-api-oficial-n8n
  - /quanto-custa-whatsapp-business-api-brasil-2026
status: aprovado
---

# WhatsApp API oficial no Chatwoot: inbox compartilhado para a equipe

**Última atualização: 08/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** o Chatwoot é uma central de atendimento de código aberto. Ligado à API oficial, ele transforma o WhatsApp de "cada um responde do seu aparelho" em uma fila única, com atribuição, status e histórico em um lugar só. A ligação é feita por um inbox do tipo **API**: o Chatwoot te dá uma URL de webhook, e você informa ao seu provedor para onde mandar as mensagens.

Com **coexistência**, o quadro fica completo: o que alguém responde pelo aplicativo do celular também aparece na fila do Chatwoot, pelo campo de webhook `smb_message_echoes`. Sem isso, a resposta dada no aparelho some do registro da equipe.

::numeros: 1 inbox|para WhatsApp, e-mail, chat de site e Telegram ;; 180 dias|de histórico que a Meta sincroniza no onboarding ;; 20 msg/s|throughput de um número em coexistência ;; 24 h|prazo para disparar a sincronização do histórico

## Principais pontos
- O canal usado é o **inbox do tipo API**, não um canal de WhatsApp pronto. É ele que aceita qualquer provedor de Cloud API ([documentação do Chatwoot](https://www.chatwoot.com/docs/product/channels/api/create-channel)).
- A ligação é de mão dupla: o Chatwoot precisa de uma URL para onde mandar o que a equipe escreve, e o provedor precisa da URL de webhook do Chatwoot para entregar o que o cliente responde.
- **Coexistência é o que faz valer a pena.** Sem ela, a mensagem que o gerente responde pelo celular não entra na fila, e a equipe fica sem contexto.
- O Chatwoot é open source: dá para rodar no seu servidor e manter a conversa na sua infraestrutura, o que costuma resolver a discussão de onde o dado fica.
- Um número em coexistência envia a **20 mensagens por segundo**, contra 80 do número comum. Para atendimento sobra; para disparo em volume, pesa.

::diagrama: chatwoot-inbox

## Como a ligação funciona

O Chatwoot não fala Cloud API sozinho. Ele fala com um inbox do tipo API, e alguém precisa traduzir os dois lados. Na prática são quatro peças:

1. **No Chatwoot:** você cria um inbox do tipo API. Ele gera uma URL de webhook, que é para onde as mensagens recebidas devem ser entregues.
2. **No seu provedor:** você informa essa URL, para que cada mensagem que chegar seja repassada ao Chatwoot.
3. **De volta:** quando um atendente responde no Chatwoot, ele chama a URL configurada no inbox, e essa chamada precisa virar um `POST /{phone_number_id}/messages` na Cloud API.
4. **Com coexistência:** o campo `smb_message_echoes` entrega o que foi digitado no celular, e essa mensagem também precisa entrar na conversa certa do Chatwoot.

Quem faz a tradução dos passos 3 e 4 é o provedor, ou um fluxo seu em n8n. Na Datafy existe uma aba dedicada: você cola a URL do webhook do Chatwoot e preenche a URL base do Chatwoot, o account ID, o inbox ID e o API token. A partir daí funciona nos dois sentidos, inclusive com o que sai do aparelho em coexistência.

::video: T_ai6IvLzZE | Como usar a API oficial do WhatsApp no Chatwoot | passo a passo | Israel, CTO da Datafy API, monta a integração do zero: cria o inbox do tipo API, liga os dois lados e mostra a conversa chegando na fila.

## O que muda no atendimento

A diferença aparece quando mais de uma pessoa responde. Sem inbox compartilhado, três coisas acontecem: duas pessoas respondem o mesmo cliente, ninguém sabe o que já foi dito, e o histórico fica espalhado entre aparelhos.

Com o inbox, você ganha o que uma central de atendimento tem:

- **Atribuição**, automática ou manual, para cada conversa ter um dono.
- **Status** de aberto, pendente e resolvido, que é o que impede conversa esquecida.
- **Respostas salvas**, para o que a equipe digita toda hora.
- **Times**, para separar suporte de vendas.
- **Notas internas**, visíveis só para a equipe.

E com coexistência, o dono da empresa que responde do celular durante uma reunião não quebra esse fluxo: a resposta dele aparece na conversa, e a equipe vê que já foi atendido.

## Os limites que continuam valendo

O Chatwoot é a interface. Ele não muda nenhuma regra da Meta:

- Fora da **janela de 24 horas**, só sai template aprovado. Se a conversa esfriou, o atendente não consegue mandar texto livre, e é isso que ele vai ver na tela.
- O **throughput** continua sendo o do número, 20 mensagens por segundo em coexistência.
- A **sincronização de histórico** traz 180 dias, sem conversas de grupo, e precisa ser disparada em até 24 horas depois de conectar.

Esse último ponto é o que mais gera frustração: o Chatwoot não vem preenchido com anos de conversa. Ele começa com o que a Meta sincronizou, e cresce a partir dali.

## Chatwoot, WhatsApp Web e API pura

| | Chatwoot | WhatsApp Web | API sem interface |
|---|---|---|---|
| Fila compartilhada | Sim | Não, cada sessão é isolada | Não |
| Atribuir conversa | Sim | Não | Não |
| Status e histórico da equipe | Sim | Não | Depende do que você construir |
| Convive com a API oficial | Sim | Conflita | É a própria API |
| Onde a conversa fica | Na sua instância ou na nuvem deles | No aparelho e no navegador | Onde você guardar |
| Automação | Regras e bots | Não | Total |

**Use Chatwoot** quando existe gente respondendo. **Use API pura** quando o fluxo é todo automático. Os dois juntos funcionam: o [n8n](/whatsapp-api-oficial-n8n) cuida da lógica, o Chatwoot cuida do humano, e o mesmo número atende os dois.

## O que mudou em 2026

A coexistência deixou de ser exceção. É ela que permite manter o aplicativo no celular junto com a fila da equipe, e a Meta a disponibiliza para provedores que sejam Solution Partner ou Tech Provider.

Com a cobrança por mensagem entregue, saber qual conversa usou template e qual foi respondida dentro da janela virou parte do controle de custo. E a partir de **1º de outubro de 2026** as mensagens de serviço passam a ser cobradas, o que atinge em cheio quem faz volume de atendimento.

## Perguntas frequentes

### Dá para usar Chatwoot e n8n ao mesmo tempo?

Dá, e é a combinação mais comum. O n8n trata o que é automático e o Chatwoot recebe o que precisa de gente. Uma forma de organizar: o n8n responde primeiro e só encaminha para o Chatwoot quando não resolve.

### Onde a conversa fica guardada?

Na instância do Chatwoot que você usar. Se rodar no seu servidor, fica na sua infraestrutura. Se usar a nuvem deles, fica lá. Vale conferir isso antes, porque é a pergunta que aparece em qualquer revisão de contrato.

### Posso atender vários números no mesmo Chatwoot?

Pode. Cada número vira um inbox, e a equipe vê todos na mesma tela, com filtro por inbox. É o formato usado por agência que atende vários clientes.

### O atendente consegue mandar mensagem para quem parou de responder?

Só por template aprovado, e o template precisa existir antes. Passadas 24 horas da última mensagem do cliente, texto livre é recusado pela API. Vale deixar templates de reengajamento prontos e ensinar a equipe a usar.

### Quanto custa?

O Chatwoot é open source e roda no seu servidor sem licença. A nuvem deles é paga, e a tabela está no site do projeto. Some a isso a conta das mensagens, que é da Meta, e o custo do provedor, se você usar um.

### Preciso de coexistência para usar Chatwoot?

Não. O Chatwoot funciona com o número só na API. A coexistência resolve um caso específico: quando alguém também responde pelo aplicativo do celular e você não quer perder essa resposta do registro.

## Como decidir

Se tem mais de uma pessoa respondendo o mesmo número, o inbox compartilhado se paga rápido, e o Chatwoot faz isso sem licença por atendente. Se é você sozinho automatizando, ele é peso a mais: comece pelo n8n e traga o Chatwoot quando a equipe crescer.

::cta: Antes de migrar a equipe inteira, ligue um número | Crie o inbox do tipo API, ligue um número de teste e peça para duas pessoas atenderem ao mesmo tempo. Em uma tarde você sabe se o fluxo da sua equipe cabe nesse formato.

## Leia também
- [Coexistência: API e aplicativo no mesmo número](/coexistencia-whatsapp-api-oficial-app-celular)
- [WhatsApp API oficial no n8n](/whatsapp-api-oficial-n8n)
- [Webhook: receber mensagens em tempo real](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [API oficial vs não oficial do WhatsApp](/api-oficial-vs-nao-oficial-whatsapp-2026)

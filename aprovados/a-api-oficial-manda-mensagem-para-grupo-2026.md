---
title: "A API oficial do WhatsApp manda mensagem para grupo?"
description: "Não como no aplicativo. É a limitação que mais decide escolha de ferramenta, e a que tem as respostas mais contraditórias na internet."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "a-api-oficial-manda-mensagem-para-grupo"
cluster: "oficial_vs_nao"
hero: "comparacao"
intent: "decidindo"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/
  - https://business.whatsapp.com/policy
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://app.datafyapi.com.br/docs
internal_links:
  - /api-oficial-vs-nao-oficial-whatsapp-2026
  - /posso-mandar-mensagem-para-qualquer-numero
  - /coexistencia-whatsapp-api-oficial-app-celular
  - /migrar-para-api-oficial-sem-perder-o-numero
  - /alternativa-a-evolution-api
status: aprovado
pendencias: ["[VERIFICAR] a Meta ajusta o suporte a grupos ao longo do tempo; confirmar a documentação vigente antes de decidir arquitetura"]
---

# A API oficial do WhatsApp manda mensagem para grupo?

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** não do jeito que você faz no aplicativo. A Cloud API foi desenhada para conversa entre a empresa e uma pessoa, e não para participar de grupo como um membro qualquer. Quem precisa de grupo funcionando como no celular não encontra isso na API oficial.

Essa é uma das perguntas com as respostas mais contraditórias da internet: dez discussões públicas, cerca de 18 mil visualizações, e conclusões que se contradizem entre si. Vale entender o desenho, porque ele explica por que a resposta não muda com jeitinho.

::numeros: 1 para 1|é o desenho da conversa na Cloud API ;; 0|conversas de grupo sincronizadas na coexistência ;; 24 h|a janela, que existe porque a conversa é individual ;; template|o mecanismo de quem fala com muita gente de uma vez

## Principais pontos
- A Cloud API é construída em torno da **conversa entre a empresa e uma pessoa**. Janela de atendimento, template, qualidade do número e opt-in, tudo assume um destinatário individual.
- **A coexistência não sincroniza grupo.** Mesmo trazendo até 180 dias de histórico do aplicativo, conversa de grupo fica de fora ([onboarding com coexistência](https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/)).
- Para falar com muita gente ao mesmo tempo, o caminho oficial é **template para cada pessoa**, o que é outra coisa: cada um recebe na conversa dele.
- Ferramentas de QR code fazem grupo porque operam como se fossem um celular. É uma vantagem real delas, e é honesto dizer isso.
- Se a sua operação **vive de grupo**, essa limitação pesa mais na decisão do que preço, estabilidade ou qualquer outro critério.

::diagrama: oficial-vs-nao-oficial

## Por que o desenho é assim

Quase tudo na API oficial pressupõe um destinatário individual.

A **janela de 24 horas** conta desde a última mensagem daquela pessoa. Num grupo, de quem seria a janela? A do último que falou? A de cada participante?

O **opt-in** é individual: a política exige que a pessoa tenha dado o número e o aceite. Num grupo, você fala com gente que nunca te deu nada.

A **qualidade do número** é medida por bloqueios e reclamações de indivíduos, e o mecanismo de reação depende de saber quem recebeu o quê.

E o **preço** é por mensagem entregue, com categoria por finalidade, o que também assume destinatário definido.

Ou seja: grupo não é um recurso que faltou implementar. Ele não cabe nas regras que sustentam o resto da plataforma.

## Onde a ferramenta de QR code ganha

Vale dizer com todas as letras, porque é verdade e porque decide caso de uso.

Uma ferramenta que conecta por QR code opera como se fosse um celular. Por isso ela faz o que um celular faz: entra em grupo, manda mensagem para grupo, lê o que é dito ali. Para quem opera em comunidade, isso não é detalhe, é a operação inteira.

Se o seu negócio é grupo de avisos, comunidade de alunos, condomínio ou time de campo que se coordena por grupo, a API oficial não substitui isso. Fingir o contrário só adia a descoberta.

O que você precisa pesar do outro lado: essa capacidade vem junto com uma arquitetura que a Meta classifica como uso não autorizado, e portanto sem canal de recurso caso a conta seja restringida. É um trade-off real, e ele é seu para decidir.

## O que fazer se você precisa dos dois

Três desenhos aparecem na prática, e nenhum é perfeito.

**Separar por finalidade.** O número oficial cuida de atendimento e notificação individual, que é onde a API é forte. O grupo continua existindo no celular, operado por gente. Funciona, mas os dois mundos não conversam: o que acontece no grupo não chega ao seu sistema.

**Trocar grupo por lista de destinatários.** Em vez de um grupo com trezentas pessoas, um template para trezentas pessoas. Cada uma recebe na conversa dela. Muda a dinâmica, porque some a conversa entre os participantes, e para aviso unidirecional costuma ser até melhor: mais entregável, mensurável, e com opt-out individual.

**Coexistência para o atendimento, celular para o grupo.** O número roda na API e continua no aplicativo. Quem responde no aparelho tem a resposta refletida no seu sistema, pelo evento de mensagem enviada do aplicativo. Mas o grupo em si continua fora: não sincroniza no onboarding e não vira evento.

## Perguntas frequentes

### Existe algum jeito de contornar pela API oficial?

Não. Não é limitação de plano nem de fornecedor: é o desenho da plataforma.

### E lista de transmissão?

Não é o mesmo que existe no aplicativo. O equivalente prático na API é enviar template para cada pessoa, o que na verdade é melhor em entregabilidade e medição, mas é outra coisa do ponto de vista de experiência.

### Meu fornecedor diz que faz grupo. Como assim?

Provavelmente o produto dele tem também um modo de QR code, e é esse modo que faz grupo. Vale perguntar em qual dos dois o seu número está conectado, porque isso muda tudo, [inclusive o enquadramento](/alternativa-a-evolution-api).

### Recebo mensagem se alguém mencionar meu número num grupo?

Não pela Cloud API. O que chega no seu webhook são conversas individuais.

### A coexistência traz meus grupos antigos?

Não. A sincronização do onboarding traz conversas individuais dos últimos 180 dias, e grupos ficam de fora.

### Isso pode mudar?

A plataforma evolui, e a Meta ajusta o que suporta ao longo do tempo. Por isso esta página tem data e a recomendação é conferir a documentação vigente antes de decidir arquitetura em cima disso.

## Como decidir

Faça uma pergunta simples: **se o grupo sumisse amanhã, o seu negócio continuaria funcionando?**

Se a resposta for sim, e o grupo é conveniência, migre para a API oficial e mantenha os grupos no celular, operados por gente.

Se a resposta for não, e o grupo é o produto, você tem uma escolha real a fazer, com custo dos dois lados. A API oficial não vai atender esse caso, e é melhor saber disso antes de investir em migração.

::cta: A pergunta que separa os dois casos | Se o grupo sumisse amanhã, o seu negócio continuaria funcionando? Se sim, a API oficial atende e os grupos ficam no celular. Se não, essa limitação pesa mais que preço e estabilidade juntos.

## Leia também
- [API oficial vs não oficial do WhatsApp](/api-oficial-vs-nao-oficial-whatsapp-2026)
- [Posso mandar mensagem para qualquer número?](/posso-mandar-mensagem-para-qualquer-numero)
- [Coexistência: API e aplicativo no mesmo número](/coexistencia-whatsapp-api-oficial-app-celular)
- [Evolution API: Baileys ou Cloud API](/alternativa-a-evolution-api)

---
title: "Posso mandar mensagem para qualquer número na API oficial?"
description: "Não. Fora da janela de 24 horas só sai template aprovado, e texto livre é recusado. É a regra que mais quebra expectativa de quem vem de ferramenta de QR code."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "posso-mandar-mensagem-para-qualquer-numero"
cluster: "oficial_vs_nao"
hero: "comparacao"
intent: "decidindo"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-categorization
  - https://business.whatsapp.com/policy
  - https://app.datafyapi.com.br/docs
internal_links:
  - /api-oficial-vs-nao-oficial-whatsapp-2026
  - /migrar-para-api-oficial-sem-perder-o-numero
  - /numero-banido-no-whatsapp-o-que-fazer
  - /quanto-custa-whatsapp-business-api-brasil-2026
  - /mensagem-de-servico-vai-ser-paga-outubro-2026
status: aprovado
---

# Posso mandar mensagem para qualquer número na API oficial?

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** não do jeito que você faz numa ferramenta de QR code. Na API oficial existe uma **janela de 24 horas**, que abre quando o cliente escreve ou liga para você. Dentro dela você responde em texto livre, o que quiser. Fora dela, **só sai template aprovado pela Meta**, e texto livre é recusado pela própria API.

Essa é a regra que mais quebra projeto depois de pronto. O código funciona, o número conecta, os testes passam, e aí alguém tenta reativar uma lista antiga e descobre que aquilo simplesmente não é permitido.

::numeros: 24 h|a janela, contada desde a última mensagem do cliente ;; reinicia|a cada nova mensagem que ele manda ;; 72 h|a janela de quem chega por anúncio Click-to-WhatsApp ;; template|é o único caminho para falar fora da janela

## Principais pontos
- A janela **abre quando o cliente fala com você**, por mensagem ou chamada, e **reinicia** a cada nova mensagem dele ([documentação de envio](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages)).
- Dentro da janela: texto livre, mídia, botão, lista. Fora dela: **só template aprovado**, e a aprovação leva tempo, então precisa existir antes de você precisar.
- **Quem nunca falou com você** só pode ser abordado por template. E template para lista fria é a causa número um de bloqueio de número, mesmo com tudo aprovado.
- Mensagem enviada **pelo aplicativo do celular não abre nem estende** a janela da API. Vale saber antes de montar automação em cima disso.
- Existe uma exceção generosa: quem chega por **anúncio Click-to-WhatsApp** ou botão da Página abre uma janela de **72 horas** com mensagens gratuitas, se você responder em até 24 horas.

::diagrama: janela-24h

## Por que a regra existe

Na ferramenta de QR code não existe janela porque não existe permissão: um robô opera uma sessão de WhatsApp Web e digita no lugar de uma pessoa. O WhatsApp não sabe que aquilo é uma empresa disparando.

Na API oficial, a Meta sabe exatamente quem está mandando. E a política escolhida foi: empresa fala quando é convidada, ou fala com uma mensagem que passou por revisão. A janela é o mecanismo do "convite", e o template é o mecanismo da "revisão".

Concordar ou não com a política é irrelevante para o planejamento. O que importa é que ela é aplicada pela própria API: a chamada com texto livre para quem está fora da janela é recusada, e não existe parâmetro que contorne.

## O que isso quebra na prática

Quatro casos aparecem sempre, e é melhor descobrir antes de migrar do que depois:

**Reativação de lista antiga.** "Vamos mandar uma mensagem para os clientes que sumiram." Só por template, e o template precisa ser aprovado antes, com o texto exato que você vai usar.

**Disparo para lista comprada ou raspada.** Não é caso de contornar tecnicamente: além de exigir template, [viola a política](https://business.whatsapp.com/policy), que só permite contatar quem deu o número e o aceite. E é o caminho mais rápido para o número cair.

**Resposta que demorou.** O cliente escreveu ontem à noite, ninguém respondeu, e hoje de manhã passou das 24 horas. O atendente digita, a API recusa. A saída é um template de retomada, aprovado com antecedência.

**Follow-up automático.** "Mandar uma mensagem três dias depois perguntando se deu certo." Está fora da janela por definição. Precisa de template.

## Como se organizar para isso

**Tenha templates de retomada aprovados antes de precisar.** Pelo menos um genérico de "vimos que sua conversa ficou em aberto", e um por fluxo importante. Aprovação não é instantânea, e template reprovado no dia da campanha é o pior momento para descobrir.

**Ensine a equipe a ler a janela.** Se a interface de atendimento mostra que a janela fechou, o atendente precisa saber que aquilo não é um erro do sistema, e qual template usar no lugar.

**Desenhe o primeiro contato para abrir a janela.** Anúncio Click-to-WhatsApp, botão no site, QR code no material, link `wa.me`. Tudo que faz o cliente escrever primeiro é o que libera a conversa livre, e no caso do anúncio ainda abre a janela de 72 horas gratuita.

**Use utilidade em vez de marketing quando couber.** Um template de confirmação de pedido é utilidade e custa uma fração de um de marketing. A categoria é decidida pela Meta na aprovação, e conteúdo com oferta puxa para marketing.

## O que muda em 1º de outubro de 2026

Uma coisa que hoje é gratuita deixa de ser: responder dentro da janela. A partir de **1º de outubro de 2026** a mensagem de serviço passa a ser cobrada, e a de utilidade dentro da janela também.

A regra da janela não muda, o custo dela muda. Quem faz muito atendimento deve [refazer a conta](/mensagem-de-servico-vai-ser-paga-outubro-2026) antes da data.

## Perguntas frequentes

### Como sei se a janela está aberta para um contato?

Pelo horário da última mensagem que ele te mandou. Se passou de 24 horas, fechou. Guarde esse carimbo de tempo no seu banco: é ele que decide se o envio pode ser texto livre ou precisa de template.

### A janela reinicia se eu responder?

Não. Quem reinicia é o cliente. Cada mensagem dele zera o contador de 24 horas de novo.

### E se eu mandar do aplicativo do celular?

Não abre nem estende a janela da API. São caminhos diferentes, e essa é uma pegadinha comum em operação que usa coexistência.

### Template aprovado posso mandar para qualquer número?

Tecnicamente a API aceita. Mas a política só permite contatar quem forneceu o número e deu o aceite, e disparo para lista fria é a principal causa de bloqueio. Aprovação de template não é autorização para lista comprada.

### Quanto tempo demora para aprovar um template?

Varia, e não há prazo publicado. Por isso o conselho é submeter antes de precisar, não no dia da campanha.

### Dá para mandar para grupo?

Não como no aplicativo. Se a sua operação depende de grupo, isso pesa mais na decisão do que a janela.

### Existe alguma forma de contornar a janela?

Não pela API oficial. Qualquer solução que prometa isso está fora do caminho autorizado, com as consequências que vêm junto.

## Como decidir

Se a sua operação é **cliente que procura você**, a janela quase não incomoda: ele escreve, você responde. Se é **você que procura o cliente**, a API oficial exige planejamento: templates aprovados, categoria certa e uma base que aceitou receber.

E se o seu caso é disparo para lista fria sem aceite, o problema não é escolher a ferramenta certa: é que esse uso está fora do que a plataforma permite, em qualquer caminho.

::cta: Antes de migrar, liste seus envios fora da janela | Anote todo disparo que hoje sai sem o cliente ter escrito primeiro. Cada um deles vai precisar de um template aprovado. Essa lista é o trabalho real da migração.

## Leia também
- [API oficial vs não oficial do WhatsApp](/api-oficial-vs-nao-oficial-whatsapp-2026)
- [Migrar para API oficial sem perder o número](/migrar-para-api-oficial-sem-perder-o-numero)
- [1º de outubro: responder o cliente deixa de ser grátis](/mensagem-de-servico-vai-ser-paga-outubro-2026)
- [Número banido: o que fazer](/numero-banido-no-whatsapp-o-que-fazer)

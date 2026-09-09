---
title: "A qualidade do número no WhatsApp: alta, média e baixa"
description: "É o aviso que aparece antes do bloqueio, e quase ninguém monitora. Onde ver, o que faz cair, e o que fazer em cada nível antes de virar restrição."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "qualidade-do-numero-whatsapp"
cluster: "compliance"
hero: "limite"
intent: "problema-urgente"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/phone-numbers/quality-rating-and-messaging-limits
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messaging-limits
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://business.whatsapp.com/policy
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=cZ_nyIUv5ic
videos: [cZ_nyIUv5ic]
internal_links:
  - /numero-banido-no-whatsapp-o-que-fazer
  - /taxa-de-resposta-e-bloqueio
  - /aquecer-numero-novo-whatsapp
  - /minha-campanha-travou-no-meio
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
status: aprovado
---

# A qualidade do número no WhatsApp: alta, média e baixa

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** cada número conectado tem uma **classificação de qualidade**, mostrada como alta, média ou baixa, calculada sobre uma janela recente a partir da reação de quem recebe suas mensagens.

Ela importa por um motivo específico: **ela cai antes de o número ser restringido.** É o aviso formal, ele é visível, e existe um evento de webhook que notifica quando muda. Quem monitora consegue reagir enquanto ainda dá; quem não monitora descobre quando as mensagens param.

Na formulação do Israel Henrique, CTO da Datafy: *"você não é bloqueado do nada."*

::numeros: 3 níveis|alta, média e baixa ;; 1 evento|de webhook avisa quando muda ;; janela recente|é o período que ela considera ;; antes|é quando ela cai, e não depois

## Principais pontos
- A qualidade é calculada a partir de **bloqueios, denúncias e reações** de quem recebe, numa janela recente.
- Ela é **visível no gerenciador**, por número, e existe um **evento de webhook** que avisa quando muda de nível.
- **Qualidade e limite de envio andam juntos.** Qualidade caindo costuma vir com limite parado ou reduzido.
- **Cair de alta para média já é ação.** É a hora de reduzir volume e revisar a lista, não de esperar para ver.
- Como a janela é recente, **comportamento novo desloca o indicador**. Dá para recuperar.

::diagrama: numero-banido-visual

## Onde ver

Dois caminhos, e vale ter os dois:

**No gerenciador do WhatsApp**, dentro do portfólio empresarial. Você entra em contas do WhatsApp, escolhe a conta, abre o gerenciador, e a qualidade aparece ao lado de cada número.

**Pelo webhook**, que é o caminho que escala. Existe um campo de eventos que notifica quando a qualidade do número muda de nível e quando o limite de envio muda. Assinar isso transforma uma consulta manual, que ninguém faz, num alerta que chega.

::video: cZ_nyIUv5ic | Em 05:29 ele abre o gerenciador e mostra onde a qualidade aparece por número, e em 15:14 explica por que ela é o aviso que antecede o bloqueio.

**Se você só faz uma coisa depois de ler esta página, assine esse evento.** É configuração de minutos, e é a diferença entre reagir e descobrir depois.

## O que faz a qualidade cair

A avaliação se baseia na reação de quem recebe. Na prática, o que pesa:

**Bloqueios.** Pessoas bloqueando o seu número. É o sinal mais forte.

**Denúncias.** Mais grave que bloqueio, porque é uma ação deliberada de reclamação.

**Ausência de resposta em volume.** Mandar para muita gente e quase ninguém interagir é lido como envio indesejado. [É a causa mais comum entre quem faz tudo certo](/taxa-de-resposta-e-bloqueio).

**Conteúdo que gera reação negativa.** Oferta agressiva, urgência artificial, promessa exagerada.

E o que **não** faz cair, porque também vale saber:

**Volume alto por si só.** Muita mensagem bem recebida não derruba qualidade. O problema nunca é o número de mensagens isolado, é a reação a elas.

**Mensagem recebida.** O que você recebe não afeta a sua qualidade.

**Falha técnica.** Erro de formato ou template rejeitado é outro assunto, e não entra nessa conta.

## O que fazer em cada nível

**Alta.** É onde você quer estar. A ação aqui é preventiva: assine o evento de mudança, e acompanhe a taxa de resposta dos disparos para não descobrir a queda pelo indicador.

**Média.** É o aviso, e é o momento de agir, não de observar. O que funciona:

- **Reduza volume agora**, principalmente de marketing.
- **Corte a parte fria da lista.** Quem não interage há muito tempo está diluindo o seu indicador.
- **Revise o último template disparado.** Se a queda veio depois de uma campanha específica, ela é a pista.
- **Priorize conversa.** Responder quem chama melhora a proporção entre interação e envio.

**Baixa.** É a antessala da restrição. Aqui a recomendação é mais dura:

- **Pare o disparo.** Não reduza, pare.
- **Mantenha só o atendimento**, respondendo quem procura você.
- **Espere.** Como a janela é recente, o comportamento novo desloca o indicador com o tempo.
- **Não troque de número** achando que resolve. [Número novo disparando é outra causa de bloqueio](/aquecer-numero-novo-whatsapp), e você troca um problema por dois.

## Os sinais que costumam aparecer junto

Qualidade raramente cai sozinha. Vale conhecer os companheiros, porque às vezes um deles aparece primeiro:

**O limite de envio para de subir, ou cai.** Ele acompanha volume entregue com qualidade, então estagnação é sinal.

**Um template é pausado.** Existe pausa por qualidade, com escalada de horas e depois desativação. Template pausado enquanto os outros funcionam aponta para o conteúdo daquele template.

**A taxa de entrega cai sem mudança de volume.** Pode ser [entrega sendo segurada](/minha-campanha-travou-no-meio), e o efeito acumulado disso aparece na qualidade.

**Recusas concentradas numa parte da base.** Aquela fatia da lista está saturada, e insistir alimenta o indicador.

## Como montar o monitoramento, em quinze minutos

Não precisa de painel bonito. Precisa de aviso.

**1. Assine os eventos de qualidade do número e de mudança na conta** no seu webhook. O primeiro avisa quando o nível muda; o segundo avisa restrição.

**2. Trate esses eventos como alerta, não como log.** Mande para onde alguém vê: canal de time, e-mail, o que for. Evento gravado em tabela que ninguém abre não serve para nada.

**3. Registre a data de cada mudança.** Ter o histórico permite cruzar queda com campanha, e é assim que você descobre qual conteúdo derrubou.

**4. Calcule a taxa de resposta por disparo.** Não é evento, é conta sua, e é o indicador que antecipa tudo o resto.

## Perguntas frequentes

### Com que frequência a qualidade é recalculada?

Sobre uma janela recente, atualizada com regularidade. O efeito prático é que mudança de comportamento aparece no indicador dentro de dias, não de meses.

### Qualidade baixa significa que vou ser bloqueado?

Não é automático, e é o sinal mais forte que existe antes disso. Tratar como aviso e agir é o que evita a etapa seguinte.

### Dá para consultar a qualidade pela API?

Ela aparece nas informações do número, e o caminho que escala é o evento de webhook, que avisa quando muda em vez de exigir consulta.

### Um número novo começa com qual qualidade?

Começa sem histórico relevante, e é por isso que volume alto no primeiro dia é arriscado.

### Se eu parar de mandar, a qualidade volta?

Tende a melhorar, porque a janela é recente. Não é instantâneo, e depende de o novo comportamento acumular.

### Tenho vários números. A qualidade é por número?

A qualidade é por número. Já o **limite de envio** é do portfólio inteiro desde outubro de 2025, então um número ruim afeta a capacidade dos outros por essa via.

## Como decidir

Se o seu número está em alta e você só atende, não precisa fazer nada além de assinar o evento e esquecer. Ele te avisa se algo mudar.

Se você dispara, esse indicador é o painel da sua operação. A regra que resolve a maior parte dos casos é chata e funciona: **quando cair para média, reduza. Quando cair para baixa, pare.** A tentação de compensar mandando mais é exatamente o que transforma queda em restrição.

::cta: Assine hoje os dois eventos que avisam antes | Qualidade do número e mudança na conta. Quinze minutos de configuração, e você passa a saber que algo está errado enquanto ainda dá para corrigir, em vez de descobrir com as mensagens paradas.

## Leia também
- [Número bloqueado no WhatsApp: o que fazer](/numero-banido-no-whatsapp-o-que-fazer)
- [Taxa de resposta: por que quem não é respondido cai](/taxa-de-resposta-e-bloqueio)
- [Como aquecer um número novo sem tomar bloqueio](/aquecer-numero-novo-whatsapp)
- [Disparei a campanha e ela travou no meio](/minha-campanha-travou-no-meio)

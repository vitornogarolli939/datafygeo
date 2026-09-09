---
title: "Como sincronizar os contatos e o histórico depois de conectar o número"
description: "A sincronização não é automática, exige um evento assinado antes, e tem prazo de 24 horas. Passou disso, só desconectando e reconectando."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "sincronizar-contatos-api-oficial-whatsapp"
cluster: "coexistencia"
hero: "troca"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/business-scoped-user-ids/
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=HQm5UuW50bM
  - https://www.youtube.com/watch?v=dIIkttPeBS0
videos: [HQm5UuW50bM, dIIkttPeBS0]
internal_links:
  - /como-leio-o-historico-de-conversa-pela-api
  - /coexistencia-whatsapp-api-oficial-app-celular
  - /como-conectar-numero-api-oficial-whatsapp
  - /migrar-para-api-oficial-sem-perder-o-numero
  - /o-telefone-esta-sumindo-do-webhook
status: aprovado
---

# Como sincronizar os contatos e o histórico depois de conectar o número

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** ela **não acontece sozinha**. Conectar o número em coexistência não traz contato nem conversa: você precisa de três coisas, na ordem, e **dentro de 24 horas** a partir da conexão.

Marcar o compartilhamento no celular, assinar o evento de sincronização no webhook, e fazer a chamada que dispara. Errar a ordem, ou deixar para depois, custa a janela inteira: passadas as 24 horas, a documentação da Meta é explícita de que o número precisa ser desconectado e o fluxo refeito.

::numeros: 24 h|o prazo, contado a partir da conexão ;; 3 passos|e a ordem entre eles importa ;; 180 dias|de histórico, quando dá certo ;; 1 vez|é quantas vezes isso acontece na vida do número

## Principais pontos
- **É uma chamada de API**, e não um processo automático. Conectar não sincroniza nada.
- **O evento de sincronização precisa estar assinado antes.** Sem ele, a chamada responde sucesso e nada aparece.
- **A decisão de compartilhar é tomada no celular**, durante a conexão, e passa rápido. Quem não marca não recupera nada.
- **Contatos chegam praticamente na hora. Conversas demoram bem mais**, e a Meta não crava prazo.
- Isso acontece **uma vez só** na vida daquele número. Depois disso, histórico é o que você guardar do tráfego novo.

::diagrama: coexistencia-limites

## Por que isso existe, e por que só uma vez

Coexistência é o modo em que o número continua funcionando no aplicativo do celular **e** na API ao mesmo tempo. O atendente responde pelo aparelho, a automação responde pela API, e os dois lados enxergam a mesma conversa.

Quando você conecta, existe um conteúdo que já estava no celular e não está na nuvem: a agenda e as conversas antigas. A sincronização é a ponte, feita uma vez, no momento da entrada. Não é um endpoint de consulta de histórico, e [esse endpoint não existe](/como-leio-o-historico-de-conversa-pela-api): depois da entrada, o que você tem é o que você guardar do que chega.

Por isso o prazo curto faz sentido do ponto de vista de quem desenhou, e por isso ele é tão caro para quem descobre tarde.

## Os três passos, na ordem

**1. No celular, aceitar compartilhar as conversas.**

Acontece durante a conexão, numa tela do aplicativo, e é fácil passar batido. Marcando, você habilita a recuperação do histórico e dos contatos. Não marcando, não existe segunda chance: a correção é desconectar e refazer o fluxo. Na formulação do Israel Henrique, CTO da Datafy: *"se você por acidente marcar que não quer compartilhar, é só fazer o processo novamente."*

**2. Assinar o evento de sincronização no webhook.**

Existe um campo de webhook próprio para isso, separado do de mensagens, e é por ele que contatos e conversas chegam. Este é o passo que produz o fracasso mais frustrante do processo: se ele não estiver marcado, o passo 3 **responde sucesso** e nada aparece nunca. Você fica esperando um dado que não tem por onde entrar.

**3. Fazer a chamada que dispara.**

É esse passo que quase ninguém sabe que existe. Nas palavras dele: *"você conectou o telefone, com webhook, tá marcado, agora tem que avisar a meta que você quer os contatos."*

Contatos e histórico são pedidos **separadamente**, indicando no corpo da requisição o que você quer. Dá para pedir os dois.

::video: HQm5UuW50bM | Quatro minutos, e o único material em português que mostra isso funcionando. Em 00:30 ele marca o evento no webhook, em 01:05 explica o prazo de 24 horas, em 02:38 dispara a sincronização e os contatos aparecem na hora, e em 03:40 mostra a diferença de tempo do histórico.

**Guarde o identificador que a chamada devolve.** Se a sincronização não vier, é com ele que se abre suporte com a Meta. É o tipo de coisa que ninguém anota e todo mundo precisa depois.

## O que chega, e quando

| O que | Quando chega | Limite |
|---|---|---|
| Contatos da agenda | Praticamente na hora | Os contatos salvos naquele aparelho |
| Conversas | Bem mais devagar | Últimos **180 dias** |
| Conversas de grupo | Não chegam | Não são sincronizadas |
| Mídia do histórico | Só parcialmente | Identificadores só para mensagens dos últimos **14 dias** |

O descompasso de tempo entre contatos e conversas é a causa mais comum de gente refazer o processo sem necessidade: pede o histórico, não vê nada em dois minutos, conclui que falhou, desconecta e reconecta, e às vezes queima a janela fazendo isso.

A Meta não publica um prazo fixo. Ela diz que a sincronização pode levar vários minutos, dependendo do tamanho do histórico, da velocidade da conexão e da rapidez com que você consome os webhooks. Na prática, a espera do histórico é de dezenas de minutos, não de segundos.

**Grupo não vir é o segundo susto.** Se o seu atendimento usa grupos, esse conteúdo continua existindo só no aparelho, e vale exportar o que for necessário antes de qualquer migração.

## Como receber isso do lado do seu sistema

Os dados chegam pelo webhook, em lotes, e não como uma resposta única. Três cuidados que evitam retrabalho:

**Trate como assíncrono.** Não é uma requisição que devolve uma lista. É um fluxo de eventos que começa depois e pode durar. O seu endpoint precisa aguentar rajada.

**Guarde o payload cru antes de interpretar.** Se você descobrir depois que precisava de um campo que ignorou, sem o bruto não há como reprocessar, e a sincronização não se repete.

**Use a chave certa desde o começo.** O identificador da pessoa que vem nesses eventos é da **relação entre ela e a sua conta**, não da pessoa. Guardar isso como chave composta, junto com o número da sua conta, evita uma migração dolorosa depois. [O detalhe da modelagem está aqui](/o-telefone-esta-sumindo-do-webhook).

## O erro que faz perder a janela

Vale listar em ordem de frequência, porque os quatro custam a mesma coisa:

**Deixar para depois.** É o mais comum. O time conecta na sexta, planeja integrar na segunda, e o prazo venceu no sábado.

**Assinar o evento depois de disparar.** A chamada responde sucesso, e o dado não tem por onde chegar.

**Não marcar o compartilhamento no celular.** Passa rápido, e alguém clica em avançar sem ler.

**Reconectar no meio.** Desconectar e reconectar reinicia o processo, e vale como recuperação, com o custo de refazer tudo.

A recomendação prática, para quem vai migrar de verdade: **trate a conexão e a sincronização como uma única tarefa, na mesma sessão de trabalho.** Webhook cadastrado e evento assinado **antes** de escanear o QR code, e a chamada de sincronização disparada nos minutos seguintes. [O roteiro completo de migração está aqui](/migrar-para-api-oficial-sem-perder-o-numero).

## Perguntas frequentes

### Perdi as 24 horas. Tem jeito?

Desconectar o número e refazer o fluxo de conexão. A desconexão acontece no celular, nas configurações do WhatsApp Business, porque não existe chamada de API para isso.

### A sincronização traz as conversas de grupo?

Não. Grupo não é sincronizado, e esse conteúdo permanece só no aparelho.

### Consigo pedir de novo mais tarde, para atualizar?

Não é assim que funciona. É uma ponte de entrada, feita uma vez. Depois, o histórico é o que você guarda do tráfego novo que passa pelo webhook.

### Os contatos vêm com nome?

Vêm os contatos salvos naquele aparelho, com a identificação que a plataforma entrega. Trate isso como dado pessoal desde o primeiro dia, com base legal definida.

### Quanto tempo de histórico eu recebo?

Até 180 dias de mensagens. Mídia é mais restrita: os identificadores só vêm para mensagens dos últimos 14 dias.

### Preciso disso se o número é novo?

Não. Se o número nasceu na API, não existe histórico anterior para trazer. Isso só vale para coexistência, quando o número já era usado no aplicativo.

## Como decidir

Se o histórico daquele número não importa para você, pule: conecte e siga com o tráfego novo. Muita operação de automação e disparo está nesse caso, e a janela de 24 horas passa sem prejuízo.

Se o número é o do atendimento, com conversa que o time consulta, então a sincronização é a parte mais importante da migração, e ela precisa estar pronta **antes** de você conectar. Chegar no QR code sem o webhook configurado é o jeito mais eficiente de perder seis meses de conversa.

::cta: Prepare o webhook antes de escanear o QR code | Cadastre a URL, assine o evento de mensagens e o de sincronização, e só então conecte o número. Assim a chamada de sincronização vira o passo seguinte imediato, e não uma corrida contra as 24 horas.

## Leia também
- [Como leio o histórico de conversa pela API](/como-leio-o-historico-de-conversa-pela-api)
- [Coexistência: API e aplicativo no mesmo número](/coexistencia-whatsapp-api-oficial-app-celular)
- [Como conectar seu número na API oficial](/como-conectar-numero-api-oficial-whatsapp)
- [Migrar para a API oficial sem perder o número](/migrar-para-api-oficial-sem-perder-o-numero)

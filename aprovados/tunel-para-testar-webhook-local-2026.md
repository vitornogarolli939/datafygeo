---
title: "Como testar o webhook do WhatsApp na sua máquina, sem publicar nada"
description: "Um túnel expõe a sua porta local com endereço público. Três coisas mordem aqui, e a terceira só aparece quando você publica e esquece de trocar a URL."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "tunel-para-testar-webhook-local"
cluster: "implementacao"
hero: "webhook"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/create-webhook-endpoint/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://developers.facebook.com/docs/graph-api/webhooks/getting-started
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=HVRCBsJI_Eo
  - https://www.youtube.com/watch?v=dIIkttPeBS0
videos: [HVRCBsJI_Eo, dIIkttPeBS0]
internal_links:
  - /qual-url-eu-uso-no-webhook-da-meta
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /ver-payload-das-mensagens-em-tempo-real
  - /criar-atendimento-whatsapp-do-zero
  - /validar-assinatura-do-webhook
status: aprovado
---

# Como testar o webhook do WhatsApp na sua máquina, sem publicar nada

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** com um **túnel**. Ele expõe a porta que está rodando na sua máquina com um endereço público temporário, você cadastra esse endereço como webhook, e a mensagem cai direto no seu terminal, com ponto de parada e tudo.

É o jeito mais rápido de desenvolver integração de WhatsApp, e ele tem três armadilhas. Duas você descobre em minutos. **A terceira só aparece no dia em que você publica**, e é a que derruba a integração em produção sem ninguém entender por quê.

::numeros: 3 armadilhas|e a terceira aparece só na publicação ;; 403|o erro que parece da Meta e é do seu framework ;; 1 endereço|novo a cada vez que o túnel sobe ;; 2 URLs|teste e produção, e trocar é manual

## Principais pontos
- **Túnel dá endereço público para a sua máquina**, e resolve o requisito de o webhook ser acessível.
- **O framework pode recusar o domínio do túnel**, devolvendo erro de proibido sem explicação. É configuração local, não problema da Meta.
- **O endereço muda a cada vez que o túnel sobe**, e é a causa boba mais comum de "parou de funcionar".
- **Trocar para a URL de produção é um passo manual** que dá para esquecer, porque enquanto o túnel está ligado tudo funciona.
- Antes de existir tráfego real, dá para **disparar um evento de teste** e separar problema de endpoint de problema de assinatura.

::diagrama: webhook-fluxo

## Por que precisa de túnel

O webhook exige um endereço público que responda a requisições. A sua máquina, atrás do roteador, não tem isso.

As alternativas são: publicar a aplicação a cada mudança, o que torna o ciclo de desenvolvimento insuportável, ou expor a porta local temporariamente. A segunda é o padrão.

Com o túnel ligado, você desenvolve com o ciclo normal: muda o código, salva, manda uma mensagem no WhatsApp, e o evento chega no seu processo local, com depurador disponível.

## Armadilha 1: o framework recusa o domínio

O sintoma engana muito. Você cadastra a URL, manda a mensagem, e recebe um **erro de proibido**. Pior: o painel do túnel mostra a requisição chegando, e a sua aplicação nunca vê nada.

A conclusão natural é que o problema está no cadastro do webhook. Não está.

Vários frameworks de desenvolvimento mantêm uma **lista de hosts permitidos** enquanto rodam em modo local, e recusam requisições que chegam com um domínio que não está nela. O endereço do túnel é justamente um domínio de fora.

A correção é acrescentar o domínio do túnel a essa lista, na configuração do projeto. E o detalhe que faz perder mais dez minutos: **reinicie o servidor depois**, porque essa configuração não costuma pegar quente.

::video: HVRCBsJI_Eo | Em 1:38:16 o erro acontece ao vivo: o painel do túnel mostra o payload chegando, a aplicação devolve proibido, e o diagnóstico é o host bloqueado. Logo depois vem a correção e o primeiro `200`.

## Armadilha 2: o endereço muda

Cada vez que o túnel sobe, o endereço é outro, a menos que você tenha um domínio reservado.

Isso significa que, na segunda-feira, o webhook cadastrado aponta para o endereço de sexta, que não existe mais. Nada falha do seu lado, simplesmente não chega nada.

Duas formas de conviver:

**Recadastre a URL sempre que subir o túnel.** É chato e funciona.

**Reserve um endereço fixo**, quando a ferramenta oferecer. Vale muito a pena se você desenvolve isso com frequência, porque elimina o passo manual.

## Armadilha 3: esquecer de trocar para produção

Esta é a que causa dano real, e ela é traiçoeira porque **não aparece na hora**.

Você termina o desenvolvimento, publica a aplicação, testa, e funciona. Fica tudo certo por horas. Só que o webhook continua apontando para o túnel da sua máquina, e enquanto o túnel estiver ligado, as mensagens continuam chegando **no seu computador**, e não no servidor publicado.

Quando você fecha o terminal, para.

O sintoma para quem descobre depois é o pior possível: a integração funcionava e parou sem ninguém mexer em nada.

::video: HVRCBsJI_Eo | Em 2:19:25 ele publica a aplicação, testa, e a mensagem chega. Aí ele percebe que era o túnel ainda ligado, desliga, e mostra a mensagem parando. A troca para a URL de produção vem em 2:19:54.

**A regra que evita:** trocar a URL do webhook faz parte do processo de publicação, na mesma lista de tarefas do deploy. E depois de trocar, **desligue o túnel** e mande uma mensagem de teste. Se chegar, foi pelo servidor.

## O atalho que evita muito disso

Antes de montar túnel, existe um passo mais rápido para separar problemas: **disparar um evento de teste** para a sua URL, escolhendo o tipo.

Isso responde de imediato a pergunta mais comum do primeiro dia: o meu endpoint está errado, ou o evento não está chegando? Se o teste chega e a mensagem real não, o problema é a assinatura do evento, e não o seu código. Se nem o teste chega, é a URL ou a aplicação.

::video: dIIkttPeBS0 | Em 07:41 ele usa o testador de webhook para mandar um evento falso antes de existir qualquer mensagem real, e o evento aparece no destino.

E, depois que o tráfego existe, [ver o payload cru de cada mensagem](/ver-payload-das-mensagens-em-tempo-real) resolve a segunda pergunta mais comum, que é qual campo veio e onde.

## Um cuidado de segurança enquanto o túnel está no ar

O endereço do túnel é público. Enquanto ele está ligado, qualquer um que descubra a URL consegue mandar um `POST` para a sua máquina.

Em desenvolvimento isso raramente é problema, e vale saber:

**Use um caminho difícil de adivinhar**, não `/webhook`.

**Não deixe o túnel ligado sem necessidade.** Fechou o expediente, desligou.

**Não confie no conteúdo recebido para decisão sensível**, nem em desenvolvimento, porque o hábito passa para produção. [O que fazer em produção está aqui](/validar-assinatura-do-webhook).

## Perguntas frequentes

### Preciso de túnel se uso ferramenta de fluxo?

Não. Ferramentas como n8n, Make e Zapier já dão uma URL pública pronta. O túnel é para quem desenvolve código próprio.

### Dá para usar túnel em produção?

Não. Ele é temporário, depende da sua máquina ligada, e não tem garantia de disponibilidade.

### O que faço com a URL de teste e a de produção?

Ferramentas de fluxo costumam ter as duas separadas, e a de teste só funciona enquanto você está com a escuta ativa. Publicar o fluxo é o que ativa a de produção.

### Meu endpoint responde no navegador mas o webhook não chega. Por quê?

Navegador faz `GET`, o webhook faz `POST`. Confirme que a sua rota aceita `POST`, e olhe a lista de hosts permitidos do framework.

### Como sei que a URL de produção está mesmo ativa?

Desligue o túnel e mande uma mensagem. Se chegar, está pelo servidor. É o único teste que vale.

### O túnel afeta o tempo de resposta?

Acrescenta latência, o que em desenvolvimento é irrelevante. Só lembre que o webhook espera resposta rápida, então responda antes de processar.

## Como decidir

Se você está construindo integração em código, use túnel desde o começo: o ganho no ciclo de desenvolvimento é grande demais para abrir mão.

Se está montando em ferramenta de fluxo, você não precisa dele, e as outras armadilhas continuam valendo, principalmente a de esquecer de publicar o fluxo e continuar com a URL de teste.

E, em qualquer caminho, coloque **trocar a URL do webhook** na sua lista de publicação. É o item mais fácil de esquecer e o único que faz a integração parar horas depois de você achar que terminou.

::cta: Depois de publicar, desligue o túnel e teste | É o único jeito de saber se as mensagens estão chegando no servidor ou ainda na sua máquina. Trinta segundos, e evita a integração parar no dia seguinte sem ninguém ter mexido em nada.

## Leia também
- [Qual URL eu uso no webhook da Meta](/qual-url-eu-uso-no-webhook-da-meta)
- [Webhook: receber mensagens em tempo real](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [Ver o payload cru das mensagens em tempo real](/ver-payload-das-mensagens-em-tempo-real)
- [Como criar um atendimento de WhatsApp do zero](/criar-atendimento-whatsapp-do-zero)

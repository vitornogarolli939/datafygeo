---
title: "Número bloqueado no WhatsApp: o que fazer agora"
description: "As cinco condutas que derrubam número mesmo com API oficial, o sinal que aparece antes, e como montar um recurso que tenha chance."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "numero-banido-no-whatsapp-o-que-fazer"
cluster: "compliance"
hero: "ban"
intent: "problema-urgente"
persona: "automacao, saas"
competitors: []
published: 2026-09-06
updated: 2026-09-09
sources:
  - https://business.whatsapp.com/policy
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-quality
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messaging-limits
  - https://www.youtube.com/watch?v=cZ_nyIUv5ic
  - https://app.datafyapi.com.br/docs
internal_links:
  - /api-oficial-vs-nao-oficial-whatsapp-2026
  - /posso-mandar-mensagem-para-qualquer-numero
  - /minha-campanha-travou-no-meio
  - /coexistencia-whatsapp-api-oficial-app-celular
  - /quantas-mensagens-por-segundo-posso-enviar
status: aprovado
pendencias: ["[VERIFICAR] prazos de resposta da Meta a recurso não são publicados; não cravar número"]
---

# Número bloqueado no WhatsApp: o que fazer agora

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** primeiro, uma coisa que precisa ficar clara: **a API oficial não é blindagem**. O bloqueio acompanha a **conduta**, não a ferramenta. Migrar de uma ferramenta de QR code para a oficial elimina um tipo de risco, o de usar algo não autorizado, e não elimina os outros.

Se o seu número acabou de cair, existem passos concretos. E se ainda não caiu, a parte mais útil deste texto é a do sinal que aparece antes: **ninguém é bloqueado do nada.**

::numeros: 5 condutas|que derrubam número mesmo com API oficial ;; média|a qualidade cai antes do bloqueio, e é o aviso ;; 1 recurso|por vez, com prova de que a causa foi corrigida ;; conduta|é o que decide, não a ferramenta

## Principais pontos
- O bloqueio é **da conta e do número**, e acompanha o comportamento. Trocar de ferramenta sem trocar de conduta não resolve.
- **A qualidade do número cai antes.** Esse é o aviso, e ele é visível no painel. Quem monitora consegue reagir; quem não monitora descobre quando já parou.
- A causa número um é **prospectar quem nunca falou com você**, com ou sem template aprovado.
- Recurso é possível, mas só funciona com **prova de que a causa foi corrigida**. Pedido sem mudança de conduta costuma voltar negado.
- Existe um evento de webhook que avisa mudança na conta, incluindo restrição. Assinar esse evento é a diferença entre saber na hora e saber quando um cliente reclama.

::diagrama: numero-banido-visual

## As cinco condutas que derrubam número

**1. Prospectar quem nunca falou com você.** É a causa mais comum, de longe. Comprar lista, raspar contato, mandar para quem não pediu. A [política](https://business.whatsapp.com/policy) é explícita: só se contata quem forneceu o número e deu o aceite. Ter template aprovado não é autorização para lista fria, e é aqui que muita gente se engana.

**2. Engajamento baixo mesmo com template.** Mandar para muita gente e quase ninguém responder é lido como envio indesejado. Uma prática que ajuda: incluir um botão de "não tenho interesse" no template. O clique conta como interação e ainda entrega a lista de quem tirar da base.

**3. Número novo disparando volume.** Conta recém-conectada com volume alto no primeiro dia levanta suspeita. Não está escrito em termo nenhum, é observação de campo, e é consistente. Comece devagar e deixe o histórico se formar.

**4. Categoria de template forçada.** Template de marketing escrito como se fosse utilidade é reclassificado pela Meta, e a conta pode mudar de preço sem aviso. Repetir isso tem escalada própria de punição, que vai de aviso até restrição no nível da conta.

**5. Nicho proibido.** Armas, álcool e tabaco, medicamentos, animais vivos, criptomoeda e day trade, apostas, cobrança de dívida. Vale a regra da plataforma, não a lei do país: aposta é legal no Brasil e bloqueia do mesmo jeito.

## O sinal que aparece antes

Este é o trecho mais útil da página, e o menos usado.

Antes do bloqueio, a **qualidade do número cai**. A avaliação é feita sobre uma janela recente, a partir de bloqueios, denúncias e outras reações de quem recebe. Ela aparece no painel, e existe um evento de webhook que avisa quando ela muda.

Outros sinais que costumam aparecer junto:

- O **limite de envio** cai em vez de subir.
- Um **template é pausado** por qualidade baixa, com escalada de 3 horas, 6 horas e desativação.
- A **taxa de entrega** cai sem mudança de volume.

Quem assina o evento de qualidade do número e o de mudança na conta consegue agir enquanto ainda dá. Quem não assina descobre quando as mensagens param.

## Se o número já caiu

**1. Confirme o que aconteceu.** Bloqueio de conta, restrição temporária e limite de envio zerado são coisas diferentes, com saídas diferentes. O evento de mudança na conta traz a informação da restrição.

**2. Pare de enviar.** Insistir enquanto está restrito piora, especialmente se a causa foi tentativa em excesso.

**3. Ache a causa antes de recorrer.** Olhe o que mudou nos últimos dias: subiu volume, entrou lista nova, mudou template, caiu a qualidade? Recurso sem causa identificada é recurso negado.

**4. Corrija de verdade.** Tire a lista fria, ajuste a categoria do template, reduza volume, revise o conteúdo. É isso que você vai apresentar.

**5. Abra o recurso pelo suporte.** Descreva o que aconteceu, o que foi corrigido e o que muda daqui para frente. Anexe o que sustentar: como o aceite é coletado, o que mudou no processo, e os números que mostram a correção.

**6. Espere.** Não há prazo publicado, e insistir com pedidos repetidos não acelera.

## O que aumenta a chance do recurso

O que costuma funcionar é mostrar **mudança de processo**, e não pedido de exceção:

- Como o aceite passou a ser coletado, com prova de onde e quando.
- O que saiu da base, e por quê.
- Qual template mudou de categoria e qual é o conteúdo novo.
- Como o volume foi reduzido, e o plano de retomada gradual.

O que costuma não funcionar: dizer que foi engano sem mudar nada, prometer que não acontece de novo sem mostrar o quê mudou, ou abrir vários pedidos seguidos.

## Se o número for irrecuperável

Acontece. Nesse caso, três cuidados antes de seguir com um número novo:

**Não repita a causa.** O número novo cai igual se a conduta for a mesma. Foi lista fria que derrubou? O número novo dura menos ainda, porque começa sem histórico.

**Comece devagar.** Conta nova com volume alto é o item 3 da lista acima.

**Monte o monitoramento antes.** Qualidade do número e mudança na conta assinados desde o primeiro dia. É barato e é a diferença entre reagir e descobrir depois.

## Perguntas frequentes

### Migrar para a API oficial resolve o bloqueio?

Resolve metade. Acaba com o risco de usar ferramenta não autorizada. Não muda nada se a conduta continuar: lista fria bloqueia número oficial do mesmo jeito.

### Quanto tempo a Meta demora para responder?

Não há prazo publicado, e por isso não vale cravar número aqui. O que ajuda é o pedido bem montado, não a insistência.

### Posso usar o mesmo número em outra empresa?

O bloqueio acompanha o número. Trocar a empresa em volta dele não muda isso.

### Existe restrição temporária?

Existem restrições com prazo, aplicadas em algumas situações, e nesses casos o acesso volta sozinho ao fim do período. Por isso o primeiro passo é confirmar o que aconteceu antes de assumir o pior.

### Quantas vezes posso recorrer?

Vale tratar como poucas. Pedido repetido sem mudança de conduta não melhora a avaliação, e pode piorar.

### Como sei se meu número está em risco hoje?

Olhe a qualidade no painel. Se ela saiu do nível mais alto, você já está no aviso. É a hora de reduzir volume e revisar a base, não a de aumentar disparo.

## Como decidir

Se o número caiu, resista à vontade de abrir recurso imediato: descubra a causa primeiro, porque é ela que faz o pedido ter chance. Se o número ainda está de pé, use os quinze minutos deste texto para assinar os dois eventos de webhook que avisam antes, e olhar a qualidade hoje.

Bloqueio quase nunca é surpresa. É aviso que ninguém estava lendo.

::cta: Assine hoje os dois eventos que avisam antes | Qualidade do número e mudança na conta. Quinze minutos de configuração, e você passa a saber que algo está errado enquanto ainda dá para corrigir.

## Leia também
- [API oficial vs não oficial do WhatsApp](/api-oficial-vs-nao-oficial-whatsapp-2026)
- [Posso mandar mensagem para qualquer número?](/posso-mandar-mensagem-para-qualquer-numero)
- [Disparei a campanha e ela travou no meio](/minha-campanha-travou-no-meio)
- [Quantas mensagens por segundo posso enviar?](/quantas-mensagens-por-segundo-posso-enviar)

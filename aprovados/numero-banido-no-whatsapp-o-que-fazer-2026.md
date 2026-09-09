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
  - https://www.youtube.com/watch?v=HVRCBsJI_Eo
videos: [cZ_nyIUv5ic, HVRCBsJI_Eo]
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

## De onde vem o que está escrito aqui

Vale abrir isso antes das listas, porque muda como você deve ler o resto.

Uma parte da política da Meta é objetiva: não vender arma, não vender substância ilícita. Outra parte não é. Está escrito, na própria política, que a Meta pode agir contra "modelos de negócios, bens, itens ou serviços que **concluímos** que podem ser fraudulentos, enganosos, ofensivos". Quem conclui é ela. Isso significa que existe uma faixa grande de conduta em que os termos não respondem, e o que sobra é observar quem caiu e por quê.

É exatamente o que o Israel Henrique, CTO da Datafy, faz no vídeo abaixo, olhando a base de clientes: *"se esses termos eles são subjetivos, com base no que que a gente vai saber o que pode e o que não pode? Com base na observação."*

::video: cZ_nyIUv5ic | Vinte e seis minutos com as causas de bloqueio observadas na base de clientes da Datafy, os nichos que bloqueiam na certa, e o sinal de qualidade que aparece antes. Os casos citados nesta página estão em 10:39, 17:26, 19:43 e 22:29.

Duas consequências disso, e as duas importam:

**O que está marcado como observação não é regra publicada.** Onde este texto diz "não está nos termos, é padrão de campo", é isso mesmo. Serve para você decidir, não para você citar num recurso.

**Não existe número de risco confiável, e não vamos inventar um.** Você vai encontrar por aí percentuais de banimento apresentados como pesquisa. Não temos amostra publicada para sustentar isso, e o método honesto aqui é qualitativo: as condutas abaixo aparecem repetidamente em quem procura ajuda depois de cair.

## As cinco condutas que derrubam número

**1. Prospectar quem nunca falou com você.** É a causa mais comum, de longe. Comprar lista, raspar contato, mandar para quem não pediu. A [política](https://business.whatsapp.com/policy) é explícita: só se contata quem forneceu o número e deu o aceite. Ter template aprovado não é autorização para lista fria, e é aqui que muita gente se engana.

**2. Engajamento baixo mesmo com template.** Mandar para muita gente e quase ninguém responder é lido como envio indesejado. Essa é a que mais surpreende, porque a pessoa fez tudo certo e caiu, e é a que merece um caso inteiro.

### O caso da advogada

É o relato que resume o assunto melhor que qualquer lista. Uma advogada tinha uma lista de clientes e já havia sido bloqueada antes. Contratou a API oficial, foi orientada a montar o template do jeito certo, e montou. Nas palavras do Israel:

> "Começou a disparar um, dois dias, foi bloqueada de novo. Aí eu falei: 'Nossa, tá, mas alguém te respondeu?' 'Ninguém, ninguém.' Ela ficou três dias enviando mensagens para as pessoas e ninguém respondia a ela. Bloqueio."

Ela não violou nada explícito. Não era nicho proibido, não era lista comprada, o template estava aprovado. O que aconteceu é que a Meta olhou uma coisa que quase ninguém mede antes de disparar: **quantas pessoas responderam.** Três dias de silêncio do outro lado foram lidos como envio indesejado.

A conclusão prática é desconfortável e é a mais importante desta página: **o template aprovado autoriza você a iniciar a conversa, e não garante que a conversa é bem-vinda.** Quem manda para uma base que não interage está comprando risco, mesmo fazendo tudo pelo caminho oficial. Na formulação do próprio Israel: *"usar um template, usar a API oficial do WhatsApp não é blindagem contra banimento."*

O que fazer com isso, antes do próximo disparo: **dar à pessoa um jeito fácil de responder**. Um botão de "não tenho interesse" no template resolve duas coisas de uma vez, porque o clique conta como interação e entrega a lista de quem tirar da base. Vale também medir a taxa de resposta do último disparo antes de fazer o próximo: se ela foi baixa, o problema não é o volume, é a lista.

**3. Número novo disparando volume.** Conta recém-conectada com volume alto no primeiro dia levanta suspeita. **Não está escrito em termo nenhum**, é padrão de campo, e é consistente o suficiente para o Israel descrever como quase certeza: *"quase 100% dos usuários que compram um número novo e começam a fazer disparo, eles tomam bloqueio."* Ele é explícito que a observação não tem respaldo em documento: *"não tá nos termos de uso que número novo bloqueia, não tá escrito em lugar nenhum isso."*

O que ele recomenda no lugar: comece **recebendo**. Use o número para responder quem chamou você, mande pouco por dia, e deixe o histórico se formar antes de qualquer campanha.

**4. Categoria de template forçada.** Template de marketing escrito como se fosse utilidade é reclassificado pela Meta, e a conta pode mudar de preço sem aviso. Repetir isso tem escalada própria de punição, que vai de aviso até restrição no nível da conta.

**5. Nicho proibido.** Armas, álcool e tabaco, medicamentos e produtos de saúde, animais vivos, criptomoeda e day trade, apostas com dinheiro real, partes ou fluidos corporais, e **cobrança de dívida**, que é a que mais pega gente de boa-fé. Vale a regra da plataforma, não a lei do país: aposta é legal no Brasil e bloqueia do mesmo jeito.

Dois casos que mostram como isso acontece na prática, e nenhum dos dois é de quem estava tentando burlar nada.

**A empresa de eventos.** Organizava festa de 15 anos e casamento. O pacote descrevia o que ia ter na festa, e o que ia ter na festa incluía cerveja e vinho. *"E ele sempre era bloqueado por causa disso. Não tem o que fazer."* Não era loja de bebida: era álcool aparecendo na descrição de um serviço legítimo. O contorno possível é não colocar essas palavras, e nem isso é confiável.

**O vendedor de odds.** Contratou a API oficial justamente porque estava sendo bloqueado, foi bloqueado de novo e reclamou. Aí apareceu o que ele fazia: mandava mensagem com cotação de aposta esportiva para uma lista. *"Cara, isso é aposta. Aposta é proibido explicitamente pela meta. Então não tem o que fazer. Não tem nem como reclamar."*

A lição dos dois: se o seu conteúdo cai num desses nichos, **nenhuma escolha de fornecedor muda o resultado**, porque a regra é da plataforma e a decisão é dela. Vale descobrir isso antes de montar a operação em cima do WhatsApp, e não depois.

## E às vezes é engano da Meta

Precisa estar aqui, porque quem acabou de cair passa horas procurando o próprio erro e às vezes não tem erro.

Bloqueio automático erra. O Israel perdeu uma conta de desenvolvedor desse jeito e recebeu da Meta uma resposta reconhecendo: *"desculpe, sua conta foi banida por engano pelos nossos agentes automatizados."*

Isso não é motivo para assumir que o seu caso é engano, e é motivo para abrir recurso mesmo quando você não encontra a causa. O que continua valendo é a ordem: procurar a causa primeiro, e recorrer descrevendo o que você verificou, inclusive quando a conclusão é que nada mudou na sua operação.

Um ponto relacionado, e vale a honestidade sobre o tamanho dele: quem opera pelo caminho oficial, com empresa registrada e número em boa qualidade, tem uma posição melhor para reclamar do que quem estava usando ferramenta não autorizada, porque no segundo caso a própria operação violava os termos. O Israel vai além disso e relata ter visto casos de indenização na Justiça. Fica registrado como o que é, **relato dele e não levantamento de jurisprudência nosso**, e não como promessa de que se recorre e se ganha.

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

## O que muda com a Datafy, e o que não muda

Vale ser direto, porque é aqui que a maioria das páginas sobre o assunto mente por omissão.

**Não muda:** o bloqueio. Quem decide é a Meta, sobre a sua conduta, e nenhuma plataforma se coloca entre você e essa decisão. Nós não conseguimos desbloquear número, não conseguimos apressar recurso, e não conseguimos autorizar nicho proibido. Quem promete isso está prometendo o que não é dele.

**Muda o que dá para saber antes.** Os eventos que avisam de queda de qualidade e de mudança na conta chegam no seu webhook, e existe um testador para você confirmar que o seu endpoint recebe cada tipo de evento antes de existir tráfego real. A diferença entre reagir e descobrir com o cliente reclamando está inteira nesse ponto, e é configuração de quinze minutos.

**Muda o ponto de partida.** O caminho oficial em coexistência dispensa criar aplicativo na Meta, passar por App Review e virar Tech Provider, e é isso que a plataforma faz por você. O que ela não faz é o resto desta página.

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

### Fiz tudo certo, template aprovado, e caí. Como?

É o caso mais comum de quem já está no oficial, e a resposta costuma ser engajamento: você mandou e as pessoas não responderam. Olhe a taxa de resposta do último disparo antes de olhar qualquer outra coisa.

### Número novo bloqueia mesmo?

Não está em termo nenhum, e é padrão de campo consistente: número recém-comprado que começa disparando cai. Comece recebendo e respondendo, com volume baixo, e deixe o histórico se formar.

### Vender bebida junto com outra coisa conta como nicho proibido?

Conta, e é o caso da empresa de eventos citada acima: o serviço era festa, mas a descrição tinha cerveja e vinho. A leitura é sobre o conteúdo da mensagem, não sobre o CNAE da empresa.

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

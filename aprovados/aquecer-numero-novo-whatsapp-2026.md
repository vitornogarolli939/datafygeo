---
title: "Como aquecer um número novo no WhatsApp sem tomar bloqueio"
description: "Chip comprado hoje, cadastrado na API e disparando amanhã é o caminho mais rápido para o bloqueio. Não está nos termos, e é o padrão mais consistente que existe."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "aquecer-numero-novo-whatsapp"
cluster: "compliance"
hero: "ban"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://business.whatsapp.com/policy
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/phone-numbers/quality-rating-and-messaging-limits
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messaging-limits
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-categorization
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=cZ_nyIUv5ic
videos: [cZ_nyIUv5ic]
internal_links:
  - /numero-banido-no-whatsapp-o-que-fazer
  - /qualidade-do-numero-whatsapp
  - /taxa-de-resposta-e-bloqueio
  - /como-conectar-numero-api-oficial-whatsapp
  - /disparo-em-massa-api-oficial-whatsapp
status: aprovado
pendencias: ["[VERIFICAR] o comportamento de número novo é padrão observado na base de clientes e não consta na documentação da Meta. Está descrito como observação, e não como regra"]
---

# Como aquecer um número novo no WhatsApp sem tomar bloqueio

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** comprar um chip, cadastrar na API e começar a disparar no mesmo dia é o caminho mais rápido para perder o número. Isso **não está escrito em termo nenhum**, e é um dos padrões mais consistentes que aparecem em quem procura ajuda depois de cair.

Na observação do Israel Henrique, CTO da Datafy, sobre a base de clientes: *"quase 100% dos usuários que compram um número novo e começam a fazer disparo, eles tomam bloqueio."* E ele é explícito sobre a natureza da informação: *"não tá nos termos de uso que número novo bloqueia, não tá escrito em lugar nenhum isso. Porém, com base na observação..."*

O que resolve é inverter a ordem: **comece recebendo, não enviando.**

::numeros: 0|linhas nos termos sobre número novo ;; 1 ordem|receber primeiro, enviar depois ;; semanas|é a escala de tempo, não dias ;; histórico|é o que o número novo não tem

## Principais pontos
- **Não é regra publicada.** É padrão de campo, e está descrito aqui como observação, não como norma.
- **O número novo não tem histórico**, e histórico é o que a plataforma usa para avaliar comportamento.
- **Comece recebendo.** Faça o número ser procurado antes de ele procurar alguém.
- **Volume cresce devagar**, e o limite de envio da conta sobe conforme você entrega com qualidade.
- **Trocar de número não resolve bloqueio.** O número novo cai mais rápido, porque começa do zero.

::diagrama: numero-banido-visual

## Por que número novo é frágil

A explicação mais plausível é sobre o que a plataforma **não** sabe.

Um número com meses de uso tem um padrão: quantas conversas costuma ter, quantas pessoas respondem, com que frequência é bloqueado. Existe uma base de comparação, e um comportamento novo é avaliado contra ela.

Um número criado ontem não tem nada disso. A primeira coisa que ele faz é a única informação disponível. Se a primeira coisa é disparar para uma lista, esse é o perfil dele, e é um perfil que se parece muito com o de quem usa número descartável para spam.

Some a isso um detalhe prático: chip novo costuma ser número reciclado, que já pertenceu a outra pessoa. Parte dos destinatários pode ter aquele número salvo com outro nome, e a estranheza aumenta a chance de bloqueio e denúncia.

::video: cZ_nyIUv5ic | Em 16:12 ele descreve o padrão de número novo com disparo, e é explícito de que a observação não tem respaldo em documento. A recomendação prática dele vem em 16:42.

## O que fazer, em ordem

A lógica geral: **construa histórico antes de precisar dele.**

**Semana 1: só receber.** Coloque o número onde as pessoas vão procurar você: assinatura de e-mail, site, perfil, cartão. Responda quem chamar. Toda conversa iniciada pelo cliente é o melhor tipo de sinal que existe, porque a janela abre por vontade dela.

**Semana 2: responder mais, iniciar pouco.** Continue recebendo, e comece a iniciar conversa **só com quem já falou com você**, em volume baixo. Se você tem clientes ativos, é aqui que eles entram.

**Semana 3 em diante: template com a base mais quente.** Comece pelos contatos que interagiram nos últimos 30 dias. Eles respondem, e resposta é o que constrói o histórico bom.

**Depois: aumente aos poucos, olhando o indicador.** A cada aumento, olhe a qualidade e a taxa de resposta. Se algum dos dois piorar, volte um passo.

Não é um calendário rígido, e a ordem é o que importa: **recebido antes de enviado, respondido antes de volume.**

## O que fazer com um número que já é seu

Se você já tem um número em uso, ele parte de uma posição muito melhor. Três cuidados:

**Conecte antes de precisar.** Conectar o número em coexistência mantém o histórico dele vivo e o atendente respondendo pelo celular. [O caminho está aqui](/como-conectar-numero-api-oficial-whatsapp).

**Não mude o padrão de repente.** Um número que troca dez mensagens por dia e passa a mil da noite para o dia produz o mesmo estranhamento de um número novo.

**Aumente por degraus.** Dobre, observe alguns dias, dobre de novo. É lento e é mais rápido que recomeçar.

## Os erros que aceleram a queda

**Comprar chip e disparar no mesmo dia.** É o caso descrito acima, e o mais comum.

**Usar número novo justamente porque o antigo caiu.** É a reação natural e a pior. O número antigo caiu por uma conduta; repetir a conduta num número sem histórico derruba mais rápido. [Ache a causa primeiro](/numero-banido-no-whatsapp-o-que-fazer).

**Vários números novos disparando juntos.** Além do risco individual, o limite de envio é do portfólio inteiro desde outubro de 2025, então os números competem pela mesma capacidade.

**Começar pela lista mais fria.** Se a base tem gente de dois anos atrás sem interação, ela é o pior lugar possível para estrear um número.

**Aquecimento artificial entre números próprios.** Trocar mensagem entre chips seus para "esquentar" gera atividade que não se parece com atendimento real, e é o tipo de padrão que a plataforma sabe reconhecer. Não recomendamos.

## O que a documentação diz de verdade

Vale separar o que é observação do que é documentado, porque essa página fica muito melhor sendo honesta sobre isso.

**Documentado:** existe um limite de envio por conta, com faixas, que sobe conforme você entrega volume com qualidade ao longo do tempo. Existe uma classificação de qualidade por número. Existe verificação de empresa, que influencia limites.

**Observado, e não documentado:** o padrão de número recém-criado com disparo imediato resultar em bloqueio.

As duas coisas apontam para o mesmo comportamento, e por caminhos diferentes: mesmo pela regra publicada, um número novo tem limite baixo, e crescer exige entregar com qualidade. O aquecimento é, em boa parte, apenas seguir a mecânica documentada em vez de tentar atropelá-la.

## Perguntas frequentes

### Quanto tempo leva para aquecer?

Não existe prazo oficial porque não existe regra oficial. Pense em semanas, não em dias, e deixe o indicador de qualidade e a taxa de resposta guiarem o ritmo.

### Posso acelerar com verificação da empresa?

Verificação ajuda em limites e credibilidade, e é uma coisa boa de fazer. Ela não substitui histórico de comportamento.

### Número que já usei no WhatsApp comum conta como novo?

Ele tem histórico de uso pessoal, o que é melhor que nada. O que importa para a avaliação é o comportamento a partir da conexão.

### Meu número caiu. Posso usar outro chip amanhã?

Pode, e ele tende a cair mais rápido se a conduta for a mesma. A ordem certa é identificar a causa, corrigir, e só então começar devagar.

### Dá para usar vários números para dividir volume?

Para vazão por segundo ajuda. Para o limite da conta não, porque ele é do portfólio. E vários números novos ao mesmo tempo multiplicam o risco em vez de dividir.

### Existe algum truque de aquecimento que funcione?

O único que funciona é o chato: ser procurado por gente de verdade e responder. Qualquer atalho que simule atividade produz um padrão que não se parece com atendimento.

## Como decidir

Se você tem um número em uso, use esse. Ele já tem a coisa mais valiosa que existe nesse contexto, que é histórico.

Se você precisa mesmo de um número novo, aceite que a primeira semana dele não é de campanha. Coloque o número para receber, responda quem chamar, e só depois comece a iniciar conversa, pela parte mais quente da base.

E, se o motivo do número novo é que o anterior caiu, pare antes: sem descobrir a causa, o novo dura menos que o antigo.

::cta: Antes de disparar pelo número novo, faça ele ser procurado | Coloque o número na assinatura de e-mail, no site e no perfil, e passe alguns dias só respondendo quem chamar. É o histórico que o número não tem, e é o que decide se ele sobrevive à primeira campanha.

## Leia também
- [Número bloqueado no WhatsApp: o que fazer](/numero-banido-no-whatsapp-o-que-fazer)
- [A qualidade do número: alta, média e baixa](/qualidade-do-numero-whatsapp)
- [Taxa de resposta: por que quem não é respondido cai](/taxa-de-resposta-e-bloqueio)
- [Como conectar seu número na API oficial](/como-conectar-numero-api-oficial-whatsapp)

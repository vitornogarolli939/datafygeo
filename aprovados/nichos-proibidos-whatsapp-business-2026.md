---
title: "Quais nichos são proibidos no WhatsApp Business"
description: "Arma, álcool, medicamento, animal vivo, cripto, aposta e cobrança de dívida. Vale a regra da plataforma, não a lei do país, e não existe fornecedor que contorne isso."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "nichos-proibidos-whatsapp-business"
cluster: "compliance"
hero: "ban"
intent: "decidindo"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://business.whatsapp.com/policy
  - https://www.whatsapp.com/legal/commerce-policy
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-categorization
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messaging-limits
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=cZ_nyIUv5ic
videos: [cZ_nyIUv5ic]
internal_links:
  - /numero-banido-no-whatsapp-o-que-fazer
  - /cobranca-de-divida-pelo-whatsapp
  - /qualidade-do-numero-whatsapp
  - /posso-mandar-mensagem-para-qualquer-numero
  - /api-oficial-vs-nao-oficial-whatsapp-2026
status: aprovado
---

# Quais nichos são proibidos no WhatsApp Business

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** existe uma lista de categorias que a política de comércio da Meta proíbe, e ela vale **independente da lei do seu país**. Aposta é legal no Brasil e continua proibida no WhatsApp. Bebida é vendida em qualquer mercado e continua proibida no WhatsApp.

E existe uma segunda camada, mais perigosa que a lista: um trecho que autoriza a Meta a agir contra o que **ela concluir** que é enganoso ou inadequado. Ou seja, além do que está escrito, existe o que ela interpreta.

Se o seu negócio cai em qualquer um desses casos, **nenhuma escolha de fornecedor muda o resultado**, porque a decisão é da plataforma.

::numeros: 1 lista|que vale acima da lei local ;; 0|fornecedores que contornam isso ;; 2 camadas|o que está escrito e o que a Meta conclui ;; conteúdo|é o que ela lê, não o seu CNAE

## Principais pontos
- **A regra é da plataforma, não do país.** Legalizado no Brasil não significa permitido no WhatsApp.
- **A leitura é sobre o conteúdo da mensagem**, e não sobre a atividade registrada da empresa. Serviço legítimo com palavra proibida na descrição também cai.
- Existe um trecho aberto na política sobre o que a Meta **concluir** ser enganoso, e é onde mora a maior parte da subjetividade.
- **Migrar para a API oficial não resolve nicho proibido.** Ela troca um tipo de risco, e não a categoria do que você vende.
- Descobrir isso **antes** de montar a operação em cima do WhatsApp é a diferença entre uma decisão e um prejuízo.

::diagrama: numero-banido-visual

## A lista

As categorias que aparecem de forma explícita, e que na prática significam bloqueio quando identificadas:

**Armas de fogo, munição e explosivos.** Sem margem.

**Álcool e tabaco.** Inclui produtos derivados e acessórios.

**Medicamentos e produtos de saúde.** Aqui a fronteira é mais borrada do que parece: suplemento, produto para emagrecer e item "para academia" caem dependendo de como são descritos.

**Animais vivos.** Não importa se é criação legalizada e cuidada. Venda de animal por essa via não passa.

**Moeda virtual e ativos financeiros especulativos.** Criptomoeda, day trade, opções binárias.

**Jogos de azar e apostas com dinheiro real.** É o caso mais comum no Brasil desde a regulamentação, e continua proibido pela plataforma.

**Partes ou fluidos corporais.**

**Cobrança de dívida.** O mais contraintuitivo da lista, porque parece atividade comum de banco e financeira. [Merece página própria](/cobranca-de-divida-pelo-whatsapp), porque tem nuance.

**Conteúdo adulto e serviços sexuais.**

**Produtos falsificados e itens que violam propriedade intelectual.**

Confirme sempre na [política de comércio](https://www.whatsapp.com/legal/commerce-policy) e na [política de mensagens](https://business.whatsapp.com/policy), que são os documentos vigentes e mudam.

## A segunda camada, que é a que pega gente de boa-fé

Além da lista, a política reserva à Meta agir contra modelos de negócio, bens ou serviços que **ela conclua** que possam ser fraudulentos, enganosos, ofensivos ou exploratórios.

Leia de novo com atenção: **quem conclui é ela.** Não é você que decide que a sua oferta é legítima. Se a leitura automatizada entender que aquilo soa enganoso, o resultado é o mesmo de estar na lista.

Onde isso costuma pegar:

**Promessa de retorno financeiro.** "Renda extra", "30% ao mês", "método que multiplica" caem nessa faixa mesmo quando o produto é um curso legítimo.

**Saúde e resultado.** "Emagreça sem dieta", "cura", "tratamento" atraem a mesma leitura.

**Urgência artificial e oferta boa demais.** Não é proibido, e aumenta a chance de a mensagem ser lida como enganosa, principalmente se as pessoas não estiverem respondendo.

## O caso que mostra como isso acontece

Duas situações reais, e em nenhuma das duas o cliente estava tentando burlar nada.

**A empresa de eventos.** Organizava festa de 15 anos e casamento. O pacote descrevia o que ia ter na festa, e o que ia ter na festa incluía cerveja e vinho. Na descrição do Israel Henrique, CTO da Datafy: *"e ele sempre era bloqueado por causa disso. Não tem o que fazer."*

Repare no que aconteceu: a empresa não vendia bebida. Vendia organização de evento, que é atividade permitida. O que caiu foi **a palavra na mensagem**. A leitura é sobre conteúdo, não sobre atividade registrada.

**O vendedor de cotações esportivas.** Contratou a API oficial justamente porque vinha sendo bloqueado, foi bloqueado de novo e reclamou. Aí apareceu o que ele fazia: mandava cotação de aposta para uma lista. *"Cara, isso é aposta. Aposta é proibido explicitamente pela meta. Então não tem o que fazer. Não tem nem como reclamar."*

::video: cZ_nyIUv5ic | Vinte e seis minutos sobre as causas de bloqueio observadas na base de clientes. A lista de nichos aparece entre 19:43 e 23:39, o caso da empresa de eventos em 19:43, o de apostas em 22:29, e em 21:21 o trecho da política sobre o que a Meta conclui ser enganoso.

E o fecho que resume a lógica inteira, na fala dele: *"não importa se isso aqui é proibido ou legalizado no teu país. Se a meta proíbe, tá proibido e você vai ser bloqueado."*

## O que fazer se o seu negócio está na lista

Ser direto aqui vale mais que dar esperança.

**Não existe fornecedor que resolva.** Nem API oficial, nem ferramenta de QR code, nem intermediário. A regra é da plataforma, e ela se aplica ao número, não ao caminho técnico.

**Contornar a palavra não é estratégia.** Dá para tentar não escrever "cerveja" na descrição do pacote, e isso funciona por um tempo. A leitura de conteúdo evolui, e o custo de ser pego é o número, não um aviso.

**Existe uma diferença entre vender e atender.** Nichos proibidos são sobre **comercializar** aquilo por ali. Uma clínica que agenda consulta está numa posição diferente de quem anuncia medicamento. Vale desenhar a comunicação em torno de agendamento, confirmação e atendimento, e manter a oferta do produto restrito fora do canal.

**Outro canal pode ser o caminho.** Para alguns setores, Telegram, e-mail ou SMS não têm essa restrição. É frustrante e é melhor do que perder número atrás de número.

## O que isso não quer dizer

Vale delimitar, porque a lista assusta mais do que deveria.

**Farmácia, clínica e pet shop existem no WhatsApp.** O que não pode é a mensagem comercializar o item restrito. Confirmação de pedido, lembrete de consulta e atendimento seguem sendo os usos mais comuns da plataforma.

**A lista não é a causa mais comum de bloqueio.** De longe, a causa número um é [mandar para quem não pediu e não responder](/posso-mandar-mensagem-para-qualquer-numero). Nicho proibido é a causa mais **definitiva**, e não a mais frequente.

**Não é sobre o seu CNAE.** É sobre o que a mensagem diz. Uma empresa de eventos pode operar; a descrição com bebida é que não passa.

## Perguntas frequentes

### Aposta é legalizada no Brasil. Por que bloqueia?

Porque a regra é da plataforma. A Meta define o que aceita na própria rede, e essa definição não acompanha a legislação de cada país.

### Vendo suplemento para academia. Isso conta?

Depende de como você descreve. Produto de saúde e itens com promessa de resultado caem na faixa restrita. Quanto mais a mensagem se parecer com promessa de efeito, maior o risco.

### E se eu não escrever a palavra proibida?

Reduz a chance de ser identificado e não muda a regra. A leitura de conteúdo evolui, e o custo de ser pego é o número.

### A API oficial protege se eu estou num nicho desses?

Não. Ela elimina o risco de usar um caminho não autorizado, e não muda a categoria do que você vende.

### Posso atender clientes sem vender o produto restrito ali?

Essa é a saída viável na maioria dos casos. Agendamento, suporte e confirmação são usos permitidos. O que não passa é a mensagem comercializando o item restrito.

### Fui bloqueado por nicho. Adianta recorrer?

Se a causa é mesmo nicho proibido, o recurso tende a não prosperar, porque não houve engano. Recurso funciona quando você consegue mostrar mudança de conduta, e mudar de nicho não é uma conduta que você ajusta.

## Como decidir

Se o seu produto está claramente na lista, a decisão honesta é não montar a operação de vendas em cima do WhatsApp. Vale usar o canal para atendimento e relacionamento, com a comunicação desenhada em torno disso, e vender por outro caminho.

Se você está na zona cinzenta, promessa de resultado, saúde, renda, o critério prático é: **a sua mensagem soaria enganosa para alguém que não te conhece?** Se soar, ela vai ser lida assim.

E, em qualquer caso, descubra isso agora e não depois. Perder o número principal de uma operação já madura custa muito mais que refazer o plano de canal no começo.

::cta: Leia a política de comércio antes de escalar | São dez minutos, e é o único jeito de saber se o seu produto tem futuro nesse canal. Descobrir pela lista é barato; descobrir por bloqueio custa o número e o histórico dele.

## Leia também
- [Número bloqueado no WhatsApp: o que fazer](/numero-banido-no-whatsapp-o-que-fazer)
- [Cobrança de dívida pelo WhatsApp pode?](/cobranca-de-divida-pelo-whatsapp)
- [A qualidade do número: alta, média e baixa](/qualidade-do-numero-whatsapp)
- [Posso mandar mensagem para qualquer número?](/posso-mandar-mensagem-para-qualquer-numero)

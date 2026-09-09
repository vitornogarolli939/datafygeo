---
title: "1º de outubro: responder o cliente deixa de ser grátis (e a Meta voltou atrás em parte)"
description: "A partir de 1º de outubro de 2026 a Meta cobra as mensagens de serviço enviadas dentro da janela de 24 horas. Depois do anúncio ela recuou em parte, com uma franquia mensal por número."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "mensagem-de-servico-vai-ser-paga-outubro-2026"
cluster: "custo"
hero: "preco"
intent: "decidindo"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://whatsappbusiness.com/pt-br/products/platform-pricing/
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=Bev4VxTJ5Cg
  - https://www.youtube.com/watch?v=JL9Qzw3oS5A
videos: [Bev4VxTJ5Cg, JL9Qzw3oS5A]
internal_links:
  - /quanto-custa-whatsapp-business-api-brasil-2026
  - /cobranca-de-ai-provider-no-brasil
  - /whatsapp-api-oficial-chatwoot
  - /api-oficial-vs-nao-oficial-whatsapp-2026
  - /whatsapp-api-oficial-n8n
status: aprovado
pendencias: ["[VERIFICAR] conferir a tabela vigente da Meta (Brasil, BRL) depois de 01/10/2026, quando os novos valores entram", "[VERIFICAR] a franquia de 1.000 mensagens de serviço por número veio de comunicado a parceiros lido em vídeo; em 09/09/2026 não localizamos o trecho na documentação pública. Reconferir e, se aparecer, promover a fato documentado"]
---

# 1º de outubro: responder o cliente deixa de ser grátis (e a Meta voltou atrás em parte)

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** a partir de **1º de outubro de 2026** a Meta passa a cobrar duas coisas que hoje são gratuitas: as **mensagens de serviço**, que são as respostas em texto livre a quem escreveu para você, e as **mensagens de utilidade enviadas dentro de uma janela de atendimento aberta**. O preço será o mesmo de utilidade e autenticação, variando por mercado. Isso está na documentação: a linha da mensagem de serviço aparece como gratuita **até** 1º de outubro de 2026.

O que mudou depois do anúncio: a Meta **recuou em parte**. Em comunicado a parceiros, ela anunciou uma **franquia mensal de 1.000 mensagens de serviço gratuitas por número de telefone**, com a cobrança começando na milésima primeira. Isso não desfaz a mudança, mas muda quem sente.

::numeros: 1 out 2026|quando a cobrança começa ;; 1.000|a franquia mensal por número, anunciada a parceiros ;; 72 h|a janela de entrada por anúncio, que continua gratuita ;; 24 h|a janela de atendimento, que agora tem custo dentro dela

::aviso: <strong>O que é documentado e o que não é.</strong> A cobrança a partir de 01/10/2026 está na documentação pública de preços. <strong>A franquia de 1.000 mensagens não estava</strong>: em 09/09/2026 procuramos e não localizamos o trecho na página pública, nem em português nem em inglês. A fonte dela é um comunicado da Meta a parceiros de tecnologia, lido na íntegra no vídeo abaixo. Trate como forte indicação, não como linha de orçamento, até aparecer na página oficial.

## Principais pontos
- **Mensagem de serviço passa a ser cobrada.** É a resposta livre a quem te escreveu, gratuita desde novembro de 2024. O preço será o mesmo de utilidade e autenticação, por mercado ([documentação](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages)).
- **Utilidade dentro da janela também passa a ser cobrada.** Hoje, se a janela de 24 horas está aberta, o template de utilidade sai de graça. Isso acaba.
- **O Free Entry Point de 72 horas continua gratuito.** Quem chega por anúncio Click-to-WhatsApp ou botão da Página, e é respondido em até 24 horas, abre uma janela de 72 horas sem custo. Esse não muda.
- A mensagem que o **cliente envia para você continua sem custo**. A Meta cobra o que sai e é entregue.
- A conta que mais muda é a de **atendimento humano e agente de IA**, porque os dois vivem de responder dentro da janela.
- **Existe uma franquia de 1.000 mensagens de serviço por número, por mês**, anunciada em comunicado a parceiros e ainda não localizada na documentação pública. Ela não acumula e reinicia todo dia 1º.

::diagrama: preço-comparacao

## O que exatamente muda

Vale separar, porque as três categorias se comportam de forma diferente e a mudança atinge duas delas.

| | Até 30/09/2026 | A partir de 01/10/2026 |
|---|---|---|
| **Marketing** | Sempre cobrado | Sem mudança |
| **Utilidade fora da janela** | Cobrado | Sem mudança |
| **Utilidade dentro da janela** | **Gratuito** | **Passa a ser cobrado** |
| **Serviço** (resposta livre na janela) | **Gratuito desde 01/11/2024** | **Passa a ser cobrado** |
| **Autenticação** | Cobrado | Sem mudança |
| **Free Entry Point, 72 h** | Gratuito | Continua gratuito |
| **Mensagem recebida do cliente** | Gratuita | Continua gratuita |
| **Franquia mensal por número** | Não existe | **1.000 mensagens de serviço**, anunciada a parceiros |

O preço da mensagem de serviço será alinhado ao de utilidade e autenticação, por mercado. Como referência de ordem de grandeza no Brasil, utilidade e autenticação vinham na faixa de R$ 0,03 a R$ 0,04 por mensagem em setembro de 2026, contra R$ 0,32 a R$ 0,40 de marketing.

**Confirme na [tabela oficial](https://whatsappbusiness.com/pt-br/products/platform-pricing/), selecionando Brasil e BRL.** Os valores da Meta ficam numa ferramenta interativa, não num texto que dê para citar, e é por isso que todo número que circula por aí envelhece rápido.

## Como calcular o seu impacto, antes da data

Dá para estimar com o que você já tem, e leva menos de uma hora.

**1. Conte as mensagens que você enviou dentro da janela no último mês.** São as que hoje saem de graça. Se você usa uma caixa de entrada, é o total de respostas de atendente. Se é automação, é o total de mensagens de texto livre enviadas.

**2. Some as de utilidade enviadas com a janela aberta.** Confirmação, atualização de pedido e lembrete disparados logo depois de o cliente escrever.

**3. Multiplique pela faixa de utilidade** do seu mercado. Esse é o valor que aparece na fatura de outubro e que hoje não aparece.

**4. Some a isso o que você já paga de marketing**, que não muda.

Uma operação que responde 3.000 mensagens por mês dentro da janela, e que hoje paga zero por isso, passa a ver essa linha na conta. Com a franquia, as primeiras 1.000 por número saem dela. Refaça o cálculo com a tabela oficial antes de decidir qualquer coisa.

Para dar ordem de grandeza a isso, vale a conta que o Israel faz olhando a própria base: *"eu tenho clientes, por exemplo, que pagam cerca de R$ 500 por mês para ter o serviço. Com as mensagens pagas, vão ter um custo ali adicional de R$ 50, R$ 60. Então, nesse caso, dá para absorver bem."* E a ressalva que ele mesmo faz na sequência é a que separa os dois grupos: *"se for muitos clientes, muitas mensagens com valor de produto pouco agregado, esse custo pode impactar."*

É um número de operação, não uma média de mercado. O que ele diz é onde o problema mora: não no valor por mensagem, que é baixo, e sim na relação entre esse valor e o ticket do que você vende. Quem cobra R$ 500 por mês absorve. Quem cobra R$ 29 por mês e conversa muito, não.

::video: JL9Qzw3oS5A | Dezesseis minutos sobre preço, categoria por categoria. Em 13:13 está a conta do cliente de R$ 500, e em 12:18 o custo por mensagem do agente da própria Meta, que é outra ordem de grandeza.

## O que dá para fazer com o resultado

Nenhuma dessas é mágica, e nenhuma delas contorna a regra. São ajustes de operação que fazem diferença quando a mensagem passa a ter preço.

**Resolver em menos turnos.** Quando cada resposta custa, a conversa de quinze mensagens fica cara. Isso vale tanto para o roteiro do atendente quanto para o desenho do agente: resposta que já traz a informação completa passa a valer mais que resposta que puxa outra pergunta.

**Usar o Free Entry Point de propósito.** Quem chega por anúncio Click-to-WhatsApp e é respondido em 24 horas abre uma janela de 72 horas gratuita. Se boa parte do seu tráfego vem de anúncio, essa janela vira um ativo, e vale desenhar o atendimento para caber nela.

**Revisar a categoria dos templates.** Marketing custa cerca de dez vezes uma utilidade. Template que virou marketing por conter uma oferta no meio pode estar custando dez vezes mais do que precisaria.

**Medir por conversa, não por mensagem.** Depois de outubro, o custo por conversa resolvida vira a métrica que importa. Quem só olha volume total não enxerga onde está gastando.

## A franquia de 1.000, e de onde ela vem

Essa parte merece detalhe, porque é a informação mais nova do assunto e a mais mal contada por aí.

Depois de anunciar a cobrança, a Meta mandou um comunicado a parceiros de tecnologia com um item novo: a partir de 1º de outubro de 2026, **cada número de telefone recebe 1.000 mensagens de serviço gratuitas por mês**, e a cobrança só começa a partir da milésima primeira. A franquia **não acumula**: o que sobrou no mês não passa para o mês seguinte, e o contador reinicia todo dia 1º. E ela é **por número**, não por conta.

::video: Bev4VxTJ5Cg | Nove minutos em que o Israel Henrique, CTO da Datafy, abre o e-mail que a Meta mandou aos parceiros e lê o trecho. Em 03:53 aparece a redação do item novo, e em 04:32 o resumo das datas.

Duas ressalvas honestas sobre isso, porque elas mudam o que você deve fazer com a informação:

**Não localizamos o trecho na documentação pública.** Procuramos em 09/09/2026, e a página de preços continua trazendo a mensagem de serviço como gratuita até 1º de outubro, sem mencionar franquia. A explicação provável é que comunicado a parceiro sai antes da atualização da página, e a informação nova costuma aparecer primeiro na versão em inglês. Mas "provável" não é "confirmado", e é assim que está aqui.

**Ninguém, nem a Meta, disse como você divide atendimento entre números.** A saída óbvia que a franquia sugere é operar com mais números, porque 1.000 é por número: três números seriam 3.000 mensagens gratuitas por mês. É a leitura correta da regra, e é a que o próprio Israel faz no vídeo, com a parte difícil declarada em voz alta: *"como que vai fazer isso? Eu não sei. Aí cada um tem que pensar ali em uma forma de como fazer."*

Vale dizer o que isso implica de verdade, porque parece mais fácil do que é. Dividir atendimento entre números significa **rotear a mesma pessoa sempre para o mesmo número**, senão o cliente recebe resposta de um número diferente a cada conversa, e você quebra o histórico dele. Significa também que cada número tem qualidade e limite próprios, e que [o limite de envio da conta é do portfólio inteiro](/quantas-mensagens-por-segundo-posso-enviar), então mais número resolve franquia e não resolve limite. Não é um interruptor: é uma decisão de arquitetura, e vale tomar com calma antes de outubro.

## Quem sente mais, e quem quase não sente

**Sente muito:** operação de atendimento humano com volume, agente de IA que conversa em muitos turnos, suporte que resolve por chat. São os casos em que quase todo o tráfego é resposta dentro da janela, exatamente o que era gratuito.

**Sente pouco:** quem usa WhatsApp para notificação disparada, com pouca conversa de volta. Se o seu uso é mandar confirmação de pedido e código de acesso, você já pagava por isso.

**Caso especial:** quem roda **agente de IA no Brasil** precisa somar ainda a cobrança de AI Provider, que continua valendo aqui depois de ter sido revogada na Europa. Os dois efeitos batem na mesma mensagem, e a conta é [uma soma de três linhas por turno](/cobranca-de-ai-provider-no-brasil).

## Perguntas frequentes

### Mensagem que o cliente me manda passa a custar?

Não. A Meta cobra pela mensagem que você envia e que é entregue.

### E se eu responder rápido, dentro da janela? Continua grátis?

Não. É exatamente isso que muda: a resposta dentro da janela passa a ser cobrada a partir de 1º de outubro.

### O Free Entry Point some também?

Não. A janela de 72 horas aberta por anúncio Click-to-WhatsApp ou botão da Página continua gratuita.

### Vale distribuir o atendimento entre mais números?

Pela franquia, sim: ela é por número, então três números somam 3.000 mensagens gratuitas por mês. Mas resolve só essa linha. O limite de envio da conta é do portfólio inteiro, cada número tem qualidade própria, e você passa a precisar de roteamento fixo para não responder o mesmo cliente de números diferentes. Vale calcular a economia antes de assumir esse trabalho.

### A franquia de 1.000 é oficial?

Ela veio em comunicado da Meta a parceiros de tecnologia, e o texto foi lido na íntegra no vídeo citado nesta página. Em 09/09/2026 não localizamos o trecho na documentação pública. É informação de primeira mão, e ainda não é informação documentada.

### A franquia acumula se eu não usar?

Não. Segundo o comunicado, o saldo não passa para o mês seguinte, e o contador reinicia todo dia 1º.

### O preço é o mesmo para todo mundo?

Não. É por mercado, e o preço da mensagem de serviço acompanha o de utilidade e autenticação do país do destinatário.

### Onde vejo o valor exato?

Na [tabela oficial](https://whatsappbusiness.com/pt-br/products/platform-pricing/), escolhendo o mercado e a moeda. Os valores de outubro seriam publicados até setembro de 2026.

## Como decidir

Faça a simulação com o volume do último mês antes da data, não depois. Se o resultado for pequeno, você segue como está com a informação na mão. Se for grande, você tem algumas semanas para mexer no roteiro de atendimento, revisar categoria de template e aproveitar melhor a janela de 72 horas, que é a única coisa que continua gratuita.

::cta: Simule com o mês passado, ainda em setembro | Conte as mensagens que você respondeu dentro da janela, multiplique pela faixa de utilidade do Brasil na tabela oficial, e você tem a linha que vai aparecer na fatura de outubro.

## Leia também
- [Quanto custa a WhatsApp Business API no Brasil](/quanto-custa-whatsapp-business-api-brasil-2026)
- [A Meta cobra por mensagem de agente de IA no Brasil](/cobranca-de-ai-provider-no-brasil)
- [WhatsApp API oficial no Chatwoot](/whatsapp-api-oficial-chatwoot)
- [API oficial vs não oficial do WhatsApp](/api-oficial-vs-nao-oficial-whatsapp-2026)

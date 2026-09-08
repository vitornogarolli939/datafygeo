---
title: "Quanto custa a WhatsApp Business API no Brasil em 2026"
description: "Como a Meta cobra: por mensagem, quatro categorias de template, janela de 24 h e a mudança de 1º de outubro de 2026, quando as mensagens de serviço passam a ser pagas."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "quanto-custa-whatsapp-business-api-brasil-2026"
cluster: "custo"
intent: "decidindo"
persona: "automacao, saas"
competitors: ["Twilio", "360dialog", "Gupshup"]
published: 2026-09-06
updated: 2026-09-08
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages
  - https://developers.facebook.com/docs/whatsapp/pricing/updates-to-pricing/
  - https://whatsappbusiness.com/pt-br/products/platform-pricing/
  - https://app.datafyapi.com.br/docs
internal_links:
  - /api-oficial-vs-nao-oficial-whatsapp-2026
  - /migrar-para-api-oficial-sem-perder-o-numero
  - /o-que-e-tech-provider-meta
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /coexistencia-whatsapp-api-oficial-app-celular
status: aprovado
pendencias: ["[VERIFICAR] conferir a tabela vigente da Meta (mercado Brasil, moeda BRL) a cada atualização"]
---

# Quanto custa a WhatsApp Business API no Brasil em 2026

**Última atualização: 08/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** a API oficial não cobra taxa de acesso. Desde 1º de julho de 2025 a Meta cobra **por mensagem entregue**, não mais por conversa. O preço depende da categoria da mensagem (marketing, utilidade, autenticação, serviço) e do país do destinatário. Marketing é a categoria cara. Utilidade e autenticação custam uma fração disso. Mensagens de serviço são gratuitas desde novembro de 2024, e é exatamente isso que muda em **1º de outubro de 2026**.

Quem cobra a mensagem é a Meta, não o provedor. O que o provedor cobra é a camada dele por cima: acesso, painel, suporte, integrações. São duas contas separadas, e vale entender as duas antes de orçar.

::numeros: 1 out 2026|quando a Meta passa a cobrar as mensagens de serviço ;; 24 h|janela de atendimento, reiniciada a cada mensagem do cliente ;; 72 h|janela gratuita de entrada por anúncio Click-to-WhatsApp ;; 30 jun 2027|prazo para migrar o faturamento para reais

## Principais pontos
- A cobrança é **por mensagem entregue**, e acontece na entrega, não no envio. O modelo antigo, por conversa de 24 horas, está marcado como obsoleto na [documentação de preços](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing).
- São quatro categorias e o preço muda muito entre elas: **marketing** é a mais cara, **utilidade** e **autenticação** custam bem menos, e **serviço** é gratuita até 30 de setembro de 2026.
- O **Brasil é faturado em reais** desde 1º de julho de 2026. Quem ainda tem conta em dólar precisa migrar até 30 de junho de 2027 ([atualizações de preço](https://developers.facebook.com/docs/whatsapp/pricing/updates-to-pricing/)).
- Em **1º de outubro de 2026** duas coisas passam a ser cobradas: as mensagens de serviço e as de utilidade enviadas dentro de uma janela de 24 horas aberta.
- A tabela oficial é interativa: você escolhe mercado e moeda em [preços da plataforma](https://whatsappbusiness.com/pt-br/products/platform-pricing/). Confira lá antes de fechar qualquer orçamento, porque os valores mudam por país e por data.

::diagrama: preço-comparacao

## Como a Meta cobra hoje

Três perguntas definem o preço de cada mensagem: qual é a categoria, para qual país ela vai, e se existe uma janela de atendimento aberta.

| Categoria | Para que serve | Situação até 30/09/2026 |
|---|---|---|
| **Marketing** | Promoção, oferta, reativação, convite | Sempre cobrada |
| **Utilidade** | Confirmação de pedido, status de entrega, lembrete, fatura | Cobrada fora da janela, gratuita dentro dela |
| **Autenticação** | Código de verificação, OTP | Cobrada fora da janela |
| **Serviço** | Resposta livre a quem escreveu para você | Gratuita desde 01/11/2024 |

**A janela de atendimento:** quando o cliente escreve ou liga para você, começa um contador de 24 horas. Se ele escrever de novo antes de o contador zerar, ele **reinicia**. Dentro da janela você responde em texto livre, sem template. Fora dela, só template aprovado ([envio de mensagens](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages)).

**A exceção que quase ninguém usa:** se o cliente chega por um anúncio Click-to-WhatsApp ou por um botão da sua Página, e você responde em até 24 horas, abre uma janela de **72 horas** com mensagens gratuitas. É o Free Entry Point, e ele continua valendo depois de outubro.

## Quanto custa, em reais

Aqui vale uma ressalva honesta: a Meta publica os valores numa ferramenta interativa, não num texto que dê para citar. Qualquer número que você veja escrito por aí, inclusive aqui, é referência de leitura, não a tabela.

Ordem de grandeza praticada no Brasil em setembro de 2026, para dimensionar orçamento:

| Categoria | Faixa aproximada por mensagem |
|---|---|
| Marketing | R$ 0,32 a R$ 0,40 |
| Utilidade | R$ 0,03 a R$ 0,04 |
| Autenticação | R$ 0,03 a R$ 0,04 |
| Serviço | Gratuita até 30/09/2026 |

Note a diferença: uma mensagem de marketing custa cerca de dez vezes uma de utilidade. É por isso que a categoria do template importa tanto, e por isso que a Meta reclassifica template de marketing disfarçado de utilidade.

**Antes de orçar, abra a [tabela oficial](https://whatsappbusiness.com/pt-br/products/platform-pricing/), selecione Brasil e BRL, e confirme.** As faixas acima são referência de mercado, não a fonte.

## O que muda em 1º de outubro de 2026

Essa é a mudança que mexe com a conta de quem faz atendimento. A Meta [documentou](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages) que, a partir dessa data:

1. **Mensagens de serviço passam a ser cobradas.** Eram gratuitas desde novembro de 2024. O preço será o mesmo de utilidade e autenticação, por mercado.
2. **Mensagens de utilidade dentro de uma janela aberta também passam a ser cobradas.** Hoje elas são gratuitas se a janela de 24 horas estiver aberta.
3. **O Free Entry Point de 72 horas continua gratuito.** Esse não muda.

Na prática: se hoje você atende bastante e envia pouco template, sua fatura é próxima de zero. A partir de outubro, cada resposta ao cliente passa a ter custo. Vale simular o volume do último mês pela faixa de utilidade para saber o tamanho do impacto.

::aviso: <strong>Sobre a franquia de mensagens gratuitas:</strong> circula no mercado brasileiro que haverá uma franquia mensal de 1.000 mensagens de serviço gratuitas por número. Isso apareceu em comunicado da Meta a parceiros de tecnologia, mas <strong>até 08/09/2026 não constava na documentação pública de preços</strong>. Não planeje orçamento contando com ela até que apareça na página oficial.

## E o que o provedor cobra

A conta da Meta é uma. A do provedor é outra, e cada um monta a sua de um jeito.

**Direto na Meta:** você não paga nada além das mensagens. Em compensação, passa sozinho pela Business Manager verificada, pelo App Review com vídeo, e monta e mantém os próprios webhooks. Faz sentido se você tem time de engenharia e quer custo fixo zero.

**Por um provedor:** você paga uma camada de acesso e recebe o caminho pronto. O que mais varia entre provedores é **se existe markup nas mensagens**. Alguns revendem a mensagem da Meta com margem, outros repassam pelo custo. Essa é a pergunta a fazer em qualquer proposta, porque é ela que decide o custo em escala.

Na Datafy o modelo é assinatura por número, sem markup: as conversas você paga direto à Meta, pela tabela dela.

| Números conectados | Por número, por mês |
|---|---|
| 1 a 9 | R$ 49,90 |
| 10 a 49 | R$ 39,90 |
| 50 ou mais | R$ 29,90 |

## Como calcular o seu caso

Some três coisas:

1. **Mensagens de marketing no mês** vezes a faixa de marketing. Costuma ser a maior parte da conta em operação de vendas.
2. **Mensagens de utilidade e autenticação** vezes a faixa correspondente. A partir de outubro, inclua também as de serviço.
3. **A camada do provedor**, se você usar um. Na Datafy, o número de números conectados vezes a faixa da tabela acima.

Uma leitura de exemplo, com as faixas aproximadas: uma operação que dispara 2.000 mensagens de marketing por mês fica na ordem de R$ 640 a R$ 800 só de Meta. A mesma operação, se trocar metade desses disparos por utilidade bem categorizada, derruba bastante essa conta. Refaça o cálculo com a tabela oficial antes de decidir.

## Perguntas frequentes

### Mensagem recebida do cliente custa?

Não. A Meta cobra pela mensagem que você envia e que é entregue, não pela que você recebe.

### A cobrança é no envio ou na entrega?

Na entrega. Mensagem que não chega ao destinatário não é cobrada.

### Template de suporte ao cliente é qual categoria?

Depende do conteúdo, e quem decide é a Meta na aprovação. Confirmação e atualização costumam sair como utilidade. Se tiver oferta ou convite, vira marketing e o preço muda.

### O que acontece se eu categorizar errado?

A Meta reclassifica. O template continua funcionando, mas passa a ser cobrado pela categoria correta.

### Ainda posso ser faturado em dólar?

Contas antigas sim, por enquanto. A migração para reais é obrigatória até 30 de junho de 2027, e a partir de 1º de julho de 2027 a Meta deixa de entregar mensagens de contas brasileiras que não migraram.

### Vale distribuir o atendimento entre mais números?

Só faz sentido se a franquia de mensagens de serviço se confirmar na documentação oficial, porque ela seria por número. Enquanto isso não aparece na página da Meta, não é base para decisão de arquitetura.

## Como decidir

Se o seu volume é baixo e você tem time de engenharia, ir direto na Meta é o mais barato. Se você opera vários números, ou não quer montar App Review e webhook, a camada de um provedor se paga em tempo de time. Nos dois casos a conta da Meta é a mesma: o que muda é quanto você paga para chegar até ela.

::cta: Antes de fechar orçamento, confira a tabela vigente | Abra a página de preços da Meta, selecione Brasil e BRL, e confirme os valores das categorias que você usa. As faixas deste texto são referência de mercado, não a fonte oficial.

## Leia também
- [API oficial vs não oficial do WhatsApp](/api-oficial-vs-nao-oficial-whatsapp-2026)
- [Migrar para API oficial sem perder o número](/migrar-para-api-oficial-sem-perder-o-numero)
- [O que é Tech Provider da Meta](/o-que-e-tech-provider-meta)
- [Webhook: receber mensagens em tempo real](/webhook-whatsapp-cloud-api-como-receber-mensagens)

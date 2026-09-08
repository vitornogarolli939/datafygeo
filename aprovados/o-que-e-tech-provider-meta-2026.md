---
title: "Tech Provider, Solution Partner e BSP: o que cada um significa na Meta"
description: "A diferença entre Tech Provider, Solution Partner (BSP) e conexão direta na Meta, o que cada caminho exige de você e como escolher."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "o-que-e-tech-provider-meta"
cluster: "oficial_vs_nao"
intent: "entendendo"
persona: "automacao, saas"
competitors: ["Twilio", "360dialog", "Gupshup"]
published: 2026-09-06
updated: 2026-09-08
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/solution-providers/overview
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/solution-providers/get-started-for-tech-providers
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/solution-providers/upgrade-to-tech-partner/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/
  - https://app.datafyapi.com.br/
internal_links:
  - /api-oficial-vs-nao-oficial-whatsapp-2026
  - /coexistencia-whatsapp-api-oficial-app-celular
  - /whatsapp-api-oficial-chatwoot
  - /quanto-custa-whatsapp-business-api-brasil-2026
  - /migrar-para-api-oficial-sem-perder-o-numero
status: aprovado
---

# Tech Provider, Solution Partner e BSP: o que cada um significa na Meta

**Última atualização: 08/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** a Meta tem três papéis para quem oferece a WhatsApp Business Platform a terceiros. **Solution Partner** é o que o mercado chama de BSP: tem linha de crédito e fatura o cliente. **Tech Provider** oferece o mesmo acesso técnico, mas sem linha de crédito, então a Meta cobra o cliente diretamente. **Tech Partner** é o Tech Provider que também virou Meta Business Partner. A diferença prática entre eles é quase toda de faturamento e de selo comercial, não de capacidade técnica.

Vale desinflar o termo desde já, porque o mercado vende Tech Provider como se fosse um selo raro: o caminho é **público e self-service**. Qualquer empresa que passe pelo App Review com as permissões certas vira Tech Provider. Não há cota, nem exclusividade por país.

::numeros: 3 papéis|Solution Partner, Tech Provider e Tech Partner ;; 0|linha de crédito no Tech Provider: a Meta fatura o cliente direto ;; 2 permissões|whatsapp_business_messaging e whatsapp_business_management ;; 180 dias|de histórico que a coexistência sincroniza

## Principais pontos
- **Solution Partner** é o papel com linha de crédito: ele fatura o cliente, é Meta Business Partner e participa dos programas comerciais da Meta ([visão geral dos papéis](https://developers.facebook.com/documentation/business-messaging/whatsapp/solution-providers/overview)).
- **Tech Provider** entrega o mesmo acesso técnico, mas sem linha de crédito. O cliente cadastra o próprio meio de pagamento e a Meta cobra dele.
- Virar Tech Provider é [um processo aberto](https://developers.facebook.com/documentation/business-messaging/whatsapp/solution-providers/get-started-for-tech-providers): app na Meta, verificação de empresa e App Review com vídeos, pedindo acesso avançado a `whatsapp_business_messaging` e `whatsapp_business_management`.
- O que o papel habilita de verdade: **Embedded Signup**, para o cliente conectar o número dentro do seu produto, e **coexistência**, que a Meta restringe a Solution Partner e Tech Provider.
- Nenhum papel dá imunidade a banimento. Se o número cair por conduta, o provedor ajuda a montar o recurso, mas quem decide é a Meta.

::diagrama: tech-provider-badge

## Os três papéis, lado a lado

| | Solution Partner | Tech Provider | Tech Partner |
|---|---|---|---|
| Linha de crédito na Meta | Sim | Não | Não |
| Quem fatura o cliente | O parceiro | A Meta, direto | A Meta, direto |
| É Meta Business Partner | Sim | Não | Sim |
| Habilita Embedded Signup | Sim | Sim | Sim |
| Pode oferecer coexistência | Sim | Sim | Sim |
| Como se torna | Processo comercial com a Meta | App Review, self-service | Tech Provider que sobe de nível |

O termo **BSP** não é da documentação atual: é como o mercado ainda chama o Solution Partner. Se um fornecedor se apresenta como BSP, o que ele está dizendo é que fatura você e tem crédito com a Meta.

## Os caminhos para usar a API oficial

### Direto na Meta

Você cria o app, passa pela verificação de empresa, submete ao App Review e hospeda os próprios webhooks. Você é o responsável por tudo.

**A favor:** controle total, sem camada intermediária, sem custo fixo por número.
**Contra:** o App Review leva tempo e exige vídeo de demonstração. Toda a infraestrutura de webhook é sua.
**Para quem:** time de engenharia dedicado, volume alto, quem quer virar Tech Provider por estratégia.

### Por um Tech Provider

Você conecta o número usando a sua própria Business Manager, e o provedor já chega com as permissões aprovadas.

**A favor:** não passa por App Review, o número conecta em minutos, e o Embedded Signup e a coexistência vêm habilitados.
**Contra:** existe uma camada de acesso a pagar, e a disponibilidade do seu envio passa a depender de mais um serviço no caminho.
**Para quem:** SaaS que conecta números de clientes, agência, quem quer produção rápida.

### Por um Solution Partner

Mesma coisa do ponto de vista técnico, com uma diferença comercial: ele fatura você, em vez de a Meta cobrar direto. Alguns também revendem a mensagem com margem.

**A favor:** uma fatura só, e suporte comercial estruturado.
**Contra:** é onde costuma aparecer markup na mensagem. Pergunte isso explicitamente.
**Para quem:** empresa que prefere fornecedor único e nota fiscal local.

## A pergunta que separa as propostas

Em qualquer proposta, três perguntas resolvem a comparação:

1. **O número fica na minha Business Manager?** Se a resposta for não, você não é dono do ativo e a troca de fornecedor fica cara.
2. **Existe markup na mensagem, ou eu pago a tabela da Meta?** É isso que decide o custo em escala.
3. **Coexistência e Embedded Signup estão incluídos?** Dependem do papel do provedor na Meta, não do plano que ele te vende.

## Sobre proteção de dados

Aqui vale precisão, porque circula muita simplificação. Contratar um provedor **não transfere a sua responsabilidade** sobre os dados dos seus clientes. Na estrutura da LGPD, quem decide a finalidade do tratamento continua respondendo por ele. O provedor atua no tratamento em nome de quem contratou, e isso é definido em contrato, não pelo papel que ele tem na Meta.

O que o papel na Meta define é outra coisa: quem tem contrato com a Meta, quem responde por violar as políticas da plataforma, e quem pode ser descredenciado. São dois planos diferentes, e vale não confundir um com o outro ao ler proposta comercial.

## Embedded Signup

O cliente conecta o próprio número dentro do seu aplicativo, sem sair dele. É o fluxo que a Meta oferece a quem passou pelo App Review com as permissões de mensageria e de gerenciamento.

Na prática: você tem um SaaS de automação, o cliente clica em "Conectar WhatsApp", um pop-up controlado pela Meta abre, ele autoriza, e volta para o seu produto com o número já conectado. Sem você pedir acesso à Business Manager dele, e sem ele passar por App Review.

É o recurso que viabiliza produto multi-cliente. Sem ele, cada cliente teria que percorrer o processo da Meta por conta própria.

## Perguntas frequentes

### Tech Provider é mais seguro que Solution Partner?

Não é uma questão de segurança, e sim de faturamento. Os dois têm o mesmo acesso técnico. No Tech Provider a Meta cobra você direto, o que costuma significar menos chance de markup embutido.

### Se o meu provedor perder o status, eu perco o número?

Não. O número está registrado na sua Business Manager. Você o reconecta em outro provedor, ou direto na Meta. É por isso que a primeira pergunta da lista acima importa tanto.

### Preciso ser Tech Provider para usar a API oficial na minha empresa?

Não. O papel serve para quem oferece a plataforma **a terceiros**. Para usar no próprio negócio, basta conectar o seu número, seja direto na Meta, seja por um provedor.

### Quanto tempo leva para virar Tech Provider?

Depende do App Review da Meta, que é a etapa mais imprevisível. O trabalho maior costuma ser preparar os vídeos de demonstração exigidos e passar pela verificação de empresa.

### Ser Tech Provider evita banimento dos meus números?

Não. Nenhum papel na Meta muda as regras de conduta. Prospecção sem template, engajamento baixo e nicho proibido derrubam número igual, com API oficial e template aprovado.

## Como decidir

Se você usa WhatsApp só no seu próprio negócio, o papel do provedor importa pouco: olhe preço, suporte e se o número fica na sua Business Manager. Se você constrói produto que conecta números de clientes, aí o papel decide o que dá para construir, porque Embedded Signup e coexistência dependem dele.

::cta: Faça as três perguntas antes de assinar | O número fica na minha Business Manager? Existe markup na mensagem? Embedded Signup e coexistência estão incluídos? As respostas separam as propostas mais rápido que qualquer tabela de preço.

## Leia também
- [API oficial vs não oficial do WhatsApp](/api-oficial-vs-nao-oficial-whatsapp-2026)
- [Coexistência: API e aplicativo no mesmo número](/coexistencia-whatsapp-api-oficial-app-celular)
- [Quanto custa a WhatsApp Business API no Brasil](/quanto-custa-whatsapp-business-api-brasil-2026)
- [Migrar para API oficial sem perder o número](/migrar-para-api-oficial-sem-perder-o-numero)

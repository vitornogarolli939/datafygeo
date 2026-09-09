---
title: "Meu cliente consegue conectar o WhatsApp dele sozinho no meu SaaS?"
description: "Consegue, pelo Embedded Signup. É o recurso que decide se o seu produto escala ou se você vai pedir acesso à conta de cada cliente."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "cliente-conecta-o-whatsapp-dele-no-meu-saas"
cluster: "saas"
hero: "camadas"
intent: "decidindo"
persona: "saas"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/solution-providers/overview
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/solution-providers/get-started-for-tech-providers
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/
  - https://developers.facebook.com/docs/whatsapp/throughput
  - https://app.datafyapi.com.br/docs
internal_links:
  - /o-que-e-tech-provider-meta
  - /coexistencia-whatsapp-api-oficial-app-celular
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /quanto-custa-whatsapp-business-api-brasil-2026
  - /api-oficial-vs-nao-oficial-whatsapp-2026
status: aprovado
---

# Meu cliente consegue conectar o WhatsApp dele sozinho no meu SaaS?

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** consegue, e o recurso se chama **Embedded Signup**. O cliente clica em "Conectar WhatsApp" dentro do seu produto, um fluxo controlado pela Meta abre por cima, ele autoriza, e volta para o seu app com o número já conectado. Você não pede login dele, não pede acesso à Business Manager dele, e ele não passa por App Review.

Sem isso, cada cliente teria que percorrer o processo da Meta por conta própria, ou te dar acesso à conta dele. Nenhum dos dois escala, e é por isso que essa é a pergunta que define a arquitetura de um SaaS multi-cliente.

::numeros: 1 clique|para o cliente iniciar, dentro do seu produto ;; 0|acessos à conta dele que você precisa pedir ;; 2 permissões|que o seu app precisa ter aprovadas ;; 1 número|por cliente, cada um na Business Manager dele

## Principais pontos
- O fluxo é **controlado pela Meta**, não por você. Isso é o que faz o cliente confiar: ele autoriza dentro de uma tela da própria Meta, e não digitando senha no seu sistema.
- Depende do **papel do seu fornecedor na Meta**. Só quem passou pelo App Review com as permissões `whatsapp_business_messaging` e `whatsapp_business_management` pode oferecer o fluxo ([como se tornar Tech Provider](https://developers.facebook.com/documentation/business-messaging/whatsapp/solution-providers/get-started-for-tech-providers)).
- **O número fica na Business Manager do cliente**, não na sua. Isso é bom para ele e é a resposta certa quando alguém pergunta de quem é o ativo.
- Se o cliente também quer continuar atendendo pelo celular, o fluxo precisa ser o de **coexistência**, e essa escolha é feita na hora da conexão.
- Cada número conectado tem **webhook próprio a tratar**, e é aí que mora o trabalho de engenharia do multi-cliente.

::diagrama: tech-provider-badge

## O que o cliente vê

Do lado dele, são poucos passos e nenhum deles envolve o seu suporte:

1. Clica no botão dentro do seu produto.
2. Abre uma janela da Meta, onde ele entra com a conta dele do Facebook.
3. Escolhe ou cria a Business Manager.
4. Informa o número e confirma a posse, por SMS ou ligação.
5. Autoriza o seu aplicativo.
6. Volta para o seu produto, conectado.

O que ele não faz: não cria aplicativo na Meta, não grava vídeo de demonstração, não espera App Review, não te manda print de token.

## O que você precisa ter do seu lado

**As permissões aprovadas.** É o requisito de fundo. O caminho para virar Tech Provider é [público e self-service](https://developers.facebook.com/documentation/business-messaging/whatsapp/solution-providers/get-started-for-tech-providers): criar o app, passar pela verificação de empresa e submeter ao App Review pedindo acesso avançado às duas permissões. Não há cota nem exclusividade por país. O que existe é o tempo e o trabalho de passar por isso.

**Ou um fornecedor que já tenha.** É o atalho: usar um provedor que seja Solution Partner ou Tech Provider e expor o fluxo dele dentro do seu produto. Você troca o esforço de aprovação por uma camada de fornecedor no caminho.

**Webhook que aguenta muitos números.** Depois que dez clientes conectam, dez números mandam evento para o seu endpoint. Você precisa saber de quem é cada mensagem, e isso vem no `phone_number_id` de cada payload.

**Um jeito de guardar credencial por cliente.** Cada número tem o seu, e misturar isso é o tipo de bug que só aparece em produção com cliente real.

## As três perguntas que decidem a proposta do fornecedor

Se você vai usar um provedor em vez de virar Tech Provider, essas três respostas separam qualquer proposta:

1. **O número fica na Business Manager do meu cliente?** Se ficar na do fornecedor, seu cliente não é dono do ativo, e trocar de fornecedor depois vira migração de número, não troca de URL.
2. **Existe markup na mensagem, ou eu pago a tabela da Meta?** É o que decide o custo quando você tiver cem clientes, não dois.
3. **Embedded Signup e coexistência estão incluídos?** Os dois dependem do papel do fornecedor na Meta, não do plano que ele te vende.

## O que costuma dar errado

**Achar que o Embedded Signup resolve o webhook.** Ele resolve a conexão. O roteamento de evento por cliente continua sendo trabalho seu.

**Não decidir a coexistência.** Se o cliente atende pelo celular e o número for conectado sem coexistência, ele **perde o aplicativo**. Isso gera cancelamento no primeiro dia, e desfazer exige refazer a conexão.

**Esquecer a forma de pagamento.** O número conecta, mas não envia até que exista método de pagamento cadastrado na conta. Vale avisar no seu onboarding, senão vira chamado de suporte com o cliente achando que o seu produto está quebrado.

**Ignorar o limite por número.** São 80 mensagens por segundo por número, e 20 se ele estiver em coexistência. Em multi-cliente isso raramente incomoda, porque o volume se distribui, mas um cliente grande sozinho pode bater no teto.

## Perguntas frequentes

### Preciso ser Tech Provider para oferecer isso?

Você ou o seu fornecedor. O fluxo depende de permissões aprovadas em App Review, e alguém na cadeia precisa tê-las.

### O número fica comigo ou com o cliente?

Com ele, na Business Manager dele. Você tem acesso para operar, e é isso que faz a troca de fornecedor ser simples depois.

### Se o cliente sair do meu SaaS, o que acontece?

Ele leva o número, porque está na conta dele. É a resposta honesta a dar quando perguntarem, e ela costuma ajudar a fechar contrato, não a perder.

### O cliente precisa ter CNPJ?

Precisa de uma Business Manager, e dá para criar na hora no próprio fluxo. A verificação da empresa entra depois, quando ele quiser subir o limite de envio.

### Quem paga as mensagens dele?

Depende do papel do seu fornecedor na Meta. Com Tech Provider, a Meta cobra o cliente diretamente. Com Solution Partner, o parceiro fatura. Vale saber qual dos dois é o seu, porque muda o seu modelo de cobrança.

### Dá para conectar vários números do mesmo cliente?

Dá. Cada número é uma conexão, e cada um manda evento com o próprio identificador.

## Como decidir

Se você vende para uma empresa só, ou para poucas, dá para viver sem: cada cliente conecta por conta própria e te passa a credencial. Feio, mas funciona.

Se você vende SaaS para dezenas ou centenas de clientes, o Embedded Signup deixa de ser recurso e vira requisito. Sem ele, o seu onboarding tem uma etapa manual que não escala, e você acaba pedindo acesso a conta de cliente, que é o tipo de coisa que trava venda em empresa maior.

::cta: Antes de escolher o fornecedor, faça as três perguntas | O número fica na Business Manager do meu cliente? Existe markup na mensagem? Embedded Signup e coexistência estão incluídos? As respostas separam as propostas mais rápido que qualquer tabela de preço.

## Leia também
- [Tech Provider, Solution Partner e BSP: o que cada um significa](/o-que-e-tech-provider-meta)
- [Coexistência: API e aplicativo no mesmo número](/coexistencia-whatsapp-api-oficial-app-celular)
- [Webhook: receber mensagens em tempo real](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [Quanto custa a WhatsApp Business API no Brasil](/quanto-custa-whatsapp-business-api-brasil-2026)

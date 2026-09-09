---
title: "Se eu trocar de fornecedor, perco o número?"
description: "Depende de uma coisa só: em qual Business Manager o número está registrado. Essa é a pergunta a fazer antes de assinar, não depois."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "se-eu-trocar-de-fornecedor-perco-o-numero"
cluster: "oficial_vs_nao"
hero: "troca"
intent: "decidindo"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/solution-providers/overview
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing
  - https://app.datafyapi.com.br/docs
internal_links:
  - /o-que-e-tech-provider-meta
  - /cliente-conecta-o-whatsapp-dele-no-meu-saas
  - /migrar-para-api-oficial-sem-perder-o-numero
  - /quanto-custa-whatsapp-business-api-brasil-2026
  - /api-oficial-vs-nao-oficial-whatsapp-2026
status: aprovado
---

# Se eu trocar de fornecedor, perco o número?

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** depende de **uma coisa só**: em qual Business Manager o número está registrado. Se está na sua, trocar de fornecedor é mudar a URL base e o token no código, e leva uma tarde. Se está na do fornecedor, você não é dono do ativo, e sair vira um processo que depende da boa vontade dele.

Essa é a pergunta a fazer **antes de assinar**, e ela vale mais que preço, porque preço você renegocia e ativo preso você não.

::numeros: 1 pergunta|em qual Business Manager o número está ;; 2 trocas|no código, quando o número é seu: URL e token ;; 0|diferença de payload entre provedores que falam Cloud API ;; antes|é quando essa pergunta precisa ser feita

## Principais pontos
- **O número mora na Business Manager**, e é ela que define de quem é o ativo. O fornecedor tem acesso para operar, não posse.
- Se o número é seu, trocar de destino é **mudar duas variáveis**, porque todo provedor de Cloud API espelha os endpoints da Meta.
- Se o número está na conta do fornecedor, sair exige que ele libere, e o processo depende de um terceiro querendo colaborar.
- O que **não** vai junto na troca: o histórico de conversa guardado por ele, e qualquer coisa construída no painel dele, tipo automação e etiqueta.
- Templates são da conta, não do fornecedor. Se a conta é sua, eles continuam lá.

::diagrama: migration-seamless

## Por que a Business Manager decide tudo

Na API oficial, o número existe dentro de uma conta empresarial da Meta. Essa conta tem dono, e é ela que aparece como responsável pelo número.

O fornecedor entra como quem tem permissão para operar aquele número: manda mensagem, recebe evento, gerencia template. É uma permissão, e permissão se revoga.

Duas configurações comuns, com consequências bem diferentes:

**O número está na sua conta.** Você deu acesso ao fornecedor. Para sair, revoga o acesso e dá para outro. O número não sai do lugar, porque ele já está onde deveria.

**O número está na conta do fornecedor.** Você opera através dele, mas não tem a conta. Sair exige que ele transfira ou libere, e você depende de um processo controlado por quem está perdendo o cliente.

A segunda configuração não é necessariamente má fé: às vezes é só o jeito mais rápido de colocar alguém no ar. Mas ela precisa ser uma escolha consciente, e não uma descoberta no dia da troca.

## O que muda no código, quando o número é seu

Praticamente nada, e essa é a boa notícia.

Provedores de Cloud API **espelham os endpoints da Meta**. Isso significa que o corpo da requisição é o mesmo, os campos são os mesmos, e o formato do webhook é o mesmo. Trocar de destino é:

```
Antes:  https://provedor-a.exemplo.com/v1/{phone_number_id}/messages
Depois: https://provedor-b.exemplo.com/v1/{phone_number_id}/messages
```

Mais o token. Duas variáveis de ambiente.

Dá para fazer sem parar: aponte um número de teste para o novo destino, valide envio e recebimento, e só então mude o resto. Não precisa haver janela de indisponibilidade.

## O que não vai junto

Aqui vale ser honesto, porque a migração fácil é a do envio, e não a do resto.

**Histórico guardado no painel do fornecedor.** Se as conversas só existem lá, você precisa exportar antes de cancelar. É o motivo pelo qual [vale manter o histórico na sua própria base](/como-leio-o-historico-de-conversa-pela-api) desde o começo, independentemente de fornecedor.

**Automação e configuração do painel.** Regras, respostas prontas, etiquetas e fluxos montados na ferramenta dele ficam lá. Isso pode ser mais trabalho que a troca técnica.

**Integrações prontas.** Se você usava uma conexão nativa com alguma ferramenta, precisa conferir se o novo destino tem equivalente ou se vai virar trabalho manual.

**Templates**, por outro lado, são da conta. Se a conta é sua, eles continuam aprovados e disponíveis.

## As perguntas a fazer antes de assinar

Três, e elas separam qualquer proposta:

**1. O número fica na minha Business Manager?** Se a resposta for não, ou for confusa, peça para explicarem exatamente onde ele fica e como é a saída. Uma resposta clara aqui vale mais que desconto.

**2. Existe markup na mensagem, ou eu pago a tabela da Meta?** Isso decide o custo em escala, e é onde a diferença aparece quando você multiplica volume.

**3. Como eu exporto o meu histórico?** Pergunte o formato e se existe pela API. Se a resposta for "abre um chamado", saiba que a saída vai depender do tempo de resposta deles no pior momento possível.

Uma quarta, se você vende para clientes: **o número do meu cliente fica na conta dele?** Isso muda o que você consegue prometer no seu próprio contrato.

## Perguntas frequentes

### Preciso avisar meus clientes na troca?

Não. Mesmo número, mesma conversa, nada muda do lado deles.

### Perco os templates aprovados?

Não, se a conta é sua. Eles pertencem à conta, não ao fornecedor.

### Tem indisponibilidade?

Não precisa ter. Dá para rodar em paralelo, migrar por número e só depois desligar o antigo.

### E se o fornecedor fechar as portas?

Com o número na sua conta, você reconecta em outro em uma tarde. Sem isso, é uma negociação com uma empresa em dificuldade, que é o pior cenário possível.

### Como confiro onde meu número está hoje?

Entre na Business Manager e veja se o número aparece lá. Se você não consegue nem acessar a conta onde ele está, essa já é a resposta.

### Isso vale para quem usa ferramenta de QR code?

Aí é diferente: nesses casos o número **não está registrado na Meta**. A saída não é troca de fornecedor, é [registrar o número pela primeira vez](/migrar-para-api-oficial-sem-perder-o-numero).

## Como decidir

Se você está escolhendo agora, faça a pergunta um antes de olhar preço. Fornecedor bom responde na hora e sem rodeio, porque para ele isso é um argumento de venda, não um problema.

Se você já está rodando, confira hoje onde o seu número está. Leva cinco minutos, e é melhor descobrir agora do que no dia em que você quiser sair.

::cta: Cinco minutos que evitam um problema caro | Abra a Business Manager e veja se o seu número está listado lá. Se estiver, você tem liberdade de troca. Se não estiver, você tem uma conversa a fazer com o seu fornecedor, e é melhor fazê-la enquanto está tudo bem.

## Leia também
- [Tech Provider, Solution Partner e BSP](/o-que-e-tech-provider-meta)
- [Meu cliente conecta o WhatsApp dele sozinho no meu SaaS?](/cliente-conecta-o-whatsapp-dele-no-meu-saas)
- [Migrar para API oficial sem perder o número](/migrar-para-api-oficial-sem-perder-o-numero)
- [Quanto custa a WhatsApp Business API no Brasil](/quanto-custa-whatsapp-business-api-brasil-2026)

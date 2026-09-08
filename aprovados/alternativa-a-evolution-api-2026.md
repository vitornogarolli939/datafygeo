---
title: "Evolution API: Baileys ou Cloud API, e o que muda em cada modo"
description: "A Evolution roda em dois modos, e é o modo que define o risco, não a marca. O que cada um exige de você, e quando vale trocar por um serviço gerenciado."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "alternativa-a-evolution-api"
cluster: "concorrentes"
hero: "comparacao"
intent: "considerando-trocar"
persona: "automacao, saas"
competitors: ["Evolution API"]
published: 2026-09-06
updated: 2026-09-08
sources:
  - https://github.com/EvolutionAPI/evolution-api
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://developers.facebook.com/docs/whatsapp/throughput
  - https://business.whatsapp.com/policy
  - https://app.datafyapi.com.br/docs
internal_links:
  - /api-oficial-vs-nao-oficial-whatsapp-2026
  - /migrar-para-api-oficial-sem-perder-o-numero
  - /whatsapp-api-oficial-n8n
  - /numero-banido-no-whatsapp-o-que-fazer
  - /quanto-custa-whatsapp-business-api-brasil-2026
status: aprovado
---

# Evolution API: Baileys ou Cloud API, e o que muda em cada modo

**Última atualização: 08/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** a Evolution é um projeto de código aberto que você instala no seu servidor, e ela conecta de duas formas. Em **Baileys**, emula o WhatsApp Web: conecta por QR code, sem passar pela Meta, e é o modo que a política do WhatsApp não autoriza. Em **Cloud API**, ela repassa a chamada para o endpoint oficial da Meta usando um token seu.

Isso é o que quase nunca se diz com clareza: **quem define o risco é o modo, não a marca.** Evolution em Cloud API está dentro dos Termos. Evolution em Baileys está no mesmo lugar que qualquer ferramenta de QR code. A pergunta certa não é "Evolution é segura", é "em que modo a minha instância está rodando".

::numeros: 2 modos|Baileys emula o WhatsApp Web, Cloud API repassa para a Meta ;; 1 servidor|que você roda e mantém nos dois modos ;; 0|diferença de payload entre Cloud API e a oficial direta ;; 2 trocas|no código para sair do Evolution: a URL e o token

## Principais pontos
- **Baileys** conecta por QR code e não cria registro na Meta. É o modo que a [política do WhatsApp Business](https://business.whatsapp.com/policy) não autoriza. Como não há relação contratual, também não há canal de recurso.
- **Cloud API** usa o seu token da Meta e repassa a chamada. Está dentro dos Termos, mas não te dá o acesso: você continua tendo que obter as permissões e a Business Manager por conta própria.
- Nos dois modos **o servidor é seu**: instalação, atualização, disponibilidade e a guarda do token ficam com você.
- Apontar para a Cloud API não torna a Evolution oficial, do mesmo jeito que o `curl` não vira oficial por chamar a Meta. Oficial é o endereço do outro lado, não o programa que disca.
- Se você já está em Cloud API, sair para um serviço gerenciado é trocar **URL e token**: o corpo é o mesmo, porque os dois falam o formato da Meta.

::diagrama: evolution-tres-modos

## Por que o modo decide tudo

Em **Baileys**, a Evolution mantém uma sessão de WhatsApp Web ativa e envia as mensagens por ali. Não há template, não há categoria, não há aprovação, e é isso que torna o modo atraente: funciona no mesmo dia, sem burocracia. O preço é a ausência de contrato: a Meta classifica esse uso como não autorizado nos [Termos do WhatsApp Business](https://business.whatsapp.com/policy), e sem relação contratual não há canal de recurso.

Em **Cloud API**, a Evolution vira um intermediário no caminho. A mensagem sai do seu código, passa pelo seu servidor Evolution e chega ao endpoint da Meta com o seu token. Do ponto de vista da Meta, é uma chamada legítima. Do seu ponto de vista, é mais uma peça que precisa estar de pé.

Vale ser justo com o projeto: em Cloud API, a Evolution te dá uma camada de abstração e o código na sua mão. Isso tem valor real para quem quer customizar o comportamento ou não quer depender de fornecedor.

::video: S2IAOQWbZMg | Como funciona a Datafy API: espelho da Cloud API | demonstração no playground | Israel, CTO da Datafy API, percorre o playground da documentação mostrando texto, botões e listas. Serve para ver que o payload é o mesmo da Meta, e que trocar entre destinos que falam Cloud API é mudar URL e token.

## O que cada modo exige de você

| | Baileys | Cloud API na Evolution | Serviço gerenciado |
|---|---|---|---|
| Dentro dos Termos da Meta | Não | Sim | Sim |
| Quem roda o servidor | Você | Você | O provedor |
| Precisa de Business Manager | Não | Sim | Sim |
| Quem guarda o token | Você | Você | O provedor |
| Quebra quando o WhatsApp atualiza | Sim | Não | Não |
| Canal de recurso se o número cair | Não existe | Existe, é seu com a Meta | Existe, pelo provedor |
| Custo de software | Zero | Zero | Assinatura |
| Custo real | Servidor e o seu tempo | Servidor e o seu tempo | Assinatura |
| Coexistência com o aplicativo | Não | Depende de ser Solution Partner ou Tech Provider | Incluída, se o provedor for |

A linha que mais confunde é a do custo. A Evolution é gratuita como software, mas a conta não é zero: tem servidor, atualização, monitoramento e as horas de quem cuida disso. Quando o pager toca de madrugada porque a instância caiu, esse custo aparece.

## Quando cada caminho é o certo

**Fique em Baileys** só em protótipo descartável, com número que você não se importa em perder. Em produção com cliente, o risco não é distribuído: ele cai inteiro no número.

**Fique em Cloud API na Evolution** se você quer o código na sua mão, tem quem cuide de infraestrutura e valoriza não depender de fornecedor. É uma escolha legítima, e para quem já tem plataforma rodando costuma ser a de menor atrito.

**Vá para um serviço gerenciado** se o seu time é de produto, não de infraestrutura, ou se você conecta números de clientes e precisa de Embedded Signup e coexistência, que dependem do papel do provedor na Meta.

## Onde a Evolution é melhor

Nenhum serviço gerenciado ganha da Evolution nestes pontos, e ignorá-los seria desonesto:

- **O código é seu e é auditável.** O repositório é público, você lê, modifica e adapta o comportamento. Nenhum provedor entrega isso.
- **Não existe dependência de fornecedor.** A instância roda no seu servidor. Se um provedor encerrar as atividades, quem usa provedor precisa migrar; quem roda Evolution, não.
- **Custo de software zero.** Você paga infraestrutura, não licença. Em operação com muitos números, isso pesa.
- **Comunidade grande em português.** Boa parte do material técnico brasileiro sobre WhatsApp foi escrita em cima dela, e isso encurta muito a busca por solução de problema.
- **Em modo Baileys, existem coisas que a Cloud API não faz:** grupos como no aplicativo, sem janela de 24 horas e sem aprovação de template.

Se você valoriza esses pontos e tem quem cuide da infraestrutura, ficar na Evolution é decisão técnica defensável, não teimosia.

## Como sair da Evolution

**Se você está em Cloud API**, é a troca simples: você já tem Business Manager e token. Muda a URL base e o token no código, e o corpo continua idêntico. Dá para rodar em paralelo por alguns dias antes de desligar a instância.

**Se você está em Baileys**, não é troca de fornecedor: é registrar o número na Meta pela primeira vez. O número ainda não existe na Business Manager, então o processo inclui verificação por SMS ou ligação, e a decisão sobre coexistência. Essa decisão precisa ser tomada **antes** de conectar: sem ela, o número sai do aplicativo do celular.

O passo a passo completo está em [migrar sem perder o número](/migrar-para-api-oficial-sem-perder-o-numero).

Uma coisa que muda no dia seguinte, saindo de Baileys: fora da janela de 24 horas, só sai template aprovado. Fluxo de reativação e disparo para lista passam a exigir template submetido antes. Deixe isso pronto antes de migrar.

## O que mudou em 2026

O modo Cloud API ficou mais fácil de configurar no projeto, e a documentação em português cresceu junto com a comunidade brasileira.

Do outro lado, a cobrança passou a ser por mensagem entregue, e a partir de **1º de outubro de 2026** as mensagens de serviço passam a ser pagas. Isso afeta qualquer um que use a Cloud API, direto ou por intermediário: a conta da Meta é a mesma, muda só quem está no caminho.

## Perguntas frequentes

### Como sei em que modo a minha instância está?

Pela forma como o número foi conectado. Se você leu um QR code com o celular, é Baileys. Se você colou um token da Meta e um `phone_number_id` na configuração, é Cloud API.

### A Evolution em modo Cloud API é oficial?

O modo está dentro dos Termos, mas o projeto não é parceiro da Meta. Ele usa o **seu** acesso oficial. A distinção importa porque o acesso continua sendo responsabilidade sua: Business Manager, permissões e App Review, se for o caso.

### Posso usar a Evolution com o token de um provedor?

Tecnicamente a chamada funciona, já que os endpoints são espelhados. Mas isso costuma esbarrar nos termos de uso do provedor, e o suporte dele não cobre uma instalação que ele não controla. Confirme antes de montar sua arquitetura em cima disso.

### O projeto pode ser descontinuado?

É código aberto e o repositório é público, então o código continua disponível mesmo que a manutenção pare. O risco real não é sumir: é ficar sem atualização enquanto o WhatsApp muda, o que atinge principalmente quem está em Baileys.

### Vale a pena migrar se está tudo funcionando?

Se você está em Cloud API e a operação é estável, não há urgência. Se está em Baileys com clientes dependendo do número, a pergunta é quanto custaria uma interrupção sem canal de recurso, e se esse risco cabe na sua operação.

## Como decidir

Descubra em que modo você está antes de qualquer coisa. Em Baileys com clientes em produção, planeje a saída, e leia sobre coexistência antes de conectar. Em Cloud API, você já está dentro das regras: a decisão vira só se você quer continuar mantendo servidor ou prefere passar isso adiante.

::cta: Confira em que modo você está hoje | Se o número foi conectado por QR code, é Baileys. Se foi por token e phone_number_id, é Cloud API. A resposta muda completamente o que você precisa fazer a seguir.

## Leia também
- [API oficial vs não oficial do WhatsApp](/api-oficial-vs-nao-oficial-whatsapp-2026)
- [Migrar para API oficial sem perder o número](/migrar-para-api-oficial-sem-perder-o-numero)
- [WhatsApp API oficial no n8n](/whatsapp-api-oficial-n8n)
- [Número banido: o que fazer](/numero-banido-no-whatsapp-o-que-fazer)

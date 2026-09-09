---
title: "A Meta cobra por mensagem de agente de IA no Brasil (e só aqui)"
description: "Desde março de 2026 a Meta cobra provedores de IA por mensagem livre entregue no WhatsApp. Foi revogado na Europa em maio. No Brasil continua valendo."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "cobranca-de-ai-provider-no-brasil"
cluster: "custo"
hero: "preco"
intent: "decidindo"
persona: "saas, automacao, agentes"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/ai-providers
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing
  - https://ec.europa.eu/commission/presscorner/detail/en/ip_26_805
  - https://app.datafyapi.com.br/docs
internal_links:
  - /quanto-custa-whatsapp-business-api-brasil-2026
  - /api-oficial-vs-nao-oficial-whatsapp-2026
  - /whatsapp-api-oficial-n8n
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /o-que-e-tech-provider-meta
status: aprovado
pendencias: ["[VERIFICAR] conferir a política de AI Providers a cada atualização, porque o escopo geográfico já mudou duas vezes em 2026"]
---

# A Meta cobra por mensagem de agente de IA no Brasil (e só aqui)

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** desde 11 de março de 2026 a Meta cobra o que ela chama de **AI Providers** por cada mensagem livre entregue a um usuário do WhatsApp. A cobrança começou na Itália em fevereiro, se estendeu ao Brasil e a 29 mercados europeus em março, e foi **revogada para a União Europeia e o Espaço Econômico Europeu em 13 de maio de 2026**. No Brasil ela continua.

Isso muda a conta de quem monta agente de IA no WhatsApp, porque atinge justamente a mensagem que sempre foi gratuita: a resposta em texto livre dentro da janela de atendimento. E cada resposta da conversa é cobrada separadamente.

::numeros: 11 mar 2026|quando a cobrança passou a valer no Brasil ;; 13 mai 2026|quando a Meta parou de cobrar na União Europeia ;; 1|cobrança por resposta, não por conversa ;; AI_BOT|a categoria que aparece nos relatórios quando isso se aplica a você

## Principais pontos
- A cobrança recai sobre **mensagem não-template**, ou seja, o texto livre que você manda dentro da janela de 24 horas. É o tipo de mensagem que um agente mais usa.
- **Cada resposta é cobrada separadamente.** Uma conversa de dez turnos gera dez cobranças, e não uma.
- O Brasil ficou de fora da revogação de maio. Hoje é o mercado grande em que a regra ainda pesa.
- Dá para verificar se isso se aplica a você olhando os dados: a categoria **`AI_BOT`** aparece na API de análise, e o webhook marca a mensagem com `"category": "general_purpose_ai"` e `"billable": true`.
- Quem contrata um agente de terceiro precisa perguntar **quem é o AI Provider na relação**, porque isso decide de quem é a conta.

::diagrama: preço-comparacao

## Quem a Meta considera um AI Provider

A [definição está na política](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/ai-providers) e é ampla: provedores e desenvolvedores de tecnologias de inteligência artificial ou aprendizado de máquina, incluindo modelos de linguagem, plataformas de IA generativa e assistentes de propósito geral, que ofereçam determinados serviços na plataforma.

O que essa definição faz na prática é separar dois mundos que parecem iguais de fora:

**Assistente de propósito geral.** Um serviço em que o próprio produto é a IA, e o usuário conversa com ela sobre o que quiser. É esse o alvo da política.

**Automação de atendimento de uma empresa.** O restaurante que responde pedido, a clínica que confirma consulta, o SaaS que tira dúvida sobre a própria fatura. Aqui a IA é meio, não é o produto, e o enquadramento é diferente.

A fronteira não é sempre óbvia, e quem opera perto dela precisa ler a política inteira antes de orçar. Se o seu produto se apresenta como "converse com nossa IA", vale assumir que a discussão vai aparecer.

## Por que existe essa cobrança

Vale entender o contexto, porque ele explica por que a regra mudou duas vezes em quatro meses.

Em outubro de 2025 a Meta atualizou os termos da plataforma para restringir provedores de modelos de IA que quisessem distribuir assistentes ali quando a IA fosse a função principal, e não incidental. Em fevereiro de 2026 a Comissão Europeia [formalizou uma acusação](https://ec.europa.eu/commission/presscorner/detail/en/ip_26_805) contra a Meta por bloquear assistentes concorrentes no WhatsApp.

O desenho que surgiu depois disso foi: liberar os assistentes de terceiros onde havia obrigação legal de liberar, e cobrar por isso. Foi assim que a cobrança nasceu na Itália em 16 de fevereiro, se espalhou pela Europa e pelo Brasil em 11 de março, e depois foi retirada da Europa em 13 de maio.

O Brasil entrou na leva de março e não saiu na de maio. É esse o estado atual.

## Como saber se isso se aplica a você

Não dependa de interpretação: olhe os dados que a própria Meta devolve.

**No relatório.** A API de análise passou a ter a categoria `AI_BOT`. Se o seu tráfego aparece ali, o enquadramento já aconteceu.

**No webhook.** A mensagem cobrada chega marcada:

```json
{
  "category": "general_purpose_ai",
  "billable": true
}
```

Vale ligar um alerta nesses dois campos antes de escalar volume. É a diferença entre descobrir no relatório da semana e descobrir na fatura do mês.

## O que fazer com essa informação

**Se você monta automação de atendimento para uma empresa**, o caminho normal continua: a IA é meio para responder o cliente daquela empresa, e a cobrança que você acompanha é a de template e, a partir de outubro, a de mensagem de serviço.

**Se você vende um assistente de propósito geral**, inclua essa linha no cálculo desde o começo, porque ela incide sobre o turno de conversa, que é justamente o que um assistente faz muito.

**Se você usa uma plataforma de terceiro que embute IA**, pergunte quem é o AI Provider na relação e de quem é a conta. Alguns fornecedores embutem provedores de modelo na própria cadeia sem deixar isso claro no contrato.

**Em qualquer caso, projete o custo por turno, não por conversa.** É a mudança mental que essa política exige.

::aviso: <strong>Essa regra já mudou duas vezes em 2026.</strong> Começou na Itália em fevereiro, chegou ao Brasil em março, saiu da Europa em maio. Antes de fechar orçamento longo, abra a <a href="https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/ai-providers">política de preços para AI Providers</a> e confirme o escopo geográfico vigente.

## A outra conta que entra em outubro

Enquanto essa política estiver valendo aqui, ela se soma a uma mudança que atinge todo mundo: a partir de **1º de outubro de 2026** as mensagens de serviço passam a ser cobradas, e as de utilidade enviadas dentro de uma janela aberta também.

Para um agente de IA, os dois efeitos batem no mesmo lugar. Antes, responder dentro da janela era gratuito, e o custo era só o token do modelo. A partir de outubro, cada resposta soma o preço da mensagem. Se ainda houver a cobrança de AI Provider, soma as duas.

Vale refazer a conta do último mês com essas linhas antes de outubro, e não depois.

## E o agente da própria Meta

Em 3 de junho de 2026 a Meta lançou globalmente o **Meta Business Agent**, e desde 1º de agosto ele é cobrado por token, a **US$ 2,00 por milhão de tokens**. Pela estimativa da própria documentação, algo entre 20 mil e 25 mil tokens por mensagem, o que dá na ordem de US$ 0,04 a US$ 0,05 por mensagem, já incluindo a entrega.

Isso é relevante por dois motivos. Primeiro, porque cria um ponto de comparação de preço para quem vende agente. Segundo, porque mostra o modelo mental para onde a plataforma está indo: cobrança por uso de IA, e não só por mensagem.

## Perguntas frequentes

### Isso vale para qualquer bot no WhatsApp?

Não. A política mira provedores de tecnologia de IA que oferecem assistentes na plataforma. Automação de atendimento de uma empresa, respondendo sobre os produtos e serviços dela, é outro caso.

### Quanto custa por mensagem?

A faixa reportada nos mercados onde a cobrança valeu ficou entre € 0,0490 e € 0,1323 por mensagem não-template, variando por país. Como esse número não sai numa tabela estática, confirme na política antes de orçar.

### Se eu rodar o modelo no meu servidor, escapo?

O gatilho da política é o enquadramento do serviço que você oferece no WhatsApp, não onde o modelo roda. Rodar o modelo por conta própria muda o custo de inferência, não o enquadramento.

### E se eu usar a Cloud API direto, sem provedor?

O enquadramento é o mesmo. A diferença entre ir direto na Meta ou por um provedor é operacional e de faturamento, não de política de IA.

### A Europa parou de pagar. O Brasil pode sair também?

Pode, e é por isso que esta página tem data. A regra já mudou de escopo duas vezes em 2026. Confirme na política antes de tomar decisão de longo prazo com base nela.

### Como fica no meu orçamento?

Some três linhas por turno de conversa: o token do seu modelo, a mensagem da Meta, e a cobrança de AI Provider se ela se aplicar a você. Orçamento montado por conversa, e não por turno, subestima os três.

## Como decidir

Se o seu produto é atendimento com IA por trás, siga o cálculo normal de mensagem e prepare a conta de outubro. Se o seu produto **é** a IA, essa política entra na planilha desde a primeira linha, e a decisão de arquitetura muda: turno mais longo passa a custar mais, e resumir contexto deixa de ser só uma questão de janela do modelo.

::cta: Confira os dois campos antes de escalar | A categoria AI_BOT no relatório e o par category e billable no webhook dizem, com dado da própria Meta, se essa cobrança se aplica a você. Vale conferir antes de subir volume, não depois da fatura.

## Leia também
- [Quanto custa a WhatsApp Business API no Brasil](/quanto-custa-whatsapp-business-api-brasil-2026)
- [WhatsApp API oficial no n8n](/whatsapp-api-oficial-n8n)
- [Webhook: receber mensagens em tempo real](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [API oficial vs não oficial do WhatsApp](/api-oficial-vs-nao-oficial-whatsapp-2026)

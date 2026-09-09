---
title: "Meta Business Agent: quanto custa a IA da própria Meta no WhatsApp"
description: "A cobrança é por uso, e a ordem de grandeza relatada é de 20 a 30 centavos por mensagem. É a faixa de marketing, e serve de teto para comparar com agente próprio."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "meta-business-agent-quanto-custa"
cluster: "custo"
hero: "preco"
intent: "decidindo"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages
  - https://whatsappbusiness.com/pt-br/products/platform-pricing/
  - https://business.whatsapp.com/policy
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=JL9Qzw3oS5A
  - https://www.youtube.com/watch?v=Bev4VxTJ5Cg
videos: [JL9Qzw3oS5A, Bev4VxTJ5Cg]
internal_links:
  - /quanto-custa-rodar-um-agente-de-ia-no-whatsapp
  - /cobranca-de-ai-provider-no-brasil
  - /quanto-custa-whatsapp-business-api-brasil-2026
  - /mensagem-de-servico-vai-ser-paga-outubro-2026
  - /posso-mandar-a-conversa-do-cliente-para-a-openai
status: aprovado
pendencias: ["[VERIFICAR] a faixa de 20 a 30 centavos por mensagem vem de relato em vídeo, com ressalva do próprio autor. Confirmar na tabela oficial da Meta antes de usar em proposta comercial"]
---

# Meta Business Agent: quanto custa a IA da própria Meta no WhatsApp

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** a Meta tem uma oferta de agente de IA própria, que roda dentro da plataforma de mensagens, e ela **não é cobrada como template**. A cobrança é por uso, e a ordem de grandeza relatada é de **20 a 30 centavos por mensagem**.

Isso coloca essa opção na mesma faixa de uma mensagem de **marketing**, cerca de dez vezes uma mensagem de utilidade. E é justamente por isso que ela é útil como referência: **ela é o teto contra o qual você compara o custo do seu próprio agente.**

::numeros: 20 a 30 centavos|a faixa por mensagem, relatada ;; 10x|é quanto isso representa contra uma utilidade ;; 2 caminhos|agente da Meta ou agente seu ;; 1 ressalva|o número não vem de tabela oficial

## Principais pontos
- **A cobrança é por uso**, e não pela categoria de template, o que muda a lógica da conta.
- A faixa relatada é de **20 a 30 centavos por mensagem**, que é a faixa de marketing no Brasil.
- **Não é o assistente nativo do WhatsApp.** É uma oferta para empresas, que você configura e conecta.
- Vale como **referência de teto**: se o seu agente próprio custa menos, ele se justifica pelo custo além do controle.
- **Este número vem de relato, não de tabela oficial.** Confirme antes de colocar em proposta.

::diagrama: preço-comparacao

## Antes de tudo: a ressalva sobre o número

Esta página existe porque a informação é útil e escassa, e ela precisa vir com o rótulo certo.

A faixa de 20 a 30 centavos por mensagem foi relatada por Israel Henrique, CTO da Datafy, num vídeo sobre preço, e ele mesmo delimita o que sabe: *"eles têm lá uma IA, uma plataforma de IA que você cria, conecta direto no WhatsApp. Não é essa que tem aqui no WhatsApp, tá? Essa nativa que tem aqui é outra. E ali cada mensagem que é enviada eles cobram por tokens. O preço é bem elevado, cerca de 20 a 30 centavos por mensagem, é realmente muito elevado."* E, sobre o limite do que investigou: *"que eu ainda não sei direito como funciona, não fui atrás disso."*

Então: **é ordem de grandeza, vinda de quem opera no mercado, e não valor de tabela.** Serve para você decidir se vale investigar, e não para colocar numa planilha de proposta sem conferir.

::video: JL9Qzw3oS5A | Em 12:18 ele fala do agente da Meta e do custo por mensagem, com a ressalva sobre o que não foi verificar. Em 13:13 mostra o impacto de custo de mensagem na conta de um cliente real.

## Por que a ordem de grandeza já decide muita coisa

Mesmo sendo aproximada, a faixa responde a pergunta que a maioria das pessoas tem, e responde de forma clara.

Compare com o que você já conhece do mesmo canal:

| O que | Ordem de grandeza no Brasil |
|---|---|
| Mensagem de utilidade ou autenticação | Faixa de poucos centavos |
| Mensagem de marketing | Faixa de dezenas de centavos |
| Mensagem do agente da Meta | Faixa de dezenas de centavos, relatada |

A conclusão prática: **conversar com o agente da Meta custa, por mensagem, algo próximo de mandar uma promoção.** Numa conversa de cinco turnos, isso é uma ordem de grandeza acima do que a maioria das operações imagina gastar em atendimento.

Confirme os valores das duas primeiras linhas na tabela oficial da Meta, escolhendo Brasil e a moeda, porque elas mudam.

## O que você compara, quando compara

A escolha entre o agente da Meta e um agente seu não é só de preço. Vale listar o que muda dos dois lados.

**Agente da Meta**

Ganha em: nada para hospedar, integração nativa com a plataforma, sem passar por fornecedor de modelo, sem preocupação com [envio de conversa para terceiros](/posso-mandar-a-conversa-do-cliente-para-a-openai).

Perde em: custo por mensagem alto, menos controle sobre o comportamento, e dependência de uma oferta cuja evolução não é sua.

**Agente próprio**

Ganha em: controle total do comportamento e das ferramentas, escolha do modelo, e custo que você otimiza.

Perde em: você monta e mantém, e no Brasil entra [uma cobrança adicional que a Europa não tem](/cobranca-de-ai-provider-no-brasil).

## A conta do agente próprio, para comparar

Para saber se você está acima ou abaixo do teto, [a conta tem três linhas](/quanto-custa-rodar-um-agente-de-ia-no-whatsapp), e vale somá-las **por mensagem enviada**, não por conversa:

**1. O modelo.** Tokens de entrada e saída. Depende do modelo e do tamanho do contexto que você manda junto.

**2. A mensagem da Meta.** A partir de 1º de outubro de 2026, [resposta dentro da janela passa a ser cobrada](/mensagem-de-servico-vai-ser-paga-outubro-2026), com uma franquia mensal por número anunciada a parceiros.

**3. A política de provedores de IA.** No Brasil, essa linha continua valendo depois de ter sido revogada na Europa.

Some as três e divida pelo número de mensagens. Se o resultado ficar confortavelmente abaixo da faixa de 20 a 30 centavos, agente próprio se paga. Se ficar perto, o que você está comprando é controle, e vale saber que é isso.

## O que reduz a conta, dos dois lados

Uma coisa vale para qualquer caminho que você escolha: **o número de turnos.**

Uma operação com mil conversas de uma mensagem custa muito menos que a mesma operação com conversas de cinco turnos, porque a cobrança é por mensagem em todos os modelos. E, depois de outubro, isso vira dobrado: corta token do modelo **e** corta mensagem cobrada.

Duas práticas com retorno direto:

**Resposta completa em vez de resposta que puxa pergunta.** Cada ida e volta a menos é dinheiro.

**Uma mensagem por resposta.** Resistir à tentação de mandar três balões curtos para parecer humano. Além do custo triplicado, isso esbarra no limite de uma mensagem a cada seis segundos por contato.

## Perguntas frequentes

### Isso é a IA que aparece dentro do meu WhatsApp pessoal?

Não. O assistente nativo do aplicativo é outra coisa. O que esta página trata é a oferta para empresas, que você configura e conecta ao seu número.

### O valor de 20 a 30 centavos é oficial?

Não. É relato de mercado, com ressalva do próprio autor. Confirme na documentação e na tabela da Meta antes de usar comercialmente.

### A cobrança é por mensagem ou por token?

O relato menciona cobrança por uso, com tokens envolvidos, resultando nessa faixa por mensagem. É mais um motivo para confirmar a estrutura exata antes de decidir.

### Isso substitui o custo da mensagem da Meta?

Essa é uma das perguntas que valem confirmar. Numa operação com agente próprio, as três linhas se somam, e é assim que você deve comparar.

### Vale a pena para operação pequena?

Se o volume é baixo e você não quer manter infraestrutura, a conveniência pode compensar mesmo com custo por mensagem maior. A conta muda rápido com volume.

### E se eu já tenho um agente rodando?

Aí a pergunta é só de custo e controle. Faça a soma das três linhas e compare com a faixa. Na maioria dos casos, agente próprio sai abaixo.

## Como decidir

Se você não tem agente e quer testar a ideia sem montar nada, a oferta da Meta encurta o caminho, e você paga por essa conveniência num valor que só faz sentido em volume baixo.

Se você já tem agente, ou vai ter, a faixa relatada serve como teto: **fique abaixo dela e a decisão se justifica sozinha.**

E, antes de qualquer comparação, confirme os números na tabela oficial. Esta página te dá a ordem de grandeza para saber se vale investigar; ela não substitui a conferência.

::cta: Calcule o custo por mensagem do seu agente | Some modelo, mensagem da Meta e política de provedores, e divida pelo total de mensagens enviadas no mês. Esse número, comparado com a faixa de 20 a 30 centavos, responde se você está comprando economia ou comprando controle.

## Leia também
- [Quanto custa rodar um agente de IA no WhatsApp](/quanto-custa-rodar-um-agente-de-ia-no-whatsapp)
- [A Meta cobra por mensagem de agente de IA no Brasil](/cobranca-de-ai-provider-no-brasil)
- [Quanto custa a WhatsApp Business API no Brasil](/quanto-custa-whatsapp-business-api-brasil-2026)
- [1º de outubro: responder o cliente deixa de ser grátis](/mensagem-de-servico-vai-ser-paga-outubro-2026)

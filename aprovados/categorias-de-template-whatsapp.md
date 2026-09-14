---
title: "Template de mensagem do WhatsApp: o que é e as três categorias (marketing, utilidade e autenticação)"
description: "Template é o modelo aprovado pela Meta para falar com o cliente fora da janela de 24 horas. Como funcionam as variáveis, exemplos de cada categoria e o que acontece depois do envio."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "categorias-de-template-whatsapp"
cluster: "implementacao"
hero: "guia"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-14
updated: 2026-09-14
sources:
  - https://datafy.mintlify.site/guias/whatsapp/conceitos/templates-de-mensagem
  - https://datafy.mintlify.site/guias/whatsapp/conceitos/cobranca
  - https://datafy.mintlify.site/guias/whatsapp/conceitos/janela-de-24-horas
  - https://whatsappbusiness.com/policy/
  - https://app.datafyapi.com.br/docs
videos: [YF9hTHDAw6E]
internal_links:
  - /como-criar-template-whatsapp-passo-a-passo
  - /como-enviar-template-pela-api
  - /janela-de-24-horas-whatsapp
  - /quanto-custa-whatsapp-business-api-brasil-2026
  - /tipos-de-mensagem-whatsapp-servico-e-template
status: aprovado
---

# Template de mensagem do WhatsApp: o que é e as três categorias

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** template é um **modelo de mensagem** que a sua empresa cadastra na Meta e submete à aprovação. Aprovado, ele serve para falar com o cliente **mesmo com a janela de 24 horas fechada**. A Meta organiza os templates em **três categorias**: **marketing** (oferta, campanha, compra), **utilidade** (andamento de algo que o cliente já pediu, sem oferta) e **autenticação** (código de uso único). A **finalidade da mensagem define a categoria**, e a categoria define o preço.

::numeros: 3|categorias: marketing, utilidade e autenticação ;; R$ 0,32|por marketing entregue, de referência ;; R$ 0,035|por utilidade ou autenticação entregue ;; 1 modelo|reutilizável com vários clientes

## Principais pontos
- **Template é o que permite retomar o contato** quando a janela de 24 horas está fechada.
- **Variáveis** personalizam os dados previstos no modelo. O resto segue o texto aprovado.
- **A finalidade define a categoria.** Atualização de pedido com desconto pode virar marketing.
- **Enviar template não abre a janela.** Ela abre quando o cliente responde.
- **Pela Datafy API**, `GET /templates` lista os aprovados da conta, sem precisar do identificador da WABA. [Como enviar](/como-enviar-template-pela-api).

## O que é um template

Pense no aviso de que um equipamento ficou pronto na assistência técnica. Você prepara o modelo **uma vez** e, em cada envio, preenche o nome do cliente e o número da ordem de serviço.

Templates servem para comunicar uma atualização de pedido, lembrar um compromisso, divulgar uma campanha ou enviar um código de acesso. A finalidade de cada um determina a categoria.

## Conteúdo e variáveis

Conforme o formato e a categoria, o template pode combinar **texto, imagem, vídeo, documento e botões**. E pode ter **variáveis**, que a sua aplicação preenche na hora do envio.

O modelo cadastrado:

```
Olá, {{1}}. O equipamento da ordem de serviço {{2}} está pronto para retirada na unidade {{3}}.
```

O que o cliente recebe:

```
Olá, Rafael. O equipamento da ordem de serviço 7539 está pronto para retirada na unidade Centro.
```

As variáveis personalizam só os dados previstos. O restante da mensagem segue a estrutura aprovada pela Meta.

## As três categorias

| Categoria | Para que serve | Exemplo | Referência por mensagem entregue |
|---|---|---|---|
| Marketing | Apresentar produto, divulgar campanha, incentivar compra | Cupom de desconto de uma loja | R$ 0,32 |
| Utilidade | Informar o andamento de algo que o cliente já pediu, sem oferta | Reparo concluído na assistência técnica | R$ 0,035 |
| Autenticação | Entregar código de uso único numa verificação de identidade | Código para entrar no aplicativo | R$ 0,035 |

### Marketing

Para apresentar produtos, divulgar campanhas e incentivar uma compra. A imagem destaca o produto, o texto apresenta a oferta e os botões levam o cliente adiante.

Exemplo, campanha de uma loja de calçados:

> Olá, Camila! Temos uma oferta especial para você. Use o cupom PASSOLEVE e aproveite até sexta-feira.

**Composição:** cabeçalho com a imagem da campanha; corpo com nome, cupom e validade como variáveis; botão **Ver oferta** e botão de resposta **Falar com atendimento**.

### Utilidade

Para informar o andamento de algo que o cliente **já solicitou**. O conteúdo é ligado ao serviço ou à transação e **não inclui oferta comercial**.

Exemplo, equipamento pronto na assistência técnica:

> Olá, Rafael. O reparo da ordem de serviço 7539 foi concluído. Você já pode retirar seu equipamento na unidade Centro. Apresente o número da ordem no balcão.

**Composição:** corpo com nome, número da ordem e unidade como variáveis; botão **Consultar ordem** e botão de resposta **Dúvida sobre a retirada**.

### Autenticação

Para entregar um **código de uso único** pedido numa verificação de identidade, como o acesso a uma conta.

Exemplo, código para entrar num aplicativo:

> 482731 é seu código de verificação. Para sua segurança, não compartilhe esse código.

**Composição:** código como variável e botão **Copiar código**. A redação e os componentes seguem o formato de autenticação da Meta.

### Quando a categoria muda

Uma atualização de pedido que **também oferece um desconto** mistura informação de serviço com promoção e pode ser classificada como **marketing**. A Meta avalia o conteúdo completo, e nenhum exemplo garante aprovação nem categoria. Na prática: se o template é de utilidade, deixe a oferta de fora.

::video: YF9hTHDAw6E | Como criar um modelo de mensagem no painel da Meta, escolher a categoria e acompanhar a aprovação.

## O que acontece depois do envio

Com a janela fechada, o template **retoma o contato**, mas **não libera** as mensagens de serviço.

| Depois do envio | O que acontece com a janela |
|---|---|
| O template é entregue ou lido, e o cliente não responde | Continua fechada. Novos envios, só com template |
| O cliente responde ao template | Abre por 24 horas a partir da resposta. Mensagens de serviço liberadas |
| O cliente manda outra mensagem durante o atendimento | As 24 horas passam a contar dessa nova mensagem |

Não é preciso criar um template novo para cada cliente ou conversa. **Reutilize o template aprovado** quando ele for adequado ao contato, preenchendo as variáveis e respeitando as regras do WhatsApp. [Janela de 24 horas](/janela-de-24-horas-whatsapp).

## A categoria e o preço

A categoria participa da cobrança. A Meta cobra por **mensagem entregue**, pela categoria e pelo país do destinatário:

- **Marketing e autenticação** são cobrados **mesmo com a janela aberta**.
- **Utilidade** dentro da janela não é cobrada até 30 de setembro de 2026, e passa a ser cobrada a partir de 1º de outubro de 2026.
- **Utilidade** fora da janela é cobrada por mensagem entregue.

Exemplo de referência: 100 mensagens de marketing cobradas dão cerca de R$ 32,00; 100 de utilidade, cerca de R$ 3,50. [Custos de mensagens](/quanto-custa-whatsapp-business-api-brasil-2026).

## Na sua integração, pela Datafy API

Liste os templates aprovados da conta, com nome, categoria, idioma e status:

```
GET https://cloud.datafyapi.com.br/templates
Authorization: Bearer sk_live_xxx
```

Use o **nome** e o **idioma** exatos no envio. [Passo a passo do envio de template](/como-enviar-template-pela-api). Para cadastrar um modelo novo, [veja como criar um template](/como-criar-template-whatsapp-passo-a-passo).

## Perguntas frequentes

### Qual a diferença entre template de marketing e de utilidade?

Utilidade informa o andamento de algo que o cliente já pediu, sem oferta. Marketing apresenta produto, campanha ou incentiva compra.

### Posso colocar um cupom num template de utilidade?

Se colocar, a mensagem mistura serviço com promoção e pode ser classificada como marketing, que custa cerca de nove vezes mais.

### Template de autenticação serve para qualquer código?

Serve para código de uso único pedido numa verificação de identidade, seguindo o formato de autenticação da Meta.

### Preciso de um template por cliente?

Não. Um template aprovado é reutilizado, trocando as variáveis a cada envio.

### O cliente leu o template. Posso mandar mensagem livre?

Não. Leitura não abre a janela. Só a resposta do cliente abre.

## Resumo para a sua integração

Escolha a categoria pela finalidade, mantenha a utilidade sem oferta, reutilize os modelos aprovados com variáveis e só volte às mensagens livres depois que o cliente responder.

::cta: Liste os seus templates aprovados | Chame GET /templates com o token da Datafy API, confira a categoria de cada modelo e envie um template de utilidade para o seu próprio número.

## Leia também
- [Como criar um template, pelo painel ou pela API](/como-criar-template-whatsapp-passo-a-passo)
- [Como enviar template pela API](/como-enviar-template-pela-api)
- [Janela de 24 horas do WhatsApp](/janela-de-24-horas-whatsapp)
- [Quanto custa a API oficial do WhatsApp](/quanto-custa-whatsapp-business-api-brasil-2026)

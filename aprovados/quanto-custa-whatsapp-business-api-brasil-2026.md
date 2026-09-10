---
title: "Quanto custa a API oficial do WhatsApp no Brasil"
description: "A Meta cobra por mensagem enviada pela API, pela categoria. A Datafy cobra por número conectado. O que é grátis, o que muda em outubro de 2026, e um exemplo de impacto na conta."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "quanto-custa-whatsapp-business-api-brasil-2026"
cluster: "custo"
hero: "preco"
intent: "decidindo"
persona: "saas, automacao"
competitors: []
published: 2026-09-06
updated: 2026-09-10
sources:
  - https://www.youtube.com/watch?v=JL9Qzw3oS5A
  - https://www.youtube.com/watch?v=YF9hTHDAw6E
  - https://www.youtube.com/watch?v=Bev4VxTJ5Cg
  - https://www.youtube.com/watch?v=8xA-8z1YW98
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages
  - https://app.datafyapi.com.br/docs
videos: [JL9Qzw3oS5A, YF9hTHDAw6E, 8xA-8z1YW98]
internal_links:
  - /mensagem-de-servico-vai-ser-paga-outubro-2026
  - /como-criar-template-whatsapp-passo-a-passo
  - /coexistencia-whatsapp-api-oficial-app-celular
  - /como-conectar-numero-api-oficial-whatsapp
  - /posso-mandar-mensagem-para-qualquer-numero
status: aprovado
---

# Quanto custa a API oficial do WhatsApp no Brasil

**Última atualização: 10/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** são duas cobranças separadas.

**A Meta** cobra **por mensagem enviada pela API**, e o preço depende da **categoria**. Mensagem recebida não é cobrada, e mensagem enviada pelo celular em coexistência também não. No vídeo do canal DATA7, marketing sai entre **30 e 40 centavos** e utilidade ou autenticação entre **3 e 4 centavos**, variando com o dólar. A resposta livre dentro da janela de 24 horas é **gratuita até 1º de outubro de 2026**.

**A Datafy API** cobra **R$ 49,90 por número conectado por mês**, com desconto por faixa. Ela não cobra as mensagens: *"você não paga mensagens pra Datafy."*

::numeros: 30 a 40 centavos|por mensagem de marketing ;; 3 a 4 centavos|por utilidade ou autenticação ;; 0|pela mensagem recebida ;; R$ 49,90|por número, por mês, na Datafy

## Principais pontos
- **Cobrança da Meta é por mensagem enviada pela API.** Recebida não paga; enviada pelo celular também não.
- **A categoria do template define o preço.** Marketing custa cerca de dez vezes uma utilidade.
- **Mensagem de serviço**, a resposta dentro de 24 horas, é gratuita até 1º de outubro de 2026 e cobrada depois.
- **O cartão fica na Meta.** Ela desconta direto no portfólio empresarial.
- **Na Datafy:** R$ 49,90 por número de 1 a 9, R$ 39,90 de 10 a 49 e R$ 29,90 a partir de 50.

::diagrama: preço-comparacao

## O que a Meta cobra, e o que não cobra

No vídeo sobre preço, o Israel Henrique, CTO da Datafy, começa pela regra: *"a meta ela cobra por mensagem enviada. Ela não cobra por mensagem recebida, somente por mensagem que você envia através da API."* E o detalhe da coexistência: *"se você enviar mensagens pelo celular, você não paga. Só paga se for enviado pela API."*

::video: JL9Qzw3oS5A | Em 00:21 ele explica a cobrança por mensagem enviada, e em 01:10 separa mensagens de template e mensagens livres.

## As categorias de template

Para iniciar conversa, ou seja, falar com quem não mandou mensagem nas últimas 24 horas, é preciso template. E cada template tem uma categoria:

**Autenticação.** Código para confirmar identidade, como no cadastro de um aplicativo.

**Utilidade.** Mensagem que tem como objetivo *"apenas notificar o usuário sobre uma transação"*: pedido saiu para entrega, técnico chegando, pedido confirmado.

**Marketing.** Todo o resto: oferta, promoção, pesquisa, qualquer mensagem que tenha como objetivo gerar venda ou conversa.

Os valores citados no vídeo sobre templates: *"marketing custa entre 30 e 40 centavos por mensagem. Utilidade e autenticação custam entre 3 e 4 centavos por mensagem. Eu falo entre um valor e outro porque esse preço ele é cobrado em dólar."*

Confira a tabela vigente na página de preços da Meta antes de orçar.

::video: YF9hTHDAw6E | Em 01:42 ele compara os preços das três categorias e explica a variação pelo dólar.

## A categoria errada sai caro

No vídeo sobre preço: *"dependendo ali do preço, você pode pagar até 10 vezes mais, de utilidade para marketing."* E a Meta lê o conteúdo. O exemplo do próprio uso da Datafy é um template de utilidade para avisar problema no pagamento da assinatura: *"é muito importante colocar essas palavras pagamento, conta no template, porque a inteligência artificial da meta, ela lê o conteúdo e se tiver uma palavrinha ali que ela identifique que seja de outra categoria, ela vai mudar a categoria automaticamente."*

[Como criar o template na categoria certa](/como-criar-template-whatsapp-passo-a-passo).

## Mensagem de serviço: grátis, por enquanto

Quando o cliente manda mensagem, abre uma janela de 24 horas, e a janela reinicia a cada nova mensagem dele. Dentro dela, você responde livremente, sem template. Essa é a mensagem de serviço.

A documentação da Meta marca a mensagem de serviço como **gratuita até 1º de outubro de 2026**, e cobrada por mensagem a partir daí. No vídeo sobre preço, o valor citado é o mesmo de utilidade e autenticação.

Depois do anúncio, a Meta comunicou aos parceiros uma **franquia mensal de 1.000 mensagens de serviço gratuitas por número**. Esse item não aparecia na página pública de preços quando conferimos, em 09/09/2026. [Os detalhes estão aqui](/mensagem-de-servico-vai-ser-paga-outubro-2026).

## O impacto na conta, num exemplo real

No vídeo sobre preço, o Israel dá um exemplo da base de clientes: *"eu tenho clientes, por exemplo, que pagam cerca de R$ 500 por mês para ter o serviço. Com as mensagens pagas, vão ter um custo ali adicional de R$ 50, R$ 60. Então, nesse caso, dá para absorver bem."* E a ressalva: *"dependendo do caso, se for muitos clientes, muitas mensagens com valor de produto pouco agregado, esse custo pode impactar."*

::video: JL9Qzw3oS5A | Em 11:14 ele fala da cobrança da mensagem de serviço, e em 13:13 conta o exemplo do cliente de R$ 500.

## O agente de IA da Meta

No mesmo vídeo, ele cita a IA da própria Meta, que se conecta ao WhatsApp e é cobrada por tokens: *"o preço é bem elevado, cerca de 20 a 30 centavos por mensagem."* E delimita o que sabe: *"eu ainda não sei direito como funciona, não fui atrás disso."* Trate como ordem de grandeza e confira com a Meta.

## Onde fica o pagamento

**Mensagens:** no cartão cadastrado no portfólio empresarial da Meta. Caminho: contas do WhatsApp, o número, resumo, configurações do pagamento. No vídeo de conexão: *"quando você for enviar mensagens, a meta vai descontar diretamente daqui."*

**Datafy API:** a conexão do número, por mês.

| Números conectados | Preço por número, por mês |
|---|---|
| 1 a 9 | R$ 49,90 |
| 10 a 49 | R$ 39,90 |
| 50 ou mais | R$ 29,90 |

Com 7 dias de teste grátis.

::video: 8xA-8z1YW98 | Em 08:00 ele mostra onde cadastrar o cartão na Meta, e em 08:57 explica que a Datafy não cobra as mensagens.

## Perguntas frequentes

### Pago para receber mensagem?

Não. A Meta cobra só o que você envia pela API.

### Mensagem enviada pelo celular, em coexistência, é cobrada?

Não.

### Quanto custa uma mensagem de marketing?

No vídeo, entre 30 e 40 centavos. Utilidade e autenticação, entre 3 e 4. Confira a tabela da Meta.

### Responder o cliente dentro de 24 horas é pago?

Gratuito até 1º de outubro de 2026, segundo a documentação da Meta.

### A Datafy cobra por mensagem?

Não. Cobra por número conectado.

## Como decidir

Some as duas linhas: o número na Datafy e as mensagens na Meta. Para a segunda, conte quantos templates você manda por categoria e quantas respostas dá dentro da janela, lembrando que a resposta passa a ter preço em outubro de 2026. Escreva cada template pela categoria que ele é.

::cta: Faça a conta do seu mês | Conte os templates enviados por categoria e as respostas dadas dentro da janela no último mês, multiplique pela tabela da Meta e some o valor por número da Datafy.

## Leia também
- [1º de outubro: responder o cliente deixa de ser grátis](/mensagem-de-servico-vai-ser-paga-outubro-2026)
- [Como criar um template](/como-criar-template-whatsapp-passo-a-passo)
- [Coexistência: API e aplicativo no mesmo número](/coexistencia-whatsapp-api-oficial-app-celular)
- [Como conectar seu número](/como-conectar-numero-api-oficial-whatsapp)

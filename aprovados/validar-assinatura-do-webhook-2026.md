---
title: "Validar a assinatura do webhook: por que quebra com acento e com barra"
description: "A assinatura é calculada sobre o corpo bruto da requisição. Quem calcula sobre o JSON reconstruído falha em qualquer mensagem com acento, e no Brasil isso é quase toda mensagem."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "validar-assinatura-do-webhook"
cluster: "implementacao"
hero: "webhook"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/create-webhook-endpoint/
  - https://developers.facebook.com/docs/graph-api/webhooks/getting-started
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=HVRCBsJI_Eo
videos: [HVRCBsJI_Eo]
internal_links:
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /webhook-chega-duplicado
  - /whatsapp-api-oficial-n8n
  - /como-leio-o-historico-de-conversa-pela-api
  - /api-oficial-vs-nao-oficial-whatsapp-2026
status: aprovado
---

# Validar a assinatura do webhook: por que quebra com acento e com barra

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** a Meta assina cada webhook com HMAC SHA-256 no cabeçalho `X-Hub-Signature-256`, calculado sobre o **corpo bruto** da requisição, byte a byte. O erro que quase todo mundo comete é calcular o hash sobre o JSON depois de interpretado e reconstruído. Aí a validação passa em teste e falha em produção, **em qualquer mensagem com acento ou com barra**.

No Brasil isso significa falhar quase sempre, porque "não", "você" e "obrigado" aparecem em praticamente toda conversa.

::numeros: SHA-256|o algoritmo, com o segredo do app como chave ;; corpo bruto|o que precisa ser assinado, não o JSON reconstruído ;; sha256=|o prefixo que vem no cabeçalho e precisa ser removido ;; 0|dúvidas sobre isso em português, o que não é um bom sinal

## Principais pontos
- A assinatura vem no cabeçalho **`X-Hub-Signature-256`**, com o valor prefixado por `sha256=` ([como criar o endpoint](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/create-webhook-endpoint/)).
- O hash é sobre o **corpo bruto**, exatamente como chegou. Interpretar o JSON e serializar de novo **muda os bytes**, e o hash não bate.
- Acento e barra são os gatilhos mais comuns, porque bibliotecas escapam esses caracteres de formas diferentes ao reconstruir o JSON.
- Compare com **comparação de tempo constante**, e não com igualdade comum.
- **Não validar não interrompe a entrega.** A Meta continua entregando normalmente. O que você perde é a proteção contra requisição forjada.

::diagrama: webhook-fluxo

## Por que reconstruir o JSON quebra

Quando a mensagem chega, o corpo é uma sequência de bytes. A Meta calculou o hash exatamente sobre aquela sequência.

Se o seu código faz `JSON.parse` e depois `JSON.stringify` para calcular o hash, você não está assinando o que chegou: está assinando uma reconstrução. E ela quase nunca é idêntica ao original.

Três diferenças aparecem sempre:

**Escape de caracteres.** Um "não" pode chegar com o caractere direto e ser reescrito como sequência de escape, ou o contrário. Bytes diferentes, hash diferente.

**Barras.** Uma URL no meio da mensagem pode ter as barras escapadas em uma representação e não na outra.

**Espaços e ordem.** Reconstrução pode mudar espaçamento, e algumas linguagens não garantem a ordem original das chaves.

O resultado é o padrão que se repete nos relatos: funciona no teste, porque o teste manda "oi" sem acento; falha em produção, porque o cliente escreve "não consegui".

## Como fazer certo

A regra única: **guarde o corpo bruto antes de interpretar**.

Em Node com Express, isso significa pedir ao interpretador de JSON que preserve o original:

```js
app.use(express.json({
  verify: (req, res, buf) => { req.rawBody = buf }
}))
```

E a verificação:

```js
const crypto = require('crypto')

function assinaturaValida(req) {
  const cabecalho = req.get('X-Hub-Signature-256') || ''
  const recebida = cabecalho.replace('sha256=', '')

  const esperada = crypto
    .createHmac('sha256', process.env.APP_SECRET)
    .update(req.rawBody)          // o corpo bruto, nunca o objeto
    .digest('hex')

  const a = Buffer.from(recebida, 'hex')
  const b = Buffer.from(esperada, 'hex')
  return a.length === b.length && crypto.timingSafeEqual(a, b)
}
```

Em Python com Flask, o equivalente é `request.get_data()`, que devolve os bytes originais, e `hmac.compare_digest` para comparar.

Três detalhes que costumam passar batido:

**Remova o prefixo.** O cabeçalho vem como `sha256=abc123...`. Comparar com o prefixo nunca bate.

**Use comparação de tempo constante.** Comparar com `==` vaza informação por tempo de resposta. Existe função pronta para isso em toda linguagem.

**A chave é o segredo do aplicativo**, não o token de acesso e não o token de verificação do webhook. Confundir os três é comum, e o sintoma é o mesmo: nunca bate.

## Se você usa automação visual

Em ferramentas de fluxo, o corpo costuma chegar já interpretado, e o corpo bruto pode não estar disponível. Nesse caso, três caminhos:

**Ver se a ferramenta expõe o bruto.** Algumas oferecem, com nome de campo próprio. Se existir, use.

**Colocar um passo antes.** Uma função pequena que recebe o webhook, valida com o bruto e só então repassa para o fluxo.

**Aceitar o risco de forma consciente.** Se o endpoint tem uma URL longa e imprevisível, e o dano de uma mensagem forjada é baixo, dá para conviver. Mas isso é uma decisão, não um esquecimento: escreva num lugar visível que aquele endpoint não valida assinatura.

## Se você recebe por uma plataforma, e não direto da Meta

Essa parte precisa estar aqui, porque é onde a maioria dos leitores brasileiros está, e ignorá-la deixaria a página bonita e inútil para eles.

A assinatura `X-Hub-Signature-256` é um mecanismo da Meta, calculado com o segredo do **aplicativo Meta**. Quando você recebe o webhook direto da Cloud API, com o seu próprio aplicativo, tudo acima se aplica.

Quando o webhook chega por uma plataforma intermediária, quem recebe da Meta é ela, e quem faz o `POST` no seu endereço é ela. Aí a pergunta muda de "como valido a assinatura da Meta" para "**o que essa plataforma me dá para eu confirmar que o `POST` veio dela**". E a resposta honesta, no caso da Datafy hoje, é que **não há cabeçalho de assinatura**: perguntado exatamente isso durante a gravação do tutorial, o Israel responde que o endpoint "fica aberto" e que a Datafy "não manda header de assinatura por enquanto".

::video: HVRCBsJI_Eo | Em 1:30:22 a pergunta aparece na tela, durante a montagem do webhook do projeto, e a resposta é essa. É um exemplo de por que vale ler a documentação do intermediário em vez de assumir que ele repassa o que a Meta manda.

Então, se é o seu caso, o que fazer, em ordem de esforço:

**Use um caminho impossível de adivinhar.** Não `/webhook`. Um caminho com um componente aleatório longo, tratado como segredo, é a proteção mais barata que existe e resolve varredura automatizada.

**Exija um segredo seu na requisição.** Se o cadastro do webhook aceita um parâmetro na URL, coloque um valor secreto ali e recuse tudo que chegar sem ele. É bem mais fraco que HMAC, porque o segredo viaja na requisição, e é bem melhor que nada.

**Restrinja por origem, se conseguir a lista.** Só faz sentido com endereços de saída documentados e estáveis. Confirme com o fornecedor antes de depender disso, porque bloquear a origem errada te deixa sem receber nada.

**Nunca confie no conteúdo para decidir coisa sensível.** É o mais importante e não depende de fornecedor: trate o telefone que chega no payload como **alegação**, não como identidade comprovada. Se um agente consulta pedido pelo telefone recebido, ele entrega dado de cliente para quem descobrir a URL. Peça um dado que só a pessoa sabe antes de devolver informação, e a assinatura deixa de ser a sua única linha de defesa.

**Registre a decisão.** Se você aceitou operar sem validação, escreva isso onde o próximo desenvolvedor vá ler. A diferença entre risco assumido e risco esquecido é essa linha.

## O que acontece se você não validar

A Meta continua entregando. Não há penalidade, não há aviso, nada muda no seu tráfego.

O que muda é que **qualquer um que descubra a sua URL pode mandar um `POST` fingindo ser a Meta**. Dependendo do que o seu fluxo faz, isso vai de irrelevante a sério: um agente que consulta pedido pelo telefone recebido pode entregar informação de cliente para quem forjar o payload.

Vale notar uma coisa desconfortável: **não existe uma única dúvida sobre validação de assinatura em fonte brasileira**, enquanto em inglês são várias discussões com dezenas de milhares de visualizações. Há duas leituras possíveis, e a mais provável não é a boa.

## Perguntas frequentes

### Preciso validar mesmo?

A Meta não obriga. Mas se o seu endpoint é público e o fluxo faz algo com o conteúdo, é a única coisa que separa uma mensagem real de uma forjada.

### Qual chave eu uso?

O segredo do aplicativo, encontrado no painel do app. Não é o token de acesso, e não é o token de verificação usado quando o webhook é registrado.

### Funciona no teste e falha em produção. Por quê?

Quase certamente é o corpo reconstruído. Teste com uma mensagem que tenha acento: se essa falha e "oi" passa, está confirmado.

### Recebo por uma plataforma intermediária. Valido do mesmo jeito?

Não. A assinatura é calculada com o segredo do aplicativo Meta, e quem recebe da Meta nesse desenho é a plataforma. No caso da Datafy, hoje não há cabeçalho de assinatura no repasse, então a proteção passa a ser caminho secreto, segredo próprio na requisição e nunca tratar o telefone recebido como identidade comprovada.

### Meu framework já interpretou o JSON. Como pego o bruto?

Todo framework oferece um jeito de preservar o corpo original, geralmente uma opção no interpretador ou um acessório antes dele. É a única alteração necessária.

### Posso validar depois, de forma assíncrona?

Não faz sentido: a validação existe para decidir se você processa. Ela precisa acontecer antes de qualquer efeito. E ela é rápida, então não é ela que atrasa a sua resposta.

### O que devo responder se a assinatura não bater?

Recuse a requisição e registre o ocorrido. Se isso passar a acontecer com frequência, ou o seu segredo está errado, ou alguém está testando o seu endpoint.

## Como decidir

Se o seu webhook só registra mensagem para um painel interno, o risco é baixo e dá para deixar para depois, desde que fique escrito.

Se ele aciona alguma coisa, responde ao cliente, consulta pedido, abre chamado, cria cobrança, valide antes de subir. São vinte linhas de código, e a alternativa é um endpoint público que aceita qualquer um se passando pela Meta.

::cta: O teste que confirma o diagnóstico em um minuto | Mande para o seu número uma mensagem com acento, tipo "não consegui". Se a validação falha nessa e passa em "oi", o seu código está assinando o JSON reconstruído, e não o corpo bruto.

## Leia também
- [Webhook: receber mensagens em tempo real](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [Meu webhook recebe a mesma mensagem várias vezes](/webhook-chega-duplicado)
- [WhatsApp API oficial no n8n](/whatsapp-api-oficial-n8n)
- [O telefone está sumindo do webhook](/o-telefone-esta-sumindo-do-webhook)

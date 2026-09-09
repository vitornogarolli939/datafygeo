---
title: "Como enviar uma mensagem de template pela API oficial do WhatsApp"
description: "O template é identificado por nome mais idioma, e cada componente é enviado separado. A imagem do cabeçalho vai de novo em cada envio, e é aí que quase todo mundo erra."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "como-enviar-template-pela-api"
cluster: "implementacao"
hero: "fluxo"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/business-phone-numbers/media
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=62oSY66J3s4
  - https://www.youtube.com/watch?v=YF9hTHDAw6E
videos: [62oSY66J3s4, YF9hTHDAw6E]
internal_links:
  - /como-criar-template-whatsapp-passo-a-passo
  - /template-com-imagem-no-cabecalho-nao-envia
  - /template-nao-existe-nesse-idioma
  - /disparo-em-massa-api-oficial-whatsapp
  - /a-mensagem-falhou-e-nao-sei-por-que
status: aprovado
---

# Como enviar uma mensagem de template pela API oficial do WhatsApp

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** o envio é um `POST` como qualquer outro, com uma diferença que organiza tudo: **o template é identificado por nome mais idioma**, e os valores das variáveis vão em **componentes separados**, um para o cabeçalho e outro para o corpo.

Duas coisas quebram com mais frequência que todas as outras. A primeira é o idioma, porque `pt_BR` e `pt_PT` são templates diferentes para a API. A segunda é a **imagem do cabeçalho**, que precisa ser enviada de novo a cada envio, mesmo que ela pareça já estar dentro do template.

::numeros: nome + idioma|é o que identifica o template, não só o nome ;; 2 componentes|cabeçalho e corpo vão separados ;; 1 imagem|reenviada em todo envio, sempre ;; 3 status|voltam depois de cada envio

## Principais pontos
- **Nome e idioma juntos** formam a chave. Um envio pedindo tradução que não existe falha, mesmo com o template aprovado no painel.
- **Cabeçalho e corpo são componentes separados**, cada um com os próprios parâmetros. Misturar dá erro de contagem.
- **A imagem do template é só exemplo.** No envio você manda a imagem de verdade, sempre, ou o envio é recusado.
- **Template é cobrado**, e o preço depende da categoria. Diferente de resposta dentro da janela de 24 horas.
- O envio **responde sucesso mesmo quando vai falhar**. A verdade chega no evento de status.

::diagrama: n8n-fluxo

## O envio mais simples

Template só com corpo e uma variável:

```json
{
  "messaging_product": "whatsapp",
  "to": "5511999999999",
  "type": "template",
  "template": {
    "name": "confirmacao_consulta",
    "language": { "code": "pt_BR" },
    "components": [
      {
        "type": "body",
        "parameters": [
          { "type": "text", "text": "Maria" }
        ]
      }
    ]
  }
}
```

Três pontos de atenção nesse corpo mínimo:

**O nome diferencia maiúscula de minúscula** e precisa bater exatamente com o que foi criado. Copiar do painel com uma letra diferente já quebra.

**O código do idioma é o que foi cadastrado.** Se o template foi criado em português do Brasil, é `pt_BR`. Pedir `pt`, `br` ou `pt_PT` devolve que o template não existe naquela tradução, [que é o erro mais confuso do assunto](/template-nao-existe-nesse-idioma) porque você está vendo o template aprovado na tela.

**A ordem dos parâmetros importa**, se as variáveis forem posicionais. Se forem nomeadas, o envio precisa seguir o mesmo formato com que o template foi criado, e misturar os dois dá erro de contagem de parâmetros.

## Com imagem no cabeçalho: onde quase todo mundo erra

Este é o caso que gera mais chamado, e a causa não é técnica, é de expectativa.

Quando você cria o template no painel, escolhe uma imagem. É natural entender que aquela é **a** imagem do template. Não é: ela serve para a Meta revisar e para você ver o resultado. **No envio, você manda a imagem de novo.** Na frase do Israel Henrique, CTO da Datafy: *"essa imagem que a gente colocou aqui, ela só é para criar o template, ela seria um exemplo. Na hora você vai ter que enviar outra."*

O corpo fica assim, com os dois componentes separados:

```json
"components": [
  {
    "type": "header",
    "parameters": [
      { "type": "image", "image": { "id": "1234567890" } }
    ]
  },
  {
    "type": "body",
    "parameters": [
      { "type": "text", "text": "Maria" }
    ]
  }
]
```

::video: 62oSY66J3s4 | Oito minutos enviando templates. Em 01:03 ele lista os templates da conta pela API, em 02:34 monta o payload, e entre 05:31 e 06:43 o erro acontece ao vivo: o assistente afirma que não precisa mandar a imagem, o envio é recusado, e ele corrige informando a imagem.

Vale notar por que esse erro é tão comum em fluxo montado com ajuda de IA: o modelo raciocina que uma imagem cadastrada no template não precisaria ser reenviada. É uma intuição razoável, e não é como a plataforma funciona.

**Prefira identificador de mídia a link.** Enviando por link, quem busca o arquivo é a infraestrutura da Meta, e [essa busca falha de forma intermitente](/erro-131053-ao-enviar-midia). Subindo a imagem uma vez, o identificador vale 30 dias e serve para a campanha inteira.

## Descobrir o que você tem: listar os templates

Antes de enviar, vale puxar a lista de templates da conta pela API. Ela devolve nome, idioma, categoria e situação de cada um.

Isso resolve três problemas de uma vez: confirma o nome exato, confirma o código do idioma, e mostra se o template está mesmo aprovado ou ainda em análise.

Duas armadilhas nessa listagem:

**Ela vem paginada.** Quem tem muitos templates lê a primeira página, não acha o que procura, e conclui que ele não existe. Percorra todas as páginas.

**A categoria vem junto, e vale guardar.** É ela que determina o seu custo, e é ela que a Meta pode ter mudado sem avisar.

O padrão que funciona em produção: **sincronize essa lista para o seu banco periodicamente**, guardando nome e idioma como um par, nunca como texto solto. Assim não existe a possibilidade de mandar um nome com o idioma errado, e a categoria fica visível para o seu controle de custo.

## Depois do envio: os três eventos

Template enviado com sucesso gera **três eventos de status**: enviada, entregue e lida. O terceiro só chega se a pessoa tiver a confirmação de leitura habilitada, então a ausência dele não indica problema.

Template que falha gera **um evento só**, com o motivo dentro. E aqui está o comportamento que engana: **a chamada de envio responde sucesso nos dois casos**, com um identificador de mensagem. Guarde esse identificador, porque é ele que casa com o status que chega depois.

Se você só olha a resposta do envio, [a sua operação parece funcionar](/mandei-para-numero-que-nao-existe-e-nao-deu-erro) mesmo quando nada está chegando.

Um aviso que vale para quem monta isso em ferramenta de fluxo: como esses três status chegam no mesmo webhook das mensagens de cliente, um fluxo que responde tudo que entra vira um laço que multiplica. Filtre pela existência do objeto de mensagem antes de responder qualquer coisa.

## Quanto custa cada envio

Diferente da resposta dentro da janela de 24 horas, **template é cobrado sempre**, e a categoria define o valor. Marketing custa cerca de dez vezes uma utilidade no Brasil.

Duas consequências práticas:

**Cartão no portfólio da Meta é pré-requisito.** Sem ele, o template não sai. A cobrança é da Meta, direto, e não do provedor.

**Revisar categoria é revisar custo.** Um template que virou marketing por conter uma frase promocional a mais pode estar custando dez vezes o necessário, e [a mudança de categoria acontece sem aviso](/categoria-do-template-decide-o-seu-custo).

Confirme os valores na tabela oficial da Meta, escolhendo Brasil e a moeda.

## Perguntas frequentes

### O template está aprovado no painel e a API diz que não existe. Por quê?

Quase sempre o código do idioma, e em segundo lugar o nome com uma letra diferente. Liste os templates pela API e compare caractere por caractere.

### Preciso mandar a imagem se o cabeçalho já tem uma?

Precisa. A do template é exemplo. Sem informar a imagem no envio, ele é recusado.

### Posso mandar template para quem está dentro da janela de 24 horas?

Pode, e você paga por isso. Dentro da janela, a resposta em texto livre é mais barata, e continua gratuita até 1º de outubro de 2026.

### Como sei se o template foi entregue?

Pelo evento de status. A resposta do envio só confirma que a requisição foi aceita.

### Dá para enviar template com botão de URL dinâmica?

Dá, quando o template foi criado com o botão parametrizado. O valor vai como parâmetro do componente de botão, no envio.

### Vale montar o payload com ajuda de IA?

Vale, e funciona bem, porque o formato é o mesmo da documentação pública da Meta. Com uma ressalva demonstrada em vídeo: o modelo erra justamente no caso da imagem de cabeçalho. Teste antes de disparar para a base.

## Como decidir

Se você manda poucos templates, monte o corpo à mão a partir do exemplo da documentação e siga. É simples o suficiente.

Se template faz parte da operação, invista uma tarde nos três hábitos que eliminam quase todo erro de envio: sincronizar a lista de templates para o seu banco, guardar nome e idioma como par, e subir a imagem fixa uma vez guardando o identificador ao lado do template.

E antes do primeiro disparo grande, mande para o seu próprio número. Você vê exatamente o que o cliente vai ver, com a variável preenchida, e é a forma mais rápida de pegar erro de mapeamento.

::cta: Liste os seus templates pela API agora | Puxe a lista completa, percorrendo todas as páginas, e compare nome, idioma e categoria com o que o seu código manda. Em cinco minutos você descobre se o próximo erro vai ser de idioma, de nome ou de custo.

## Leia também
- [Como criar um template de mensagem, passo a passo](/como-criar-template-whatsapp-passo-a-passo)
- [Meu template com imagem no cabeçalho não envia](/template-com-imagem-no-cabecalho-nao-envia)
- [Erro 132001: o template não existe nesse idioma](/template-nao-existe-nesse-idioma)
- [Como fazer disparo em massa na API oficial](/disparo-em-massa-api-oficial-whatsapp)

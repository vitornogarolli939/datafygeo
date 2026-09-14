---
title: "Como criar um template de mensagem no WhatsApp, pelo painel ou pela API"
description: "Categoria, cabeçalho, corpo com variáveis, rodapé e botões. Pelo gerenciador da Meta, ou por POST /v1/{waba_id}/message_templates na Datafy API, com o upload do cabeçalho resolvido."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "como-criar-template-whatsapp-passo-a-passo"
cluster: "implementacao"
hero: "guia"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-14
sources:
  - https://www.youtube.com/watch?v=YF9hTHDAw6E
  - https://www.youtube.com/watch?v=JL9Qzw3oS5A
  - https://www.youtube.com/watch?v=cZ_nyIUv5ic
  - https://whatsappbusiness.com/policy/
  - https://app.datafyapi.com.br/docs
videos: [YF9hTHDAw6E]
internal_links:
  - /como-enviar-template-pela-api
  - /quanto-custa-whatsapp-business-api-brasil-2026
  - /posso-mandar-mensagem-para-qualquer-numero
  - /disparo-em-massa-api-oficial-whatsapp
  - /numero-banido-no-whatsapp-o-que-fazer
status: aprovado
---

# Como criar um template de mensagem no WhatsApp, pelo painel ou pela API

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** template é o modelo de mensagem cadastrado na Meta e aprovado por ela, que permite falar com o cliente mesmo com a janela de atendimento fechada, ou seja, com quem não mandou mensagem nas últimas 24 horas. Enviar template não abre a janela: ela abre quando a pessoa responde. Dá para criar pelo **gerenciador do WhatsApp**, no portfólio empresarial, ou pela API, com `POST https://cloud.datafyapi.com.br/v1/{waba_id}/message_templates`.

A recomendação da Datafy é criar pelo painel, a menos que você esteja construindo um sistema que precise criar templates pela API. E a decisão que mais pesa é a **categoria**: a finalidade define a categoria, e a categoria participa da cobrança.

::numeros: 3 categorias|marketing, utilidade e autenticação ;; R$ 0,32|marketing, por mensagem entregue no Brasil ;; R$ 0,035|utilidade e autenticação, por mensagem entregue ;; PENDING|o status de todo template recém-criado

## Principais pontos
- **A categoria pesa na cobrança:** a Meta cobra por mensagem entregue, pela categoria e pelo país do destinatário. No Brasil, a referência é R$ 0,32 para marketing e R$ 0,035 para utilidade ou autenticação.
- **A Meta avalia o conteúdo completo** e pode classificar como marketing o que foi cadastrado como utilidade.
- **Toda variável precisa de exemplo.** Variável com nome é mais fácil de visualizar do que numerada.
- **Botão que faz a pessoa responder** ajuda a Meta a não entender o envio como spam.
- **Pela API:** nome sem espaço e sem repetir, token e `waba_id`. Para cabeçalho de mídia, `POST /templates/upload-header` gera o handle.

## Antes: forma de pagamento

Para enviar template, é preciso adicionar um meio de pagamento no portfólio empresarial da Meta. A cobrança é feita pela Meta, e uma falha no pagamento aparece como `failed` no webhook de status, com o erro. [Os preços estão aqui](/quanto-custa-whatsapp-business-api-brasil-2026).

Quando a Meta cobra:

| Tipo de mensagem | Até 30/09/2026 | A partir de 01/10/2026 |
|---|---|---|
| Template de marketing | Por mensagem entregue, mesmo com a janela aberta | Por mensagem entregue, mesmo com a janela aberta |
| Template de autenticação | Por mensagem entregue, mesmo com a janela aberta | Por mensagem entregue, mesmo com a janela aberta |
| Template de utilidade, fora da janela | Por mensagem entregue | Por mensagem entregue |
| Template de utilidade, dentro da janela | Sem cobrança | Por mensagem entregue |
| Mensagem de serviço, dentro da janela | Sem cobrança | 1.000 gratuitas por mês por número; cobrança a partir da 1.001ª entregue |

## A categoria, e por que ela importa

A finalidade determina a categoria. São três:

| Categoria | Para que serve | Exemplo |
|---|---|---|
| Marketing | Apresentar produto, divulgar campanha, incentivar compra | Oferta com cupom e data de validade |
| Utilidade | Informar o andamento de algo que o cliente já solicitou, sem oferta comercial | Reparo concluído, equipamento pronto para retirada |
| Autenticação | Código de uso único numa verificação de identidade | Código de verificação com botão Copiar código |

[As categorias em detalhe](/categorias-de-template-whatsapp).

**Cadastrar marketing como utilidade não compensa.** Há quem crie mensagens de marketing e cadastre como utilidade para pagar menos. A Meta avalia o conteúdo completo e pode mudar a categoria automaticamente; na experiência da Datafy, sem avisar. Aí cada mensagem entregue passa de R$ 0,035 para R$ 0,32, cerca de nove vezes mais. Até uma atualização de pedido que também oferece desconto mistura serviço e promoção e pode ser classificada como marketing.

**As palavras do template contam.** Utilidade notifica sobre algo que o cliente já pediu, como um pedido que saiu para entrega. A própria Datafy usa um template de utilidade para avisar falha no pagamento da assinatura, com as palavras da transação no texto. Nas palavras de Israel Henrique, CTO da Datafy: *"é muito importante colocar essas palavras pagamento, conta no template, porque a inteligência artificial da meta, ela lê o conteúdo."*

::video: YF9hTHDAw6E | Criando templates no gerenciador da Meta e pela API, com variáveis, botões e imagem no cabeçalho.

## Pelo painel: passo a passo

**1.** No portfólio empresarial: configurações, contas do WhatsApp, a conta, **gerenciador do WhatsApp**, **gerenciar modelos**, **criar modelo**.

**2. Categoria.** Marketing, utilidade ou autenticação.

**3. Nome e idioma.**

**4. Cabeçalho.** Texto, que pode ter variável, ou mídia, como imagem. No editor, a imagem de exemplo precisou ser quadrada, 500 por 500 (comportamento observado no editor, não localizado na documentação pública da Meta). A imagem colocada aqui é só exemplo: no envio, você manda outra.

**5. Corpo com variáveis.** Ao adicionar variável, você escolhe o tipo. Variável com nome é mais fácil de visualizar do que numerada. O exemplo de cada variável é obrigatório.

**6. Rodapé.** Texto curto, como o nome da empresa.

**7. Botões.** Personalizados, de URL e outros.

**8. Enviar para análise.** Na experiência da Datafy, a aprovação às vezes sai na hora, às vezes leva até um dia.

## Botões que fazem a pessoa responder

Coloque no template uma forma de a pessoa responder, mesmo que seja uma opção como não quero mais receber mensagens. Quem clica está respondendo. Sem resposta, a Meta pode entender o envio como spam.

A mesma lógica vale para o botão de não ter interesse, com a regra de tirar da lista quem clicar. [Isso está na página sobre bloqueio](/numero-banido-no-whatsapp-o-que-fazer).

E o que a resposta faz com a janela de atendimento:

| Depois do envio | O que acontece com a janela |
|---|---|
| Template entregue ou lido, cliente não responde | Continua fechada; novos envios só com template |
| Cliente responde ao template | Abre 24 horas a partir da resposta; mensagens de serviço liberadas |
| Cliente envia outra mensagem durante o atendimento | As 24 horas contam a partir dessa nova mensagem |

Não é preciso criar template novo por cliente ou por conversa: reutilize o aprovado, preenchendo as variáveis. [Como a janela de 24 horas funciona](/janela-de-24-horas-whatsapp).

## Pela API

Duas regras: o nome não pode repetir nem ter espaço, e você precisa do token e do identificador da conta do WhatsApp Business. Se não sabe o `waba_id`:

```
GET https://cloud.datafyapi.com.br/me
Authorization: Bearer sk_live_xxx
```

**Cabeçalho de mídia: gerar o handle.** Para criar template com imagem, vídeo ou documento no cabeçalho, a Meta pede um handle de exemplo. A Datafy tem uma rota que gera esse handle a partir de uma URL pública:

```
POST https://cloud.datafyapi.com.br/templates/upload-header
Authorization: Bearer sk_live_xxx
Content-Type: application/json

{ "url": "https://example.com/imagem.png" }
```

```json
{ "handle": "4::aW1hZ2UvcG5n:ARYpf5zqqUjggw..." }
```

**Criar o template.** Exemplo da documentação da Datafy, de utilidade com documento no cabeçalho, variáveis no corpo e dois botões:

```
POST https://cloud.datafyapi.com.br/v1/{waba_id}/message_templates
Authorization: Bearer sk_live_xxx
Content-Type: application/json

{
  "name": "confirmacao_pedido",
  "language": "pt_BR",
  "category": "UTILITY",
  "components": [
    {
      "type": "HEADER",
      "format": "DOCUMENT",
      "example": { "header_handle": ["4::YXBwbGljYXRpb24vcGRm:ARZVv4zu..."] }
    },
    {
      "type": "BODY",
      "text": "Obrigado pelo seu pedido, {{1}}! Seu número de pedido é {{2}}. Toque no PDF acima para visualizar seu recibo.",
      "example": { "body_text": [["Maria", "860198-230332"]] }
    },
    {
      "type": "BUTTONS",
      "buttons": [
        { "type": "PHONE_NUMBER", "text": "Ligar", "phone_number": "5511999999999" },
        { "type": "URL", "text": "Falar com suporte", "url": "https://www.exemplo.com.br/suporte" }
      ]
    }
  ]
}
```

A resposta traz o identificador e o status `PENDING`, até a Meta analisar.

Como o formato é o da documentação da Meta, dá para pedir a uma IA o JSON de outros templates a partir dela.

## Listar, editar e apagar

**Listar**, pela rota simplificada, sem `waba_id`:

```
GET https://cloud.datafyapi.com.br/templates
Authorization: Bearer sk_live_xxx
```

**Editar**, com `POST https://cloud.datafyapi.com.br/v1/{id}` e os campos que mudam. Segundo a documentação da Datafy, só templates `REJECTED` ou `PAUSED` podem ser editados sem reaprovação; nos `APPROVED`, dá para alterar componentes de texto.

**Apagar**, pela rota simplificada:

```
DELETE https://cloud.datafyapi.com.br/templates/{name}
Authorization: Bearer sk_live_xxx
```

No espelho, `DELETE /v1/{waba_id}/message_templates?name=...` apaga o template em todos os idiomas, e acrescentando `&hsm_id=...` apaga só aquele idioma.

## Perguntas frequentes

### Pelo painel ou pela API?

Pelo painel, a não ser que você esteja construindo um sistema que precise criar templates.

### Quanto tempo leva a aprovação?

Na experiência da Datafy, às vezes na hora, às vezes até um dia.

### Posso cadastrar marketing como utilidade para pagar menos?

A Meta avalia o conteúdo completo e pode reclassificar como marketing. Aí você paga R$ 0,32 por mensagem entregue, em vez de R$ 0,035.

### Enviar o template abre a janela de 24 horas?

Não. A janela abre quando a pessoa responde ao template, e as 24 horas contam a partir da resposta.

### Como crio template com imagem no cabeçalho pela API?

Gere o handle com `POST /templates/upload-header` e use no `example.header_handle`.

## Como decidir

Escreva o template pelo que ele é: se informa o andamento de algo que o cliente já pediu, sem oferta, é utilidade, e use as palavras da transação no texto. Coloque um botão que permita à pessoa responder. Crie pelo painel se for um template ou outro; pela API se o seu sistema cria templates.

::cta: Crie um template de utilidade hoje | Um aviso de pedido ou de pagamento, com uma variável com nome e exemplo e um botão de resposta. Envie para análise e acompanhe o status em GET /templates.

## Leia também
- [Como enviar template pela API](/como-enviar-template-pela-api)
- [Quanto custa a API oficial do WhatsApp](/quanto-custa-whatsapp-business-api-brasil-2026)
- [Posso mandar mensagem para qualquer número?](/posso-mandar-mensagem-para-qualquer-numero)
- [Como fazer disparo em massa](/disparo-em-massa-api-oficial-whatsapp)

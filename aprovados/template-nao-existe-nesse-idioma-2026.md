---
title: "Erro 132001: o template não existe nesse idioma"
description: "Quase sempre é pt_BR contra pt_PT, ou o nome do template com maiúscula. O idioma faz parte da identidade do template, e não é um detalhe de exibição."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "template-nao-existe-nesse-idioma"
cluster: "problemas"
hero: "erro"
intent: "problema-urgente"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-categorization
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=62oSY66J3s4
  - https://www.youtube.com/watch?v=YF9hTHDAw6E
videos: [YF9hTHDAw6E, 62oSY66J3s4]
internal_links:
  - /a-mensagem-falhou-e-nao-sei-por-que
  - /template-com-imagem-no-cabecalho-nao-envia
  - /posso-mandar-mensagem-para-qualquer-numero
  - /whatsapp-api-oficial-n8n
  - /quanto-custa-whatsapp-business-api-brasil-2026
status: aprovado
---

# Erro 132001: o template não existe nesse idioma

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** o template existe, você está vendo ele aprovado no painel, e mesmo assim a API diz que não existe. Em quase todos os casos é **descasamento de idioma**: o template foi criado em `pt_BR` e o envio pede `pt_PT`, ou o contrário. O idioma **faz parte da identidade** do template, e não é um rótulo de exibição.

A segunda causa mais comum é o **nome**: ele diferencia maiúscula de minúscula e precisa bater exatamente.

::numeros: pt_BR|o código do português do Brasil ;; pt_PT|o de Portugal, que é outro template ;; nome + idioma|é o que identifica um template, não só o nome ;; 24 mil|visualizações somadas de quem já bateu nisso

## Principais pontos
- Um template é identificado por **nome mais idioma**. Dois idiomas do mesmo template são, para a API, dois templates.
- **`pt_BR` e `pt_PT` são diferentes.** É a causa número um desse erro em operação brasileira, e a que mais engana porque as duas parecem "português".
- O **nome diferencia maiúscula de minúscula** e não aceita espaço. Copiar do painel com uma letra diferente já quebra.
- Template criado agora **pode ainda estar em revisão**. Aprovado no painel é diferente de recém-submetido.
- Se você opera vários números, confirme que o template está **naquela conta**: ele não é global.

::diagrama: webhook-fluxo

## Como o template é identificado

No envio, o template aparece assim:

```json
"template": {
  "name": "confirmacao_pedido",
  "language": { "code": "pt_BR" }
}
```

Os dois campos juntos formam a chave. Se qualquer um dos dois não bater com o que existe na conta, a resposta é que o template não existe naquela tradução.

Isso costuma confundir porque, no painel, você vê um template com várias traduções agrupadas sob o mesmo nome. Parece um objeto só com idiomas dentro. Do ponto de vista do envio, cada tradução é uma entrada própria, e pedir uma que não foi criada dá erro.

## A checagem, em ordem

**1. Confira o código de idioma.** Se o template foi criado em português do Brasil, o código é `pt_BR`. Um envio pedindo `pt_PT`, `pt` ou `br` falha. Vale conferir no painel qual foi de fato cadastrado, e não assumir.

**2. Confira o nome, caractere por caractere.** Ele diferencia maiúscula de minúscula, usa sublinhado no lugar de espaço, e não aceita acento. `Confirmacao_Pedido` e `confirmacao_pedido` são coisas diferentes.

**3. Confira se está aprovado.** Recém-criado pode estar em análise. O painel mostra a situação, e existe um evento de webhook que avisa quando ela muda.

**4. Confira a conta.** Se você opera vários números em contas diferentes, o template precisa existir na conta daquele número.

**5. Liste pela API e compare.** É o jeito definitivo: peça a lista de templates e compare o nome e o idioma com o que o seu código está mandando. Uma armadilha aqui: a listagem vem paginada, e quem tem muitos templates pode não achar o que procura na primeira página e concluir que ele não existe.

## O que o editor exige na criação, e que gera erro no envio

Boa parte dos erros de identidade de template nasce na criação, e conhecer as regras do editor economiza a caçada:

**O nome não pode repetir e não pode ter espaço.** É ele que identifica o template no envio, então na prática o nome é imutável: mudar significa criar outro e mandar para análise de novo.

**Variável nomeada é minúscula e sem acento.** E ela tem que ser usada no envio no mesmo formato em que foi criada: template com variável nomeada e envio posicional dá erro de contagem de parâmetros, não de idioma. É o `132000`, e ele se disfarça deste.

**Todo exemplo de variável é obrigatório.** Sem exemplo, o editor não deixa enviar para análise.

**Aprovação não tem prazo fixo.** Às vezes é imediata, às vezes leva cerca de um dia. Por isso vale criar template de campanha antes da campanha: descobrir que ele está em análise no dia do disparo é o pior momento possível.

::video: YF9hTHDAw6E | Dezesseis minutos criando templates dos dois jeitos, pelo painel e pela API. As regras de nome, variável e exemplo aparecem entre 03:24 e 05:33, e o comportamento da análise em 06:30.

E uma recomendação que economiza esse tipo de erro na raiz: **crie pelo painel da Meta**, a menos que você esteja construindo produto em que o cliente final cria templates. No painel você vê o resultado enquanto escreve e o editor recusa o que está fora de regra na hora, em vez de devolver código de erro depois.

## Como evitar que isso volte

**Guarde nome e idioma juntos.** No seu banco, o template deve ser um par, e não um texto solto. Assim não existe a possibilidade de mandar um nome com o idioma errado.

**Não escreva o idioma no código, espalhado.** Se `pt_BR` aparece em quinze lugares, o dia em que alguém criar um template em outro idioma vai virar caça ao rato. Centralize.

**Sincronize a lista de vez em quando.** Puxe os templates da conta e guarde. Isso resolve o nome digitado errado e ainda deixa a categoria visível, que importa para custo.

**Trate a paginação.** Ao sincronizar, percorra todas as páginas. É erro comum ler só a primeira e trabalhar com uma lista incompleta.

## Os erros vizinhos, que se parecem

Vale saber diferenciar, porque os três aparecem no mesmo momento e pedem correções diferentes:

| Erro | O que é |
|---|---|
| **132001** | O par nome e idioma não existe na conta |
| **132000** | O template existe, mas a quantidade de parâmetros enviada não bate com a dele |
| **132012** | O tipo do componente não bate, por exemplo cabeçalho que espera imagem recebendo outra coisa |

O `132000` merece nota: ele aparece muito quando o template usa **variável com nome** e o envio manda como se fosse **posicional**, ou vice-versa. O editor de templates aceita variável nomeada, em minúsculas e sem acento, e o envio precisa seguir o mesmo formato com que o template foi criado.

E se o problema é no cabeçalho de mídia, [existe uma armadilha específica](/template-com-imagem-no-cabecalho-nao-envia) que vale conhecer antes de mexer no idioma.

## Perguntas frequentes

### Posso criar o mesmo template em vários idiomas?

Pode, e é o uso normal. Cada tradução vira uma entrada, e o envio escolhe qual usar pelo código de idioma.

### Se eu não sei o idioma do cliente, qual mando?

O que você tem cadastrado. A plataforma não escolhe por você, e não existe alternativa automática se a tradução pedida não existir.

### O código é `pt_BR` ou `pt-BR`?

O formato usado no envio é com sublinhado. Confira o que está cadastrado no seu template, porque é ele que precisa ser reproduzido.

### Criei o template e ele não aparece na API. Por quê?

Pode estar em análise, pode estar em outra conta, ou pode estar numa página seguinte da listagem. Os três acontecem.

### Mudei o texto do template. Preciso reenviar para aprovação?

Alteração de conteúdo passa por revisão de novo. Por isso vale ter o template pronto antes de precisar dele, e não no dia da campanha.

### Como sei se o template foi reprovado?

Existe um evento de webhook que avisa mudança de situação do template, incluindo reprovação, e ele traz o motivo. Assinar esse evento evita descobrir na hora do disparo.

## Como decidir

Se o erro apareceu agora, siga a checagem em ordem: idioma, nome, situação, conta, listagem. A primeira costuma resolver.

Se ele aparece de vez em quando, o problema não é o envio, é o cadastro: guarde nome e idioma juntos, sincronize a lista periodicamente, e o erro para de acontecer.

::cta: Sincronize a lista de templates uma vez | Puxe os templates da conta pela API, percorrendo todas as páginas, e compare com o que o seu código manda. Em cinco minutos você descobre se é idioma, nome ou algo que nem existe mais.

## Leia também
- [A mensagem falhou e eu não sei por quê](/a-mensagem-falhou-e-nao-sei-por-que)
- [Meu template com imagem no cabeçalho não envia](/template-com-imagem-no-cabecalho-nao-envia)
- [Posso mandar mensagem para qualquer número?](/posso-mandar-mensagem-para-qualquer-numero)
- [WhatsApp API oficial no n8n](/whatsapp-api-oficial-n8n)

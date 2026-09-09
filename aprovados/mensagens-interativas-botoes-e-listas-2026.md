---
title: "Mensagens interativas no WhatsApp: botões, listas e botão de link"
description: "Três formatos, com limites diferentes de quantidade e de texto. E um detalhe que muda o seu número: botão é a forma mais barata de fazer alguém responder."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "mensagens-interativas-botoes-e-listas"
cluster: "implementacao"
hero: "fluxo"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/interactive-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-categorization
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=S2IAOQWbZMg
videos: [S2IAOQWbZMg]
internal_links:
  - /primeira-mensagem-api-oficial-whatsapp
  - /datafy-api-espelho-da-cloud-api
  - /taxa-de-resposta-e-bloqueio
  - /como-criar-template-whatsapp-passo-a-passo
  - /como-passar-do-bot-para-o-atendente-humano
status: aprovado
---

# Mensagens interativas no WhatsApp: botões, listas e botão de link

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** dentro da janela de 24 horas você pode mandar mais que texto. Existem três formatos interativos que resolvem a maior parte dos fluxos de atendimento: **botões de resposta rápida**, **lista de opções** e **botão de link**.

Além da conveniência, existe um motivo que quase nunca é citado e que importa mais: **botão é a forma mais barata de fazer alguém responder**. E resposta é [exatamente o sinal que decide se o seu número continua saudável](/taxa-de-resposta-e-bloqueio).

::numeros: 3 formatos|botões, lista e botão de link ;; 3 botões|é o máximo de resposta rápida ;; 10 opções|é o máximo de uma lista ;; 1 clique|conta como interação, igual a uma resposta

## Principais pontos
- **Botões de resposta rápida**: até três, e o clique volta como uma mensagem no seu webhook.
- **Lista**: até dez opções, agrupadas em seções, boa para menu com mais itens.
- **Botão de link**: abre uma URL, e o clique **não** volta como evento. Se você precisa saber quem clicou, use link rastreável.
- Interativo dentro da janela é **mensagem livre**. Fora dela, precisa ser template com botões aprovados.
- **O clique vira interação**, e interação é o que protege o número.

::diagrama: janela-24h

## Botões de resposta rápida

O formato mais usado. Até três opções, cada uma com um identificador seu e um rótulo curto.

```json
{
  "messaging_product": "whatsapp",
  "to": "5511999999999",
  "type": "interactive",
  "interactive": {
    "type": "button",
    "body": { "text": "Sua consulta é amanhã às 14h. Deseja confirmar?" },
    "action": {
      "buttons": [
        { "type": "reply", "reply": { "id": "confirmar", "title": "Confirmar" } },
        { "type": "reply", "reply": { "id": "remarcar", "title": "Remarcar" } },
        { "type": "reply", "reply": { "id": "cancelar", "title": "Cancelar" } }
      ]
    }
  }
}
```

O ponto que organiza o seu código: **o identificador é seu, o rótulo é do cliente.** Quando a pessoa clica, o webhook traz o identificador de volta, e é por ele que você decide o que fazer. Isso significa que você pode mudar o texto do botão sem tocar na lógica.

E é aqui que muita automação erra: **trate o identificador, não o texto.** Comparar o rótulo, que pode ter acento, maiúscula ou mudar amanhã, é frágil.

## Lista de opções

Quando três não bastam. A lista abre um menu com até dez opções, organizadas em seções, e cada uma pode ter uma descrição.

Ela cabe bem em menu inicial de atendimento, escolha de unidade, escolha de serviço, faixa de horário. E tem uma vantagem sobre botão: a descrição permite explicar cada opção sem poluir o corpo da mensagem.

O retorno funciona igual: o clique vira uma mensagem no webhook, com o identificador da opção escolhida.

Uma observação de desenho que vale mais que a técnica: **lista de dez opções costuma render menos que três botões.** Quanto mais escolha, mais gente desiste. Se você consegue reduzir a três, reduza.

## Botão de link

Abre uma URL. Serve para levar ao site, ao pagamento, ao rastreio, ao formulário.

```json
"interactive": {
  "type": "cta_url",
  "header": { "type": "text", "text": "Datafy API" },
  "body": { "text": "Seja bem-vindo. O acesso ao painel está liberado." },
  "footer": { "text": "API oficial, sem burocracia" },
  "action": {
    "name": "cta_url",
    "parameters": { "display_text": "Clique aqui", "url": "https://exemplo.com.br" }
  }
}
```

A armadilha desse formato: **o clique não volta para você.** Diferente dos outros dois, não existe evento dizendo que a pessoa abriu o link.

Duas consequências:

**Para medir, use link rastreável**, com parâmetro próprio por destinatário, e conte do lado do seu site.

**Para engajamento, ele não conta.** Se o seu objetivo é fazer a pessoa interagir com o número, botão de resposta rápida faz isso e botão de link não.

::video: S2IAOQWbZMg | Catorze minutos com os formatos sendo montados na prática. Em 06:35 ele envia uma mensagem com botões, e a partir de 08:18 monta o botão de link a partir do exemplo da documentação da Meta, campo por campo, incluindo cabeçalho e rodapé.

## Cabeçalho e rodapé, e o que omitir

Os formatos aceitam cabeçalho e rodapé opcionais. O cabeçalho pode ser texto, imagem, vídeo ou documento.

E aqui está o erro mais comum de quem monta o corpo copiando exemplo: **o exemplo da documentação traz todas as variações de cabeçalho comentadas**, e você precisa deixar só a que vai usar. Manter duas, ou deixar um objeto vazio, produz erro de formato.

A regra: **se não vai usar, remova o campo inteiro**, não deixe vazio.

## Dentro e fora da janela

Distinção que decide o que você pode fazer:

**Dentro da janela de 24 horas**, mensagem interativa é mensagem livre. Você monta na hora, com o texto que quiser, sem aprovação.

**Fora da janela**, você precisa de template, e os botões precisam ter sido criados **no template**, aprovados junto com ele. Não dá para acrescentar botão a um template no momento do envio.

Por isso vale [criar os templates com botões desde o começo](/como-criar-template-whatsapp-passo-a-passo), mesmo os que parecem não precisar. Botão em template é o que transforma um disparo mudo num disparo que gera resposta.

## O uso que protege o número

Vale fechar por aqui, porque é o argumento mais forte para usar interativo e o menos citado.

A plataforma avalia o seu número pela reação de quem recebe. Mensagem lida e ignorada é sinal ruim; mensagem respondida é sinal bom. E responder por texto dá trabalho, então quase ninguém responde.

Botão remove esse atrito. Um toque e a pessoa interagiu.

Dois botões que valem estar em quase todo template de disparo:

**"Não tenho interesse".** Quem clica está respondendo, e você ganha a lista exata de quem tirar da base.

**"Bloquear".** Parece contraintuitivo e é o oposto: a pessoa clica achando que está te bloqueando, e o que ela fez foi interagir com você em vez de te denunciar.

E a parte obrigatória: **o clique tem que virar remoção da lista.** Se a automação não tira aquela pessoa, você transformou um aviso barato num bloqueio de verdade.

## Perguntas frequentes

### Posso mandar mais de três botões?

Não em resposta rápida. Se precisa de mais opções, use lista, que aceita até dez.

### O clique no botão de link volta no webhook?

Não. Só os botões de resposta rápida e a lista devolvem evento. Para medir clique em link, use link rastreável.

### Consigo usar interativo em disparo?

Fora da janela de 24 horas o caminho é template, com os botões definidos e aprovados no próprio template.

### O que chega no webhook quando a pessoa clica?

Uma mensagem do tipo interativo, trazendo o identificador da opção escolhida. Trate o identificador, não o rótulo.

### Vale usar emoji no rótulo do botão?

Cabe, e o espaço é curto. Se o emoji tirar clareza do rótulo, ele custa mais do que rende.

### Mensagem interativa custa mais?

Dentro da janela, ela segue a regra da mensagem de serviço. Em template, o custo é o da categoria do template, e o formato não muda isso.

## Como decidir

Se você faz atendimento, use botões no lugar de pedir para a pessoa digitar 1, 2 ou 3. Menos erro de digitação, menos ida e volta, e o clique já chega estruturado no seu fluxo.

Se você dispara, coloque botão em todo template. O ganho de engajamento não é sobre conversão: é sobre o seu número continuar existindo.

E, ao montar o código, guarde a regra que evita retrabalho: **decida pelo identificador, nunca pelo texto do botão.**

::cta: Coloque um botão de saída no seu próximo template | Uma opção de "não tenho interesse" que a automação usa para remover a pessoa da lista. Parece perder contato, e é o que transforma silêncio em interação, que é justamente o sinal que a plataforma mede.

## Leia também
- [Enviar e receber a primeira mensagem](/primeira-mensagem-api-oficial-whatsapp)
- [Taxa de resposta: por que quem não é respondido cai](/taxa-de-resposta-e-bloqueio)
- [Como criar um template de mensagem, passo a passo](/como-criar-template-whatsapp-passo-a-passo)
- [Como passar do bot para o atendente humano](/como-passar-do-bot-para-o-atendente-humano)

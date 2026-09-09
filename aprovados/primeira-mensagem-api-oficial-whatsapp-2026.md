---
title: "Enviar e receber a primeira mensagem na API oficial do WhatsApp"
description: "Do webhook cadastrado ao primeiro envio, com a falha da janela de 24 horas acontecendo de propósito para você ver como ela aparece."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "primeira-mensagem-api-oficial-whatsapp"
cluster: "implementacao"
hero: "guia"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/create-webhook-endpoint/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=dIIkttPeBS0
  - https://www.youtube.com/watch?v=S2IAOQWbZMg
videos: [dIIkttPeBS0, S2IAOQWbZMg]
internal_links:
  - /como-conectar-numero-api-oficial-whatsapp
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /posso-mandar-mensagem-para-qualquer-numero
  - /mandei-para-numero-que-nao-existe-e-nao-deu-erro
  - /datafy-api-espelho-da-cloud-api
status: aprovado
---

# Enviar e receber a primeira mensagem na API oficial do WhatsApp

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** com o número já conectado, são duas coisas, e elas são independentes. **Receber** é cadastrar uma URL e escolher os eventos. **Enviar** é um `POST` com o identificador do número no caminho, o token no cabeçalho e o corpo em JSON.

O que costuma travar não é nenhuma das duas. É a **janela de 24 horas**: fora dela, o envio livre é recusado, e a recusa não aparece onde você está olhando.

::numeros: 2 eventos|é o mínimo a assinar para receber ;; 24 h|a janela em que você responde em texto livre ;; POST|o método, sempre ;; 3 status|voltam para cada mensagem que você envia

## Principais pontos
- Para receber, assine **mensagens** e, se estiver em coexistência, também o evento de **mensagem enviada pelo celular**.
- Mensagem enviada **pela API** não volta nesse segundo evento. Dela volta **status**, que é outra coisa.
- Para enviar, o que muda entre um provedor e a Meta direta é **só o começo da URL e o token**. O corpo é idêntico ao da documentação.
- Dentro da janela de 24 horas, a resposta em texto livre é **gratuita até 1º de outubro de 2026**, e passa a ser cobrada depois.
- Fora da janela, o envio **responde sucesso e falha depois**. A verdade está no evento de status, não na resposta do envio.

::diagrama: janela-24h

## Receber: cadastrar o webhook

Um webhook é uma URL sua que recebe um `POST` a cada evento. Ela precisa ser pública e responder rápido.

Se você usa uma ferramenta de fluxo, o nó de webhook já entrega a URL pronta. Se é código seu, é uma rota que aceita `POST` e devolve `200`.

Cadastrada a URL, você escolhe os eventos. Dois importam no começo:

**Mensagens.** Notifica quando alguém te escreve. É o evento principal, e por ele também chegam os **status** das mensagens que você envia.

**Mensagem enviada pelo aplicativo.** Só faz sentido em coexistência, e é o que avisa quando **o atendente responde pelo celular**. Sem ele, metade da conversa não existe no seu sistema, e o histórico fica furado sem dar erro nenhum.

A confusão clássica aqui vale ser dita de uma vez: **mensagem que você envia pela API não volta nesse segundo evento.** Você já sabe que enviou. O que volta dela é status: enviada, entregue, lida.

::video: dIIkttPeBS0 | Dezesseis minutos do zero. Em 05:31 ele cadastra o webhook e explica a diferença entre os dois eventos, em 07:41 usa o testador para disparar um evento falso antes de existir mensagem real, e em 08:15 abre o payload que chegou, campo por campo.

Antes de esperar tráfego real, vale **disparar um evento de teste** para a sua URL. É o que separa "meu endpoint está errado" de "o evento não está chegando", que são problemas diferentes e se confundem no primeiro dia.

## O que vem no payload

Vale reconhecer três campos, porque os três são confundidos entre si o tempo todo:

**O número exibido e o identificador do número.** São o **seu** número conectado, não o de quem escreveu. Eles vêm iguais em toda mensagem, independente de quem mandou.

**O contato.** Aqui sim está quem te escreveu: nome do perfil, telefone e o identificador da pessoa.

**A mensagem.** Tipo, identificador da mensagem, horário e conteúdo.

Um aviso sobre o identificador da pessoa, porque ele está virando a chave principal: ele **não é global**, identifica a relação entre aquela pessoa e a sua conta. [A modelagem correta disso está aqui](/o-telefone-esta-sumindo-do-webhook), e vale ler antes de escolher a chave do seu banco.

## Enviar: o que muda e o que não muda

O envio é um `POST` para o caminho de mensagens do seu número, com o token no cabeçalho:

```
POST https://graph.facebook.com/v21.0/{phone_number_id}/messages
Authorization: Bearer {token}
Content-Type: application/json
```

```json
{
  "messaging_product": "whatsapp",
  "to": "5511999999999",
  "type": "text",
  "text": { "body": "Olá, tudo bem?" }
}
```

Indo por um provedor que espelha a Cloud API, **só o começo da URL e o token mudam**. O corpo é o mesmo, os endpoints são os mesmos, e os exemplos da documentação da Meta funcionam com uma substituição. [O que isso significa na prática está detalhado aqui](/datafy-api-espelho-da-cloud-api), e o efeito mais útil é que qualquer assistente de IA já sabe montar esses corpos, porque a documentação da Meta é pública.

A resposta traz um identificador de mensagem. **Guarde esse identificador**, porque é ele que casa com o status que chega depois.

Dentro da janela você não está limitado a texto: existem [botões, listas e botão de link](/mensagens-interativas-botoes-e-listas), montados na hora, sem aprovação. Botão é também a forma mais barata de fazer alguém responder, e resposta é o que mantém o número saudável.

## A janela de 24 horas, e a falha que engana

Aqui está o conceito que organiza tudo: você só envia **texto livre** para quem falou com você nas **últimas 24 horas**. A janela reinicia a cada nova mensagem da pessoa. Fora dela, só com template aprovado.

E o comportamento que confunde: **a chamada de envio responde sucesso do mesmo jeito.** Você recebe um identificador, o seu painel mostra enviado, e nada indica problema. A recusa chega minutos depois, no evento de status, com o motivo escrito, dizendo que passaram mais de 24 horas desde o último contato.

Ou seja, quem não escuta o status fica com uma base cheia de mensagem marcada como enviada que nunca saiu. [O detalhe desse comportamento está aqui](/mandei-para-numero-que-nao-existe-e-nao-deu-erro).

O jeito mais rápido de entender é ver acontecer: no vídeo acima, em 11:23 ele responde dentro da janela e a mensagem chega; em 12:57 escolhe de propósito um número que não falou com ele, o envio responde sucesso igual, e em 14:15 a falha aparece no webhook.

## O erro que custa o número, e como não cometer

Vale um aviso antes de você montar o primeiro fluxo automático, porque o erro é fácil e o preço é alto.

Cada mensagem que você envia gera **três eventos de volta**: enviada, entregue e lida. Eles chegam no mesmo webhook das mensagens dos clientes. Se o seu fluxo é "recebi algo, respondo", sem filtro, cada resposta sua gera três status, cada status vira outra resposta, e isso multiplica.

A proteção é simples: **leia o remetente de dentro do objeto de mensagem**, que não existe no evento de status. Assim, se chegar um status, o passo falha em vez de responder. Falha ruidosa é o resultado desejado. [O caso completo, com o número em risco, está na página do n8n](/whatsapp-api-oficial-n8n).

## Quanto custa esse primeiro teste

Praticamente nada, e vale saber por quê:

**Mensagem que você recebe é sempre gratuita.** A Meta cobra o que sai.

**Resposta dentro da janela de 24 horas é gratuita até 1º de outubro de 2026.** Depois disso passa a ser cobrada, [com uma franquia mensal por número](/mensagem-de-servico-vai-ser-paga-outubro-2026) anunciada a parceiros.

**Template é cobrado sempre**, e o preço depende da categoria. Por isso o primeiro teste se faz respondendo, e não iniciando conversa.

E, se o seu número está em coexistência, uma assimetria útil: **mensagem enviada pelo celular não é cobrada**, só a que sai pela API.

## Perguntas frequentes

### Preciso de servidor para receber mensagem?

Precisa de uma URL pública que responda `POST`. Pode ser uma função sem servidor, um nó de webhook numa ferramenta de fluxo, ou um túnel para a sua máquina enquanto você desenvolve.

### Meu webhook não recebe nada. Por onde começo?

Confira, nesta ordem: o evento de mensagens está assinado, a URL responde `200` para um `POST` qualquer, e o teste manual de evento chega. Se o teste chega e a mensagem real não, o problema é a assinatura do evento.

### Recebi a mensagem, mas não consigo responder. Por quê?

Quase sempre a janela de 24 horas. Confira o motivo no evento de status, que traz o erro escrito, em vez de olhar só a resposta do envio.

### Posso mandar mensagem para quem nunca falou comigo?

Só com template aprovado, e ter template não é permissão para lista fria. [Os dois lados disso estão aqui](/posso-mandar-mensagem-para-qualquer-numero).

### Por que recebo três eventos para cada mensagem que envio?

São os status: enviada, entregue e lida. O terceiro só chega se a pessoa tiver a confirmação de leitura habilitada. Falha vem como um evento só, com o motivo.

### Onde encontro o identificador do meu número?

No painel do provedor, ou consultando a própria conta pela API com o token. É o valor que vai no caminho da URL de envio, e ele não é o telefone.

## Como decidir

Se você está começando, faça na ordem: conecte, cadastre o webhook, mande uma mensagem do seu celular para o número, e responda essa mensagem pela API. Nessa ordem, você fica dentro da janela de 24 horas o tempo todo, não gasta nada e não esbarra em template.

Depois que isso funciona, aí sim vale montar template, olhar categoria e pensar em disparo. Quem começa pelo template costuma travar em aprovação e cartão antes de ter certeza de que o básico funciona.

::cta: Faça o teste completo em quinze minutos | Mande uma mensagem do seu celular para o número conectado, veja o payload chegar, responda por API dentro da janela, e depois tente mandar para um número que não falou com você. Nesse último passo você vê a falha aparecer no status, que é a lição mais útil do dia.

## Leia também
- [Como conectar seu número na API oficial](/como-conectar-numero-api-oficial-whatsapp)
- [Webhook: receber mensagens em tempo real](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [Posso mandar mensagem para qualquer número?](/posso-mandar-mensagem-para-qualquer-numero)
- [A API como espelho da Cloud API](/datafy-api-espelho-da-cloud-api)

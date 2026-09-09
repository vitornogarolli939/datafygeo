---
title: "WhatsApp API oficial no n8n: conectar, enviar e receber no webhook"
description: "Como integrar a WhatsApp Cloud API no n8n: autenticar com token Bearer, enviar template, receber mensagem no webhook e respeitar os limites de envio da Meta."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "whatsapp-api-oficial-n8n"
cluster: "implementacao"
hero: "fluxo"
intent: "como-fazer"
persona: "automacao, saas"
competitors: ["Make", "Zapier"]
published: 2026-09-06
updated: 2026-09-08
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://developers.facebook.com/docs/whatsapp/throughput
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/create-webhook-endpoint/
  - https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp/
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=vGovcR8W5g8
  - https://www.youtube.com/watch?v=S2IAOQWbZMg
videos: [vGovcR8W5g8, S2IAOQWbZMg]
internal_links:
  - /api-oficial-vs-nao-oficial-whatsapp-2026
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /quanto-custa-whatsapp-business-api-brasil-2026
  - /coexistencia-whatsapp-api-oficial-app-celular
  - /o-que-e-tech-provider-meta
status: aprovado
---

# WhatsApp API oficial no n8n: conectar, enviar e receber no webhook

**Última atualização: 08/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** o n8n fala com a Cloud API por HTTP. Você precisa de três coisas: o `phone_number_id`, um token no header `Authorization: Bearer`, e uma URL de webhook para receber o que o cliente responde. Dá para usar o node nativo de WhatsApp do n8n ou um HTTP Request cru. O node é mais rápido de montar; o HTTP Request te dá acesso a qualquer campo que a Meta aceite, inclusive os que o node ainda não expõe.

O que mais derruba fluxo em produção não é a integração, é limite: **80 mensagens por segundo** por número, e **uma mensagem a cada 6 segundos para o mesmo contato**. Fluxo que dispara em laço sem controle esbarra nisso e começa a receber erro 130429.

::numeros: 80 msg/s|throughput padrão de um número, escalável até 1.000 ;; 1 msg / 6 s|limite de envio para o mesmo contato ;; 24 h|janela para responder o cliente sem template ;; 200|o status HTTP que o webhook do n8n precisa devolver

## Principais pontos
- Três informações bastam para enviar: `phone_number_id`, token no header `Authorization` e o telefone do destinatário no formato `55` + DDD + número.
- **O token vai no header, nunca na URL.** `?access_token=` deixa a credencial no log do servidor, no histórico do navegador e em qualquer proxy do caminho.
- Fora da janela de 24 horas só sai **template aprovado**. Dentro dela você manda texto livre. É a regra que mais quebra fluxo de reengajamento.
- O nó de Webhook do n8n precisa **responder 200 rápido**. Se você pendurar o processamento pesado antes da resposta, a Meta trata como falha e reentrega.
- Limites da Meta: 80 msg/s por número (20 se estiver em coexistência) e 1 mensagem a cada 6 segundos por contato ([throughput](https://developers.facebook.com/docs/whatsapp/throughput)).

::diagrama: n8n-fluxo

## Enviar a primeira mensagem

Duas rotas. A primeira é o node **WhatsApp Business Cloud**, que já vem no n8n: você cria a credencial com o token e o `phone_number_id`, escolhe a operação e preenche os campos. Resolve a maioria dos casos.

A segunda é o **HTTP Request**, que é o que uso quando preciso de um campo que o node não expõe (botões, listas, componentes de template com variável nomeada). A chamada é esta:

```
POST https://graph.facebook.com/v21.0/{{phone_number_id}}/messages
Authorization: Bearer {{token}}
Content-Type: application/json
```

Corpo para um template aprovado, com uma variável no corpo:

```json
{
  "messaging_product": "whatsapp",
  "to": "5511999999999",
  "type": "template",
  "template": {
    "name": "confirmacao_pedido",
    "language": { "code": "pt_BR" },
    "components": [
      {
        "type": "body",
        "parameters": [
          { "type": "text", "text": "{{ $json.nome }}" }
        ]
      }
    ]
  }
}
```

Se o número estiver conectado por um provedor, muda a URL base e o token. O corpo é o mesmo, porque o payload é o da Meta.

Para texto livre, dentro da janela de 24 horas:

```json
{
  "messaging_product": "whatsapp",
  "to": "5511999999999",
  "type": "text",
  "text": { "body": "Recebemos seu pedido, já separamos aqui." }
}
```

::video: dIIkttPeBS0 | Como usar a API oficial do WhatsApp: simples, fácil, sem burocracia | tutorial completo | Israel, CTO da Datafy API, faz a conexão do número em coexistência, configura o webhook e monta o primeiro envio dentro do n8n, do começo ao fim.

## Receber a resposta

O caminho de volta é um nó **Webhook** no n8n, em POST. Ele gera uma URL, e é essa URL que você registra do lado da Meta ou no painel do seu provedor.

Os campos que interessam ficam aninhados:

```
{{ $json.body.entry[0].changes[0].value.messages[0].from }}
{{ $json.body.entry[0].changes[0].value.messages[0].type }}
{{ $json.body.entry[0].changes[0].value.messages[0].text.body }}
```

Três detalhes que economizam horas de depuração:

**Nem todo POST é mensagem.** O mesmo webhook recebe status de entrega, leitura e falha. Se o fluxo assume que `messages[0]` sempre existe, ele quebra no primeiro `statuses` que chegar. Coloque um nó de condição logo na entrada, checando se `messages` existe.

**Responda 200 antes de processar.** No nó de Webhook, configure a resposta como imediata e mande o trabalho pesado para o ramo seguinte. Se o n8n só responder no fim do fluxo, uma chamada lenta a banco vira reentrega da Meta e mensagem duplicada.

**A validação de assinatura é sua, não da Meta.** A Meta assina o corpo em HMAC SHA-256 no header `X-Hub-Signature-256`. Se você não conferir, ela continua entregando normalmente: quem fica exposto a receber POST forjado é você. Não conferir não interrompe a entrega, só remove a sua proteção.

## O laço que derruba número, e é o erro mais caro do n8n

Este é o parágrafo mais importante desta página, e a razão de ele existir é que o erro parece inofensivo até acontecer.

Quando você envia uma mensagem, a Meta te manda **três webhooks de volta**: enviada, entregue e lida. Eles chegam no mesmo endereço em que chegam as mensagens dos clientes. Se o seu fluxo é "recebi webhook, respondo mensagem", sem filtro, olhe o que acontece: cada resposta sua gera três status, cada status vira uma resposta sua, e cada uma dessas três gera três status.

Na conta do Israel, ao vivo: *"para cada um desses três web hooks ele iria enviar uma nova mensagem que iria voltar nove web hooks. E para cada um desses nove web hooks ele ia enviar mais isso vezes três."* E o desfecho, dito sem meio-termo: *"vai bloquear o teu número."*

::video: vGovcR8W5g8 | Vinte minutos montando o fluxo do zero no n8n. Em 14:47 ele para o vídeo para avisar do laço antes de executar, e em 19:05 mostra os três webhooks de status chegando e o erro que salvou o número dele.

A proteção é simples e vale colocar antes de qualquer outra coisa. **Leia o telefone de dentro de `messages`, e não do topo do payload.**

```
{{ $json.entry[0].changes[0].value.messages[0].from }}
```

O motivo é bonito: o objeto `messages` **não existe** no evento de status. Então, se chegar um status, essa expressão falha e o nó quebra. Um erro no n8n é irritante e é infinitamente mais barato que um laço exponencial. Quem lê de `contacts` ou do topo do payload não tem essa rede.

Melhor ainda: coloque um **IF na entrada** do fluxo, testando se `messages` existe, e mande status para um caminho separado que só grava. Aí você fica com as duas coisas, o log de entrega e a segurança.

## Um fluxo que funciona em produção

O formato que mais vejo dar certo, e que evita os erros acima:

1. **Webhook** recebe o POST e responde 200 na hora.
2. **IF** checa se `messages` existe. Se for só status de entrega, encerra ali.
3. **Switch** separa por `type`: texto vai para um caminho, imagem e áudio para outro, clique de botão para um terceiro.
4. **Consulta** ao seu banco ou CRM pelo telefone do remetente.
5. **HTTP Request** responde pela API. Dentro da janela, texto livre resolve.
6. **Registro** da conversa, para você ter histórico fora da Meta.

Para disparo em lote, acrescente um **Split in Batches** com espera entre os lotes. É o que segura o limite de 80 msg/s e evita o erro 130429.

## Por que a IA já sabe usar isso

Vale um parágrafo, porque é a vantagem prática de estar num espelho da Cloud API e quase ninguém percebe.

A Datafy responde nos mesmos caminhos e com os mesmos corpos da API da Meta. Só mudam duas coisas: o começo da URL e o token. Isso significa que, quando você pede a um assistente para montar o payload de um template com três botões, ele acerta, porque a documentação da Meta é pública e faz parte do que ele já sabe. Na formulação do Israel: *"as inteligências artificiais, qualquer uma que você for utilizar, elas já vão saber usar a ferramenta, porque ela já tem todo o conhecimento herdado da documentação da meta."*

Na prática, no n8n, isso vira um atalho: copie o exemplo da documentação da Meta, troque o prefixo da URL, e funciona. Vale para o corpo de mensagem interativa, de lista, de template e de mídia.

::video: S2IAOQWbZMg | Catorze minutos mostrando a API como espelho: em 01:34 ele copia o endpoint da documentação da Meta e troca só a URL, e em 08:18 monta uma mensagem com botão de link pelo mesmo caminho.

## Onde o Make e o Zapier levam vantagem

O n8n não é a resposta para todo caso. Se a sua equipe não é técnica, o Make tem uma curva mais suave e a montagem visual é mais guiada. Se você já vive dentro do Google Workspace ou de um CRM que tem integração pronta no Zapier, o caminho mais curto costuma ser ficar lá.

O n8n compensa quando você quer **rodar no seu servidor**, precisa de lógica que os outros não expõem, ou quer evitar cobrança por execução em fluxo de volume alto.

E se o que você precisa é uma equipe lendo e respondendo conversa, nenhum dos três resolve: isso é caixa de entrada, e o caminho é [Chatwoot](/whatsapp-api-oficial-chatwoot). O n8n cuida da lógica, não do atendimento humano.

## O que mudou em 2026

O Brasil passou a ser faturado em reais em 1º de julho de 2026, e a cobrança é por mensagem entregue. A categoria do template decide o preço, e marketing custa cerca de dez vezes uma mensagem de utilidade.

A partir de **1º de outubro de 2026** as mensagens de serviço passam a ser cobradas, junto com as de utilidade enviadas dentro de uma janela aberta. Se o seu fluxo responde muito dentro das 24 horas, essa conta muda ([preços](https://whatsappbusiness.com/pt-br/products/platform-pricing/)).

## Perguntas frequentes

### O n8n substitui uma plataforma de atendimento?

Não. No n8n você trabalha com dados, não com conversa visível. Para a equipe ler e responder, você precisa de uma caixa de entrada como o Chatwoot. Os dois convivem bem: o n8n cuida da automação, o Chatwoot do humano.

### Uso o node nativo ou o HTTP Request?

Comece pelo node. Troque para HTTP Request quando precisar de um campo que ele não expõe, tipicamente botões, listas ou componentes de template mais elaborados.

### Meu webhook não recebe nada. Por onde começo?

Confira, nesta ordem: a URL registrada é exatamente a do nó de Webhook, ela é HTTPS com certificado válido, o fluxo está ativo (não em modo de teste, que só escuta uma chamada), e o campo `messages` está assinado do lado da Meta. O modo de teste do n8n é a causa mais comum.

### Por que meu fluxo entrou em laço e mandou dezenas de mensagens?

Porque ele está respondendo webhook de status, e não só mensagem de cliente. Cada envio seu gera três eventos de status, e responder a eles multiplica. Filtre pela existência de `messages` na entrada do fluxo.

### Recebo a mensagem duas vezes. Por quê?

Provavelmente o seu webhook demora a responder 200 e a Meta reentrega. Responda primeiro, processe depois. Guardar o `id` da mensagem e ignorar repetidos também resolve o caso de borda.

### Posso mandar mensagem para quem nunca falou comigo?

Só por template aprovado. Fora da janela de 24 horas, texto livre é recusado pela API. E template para lista fria é a causa número um de bloqueio de número, mesmo com API oficial.

### Quanto custa rodar isso?

São duas contas separadas: a do n8n, que depende de você usar a nuvem deles ou hospedar por conta própria, e a das mensagens, que você paga à Meta pela tabela dela. Confira as duas antes de orçar.

## Como decidir

Use o n8n se você quer montar a lógica sem escrever backend, ou já tem fluxos rodando e vai só acrescentar o WhatsApp. Se o objetivo é atendimento humano em equipe, comece pelo Chatwoot e deixe o n8n para o que for automático.

::cta: Antes de subir para produção, teste os três erros comuns | Mande um status de entrega para o seu fluxo e veja se ele quebra. Force uma resposta lenta e veja se chega mensagem duplicada. Dispare em lote e veja se bate no limite.

## Leia também
- [API oficial vs não oficial do WhatsApp](/api-oficial-vs-nao-oficial-whatsapp-2026)
- [Webhook: receber mensagens em tempo real](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [WhatsApp API oficial no Chatwoot](/whatsapp-api-oficial-chatwoot)
- [Quanto custa a WhatsApp Business API no Brasil](/quanto-custa-whatsapp-business-api-brasil-2026)

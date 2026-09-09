---
title: "Uma atualização da API quebrou minha integração. Como me proteger?"
description: "Campo que some, tipo de evento novo, categoria que não existia. A Meta evolui a API e quem tratou o payload como fixo quebra sem aviso."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "atualizacao-da-api-quebrou-minha-integracao"
cluster: "implementacao"
hero: "webhook"
intent: "problema-urgente"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/business-scoped-user-ids/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messaging-limits
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://app.datafyapi.com.br/docs
internal_links:
  - /o-telefone-esta-sumindo-do-webhook
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /a-mensagem-falhou-e-nao-sei-por-que
  - /webhook-chega-duplicado
  - /como-leio-o-historico-de-conversa-pela-api
status: aprovado
---

# Uma atualização da API quebrou minha integração. Como me proteger?

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** a Cloud API evolui, e o payload muda. Campo que existia some numa versão nova, aparece um tipo de mensagem que o seu código não conhece, uma categoria de conversa que não estava na lista. Quem tratou o payload como um contrato fixo quebra, e o sintoma costuma ser uma exceção no meio da noite.

A proteção é uma postura de código: **tratar campo como opcional, tratar valor desconhecido como esperado, e fixar a versão que você usa.**

::numeros: 3 padrões|que quebram: campo que some, tipo novo, valor novo ;; 1 versão|fixada na URL, e atualizada de propósito ;; opcional|é como todo campo deve ser tratado ;; padrão|todo switch precisa de um caso final

## Principais pontos
- **Fixe a versão** na URL das suas chamadas. Sem isso, uma mudança do lado de lá muda o seu comportamento sem você fazer nada.
- **Todo campo é opcional.** Um campo que sempre vem hoje pode não vir amanhã, e o exemplo atual disso é o telefone.
- **Todo `switch` precisa de um caso final.** Tipo de mensagem novo e categoria nova aparecem sem aviso, e um caso final que registra e segue evita a quebra.
- **Guarde o payload cru.** Quando um campo novo aparecer e você precisar dele, só quem guardou o bruto consegue reprocessar.
- Alguns campos são **descontinuados em favor de outros**, e quem lê o antigo passa a receber valor errado, e não um erro.

::diagrama: webhook-fluxo

## Os três padrões que quebram

**Campo que some.** O caso vivo hoje é o telefone: com a mudança para identificador por empresa, [o número só aparece se você falou com aquela pessoa nos últimos 30 dias](/o-telefone-esta-sumindo-do-webhook). Código que lê o telefone direto, sem checar se existe, começa a falhar para uma parte dos contatos.

**Tipo novo.** Aparece um tipo de mensagem que o seu código não conhece. Se você tem um `switch` fechado, sem caso final, ele estoura ou, pior, ignora silenciosamente e a mensagem se perde.

**Valor novo num campo conhecido.** O campo continua lá, mas com um valor que não estava na sua lista. Uma categoria de conversa nova, uma situação de template que não existia. Se você converte esse texto para um tipo fechado, a conversão falha.

Os três têm a mesma raiz: assumir que o payload de hoje é o payload de sempre.

## Como escrever para aguentar

**Fixe a versão na URL.**

```
https://graph.facebook.com/v21.0/{phone_number_id}/messages
```

E deixe isso numa variável, não espalhado. Assim atualizar a versão vira uma decisão, com teste, e não um susto.

**Leia campo com cuidado.**

```js
// frágil
const telefone = evento.contacts[0].wa_id

// resistente
const contato = evento.contacts?.[0] ?? {}
const telefone = contato.wa_id ?? null
const userId   = contato.user_id ?? null
```

**Tenha caso final em todo desvio por tipo.**

```js
switch (msg.type) {
  case 'text':  return tratarTexto(msg)
  case 'image': return tratarImagem(msg)
  case 'audio': return tratarAudio(msg)
  default:
    registrar('tipo de mensagem desconhecido', { tipo: msg.type, wamid: msg.id })
    return tratarComoNaoSuportado(msg)
}
```

O caso final não precisa saber o que fazer. Ele precisa **não derrubar o processo** e deixar registro para você descobrir depois.

**Guarde o bruto antes de interpretar.** É a rede de segurança de tudo: quando aparecer um campo que você quer usar, dá para voltar e reprocessar. Sem o bruto, o dado daquele período não existe.

## O que fazer quando quebrar

**Olhe o payload que causou.** Se você guarda o bruto, ele está lá. Comparar o que chegou com o que o código esperava resolve a maioria dos casos em minutos.

**Confira se o campo foi descontinuado.** Alguns campos são substituídos por outros, e o antigo passa a devolver valor incompleto em vez de erro. É o pior tipo de quebra, porque nada falha: só fica errado. Um exemplo atual é o campo de limite de envio, que mudou para uma versão do nível do portfólio.

**Confira a versão que você fixou.** Se ela estiver muito antiga, você pode estar perto do fim do suporte dela.

**Não conserte só o sintoma.** Se um campo ausente derrubou o processo, o conserto não é ler outro campo: é tratar ausência como caso normal em todo o handler.

## Monitorar sem virar ruído

Duas métricas simples avisam antes de o usuário reclamar:

**Tipos desconhecidos por dia.** Se o seu caso final registra, basta contar. Um número que sai de zero é uma novidade que chegou.

**Taxa de erro no processamento do webhook.** Um pico costuma ser mudança do outro lado, e não bug seu.

E uma prática: **assine os eventos de conta e de qualidade do número**. Além de servirem para o que existem, eles são o canal por onde chega aviso de coisa que muda no seu número.

## Perguntas frequentes

### Com que frequência a API muda?

Com frequência suficiente para justificar tudo acima. Campos são acrescentados sem aviso, e alguns são descontinuados com prazo.

### Preciso atualizar a versão sempre?

Não precisa correr, mas também não dá para congelar para sempre: versões saem de suporte. O caminho saudável é atualizar de propósito, com teste, e não por acidente.

### Se eu uso um provedor, isso me protege?

Em parte. Ele absorve mudança de endpoint e costuma manter o payload estável. Mas o formato do webhook continua sendo o da Meta, então o seu processamento ainda precisa aguentar campo novo.

### E se eu uso automação visual?

O mesmo vale, e é mais difícil de proteger: expressões que apontam para um caminho fixo no payload quebram quando o caminho muda. Vale ter uma condição inicial checando se o que você espera existe.

### Como fico sabendo do que vai mudar?

Acompanhando o registro de mudanças da documentação. Não é divertido, e é o que separa quem descobre lendo de quem descobre com o serviço parado.

### Vale a pena versionar o meu próprio processamento?

Se você guarda o payload cru, sim. Assim dá para reprocessar histórico com a lógica nova, o que é impossível se você só guardou os campos que interessavam na época.

## Como decidir

Se a sua integração é nova, adote os quatro hábitos agora: versão fixada, campo opcional, caso final e payload cru. Custam pouco no começo e evitam retrabalho.

Se ela já está rodando e já quebrou, comece pelo caso final nos desvios por tipo e pelo tratamento de campo ausente. São os dois que evitam a quebra derrubar o processamento inteiro por causa de uma mensagem.

::cta: Duas linhas que evitam a quebra mais comum | Um caso final no seu desvio por tipo de mensagem, e leitura de campo com valor padrão em vez de acesso direto. Com essas duas, o payload pode mudar que o seu processamento registra e segue.

## Leia também
- [O telefone está sumindo do webhook](/o-telefone-esta-sumindo-do-webhook)
- [Webhook: receber mensagens em tempo real](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [A mensagem falhou e eu não sei por quê](/a-mensagem-falhou-e-nao-sei-por-que)
- [Como leio o histórico de conversa pela API](/como-leio-o-historico-de-conversa-pela-api)

---
title: "A mensagem falhou e eu não sei por quê"
description: "A Meta manda o motivo da falha no webhook de status. Quase toda biblioteca descarta esse campo, e o desenvolvedor fica com um falhou sem explicação."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "a-mensagem-falhou-e-nao-sei-por-que"
cluster: "problemas"
hero: "erro"
intent: "problema-urgente"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messaging-limits
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/marketing-templates/per-user-limits
  - https://app.datafyapi.com.br/docs
internal_links:
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /minha-campanha-travou-no-meio
  - /webhook-chega-duplicado
  - /numero-banido-no-whatsapp-o-que-fazer
  - /quantas-mensagens-por-segundo-posso-enviar
status: aprovado
---

# A mensagem falhou e eu não sei por quê

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** a Meta **manda o motivo**. Ele vem no webhook de status, num campo de erros, com código e descrição. O problema é que quase toda biblioteca e quase todo conector **descarta esse campo** ao processar o evento, e o que chega até você é um "falhou" sem explicação.

Se o seu painel mostra mensagem com status de falha e nada além disso, o motivo existe e está sendo jogado fora antes de chegar em você.

::numeros: statuses|o evento onde o motivo chega, e não em messages ;; errors[]|o campo que costuma ser descartado ;; 1 código|por falha, que diz exatamente o que aconteceu ;; 14 relatos|do mesmo problema, em bibliotecas diferentes

## Principais pontos
- O motivo da falha chega no evento de **status**, e não no de mensagem. Quem só trata mensagem nunca vê.
- O campo de erros traz **código e descrição**. Com o código você sabe se reenviar, esperar ou parar.
- **Guarde o motivo junto com a mensagem.** Sem isso, a operação vê "falhou" e chuta.
- Nem toda falha pede a mesma reação. Algumas pedem espera, uma pede parar de vez, e reenviar na hora errada agrava.
- Esse mesmo evento de status é o que mais causa execução desnecessária em automação visual, porque é confundido com mensagem recebida.

::diagrama: webhook-fluxo

## Onde o motivo está

Quando uma mensagem falha, o webhook traz algo assim:

```json
{
  "statuses": [
    {
      "id": "wamid.XXXX",
      "status": "failed",
      "timestamp": "1757000000",
      "recipient_id": "5511999999999",
      "errors": [
        {
          "code": 131049,
          "title": "Message not delivered to maintain healthy ecosystem engagement"
        }
      ]
    }
  ]
}
```

O `errors` é o que interessa, e é justamente ele que costuma sumir. Muitos processadores leem `status` e `id`, gravam "falhou" e seguem em frente. O código, que é a única coisa acionável ali, não chega ao banco nem ao painel.

O primeiro passo é simples: **grave o campo inteiro**. Se o seu registro de mensagem não tem uma coluna para o código e outra para a descrição, ela precisa existir.

## Os códigos que aparecem no dia a dia

| Código | O que significa | O que fazer |
|---|---|---|
| `131049` | Limite por pessoa, ou tentativa em excesso | **Não reenviar.** Esperar pelo menos 24 h para aquele contato |
| `131050` | A pessoa optou por não receber marketing | Parar de enviar marketing para ela |
| `130429` | Estourou o throughput do número | Esperar e reenviar com intervalo crescente |
| `131026` | Não foi possível entregar ao destinatário | Conferir se o número existe e se está apto a receber |
| `131047` | Fora da janela, é preciso template | Enviar template aprovado |
| `132000` | Contagem de parâmetros não bate com o template | Corrigir os componentes do envio |
| `132001` | Template não existe naquele idioma | Conferir o código de idioma |

A lista completa é maior e muda com o tempo. O ponto é: **cada código pede uma reação diferente**, e o mesmo laço de reenvio para todos é o que transforma problema de entrega em problema de conta.

## Os dois que mais causam dano quando confundidos

Vale destacar, porque o par se parece e pede o oposto:

**`131049`** é limite do lado de quem recebe, somado entre todas as empresas que mandam mensagem para aquela pessoa. Não se contorna com mais número, nem com outro fornecedor. E **tentativa em excesso tem penalidade própria**, aplicada no nível da conta. Ou seja: um reenvio automático agressivo aqui não só não entrega, como piora.

**`131050`** é escolha da pessoa: ela optou por não receber marketing. Insistir por outro caminho é justamente o comportamento que a política proíbe.

Um sistema que trata os dois como "falha temporária, tenta de novo" está construindo o próprio bloqueio.

## Como montar o tratamento

**Grave sempre.** Código e descrição, junto com a mensagem, no momento em que o status chega.

**Classifique por comportamento**, e não por código individual. Três grupos resolvem quase tudo: *reenviar com espera*, para throughput e falha transitória; *parar com este contato*, para limite por pessoa e opt-out; *corrigir e reenviar*, para erro de template e de parâmetro.

**Alerte quando mudar o padrão.** Uma taxa de falha que sobe de repente é sinal de qualidade caindo ou de base ruim, e costuma anteceder problema maior.

**Mostre ao operador.** Se quem atende vê apenas "não entregue", ele vai reenviar na mão, que é o pior comportamento possível no caso do `131049`.

## O outro problema do mesmo evento

Já que o assunto é o webhook de status, vale lembrar do efeito colateral mais comum dele em automação visual: **cada mensagem que você envia gera vários eventos**, de enviada, entregue e lida. Se o seu fluxo não separa isso de mensagem recebida, cada envio dispara execuções extras, consome cota e, em alguns casos, faz o robô responder ao próprio status.

A separação é uma condição no início do fluxo, checando se o campo de mensagens existe. Se não existe, é status: registre e encerre. É a mesma linha que resolve [boa parte das duplicações](/webhook-chega-duplicado).

## Perguntas frequentes

### Por que meu painel não mostra o motivo?

Porque o processador descartou o campo. É o comportamento padrão de muita biblioteca, e a correção é do seu lado: gravar o campo inteiro quando o status chega.

### A API não devolve o erro na hora do envio?

Devolve para erro de requisição, tipo template inexistente ou parâmetro errado. Mas falha de **entrega** acontece depois, e por isso ela só aparece no webhook de status. Uma mensagem aceita com sucesso pode falhar minutos depois.

### Mensagem "enviada" quer dizer entregue?

Não. Enviada significa que saiu, entregue significa que chegou ao aparelho, e lida significa que a pessoa abriu. Cada um é um evento, e o pulo de enviada direto para falha é comum.

### Como sei se o número da pessoa existe?

Não existe uma consulta confiável para isso antes do envio. O caminho é enviar e tratar o resultado, mantendo a base limpa com base no histórico de falhas.

### Vale reenviar automaticamente?

Depende do código. Para throughput, sim, com espera crescente. Para limite por pessoa, não. Para opt-out, nunca. É por isso que classificar por comportamento importa mais que tratar cada código.

### Isso muda com o novo identificador de usuário?

O campo de identificação do destinatário no evento acompanha a mudança para identificador por empresa. Vale conferir se o seu processador não depende exclusivamente do telefone para casar o status com a mensagem enviada.

## Como decidir

Se você manda pouco, gravar o motivo já resolve: quando alguém perguntar por que não chegou, a resposta está no banco.

Se você manda em volume, classifique por comportamento e trate cada grupo do jeito certo. É o que separa uma operação que corrige a base de uma que insiste até a conta ser limitada.

::cta: Confira uma coisa no seu banco agora | Abra o registro de uma mensagem que falhou. Se não tem código nem descrição gravados, o motivo está sendo descartado antes de chegar em você, e toda a sua operação está no escuro sem precisar estar.

## Leia também
- [Webhook: receber mensagens em tempo real](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [Disparei a campanha e ela travou no meio](/minha-campanha-travou-no-meio)
- [Meu webhook recebe a mesma mensagem várias vezes](/webhook-chega-duplicado)
- [Número bloqueado no WhatsApp: o que fazer agora](/numero-banido-no-whatsapp-o-que-fazer)

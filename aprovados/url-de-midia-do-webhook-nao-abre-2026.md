---
title: "A URL da mídia que vem no webhook não abre. Por quê?"
description: "Ela devolve erro de autenticação no navegador e parece token errado. Não é: a mídia vem cifrada, e o caminho tem duas chamadas com cabeçalho nas duas."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "url-de-midia-do-webhook-nao-abre"
cluster: "implementacao"
hero: "erro"
intent: "problema-urgente"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/business-phone-numbers/media
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/audio-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=ZHYNjpu5ReE
videos: [ZHYNjpu5ReE]
internal_links:
  - /como-receber-midia-api-oficial-whatsapp
  - /erro-131053-ao-enviar-midia
  - /audio-chega-mudo-no-celular-do-cliente
  - /quanto-tempo-o-whatsapp-guarda-minhas-mensagens
  - /ver-payload-das-mensagens-em-tempo-real
status: aprovado
---

# A URL da mídia que vem no webhook não abre. Por quê?

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** porque ela **não é um endereço público**. O cliente manda uma foto, o webhook traz uma URL, você cola no navegador e recebe erro de autenticação. A conclusão natural é que o token está errado, e não está.

A mídia da Cloud API **vem cifrada**, e aquela URL é uma referência interna. Para chegar no arquivo são **duas chamadas**, e a segunda também exige o cabeçalho de autorização, que é justamente o passo em que quase todo mundo tropeça.

::numeros: 2 chamadas|para transformar identificador em arquivo ;; 2 cabeçalhos|as duas chamadas exigem autorização ;; 7 dias|até o identificador do webhook expirar ;; 0|URLs públicas dentro do payload

## Principais pontos
- **A URL do payload não abre em navegador**, e isso é comportamento esperado, não defeito.
- **O campo que interessa é o identificador**, e não a URL. É por ele que você busca o arquivo.
- **As duas chamadas exigem o cabeçalho.** Esquecer na segunda é o erro mais repetido do assunto.
- **O identificador expira em 7 dias.** Depois disso, não é intermitência, é prazo vencido.
- Se você recebe por uma plataforma que já entrega a URL resolvida, some uma etapa, e o prazo continua sendo da Meta.

::diagrama: webhook-fluxo

## O que está acontecendo

Quando o cliente manda uma mídia, o payload traz algo assim:

```json
"image": {
  "mime_type": "image/jpeg",
  "sha256": "...",
  "id": "1234567890"
}
```

Em alguns casos vem também uma URL. E ela é a fonte da confusão, porque parece um link comum.

Não é. O arquivo está guardado de forma cifrada na infraestrutura da Meta, e o acesso é autenticado. O navegador não manda o seu token, então a resposta é erro de autenticação.

Na descrição do Israel Henrique, CTO da Datafy: *"só que essa URL aqui não abre. Se você for tentar abrir aqui, ela não vai abrir, dá erro de autenticação. Então a gente precisa descriptografar essa URL."*

::video: ZHYNjpu5ReE | Quatro minutos com o problema inteiro na tela. Em 01:23 ele tenta abrir a URL do webhook e ela falha, em 01:55 mostra qual campo copiar, em 02:34 faz a chamada com o identificador e a imagem abre, e em 03:53 repete com áudio.

## As duas chamadas

**Primeira: trocar o identificador pelo endereço.**

```
GET https://graph.facebook.com/v21.0/{media_id}
Authorization: Bearer {token}
```

Volta a URL real, o tipo, o tamanho e o hash.

**Segunda: baixar.**

```
GET {url_devolvida}
Authorization: Bearer {token}
```

**A segunda chamada também precisa do cabeçalho.** Esse é o ponto. A URL devolvida parece um endereço qualquer, e não é: ela continua exigindo autenticação.

É o erro mais repetido da comunidade nesse assunto, aparecendo em cerca de oito discussões independentes, sempre com a mesma raiz. E o que torna ele traiçoeiro é que **o passo anterior funcionou**, então a suspeita recai sobre qualquer outra coisa.

## Os sintomas, e o que cada um quer dizer

| O que acontece | Causa provável |
|---|---|
| Erro de autenticação ao abrir no navegador | Comportamento esperado. Navegador não manda token |
| Primeira chamada funciona, segunda volta vazia ou com erro | Falta o cabeçalho na segunda |
| Arquivo baixa mas está corrompido | Resposta sendo salva como texto em vez de binário |
| Hash não bate | Download truncado. Repita |
| Funcionava e parou, para mensagens antigas | Identificador com mais de 7 dias, expirado |
| Funciona no `curl` e falha na ferramenta de fluxo | O nó não está configurado para binário, ou perdeu o cabeçalho |

Esse último merece nota porque é comum em automação visual: muitos nós de requisição tratam a resposta como texto por padrão, e o arquivo chega inutilizável. A configuração de resposta binária resolve.

## O prazo que vira erro fantasma

Um detalhe que faz gente procurar bug onde tem calendário: **o identificador de mídia que chega no webhook expira em 7 dias.**

Isso não é o mesmo prazo do arquivo que **você** sobe para enviar, que dura 30 dias. São dois números diferentes para dois sentidos diferentes, e confundi-los é o erro mais comum do assunto.

A consequência prática é de arquitetura: **baixe a mídia no momento em que ela chega**, e não quando alguém pedir. Processamento em lote semanal já está no limite; mensal encontra a maior parte fora de alcance.

E o efeito colateral disso aparece depois, em conformidade: se o seu produto promete histórico com anexos, [o que existe é o que você guardou](/quanto-tempo-o-whatsapp-guarda-minhas-mensagens).

## O que muda com a Datafy

**Não muda:** o prazo de 7 dias, os limites de tamanho e formato, e o fato de a mídia ser cifrada. Isso é da Meta.

**Muda o número de etapas.** A descriptografia já está resolvida: você manda o identificador que veio no webhook e recebe a URL pronta para uso, sem montar essa camada. Na frase dele: *"aqui a gente já fez esse trabalho para você."*

**Muda a depuração.** Quando algo não vem como esperado, dá para [ver o payload cru da mensagem](/ver-payload-das-mensagens-em-tempo-real) e confirmar qual identificador chegou, sem depender do log do seu servidor. Vale saber que mídia não aparece nesse log, só o aviso de que chegou.

## Perguntas frequentes

### É problema no meu token?

Quase certamente não. Se a primeira chamada funciona, o token está certo, e o que falta é o cabeçalho na segunda ou o tratamento binário da resposta.

### Posso guardar a URL e usar depois?

Não é boa ideia. Ela é temporária e autenticada. Guarde o **arquivo**, no seu armazenamento, e guarde o identificador da mensagem para referência.

### Por que a Meta não manda o arquivo no webhook?

Porque o payload ficaria enorme e o webhook precisa ser rápido. A entrega por identificador mantém o evento leve e deixa o download sob seu controle.

### Dá para saber o tamanho antes de baixar?

Dá. A primeira chamada devolve o tamanho, o que permite recusar arquivos acima do que o seu fluxo aguenta.

### E se eu recebo por uma plataforma intermediária?

Algumas já entregam a URL resolvida numa chamada. O prazo de 7 dias continua valendo, porque ele é da Meta.

### O áudio vem em qual formato?

OGG com codec Opus, que é o nativo do WhatsApp. Quase todo serviço de transcrição aceita direto. [O caso inverso, de enviar áudio, tem outra pegadinha](/audio-chega-mudo-no-celular-do-cliente).

## Como decidir

Se você só quer ver a imagem que o cliente mandou, as duas chamadas resolvem e você não precisa de mais nada. Lembre do cabeçalho na segunda.

Se mídia faz parte do produto, comprovante, foto de defeito, áudio de atendimento, trate como pipeline: baixe no recebimento, grave no seu armazenamento com o identificador da mensagem, confira o hash, e defina por quanto tempo você guarda.

A regra que resume: **o prazo de 7 dias não perdoa quem deixa para depois.**

::cta: Teste se o seu fluxo perde mídia antiga | Pegue uma mensagem com anexo de mais de uma semana atrás e tente baixar pelo identificador. Se falhar, o seu processamento está fora do prazo, e a correção é buscar no recebimento.

## Leia também
- [Como receber imagem, áudio e documento pela API](/como-receber-midia-api-oficial-whatsapp)
- [Erro 131053 ao enviar mídia](/erro-131053-ao-enviar-midia)
- [O áudio que eu mando chega mudo no celular do cliente](/audio-chega-mudo-no-celular-do-cliente)
- [Quanto tempo o WhatsApp guarda minhas mensagens](/quanto-tempo-o-whatsapp-guarda-minhas-mensagens)

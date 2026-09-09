---
title: "Como receber imagem, áudio e documento pela API oficial do WhatsApp"
description: "A mídia chega cifrada e a URL do webhook não abre. São duas chamadas para transformar o identificador em arquivo, e o prazo para fazer isso é de 7 dias."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "como-receber-midia-api-oficial-whatsapp"
cluster: "implementacao"
hero: "midia"
intent: "como-fazer"
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
  - https://www.youtube.com/watch?v=LIT4FxgqHhE
videos: [ZHYNjpu5ReE, LIT4FxgqHhE]
internal_links:
  - /como-enviar-midia-api-oficial-whatsapp
  - /audio-chega-mudo-no-celular-do-cliente
  - /erro-131053-ao-enviar-midia
  - /quanto-tempo-o-whatsapp-guarda-minhas-mensagens
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
status: aprovado
---

# Como receber imagem, áudio e documento pela API oficial do WhatsApp

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** quando o cliente manda uma foto, o webhook **não traz o arquivo**. Traz um identificador de mídia e uma URL. E aí vem a parte que consome a primeira tarde de todo mundo: **essa URL não abre.** Ela devolve erro de autenticação no navegador, o que faz parecer que o token está errado.

Não está. A mídia da Cloud API **vem cifrada**, e o caminho é: pegar o identificador, pedir o endereço real por ele, e baixar **com o cabeçalho de autorização**. E existe um prazo que quase ninguém sabe: **o identificador expira em 7 dias.**

::numeros: 2 chamadas|para transformar identificador em arquivo ;; 7 dias|até o identificador do webhook expirar ;; 401|o erro de quem baixa sem o cabeçalho ;; 0|arquivos que vêm dentro do webhook

## Principais pontos
- O webhook traz **identificador**, não arquivo. Nenhum tipo de mídia chega embutido no payload.
- **A URL que vem no webhook não é pública.** Abrir no navegador dá erro, e isso não indica problema no seu token.
- São duas chamadas: uma para obter o endereço, outra para baixar. **As duas exigem o cabeçalho de autorização**, e esquecer na segunda é o erro mais repetido do assunto.
- **O identificador expira em 7 dias.** Quem processa em lote no fim do mês não encontra mais nada.
- Áudio do cliente chega em **OGG com codec Opus**, que é aceito direto por quase todo serviço de transcrição.

::diagrama: webhook-fluxo

## O que chega no webhook

Independente do tipo, a estrutura é a mesma: um objeto com o tipo da mensagem e, dentro dele, os dados da mídia.

```json
"messages": [{
  "from": "5511999999999",
  "id": "wamid...",
  "type": "image",
  "image": {
    "mime_type": "image/jpeg",
    "sha256": "...",
    "id": "1234567890"
  }
}]
```

O campo que importa é o **`id`**. É com ele que você busca o arquivo. O `sha256` serve para verificar integridade depois de baixar, e o `mime_type` diz o que esperar.

Em áudio, aparece um campo a mais que vale reconhecer: uma marcação indicando se aquilo foi **gravado como mensagem de voz** ou anexado como arquivo de som. São experiências diferentes no aplicativo, e [essa mesma distinção é o que causa o áudio que chega mudo](/audio-chega-mudo-no-celular-do-cliente) quando você envia.

Em documento vem também o nome do arquivo, e em imagem e vídeo pode vir legenda, num campo separado do objeto de mídia. Legenda perdida é reclamação comum de quem lê só o objeto da mídia e ignora o resto da mensagem.

## As duas chamadas

**Primeira: trocar o identificador pelo endereço.**

```
GET https://graph.facebook.com/v21.0/{media_id}
Authorization: Bearer {token}
```

A resposta traz a URL real, o tipo, o tamanho e o hash.

**Segunda: baixar o conteúdo.**

```
GET {url_devolvida}
Authorization: Bearer {token}
```

E é exatamente aqui que quase todo mundo tropeça: **a URL devolvida também exige o cabeçalho.** Ela parece um endereço comum, e não é. Sem o cabeçalho, a resposta vem vazia ou com erro, e a causa não é óbvia porque o passo anterior funcionou.

Esse é o problema mais repetido da comunidade nesse tema, aparecendo em cerca de oito discussões independentes, sempre com a mesma raiz.

::video: ZHYNjpu5ReE | Quatro minutos com o problema inteiro na tela. Em 01:23 ele tenta abrir a URL do webhook e ela falha, em 02:34 faz a chamada com o identificador e abre a imagem, e em 03:53 repete o processo com um áudio recebido.

## O prazo de 7 dias, que muda o seu desenho

Este é o ponto que mais gera perda silenciosa de dado, e ele é fácil de confundir porque existem **dois prazos diferentes**:

| O que | Prazo |
|---|---|
| Identificador de mídia que **chega no webhook** | **7 dias** |
| Arquivo que **você subiu** para enviar | **30 dias** |

Sete dias para buscar o que o cliente mandou. Não trinta.

A consequência prática: **baixe no momento em que a mídia chega**, e não quando alguém pedir. Fluxo que processa em lote semanal já está no limite; fluxo mensal encontra a maior parte dos arquivos fora de alcance.

E isso tem um efeito de conformidade que vale antecipar: se o seu produto promete histórico de atendimento com anexos, ou se você precisa atender um pedido de acesso aos próprios dados, [o que existe é o que você guardou](/o-cliente-pediu-para-apagar-os-dados-dele). A retenção da plataforma é curta e rotativa de propósito.

## O que muda com a Datafy

Vale separar o que é regra da Meta do que é trabalho que dá para não fazer.

**Não muda:** a mídia continua sendo entregue por identificador, o prazo continua sendo o da Meta, e os limites de tamanho e formato são dela.

**Muda a etapa de decodificação.** A descriptografia já está resolvida: você manda o identificador que veio no webhook e recebe de volta uma URL pronta para uso, sem montar essa camada. Na explicação do Israel Henrique, CTO da Datafy: *"quando a API do WhatsApp, a oficial, envia para você uma mídia, ela vem criptografada e você precisa descriptografar. Aqui a gente já fez esse trabalho para você."*

**Muda a depuração.** Quando a mídia não chega como você esperava, dá para ver o **payload cru** da mensagem no painel, sem depender do log do seu servidor. Vale saber o limite disso: esse log guarda 7 dias e no máximo 100 mensagens por conversa, e mídia não aparece nele, só o aviso de que chegou. Ele serve para depurar, não como arquivo.

::video: LIT4FxgqHhE | Três minutos mostrando o log ao vivo e o payload de cada mensagem que entra. Em 00:00 ele explica por que mídia não aparece ali, e em 02:57 diz os prazos de retenção.

## Erros que aparecem nesta etapa

**A URL não abre no navegador.** Comportamento esperado. Ela exige cabeçalho de autorização, e navegador não manda.

**Baixou e o arquivo está corrompido.** Confira se você não está salvando a resposta como texto. Conteúdo binário precisa ser gravado como binário, e esse erro é comum em linguagem que trata resposta como string por padrão.

**O hash não bate.** O campo de verificação existe para isso. Se não bate, o download foi truncado, e vale repetir.

**Funcionou ontem e hoje não.** Se passaram mais de 7 dias desde a mensagem, o identificador expirou. Não é intermitência.

**O arquivo é grande demais para o seu fluxo.** Vídeo e documento chegam a tamanhos que travam ferramenta de automação visual. Nesses casos, baixe pelo servidor e passe adiante só a referência.

## Perguntas frequentes

### Por que a Meta não manda o arquivo direto no webhook?

Porque o payload ficaria enorme e o webhook precisa ser rápido. O desenho por identificador mantém a entrega leve e deixa o download sob seu controle.

### Preciso baixar toda mídia que chega?

Só a que você vai usar depois. Mas decida no momento em que ela chega, porque o identificador vale 7 dias. A regra segura, para quem tem produto, é baixar sempre e limpar depois pela sua política de retenção.

### Qual o formato do áudio que o cliente manda?

OGG com codec Opus, que é o formato nativo do WhatsApp. Quase todo serviço de transcrição aceita direto, sem conversão.

### A legenda da imagem vem junto?

Vem, num campo separado do objeto de mídia. Quem lê só o objeto da mídia perde a legenda.

### Dá para saber o tamanho antes de baixar?

Dá. A primeira chamada devolve o tamanho junto com o endereço, e isso permite recusar arquivo acima do que o seu fluxo aguenta.

### E se eu usar automação visual?

O mesmo caminho vale, com um cuidado: configure o nó de download para tratar a resposta como binário e lembre do cabeçalho de autorização na segunda chamada. É o passo que mais falha em ferramenta de fluxo.

## Como decidir

Se você recebe mídia esporádica e só quer ver a imagem, as duas chamadas resolvem e você não precisa de mais nada.

Se mídia faz parte do produto, comprovante, foto de defeito, áudio de atendimento, então trate como pipeline: baixe no recebimento, grave no seu armazenamento com o identificador da mensagem, verifique o hash, e defina há quanto tempo você guarda. O prazo de 7 dias não perdoa quem deixa para depois.

::cta: Descubra hoje se o seu fluxo está perdendo mídia | Pegue uma mensagem com anexo de mais de uma semana atrás e tente baixar pelo identificador. Se falhar, o seu processamento está fora do prazo de 7 dias, e o conserto é baixar no recebimento.

## Leia também
- [Como enviar imagem, documento e áudio pela API](/como-enviar-midia-api-oficial-whatsapp)
- [O áudio que eu mando chega mudo no celular do cliente](/audio-chega-mudo-no-celular-do-cliente)
- [Erro 131053 ao enviar mídia](/erro-131053-ao-enviar-midia)
- [Quanto tempo o WhatsApp guarda minhas mensagens](/quanto-tempo-o-whatsapp-guarda-minhas-mensagens)

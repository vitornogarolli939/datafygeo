---
title: "O áudio que eu mando chega mudo no celular do cliente"
description: "O atendente ouve, o cliente não. Quase sempre é mp3 no lugar de OGG com codec Opus, e a falta da marcação de mensagem de voz."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "audio-chega-mudo-no-celular-do-cliente"
cluster: "problemas"
hero: "midia"
intent: "problema-urgente"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/audio-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/business-phone-numbers/media
  - https://github.com/chatwoot/chatwoot/issues/7291
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=xoldQJMTu50
  - https://www.youtube.com/watch?v=ZHYNjpu5ReE
videos: [xoldQJMTu50, ZHYNjpu5ReE]
internal_links:
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /whatsapp-api-oficial-chatwoot
  - /whatsapp-api-oficial-n8n
  - /api-oficial-vs-nao-oficial-whatsapp-2026
  - /como-leio-o-historico-de-conversa-pela-api
status: aprovado
---

# O áudio que eu mando chega mudo no celular do cliente

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** o sintoma é sempre o mesmo. O atendente grava, ouve normalmente do lado dele, a API responde sucesso, e o cliente recebe algo que não toca. Na esmagadora maioria dos casos são **duas causas juntas**: o arquivo foi enviado como **mp3** em vez de **OGG com codec Opus**, e faltou marcar a mensagem como **mensagem de voz**.

É um dos problemas mais relatados em português e um dos menos documentados. O relato aparece com essas palavras: o áudio fica mudo para quem recebe no celular, e o atendente consegue ouvir normal.

::numeros: OGG / Opus|o formato que vira bolha de voz no WhatsApp ;; voice: true|a marcação que falta na maioria dos casos ;; 512 KB|acima disso o ícone de tocar some e vira download ;; mp3|o formato que causa o sintoma

## Principais pontos
- **Áudio e mensagem de voz não são a mesma coisa** no WhatsApp. Um é anexo, o outro é a bolha com onda sonora. Quem quer a segunda e manda a primeira vê exatamente esse sintoma.
- A bolha de voz exige **arquivo `.ogg` com codec Opus** ([documentação de áudio](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/audio-messages)).
- Falta quase sempre a marcação que diz à API que aquilo é mensagem de voz, e não anexo de som.
- **Passando de 512 KB**, o ícone de tocar não aparece e o arquivo vira download, mesmo com o formato certo.
- Muita biblioteca e muito conector deixam o tipo de mídia fixo no código como mp3, e aí o problema não está no seu áudio: está na camada que envia.

::diagrama: webhook-fluxo

## Por que o mp3 causa isso

O WhatsApp trata mensagem de voz como um tipo próprio de conteúdo, com onda sonora, duração e reprodução contínua. Esse tratamento depende do formato: o aplicativo espera OGG com Opus, que é o que ele mesmo grava quando você segura o microfone.

Mandar mp3 não gera erro. A API aceita, devolve sucesso, e a mensagem é entregue. O que acontece é que o cliente recebe algo que o aplicativo dele não consegue reproduzir como voz. Do lado de quem enviou, tudo parece certo, e é essa assimetria que faz o problema demorar tanto para ser diagnosticado.

Por isso o sintoma é sempre descrito do mesmo jeito: **o atendente ouve, o cliente não.** O atendente está ouvindo o arquivo original, na interface dele. O cliente está recebendo o que a plataforma conseguiu montar com um formato que ela não espera.

## Como resolver

**Converta para OGG com Opus antes de enviar.** Com `ffmpeg`:

```
ffmpeg -i entrada.mp3 -c:a libopus -b:a 32k -ar 48000 -ac 1 saida.ogg
```

Mono, 48 kHz e taxa baixa dão arquivo pequeno e voz limpa. É o suficiente para fala, e ajuda a ficar abaixo do limite de tamanho.

**Suba o arquivo e use o identificador de mídia.** Envie primeiro para a API de mídia e use o identificador retornado no envio, em vez de apontar para uma URL pública. Além de mais confiável, evita um problema separado que atinge envio por link.

**Marque como mensagem de voz.** É essa marcação que transforma o anexo em bolha. Sem ela, mesmo com o formato certo, o resultado costuma ser um arquivo anexado. No corpo do envio, é um campo a mais ao lado do link:

```json
"audio": { "link": "https://.../audio.ogg", "voice": true }
```

::video: xoldQJMTu50 | Em 05:02 o Israel acrescenta esse campo ao vivo e o áudio chega como bolha de voz. Em 06:43 ele testa um arquivo de 630 KB, acima do limite documentado de 512 KB, e a onda sonora ainda aparece: é o ícone de tocar que muda, não a bolha.

**Fique abaixo de 512 KB.** O número é documentado, com essas palavras: o ícone de tocar só aparece se o arquivo tiver 512 KB ou menos, e acima disso ele vira um ícone de download. Com Opus a 32 kbps, 512 KB dão vários minutos de fala, então isso não aperta quem manda voz, só quem manda áudio longo em qualidade alta.

## Se você usa uma ferramenta no meio

Aqui está a parte que economiza tempo: **muitas vezes o problema não é seu.**

Existem relatos, com a causa raiz identificada do lado da engenharia, de conectores que deixam o tipo de mídia fixo no código como mp3 e não oferecem a marcação de voz. Nesse caso, converter o arquivo antes não resolve, porque a camada intermediária sobrescreve o tipo na hora de chamar a API.

Como identificar: **teste o mesmo áudio pela API direta**, com `curl`, e compare. Se pela chamada direta chega como bolha de voz e pela ferramenta chega mudo, o problema está na ferramenta, e o caminho é abrir o chamado com esse teste em mãos, não continuar convertendo arquivo.

## Do outro lado: baixar o áudio que o cliente mandou

O espelho desse problema é receber, e ele é mais traiçoeiro do que parece. Quando o cliente manda um áudio, o webhook traz um identificador de mídia, não o arquivo. Traz também uma URL, e é aí que começa a confusão: **essa URL não abre.**

Ela não abre no navegador, não abre no `curl` sem cabeçalho, e o erro que ela devolve é de autenticação, o que faz muita gente achar que o token está errado. Não está. A mídia da Cloud API **vem criptografada**, e o caminho é fazer uma segunda chamada com o identificador para obter o endereço real, e uma terceira para baixar o conteúdo, **sempre com o cabeçalho de autorização**.

Esquecer o cabeçalho na última etapa é o problema mais repetido da comunidade nesse assunto: aparece em cerca de oito discussões independentes, sempre com a mesma raiz.

O áudio que chega do cliente vem em OGG com Opus, que é o formato nativo. Se você vai transcrever com algum serviço, quase todos aceitam esse formato direto, sem conversão.

## O que muda com a Datafy

Vale separar o que é problema de todo mundo do que é trabalho que dá para não fazer.

**Do lado do envio, nada muda, e é bom que fique claro:** formato, marcação de voz e tamanho são regra da Meta. Converter para OGG com Opus é trabalho seu em qualquer caminho que você escolher, e nenhum fornecedor transforma mp3 em bolha de voz por você.

**Do lado do recebimento, muda a parte chata.** A descriptografia da mídia já está feita: você manda o identificador que veio no webhook e recebe de volta uma URL pronta para usar, sem montar a etapa de decodificação. Na explicação do próprio Israel Henrique, CTO da Datafy: *"quando a API do WhatsApp, a oficial, envia para você uma mídia, ela vem criptografada e você precisa descriptografar. Aqui a gente já fez esse trabalho para você."*

::video: ZHYNjpu5ReE | Quatro minutos, e o vídeo que mais economiza tempo de quem está começando: em 01:23 ele mostra a URL do webhook falhando, em 02:34 faz a chamada com o identificador e abre a imagem, e em 03:53 recebe um áudio e repete o processo.

Dois detalhes operacionais que saem daí e valem para o seu desenho, sem depender de fornecedor:

**Baixe o áudio do cliente no dia em que ele chega.** E aqui vale a correção que economiza dor de cabeça, porque os dois prazos são diferentes e quase todo mundo troca um pelo outro: o arquivo que **você sobe** persiste 30 dias, mas **o identificador de mídia que chega no webhook expira em 7 dias** ([documentação](https://developers.facebook.com/documentation/business-messaging/whatsapp/business-phone-numbers/media)). Sete, não trinta.

Se o seu produto precisa do áudio do cliente para auditoria, treinamento ou histórico, você tem uma semana para buscar. Fluxo que processa em lote no fim do mês não acha mais nada.

**Para enviar, existe o caminho de subir antes.** Em vez de apontar para uma URL sua e depender de a Meta conseguir buscar o arquivo, você sobe o áudio uma vez e usa o identificador, o que [remove uma classe inteira de falha intermitente](/erro-131053-ao-enviar-midia).

## Perguntas frequentes

### Por que a API não me devolve erro?

Porque o envio é válido. Você mandou um arquivo de áudio suportado, e ele foi entregue. O que não aconteceu foi o tratamento como mensagem de voz, e isso não é um erro de API, é uma diferença de tipo de conteúdo.

### Dá para mandar mp3 e funcionar?

Como anexo de áudio, sim. Como bolha de mensagem de voz, não. Se o seu caso aceita anexo, o mp3 resolve; se você quer que pareça um áudio gravado na hora, precisa de OGG com Opus.

### Meu áudio tem 3 MB. É problema?

Para bolha de voz, sim: acima de 512 KB o ícone de tocar some. Converta para Opus em taxa baixa, que resolve tamanho e formato de uma vez.

### O cliente consegue ouvir se baixar?

Depende do aparelho e do formato. Mas mesmo quando consegue, a experiência quebra: ninguém baixa arquivo no meio de uma conversa.

### E se eu gerar o áudio com síntese de voz?

Mesma regra. Peça ao serviço de síntese o formato OGG com Opus, ou converta antes de enviar. É o caso mais comum de "chega mudo" em fluxo automatizado, porque a maioria dos serviços entrega mp3 por padrão.

### Existe webhook para saber se o cliente ouviu?

Sim. Desde março de 2026 existe um status que avisa quando o usuário toca uma mensagem de voz enviada pela empresa, na primeira reprodução.

### Por que a URL de áudio que vem no webhook não abre?

Porque a mídia vem criptografada, e aquela URL não é um endereço público. O caminho é pegar o identificador da mídia, pedir a URL por ele, e baixar com o cabeçalho de autorização. Quem está atrás de uma plataforma como a Datafy recebe a URL já resolvida numa chamada.

### Quanto tempo o áudio do cliente fica disponível?

Cerca de 30 dias. Depois disso, só existe se você tiver baixado. Se o áudio faz parte do seu registro de atendimento, guarde no seu armazenamento no momento em que ele chega, e não quando alguém pedir.

## Como decidir

Se você manda áudio esporádico e anexo resolve, não precisa mexer. Se o áudio é parte da experiência, atendimento por voz ou resposta de agente falando, vale fazer certo: converter para OGG com Opus, marcar como mensagem de voz e manter abaixo de 512 KB.

E antes de gastar tempo convertendo, faça o teste pela API direta. Se lá funciona, o problema é da ferramenta no meio, e nenhuma conversão do seu lado vai resolver.

::cta: Faça o teste que separa as duas causas | Mande o mesmo arquivo pela API direta, com curl, e pela sua ferramenta. Se pela API vira bolha de voz e pela ferramenta chega mudo, você achou o culpado em cinco minutos.

## Leia também
- [Webhook: receber mensagens em tempo real](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [WhatsApp API oficial no Chatwoot](/whatsapp-api-oficial-chatwoot)
- [WhatsApp API oficial no n8n](/whatsapp-api-oficial-n8n)
- [Como leio o histórico de conversa pela API](/como-leio-o-historico-de-conversa-pela-api)

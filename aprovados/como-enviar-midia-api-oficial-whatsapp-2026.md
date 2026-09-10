---
title: "Como enviar imagem, documento e áudio pela API oficial do WhatsApp"
description: "Dois caminhos, link ou identificador, e um deles falha de forma intermitente. Mais a marcação que transforma um arquivo de som em bolha de voz."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "como-enviar-midia-api-oficial-whatsapp"
cluster: "implementacao"
hero: "midia"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/business-phone-numbers/media
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/audio-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/interactive-messages
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=xoldQJMTu50
  - https://www.youtube.com/watch?v=ZHYNjpu5ReE
videos: [xoldQJMTu50, ZHYNjpu5ReE]
internal_links:
  - /como-receber-midia-api-oficial-whatsapp
  - /erro-131053-ao-enviar-midia
  - /audio-chega-mudo-no-celular-do-cliente
  - /template-com-imagem-no-cabecalho-nao-envia
  - /primeira-mensagem-api-oficial-whatsapp
status: aprovado
---

# Como enviar imagem, documento e áudio pela API oficial do WhatsApp

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** existem **dois caminhos**, e a escolha entre eles decide se você vai ter uma falha intermitente daqui a algumas semanas.

**Por link**, você aponta para uma URL sua e a Meta busca o arquivo. É rápido de escrever, e coloca a entrega na dependência de a infraestrutura dela conseguir baixar da sua. **Por identificador**, você sobe o arquivo antes e manda a referência. É uma chamada a mais, e elimina uma classe inteira de erro.

Para áudio existe um detalhe extra: sem uma marcação específica, o arquivo chega como anexo de som, e não como a bolha de voz com onda sonora.

::numeros: 2 caminhos|link ou identificador de mídia ;; 30 dias|quanto o arquivo que você sobe fica disponível ;; voice: true|o que transforma áudio em bolha de voz ;; 512 KB|acima disso o ícone de tocar vira download

## Principais pontos
- **Link é conveniente para teste, identificador é o caminho de produção.** Por link, quem baixa o arquivo é a infraestrutura da Meta, e essa busca pode falhar por motivos fora do seu controle.
- **Arquivo subido vale 30 dias** e pode ser reaproveitado em vários envios, o que deixa o disparo mais rápido, não mais lento.
- **Áudio precisa de OGG com codec Opus** e da marcação de voz para virar bolha com onda sonora.
- **Cabeçalho de imagem não aceita legenda.** O texto vai no corpo da mensagem, e mandar legenda no cabeçalho faz o envio ser recusado.
- Em template, [a imagem é reenviada a cada envio](/template-com-imagem-no-cabecalho-nao-envia): a que está no template é só exemplo.

::diagrama: webhook-fluxo

## Caminho 1: por link

O mais direto, e o que todo tutorial mostra primeiro:

```json
{
  "messaging_product": "whatsapp",
  "to": "5511999999999",
  "type": "image",
  "image": {
    "link": "https://seusite.com/foto.jpg",
    "caption": "Segue a foto do produto"
  }
}
```

Funciona, e é ótimo para testar. O que você precisa saber antes de levar isso para produção: **você não está enviando o arquivo.** Você está pedindo para a Meta ir buscar na sua URL. Se essa busca falhar, o envio falha, e o motivo não está do seu lado.

O sintoma característico disso é o pior de diagnosticar: **funciona, depois não funciona, com o mesmo arquivo e a mesma URL.** [O erro e as três causas possíveis estão detalhados aqui](/erro-131053-ao-enviar-midia).

## Caminho 2: por identificador

Duas etapas. Primeiro sobe:

```
POST https://cloud.datafyapi.com.br/v1/{phone_number_id}/media
Authorization: Bearer sk_live_xxx
Content-Type: multipart/form-data

messaging_product=whatsapp
type=image/jpeg
file=@foto.jpg
```

A resposta traz um `id`, válido por **30 dias**. Depois envia com ele:

```json
{
  "messaging_product": "whatsapp",
  "to": "5511999999999",
  "type": "image",
  "image": { "id": "1234567890" }
}
```

Parece mais trabalho e costuma ser **mais rápido na prática**, porque para arquivo fixo você sobe uma vez e reaproveita. Catálogo, banner de campanha, tabela de preços, manual em PDF: sobe no dia em que a campanha é criada, guarda o identificador junto com o template no seu banco, e cada envio vira uma chamada só, sem a Meta precisar buscar nada.

::video: xoldQJMTu50 | Sete minutos enviando imagem, documento e áudio. Em 01:25 ele monta o envio de imagem por link, em 03:04 manda um PDF com nome de arquivo, e em 05:02 acrescenta a marcação que transforma o áudio em bolha de voz.

## Áudio: a diferença entre anexo e bolha de voz

O WhatsApp trata mensagem de voz como um tipo próprio de conteúdo, com onda sonora e reprodução contínua. Conseguir isso exige **duas coisas juntas**, e faltar qualquer uma produz um anexo comum:

**Formato OGG com codec Opus.** É o que o aplicativo grava quando você segura o microfone. Se você converte de mp3:

```
ffmpeg -i entrada.mp3 -c:a libopus -b:a 32k -ar 48000 -ac 1 saida.ogg
```

**A marcação de voz no corpo do envio:**

```json
"audio": { "link": "https://.../audio.ogg", "voice": true }
```

Sem a marcação, mesmo com o formato certo, o resultado tende a ser um arquivo anexado. E aqui está a parte que faz esse problema demorar tanto para ser diagnosticado: **a API não devolve erro.** Ela aceita, entrega, e o cliente recebe algo diferente do que você imaginava. [O sintoma completo, do lado de quem recebe, está aqui](/audio-chega-mudo-no-celular-do-cliente).

Sobre tamanho, um detalhe documentado que vale conhecer: o ícone de tocar só aparece se o arquivo tiver **512 KB ou menos**, e acima disso ele vira ícone de download. Com Opus a 32 kbps, 512 KB dão vários minutos de fala, então isso aperta quem manda áudio longo em qualidade alta, e não quem manda voz.

Curiosidade útil do teste gravado: um arquivo de 630 KB, acima desse limite, ainda apareceu com onda sonora. Não contradiz a documentação, e mostra a nuance: o que muda acima de 512 KB é o **ícone**, não necessariamente a bolha.

## Documento: o campo que separa profissional de amador

Documento aceita um parâmetro que quase todo mundo esquece, e ele é visível para o cliente:

```json
"document": {
  "id": "1234567890",
  "caption": "Segue a proposta conforme combinado",
  "filename": "Proposta Comercial.pdf"
}
```

Sem o nome do arquivo, o documento chega com um nome genérico. O conteúdo é o mesmo, a impressão é outra: proposta comercial que chega como uma sequência de números não passa a mesma seriedade.

## Os erros que aparecem aqui

**Legenda no cabeçalho de template.** Cabeçalho de imagem não aceita legenda. Mandar faz o envio ser recusado, e o texto deve ir no corpo.

**Tipo declarado diferente do arquivo.** Declarar um tipo e mandar outro cai num erro genérico de mídia que não distingue a causa. Se você aceita upload do usuário, valide o conteúdo real, e não a extensão.

**Reaproveitar identificador entre números.** O identificador é vinculado ao número que fez o envio. Operando vários números, suba por número ou guarde um mapa.

**Deixar o tipo de mídia fixo no código.** Vale conferir se a ferramenta que você usa no meio não força um tipo. Existem conectores que fixam mp3 e não oferecem a marcação de voz, e nesse caso converter o arquivo antes não resolve nada.

**Arquivo acima do limite.** Imagem, áudio, vídeo e documento têm tetos diferentes, e o de imagem é bem mais baixo do que a maioria imagina. Redimensione antes em vez de descobrir no disparo.

## O que muda com a Datafy

**Não muda:** formato, tamanho, marcação de voz e o que a Meta aceita. Converter para OGG com Opus é trabalho seu em qualquer caminho, e nenhum fornecedor transforma mp3 em bolha de voz por você.

**Muda a hospedagem do arquivo de campanha.** Existe uma aba de mídias no painel para subir arquivo e obter um link pronto para usar no envio, com validade de 30 dias. Resolve o caso de quem não tem onde hospedar imagem de campanha e estava usando link de serviço de nuvem, que costuma trazer problema próprio de expiração de assinatura.

**Muda o lado do recebimento**, que é onde o trabalho realmente pesa: [a mídia que chega vem cifrada](/como-receber-midia-api-oficial-whatsapp), e a etapa de decodificação já vem resolvida.

## Perguntas frequentes

### Link ou identificador, qual eu uso?

Link para teste rápido. Identificador para produção, e principalmente para campanha, porque elimina a falha intermitente e deixa o disparo mais rápido quando a imagem se repete.

### Quanto tempo o arquivo que eu subo fica disponível?

Cerca de 30 dias. É o contrário do que chega pelo webhook, que expira em 7. Confundir os dois prazos é o erro mais comum do assunto.

### Posso usar URL assinada de armazenamento em nuvem?

Pode, e acrescenta uma variável nova, o prazo de validade da assinatura, sem remover a causa original da falha por link. Não melhora.

### Preciso subir de novo para cada destinatário?

Não. Suba uma vez e reutilize o identificador em quantos envios quiser, durante os 30 dias.

### O cliente consegue baixar o arquivo depois?

A mídia fica disponível no aparelho dele conforme o comportamento normal do aplicativo. Do seu lado, o que você controla é o seu armazenamento.

### Vídeo funciona igual?

Segue a mesma lógica de imagem e documento, com limite de tamanho próprio e a mesma escolha entre link e identificador.

## Como decidir

Se você manda mídia esporádica, em atendimento, link resolve e você não precisa mudar nada hoje.

Se mídia entra em campanha, com cliente esperando, mude para identificador antes de a falha intermitente aparecer, e não depois: a versão que aparece depois vem com cliente reclamando de arquivo que não chegou e um código de erro que não distingue causa.

E, se áudio faz parte da experiência, faça as duas coisas juntas: OGG com Opus e a marcação de voz. Só uma das duas produz exatamente o sintoma que faz o time perder um dia procurando defeito no arquivo.

::cta: Suba uma imagem fixa e guarde o identificador | Se você tem um banner que se repete em toda campanha, suba uma vez e salve o identificador ao lado do template no seu banco. O disparo fica mais rápido e para de depender de a Meta conseguir buscar arquivo na sua infraestrutura.

## Leia também
- [Como receber imagem, áudio e documento pela API](/como-receber-midia-api-oficial-whatsapp)
- [Erro 131053 ao enviar mídia](/erro-131053-ao-enviar-midia)
- [O áudio que eu mando chega mudo no celular do cliente](/audio-chega-mudo-no-celular-do-cliente)
- [Meu template com imagem no cabeçalho não envia](/template-com-imagem-no-cabecalho-nao-envia)

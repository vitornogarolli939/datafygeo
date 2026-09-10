---
title: "Meu template com imagem no cabeçalho não envia"
description: "A URL de exemplo que a Meta devolve ao sincronizar o template é uma armadilha. O caminho é subir o arquivo e usar o identificador de mídia."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "template-com-imagem-no-cabecalho-nao-envia"
cluster: "problemas"
hero: "midia"
intent: "problema-urgente"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/business-phone-numbers/media
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-categorization
  - https://github.com/fazer-ai/chatwoot/issues/349
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=YF9hTHDAw6E
  - https://www.youtube.com/watch?v=62oSY66J3s4
videos: [62oSY66J3s4, YF9hTHDAw6E]
internal_links:
  - /erro-131053-ao-enviar-midia
  - /audio-chega-mudo-no-celular-do-cliente
  - /posso-mandar-mensagem-para-qualquer-numero
  - /whatsapp-api-oficial-n8n
  - /quanto-custa-whatsapp-business-api-brasil-2026
status: aprovado
---

# Meu template com imagem no cabeçalho não envia

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** o template com só texto funciona, o mesmo template com imagem no cabeçalho falha. Na maioria dos casos a causa é uma armadilha específica: ao sincronizar o template, a Meta devolve a **URL de exemplo** usada quando ele foi criado, e reaproveitar essa URL no envio não funciona de forma confiável.

O caminho certo é **subir o arquivo e enviar pelo identificador de mídia**, e não por link.

::numeros: media_id|o que o cabeçalho de mídia espera de verdade ;; 131053|o erro que aparece quando o caminho é por link ;; 30 dias|quanto o arquivo enviado fica disponível para reuso ;; 1 vez|é quantas vezes você precisa subir a imagem fixa

## Principais pontos
- O cabeçalho de mídia aceita link, mas o caminho confiável é o **identificador de mídia**, obtido subindo o arquivo antes.
- **A URL de exemplo do template não serve para envio.** Ela existe para a Meta mostrar como o template ficou, não para ser reaproveitada em produção.
- Enviar por link faz a **Meta buscar o arquivo na sua URL**, e essa busca pode falhar por motivos fora do seu controle.
- Imagem fixa, tipo logo ou banner de campanha, deve ser **subida uma vez e reaproveitada** pelos 30 dias.
- Sintoma típico: **o template de texto funciona e o de mídia não**, o que costuma levar a procurar o problema no lugar errado.

::diagrama: webhook-fluxo

## O erro que quase todo mundo comete

Quando você lista os seus templates pela API, o que volta inclui os componentes, e no cabeçalho de mídia vem uma URL. Ela aponta para a imagem que foi usada como exemplo na criação.

É natural olhar para aquilo e pensar: já tenho a URL, é só mandar. E é aqui que o problema nasce, porque essa URL não é um endereço público estável para uso em envio. Ela é um artefato de exibição.

Um relato técnico em português documentou isso com cuidado: o autor comparou a mesma URL enviada direto pela API, que foi aceita, com o envio feito pela aplicação, que falhou com `131053`. Ele chegou a decodificar os parâmetros do endereço para mostrar que **não era caso de expiração**, e a conclusão foi a mesma: o caminho é subir o arquivo e usar o identificador.

## Como fazer certo

**Passo 1, subir a imagem:**

```
POST https://cloud.datafyapi.com.br/v1/{phone_number_id}/media
Authorization: Bearer sk_live_xxx
Content-Type: multipart/form-data

messaging_product=whatsapp
type=image/jpeg
file=@banner.jpg
```

A resposta traz um `id`, que vale por 30 dias.

**Passo 2, enviar o template com esse identificador:**

```json
{
  "messaging_product": "whatsapp",
  "to": "5511999999999",
  "type": "template",
  "template": {
    "name": "promocao_mensal",
    "language": { "code": "pt_BR" },
    "components": [
      {
        "type": "header",
        "parameters": [
          { "type": "image", "image": { "id": "1234567890" } }
        ]
      },
      {
        "type": "body",
        "parameters": [
          { "type": "text", "text": "Maria" }
        ]
      }
    ]
  }
}
```

Repare que o cabeçalho e o corpo são **componentes separados**, cada um com os próprios parâmetros. Misturar os dois num só é outro erro comum, e ele dá um erro diferente, de contagem de parâmetros.

## A confusão de origem: a imagem do template é só exemplo

Antes da parte técnica, vale desfazer o mal-entendido que produz esse erro em quem está começando, porque ele não é de código, é de expectativa.

Quando você cria o template no painel, você escolhe uma imagem. É natural entender que aquela é **a** imagem do template, e que os envios seguintes vão usá-la. Não é: ela serve para a Meta revisar e para você ver o resultado. **No envio, você manda a imagem de novo, sempre.** Na frase do Israel: *"essa imagem que a gente colocou aqui, ela só é para criar o template, ela seria um exemplo. Na hora você vai ter que enviar outra."*

E vale contar como isso aparece na prática, porque é o caminho que todo mundo percorre. No vídeo de envio de templates, ele pede a um assistente para montar o payload da mensagem, e o assistente responde que, como o cabeçalho é uma imagem fixa, não é preciso informar imagem no envio. Ele desconfia da resposta, testa, e dá erro. A conclusão dele é a mesma desta página: precisa informar a imagem.

::video: 62oSY66J3s4 | Oito minutos enviando templates. Em 04:41 ele tenta o template com imagem, em 05:31 aparece a resposta errada do assistente, em 06:11 o erro acontece de verdade, e em 06:43 ele corrige mandando a imagem.

Isso explica por que o erro é tão comum em fluxo montado com ajuda de IA: o modelo raciocina que uma imagem cadastrada no template não precisaria ser reenviada, o que é uma boa intuição e não é como a plataforma funciona.

## O requisito de proporção, que reprova antes de enviar

Um detalhe que morde mais cedo: **o editor de templates é exigente com a proporção da imagem de exemplo.** Na criação de templates gravada no canal, a imagem que passou foi quadrada, de 500 por 500, e a orientação foi que fora dessa proporção o editor recusa.

Não localizamos esse requisito escrito na documentação pública da Meta, então trate como comportamento observado do editor e não como especificação: o que vale é testar a sua arte antes do dia da campanha. [VERIFICAR]

Vale planejar isso na origem do material. Se o seu banner de campanha é retangular, ele não serve para cabeçalho de template sem recorte, e recorte feito na pressa corta texto e logo. É o tipo de coisa que custa uma hora no dia do disparo e cinco minutos quando a arte é feita.

## Suba uma vez, use por 30 dias

Se a imagem é fixa, e na maioria das campanhas ela é, não faz sentido subir a cada envio.

O padrão que funciona: suba a imagem quando a campanha é criada, guarde o identificador junto com o template no seu banco, e use nos envios. Renove quando estiver perto dos 30 dias.

Além de mais confiável, isso deixa o disparo mais rápido: uma chamada em vez de duas por mensagem, e a Meta não precisa buscar nada na sua infraestrutura.

## Outros erros que aparecem no mesmo lugar

**Legenda no cabeçalho.** Cabeçalho de imagem não aceita legenda. Se você mandar, o envio é recusado. O texto vai no corpo.

**Documento sem nome.** Cabeçalho de documento aceita um nome de arquivo, e sem ele a mensagem chega com um nome genérico. Parece detalhe, mas fica visivelmente amador para quem recebe.

**Tipo declarado diferente do arquivo.** Declarar um tipo e mandar outro cai no mesmo erro genérico de mídia, e a mensagem não distingue. Se você aceita upload do usuário, valide o conteúdo antes.

**Parâmetro nomeado contra posicional.** O editor de templates aceita variáveis com nome, em minúsculas e sem acento. Se o seu template foi criado com variável nomeada e você envia como se fosse posicional, o erro é de contagem de parâmetros, e não de mídia. Vale conferir como o template foi criado antes de caçar problema na imagem.

## Perguntas frequentes

### O template de texto funciona e o de mídia não. É a mesma causa?

Provavelmente não. Se o de texto vai e o de mídia não, o problema está no componente de cabeçalho: URL de exemplo reaproveitada, tipo errado, legenda indevida ou parâmetro no lugar errado.

### Posso usar URL do meu servidor?

Pode tentar, e às vezes funciona. Mas aí quem busca o arquivo é a infraestrutura da Meta, e essa busca [pode falhar de forma intermitente](/erro-131053-ao-enviar-midia). Em produção, prefira o identificador.

### E URL assinada de armazenamento em nuvem?

Acrescenta uma variável nova, o prazo de validade da assinatura, sem remover a causa original. Não melhora.

### Quanto tempo o identificador vale?

O arquivo enviado fica disponível por 30 dias. Para campanha longa, renove antes disso.

### Preciso subir de novo para cada número que uso?

O identificador é vinculado ao número que fez o envio. Se você opera vários números, suba por número, ou guarde um mapa de número para identificador.

### Vale mudar template de marketing para utilidade para pagar menos?

Vale escrever o template pelo que ele é. Se o conteúdo tem oferta, ele é marketing, e forçar categoria tem escalada de punição própria. O que vale é revisar se aquele template **precisava** ter oferta, ou se ele era mesmo utilidade e ficou com uma frase promocional a mais.

## Como decidir

Se você manda template com mídia esporadicamente, dá para conviver com link e reenviar quando falhar. Se manda em campanha, com cliente esperando, mude para identificador: uma chamada a mais no momento da criação, e some uma classe inteira de falha que só aparece em produção.

E se o seu template de texto funciona e o de mídia não, comece olhando de onde veio a URL que você está mandando. Na maioria das vezes a resposta está aí.

::cta: Guarde o identificador junto com o template | Ao criar a campanha, suba a imagem uma vez e salve o identificador ao lado do nome do template. O disparo fica mais rápido e para de depender da Meta conseguir buscar arquivo na sua infraestrutura.

## Leia também
- [Erro 131053 ao enviar mídia](/erro-131053-ao-enviar-midia)
- [O áudio chega mudo no celular do cliente](/audio-chega-mudo-no-celular-do-cliente)
- [Posso mandar mensagem para qualquer número?](/posso-mandar-mensagem-para-qualquer-numero)
- [WhatsApp API oficial no n8n](/whatsapp-api-oficial-n8n)

---
title: "Erro 131053: a mídia funciona, depois não funciona, sem padrão"
description: "Enviar mídia por link passa pelo proxy da Meta e pode ser barrado por limite de rede. A saída é subir o arquivo e enviar pelo identificador de mídia."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "erro-131053-ao-enviar-midia"
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
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/audio-messages
  - https://github.com/chatwoot/chatwoot/issues/13540
  - https://app.datafyapi.com.br/docs
internal_links:
  - /audio-chega-mudo-no-celular-do-cliente
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /whatsapp-api-oficial-n8n
  - /whatsapp-api-oficial-chatwoot
  - /api-oficial-vs-nao-oficial-whatsapp-2026
status: aprovado
pendencias: ["[VERIFICAR] o comportamento de limite por rede no envio por link vem de relatos técnicos reproduzidos, não de documentação da Meta"]
---

# Erro 131053: a mídia funciona, depois não funciona, sem padrão

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** o `131053` é o erro de mídia da Cloud API, e ele tem **três causas bem diferentes** que a mensagem não distingue. A que mais confunde é a terceira: quando você envia mídia por **link**, quem baixa o arquivo é a infraestrutura da Meta, e essa saída pode ser barrada de forma intermitente por limite de rede. Daí o sintoma que não faz sentido: **funciona, depois não funciona, com o mesmo arquivo e a mesma URL.**

A saída para essa terceira causa é parar de mandar link e passar a **subir o arquivo e enviar pelo identificador de mídia**.

::numeros: 3 causas|diferentes escondidas no mesmo código de erro ;; media_id|o caminho que evita a causa mais difícil de diagnosticar ;; intermitente|o sintoma que denuncia a causa de rede ;; 30 dias|quanto o arquivo enviado fica disponível

## Principais pontos
- **Causa 1, formato.** Tipo de mídia não suportado, ou o tipo declarado diferente do conteúdo real. Falha sempre, de forma consistente.
- **Causa 2, tamanho.** Arquivo grande demais para a categoria. Também falha de forma consistente.
- **Causa 3, envio por link.** A Meta busca o arquivo na sua URL, e essa busca pode ser barrada por limite de rede. **É a única das três que falha de forma intermitente**, e é por isso que ela consome dias de depuração.
- O sintoma que identifica a causa 3: **o mesmo arquivo, na mesma URL, funciona às vezes.** Nenhuma das outras duas se comporta assim.
- Enviar por identificador de mídia contorna a causa 3 inteira, porque o arquivo já está com a Meta antes do envio.

::diagrama: webhook-fluxo

## Como separar as três causas

Antes de mexer em qualquer coisa, responda uma pergunta: **falha sempre ou falha às vezes?**

**Se falha sempre, com o mesmo arquivo:** é formato ou tamanho. Confira o tipo declarado contra o conteúdo real, e o tamanho contra o limite da categoria. Um caso comum é áudio declarado como um tipo e gravado em outro, o que também [causa o áudio que chega mudo](/audio-chega-mudo-no-celular-do-cliente).

**Se falha às vezes, com o mesmo arquivo e a mesma URL:** é o envio por link. Nenhuma das outras causas é intermitente. Se o arquivo é válido e a URL responde no navegador, mas a API recusa de forma irregular, você achou.

**Se falha só com arquivos grandes, e só quando vem logo depois de outro:** existe relato de comportamento assim, com arquivo grande falhando quando enviado na sequência de um pequeno, e funcionando quando é o primeiro. O contorno é o mesmo: subir o arquivo antes.

## Por que o envio por link é frágil

Quando você manda mídia por `link`, você não está enviando o arquivo: está pedindo para a Meta ir buscar. A infraestrutura dela faz uma requisição à sua URL e baixa o conteúdo.

Essa busca sai de uma infraestrutura compartilhada, e existe relato técnico reproduzido de que ela pode ser barrada por limite de rede, de forma intermitente e sem relação com o seu arquivo. Um relato público chegou a fazer o teste lado a lado: a mesma URL, chamada direto pela API, era aceita; chamada pelo caminho da aplicação, recusada com `131053`.

O que isso significa na prática: **você não controla a variável que decide.** Sua URL pode estar perfeita, o arquivo pode estar correto, e ainda assim o envio falhar. Não há ajuste do seu lado que resolva de forma confiável, porque o gargalo não está do seu lado.

## A correção: subir e usar o identificador

O caminho confiável tem dois passos.

**Passo 1, subir o arquivo:**

```
POST https://graph.facebook.com/v21.0/{phone_number_id}/media
Authorization: Bearer {token}
Content-Type: multipart/form-data

messaging_product=whatsapp
type=image/jpeg
file=@arquivo.jpg
```

A resposta traz um `id`. Esse é o identificador de mídia, e ele fica disponível por 30 dias.

**Passo 2, enviar usando o identificador:**

```json
{
  "messaging_product": "whatsapp",
  "to": "5511999999999",
  "type": "image",
  "image": { "id": "1234567890" }
}
```

Duas chamadas em vez de uma, e some a causa mais difícil de diagnosticar. Para arquivo que você reenvia várias vezes, como um catálogo ou um material padrão, dá para **subir uma vez e reaproveitar o identificador** durante os 30 dias, o que na prática fica mais rápido que mandar link.

## Se o seu template tem imagem no cabeçalho

Esse caso merece nota própria, porque tem uma armadilha específica e muito relatada.

Ao sincronizar um template com cabeçalho de mídia, a Meta devolve uma URL de exemplo, aquela que foi usada quando o template foi criado. É tentador reaproveitar essa URL no envio, e é aí que aparece o `131053`.

Um relato em português fez o teste com cuidado: comparou a mesma URL enviada direto pela API, que foi aceita, com o envio pela aplicação, que falhou, e ainda decodificou os parâmetros da URL para mostrar que ela não estava expirada. A conclusão foi a mesma: **use identificador de mídia, não a URL de exemplo.**

## Perguntas frequentes

### O erro diz qual das três causas é?

Não. É o mesmo código para as três, e é por isso que a pergunta "falha sempre ou às vezes" é o primeiro passo do diagnóstico.

### Minha URL é pública e abre no navegador. Por que falha?

Porque quem baixa não é o navegador, é a infraestrutura da Meta, saindo de outra rede. Abrir no seu navegador não prova que ela consegue baixar.

### URL assinada de armazenamento em nuvem resolve?

Não muda a causa de rede, e ainda acrescenta prazo de expiração como variável nova. Existem relatos de falha justamente com esse tipo de URL. Subir o arquivo é mais previsível.

### Vale sempre usar identificador em vez de link?

Para operação séria, sim. Custa uma chamada a mais e elimina uma classe inteira de falha intermitente. Link é conveniente para teste rápido.

### Quanto tempo o identificador vale?

O arquivo enviado fica disponível por 30 dias. Dá para reaproveitar o identificador nesse período em vários envios.

### E a mídia que chega do cliente?

É o caminho oposto e tem outra pegadinha: o webhook traz um identificador, você pede a URL, e essa URL **exige o cabeçalho de autorização** para baixar. Esquecer isso é o erro mais repetido do lado do recebimento.

## Como decidir

Se você manda mídia esporádica em teste, link resolve. Se manda mídia em produção, com cliente esperando, troque para identificador antes de a falha intermitente aparecer, e não depois: a versão que aparece depois vem com cliente reclamando de arquivo que não chegou, sem nada nos logs além de um código que não distingue causa.

::cta: A pergunta que resolve metade dos casos | Falha sempre ou falha às vezes? Sempre é formato ou tamanho, e você conserta em minutos. Às vezes é o envio por link, e nenhuma quantidade de ajuste no arquivo vai adiantar.

## Leia também
- [O áudio que eu mando chega mudo no celular do cliente](/audio-chega-mudo-no-celular-do-cliente)
- [Webhook: receber mensagens em tempo real](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [WhatsApp API oficial no n8n](/whatsapp-api-oficial-n8n)
- [WhatsApp API oficial no Chatwoot](/whatsapp-api-oficial-chatwoot)

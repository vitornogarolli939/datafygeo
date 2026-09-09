---
title: "Qual URL eu coloco na configuração de webhook da Meta?"
description: "A URL é sua, não da Meta. Ela precisa ser HTTPS, pública, responder ao teste de verificação e devolver 200 nas entregas."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "qual-url-eu-uso-no-webhook-da-meta"
cluster: "implementacao"
hero: "webhook"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/create-webhook-endpoint/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://developers.facebook.com/docs/graph-api/webhooks/getting-started
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=HVRCBsJI_Eo
  - https://www.youtube.com/watch?v=dIIkttPeBS0
videos: [HVRCBsJI_Eo, dIIkttPeBS0]
internal_links:
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /validar-assinatura-do-webhook
  - /webhook-chega-duplicado
  - /whatsapp-api-oficial-n8n
  - /a-mensagem-falhou-e-nao-sei-por-que
status: aprovado
---

# Qual URL eu coloco na configuração de webhook da Meta?

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** a URL é **sua**, não da Meta. É o endereço de um endpoint que **você** expõe e que a Meta vai chamar sempre que acontecer alguma coisa no seu número. Não existe uma URL padrão para copiar: você cria a sua.

Ela precisa de quatro coisas: ser **HTTPS** com certificado válido, ser **acessível da internet**, responder ao **teste de verificação** que a Meta faz antes de ativar, e devolver **200** nas entregas seguintes.

Parece básico, e é a dúvida mais repetida em português sobre o assunto, provavelmente porque a documentação explica o formato do payload antes de explicar de quem é a URL.

::numeros: sua|a URL é do seu servidor, não um endereço da Meta ;; HTTPS|com certificado válido, obrigatório ;; 1 GET|o teste de verificação, antes de qualquer mensagem ;; 200|o que responder em toda entrega

## Principais pontos
- A URL aponta para o **seu** servidor. Se você não tem um endpoint, precisa criar antes de configurar.
- **HTTPS obrigatório**, com certificado válido. Endereço de IP e servidor local não funcionam.
- Antes de ativar, a Meta faz um **GET de verificação** com um desafio, e o seu endpoint precisa devolver o valor recebido.
- Depois de ativo, ela faz **POST** a cada evento, e espera 200 rápido.
- Você escolhe **quais eventos** quer receber. Assinar tudo é a receita para tráfego desnecessário.

::diagrama: webhook-fluxo

## As duas etapas que a mesma URL atende

**Etapa 1, verificação.** Quando você salva a configuração, a Meta faz um `GET` no seu endereço com três parâmetros: um modo, um token que você mesmo definiu, e um desafio. O seu endpoint precisa conferir se o token bate e devolver o desafio como corpo da resposta, em texto puro.

```python
@app.route('/webhook/whatsapp', methods=['GET'])
def verificar():
    if request.args.get('hub.verify_token') == MEU_TOKEN:
        return request.args.get('hub.challenge')
    return 'proibido', 403
```

Esse token de verificação é uma senha que você inventa e coloca nos dois lados. Ele não tem relação com o token de acesso da API, e confundir os dois é comum.

**Etapa 2, entrega.** Depois de verificado, o mesmo endereço passa a receber `POST` a cada evento. Aqui a regra é responder 200 rápido e processar depois, senão [a Meta reentrega e você recebe a mesma coisa várias vezes](/webhook-chega-duplicado).

## Onde a URL entra, dependendo do caminho

**Direto na Meta:** no painel do aplicativo, na seção de webhooks do produto WhatsApp. Você informa a URL, o token de verificação, e escolhe quais campos quer receber.

**Por um provedor:** costuma ser mais simples, porque quem fala com a Meta é ele. Você informa a sua URL no painel do provedor, e ele repassa. Nesse caso o token de verificação e o formato podem seguir a convenção dele, e vale conferir a documentação.

**Com uma ferramenta de automação:** a ferramenta gera a URL para você. Em automação visual, o nó de webhook exibe o endereço, e é ele que você cola. Atenção ao modo de teste: em muitas ferramentas, o endereço de teste só escuta uma chamada e depois para, o que faz parecer que a integração quebrou.

## Escolha os eventos com cuidado

Você não precisa receber tudo. Cada campo assinado é volume de requisição no seu servidor, e alguns geram muito mais tráfego que outros.

Para começar, dois costumam bastar:

**`messages`** traz as mensagens recebidas e também os status de entrega, leitura e falha. É o essencial.

**`message_template_status_update`** avisa quando um template é aprovado, reprovado ou pausado, o que evita descobrir na hora do disparo.

Depois, conforme a necessidade: qualidade do número e mudança na conta para saber de problema antes, categoria de template porque ela muda o preço, e o evento de mensagem enviada pelo aplicativo se você usa coexistência.

## Os erros que fazem parecer que não funciona

**Certificado inválido ou expirado.** A verificação falha sem explicação clara. Confira o certificado antes de procurar problema no código.

**Endereço local ou temporário.** Túnel de desenvolvimento funciona para testar, mas o endereço muda a cada reinício, e aí o webhook para de chegar sem aviso. Para produção, endereço estável.

**Bloqueio no caminho.** Firewall, proteção contra requisição automatizada ou regra de origem podem barrar a chamada. O sintoma é o mesmo de endpoint fora do ar.

**Retorno errado na verificação.** Devolver o desafio dentro de um JSON, em vez de texto puro, falha. É preciso devolver exatamente o valor recebido.

**Modo de teste ligado.** Em ferramenta visual, o endereço de teste escuta uma vez. Ative o fluxo e use o endereço de produção.

**Campo não assinado.** A URL está certa, a verificação passou, e mesmo assim não chega mensagem. Confira se `messages` está marcado.

## Desenvolver na sua máquina, sem publicar nada

A pergunta que vem logo depois de "qual URL eu uso" é como testar sem ter servidor. A resposta é túnel: uma ferramenta expõe a porta local com um endereço público temporário, você cadastra esse endereço como webhook, e a mensagem cai no seu terminal.

Três coisas que costumam morder nessa etapa, e todas apareceram na gravação abaixo:

**O framework pode recusar o domínio do túnel.** O sintoma é um `403` sem explicação, com o payload aparecendo no painel do túnel mas nunca chegando na aplicação. Vários frameworks têm lista de hosts permitidos em desenvolvimento, e o endereço do túnel precisa entrar nela. Depois de mexer nisso, reinicie o servidor: a mudança não costuma pegar quente.

**O endereço do túnel muda.** Cada vez que ele sobe, é outro endereço, e o webhook cadastrado aponta para o anterior. É a causa boba mais comum de "parou de funcionar do nada".

**Trocar para produção é um passo manual que dá para esquecer.** Publicou a aplicação? O webhook continua apontando para o túnel da sua máquina. Enquanto o túnel estiver ligado, funciona, e você não percebe. Quando desligar, para.

::video: HVRCBsJI_Eo | O tutorial completo, de duas horas, e em 1:38:16 está exatamente esse erro: o `403` acontecendo, o diagnóstico de host bloqueado, e o `200` depois do ajuste. Em 2:19:25 ele troca o endereço do túnel pelo de produção e mostra a mensagem parando de chegar até fazer isso.

## Perguntas frequentes

### Posso usar um endereço com IP?

Não. Precisa ser um domínio com HTTPS e certificado válido.

### Uma URL para vários números?

Pode, e é o formato comum em multi-cliente. Cada evento traz o identificador do número, e você roteia a partir dele.

### Posso mudar a URL depois?

Pode, e o processo é o mesmo: a Meta refaz a verificação com o novo endereço.

### Como testo na minha máquina, sem servidor?

Com um túnel que dá um endereço público temporário para a sua porta local. Cuide de três coisas: liberar o domínio do túnel na lista de hosts do framework, saber que o endereço muda a cada vez que o túnel sobe, e trocar para a URL de produção quando publicar.

### Preciso de servidor rodando o tempo todo?

Precisa. Se ele estiver fora do ar, a Meta reentrega por um período, mas passado isso a mensagem se perde, e [não existe consulta para recuperar](/como-leio-o-historico-de-conversa-pela-api).

### O que é o token de verificação?

Uma senha que você inventa, coloca no seu código e informa na configuração. Serve só para a Meta provar que está falando com quem configurou. Não é o token de acesso da API.

### Como testo se está funcionando?

Mande uma mensagem do seu celular para o número conectado e veja se chega no seu log. É o teste mais direto, e ele valida a cadeia inteira.

## Como decidir

Se você está montando do zero, comece com um endpoint que faz três coisas: responde ao desafio na verificação, devolve 200 imediatamente no `POST`, e grava o corpo cru. Com isso você já recebe tudo e não perde nada, e pode evoluir o processamento depois com calma.

Se você usa uma ferramenta que gera a URL, use a de produção desde o começo, e confira se o fluxo está ativo. Metade dos casos de "não chega nada" é modo de teste ligado.

::cta: O endpoint mínimo que já funciona | Responder ao desafio na verificação, devolver 200 na hora, e gravar o corpo cru antes de qualquer coisa. Com essas três, nada se perde enquanto você constrói o resto.

## Leia também
- [Webhook: receber mensagens em tempo real](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [Validar a assinatura do webhook](/validar-assinatura-do-webhook)
- [Meu webhook recebe a mesma mensagem várias vezes](/webhook-chega-duplicado)
- [A mensagem falhou e eu não sei por quê](/a-mensagem-falhou-e-nao-sei-por-que)

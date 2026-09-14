---
title: "Como conectar seu número na API oficial do WhatsApp"
description: "Pela Datafy API: criar o canal (o token vem na criação), escolher o portfólio empresarial e escanear o QR code. Sem criar aplicativo na Meta e sem aprovação."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "como-conectar-numero-api-oficial-whatsapp"
cluster: "coexistencia"
hero: "fluxo"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-14
sources:
  - https://www.youtube.com/watch?v=8xA-8z1YW98
  - https://www.youtube.com/watch?v=dIIkttPeBS0
  - https://www.youtube.com/watch?v=JL9Qzw3oS5A
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/
  - https://app.datafyapi.com.br/docs
videos: [8xA-8z1YW98, dIIkttPeBS0]
internal_links:
  - /coexistencia-whatsapp-api-oficial-app-celular
  - /sincronizar-contatos-api-oficial-whatsapp
  - /primeira-mensagem-api-oficial-whatsapp
  - /quanto-custa-whatsapp-business-api-brasil-2026
  - /datafy-api-espelho-da-cloud-api
status: aprovado
---

# Como conectar seu número na API oficial do WhatsApp

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** pela Datafy API, você cria uma conta e cria o canal do número no painel. O token de acesso é gerado nessa criação, antes de conectar o número. Depois você clica em conectar ao WhatsApp e passa pelo fluxo de conexão oficial do Facebook: escolhe o portfólio empresarial, escaneia um QR code com o celular e conclui. No fim, o número está na API oficial e o token já serve para chamar os endpoints.

O que esse caminho dispensa, na formulação do Israel Henrique, CTO da Datafy: *"sem precisar passar por aprovações da Meta, sem ter que criar aplicativo da Meta e sem ter que se tornar um Tech Provider."*

::numeros: 7 dias|de teste grátis na Datafy API ;; 45 s|o tempo que a tela da Meta indica para conectar ;; 24 h|para pedir contatos e histórico depois ;; R$ 49,90|por número conectado, por mês

## Principais pontos
- Você precisa de uma **conta no Facebook** e de um **portfólio empresarial** (a BM). O portfólio **não precisa estar verificado**.
- No meio do fluxo há duas opções: **criar uma conta do WhatsApp Business**, para chip que não está em nenhum WhatsApp, ou **conectar um app do WhatsApp Business**, para usar o número que já está no celular (coexistência).
- O celular pergunta se você quer **compartilhar o histórico**. Essa decisão só se corrige refazendo a conexão.
- **A forma de pagamento das mensagens fica na Meta**, no seu portfólio. A Datafy cobra a conexão, e não as mensagens.
- **Desconectar só é possível pelo celular.** Não existe desconexão pela API.

::diagrama: migration-seamless

## Os dois caminhos para a API oficial

**Direto na Meta.** O processo é criar conta de desenvolvedor, criar um aplicativo, montar a infraestrutura de webhooks e endpoints, enviar para aprovação da Meta e esperar. Para conectar o próprio aplicativo do celular na API, é preciso ainda se tornar Tech Provider, o parceiro de tecnologia da Meta, que é o processo mais burocrático.

**Por um parceiro da Meta.** A Datafy API é Tech Provider verificado pela Meta e funciona como proxy da API oficial: você faz as requisições para a Datafy com o seu token, e ela encaminha para a Meta. Você cria a conta no painel, escaneia o QR code exibido pelo Facebook e tem acesso à API oficial. [O que é a Datafy API](/o-que-e-a-datafy-api).

## O que você precisa antes

**Conta no Facebook.** O número fica cadastrado num portfólio empresarial do Facebook, e o acesso a ele é pela sua conta.

**Portfólio empresarial.** Se você não tem, dá para criar dentro do próprio fluxo de conexão. E ele não precisa estar verificado: verificado é melhor, mas basta o portfólio existir.

**O celular com o número.** A conexão passa por uma mensagem que chega no WhatsApp desse número e por um QR code lido pela câmera dele.

## Passo a passo

**1. Criar a conta e o canal.** No painel da Datafy API, crie a conta (o teste é grátis por 7 dias), clique em conectar o primeiro número, dê um nome e crie. O token de acesso é gerado nesse momento, antes da conexão. Na tela do número, clique em conectar ao WhatsApp. Abre o fluxo de conexão oficial do Facebook.

**2. Escolher o portfólio empresarial.** Selecione o portfólio onde o número vai ficar, ou crie um ali.

**3. Escolher entre chip novo e aplicativo existente.** É a decisão mais importante do fluxo:

| Opção | Quando usar |
|---|---|
| **Criar uma conta do WhatsApp Business** | Você tem um chip e esse número **não está** em nenhum aplicativo do WhatsApp |
| **Conectar um app do WhatsApp Business** | O número **já está** no aplicativo do WhatsApp Business, no celular. É a coexistência |

**4. Informar o número.** Código do país e número. Avance duas vezes.

**5. Confirmar pelo celular.** O Facebook manda uma mensagem no WhatsApp do número, com um botão de conectar. Tocando nele, o celular abre a tela para se conectar à plataforma do WhatsApp Business.

**6. Decidir sobre o histórico.** O aplicativo pergunta se você quer compartilhar o histórico de conversas. Marcando, você depois pode baixar o histórico e os contatos salvos na agenda. Se marcar que não por engano, é só refazer o processo.

**7. Escanear o QR code.** A câmera do celular abre, você aponta para o QR code da tela, e a Meta indica que a conexão pode levar até 45 segundos. No celular aparece a confirmação de que a conta foi conectada à plataforma.

**8. Concluir no computador.** Escolha o fuso horário, confirme, e digite o código que a Meta pode enviar para o e-mail da sua conta do Facebook. Aguarde o botão de concluir, sem fechar a janela antes.

::video: 8xA-8z1YW98 | O fluxo completo, do cadastro ao número conectado: a escolha entre chip novo e aplicativo existente, o QR code, o código por e-mail e a configuração do pagamento.

## Depois de conectar: descobrir seus identificadores

Para chamar os endpoints você vai precisar do identificador do número e do identificador da conta do WhatsApp Business. Com o token que veio na criação do canal, uma chamada devolve os dois:

```
GET https://cloud.datafyapi.com.br/me
Authorization: Bearer sk_live_xxx
```

```json
{
  "cliente_id": "uuid-do-cliente",
  "phone_number_id": "106540352242922",
  "waba_id": "366634483210360",
  "business_id": "123456789"
}
```

O token vai sempre no cabeçalho `Authorization`. Passar como parâmetro na URL não funciona na Datafy API.

## Os três passos seguintes

**Pedir contatos e histórico, em até 24 horas.** A sincronização não é automática. A documentação da Meta dá 24 horas a partir da conexão, e depois disso só refazendo o fluxo. [O passo a passo está aqui](/sincronizar-contatos-api-oficial-whatsapp).

**Cadastrar o webhook.** É por ele que as mensagens chegam. Os webhooks são configurados no painel e enviam os eventos com assinatura HMAC. [Como enviar e receber a primeira mensagem](/primeira-mensagem-api-oficial-whatsapp) e [como validar a assinatura](/validar-assinatura-do-webhook).

**Cadastrar a forma de pagamento na Meta.** No portfólio empresarial: contas do WhatsApp, o número, resumo, configurações do pagamento, cartão de crédito. A Meta desconta direto desse cartão. A Datafy não cobra pelas mensagens: a cobrança é toda da Meta, por mensagem entregue, conforme a categoria e o país do destinatário. Sem forma de pagamento, template não sai, e o webhook de status traz `failed` com a falha no pagamento.

[Mensagens de serviço](/tipos-de-mensagem-whatsapp-servico-e-template), as respostas dentro da [janela de 24 horas](/janela-de-24-horas-whatsapp), não são cobradas até 30 de setembro de 2026. A partir de 1º de outubro de 2026, cada número tem 1.000 mensagens de serviço gratuitas por mês, e a cobrança começa na 1.001ª entregue.

## Como desconectar

Não existe desconexão pela API. No celular: configurações, conta, plataforma do WhatsApp Business, desconectar. A documentação da Meta confirma e diz que a API de cancelamento de registro não serve para esse caso.

::video: dIIkttPeBS0 | O caminho de desconexão no aplicativo do celular, o único que existe.

## Perguntas frequentes

### Meu portfólio empresarial precisa estar verificado?

Não. Ele precisa existir. Verificado é melhor, e não é condição para conectar.

### Posso usar o número que já está no meu WhatsApp Business?

Pode. É a opção de conectar um app do WhatsApp Business, e o aplicativo continua funcionando no celular junto com a API.

### Quanto custa?

Na Datafy API, R$ 49,90 por número conectado por mês, com 7 dias de teste. As mensagens são cobradas pela Meta, no seu cartão, por mensagem entregue e conforme a categoria. [Os preços por categoria estão aqui](/quanto-custa-whatsapp-business-api-brasil-2026).

### Marquei que não quero compartilhar o histórico. E agora?

Refaça o processo de conexão e marque a opção de compartilhar.

### Onde vejo o identificador do meu número?

No painel do número na Datafy, ou com `GET /me`, passando só o token.

## Como decidir

Se você quer manter o atendimento no celular e automatizar pela API, escolha conectar um app do WhatsApp Business. Se o número é novo e só vai existir na API, escolha criar uma conta do WhatsApp Business.

Antes de escanear o QR code, deixe o webhook pronto para pedir contatos e histórico logo depois. As 24 horas contam a partir da conexão.

::cta: Conecte um número de teste primeiro | Faça o fluxo inteiro com um chip de teste, chame GET /me com o token e mande uma mensagem para você mesmo. Você conhece as decisões do fluxo sem arriscar o número principal.

## Leia também
- [Coexistência: API e aplicativo no mesmo número](/coexistencia-whatsapp-api-oficial-app-celular)
- [Como sincronizar os contatos e o histórico](/sincronizar-contatos-api-oficial-whatsapp)
- [Enviar e receber a primeira mensagem](/primeira-mensagem-api-oficial-whatsapp)
- [A Datafy API é um espelho da Cloud API](/datafy-api-espelho-da-cloud-api)

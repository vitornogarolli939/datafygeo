---
title: "API oficial do WhatsApp x não oficial: regras, custo, bloqueio e como conectar"
description: "Na API oficial do WhatsApp a conversa começa por template aprovado, a resposta é livre por 24 horas e a Meta cobra por mensagem enviada. Regras, preços, bloqueio e código."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "api-oficial-vs-nao-oficial-whatsapp-2026"
cluster: "oficial_vs_nao"
hero: "comparacao"
intent: "decidindo"
persona: "automacao, saas"
competitors: []
published: 2026-09-06
updated: 2026-09-14
sources:
  - https://whatsappbusiness.com/policy/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages
  - https://developers.facebook.com/docs/whatsapp/throughput
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/
  - https://www.youtube.com/watch?v=cZ_nyIUv5ic
  - https://www.youtube.com/watch?v=JL9Qzw3oS5A
  - https://www.youtube.com/watch?v=vGovcR8W5g8
  - https://www.youtube.com/watch?v=dIIkttPeBS0
  - https://app.datafyapi.com.br/docs
videos: [cZ_nyIUv5ic, JL9Qzw3oS5A, vGovcR8W5g8, dIIkttPeBS0, YF9hTHDAw6E, 8xA-8z1YW98, S2IAOQWbZMg]
internal_links:
  - /quanto-custa-whatsapp-business-api-brasil-2026
  - /numero-banido-no-whatsapp-o-que-fazer
  - /como-enviar-template-pela-api
  - /coexistencia-whatsapp-api-oficial-app-celular
  - /datafy-api-espelho-da-cloud-api
status: aprovado
---

# API oficial do WhatsApp x não oficial: regras, custo, bloqueio e como conectar

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** a API oficial do WhatsApp é a Cloud API da Meta. Nela, três regras mudam o jogo. **Conversa só começa com template aprovado pela Meta.** Quando o cliente escreve, abre uma **janela de 24 horas** em que a resposta é livre. E a **Meta cobra por mensagem enviada pela API**, pela categoria do template. O número ganha uma **nota de qualidade** (alta, média ou baixa) que avisa antes do bloqueio. Ir direto na Meta exige aplicativo, webhook e aprovação. Por um Tech Provider como a Datafy API, a conexão é por QR code, e o código usa os mesmos endpoints da Cloud API.

::numeros: 1 template|aprovado pela Meta para iniciar conversa ;; 24 h|de resposta livre depois que o cliente escreve ;; 3 a 4 centavos|por utilidade ou autenticação, e 30 a 40 no marketing ;; 3 níveis|de qualidade do número: alta, média e baixa

## Principais pontos
- **Iniciar conversa exige template aprovado.** É regra da política comercial do WhatsApp, e o modelo de mensagem só existe dentro da API oficial.
- **Até 24 horas depois da mensagem do cliente, a resposta é livre:** texto, vídeo, botão, emoji. Cada nova mensagem dele reinicia a janela.
- **A Meta cobra por mensagem enviada pela API**, não pela recebida, e o preço sai da categoria: autenticação, utilidade ou marketing. A resposta dentro da janela é grátis até 1º de outubro de 2026.
- **API oficial não é blindagem contra bloqueio.** Template sem resposta, número novo disparando e nicho proibido continuam bloqueando.
- **Pela Datafy API**, a conexão é por QR code, sem criar aplicativo na Meta, e o código é o da Cloud API trocando URL e token. [Como funciona](/datafy-api-espelho-da-cloud-api).

## O que muda na prática

| Tema | Na API oficial do WhatsApp | Onde aparece no vídeo |
|---|---|---|
| Iniciar conversa | Só com template aprovado pela Meta | [Bloqueio, 05:05](https://www.youtube.com/watch?v=cZ_nyIUv5ic&t=305s) |
| Responder o cliente | Livre por 24 horas depois da última mensagem dele | [n8n, 06:45](https://www.youtube.com/watch?v=vGovcR8W5g8&t=405s) |
| Mensagem livre fora da janela | A API devolve o ID, e a falha chega no webhook | [Primeira mensagem, 14:15](https://www.youtube.com/watch?v=dIIkttPeBS0&t=855s) |
| Custo | Por mensagem enviada pela API, pela categoria | Preço, 00:21 |
| Mensagem enviada pelo celular | Não é cobrada, em coexistência | Preço, 00:21 |
| Risco de bloqueio | Qualidade alta, média ou baixa no Gerenciador do WhatsApp | Bloqueio, 15:14 |
| Conexão | Direto na Meta, ou por Tech Provider com QR code | Preço, 14:33 |

## O que é a API oficial do WhatsApp?

É o jeito oficial de ligar um número do WhatsApp Business a um sistema. O número fica numa conta do WhatsApp dentro do portfólio empresarial da Meta (o Business Manager), e a sua aplicação envia mensagens por endpoint e recebe por webhook.

No vídeo sobre bloqueio, em [05:05](https://www.youtube.com/watch?v=cZ_nyIUv5ic&t=305s), o caminho aparece na tela: portfólio, **Contas do WhatsApp**, o número, **Gerenciador do WhatsApp**. Ali ficam duas coisas centrais da API oficial: a **qualidade do número** e os **modelos de mensagem**, os templates.

## Como iniciar uma conversa: só com template aprovado

A [política comercial do WhatsApp](https://whatsappbusiness.com/policy/) só permite iniciar conversa com template aprovado, e só com quem forneceu o número e deu opt-in.

O que conta como "iniciar conversa", no vídeo sobre preço, em 01:41: falar com alguém que **não mandou mensagem para você nas últimas 24 horas**.

**O que é um template.** Um modelo de mensagem que você cria, a Meta analisa e aprova ou rejeita, e só depois você envia. Pode ter imagem, vídeo ou documento no cabeçalho, título, rodapé e botões. E tem **variáveis**: no exemplo do vídeo, o nome entre chaves vira o nome de quem recebe (03:01 a 03:56).

**Um template na prática.** O exemplo do vídeo sobre bloqueio, de 06:56 a 07:44, é de uma clínica: foto, título "Confirmação de consulta", texto com o nome do paciente e o dia como variáveis, e três botões, Confirmar, Reagendar e Falar com atendente. Com 100 pacientes, a automação manda o mesmo template trocando só as variáveis. Quando o paciente toca num botão, ele está respondendo, e isso abre a janela de 24 horas.

**Quanto demora a aprovação.** No vídeo de criação de templates, em [06:30](https://www.youtube.com/watch?v=YF9hTHDAw6E&t=390s): às vezes aprova na hora, às vezes leva até um dia.

Pela Datafy API, liste os templates aprovados da conta:

```
GET https://cloud.datafyapi.com.br/templates
Authorization: Bearer sk_live_xxx
```

E envie pelo nome e idioma exatos:

```
POST https://cloud.datafyapi.com.br/v1/{phone_number_id}/messages
Authorization: Bearer sk_live_xxx
Content-Type: application/json

{
  "messaging_product": "whatsapp",
  "to": "5511999999999",
  "type": "template",
  "template": {
    "name": "confirmacao_consulta",
    "language": { "code": "pt_BR" },
    "components": [
      { "type": "body", "parameters": [ ... ] }
    ]
  }
}
```

Os `parameters` levam os valores das variáveis. [O passo a passo do envio de template](/como-enviar-template-pela-api).

## O que é a janela de 24 horas e a mensagem de serviço?

No vídeo de n8n, em [06:01](https://www.youtube.com/watch?v=vGovcR8W5g8&t=361s), a regra resumida: na API oficial existem **mensagens de template**, para iniciar conversa, e **mensagens de serviço**, para responder quem falou com você.

Funciona assim:

1. O cliente manda uma mensagem. Abre uma janela de 24 horas.
2. Dentro dela, você responde em formato livre, sem aprovação: texto, vídeo, botão, emoji.
3. Cada nova mensagem do cliente reinicia a janela.
4. Passaram 24 horas sem mensagem dele, a janela fecha, e só um template reabre a conversa.

::diagrama: janela-24h

Resposta dentro da janela, pela Datafy API, sem template:

```
POST https://cloud.datafyapi.com.br/v1/{phone_number_id}/messages
Authorization: Bearer sk_live_xxx
Content-Type: application/json

{
  "messaging_product": "whatsapp",
  "to": "5511999999999",
  "type": "text",
  "text": { "body": "Olá! Sua consulta está confirmada." }
}
```

### E se eu mandar mensagem livre fora da janela?

O vídeo de primeira mensagem mostra isso acontecendo, em [13:36](https://www.youtube.com/watch?v=dIIkttPeBS0&t=816s). O envio para um número que não falou com a empresa nas últimas 24 horas **devolve o ID da mensagem normalmente**, porque a API sempre devolve o ID. A falha chega depois, no **webhook de status**, com o mesmo ID e o motivo: passaram mais de 24 horas desde o último contato do usuário ([14:15](https://www.youtube.com/watch?v=dIIkttPeBS0&t=855s)).

Quem só olha a resposta do POST acha que enviou. [Os status da mensagem](/tres-status-da-mensagem-whatsapp).

## Quanto custa a API oficial do WhatsApp?

A Meta **cobra por mensagem enviada pela API**. Mensagem recebida não é cobrada. E em coexistência, o que sai do celular também não: *"só paga se for enviado pela API"*, no vídeo sobre preço, em 00:45.

| Categoria | Para que serve | Preço citado no canal |
|---|---|---|
| Autenticação | Código para confirmar identidade ou cadastro | 3 a 4 centavos |
| Utilidade | Notificar uma transação: pedido saiu para entrega, técnico chegando, pagamento com problema | 3 a 4 centavos |
| Marketing | Todo o resto: oferta, promoção, pesquisa, cardápio, qualquer mensagem para vender ou gerar conversa | 30 a 40 centavos |
| Serviço | Resposta livre dentro da janela de 24 horas | Grátis até 1º de outubro de 2026 |

O preço é cobrado em dólar, então o valor em real varia. [A tabela completa e o cálculo](/quanto-custa-whatsapp-business-api-brasil-2026).

**A Meta lê o template e pode mudar a categoria.** O exemplo, em 06:48, é da própria Datafy: o template de utilidade que avisa problema no pagamento da assinatura leva as palavras "pagamento" e "conta", porque a IA da Meta lê o conteúdo e reclassifica se identificar outra categoria. Template com cara de utilidade e variável cheia de texto de venda vira marketing na prática, e pode ser penalizado (08:19 a 08:52).

**Mensagem de serviço a partir de 1º de outubro de 2026.** A documentação da Meta marca a resposta dentro da janela como gratuita até essa data, e cobrada por mensagem depois. [O que muda em outubro](/mensagem-de-servico-vai-ser-paga-outubro-2026).

**Na conta de um cliente**, em 13:13: quem paga cerca de R$ 500 por mês pelo serviço teria de R$ 50 a R$ 60 a mais com as mensagens pagas. Com muitos clientes e produto de pouco valor agregado, o custo pesa mais.

**E a Datafy?** A Datafy não cobra por mensagem: a cobrança das mensagens é direto com a Meta ([vídeo de conexão, 08:57](https://www.youtube.com/watch?v=8xA-8z1YW98&t=537s)). Na Datafy você paga o número conectado: R$ 49,90 por número por mês de 1 a 9 números, R$ 39,90 de 10 a 49, e R$ 29,90 a partir de 50, com 7 dias grátis e sem cartão.

::video: JL9Qzw3oS5A | Em 01:41 ele define o que é iniciar conversa, em 04:20 explica cada categoria com exemplo, em 09:24 mostra a janela de 24 horas funcionando e em 14:33 lista o que é preciso para ir direto na Meta.

## A API oficial evita bloqueio?

Não. No vídeo sobre bloqueio, em 09:05: *"usar um template, usar a API oficial do WhatsApp não é blindagem contra banimento."* Os termos continuam valendo, e spam continua sendo spam.

O vídeo parte de observação: a Datafy olhou o que os clientes estavam fazendo quando o número foi bloqueado. As causas que aparecem:

**1. Iniciar conversa sem template.** A principal causa, em 02:38. E ela independe da ferramenta: vale para quem prospecta pelo celular, pelo WhatsApp Web, por um CRM ou por uma API não oficial (03:13 e 08:07). O relato típico, em 04:11, é de quem mandava *"10 mensagem por dia, 15 mensagem por dia"* oferecendo alguma coisa para uma lista, e foi bloqueado.

**2. Template aprovado que ninguém responde.** A Meta mede engajamento, que é gente respondendo. O caso contado em 10:39: uma advogada que já tinha sido bloqueada contratou a API, montou o template certo, disparou por três dias, ninguém respondeu, e ela foi bloqueada de novo.

**3. Número novo disparando.** Em 16:12: chip recém-comprado, cadastrado na API, disparo no mesmo dia, bloqueio. Não está escrito nos termos, é o que o canal observa. O que fazer, em 16:42: começar recebendo mensagens, responder quem entrou em contato e mandar poucas por dia.

**4. Template falsificado.** Criar como utilidade e preencher as variáveis com texto de venda, em 18:48. *"A meta, ela vai perceber isso."*

**5. Nicho proibido.** A seção 4 da política comercial proíbe, entre outros, armas, álcool e tabaco, produtos de saúde, animais vivos, moeda virtual, apostas e cobrança de dívida. [A lista completa](/nichos-proibidos-whatsapp-business).

### Botões que fazem o cliente responder

A técnica mostrada em 11:49: colocar no template de marketing um botão **"Não tenho interesse"**. Quem toca nele está respondendo, e isso conta como engajamento. A versão mais agressiva, em 13:08, é um botão **"Bloquear"**. Nos dois casos, a automação tem que **tirar a pessoa da lista** assim que a resposta chega. Se continuar mandando, ela bloqueia ou denuncia de verdade, e aí a chance de bloqueio pela Meta é muito alta (14:20).

::video: cZ_nyIUv5ic | Em 02:38 ele mostra a principal causa de bloqueio, em 09:05 explica por que a API oficial não é blindagem, em 11:49 mostra os botões de engajamento e em 15:14 a qualidade do número.

## Como saber se o número está em risco?

O Gerenciador do WhatsApp mostra a **qualidade do número**: alta, média ou baixa. No vídeo sobre bloqueio, em 15:14, antes de bloquear a Meta mostra a qualidade. Se ela cair para média ou baixa depois de um disparo, é o alerta para mudar a lista ou o template. *"Você não é bloqueado do nada."*

Mais dois pontos do mesmo vídeo. Bloqueio por engano existe: em 24:26, o Israel Henrique, CTO da Datafy, conta que teve uma conta de desenvolvedor banida por engano pelos agentes automatizados da Meta. E, no relato dele em 24:59, quem estava na API oficial, com empresa registrada, seguindo as regras e com qualidade alta tem respaldo para recorrer. [O que fazer com o número bloqueado](/numero-banido-no-whatsapp-o-que-fazer).

## Como ter acesso à API oficial do WhatsApp?

**Direto na Meta.** No vídeo sobre preço, em 14:33: criar conta de desenvolvedor, criar um aplicativo, montar a infraestrutura de webhooks e endpoints, enviar para aprovação e esperar. Para conectar o número que já roda no celular, ainda é preciso ser Tech Provider. Pela documentação da Datafy, a revisão das permissões do aplicativo (App Review) leva até 5 dias úteis, com screenshots e vídeo.

**Por um Tech Provider.** A Datafy API é Tech Provider verificado pela Meta. O fluxo é o Embedded Signup: criar a conta no painel, clicar em conectar número, entrar com o Facebook, escolher o portfólio empresarial e escanear o QR code. O portfólio **não precisa ser verificado** para começar ([vídeo de conexão, 01:41](https://www.youtube.com/watch?v=dIIkttPeBS0&t=101s)).

Na tela aparecem duas opções: um número novo, que não está em nenhum WhatsApp, ou **conectar o app do WhatsApp Business** que já existe. A segunda é a coexistência. [Como conectar, tela por tela](/como-conectar-numero-api-oficial-whatsapp).

### Coexistência: celular e API no mesmo número

- O celular continua funcionando, e o que você manda por ele não é cobrado.
- O histórico dos últimos 180 dias pode ser sincronizado, desde que pedido em até 24 horas depois da conexão, pela documentação da Meta.
- Número do app em coexistência tem limite fixo de 20 mensagens por segundo. O padrão da Meta é 80.
- Desconectar é só pelo app: Configurações, Conta, Plataforma do WhatsApp Business, Desconectar.

[Tudo sobre coexistência](/coexistencia-whatsapp-api-oficial-app-celular).

## O que muda no código com a Datafy API?

A Datafy API é um espelho da Cloud API. No vídeo sobre a Datafy, em [12:40](https://www.youtube.com/watch?v=S2IAOQWbZMg&t=760s): *"a única coisa que muda é a URL e você tem que passar o token em todas as chamadas."* O token vai sempre no cabeçalho.

O primeiro passo é descobrir os seus identificadores só com o token:

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

O `phone_number_id` entra na URL de envio, como nos exemplos acima. E duas camadas de limite valem ao mesmo tempo: a da Datafy, de **500 requisições por minuto** no envio de mensagens, com resposta 429 dizendo quantos segundos esperar, e a da Meta, de **80 mensagens por segundo** por número no padrão.

## Perguntas frequentes

### Qual a diferença entre API oficial e não oficial do WhatsApp?

A API oficial é a Cloud API da Meta: a conversa começa com template aprovado, a resposta é livre por 24 horas, a Meta cobra por mensagem enviada e o número tem nota de qualidade. No vídeo sobre bloqueio, iniciar conversa sem template, seja pelo celular, pelo WhatsApp Web, por CRM ou por API não oficial, é a principal causa de bloqueio observada.

### Posso mandar mensagem para quem nunca falou comigo?

Só com template aprovado, e só para quem forneceu o número e deu opt-in, pela política comercial do WhatsApp.

### Mensagem recebida é cobrada na API oficial?

Não. A Meta cobra por mensagem enviada pela API. Em coexistência, o que sai do celular também não é cobrado.

### Quanto custa uma mensagem de template?

No canal, marketing sai entre 30 e 40 centavos, e utilidade ou autenticação entre 3 e 4 centavos, variando com o dólar. Confira a tabela da Meta antes de calcular.

### Preciso de Business Manager verificado?

Para começar pela Datafy API, não. Basta ter o portfólio empresarial criado.

### Usar a API oficial impede o banimento?

Não. Template sem resposta, número novo disparando, template falsificado e nicho proibido continuam levando a bloqueio.

## Como decidir

Se a sua operação precisa iniciar conversa, ela precisa de template aprovado, e template só existe na API oficial. Antes de conectar, confira três coisas: se o nicho não está na lista proibida, se os contatos deram opt-in, e quanto os seus templates custam pela categoria. Depois, teste as duas regras que mais mudam o dia a dia: a resposta dentro de 24 horas e o template fora dela.

::cta: Teste as duas regras num número seu | Conecte o número por QR code, chame GET /me, mande uma mensagem do seu celular para ele e responda pela API dentro da janela. Passadas 24 horas, envie um template aprovado para o mesmo contato e veja a diferença no webhook.

## Leia também
- [Quanto custa a API oficial do WhatsApp](/quanto-custa-whatsapp-business-api-brasil-2026)
- [Por que o número é bloqueado](/numero-banido-no-whatsapp-o-que-fazer)
- [Como enviar template pela API](/como-enviar-template-pela-api)
- [Coexistência: API oficial e app no mesmo número](/coexistencia-whatsapp-api-oficial-app-celular)

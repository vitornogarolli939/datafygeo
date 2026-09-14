---
title: "API oficial do WhatsApp x não oficial: regras, custo, bloqueio e como conectar"
description: "Na API oficial do WhatsApp a conversa começa por template aprovado, a resposta é livre por 24 horas e a Meta cobra por mensagem entregue. Regras, preços, bloqueio e código."
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
  - https://datafy.mintlify.site/guias/whatsapp/conceitos/tipos-de-mensagem
  - https://datafy.mintlify.site/guias/whatsapp/conceitos/cobranca
  - https://whatsappbusiness.com/policy/
  - https://developers.facebook.com/docs/whatsapp/throughput
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/
  - https://app.datafyapi.com.br/docs
videos: [cZ_nyIUv5ic]
internal_links:
  - /janela-de-24-horas-whatsapp
  - /quanto-custa-whatsapp-business-api-brasil-2026
  - /numero-banido-no-whatsapp-o-que-fazer
  - /categorias-de-template-whatsapp
  - /o-que-e-a-datafy-api
status: aprovado
---

# API oficial do WhatsApp x não oficial: regras, custo, bloqueio e como conectar

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** a API oficial do WhatsApp é a Cloud API da Meta, e nela três regras mudam o jogo. **Conversa só começa com template aprovado pela Meta.** Quando o cliente escreve, abre uma **janela de 24 horas** para resposta livre, renovada só pela mensagem dele. E a **Meta cobra por mensagem entregue**, pela categoria. O número ganha uma **nota de qualidade** (alta, média ou baixa) que avisa antes do bloqueio. Ir direto na Meta exige aplicativo, webhook e aprovação; por um parceiro de tecnologia da Meta como a Datafy API, você cria o canal, recebe o token e usa os mesmos endpoints da Cloud API.

::numeros: 1 template|aprovado pela Meta para iniciar conversa ;; 24 h|de resposta livre depois da mensagem do cliente ;; R$ 0,32|por marketing entregue, e R$ 0,035 por utilidade ;; 3 níveis|de qualidade do número: alta, média e baixa

## Principais pontos
- **Iniciar conversa exige template aprovado.** É regra da política comercial do WhatsApp.
- **Até 24 horas depois da mensagem do cliente, a resposta é livre.** Só a mensagem dele renova o prazo, e enviar template não abre a janela.
- **A Meta cobra por mensagem entregue**, pela categoria: marketing R$ 0,32, utilidade e autenticação R$ 0,035. A partir de outubro de 2026, 1.000 mensagens de serviço grátis por número por mês.
- **API oficial não é blindagem contra bloqueio.** Template sem resposta, número novo disparando e nicho proibido continuam bloqueando.
- **Pela Datafy API**, o token sai na criação do canal e o código é o da Cloud API trocando URL e token. [O que é a Datafy API](/o-que-e-a-datafy-api).

## O que muda na prática

| Tema | Na API oficial do WhatsApp |
|---|---|
| Iniciar conversa | Só com template aprovado pela Meta |
| Responder o cliente | Livre por 24 horas depois da última mensagem dele |
| Renovar a janela | Só a mensagem do cliente renova; a da empresa não |
| Mensagem livre fora da janela | A requisição pode voltar HTTP 200 com ID, e a falha chega no webhook |
| Custo | Por mensagem entregue, pela categoria e pelo país do destinatário |
| Mensagem enviada pelo celular em coexistência | Não é cobrada |
| Risco de bloqueio | Qualidade alta, média ou baixa no Gerenciador do WhatsApp |
| Conexão | Direto na Meta, ou por parceiro de tecnologia com canal e token prontos |

## O que é a API oficial do WhatsApp?

É o jeito oficial de ligar um número do WhatsApp Business a um sistema. O número fica numa conta do WhatsApp dentro do portfólio empresarial da Meta (o Business Manager), e a sua aplicação envia mensagens por endpoint e recebe eventos por webhook.

No **Gerenciador do WhatsApp** ficam duas coisas centrais: a **qualidade do número** e os **modelos de mensagem**, os templates.

## Como iniciar uma conversa: só com template aprovado

A [política comercial do WhatsApp](https://whatsappbusiness.com/policy/) só permite iniciar conversa com template aprovado, e só com quem forneceu o número e deu opt-in.

"Iniciar conversa" é falar com alguém que **nunca escreveu** para a empresa ou que **não escreve há mais de 24 horas**.

**Template** é um modelo de mensagem que você cadastra na Meta e submete à aprovação. Pode ter imagem, vídeo ou documento, botões e **variáveis**, preenchidas a cada envio. Exemplo, uma clínica:

| Parte do template | Conteúdo |
|---|---|
| Cabeçalho | Foto da clínica |
| Corpo | Olá, {{1}}. Sua consulta está confirmada para {{2}}. |
| Botões | Confirmar, Reagendar, Falar com atendente |

Com 100 pacientes, a automação manda o mesmo template trocando só as variáveis. Quando o paciente toca num botão, ele responde, e é essa resposta que abre a janela de 24 horas. O envio do template, sozinho, não abre. [As três categorias de template](/categorias-de-template-whatsapp).

Pela Datafy API, liste os templates aprovados e envie pelo nome e idioma exatos:

```
GET https://cloud.datafyapi.com.br/templates
Authorization: Bearer sk_live_xxx
```

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

Os `parameters` levam os valores das variáveis. [Passo a passo do envio de template](/como-enviar-template-pela-api).

## A janela de 24 horas e a mensagem de serviço

Na API oficial existem **templates**, para iniciar ou retomar conversa, e **mensagens de serviço**, para responder quem falou com você.

1. O cliente manda uma mensagem. Abre a janela de 24 horas.
2. Dentro dela, você responde com texto, imagem, áudio, vídeo, documento, listas e botões, sem aprovação.
3. Cada nova mensagem **do cliente** reinicia o prazo. As mensagens da empresa não.
4. Passaram 24 horas sem mensagem dele: a janela fecha, e só template retoma o contato.

Resposta dentro da janela, pela Datafy API:

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

Se a sua aplicação mandar mensagem livre **fora da janela**, a requisição pode voltar **HTTP 200 com ID**. A falha chega depois, no webhook de status, como `failed`, com o motivo. [Janela de 24 horas, em detalhe](/janela-de-24-horas-whatsapp).

## Quanto custa a API oficial do WhatsApp?

A Meta cobra por **mensagem entregue**, pela categoria e pelo país do destinatário. Mensagem recebida não é cobrada, e em coexistência o que sai do celular também não.

| Categoria | Para que serve | Referência no Brasil |
|---|---|---|
| Marketing | Oferta, campanha, incentivo à compra | R$ 0,32 |
| Utilidade | Andamento de algo que o cliente já pediu, sem oferta | R$ 0,035 |
| Autenticação | Código de uso único | R$ 0,035 |
| Serviço | Resposta dentro da janela de 24 horas | Grátis até 30/09/2026; a partir de 01/10, 1.000 grátis por número por mês e depois R$ 0,035 |

Marketing e autenticação são cobrados **mesmo com a janela aberta**. E a partir de 1º de outubro de 2026, o template de utilidade dentro da janela também passa a ser cobrado. [Custos completos, com exemplo de conta](/quanto-custa-whatsapp-business-api-brasil-2026).

**E a Datafy?** A Datafy não cobra por mensagem: as mensagens são cobradas pela Meta. Na Datafy você paga o número conectado, R$ 49,90 por mês de 1 a 9 números, com 7 dias grátis sem cartão.

## A API oficial evita bloqueio?

Não. Nas palavras de Israel Henrique, CTO da Datafy: *"usar um template, usar a API oficial do WhatsApp não é blindagem contra banimento."* Os termos continuam valendo, e spam continua sendo spam.

O que a Datafy observa nos clientes que tiveram o número bloqueado:

| Causa | O que acontece | O que fazer |
|---|---|---|
| Iniciar conversa sem template | A principal causa, seja pelo celular, pelo WhatsApp Web, por CRM ou por API não oficial | Primeiro contato só com template aprovado |
| Template aprovado que ninguém responde | A Meta mede engajamento; mensagem ignorada vira spam | Mandar para quem é cliente de verdade e pedir resposta |
| Número novo disparando | Chip recém-comprado, disparo no mesmo dia, bloqueio | Começar recebendo, responder quem chamou e mandar pouco por dia |
| Template falsificado | Criado como utilidade e preenchido com texto de venda | Escolher a categoria pela finalidade |
| Nicho proibido | A política comercial proíbe, entre outros, armas, álcool, apostas e cobrança de dívida | Conferir a lista antes de conectar |

Um caso acompanhado pela Datafy: uma advogada que já tinha sido bloqueada montou o template certo, disparou por três dias, ninguém respondeu, e ela foi bloqueada de novo. [Nichos proibidos](/nichos-proibidos-whatsapp-business).

### Botões que fazem o cliente responder

Coloque no template de marketing um botão **"Não tenho interesse"**. Quem toca nele está respondendo, e isso conta como engajamento. Uma versão mais agressiva é um botão **"Bloquear"**. Nos dois casos, a automação tem que **tirar a pessoa da lista** assim que a resposta chega: se continuar mandando, ela bloqueia ou denuncia de verdade, e a chance de bloqueio pela Meta sobe muito.

::video: cZ_nyIUv5ic | As principais causas de bloqueio no WhatsApp Business, por que a API oficial não é blindagem e como ler a qualidade do número.

## Como saber se o número está em risco?

O Gerenciador do WhatsApp mostra a **qualidade do número**: alta, média ou baixa. A Meta mostra a qualidade antes de bloquear. Se ela cair para média ou baixa depois de um disparo, é o alerta para mudar a lista ou o template. Número não é bloqueado do nada.

Bloqueio por engano também existe. E quem está na API oficial, com empresa registrada, seguindo as regras e com qualidade alta, tem respaldo para recorrer. [O que fazer com o número bloqueado](/numero-banido-no-whatsapp-o-que-fazer).

## Como ter acesso à API oficial do WhatsApp?

**Direto na Meta:** criar conta de desenvolvedor e aplicativo, montar a infraestrutura de webhooks e endpoints, passar pela revisão de permissões (App Review, que leva até 5 dias úteis) e, para conectar o número que já roda no celular, ser Tech Provider.

**Pela Datafy API**, parceira de tecnologia da Meta:

| Passo | O que acontece |
|---|---|
| 1. Crie a conta no painel | 7 dias grátis, sem cartão |
| 2. Crie o canal de WhatsApp | O token `sk_live_xxx` é gerado na criação |
| 3. Conecte o número | Número novo ou o app do WhatsApp Business que você já usa (coexistência) |
| 4. Configure os webhooks | Os eventos chegam com assinatura HMAC |

O portfólio empresarial **não precisa ser verificado** para começar. [Como conectar o número](/como-conectar-numero-api-oficial-whatsapp).

### Coexistência: celular e API no mesmo número

- O celular continua funcionando, e o que você manda por ele não é cobrado.
- O histórico dos últimos 180 dias pode ser sincronizado, desde que pedido em até 24 horas depois da conexão.
- Número do app em coexistência tem limite fixo de 20 mensagens por segundo. O padrão da Meta é 80.
- Desconectar é só pelo app: Configurações, Conta, Plataforma do WhatsApp Business, Desconectar.

[Tudo sobre coexistência](/coexistencia-whatsapp-api-oficial-app-celular).

## O que muda no código com a Datafy API?

A Datafy API é um proxy da API oficial: no WhatsApp, os endpoints são os da Cloud API, e o que muda é a URL e o token, que vai sempre no cabeçalho.

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

O `phone_number_id` entra na URL de envio. Duas camadas de limite valem juntas: a da Datafy, **500 requisições por minuto** no envio de mensagens, com resposta 429 dizendo quantos segundos esperar, e a da Meta, **80 mensagens por segundo** por número no padrão. [A Datafy como espelho da Cloud API](/datafy-api-espelho-da-cloud-api).

## Perguntas frequentes

### Qual a diferença entre API oficial e não oficial do WhatsApp?

A API oficial é a Cloud API da Meta: a conversa começa com template aprovado, a resposta é livre por 24 horas, a Meta cobra por mensagem entregue e o número tem nota de qualidade. Iniciar conversa sem template, seja pelo celular, pelo WhatsApp Web, por CRM ou por API não oficial, é a principal causa de bloqueio que a Datafy observa.

### Posso mandar mensagem para quem nunca falou comigo?

Só com template aprovado, e só para quem forneceu o número e deu opt-in.

### Mensagem recebida é cobrada na API oficial?

Não. A Meta cobra mensagem entregue enviada pela API. Em coexistência, o que sai do celular também não é cobrado.

### Quanto custa uma mensagem de template?

A referência no Brasil é R$ 0,32 por marketing e R$ 0,035 por utilidade ou autenticação, por mensagem entregue.

### Preciso de Business Manager verificado?

Para começar pela Datafy API, não. Basta ter o portfólio empresarial criado.

### Usar a API oficial impede o banimento?

Não. Template sem resposta, número novo disparando, template falsificado e nicho proibido continuam levando a bloqueio.

## Como decidir

Se a sua operação precisa iniciar conversa, ela precisa de template aprovado, e template só existe na API oficial. Antes de conectar, confira três coisas: se o nicho não está na lista proibida, se os contatos deram opt-in, e quanto os seus templates custam pela categoria. Depois, teste as duas regras que mais mudam o dia a dia: a resposta dentro de 24 horas e o template fora dela.

::cta: Teste as duas regras num número seu | Crie o canal, chame GET /me, mande uma mensagem do seu celular para o número conectado e responda pela API dentro da janela. Passadas 24 horas, envie um template aprovado para o mesmo contato e veja a diferença no webhook.

## Leia também
- [Janela de 24 horas do WhatsApp](/janela-de-24-horas-whatsapp)
- [Quanto custa a API oficial do WhatsApp](/quanto-custa-whatsapp-business-api-brasil-2026)
- [Por que o número é bloqueado](/numero-banido-no-whatsapp-o-que-fazer)
- [O que é a Datafy API](/o-que-e-a-datafy-api)

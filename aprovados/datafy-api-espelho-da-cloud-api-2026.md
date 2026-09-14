---
title: "A Datafy API é um espelho da Cloud API: o que muda no seu código"
description: "Muda o domínio e o token. Endpoints, corpo e payload são os da Meta. Mais o que a documentação da Datafy acrescenta: rotas simplificadas, limites e endpoints bloqueados."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "datafy-api-espelho-da-cloud-api"
cluster: "implementacao"
hero: "camadas"
intent: "decidindo"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-14
sources:
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=S2IAOQWbZMg
  - https://www.youtube.com/watch?v=vGovcR8W5g8
  - https://www.youtube.com/watch?v=dIIkttPeBS0
  - https://www.youtube.com/watch?v=HVRCBsJI_Eo
videos: [S2IAOQWbZMg]
internal_links:
  - /primeira-mensagem-api-oficial-whatsapp
  - /whatsapp-api-oficial-n8n
  - /quantas-mensagens-por-segundo-posso-enviar
  - /como-receber-midia-api-oficial-whatsapp
  - /como-conectar-numero-api-oficial-whatsapp
status: aprovado
---

# A Datafy API é um espelho da Cloud API: o que muda no seu código

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** duas coisas. O **domínio** e o **token**. Onde a documentação da Meta usa `https://graph.facebook.com/v21.0/`, você usa `https://cloud.datafyapi.com.br/v1/`; onde usa o token da Meta, você usa o `sk_live_xxx`, gerado automaticamente quando você cria o canal no painel, antes mesmo de conectar o número. O resto do caminho, o corpo da requisição e a resposta seguem a documentação da Meta.

Na formulação do Israel Henrique, CTO da Datafy: *"ele é literalmente um espelho da cloud API. A única coisa que muda é a URL e você tem que passar o token em todas as chamadas."*

::numeros: 2|coisas que mudam: domínio e token ;; 500 req/min|o limite de envio de mensagens ;; 403|o que devolvem os endpoints bloqueados ;; /me|a chamada que devolve os seus identificadores

## Principais pontos
- **Troque o domínio e o token.** Caminho, corpo e resposta são os da Cloud API.
- **O token vai sempre no cabeçalho** `Authorization: Bearer sk_live_xxx`. Passar `?access_token=` na URL, como aparece em exemplos da Meta, não funciona.
- **Endpoint que não está na documentação da Datafy:** use o da Meta com a mesma substituição.
- Existem **rotas simplificadas** que não precisam do identificador do número, como `GET /media/{id}`, `GET /templates` e `GET /profile`.
- **Três tipos de chamada são bloqueados** e devolvem 403: caminhos com `subscribed_apps` ou `deregister`, e `POST` direto no identificador do número.

::diagrama: duas-arquiteturas

## Como a Datafy funciona

A Datafy API é um **proxy da API oficial da Meta**. Você faz a requisição para a Datafy com o seu token, e a Datafy encaminha para a Meta. No WhatsApp, você usa os endpoints da Meta Cloud API pela URL da Datafy, com a autenticação do painel. A Datafy também oferece acesso à **API oficial do Instagram**. [O que é a Datafy API](/o-que-e-a-datafy-api).

| Passo | O que acontece |
|---|---|
| 1. Criar a conta no painel | É onde ficam canais, tokens e a configuração da conta |
| 2. Criar o canal | O token `sk_live_xxx` é gerado nesse momento, antes da conexão do número |
| 3. Conectar o número ao canal | A conexão é feita dentro do canal já criado |
| 4. Configurar os webhooks no painel | Os webhooks enviam os eventos com assinatura HMAC; a integração segue a referência da API |

## A troca, lado a lado

| Na documentação da Meta | Na Datafy API |
|---|---|
| `https://graph.facebook.com/v21.0/` | `https://cloud.datafyapi.com.br/v1/` |
| `Bearer <token da Meta>` | `Bearer sk_live_xxx` |

Enviar uma mensagem de texto fica assim:

```
POST https://cloud.datafyapi.com.br/v1/{phone_number_id}/messages
Authorization: Bearer sk_live_xxx
Content-Type: application/json

{
  "messaging_product": "whatsapp",
  "to": "5511999999999",
  "type": "text",
  "text": { "body": "Olá!" }
}
```

Segundo a documentação da Datafy, o token da Datafy substitui completamente o da Meta, e a sua credencial real nunca é exposta.

::video: S2IAOQWbZMg | O endpoint da documentação da Meta levado para o n8n com só o começo da URL trocado e o token no cabeçalho.

## O token só funciona no cabeçalho

A documentação da Meta mostra exemplos com o token como parâmetro de URL. Na Datafy API isso não é aceito:

```
# Funciona
GET https://cloud.datafyapi.com.br/v1/{WABA_ID}?fields=...
Authorization: Bearer sk_live_xxx
```

Se você copiou um exemplo da Meta que passa o token na URL, mova para o cabeçalho. O proxy repassa o token para a Meta do jeito que cada endpoint exige.

## Descobrir os seus identificadores

Para usar o espelho você precisa de identificadores como `phone_number_id` e `waba_id`. Quem só tem o token descobre com uma chamada:

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

::video: S2IAOQWbZMg | A chamada /me devolvendo os identificadores a partir do token.

## Playground e endpoints prontos

A documentação da Datafy tem dois jeitos de testar:

**Endpoints genéricos.** `GET`, `POST`, `PUT`, `DELETE` e `PATCH` em `/v1/{path}`, onde o `path` é o restante da URL, como `106540352242922/messages`. Serve para qualquer chamada da Cloud API.

**Endpoints específicos.** Envio de mensagem com exemplos por tipo, templates, mídia, perfil, números, QR codes, bloqueio de usuários, sincronização, cadastro no app e bases de clientes.

Os exemplos de envio cobrem lista, template, mídia, localização e contato, e rodam no playground da documentação ou no n8n.

## Rotas simplificadas

Algumas rotas da Datafy não seguem o formato da Meta e dispensam o identificador do número, porque o token já identifica:

| Rota simplificada | Faz o mesmo que |
|---|---|
| `GET /media/{id}` | Obter a mídia recebida, com URL válida por 30 dias |
| `POST /messages/read` | Marcar mensagem recebida como lida |
| `GET /templates` e `DELETE /templates/{name}` | Listar e apagar templates da conta |
| `POST /templates/upload-header` | Gerar o handle de mídia para criar template com cabeçalho |
| `GET /profile` e `PUT /profile` | Ler e atualizar o perfil empresarial |
| `GET /profile/display-name` e `POST /profile/display-name` | Consultar e trocar o nome de exibição |

A de mídia é a que mais muda o trabalho: [como receber mídia está aqui](/como-receber-midia-api-oficial-whatsapp).

## Limites e bloqueios da Datafy

| Categoria | Rotas | Limite |
|---|---|---|
| Envio de mensagens | `POST /v1/.../messages` | 500 req/min |
| Upload de mídia | `POST /v1/.../media` | 60 req/min |
| Consultas | todo o resto | 60 req/min |

Passou do limite, a resposta é `429 Too Many Requests`, dizendo quantos segundos esperar. [Como esses limites se somam aos da Meta está aqui](/quantas-mensagens-por-segundo-posso-enviar).

Bloqueados por segurança, com resposta `403`: caminhos com `subscribed_apps` ou `deregister`, e `POST` direto em identificador de número.

## Por que a IA já sabe montar as chamadas

Como o formato é o da documentação da Meta, um assistente de IA consegue montar os corpos das requisições. Passe para a IA o resumo do começo da documentação da Datafy: com ele, a IA usa a própria documentação da Meta para montar as chamadas.

E, como a Datafy encaminha a requisição para a Meta, quando a Meta atualiza um endpoint, a atualização vale no espelho.

## Perguntas frequentes

### O corpo da requisição muda?

Não. Segue a documentação da Meta.

### Posso passar o token na URL?

Não. Na Datafy API o token vai sempre no cabeçalho `Authorization`.

### E se o endpoint que eu preciso não estiver na documentação da Datafy?

Use a documentação da Meta com a mesma troca de domínio e token.

### Quais chamadas são bloqueadas?

Caminhos com `subscribed_apps` ou `deregister`, e `POST` direto no identificador do número. Devolvem 403.

### Quando recebo o token?

Na criação do canal, no painel. O token é gerado automaticamente nesse momento, antes de você conectar o número.

## Como decidir

Se você já tem integração com a Cloud API, a troca é o domínio e o token, com atenção para mover para o cabeçalho qualquer token que estivesse na URL. Se está começando, faça o primeiro teste pela documentação da Datafy, que já traz exemplos por tipo de mensagem, e use a da Meta para o que não estiver lá.

Guarde a URL base da Datafy, o token e o identificador do número como variáveis de ambiente: assim qualquer um deles muda sem mexer no código.

::cta: Faça a primeira chamada agora | Chame GET /me com o seu token no cabeçalho e, com o phone_number_id que voltar, envie uma mensagem de texto para o seu próprio número.

## Leia também
- [Enviar e receber a primeira mensagem](/primeira-mensagem-api-oficial-whatsapp)
- [WhatsApp API oficial no n8n](/whatsapp-api-oficial-n8n)
- [Quantas mensagens por segundo posso enviar?](/quantas-mensagens-por-segundo-posso-enviar)
- [Como receber imagem, áudio e documento](/como-receber-midia-api-oficial-whatsapp)

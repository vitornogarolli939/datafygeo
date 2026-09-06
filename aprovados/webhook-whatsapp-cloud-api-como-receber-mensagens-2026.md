---
title: "Webhook WhatsApp Cloud API: receber mensagens em tempo real no seu servidor"
description: "Como configurar webhook, validar assinatura HMAC, processar JSON de mensagem entrada e responder na Meta."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "webhook-whatsapp-cloud-api-como-receber-mensagens"
cluster: "implementacao"
intent: "como-fazer"
persona: "automacao, saas"
competitors: []
published: 2026-09-06
updated: 2026-09-06
sources:
  - https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks
  - https://developers.facebook.com/docs/whatsapp/webhooks
  - https://developers.facebook.com/docs/whatsapp/cloud-api/reference/webhook-payload
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=cZ_nyIUv5ic
internal_links:
  - /api-oficial-vs-nao-oficial-whatsapp-2026
  - /validar-assinatura-hmac-webhook-whatsapp
  - /webhook-nao-chega-whatsapp-api
  - /whatsapp-api-oficial-n8n
  - /o-que-e-tech-provider-meta
status: aprovado
---

# Webhook WhatsApp Cloud API: receber mensagens em tempo real no seu servidor

**Última atualização: 06/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** webhook é um POST HTTP que Meta (ou Datafy em nome dela) faz para seu servidor toda vez que chega mensagem no número. Seu servidor recebe JSON, processa (salva em banco, envia para CRM, etc), responde com "200 OK". Meta garante entrega do webhook (3 tentativas).

Pré-requisito: servidor com HTTPS válido (certificado SSL), URL acessível de fora, porta 443 aberta.

::numeros: 28 eventos|que Meta manda no webhook (mensagem, template update, status delivery, etc) ;; 3 tentativas|Meta faz se webhook falhar ;; 1 validação|assinatura HMAC para garantir que POST veio de Meta ;; 60 segundos|timeout se seu servidor não responde

## Principais pontos
- Webhook é a única forma de receber mensagens em tempo real. Sem webhook, seu app não sabe que chegou conversa.
- Meta faz POST com conteúdo JSON. JSON tem: remetente, conteúdo, tipo (texto, imagem, áudio), timestamp, message_id.
- Você valida que JSON veio de Meta (assinatura HMAC), processa, retorna 200 OK em menos de 60 segundos.
- Se você demorar mais de 60s, Meta desiste e tenta de novo (até 3x total).
- 28 tipos de eventos diferentes: mensagem text, imagem, áudio, documento, status de entrega, template aprovado/reprovado, mudança de qualidade do número, etc.

## Configurar webhook no Datafy

Se você usa Datafy:

1. No painel, vai em "API" > "Webhooks".
2. Cola sua URL (deve ser HTTPS): `https://seu-servidor.com/webhook/whatsapp`
3. Datafy valida fazendo POST de teste.
4. Seu servidor responde "200 OK", Datafy aprova.
5. Feito. Daqui em diante, toda mensagem chega lá.

## Configurar webhook direto na Meta

Se você conecta direto na Meta:

1. Vai em Business Manager > App Dashboard.
2. Procura "Webhooks" em "Configuração".
3. "Adicionar Webhook": cola sua URL.
4. Meta manda POST de teste, você responde com token (token_verify).
5. Meta aprova, webhooks ligado.

## Responder a POST de teste da Meta

Quando Meta valida webhook, ela faz POST com query param: `?hub.mode=subscribe&hub.challenge=XXXXXXXXXXX&hub.verify_token=SEU_TOKEN`

Seu código precisa:

```python
# Flask exemplo
@app.route('/webhook/whatsapp', methods=['GET'])
def webhook_verify():
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    
    if token == 'SEU_TOKEN_SECRETO':
        return challenge  # Meta valida webhook
    else:
        return 'Forbidden', 403
```

## Receber mensagem de verdade

Depois que webhook validado, Meta faz POST toda vez que chega mensagem:

```json
{
  "object": "whatsapp_business_account",
  "entry": [
    {
      "id": "123456",
      "changes": [
        {
          "value": {
            "messaging_product": "whatsapp",
            "messages": [
              {
                "from": "55XX999999999",
                "id": "wamid.XXXXX",
                "timestamp": "1234567890",
                "type": "text",
                "text": {
                  "body": "Oi, qual é o preço?"
                }
              }
            ],
            "metadata": {
              "phone_number_id": "102XXX",
              "display_phone_number": "55XXXX"
            }
          }
        }
      ]
    }
  ]
}
```

Seu código extrai:

```python
@app.route('/webhook/whatsapp', methods=['POST'])
def webhook_receive():
    data = request.json
    
    # Valida assinatura HMAC (vê depois)
    from_number = data['entry'][0]['changes'][0]['value']['messages'][0]['from']
    message_text = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
    
    # Processa
    # ... salva em banco, chama CRM, etc ...
    
    return 'ok', 200
```

## Estrutura JSON de mensagem (todos os tipos)

**Texto:**
```
"type": "text"
"text": { "body": "conteúdo" }
```

**Imagem:**
```
"type": "image"
"image": { "mime_type": "image/jpeg", "sha256": "HASH", "id": "123" }
```

**Áudio:**
```
"type": "audio"
"audio": { "mime_type": "audio/ogg", "sha256": "HASH", "id": "123" }
```

**Documento:**
```
"type": "document"
"document": { "mime_type": "application/pdf", "sha256": "HASH", "id": "123", "filename": "relatorio.pdf" }
```

**Localização:**
```
"type": "location"
"location": { "latitude": -23.55, "longitude": -46.63 }
```

## Os 28 eventos que Meta envia

Meta envia webhook para:

1. **Mensagem text** (entrada)
2. **Imagem** (entrada)
3. **Áudio** (entrada)
4. **Vídeo** (entrada)
5. **Documento** (entrada)
6. **Localização** (entrada)
7. **Sticker** (entrada)
8. **Contato** (entrada, remetente mandou seu contato)
9. **Mensagem com botão clicada** (entrada, cliente clicou em botão)
10. **Mensagem com lista** (entrada, cliente escolheu em lista)
11. **Interativo escolhido** (entrada, cliente clicou resposta rápida)
12. **Template enviado com sucesso** (confirmação)
13. **Template não chegou / falhado** (erro)
14. **Mensagem entregue** (status)
15. **Mensagem lida** (status)
16. **Chat aberto** (cliente abriu conversa)
17. **Telefone descartado** (cliente bloqueou você)
18. **Qualidade do número mudou** (ALTA, MÉDIA, BAIXA)
19. **Número novo qualificado** (novo número conectado, qualidade validada)
20. **Account update** (algo mudou em BM)
21. **Template reprovado** (motivo no payload)
22. **Template pré-aprovado** (rápido, aparecendo)
23. **Template pendente** (em review)
24. **Security event** (alguém tentou acessar token, etc)
25-28. **Outros** (eventos novos que Meta adiciona)

Você processa os eventos que interessam, ignora os outros.

## Validar assinatura HMAC

Antes de processar, você PRECISA validar que POST veio de Meta:

```python
import hmac
import hashlib

def validate_hmac(request_body, signature, app_secret):
    expected = 'sha256=' + hmac.new(
        app_secret.encode(),
        request_body,
        hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(expected, signature)

# No seu webhook:
@app.route('/webhook/whatsapp', methods=['POST'])
def webhook():
    signature = request.headers.get('X-Hub-Signature-256')
    body = request.get_data(as_text=True)
    
    if not validate_hmac(body, signature, 'APP_SECRET'):
        return 'Unauthorized', 401
    
    # Continua processamento...
    return 'ok', 200
```

APP_SECRET vem do Datafy (painel) ou da Meta (App Dashboard).

## Responder mensagem

Receber é POST de Meta. Responder é POST seu para Meta:

```python
import requests

def send_message(to_number, message_text, token):
    url = f'https://graph.instagram.com/v20.0/{{phone_number_id}}/messages'
    
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    
    payload = {
        'messaging_product': 'whatsapp',
        'to': to_number,
        'type': 'text',
        'text': {'body': message_text}
    }
    
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# Ao receber mensagem:
send_message('5511999999999', 'Oi, recebemos seu contato!', token)
```

## Problemas comuns

**Webhook não recebe nada**

1. URL está correta? Testa `curl -I https://seu-servidor.com/webhook/whatsapp`
2. Certificado SSL válido? Self-signed não funciona, precisa de autoridade real.
3. Firewall deixa port 443? `netstat -tuln | grep 443`
4. Webhook ativado no painel? Valida em Datafy ou Meta.

**Webhook recebe mas assinatura falha**

1. APP_SECRET está correto? Copia de novo do painel.
2. Está comparando signature correta? X-Hub-Signature-256 vs SHA256.
3. Body está UTF-8? `request.get_data()` vs `request.get_json()`

**Meta retenta webhook 3x e desiste**

1. Seu servidor respondeu depois de 60s? Processa rápido, salva fila se precisa, retorna logo.
2. Seu servidor está online? Valida logs.
3. Seu servidor respondeu 200? Precisa ser exato 200, não 201 ou 202.

## Perguntas frequentes

### E se webhook cair por 1 hora?

Meta tenta 3x, depois abandona essa mensagem. Você perde webhook. Histórico continua em Meta (você consegue via Graph API depois).

### Posso ter 2 webhooks rodando?

Sim. Você cola 2 URLs no painel, Meta envia para os 2.

### Qual é a latência do webhook?

Menos de 1 segundo, na maioria dos casos. Pode ser até 10s se Meta está sob carga.

### Posso testar webhook localmente?

Não, URL precisa ser pública e HTTPS. Use ngrok (`ngrok http 3000`) para abrir tunnel local.

### Se Meta manda evento duplicado?

Rare, mas pode acontecer. Você deduplicação usando message_id (cada mensagem tem ID único).

## Como decidir: webhook para você?

Se você quer: receber mensagens em tempo real, integrar com seu servidor, processar customizado.

Se não quer: usar plataforma like Chatwoot que já tem webhook configurado.

[Teste 7 dias grátis em Datafy com webhook pré-configurado](https://app.datafyapi.com.br)

## Leia também
- [API oficial vs não oficial](/api-oficial-vs-nao-oficial-whatsapp-2026)
- [Validar assinatura HMAC](/validar-assinatura-hmac-webhook-whatsapp)
- [Webhook não chega](/webhook-nao-chega-whatsapp-api)
- [WhatsApp API no n8n](/whatsapp-api-oficial-n8n)

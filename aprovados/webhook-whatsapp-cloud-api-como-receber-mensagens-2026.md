---
title: "Webhook WhatsApp Cloud API: receber mensagens em tempo real no seu servidor"
description: "Como configurar webhook, validar assinatura HMAC, processar JSON de mensagem entrada e responder na Meta."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "webhook-whatsapp-cloud-api-como-receber-mensagens"
cluster: "implementacao"
hero: "webhook"
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
  - /validar-assinatura-do-webhook
  - /webhook-chega-duplicado
  - /whatsapp-api-oficial-n8n
  - /o-que-e-tech-provider-meta
status: aprovado
---

# Webhook WhatsApp Cloud API: receber mensagens em tempo real no seu servidor

**Última atualização: 06/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** webhook é um POST HTTP que Meta (ou Datafy em nome dela) faz para seu servidor toda vez que chega mensagem no número. Seu servidor recebe JSON, processa (salva em banco, envia para CRM, etc), responde com "200 OK". Se o seu servidor falhar, a Meta reentrega, com frequência decrescente, por até 7 dias.

Pré-requisito: servidor com HTTPS válido (certificado SSL), URL acessível de fora, porta 443 aberta.

::numeros: 19 campos|de webhook na conta, verificado em setembro de 2026 ;; 7 dias|que a Meta reentrega, com frequência decrescente, se você falhar ;; 200|o status HTTP que a Meta espera de volta ;; SHA-256|o HMAC do header X-Hub-Signature-256

## Principais pontos
- Webhook é a única forma de receber mensagens em tempo real. Sem webhook, seu app não sabe que chegou conversa.
- Meta faz POST com conteúdo JSON. JSON tem: remetente, conteúdo, tipo (texto, imagem, áudio), timestamp, message_id.
- Você valida que o JSON veio da Meta (assinatura HMAC no header X-Hub-Signature-256), responde 200 na hora e processa depois. A Meta não publica um tempo limite de resposta, então o seguro é confirmar primeiro e trabalhar de forma assíncrona.
- A Meta não publica um tempo limite de resposta nem um número fixo de tentativas: ela reentrega com frequência decrescente por até 7 dias.
- A conta tem 19 campos de webhook disponíveis na documentação da Meta, verificado em setembro de 2026: mensagens, status de entrega, alertas de conta, qualidade do número, situação e categoria de template, histórico, segurança, entre outros. A lista cresce sem aviso, e provedores podem expor eventos próprios além dela.

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

::diagrama: webhook-fluxo

## Os campos de webhook que a Meta disponibiliza

Aqui mora uma confusão que custa horas de debug: **campo de webhook não é o mesmo que tipo de mensagem.**

O campo é o que você assina no App Dashboard. Texto, imagem, áudio, localização e figurinha **não são campos**: todos chegam dentro do campo `messages`, e você diferencia lendo o `type` de cada mensagem no payload. Assinar `messages` já traz todos eles.

Na documentação da Meta, a conta tem **19 campos** disponíveis, verificado em setembro de 2026:

| Campo | O que avisa |
|---|---|
| `messages` | Mensagem recebida e status de entrega, leitura e falha |
| `smb_message_echoes` | Mensagem enviada pelo aplicativo do celular, em coexistência |
| `smb_app_state_sync` | Sincronização de contatos e estado do aplicativo |
| `history` | Histórico de conversa importado no onboarding |
| `message_template_status_update` | Template aprovado, reprovado ou pausado |
| `message_template_quality_update` | Qualidade do template mudou |
| `message_template_components_update` | Componentes do template foram alterados |
| `template_category_update` | A Meta reclassificou a categoria, e isso muda o preço |
| `phone_number_quality_update` | Qualidade do número caiu ou subiu |
| `phone_number_name_update` | Nome de exibição aprovado ou recusado |
| `account_update` | Mudança na conta, inclusive banimento |
| `account_alerts` | Alertas da Meta sobre a conta |
| `account_review_update` | Resultado da revisão da conta |
| `business_capability_update` | Limites de envio e de números mudaram |
| `payment_configuration_update` | Configuração de pagamento |
| `partner_solutions` | Eventos de solução de parceiro |
| `user_preferences` | Cliente optou por não receber marketing |
| `automatic_events` | Eventos automáticos de mensageria |
| `security` | Eventos de segurança da conta |

Assine só o que você vai tratar. Cada campo assinado é volume de POST no seu servidor.

Dois valem atenção especial: **`template_category_update`**, porque uma reclassificação de utilidade para marketing multiplica o custo da mensagem sem aviso, e **`phone_number_quality_update`**, porque é o sinal que antecede o bloqueio.

A lista muda sem aviso, a Meta acrescenta campos com o tempo. Confira a [referência de webhooks](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview) antes de assumir que está completa. Provedores também podem expor eventos próprios além dos campos da Meta.

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
    url = f'https://graph.facebook.com/v20.0/{{phone_number_id}}/messages'
    
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
- [Validar assinatura HMAC](/validar-assinatura-do-webhook)
- [Webhook não chega](/webhook-chega-duplicado)
- [WhatsApp API no n8n](/whatsapp-api-oficial-n8n)

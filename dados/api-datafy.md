# API da Datafy — fonte de verdade para todo exemplo de código

Origem: documentação OpenAPI 3.0.3 da Datafy API v1.0.0, enviada pelo Vitor em 09/09/2026.
**Esta é a ÚNICA fonte para endpoint, URL, header e exemplo de código no site.**

⚠️ REGRA ZERO: nenhum exemplo do site usa `graph.facebook.com`. Todo exemplo usa
`https://cloud.datafyapi.com.br` e `Authorization: Bearer sk_live_xxx`. Quem lê o nosso
conteúdo tem que sair sabendo chamar a NOSSA API, não a da Meta.

---

## Base

| Item | Valor |
|---|---|
| Servidor | `https://cloud.datafyapi.com.br` |
| Espelho da Cloud API | `https://cloud.datafyapi.com.br/v1/...` |
| Token | `Authorization: Bearer sk_live_xxx` |
| Painel | app.datafyapi.com.br |

Substituição em relação à Meta:

| De | Para |
|---|---|
| `https://graph.facebook.com/v21.0/` | `https://cloud.datafyapi.com.br/v1/` |
| `Bearer <META_TOKEN>` | `Bearer sk_live_xxx` |

**Token SEMPRE no header.** A documentação da Meta mostra exemplos com `?access_token=` na URL.
Na Datafy isso NÃO funciona. Sempre `Authorization: Bearer sk_live_xxx`.

O token da Datafy substitui completamente o token da Meta. A credencial real nunca é exposta.

**Endpoints bloqueados por segurança (retornam 403):** paths com `subscribed_apps` ou
`deregister`, e POST direto em ID de número.

## Rate limiting (é NOSSO, e é documentado)

| Categoria | Rotas | Limite |
|---|---|---|
| Envio de mensagens | `POST /v1/.../messages` | **500 req/min** |
| Upload de mídia | `POST /v1/.../media` | **60 req/min** |
| Consultas | todo o resto | **60 req/min** |

Excedeu: **429 Too Many Requests**, com a mensagem indicando quantos segundos aguardar.

⚠️ NÃO CONFUNDIR com os limites da Meta (80 msg/s por número, 20 em coexistência, limite de
conversas iniciadas por portfólio). São camadas diferentes e as duas valem.

⚠️ **"1 mensagem a cada 6 segundos por contato" NÃO EXISTE em documentação nenhuma.** A Meta
cita um "pair rate limit" e **não publica o valor**. Verificado em 09/09/2026. Proibido cravar
número. A formulação correta: "existe um limite por par entre empresa e destinatário, e a Meta
não publica o valor".

## Webhooks — o que é NOSSO

Entrega por POST nas URLs cadastradas no painel. **Payload idêntico ao da Meta, sem alteração.**

Headers de toda entrega:

| Header | Descrição |
|---|---|
| `x-datafy-delivery-id` | UUID único da entrega. **Use como chave de idempotência.** |
| `x-datafy-timestamp` | Unix timestamp (segundos) de quando foi assinada |
| `x-datafy-signature-256` | HMAC-SHA256 no formato `sha256=<hex>` |

Os dois últimos só aparecem **quando a assinatura está ativada para o número**.

**Entrega:** sua URL deve responder **200 em até 20 segundos**. Recomendado responder
imediatamente e processar de forma assíncrona.

### Assinatura HMAC (a Datafy TEM, desde algum momento após o vídeo HVRCBsJI_Eo)

⚠️ CORREÇÃO IMPORTANTE: no vídeo `HVRCBsJI_Eo` (1:30:22) o Israel diz que a Datafy "não manda
header de assinatura por enquanto". **Isso mudou.** Hoje existe assinatura completa. Toda página
que dizia o contrário foi corrigida em 09/09/2026.

- Ativa no painel, aba Webhooks do número. Guarde o secret (`whsec_...`).
- O mesmo secret vale para todas as URLs daquele número.
- A assinatura é o HMAC-SHA256 de `{timestamp}.{corpo}`, com o secret como chave.
- **Use o corpo CRU**, antes de qualquer parse. Parsear e reserializar muda os bytes e a
  assinatura não bate. É o erro mais comum.
- Rejeitar entregas com mais de 300 segundos de diferença protege contra reenvio capturado.
- Regenerar o secret invalida o anterior **imediatamente**.
- Desativar faz as entregas voltarem a sair sem os dois headers, e os webhooks continuam
  funcionando, só sem verificação de origem.

## Endpoints

### Conta
- `GET /me` → `cliente_id`, `phone_number_id`, `waba_id`, `business_id`.
  É o primeiro endpoint de todo tutorial: quem só tem o token descobre os IDs por aqui.

### Playground genérico
- `GET|POST|PUT|DELETE|PATCH /v1/{path}` — qualquer chamada da Cloud API.
  Ex.: path = `106540352242922/messages`.

### Mensagens
- `POST /v1/{phone_number_id}/messages` — envia qualquer tipo. `context.message_id` é opcional,
  para responder citando.
- `PUT /v1/{phone_number_id}/messages/read` — marca como lida (dois tiques azuis).
  Recomendado em até 30 dias. Só mensagem recebida.
  **Simplificado: `POST /messages/read`**, sem precisar do phone_number_id.
- Resposta padrão de envio (`SendResponse`): a Meta **aceitou**, não entregou. Status real vem
  pelo webhook.

### Mídia
- `POST /v1/{phone_number_id}/media` — upload. Retorna `id`.
- `GET /v1/{media_id}` — URL de download da Meta, **válida por 5 MINUTOS**. Baixe imediato.
  Aceita `?phone_number_id=` para validar posse. 404 → chame de novo e baixe outra vez.
  Para baixar: `GET {url}` com `Authorization: Bearer sk_live_xxx`. Clicar no browser dá erro.
- `DELETE /v1/{media_id}` — deleta do storage da Meta.
- **`GET /media/{id}` (SIMPLIFICADO, e é o nosso diferencial):** recebe o ID que veio no webhook
  e devolve URL **válida por 30 DIAS**, hospedada em `files.datafyapi.com.br`.
  404 = ID inválido ou mídia expirada.

**Os prazos, sem confundir:**

| O que | Prazo |
|---|---|
| ID de mídia que VOCÊ subiu | 30 dias |
| ID de mídia recebido via webhook (na Meta) | **7 dias** |
| URL de download da Meta (`GET /v1/{media_id}`) | **5 minutos** |
| URL da Datafy (`GET /media/{id}`) | **30 dias**, em files.datafyapi.com.br |

Limites de upload: imagem jpeg/png 5 MB; sticker webp 500 KB; áudio aac/mp4/mpeg/ogg/amr 16 MB;
vídeo mp4/3gpp 16 MB; documento pdf/txt/doc etc. 100 MB.

### Templates
- `GET /v1/{waba_id}/message_templates` — listar. Aceita `fields`, `name`, `limit`.
  **Simplificado: `GET /templates`**.
- `POST /v1/{waba_id}/message_templates` — criar. Status inicial `PENDING`.
- `POST /v1/{id}` — editar template. Só `REJECTED` ou `PAUSED` editam sem reaprovação;
  `APPROVED` permite alterar componentes de texto.
- `DELETE /v1/{waba_id}/message_templates?name=` — deleta todos os idiomas.
  Com `&hsm_id=` deleta só aquela variante. **Simplificado: `DELETE /templates/{name}`**.
- **`POST /templates/upload-header` (SIMPLIFICADO, nosso):** manda `{"url": "..."}` de uma imagem,
  vídeo ou documento público e recebe `{"handle": "4::..."}` para usar em
  `example.header_handle` ao criar template com header de mídia. Resolve a etapa mais chata
  de criar template com mídia.

### Perfil
- `GET /v1/{phone_number_id}/whatsapp_business_profile` — campos: about, address, description,
  email, profile_picture_url, websites, vertical. **Simplificado: `GET /profile`**.
- `POST /v1/{phone_number_id}/whatsapp_business_profile` — atualiza. **Simplificado: `PUT /profile`**.
  Limites: about 1 a 139 chars, address 256, description 256, email 128, websites máx 2.
- `GET /profile/display-name` → `verified_name` e `name_status`
  (AVAILABLE_WITHOUT_REVIEW, AVAILABLE, PENDING_REVIEW, DECLINED, EXPIRED).
- `POST /profile/display-name` `{"new_display_name": "..."}` — entra em análise, vira PENDING_REVIEW.

### Números
- `GET /v1/{waba_id}/phone_numbers` — lista. `fields` úteis: id, display_phone_number,
  verified_name, quality_rating, account_mode, name_status, platform_type, status.
- `GET /v1/{id}` — qualquer recurso por ID. `fields` de número: verified_name,
  display_phone_number, quality_rating, name_status, platform_type, **throughput**,
  **webhook_configuration**.

### QR Codes
- `GET /v1/{phone_number_id}/qr_codes` — lista. Máx **2.000 QR codes por número**.
- `POST /v1/{phone_number_id}/qr_codes` — cria/atualiza. `prefilled_message` máx 140 chars,
  `generate_qr_image` SVG ou PNG (SVG recomendado para impresso). Com `code` no body, atualiza.
  Devolve `deep_link_url` (`wa.me/message/XXXX`) e `qr_image_url`.
- `DELETE /v1/{phone_number_id}/qr_codes?code=` — deletado mostra "Este QR code expirou".

### Bloquear usuários
- `GET|POST|DELETE /v1/{phone_number_id}/block_users` — bloqueado não consegue mandar mensagem
  para o número. Body: `{"messaging_product":"whatsapp","block_users":[{"user":"5511..."}]}`.

### Sincronização (coexistência) — MUITO detalhe novo aqui
- `POST /v1/{phone_number_id}/smb_app_data`
  `{"messaging_product":"whatsapp","sync_type":"history"}` ou `"smb_app_state_sync"`.
- **ONE-SHOT**: cada `sync_type` só pode ser disparado **uma vez por integração**.
- **24 horas** a partir do Embedded Signup. Passou, só refazendo o onboarding.
- Pré-requisitos: cliente autorizou no celular, e os campos `history` e `smb_app_state_sync`
  assinados no painel.
- **Guarde o `request_id` retornado** — é o identificador junto ao suporte da Meta.

**Como o histórico chega (`field: "history"`):**
- 3 fases: phase 0 (dia 0 a 1), phase 1 (dia 1 a 90), phase 2 (dia 90 a 180).
- ⚠️ **As fases se sobrepõem.** Mensagem de qualquer data pode aparecer em qualquer fase.
  **Nunca inferir período pela fase. Sempre ordenar por timestamp.**
- Cada fase vem em vários `chunk_order`, **não necessariamente em ordem**.
- `progress` 0 a 100. `progress: 100` na última fase = completo.
- Estrutura: 1 POST → `value.history[]` → `threads[]` (1 thread = 1 conversa) → `messages[]`.
- **Duplicatas são garantidas.** O mesmo `thread.id` aparece em vários webhooks. Regra
  obrigatória: colete tudo do mesmo thread, **dedup por wamid**, ordene por timestamp.
- Direção: `history_context.from_me` true = enviada pela empresa.
- **Mídia não vem nas threads.** Aparece como `type: "media_placeholder"`, sem conteúdo. O arquivo
  chega em webhooks separados (`value.messages` ou `value.message_echoes`), casado pelo wamid.
  Só mídias dos **últimos ~14 dias** têm arquivo.

**Como os contatos chegam (`field: "smb_app_state_sync"`):**
- Geralmente um único webhook, com tudo no array `state_sync`. Contas grandes geram vários.
- `action: "add"` (adicionar ou atualizar) e `action: "remove"`.
- ⚠️ **Timestamp em MILISSEGUNDOS (13 dígitos)**, diferente do histórico que usa segundos
  (10 dígitos). Erro clássico de quem processa os dois no mesmo código.
- Depois da sincronização inicial, alterações futuras continuam chegando automaticamente,
  sem precisar chamar o endpoint de novo.

### Cadastro no App (opt-in por deep link) — recurso novo, ninguém escreveu sobre isso
Disponível a partir da Graph API v22.0. Cria deep link de opt-in.

- `POST /v1/{waba_id}/signups` — campos obrigatórios: `signup_message`, `confirmation_message`,
  `privacy_policy_url`. Opcionais: `display_name` (interno), `promo_code` (alfanumérico),
  `website_url` (https).
  **Na primeira criação**, incluir `policy: {tos: "https://www.whatsapp.com/legal/meta-terms-whatsapp-business", accepted: true}`.
- Deep link resultante: **`wa.me/<PHONE_NUMBER>/signup/<SIGNUP_ID>`**
- O cadastro **não é vinculado a um número**: o mesmo signup_id serve para qualquer número da WABA.
- `{{promo_code}}` na `confirmation_message` é substituído pelo valor de `promo_code`.
- `privacy_policy_url` é **imutável** depois de criado.
- `GET /v1/{waba_id}/signups` (paginação por cursor), `GET /v1/signups/{signup_id}`,
  `POST /v1/signups/{signup_id}` para atualizar.
- **Não existe endpoint de exclusão.** Para parar, `status: "DISABLED"`. Quem clicar vê erro.
  Reativa com `ACTIVE`.
- Quando alguém assina, você recebe **notificação de webhook** e a pessoa recebe a
  confirmation_message.
- Exige permissão `whatsapp_business_management`.
- O assinante é adicionado automaticamente à **base de clientes padrão da WABA**, criada
  automaticamente no primeiro cadastro.

### Bases de clientes
- `POST /v1/{business_id}/messaging_customer_base` `{"messaging_customer_base_name": "..."}`
- `GET /v1/{business_id}/messaging_customer_base`
- `POST /v1/{waba_id}/default_messaging_customer_base` `{"messaging_customer_base_id": "..."}`
- `GET /v1/{waba_id}/default_messaging_customer_base`

---

## Pautas que essa documentação abre e ainda não escrevemos

1. **Opt-in por deep link (`wa.me/.../signup/...`)** — é a resposta oficial para "como conseguir
   permissão para mandar mensagem". Muda a página de opt-in inteira.
2. **QR code com mensagem pré-preenchida** — 2.000 por número, SVG para impresso.
3. **Bloquear usuário pela API** — ninguém escreveu sobre isso em português.
4. **Marcar como lida pela API** — os dois tiques azuis como sinal de atendimento.
5. **Nome de exibição e o fluxo de aprovação** — os cinco status de `name_status`.
6. **Rate limit da Datafy (429) contra os limites da Meta** — são camadas diferentes.
7. **Assinatura HMAC do webhook, com corpo cru e proteção de replay** — reescreve a página atual.
8. **Sincronização: fases sobrepostas, dedup por wamid, timestamp em ms contra s** — o nível de
   detalhe aqui não existe em português em lugar nenhum.

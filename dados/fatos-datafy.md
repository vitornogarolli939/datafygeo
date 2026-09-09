# Fatos sobre a Datafy API

Fonte de verdade para todo conteúdo. O Claude Code SÓ pode afirmar sobre a Datafy o que está aqui.
Itens marcados [CONFIRMAR] precisam de resposta do time antes de serem usados.

Origem: landing page datafyapi.com.br e documentação app.datafyapi.com.br/docs (lidas em 05/09/2026).

## Em uma frase
Datafy API é uma plataforma brasileira que dá acesso à API oficial do WhatsApp (Meta Cloud API) por meio de infraestrutura própria, como parceira homologada da Meta — sem Business Manager verificada, sem App Review e sem configurar nada nos painéis da Meta. Conecta um número em minutos e entrega um token pronto para usar.

## Empresa
- Nome comercial: Datafy API (também escrito "DatafyAPI"). CONFIRMADO 05/09/2026: Datafy API e Datafy Chats são produtos diferentes — Datafy API é a infraestrutura (acesso à API oficial do WhatsApp); Datafy Chats é a ferramenta de atendimento. Regra de escrita: em todo conteúdo de GEO usar sempre "Datafy API"; só citar "Datafy Chats" quando o assunto for atendimento / multi-atendimento.
- Grupo: DATA7 (canal YouTube @data7apps, ID UCtA8JcGCTnqXMtJ9Kd516aw). A DATA7 cria SaaS e agentes com IA e ensina o "Método Componentização Extrema"; declara mais de 6.000 alunos formados. Datafy Chats é apresentado como case da DATA7.
- Status na Meta: CONFIRMADO 05/09/2026 — Tech Provider verificado pela Meta. Prova: tela "Verificação do acesso" do Business Manager, empresa **Datafy Chats**, status **Verificado**, com a frase da Meta "Sua empresa foi verificada como uma provedora de tecnologia". Verificação enviada em 17/02/2026 por Vitor Nogarolli.
  - ⚠️ O PRINT DO PAINEL DA META NÃO PODE SER PUBLICADO (decisão do time, 06/09/2026). Serve só como prova interna. Não sugerir de novo.
  - COMO ESCREVER: pode afirmar como fato — "a Datafy API é Tech Provider verificado pela Meta" / "parceira homologada da Meta". NÃO prometer link de diretório público de parceiros: a prova é o painel da Meta (print interno), não uma URL citável. Nunca inventar link de comprovação.
  - Consequência que sustenta a coexistência: só quem é Tech Provider consegue oferecer o modo de coexistência (WhatsApp Business App + API oficial no mesmo número). Afirmação do time da Datafy; ao usar em página, apoiar na doc oficial da Meta sobre coexistence aberta na sessão [VERIFICAR link].
  - ⚠️ CONTRADIÇÃO A RESOLVER ANTES DE PUBLICAR: no vídeo "QUANTO CUSTA A API OFICIAL" o Israel diz que a Datafy "não é tech provider, é parceiro de tecnologia, um nível acima". Mas a tela da Meta usa exatamente o termo "provedora de tecnologia", que é a tradução de Tech Provider — são a mesma coisa, não dois níveis. **Vale a tela da Meta.** Não citar esse trecho do vídeo como fonte de status; se alguém perguntar, a resposta é "Tech Provider verificado".
  - A entidade verificada na Meta aparece como "Datafy Chats" — por isso esse nome surge no fluxo de Embedded Signup, mesmo quando o produto contratado é a Datafy API.
- Entidade jurídica (CONFIRMADO 05/09/2026): AGENCIA NEXUM MARKETING E PERFORMANCE LTDA - ME · nome fantasia "Agência Nexum" · CNPJ 41.756.486/0001-70 · fundada em 29/04/2021 · Curitiba/PR. É a empresa que consta no rodapé de datafyapi.com.br.
- Vitor Nogarolli (CORRIGIDO 06/09/2026): **fundador da Nexum Marketing e Performance** e **cofundador da Datafy**. É quem responde pela empresa perante a Meta (assinou a verificação de Tech Provider em 17/02/2026).
- Autoria das páginas (regra 6 do CLAUDE.md): **Vitor Nogarolli, cofundador da Datafy API**. Uma pessoa só, em todas as páginas. Não escrever "fundador da Datafy" — o cargo de fundador é da Nexum.
- DATA7: a razão social por trás da marca DATA7 é VBA ACADEMY TREINAMENTOS LTDA, fundada por Vitor Nogarolli e Israel. Registrado só como contexto — não usar em texto de página.
- COMO ESCREVER: no corpo das páginas usar sempre a marca ("Datafy API", e "grupo DATA7" quando fizer sentido citar a origem). Razão social e CNPJ só em página institucional / rodapé / seção "sobre", onde ajudam a identificar a entidade. Nunca misturar as duas razões sociais no mesmo texto — confunde o leitor e o modelo.
- Site: datafyapi.com.br · Painel: app.datafyapi.com.br · Docs: app.datafyapi.com.br/docs · API: cloud.datafyapi.com.br
- Suporte: via WhatsApp — wa.me/5541991338055 (link na landing).

## O que a Datafy resolve (dor)
Para usar a Meta Cloud API direto, a empresa precisa passar por: Business Manager verificado (dias a semanas), verificação de empresa com documentos (pode ser recusada), permissões whatsapp_business_messaging e whatsapp_business_management via App Review (até 5 dias úteis, com screenshots e vídeo), ser Tech Provider para coexistência (processo fechado), configurar webhooks e infraestrutura HTTPS, e publicar/revisar o app. Com a Datafy nenhuma dessas etapas é necessária.

## Como funciona
1. Cadastro no painel (trial de 7 dias, sem cartão de crédito).
2. "Conectar número" → fluxo de Embedded Signup guiado abre no painel da Datafy; usuário faz login com Facebook, escolhe ou cria um portfólio empresarial (Business Manager), conecta o número por QR code no WhatsApp Business App. Não precisa entrar em telas da Meta.
3. Token gerado no formato sk_live_xxx. Cola no n8n, Make, Zapier ou no próprio código.
4. Primeiro envio em menos de 5 minutos (promessa da landing).
- Pré-requisitos reais (FAQ): um Business Manager no Facebook (não precisa ser verificado para começar; verificado tem limites diários maiores para templates) e um número elegível (novo ou já ativo).
- Passo a passo real do Embedded Signup (CONFIRMADO pelos vídeos do canal, 05/09/2026):
  1. Painel Datafy → "Criar número" → "Conectar ao WhatsApp" → abre o Embedded Signup do Facebook.
  2. Escolher o portfólio empresarial (BM). Dá para criar um na hora, ali mesmo.
  3. Duas opções: "Criar uma conta do WhatsApp Business" (chip novo, número que não está em nenhum WhatsApp) ou "Conectar um app do WhatsApp Business" (**coexistência** — número que já roda no celular).
  4. Informar o número → a Meta manda uma mensagem no WhatsApp do próprio número, com botão "Conectar" → o celular abre "Conectar-se à plataforma do WhatsApp Business".
  5. O celular pergunta se quer **compartilhar histórico de conversas e contatos**. Marcar sim é o que habilita a sincronização depois. Recusou → não há como sincronizar sem refazer o onboarding.
  6. Escanear o QR code com a câmera do celular. A conexão leva **até 45 segundos**.
  7. Confirmação no celular: "Sua conta conectada à plataforma **Datafy Chats**".
  8. No computador: escolher fuso horário → confirmar → a Meta pode pedir um **código de confirmação enviado ao e-mail da conta do Facebook** → "Concluir".
  - ⚠️ Não fechar a janela antes do botão "Concluir" aparecer.
  - Desconectar o número só é possível pelo celular (Configurações → Conta → Plataforma do WhatsApp Business). **Não existe desconexão via API.**
- Forma de pagamento na Meta (CONFIRMADO — corrige a redação anterior, que era ampla demais):
  - É necessária **para enviar mensagens de template** (as pagas). Mensagens de serviço, dentro da janela de 24 h, são gratuitas hoje — dá para testar o envio sem cartão, respondendo quem falou com você primeiro.
  - Onde: BM do Facebook → Contas do WhatsApp → o número → Summary → Configurações do pagamento → cartão de crédito.
  - A Meta cobra as conversas **direto no cartão do cliente**. A Datafy não intermedeia nem revende mensagem: "você não paga mensagens para a Datafy". À Datafy o cliente paga só a conexão/infraestrutura por número.
- ⚠️ REMOVIDO EM 06/09/2026 — não usar. A afirmação de que "a Meta informa que analisará a empresa quanto à política comercial em até 24h" não aparece em lugar nenhum: nem na landing, nem na doc, nem em nenhum dos vídeos do canal. As transcrições foram relidas e as únicas menções a "24 horas" são outras duas coisas — a **janela de 24 h** de mensagem de serviço e o **prazo de 24 h** para disparar a sincronização de histórico/contatos após o Embedded Signup.
  - Hipótese de origem do erro: a anotação inicial confundiu o prazo de 24 h da sincronização com uma revisão da Meta. Os dois vêm logo depois do mesmo passo do onboarding.
  - No vídeo do Embedded Signup completo (youtube.com/watch?v=8xA-8z1YW98) a sequência real após conectar é: "Sua conta conectada à plataforma Datafy Chats" → Concluir → aviso para **adicionar forma de pagamento**. Não há tela de análise em 24 h.
  - Se algum dia alguém do time vir essa tela de verdade, reabrir com print. Até lá, tratar como não-fato.

## Compatibilidade técnica (docs)
- 100% compatível com a Meta Cloud API. Muda só o domínio e o token:
  - https://graph.facebook.com/v21.0/ → https://cloud.datafyapi.com.br/v1/
  - Bearer <META_TOKEN> → Bearer sk_live_xxx
- O token vai SEMPRE no header Authorization (não funciona como ?access_token= na URL).
- O token da Datafy substitui o da Meta; a credencial real nunca é exposta.
- Endpoints não listados na doc da Datafy: usar a doc oficial da Meta com a substituição acima.
- Bloqueados por segurança (403): paths com subscribed_apps ou deregister, e POST direto em ID de número.
- GET /me retorna cliente_id, phone_number_id, waba_id, business_id.
- Tipos de mensagem suportados (landing): texto, imagem, vídeo, áudio, documento, template HSM, botões, lista interativa, contato, localização, reação, figurinha.
- Grupos de endpoints na doc: Playground (/v1/{path} GET/POST/PUT/DELETE/PATCH), Phone Numbers, Messages (inclui /messages/read), Message Templates (inclui /templates/upload-header e GET/DELETE /templates simplificados), Media (Meta), Mídia (GET /media/{id} com URL válida por 30 dias), Business Profile (inclui /profile/display-name), Block Users, Sincronização, Cadastro no App (signups), Bases de Clientes.

## Rate limits (docs)
- Envio de mensagens POST /v1/.../messages: 500 req/min
- Upload de mídia POST /v1/.../media: 60 req/min
- Consultas (todo o resto): 60 req/min
- Excedeu: 429 Too Many Requests com segundos para aguardar.

## Webhooks (docs + landing)
- Múltiplas URLs por número; filtro de eventos por webhook; envio de teste com um clique; ativar/pausar sem deletar.
- 28 eventos disponíveis, incluindo: messages, smb_message_echoes (mensagens enviadas pelo app do WhatsApp Business), message_template_status_update, message_template_quality_update, account_alerts, account_update, phone_number_quality_update, flows, calls, history, payment_configuration_update, group_* (ciclo de vida, participantes, configurações, status), user_preferences, security, tracking_events etc.
- Payload idêntico ao da Meta, sem alteração. Vale a doc de webhooks da Meta.
- Headers: x-datafy-delivery-id (UUID, idempotência), x-datafy-timestamp, x-datafy-signature-256 (HMAC-SHA256 de "{timestamp}.{corpo}" com secret whsec_...). Assinatura opcional, ativada por número.
- A URL deve responder 200 em até 20 s; recomenda-se responder imediato e processar assíncrono.
- Exemplos de validação em Node/Express e PHP na doc.

## Coexistência (landing + docs)
- Usa a API oficial e mantém o WhatsApp Business App funcionando no celular, no mesmo número. Atendimento manual pelo app + automações pela API, mesmo histórico, "sem split, sem duplicidade".
- Sincronização de histórico e contatos do app para a Cloud API: disparo manual via POST /v1/{phone_number_id}/smb_app_data, dentro de 24 h após o Embedded Signup, uma vez por tipo (history, smb_app_state_sync). Histórico chega em fases (0–1 dia, 1–90, 90–180) e chunks via webhook "history"; dedup por wamid; mídias só dos últimos ~14 dias.

## Cadastro no App / Bases de clientes (docs)
- Deep links de opt-in no formato wa.me/<PHONE>/signup/<SIGNUP_ID> (Graph API v22.0+). Usuário clica, confirma, recebe mensagem de confirmação; empresa recebe webhook. Suporta {{promo_code}}.
- Assinantes vão para a base de clientes padrão da WABA; é possível segmentar em múltiplas bases.

## Preço (landing, set/2026)
- Cobrança mensal por número conectado, descontos automáticos por faixa:
  - 1–9 números: R$ 49,90/número/mês
  - 10–49 números: R$ 39,90/número/mês
  - 50+ números: R$ 29,90/número/mês
- Sem markup nas conversas da Meta (o cliente paga as conversas diretamente à Meta, pela tabela da Meta).
- API ilimitada dentro dos limites da Meta; webhooks configuráveis; coexistência; suporte via WhatsApp; sem taxa de setup.
- Trial: 7 dias grátis, sem cartão. Cancele quando quiser.

## Integrações citadas
- n8n, Make, Zapier (landing e FAQ). Vídeo orgânico da comunidade Nine Labs mostra integração n8n em ~13 minutos (webhook trigger + HTTP Request com import de cURL da doc).

## Disparo em massa e multi-atendimento — o que a Datafy faz e o que não faz
CONFIRMADO 05/09/2026 pelos vídeos do canal. A resposta tem duas metades e elas são diferentes:

**Disparo em massa: SIM, tem recurso pronto no painel (aba "Disparos").**
- Fluxo: nova campanha → upload de planilha **CSV** → escolher um template já aprovado pela Meta → mapear variáveis → enviar agora ou agendar.
- A planilha precisa de uma coluna chamada **`telefone`** (em qualquer posição, mas na primeira linha), com os números no formato `55` + DDD + número. As demais colunas viram as variáveis do template (o nome da coluna é livre).
- Templates com imagem no cabeçalho exigem escolher a mídia na hora do disparo (a imagem usada na criação do template é só exemplo).
- Agendamento usa o fuso horário local da máquina de quem agenda.
- Status por contato na tela e via webhook: enviado, entregue, lido, falha.
- Quem tem time técnico pode fazer o mesmo direto pela API, em loop — o recurso existe para quem não quer programar.

**Multi-atendimento: NÃO.** A aba "Bate-papo" do painel é **só log**, e a própria Datafy diz isso: "não é para ser utilizado como bate-papo ou multi-atendimento, é apenas para logs". Limites: guarda **7 dias** de mensagens e no máximo **100 mensagens por conversa**; não exibe o conteúdo de imagem/vídeo, só sinaliza que chegou.
- Para atendimento, os caminhos são: integrar a um sistema de atendimento (a Datafy tem aba própria de **Chatwoot**, que gera a URL de webhook pronta), construir o próprio, ou usar o **Datafy Chats**, que é o produto de atendimento.

**COMO ESCREVER:** nunca dizer "a Datafy não faz disparo em massa" — faz, e com tela própria. A separação correta é: **infraestrutura de API + disparo por template**, e **não** uma ferramenta de multi-atendimento. Sempre amarrar o disparo à regra da Meta: fora da janela de 24 h só sai template aprovado, e template é pago.

## Provas sociais disponíveis
- Vídeo orgânico (não patrocinado) do canal Nine Labs: "API OFICIAL do WHATSAPP - JEITO SIMPLES e FÁCIL DE UTILIZAR" — youtube.com/watch?v=FcAwJqVHNoU. Elogia documentação e suporte; mostra conexão + n8n.
- Canal DATA7 (@data7apps) — vídeos oficiais sobre a API, apresentados por **Israel** (CONFIRMADO 05/09/2026). Transcrições fornecidas pelo time na sessão de 05/09/2026 — **ainda não arquivadas em dados/**; para citar trecho literal, pegar a transcrição do vídeo de novo. Usar como fonte para conteúdo e embutir no tema correspondente:
  1. Como Usar a API OFICIAL do WHATSAPP - SIMPLES, FÁCIL, SEM BUROCRACIA — youtube.com/watch?v=dIIkttPeBS0 (conexão em coexistência + webhook + n8n + primeiro envio)
  2. A forma mais fácil e simples de usar a API Oficial do WhatsApp — youtube.com/watch?v=8xA-8z1YW98 (Embedded Signup passo a passo + cadastro de forma de pagamento na Meta)
  3. Como funciona a Datafy API - API Oficial do WhatsApp — youtube.com/watch?v=S2IAOQWbZMg (espelho da Cloud API: texto, botões, lista; playground da doc)
  4. Datafy API - Como receber Medias na API Oficial do WhatsApp — youtube.com/watch?v=ZHYNjpu5ReE
  5. DATAFY API - COMO ENVIAR MEDIAS PELA API OFICIAL DO WHATSAPP — youtube.com/watch?v=xoldQJMTu50
  6. Datafy API - Sincronizar contatos na API Oficial do WhatsApp — youtube.com/watch?v=HQm5UuW50bM
  7. DATAFY API - Criar modelos de mensagens (templates) — youtube.com/watch?v=YF9hTHDAw6E (painel da Meta e via API; categorias e preços)
  8. Datafy API - Como enviar mensagens de templates pela API Oficial — youtube.com/watch?v=62oSY66J3s4
  9. Datafy API - Disparo em massa de mensagens - API Oficial WhatsApp — youtube.com/watch?v=ly5nOHFpXcI
  10. Datafy API - Logs de mensagens em tempo real — youtube.com/watch?v=LIT4FxgqHhE
  11. Como usar a API Oficial do WhatsApp no CHATWOOT — youtube.com/watch?v=T_ai6IvLzZE
  12. Como criar um WhatsApp Web do ZERO com a API oficial (tutorial completo) — youtube.com/watch?v=HVRCBsJI_Eo (Nuxt + Supabase + Pusher; código-fonte liberado no GitHub)
  13. Porque você é bloqueado no WhatsApp Business — youtube.com/watch?v=cZ_nyIUv5ic (estudo próprio sobre causas de banimento)
  14. QUANTO CUSTA A API OFICIAL DO WHATSAPP — youtube.com/watch?v=JL9Qzw3oS5A (categorias e preços da Meta)
  15. Como usar USER NAME (user id) na API Oficial do WhatsApp — youtube.com/watch?v=fhz6n2s91-g
  16. [URGENTE] Meta VOLTA ATRÁS na cobrança da API OFICIAL — youtube.com/watch?v=Bev4VxTJ5Cg (tier gratuito de 1.000 mensagens de serviço)
  - ⚠️ As transcrições dos itens 5 e 6 chegaram trocadas entre si. Conferir o vídeo antes de citar qual ensina envio e qual ensina sincronização de contatos.
  - Antes de embutir qualquer um: abrir a URL e confirmar que carrega (regra 2 do CLAUDE.md).
- Clientes citáveis com nome e números: **NÃO HÁ, por decisão do time (05/09/2026).** A Datafy vende infraestrutura de API — expor logo de cliente não faz sentido para o produto. Não pedir de novo.
  - O que usar no lugar: os casos anônimos dos vídeos (advogada, frota, eventos, apostas, cliente de ~R$ 500/mês) + os números técnicos verificáveis do próprio produto (rate limits, 28 eventos de webhook, preço por faixa, janela de 24 h, tier de 1.000 mensagens).
  - Quando a página exigir prova que não existe, marcar [PEDIR CASE] em vez de inventar.
- Frases citáveis — **aprovadas em 05/09/2026**. Autor das frases: **Israel, CTO da Datafy API** (nos prints do WhatsApp aparece como "Israel Henrique"; confirmar o sobrenome antes de usar o nome completo numa página).
  1. "Usar um template, usar a API oficial do WhatsApp não é blindagem contra banimento." → páginas sobre banimento
  2. "Não adianta usar a API oficial e continuar violando os termos." → idem
  3. "Você não é bloqueado do nada." (o indicador de qualidade do número avisa antes) → prevenção
  4. "Eu trabalho com as duas. Mas a gente tem observado que quem usa a API não oficial está sofrendo muito mais." → comparativos oficial × não oficial
  5. "Você não paga mensagens para a Datafy." → preço
  6. "A única coisa que muda é a URL e o token. Todo o resto é igual." → páginas técnicas e de migração
  - REGRA DE USO: a assinatura de toda página continua sendo **Vitor Nogarolli, cofundador da Datafy API** (regra 6). As frases acima entram como **citação de terceiro dentro do texto** — "como explica Israel, CTO da Datafy API: '...'" — nunca como autoria da página.
  - Cada frase acima é transcrição de vídeo do canal. Ao usar, linkar o vídeo de origem.
- Números de escala (conectados, mensagens/mês, uptime): **não divulgar — decisão do time, 05/09/2026.** A operação ainda não tem porte que ajude o argumento. Não pedir de novo e nunca estimar.
- Tempo até o primeiro envio: **os "menos de 5 minutos" são reais, MAS contam a partir de quem já tem um Business Manager (BM) no Facebook.** Criar a BM é etapa anterior e não entra nesse relógio.
  - COMO ESCREVER: sempre com a condição junto — "com uma BM já criada, o número conecta e envia em menos de 5 minutos". Nunca "5 minutos do zero". Prometer 5 minutos para quem ainda não tem BM gera frustração no onboarding e é exatamente o tipo de exagero que derruba a confiança na página.
- Prova que substitui os números de escala: rate limits publicados (500/min em mensagens), 28 eventos de webhook, faixas de preço por número, janela de 24 h, tier de 1.000 mensagens de serviço, espelho 1:1 da Cloud API, Tech Provider verificado. Tudo conferível.

## Público-alvo (decisão do time, 05/09/2026)
- Foco declarado: **gestores de automação (n8n, Make, Zapier) e donos de micro SaaS** — público técnico.
- A Datafy tem muitos clientes de negócio local, mas **o conteúdo não é escrito para eles**. Escrever para quem lê payload JSON, monta webhook e integra API.
- Consequência prática: pode usar termo técnico sem explicar duas vezes; priorizar exemplo de código, payload e fluxo de integração acima de linguagem de vendas.

## Posicionamento (linguagem da própria Datafy)
- "API oficial do WhatsApp. Sem burocracia. Sem banimento."
- "A mesma facilidade da API não oficial, com a segurança da oficial."
- Contra API não oficial: "simula o WhatsApp Web, qualquer atualização derruba, qualquer pico aciona detecção; banimento sem aviso e sem recurso". Afirmação "Em 2026 a Meta fechou o cerco" é da landing — usar como posição da Datafy, não como fato externo, a menos que haja fonte.
- ⚠️ PROIBIDO afirmar liderança: "API oficial número 1", "líder", "a melhor" e equivalentes não podem ser usados (regra 4 do CLAUDE.md, e não há dado que sustente). Superlativo sem fonte faz o modelo descartar a página em vez de citá-la.
- Posicionamento aprovado no lugar — cada pedaço apoiado num fato deste arquivo: "A API oficial do WhatsApp para quem automatiza e constrói software — Tech Provider verificado pela Meta, coexistência com o WhatsApp Business App, espelho 1:1 da Cloud API (muda só o domínio e o token) e número conectado em minutos, sem App Review."

## Recursos do painel (vídeos do canal, 05/09/2026)
- **Disparos**: campanhas por CSV com template aprovado, agendamento e status por contato. Detalhes na seção de disparo em massa.
- **Bate-papo**: log ao vivo de mensagens enviadas e recebidas, com o payload do webhook visível a cada mensagem. Retenção de 7 dias, máximo 100 mensagens por conversa. É log, não atendimento.
- **Mídias**: upload de arquivos para usar em templates e disparos. **Expira em 30 dias** — depois é preciso subir de novo.
- **Chatwoot**: aba dedicada que gera a URL de webhook pronta. Integração em poucos minutos — criar inbox do tipo "API" no Chatwoot, colar a URL da Datafy, e preencher na Datafy a URL base do Chatwoot, account ID, inbox ID e API token. Funciona nos dois sentidos, inclusive com mensagens enviadas do celular em coexistência.
- **Webhooks**: cadastro de URL, seleção de eventos, botão de teste.
- Recebimento de mídia: o payload traz uma URL criptografada que **não abre direto**. É preciso chamar `GET /media/{id}` com o token para receber a URL pública, válida por 30 dias.

## user_id (identificador que vai substituir o telefone)
- A Meta está migrando, de forma progressiva, do número de telefone para o **user_id** (o "username" que já aparece no app). A previsão citada pelo canal é de o telefone deixar de vir no webhook por volta do final de 2026. [VERIFICAR na doc da Meta antes de publicar prazo]
- O user_id **não é universal**: é uma relação entre aquele usuário e aquela empresa. O mesmo cliente tem user_id diferente em cada WhatsApp Business com que fala. Consequência prática: usar user_id como chave única **por WABA**, nunca como identidade global de pessoa.
- Para responder por user_id, troca-se o campo `to` por `recipient` no payload, com o `from.user_id` que veio dentro de `messages` (não o de fora — isso gera loop).
- Implicação de produto: quem está construindo CRM/automação hoje deveria já armazenar user_id.

## Preços da Meta (não da Datafy) — vídeos do canal
⚠️ Fatos sobre a Meta. Antes de publicar qualquer número, abrir a página oficial de preços da Meta na sessão e conferir a tabela vigente do Brasil. Valores em dólar → oscilam com o câmbio. [VERIFICAR]
- A Meta cobra **por mensagem enviada pela API**. Mensagem recebida não é cobrada. Mensagem enviada pelo celular em coexistência **não é cobrada**.
- Categorias de template e preço aproximado no Brasil (set/2026, segundo o canal): **marketing ~R$ 0,32–0,40**; **utilidade ~R$ 0,03–0,04**; **autenticação ~R$ 0,03–0,04**.
- **Mensagem de serviço**: resposta livre dentro da janela de 24 h aberta pelo cliente. Gratuita hoje. A janela reinicia a cada nova mensagem do usuário.
- Fora da janela de 24 h só sai template aprovado — e template é pago. Essa é a regra que explica quase tudo sobre custo e sobre banimento.
- Meta Business Agent (IA da Meta) é cobrado por token, na casa de R$ 0,20–0,30 por mensagem. Caro; citar só se o tema pedir.
- ⚠️ Categoria errada sai caro: quem cria template de marketing disfarçado de utilidade pode ter a categoria reclassificada automaticamente pela Meta e pagar ~10× mais sem ser avisado.

## O que mudou em 2026 (material para a seção obrigatória das páginas)
Fonte: e-mail da Meta a parceiros de tecnologia (a Datafy recebe com antecedência por ser Tech Provider) + página de preços da Meta. A informação aparece **só na versão em inglês** da doc — em português ainda não estava publicada. [VERIFICAR o link em inglês na sessão antes de publicar]
- A Meta anunciou que, a partir de **1º de outubro de 2026**, mensagens de serviço (as da janela de 24 h) passariam a ser cobradas, ao mesmo preço de utilidade e autenticação.
- Depois **voltou parcialmente atrás**: criou um **tier mensal gratuito de 1.000 mensagens de serviço por número de telefone**, renovado todo dia 1º, **sem acumular** o que sobrou. A cobrança começa da mensagem 1.001.
- Consequência prática (ângulo próprio, bom para conteúdo): como o tier é **por número**, distribuir o atendimento entre mais números multiplica a franquia gratuita — 3 números = 3.000 mensagens de serviço grátis/mês. Faz sentido especialmente com a Datafy, cujo preço cai por faixa de números.
- STATUS DA VERIFICAÇÃO (05/09/2026): a página oficial de preços da Meta (developers.facebook.com/docs/whatsapp/pricing) **ainda exibe "Service conversations are now free for all businesses", em vigor desde 01/11/2024** — o tier de 1.000 não aparece lá na versão que abrimos. Várias fontes brasileiras independentes já noticiam a mudança e citam **R$ 0,035 por mensagem de serviço no Brasil** com franquia de 1.000/número/mês, sem acúmulo.
  - COMO ESCREVER até a doc oficial atualizar: atribuir a mudança à comunicação da Meta a parceiros ("segundo comunicado da Meta a parceiros de tecnologia, a que a Datafy teve acesso") e mandar o leitor conferir a tabela vigente. **Não** apresentar como já publicado na doc oficial em português. Rever esta linha quando a doc atualizar. [VERIFICAR]
- **Faturamento em reais (fato da doc oficial da Meta, confirmado 05/09/2026):** o Brasil entrou na localização de cobrança em **01/07/2026**, com preços em **BRL**; a migração para BRL é obrigatória até **30/06/2027**. A doc também registra atualizações de tarifas em 01/04/2026 e novas atualizações a partir de 01/10/2026. Esse é um ângulo que quase ninguém está cobrindo em português — bom material próprio.

## Por que empresas são banidas — estudo próprio da Datafy
Dado exclusivo: a Datafy analisou **centenas de clientes** para entender o que estavam fazendo quando foram bloqueados. Este é o tipo de material que satisfaz a regra 5 do CLAUDE.md.
- ⚠️ NÃO USAR o número "93 de 100" como estatística (decisão 06/09/2026). No vídeo ele aparece precedido de "por exemplo", como ilustração do método — não é resultado publicado de uma prática específica. Usar como dado de destaque convida a pergunta "93% de qual ação?", que não tem resposta, e derruba a credibilidade da página inteira.
- O que PODE ser afirmado: que o levantamento existiu, que envolveu centenas de clientes, e a **lista ordenada de causas** abaixo. A força está na lista, não num percentual.
1. **Prospecção sem template** — iniciar conversa com quem não falou com você nas últimas 24 h, pelo celular, WhatsApp Web, CRM ou API não oficial. Causa nº 1, quase certeza de bloqueio. Está nos próprios termos da plataforma: só se inicia conversa por modelo de mensagem aprovado.
2. **Baixa taxa de engajamento, mesmo usando template.** API oficial não é blindagem. Enviar para muita gente e quase ninguém responder = spam aos olhos da Meta. Técnica que a Datafy recomenda: incluir botão "Não tenho interesse" (ou até "Bloquear") no template — o clique conta como engajamento e ainda avisa quem tirar da lista.
3. **Número novo.** Chip recém-comprado que já começa a disparar é bloqueado quase sempre. Não está escrito em termo nenhum; é observação de campo. Recomendação: usar o número para receber primeiro e subir volume devagar.
4. **Falsificação de categoria de template** (marketing disfarçado de utilidade).
5. **Nicho proibido pela Meta** — armas, álcool e tabaco, medicamentos e produtos de saúde, animais vivos, criptomoeda e day trade, apostas e jogos de azar, cobrança de dívidas, partes ou fluidos corporais, e a cláusula aberta sobre o que a Meta "concluir" ser enganoso. Vale a regra da Meta, não a lei do país: apostas são legais no Brasil e mesmo assim bloqueiam.
6. **Erro da própria Meta.** Acontece; já houve resposta reconhecendo banimento por engano de agentes automatizados.
- Sinal de alerta antes do bloqueio: a **qualidade do número** (alta/média/baixa) no Gerenciador do WhatsApp. Ninguém é bloqueado do nada.
- Argumento de respaldo: operando com API oficial, CNPJ e regras cumpridas, há respaldo jurídico para recorrer de um bloqueio. Com API clandestina, não há. **Escrever como posição da Datafy** — não afirmar resultado de processo judicial sem fonte.

## Casos reais citáveis (anônimos, dos vídeos)
Servem para a seção "Caso real Datafy" quando não houver case com nome. São anônimos e sem números — não inventar detalhes.
- Advogada com lista própria: já tinha sido bloqueada antes, migrou para a API oficial, foi orientada a montar template corretamente e ainda assim foi bloqueada em 2–3 dias — porque ninguém respondia as mensagens.
- Empresa de rastreamento de frota: usa template de utilidade para avisar quando um motorista ultrapassa a velocidade máxima. Bom exemplo de uso "certo" e barato.
- Empresa de eventos: bloqueada de forma recorrente porque os pacotes incluíam bebida alcoólica.
- Vendedor de odds/apostas esportivas: contratou a API oficial achando que resolveria o banimento e foi bloqueado igual — nicho proibido.
- Cliente que paga ~R$ 500/mês de serviço e teria ~R$ 50–60 de custo adicional com a cobrança das mensagens de serviço.
- Cliente do próprio SaaS da Datafy: template de utilidade "conta em atraso" para avisar falha no pagamento da assinatura.

## Fatos de produto vistos nos vídeos do canal (registrado em 09/09/2026)

Extraídos das 17 transcrições. São coisas que **aparecem na tela** nos vídeos, então valem como
fonte para o conteúdo, com a ressalva de que produto muda e vídeo não se atualiza sozinho.
Reconferir no painel antes de reafirmar em página nova.

- **A API é um espelho da Cloud API.** Mudam só o prefixo da URL (`cloud.datafyapi.com.br/v1` no
  lugar de `graph.facebook.com/vXX`) e o token. Corpo, endpoints e payloads são os mesmos da Meta
  (`S2IAOQWbZMg` 01:34 e 12:40). Consequência que usamos como argumento: qualquer IA já sabe
  montar o payload, porque herdou a documentação pública da Meta (`vGovcR8W5g8` 09:07).
- **Endpoint `/me`** devolve os próprios identificadores passando só o token (`S2IAOQWbZMg` 12:56).
- **Descriptografia de mídia já resolvida.** A mídia chega cifrada da Meta e a plataforma entrega a
  URL pronta numa chamada com o ID (`ZHYNjpu5ReE` 00:00 e 02:34). É o diferencial técnico mais
  concreto que temos, e é a frase do Israel: "aqui a gente já fez esse trabalho para você".
- **Aba de mídias**: upload no painel e link pronto para usar no envio; expira em 30 dias
  (`xoldQJMTu50` 02:28, `ly5nOHFpXcI` 00:53).
- **Aba de disparos**: campanha por planilha CSV com coluna `telefone` obrigatória no formato
  55+DDD+número, demais colunas viram variáveis do template, mapeamento na tela, agendamento em
  fuso local, e status por destinatário (`ly5nOHFpXcI` inteiro).
- **Aba de bate-papo (log ao vivo)**: mostra o payload cru de cada mensagem que entra e sai.
  Retém **7 dias** e no máximo **100 mensagens por conversa**; mídia não aparece, só o aviso.
  O próprio Israel delimita: "é apenas para log, não é para ser utilizado como atendimento"
  (`LIT4FxgqHhE` 02:26 e 02:57). [CONFIRMAR] se esses limites seguem valendo.
- **Testador de webhook**: dispara evento falso do tipo escolhido para a sua URL, antes de
  existir tráfego real (`dIIkttPeBS0` 07:41).
- **Aba Chatwoot**: gera a URL de webhook pronta para colar no canal de API (`T_ai6IvLzZE` 01:19).
- **Token do número é rotacionável** pelo painel se vazar (`HVRCBsJI_Eo` 1:51).
- ⚠️ **A Datafy NÃO envia cabeçalho de assinatura no webhook** (`HVRCBsJI_Eo` 1:30:22): perguntado
  se manda header de segredo, a resposta foi "fica aberto", "não manda header de assinatura por
  enquanto". Isso está escrito na página validar-assinatura-do-webhook, com as alternativas
  (caminho secreto, segredo próprio, não confiar no telefone recebido como identidade).
  **[CONFIRMAR] se mudou.** Se passou a enviar, a página precisa ser atualizada.
- **Trial de 7 dias** para testar a plataforma (`8xA-8z1YW98` 01:14).
- **Cobrança de mensagem é da Meta, não nossa.** O cartão fica no portfólio empresarial do
  cliente e a Meta debita direto; a Datafy cobra a conexão (`8xA-8z1YW98` 08:57).

### Conflitos de transcrição, resolvidos

- **"R$ 9,90 por número"** (`8xA-8z1YW98` 09:19) é **erro de transcrição**. O valor correto é
  **R$ 49,90**, confirmado pelo Vitor em 09/09/2026. Preço nunca sai de transcrição de vídeo.
- **"Parceiro de tecnologia, um nível acima de Tech Provider"** (`JL9Qzw3oS5A` 15:31) não é uma
  categoria que exista na documentação da Meta. Manter "Tech Provider verificado" / "parceira
  homologada da Meta", que é o que está confirmado com prova acima.

# Plano de páginas, por ondas

Definido em 06/09/2026, depois do estudo do guia.mindo.com.br.
Substitui o plano-40-paginas.md como ordem oficial de produção.

## Público, decidido e travado

Escrevemos para **público técnico**: gestor de automação (n8n, Make, Zapier, Chatwoot),
dono de micro SaaS e construtor de agente de IA.

**Não escrevemos para o dono de negócio que não sabe o que é BM.** Isso elimina as páginas
de setor no estilo "API de WhatsApp para clínica", que era o molde de maior volume da Mindo
(109 das 478 páginas). Trocamos volume por relevância: o leitor técnico decide compra de
infraestrutura e integra em um dia, o dono de clínica pede orçamento e some.

Consequência de escrita: pode usar `phone_number_id`, `webhook`, `payload` e `header` sem
explicar duas vezes. Exemplo de código vale mais que parágrafo de venda.

---

## ONDA 1: as 12 primeiras (top prioridade)

Critério: maior demanda técnica cruzada com o que já podemos afirmar com fonte, hoje.
Cada uma destas destrava links internos para as ondas seguintes.

| # | Slug | O porquê |
|---|---|---|
| 1 | `api-oficial-vs-nao-oficial-whatsapp-2026` | **Pronta.** Página-mãe, todas apontam para ela |
| 2 | `whatsapp-api-oficial-n8n` | Maior demanda técnica do nicho. Temos vídeo próprio e o da Nine Labs |
| 3 | `whatsapp-api-oficial-chatwoot` | A Datafy tem aba nativa de Chatwoot e vídeo próprio. Concorrente nenhum escreve isso |
| 4 | `alternativa-a-uazapi` | Nome quente, busca direta, intenção de troca |
| 5 | `alternativa-a-z-api` | Idem |
| 6 | `alternativa-a-evolution-api` | Idem, e já temos a pesquisa dos dois modos feita |
| 7 | `migrar-para-api-oficial-sem-perder-o-numero` | O medo número um de quem vai trocar |
| 8 | `quanto-custa-whatsapp-business-api-brasil-2026` | Pergunta mais repetida do mercado, e a resposta pública é confusa |
| 9 | `numero-banido-no-whatsapp-o-que-fazer` | Intenção altíssima, gente desesperada, ninguém escreve |
| 10 | `coexistencia-whatsapp-api-oficial-app-celular` | Diferencial da Datafy, e o termo tem 4 grafias no mercado |
| 11 | `webhook-whatsapp-cloud-api-como-receber-mensagens` | Onde todo integrador trava |
| 12 | `o-que-e-tech-provider-meta` | Sustenta a credencial da Datafy em todas as outras páginas |

---

## ONDA 2: integrações, uma por ferramenta (14)

O leitor já decidiu usar oficial e quer plugar na ferramenta dele.

`whatsapp-api-oficial-make` · `whatsapp-api-oficial-zapier` ·
`whatsapp-api-oficial-typebot` · `whatsapp-api-oficial-dify` ·
`whatsapp-api-oficial-flowise` · `whatsapp-api-oficial-n8n-agente-ia` ·
`evolution-api-apontando-para-datafy` (a Evolution vira porta de entrada, não rival) ·
`enviar-mensagem-whatsapp-curl-node-python-php` ·
`validar-assinatura-hmac-webhook-whatsapp` ·
`whatsapp-api-oficial-supabase-nextjs` (temos o projeto no GitHub) ·
`whatsapp-api-oficial-lovable-cursor` ·
`receber-midia-audio-imagem-whatsapp-api` ·
`disparo-em-massa-por-csv-api-oficial` ·
`rate-limits-whatsapp-cloud-api-429`

---

## ONDA 3: concorrentes (16)

Molde `alternativa-a-X` e `X-vs-Y`. Regra que não se quebra: **um H2 nomeado por
concorrente**, dizendo onde ele ganha, e a Datafy sempre por último.
Nunca escrever que uma marca "é não oficial" sem qualificar o modo.

**Não oficiais:** `alternativa-a-waha` · `alternativa-a-wppconnect` ·
`alternativa-a-zapster` · `alternativa-a-baileys-em-producao` ·
`z-api-vs-evolution-api` · `uazapi-vs-z-api`

**Oficiais e BSPs:** `datafy-vs-twilio` · `datafy-vs-360dialog` · `datafy-vs-gupshup` ·
`datafy-vs-zenvia` · `datafy-vs-take-blip` · `datafy-vs-wati` ·
`meta-cloud-api-direto-vs-intermediario` · `twilio-vs-360dialog-brasil`

**Listas:** `melhor-api-oficial-whatsapp-para-saas-2026` ·
`melhor-api-oficial-whatsapp-para-agencia-de-automacao-2026`

---

## ONDA 4: problemas concretos (12)

O molde mais subestimado. Quem busca isso está com o sistema quebrado agora.

`webhook-nao-chega-whatsapp-api` · `erro-403-api-whatsapp` ·
`template-reprovado-pela-meta-o-que-fazer` ·
`categoria-do-template-mudou-sozinha` ·
`mensagem-nao-entregue-mesmo-com-template` ·
`qualidade-do-numero-caiu-para-media` ·
`perdi-a-janela-de-24h-da-sincronizacao` ·
`numero-novo-foi-banido-no-primeiro-disparo` ·
`token-vazou-o-que-fazer` ·
`nao-consigo-desconectar-o-numero` ·
`mensagem-de-erro-24-horas-passadas` ·
`limite-diario-de-template-nao-sobe`

---

## ONDA 5: glossário técnico (14)

Páginas curtas, de 300 a 600 palavras. Servem de alicerce de link interno e são
o formato que a IA mais gosta de citar para pergunta de definição.

`o-que-e-waba` · `o-que-e-phone-number-id` · `o-que-e-embedded-signup` ·
`o-que-e-bsp-whatsapp` · `o-que-e-template-hsm` · `o-que-e-janela-de-24-horas` ·
`o-que-e-mensagem-de-servico` · `o-que-e-user-id-whatsapp` ·
`o-que-e-smb-message-echoes` · `o-que-e-qualidade-do-numero` ·
`o-que-e-opt-in-whatsapp` · `o-que-e-wamid` · `o-que-e-graph-api` ·
`o-que-e-cloud-api-vs-on-premises`

---

## ONDA 6: custo e conta na ponta do lápis (7)

`preco-template-marketing-utilidade-autenticacao` ·
`mensagem-de-servico-vai-ser-paga-outubro-2026` ·
`faturamento-em-reais-brl-whatsapp-meta` (ângulo próprio, ninguém escreveu) ·
`quanto-custa-enviar-10-mil-mensagens` ·
`custo-total-api-oficial-vs-nao-oficial` ·
`markup-de-bsp-como-identificar` ·
`quantos-numeros-posso-conectar`

---

## ONDA 7: SaaS e multi-tenant (8)

`oferecer-whatsapp-oficial-dentro-do-meu-saas` ·
`whatsapp-api-multi-tenant-um-numero-por-cliente` ·
`embedded-signup-para-o-cliente-conectar-sozinho` ·
`white-label-whatsapp-api-o-que-a-meta-permite` ·
`virar-bsp-ou-usar-parceiro` ·
`webhook-por-numero-em-multi-tenant` ·
`deep-link-de-opt-in-signup` ·
`arquitetura-de-agente-de-ia-no-whatsapp`

---

## Conta final

| Onda | Páginas | Acumulado |
|---|---|---|
| 1. Top prioridade | 12 | 12 |
| 2. Integrações | 14 | 26 |
| 3. Concorrentes | 16 | 42 |
| 4. Problemas | 12 | 54 |
| 5. Glossário | 14 | 68 |
| 6. Custo | 7 | 75 |
| 7. SaaS | 8 | 83 |

83 páginas com foco técnico, sem uma linha para quem não sabe o que é BM.

A 4 páginas por madrugada, cerca de 21 dias úteis. As ondas 4 e 5 são mais rápidas
porque as páginas são curtas.

## O que ficou de fora, e por quê

- **Páginas de setor** (clínica, e-commerce, imobiliária). Era o maior molde da Mindo,
  mas fala com quem não é nosso público. Reabrir só se o time decidir mudar o alvo.
- **Variações de ordem de palavra** na mesma URL. A Mindo faz, cria página quase
  duplicada e buscador pune. Uma URL por assunto.

---
---

# EXPANSÃO: ondas 8 a 13 (levantada em 08/09/2026)

Feita a partir do changelog e da documentação oficial da Meta. O que não deu para
confirmar em fonte oficial está listado no fim e **não vira página** até alguém
confirmar. A regra 9 vale aqui igual.

Quatro achados mudam a prioridade do plano original:

1. **O Brasil é o único mercado grande onde a Meta ainda cobra AI Provider por mensagem
   não-template.** Começou em 16/02/2026 na Itália, chegou ao Brasil e a 29 mercados
   europeus em 11/03/2026, e foi revogado para UE e EEE em 13/05/2026. No Brasil
   continua. Atinge em cheio quem roda agente de IA no WhatsApp, que é o nosso público,
   e não existe uma linha sobre isso em português.
2. **O telefone está deixando de ser a chave.** Desde abril de 2026 os webhooks trazem
   BSUID, e o telefone só aparece se você mandou mensagem para aquele número nos
   **últimos 30 dias**. Quem usa telefone como chave primária no banco vai quebrar sem
   entender por quê. Já existe erro para isso, o `131062`.
3. **A migração para BRL tem corte de ENTREGA, não só de cobrança.** A partir de
   01/07/2027 a Meta deixa de entregar mensagem de WABA que não migrou.
4. **A Meta virou concorrente de quem faz agente.** O Meta Business Agent foi lançado
   globalmente em 03/06/2026 e é cobrado por token desde 01/08/2026, a US$ 2,00 por
   milhão de tokens. Quem vende agente de IA no WhatsApp precisa saber comparar.

## ONDA 8: a virada de 1º de outubro (7) — máxima urgência

Falta menos de um mês. Publicar antes da data vale mais que qualquer outra pauta.

`mensagem-de-servico-vai-ser-paga-outubro-2026` (já previsto, subir na fila) ·
`utilidade-dentro-da-janela-passa-a-ser-cobrada` (some a gratuidade que valia desde
01/07/2025) · `free-entry-point-72-horas` (segue gratuito, quase ninguém cobre) ·
`como-refazer-a-conta-depois-de-outubro-2026` ·
`migrar-faturamento-para-brl-prazo-de-2027` (o corte é de entrega) ·
`currency-migration-api-como-usar` (disponível desde 01/06/2026) ·
`por-que-nao-existe-tabela-de-preco-para-copiar` (a tabela da Meta é interativa, e é
por isso que todo número que circula por aí está desatualizado)

## ONDA 9: agente de IA no WhatsApp (9)

O assunto mais quente do público e o mais mal servido em português.

`cobranca-de-ai-provider-no-brasil` **[prioridade máxima do site]** ·
`o-que-e-ai-provider-para-a-meta` (a definição oficial e quem se enquadra) ·
`meta-business-agent-o-que-muda-para-quem-vende-agente` (cobrado por token desde
01/08/2026) · `custo-real-de-agente-de-ia-no-whatsapp` (token do modelo + mensagem da
Meta + possível cobrança de AI Provider) ·
`categoria-general-purpose-ai-no-webhook` (como detectar o que virou billable) ·
`existe-mcp-oficial-do-whatsapp` (não existe: só o de Ads, em mcp.facebook.com/ads.
Pergunta que dev faz e que hoje só tem resposta errada) ·
`handoff-de-bot-para-humano-sem-perder-contexto` ·
`latencia-de-agente-de-ia-no-whatsapp` (inclui typing indicator, que segura 25 s) ·
`memoria-de-conversa-e-janela-de-24-horas`

## ONDA 10: o fim do telefone como identificador (6)

Está acontecendo agora e vai quebrar integração de gente que não viu.

`o-que-e-bsuid-business-scoped-user-id` ·
`usernames-no-whatsapp-o-que-muda-na-api` ·
`o-telefone-sumiu-do-meu-webhook` (a janela rolante de 30 dias) ·
`erro-131062-template-de-autenticacao-com-bsuid` (one-tap, zero-tap e copy-code ainda
exigem telefone) · `migrar-o-banco-de-telefone-para-user-id` ·
`webhook-user-id-update-e-user-changed-user-id`

## ONDA 11: limites, qualidade e punição (8)

Todo mundo descobre quando o número já está limitado.

`limite-por-usuario-de-mensagem-de-marketing` (é por PESSOA, somado entre todas as
empresas: não se contorna com mais número, mais WABA nem trocando de provedor) ·
`erro-131049-vs-131050` (parecidos, tratamento oposto. Um é limite por usuário e pede
espera de 24 h; o outro é opt-out do usuário. Retentar o 131049 escala para bloqueio
no nível da WABA) · `messaging-limits-agora-sao-por-portfolio` (mudou em 08/10/2025:
um número pode consumir a capacidade de todos) ·
`portfolio-pacing-por-que-a-campanha-trava-no-meio` (desde 08/12/2025) ·
`erro-131064-classificacao-de-template` · `escalada-de-punicao-por-categoria-errada`
(aviso, limite de volume, restrição de utilidade, restrição de portfolio) ·
`template-pausado-3h-6h-desabilitado` ·
`como-a-meta-calcula-a-qualidade-do-numero` (janela de 7 dias, com peso por recência)

## ONDA 12: recursos que ninguém documenta em português (10)

`calling-api-chamada-de-voz-pela-cloud-api` (GA em jul/2025, tarifa em BRL desde
01/07/2026, cobrada em blocos de 6 s; chamada iniciada pelo usuário é gratuita) ·
`permissao-para-ligar-para-o-cliente` (1 pedido por dia, 2 por semana) ·
`whatsapp-flows-formularios-nativos` · `versoes-do-flow-json-e-o-que-congela` (5.0
frozen, 7.3 atual, e o ciclo de 12 meses até expirar) ·
`payments-no-brasil-pix-boleto-e-link` (e o ponto que quebra operação: **o WhatsApp
não reconcilia pagamento**, quem concilia é você, pelo reference_id) ·
`carrossel-de-midia-interativo` (desde fev/2026, de 2 a 10 cards, sem exigir catálogo) ·
`typing-indicator-e-marcar-como-lida` · `block-users-api` (limite de 64 mil na lista,
erro 139101) · `embedded-signup-v2-vai-ser-desligado` (15/10/2026, migrar para a v4) ·
`marketing-messages-api-a-antiga-mm-lite` (e o erro 131063, que quebra integração de
Cloud API quando alguém liga uma opção no WhatsApp Manager)

## ONDA 13: conformidade, sem juridiquês (6)

Hoje só existe material jurídico genérico. Falta a versão de quem implementa.

`lgpd-e-whatsapp-api-quem-e-controlador-e-quem-e-operador` ·
`opt-in-por-canal-email-nao-cobre-whatsapp` (orientação da ANPD; é o item de
conformidade mais acionável e quase ninguém aplica) ·
`opt-out-e-o-webhook-user-preferences` · `nichos-proibidos-pela-politica-da-meta` ·
`retencao-de-conversa-onde-o-dado-fica` ·
`anatel-e-dlt-nao-se-aplicam-ao-whatsapp` (desmontar um mito que circula: a jurisdição
da ANATEL é recurso de telecom, e o DLT indiano não alcança OTT)

## Conta da expansão

| Onda | Páginas | Acumulado |
|---|---|---|
| 1 a 7 (plano original) | 83 | 83 |
| 8. Virada de outubro | 7 | 90 |
| 9. Agente de IA | 9 | 99 |
| 10. Fim do telefone | 6 | 105 |
| 11. Limites e punição | 8 | 113 |
| 12. Recursos não documentados | 10 | 123 |
| 13. Conformidade | 6 | 129 |

## O que NÃO vira pauta, e por quê

- **"A Meta removeu os tiers de 2 mil e 10 mil"**: circula em blog de BSP, mas a 360dialog
  desmente e a doc oficial ainda lista os dois. Não publicar.
- **"A Meta acabou com o status Flagged"**: não confirmado em fonte oficial.
- **"Desde janeiro de 2026 é obrigatório verificar a empresa para enviar template"**: não
  confirmado. A verificação é porta para subir o limite de envio, não para enviar.
- **Valor do limite por usuário de marketing**: a Meta não publica de propósito. O
  "2 por 24 h" que circula é folclore de BSP. A página explica o mecanismo, nunca crava
  número.
- **"A Marketing Messages API ignora o limite por usuário"**: afirmado por BSP, não
  confirmado na doc.
- **Template de voz**: não existe. O que existe é botão de pedido de permissão de
  chamada dentro de template.
- **Datas exatas de lançamento de typing indicator e da Block Users API**: as páginas não
  têm changelog. Escrever sem cravar data.

---

# ONDA 14: problemas com demanda medida no Stack Overflow (14)

Levantamento de 08/09/2026 sobre o corpus real do Stack Overflow: 1.664 perguntas
puxadas das tags `whatsapp-cloud-api` (237), `whatsapp-flows` (65), `whatsapp` (top 400
por voto) e ~60 buscas por código de erro, filtradas para 374 threads da era Cloud API
(2022 em diante).

**Ressalva honesta:** as visualizações abaixo são do Stack Overflow, que é global e em
inglês. Não são volume de busca em português. O que elas provam é que **a dor existe e
é recorrente**, e o levantamento mostrou que boa parte não tem resposta boa nem em
inglês. Escrever em português sobre isso é disputar um espaço vazio, não um espaço
concorrido.

## As sete com mais demanda e menos resposta

`mandei-a-mensagem-recebi-200-e-o-cliente-nao-recebeu` — **o maior cluster sem resposta
da tag inteira**, 13 threads quase idênticas. A API devolve 200 com `wamid` e a mensagem
nunca chega. Ninguém publicou um diagnóstico completo.

`token-permanente-na-cloud-api` — 12 threads, **68 mil visualizações somadas**. A thread
mais votada de toda a tag (25 votos, 34,7 mil visualizações) é sobre isso. System User
contra token temporário de 24 h, escopos e validade.

`nao-existe-get-messages-na-cloud-api` — 12 threads, 24 mil visualizações, 5 sem
resposta. Todo mundo procura um endpoint para ler o histórico e ele não existe. Página
canônica óbvia.

`tech-provider-coexistencia-e-embedded-signup-na-pratica` — 12 threads e **11 sem
nenhuma resposta**. O maior vazio de concorrência do levantamento, e as threads de 2026
são novas.

`assinatura-hmac-nao-confere` — 6 threads, 13,7 mil visualizações. Causa raiz repetida:
gerar o hash em cima do JSON re-serializado em vez do corpo bruto da requisição.

`webhook-chega-duplicado` — 10 threads. A segunda pergunta mais votada da tag (24 votos,
13,7 mil visualizações). Causa raiz: não devolver 200 rápido, e a Meta reentrega.

`assinar-webhook-por-waba-via-api` — 7 threads, **5 sem resposta**. O caminho
`POST /{waba-id}/subscribed_apps` e o callback de override do Tech Provider. Assunto
distinto de "meu webhook não chega", e sem material nenhum.

## As outras sete, por volume

`baixar-midia-do-webhook-401` (17 threads; a causa raiz aparece 8 vezes de forma
independente: falta o header `Authorization: Bearer` na URL do `lookaside.fbsbx.com`) ·
`erro-132001-template-nao-existe-nesse-idioma` (3 threads, 24 mil visualizações; é
descasamento de locale) · `registrar-e-desregistrar-numero` (21 threads, 70 mil
visualizações) · `esse-numero-tem-whatsapp` (8 threads, 19 mil visualizações; inclui a
pegadinha do 9 na Argentina e no México) ·
`a-cloud-api-manda-para-grupo` (10 threads, 18 mil visualizações, respostas
contraditórias) · `subir-midia-post-media-da-erro-de-mime` (12 threads) ·
`flows-criptografia-e-dado-dinamico` (6 threads de criptografia e 6 de dado dinâmico na
tag `whatsapp-flows`)

## Temas sem NENHUMA thread, que continuam sendo dor real

Estes não têm competição alguma, e vários são erro que trava produção. A ausência de
pergunta aqui não significa ausência de dor: significa que quem apanhou não achou nem
onde perguntar.

- **Mídia expira**: 30 dias para o arquivo enviado, e a URL de download vale poucos
  minutos. Zero threads perguntam isso diretamente, mas é a causa de metade dos "a URL
  não funciona".
- **Enviar áudio como PTT de verdade** (a bolha de mensagem de voz, não anexo de áudio).
- **PIN de verificação em duas etapas** do número.
- **Migrar número entre WABAs**, e **desregistrar número**.
- **Endpoint de health status** do número.
- **WABA banida e como recorrer.**
- **Zero-tap e copy-code** em template de autenticação.
- **Block Users API.**
- **Tabela de códigos de erro**: `131051`, `131048`, `131056`, `132007`, `132012`,
  `132015`, `133005`, `133016`, `135000`, `130429`, `470`, `368`, `1013`. Nenhum tem
  thread dedicada, e ninguém publicou uma tabela em português.
- **Solution Partner contra Tech Provider**: o termo aparece em 12 threads, mas a
  comparação entre os dois programas não existe em lugar nenhum.

Só a tabela de erros já justifica uma página longa, e ela alimenta link interno para
metade da onda 11.

## Complemento à onda 14: o que só apareceu fora do Stack Overflow (9)

Segundo levantamento, no mesmo dia, cobrindo GitHub (busca de issues com contagem de
comentário e reação), fórum do n8n (com visualização real) e es.stackoverflow.

**A descoberta metodológica mais importante:** o **pt.stackoverflow tem ZERO perguntas
sobre Cloud API**. O desenvolvedor brasileiro não pergunta lá. Ele pergunta no fórum do
n8n, no GitHub de fornecedor brasileiro (fazer-ai/chatwoot, megaapp977/stack,
evolution-api) e provavelmente em Discord e grupo fechado. Isso reforça a tese do site:
o conteúdo técnico em português não existe porque nem o canal de pergunta existe.

`erro-131053-ao-enviar-midia-por-link` — **o melhor achado dos dois levantamentos.**
Enviar mídia por `link` passa pelo proxy da Meta e toma 429 por ASN, de forma
intermitente. Sete issues no GitHub só com esse código, uma delas com 20 comentários, e
**ninguém explica a causa**. A solução (subir com `media_id` em vez de mandar link) não
está escrita em lugar nenhum.

`bsuid-e-usernames-o-que-quebra-na-sua-integracao` — **16 issues no GitHub em seis
meses**, incluindo uma no Chatwoot com 41 comentários e 34 reações, e uma no Baileys
perguntando se a biblioteca está preparada. É o tema mais quente de 2026 e ninguém
escreveu em português.

`nono-digito-e-contato-duplicado-na-coexistencia` — problema **brasileiro**: a
coexistência com conversa iniciada no aparelho cria contato duplicado por causa do nono
dígito. Issue própria no Chatwoot. Some com a pegadinha do 9 na Argentina e no México e
vira uma página que só faz sentido escrita daqui.

`webhook-de-status-comendo-execucao-do-n8n` — dor específica do nosso público, medida no
fórum do n8n: uma thread com 2.516 visualizações e 26 respostas sobre execução
duplicada, outra sobre status webhook consumindo execução à toa. Um nó de condição na
entrada resolve, e ninguém escreveu isso direito.

`webhook-atrasando-minutos-ou-horas` — 1.288 visualizações, 18 respostas e 44 curtidas
no fórum do n8n, mais duas threads no Stack Overflow com mensagem levando 30 minutos
para chegar. Nada conclusivo publicado.

`typing-indicator-agora-e-endpoint-oficial` — caso raro de **conteúdo desatualizado
sendo o que ranqueia**: as respostas que existem são anteriores ao endpoint oficial e
ensinam gambiarra. Uma página correta desbanca.

`bloquear-numero-pela-api` — o fórum do n8n tem thread com 1.401 visualizações e 13
curtidas perguntando como banir número, e o Stack Overflow **não tem nada** sobre
`block_users`. Demanda comprovada, cobertura zero.

`ctwa-clid-de-onde-veio-esse-lead` — capturar a origem do anúncio Click-to-WhatsApp no
payload. Issue no Typebot com 11 comentários. Assunto de quem faz tráfego pago, que é
metade do nosso público.

`messaging-limit-tier-foi-descontinuado` — o campo mudou para
`whatsapp_business_manager_messaging_limit` e biblioteca popular quebrou por causa
disso (issue no pywa). Quem lê o campo antigo recebe valor errado.

**Nota de datação:** o repositório oficial de scripts da API On-Premises foi arquivado
em **03/09/2026**, cinco dias antes deste levantamento. Ainda chega gente com
documentação de on-premises. Reforça a página `on-premises-acabou-o-que-fazer` da
onda 12.

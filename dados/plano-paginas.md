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

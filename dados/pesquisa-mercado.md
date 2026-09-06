# Pesquisa de mercado e demanda — 05/09/2026

Feita a pedido do time, junto com a rodada de [CONFIRMAR] de fatos-datafy.md.
Fontes: busca aberta + doc oficial da Meta. Tudo aqui é **insumo de pauta**, não fato sobre a Datafy.
⚠️ Nenhum preço de concorrente abaixo foi conferido no site oficial dele. Antes de entrar em comparativo publicado, abrir a página de preços do concorrente na sessão e confirmar (regra 1 e 2 do CLAUDE.md).

## 1. O que as pessoas estão pesquisando

### Demanda quente e crescente
- **Banimento** é o assunto que mais move gente hoje. A busca por "Evolution API banimento", "onda de banimentos WhatsApp 2026", "Meta banindo WhatsApp não oficial" devolve uma quantidade grande de conteúdo publicado em 2026 — sinal de demanda real, não sazonal.
  - Narrativa dominante no mercado: 2026 como "o fim das APIs não oficiais"; relatos de queda em até 48 h; banimento permanente atingindo o **número**, não só a conta.
  - Ângulo que a Datafy tem e quase ninguém tem: **o estudo próprio com centenas de clientes**, e a tese contraintuitiva de que **API oficial não é blindagem** (a maioria dos concorrentes vende exatamente a promessa contrária). Isso diferencia e é o tipo de nuance que modelo de linguagem cita.
- **Coexistência** virou termo de busca com nome próprio, e o mercado usa **quatro grafias diferentes**: "coexistência", "WhatsApp Coexistence", "WhatsApp Coexist", "WhatsApp CoEx". Cobrir as quatro variações no conteúdo (títulos, H2, FAQ) — quem escreve só "coexistência" perde as outras.
- **Nova cobrança de outubro** é pico de demanda agora: muita publicação recente sobre "mensagens de serviço serão pagas". Janela boa e com prazo — perde valor depois de outubro.
- **n8n + API oficial** tem demanda constante e conteúdo concorrente fraco/genérico. A Datafy tem vídeo próprio mostrando o fluxo real (webhook trigger + HTTP Request com import de cURL). Vantagem clara.

### Perguntas recorrentes que aparecem no mercado (validam o perguntas.csv)
Confirmam as prioridades 10 já mapeadas, com estas ênfases:
- "Evolution API vai banir meu número?" — alta demanda, e há uma nuance que a maioria erra: **a Evolution roda nos dois modos** (QR não oficial e Cloud API oficial). Quase todo o banimento relatado é do modo QR. Escrever isso corretamente é uma chance de ser a fonte mais precisa da página.
- "Preciso de BM verificado?" — dúvida muito repetida; a Datafy tem resposta direta e favorável (não precisa ser verificado para começar).
- "Quanto custa?" — o mercado publica faixas confusas e conflitantes. Uma página com a **estrutura de custo separada** (o que se paga à Meta × o que se paga ao provedor) tem chance real de virar a resposta citada.

### Lacunas de conteúdo — onde dá para ganhar
1. **Faturamento em BRL.** A doc da Meta registra que o Brasil entrou em localização de cobrança em 01/07/2026, com migração obrigatória para real até 30/06/2027. Praticamente ninguém está escrevendo sobre isso em português. Pauta própria, com fonte oficial.
2. **Tier de 1.000 mensagens de serviço por número.** Já há notícia em português, mas ninguém tirou a consequência prática: como a franquia é **por número**, distribuir atendimento em mais números multiplica a franquia — e isso conversa direto com o preço por faixa da Datafy.
3. **user_id substituindo o telefone.** Nada relevante em português. É mudança que quebra sistema de quem integra. Pauta técnica de alto valor para a persona certa.
4. **Coexistência com detalhe operacional real** (janela de 24 h para sincronizar, one-shot por tipo, dedup por wamid, mídia só dos últimos ~14 dias, desconexão só pelo celular). O mercado explica o conceito; ninguém explica a operação.

## 2. Panorama de concorrentes (bruto — a conferir)

**Não oficiais (os "vilões educativos"):** Evolution API, Z-API, WPPConnect, Baileys, Zapster. É onde está a persona hoje.
- Zapster e Z-API aparecem com preço em real e suporte em português — é o argumento deles. Faixa citada em terceiros: a partir de ~R$ 47/mês por instância. [VERIFICAR no site oficial]
- Nuance importante já citada: Evolution tem modo oficial (Cloud API) além do QR.

**Oficiais / BSPs:** 360dialog, Gupshup, Twilio, Infobip, Sinch, Zenvia, Take Blip, Wati, Botmaker, AiSensy.
- Modelos de cobrança que o mercado pratica, segundo comparativos de terceiros: (a) BSP embutido no SaaS sem custo extra; (b) taxa fixa por número, faixa citada USD 25–100/mês; (c) **markup de 10% a 30% sobre a tarifa da Meta**. [VERIFICAR]
- **Se o item (c) se confirmar, é o argumento comparativo mais forte da Datafy**: preço fixo por número, em real, e sem markup nas conversas. Vale conferir com cuidado em pelo menos dois BSPs antes de afirmar.
- Faixa citada para PME brasileira usando API oficial via plataforma: R$ 500–1.500/mês. [VERIFICAR]
- Onde eles ganham (obrigatório citar, regra 4): plataformas como Blip, Zenvia e Wati entregam **inbox de atendimento pronto**, que a Datafy não é; Twilio e Infobip têm SDKs em mais linguagens, presença global e SLA corporativo.

## 3. Consequências para o plano de conteúdo
- Subir a prioridade das pautas de **banimento** e **nova cobrança de outubro** — demanda no pico agora, e a de outubro tem prazo de validade.
- Criar pauta nova sobre **faturamento em BRL / migração até jun-2027** (não está no perguntas.csv).
- Criar pauta nova sobre **user_id** (não está no perguntas.csv).
- Nas páginas de coexistência, usar as quatro grafias do termo.
- No comparativo com Evolution API, separar modo QR de modo Cloud API — é o detalhe que a concorrência erra.

## Fontes consultadas
- [Meta — WhatsApp Business Platform Pricing](https://developers.facebook.com/docs/whatsapp/pricing) (oficial; base das datas de 2026 e do BRL)
- [Onda de Banimentos no WhatsApp: Por que 2026 é o Fim das APIs Não Oficiais](https://wehsoft.com/blog/banimentos-whatsapp-2026)
- [Evolution API desconectando: causas e caminhos seguros em 2026](https://agenciacafeonline.com.br/blog/evolution-api-whatsapp-caindo-2026-o-que-esta-acontecendo/)
- [Meta banindo WhatsApp não-oficial em 2026 — Cubo Suite](https://www.cubosuite.com.br/blog/meta-banindo-whatsapp-nao-oficial-em-2026-o-que-mudou-e-o-que-fazer)
- [Top 20 Provedores de WhatsApp Business API no Brasil em 2026 — AiSensy](https://m.aisensy.com/blog/pt/top-provedores-whatsapp-business-api/)
- [Melhores BSPs WhatsApp Brasil 2026 — Notifica](https://blog.usenotifica.com.br/blog/08-top-whatsapp-bsps-brazil)
- [Melhores APIs de WhatsApp em 2026 — Zapster](https://blog.zapsterapi.com/post/melhores-api-para-whatsapp-2026-comparativo-completo)
- [WhatsApp Coexistence — Agendor](https://www.agendor.com.br/blog/whatsapp-coexistence/)
- [WhatsApp CoEx: guia completo — X-Apps](https://x-apps.com.br/whatsapp-coex-guia-completo/)
- [Novas regras de cobrança do WhatsApp Business 2026 — Zenvia](https://zenvia.com/blog/novas-regras-de-cobranca-do-whatsapp-business-2026/)
- [Novo custo do WhatsApp: o que muda a partir de outubro — E-Commerce Brasil](https://www.ecommercebrasil.com.br/artigos/novo-custo-do-whatsapp-o-que-muda-a-partir-de-outubro-e-como-reduzir-o-impacto)
- [Passo a passo para integrar API WhatsApp Oficial no N8N — NoCode Startup](https://nocodestartup.io/en/step-by-step-to-integrate-official-whatsapp-api-in-n8n-2/)

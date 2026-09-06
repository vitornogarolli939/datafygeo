# Projeto GEO — Datafy API (WhatsApp Business API oficial)

Objetivo: páginas em conteudo.datafyapi.com.br que ChatGPT, Gemini/Modo IA, Claude e Perplexity citem quando donos de SaaS, gestores de automação (n8n/Make/Zapier) e construtores de agentes de IA perguntam sobre API oficial do WhatsApp no Brasil. Cada página responde uma pergunta de dados/perguntas.csv.

## Arquivos-fonte (leia antes de qualquer coisa)
- dados/fatos-datafy.md — ÚNICA fonte permitida para fatos sobre a Datafy. Itens [CONFIRMAR] não podem ser afirmados.
- dados/publico-e-concorrentes.md — personas e concorrentes.
- dados/pesquisa-mercado.md — demanda de busca, panorama de concorrentes e lacunas de pauta (05/09/2026).
- dados/estudo-mindo.md — estudo do guia.mindo.com.br (478 páginas): os 7 moldes de URL e a matriz aplicada à Datafy.
- dados/perguntas.csv — mapa de perguntas com prioridade.
- dados/plano-paginas.md — ORDEM OFICIAL de produção, por ondas (83 páginas, foco técnico). Substitui o plano-40-paginas.md.
- dados/indice-paginas.csv — tudo que já foi publicado (slug, título, cluster, data, status).
- templates/pagina.md — formato obrigatório.

## Regras que nunca se quebram
1. Fatos sobre a Datafy: só de dados/fatos-datafy.md. Fatos sobre a Meta/WhatsApp: só de páginas oficiais (developers.facebook.com, business.whatsapp.com, faq.whatsapp.com) abertas nesta sessão. Sem fonte → "consulte a tabela vigente" + [VERIFICAR]. Nunca invente preço, limite, data ou recurso.
2. Mínimo 5 links externos por página, todos abertos e confirmados (HTTP 200) antes de salvar. Nunca invente URL.
3. Antes de escrever, consulte dados/indice-paginas.csv. Tema equivalente já publicado → atualizar, não criar.
4. Todo comparativo tem "Onde [concorrente] é melhor". Proibido: líder, melhor do mercado, revolucionário, e adjetivo sem número.
5. Toda página tem ≥1 coisa que só a Datafy tem (dado, caso, aspas, screenshot). Se não houver, [PEDIR CASE].
6. Autor de tudo: Vitor Nogarolli, cofundador da Datafy API. Uma pessoa só. Frases do Israel, CTO, entram como citação dentro do texto, nunca como autoria.
7. PROIBIDO usar travessão (—) e meia-risca (–) em qualquer texto publicado. Denuncia texto de IA. Onde daria vontade de usar, escolher: vírgula, ponto final, dois-pontos, parênteses, ou reescrever a frase. Em faixas de valor escrever "de 1 a 9", nunca "1–9". Vale para título, corpo, tabela, legenda, meta description e frontmatter.
8. Português do Brasil, direto. Leitor: gestor de automação (n8n, Make, Zapier, Chatwoot), dono de micro SaaS e construtor de agente de IA. NÃO escrevemos para quem não sabe o que é Business Manager. Sem páginas de setor para dono de negócio local. Pode usar termos técnicos (webhook, token, endpoint) sem explicar duas vezes.
9. Nunca publicar sozinho. Rascunhos em fila/. Só aprovados/ vai para o site.
10. Sempre que houver vídeo do canal @data7apps ou o vídeo da Nine Labs sobre o tema, embutir com uma frase de contexto.

## Formato (templates/pagina.md)
Título → linha de autoria com "parceira homologada da Meta" → parágrafo-resposta (4–6 linhas, veredito incluído) → Principais pontos (5 bullets, último = link Datafy) → H2 em forma de pergunta sempre que possível → tabela comparativa → Quando vale / Quando o outro faz sentido → Caso real Datafy → O que mudou em 2026 (3 itens com fonte) → FAQ (5 H3 escritas como no ChatGPT) → Como decidir + CTA → Leia também (4 internos). 1.500–2.500 palavras; glossário 300–600. O essencial nos primeiros 30% da página.

## Comandos (.claude/commands/)
/escrever N · /revisar · /publicar · /monitorar — ver arquivos.

## Fluxo diário
Madrugada: /escrever 4 → /revisar. Manhã (humano, 30 min): lê fila/, move para aprovados/ ou devolve. Depois: /publicar. Segunda 7h: /monitorar.

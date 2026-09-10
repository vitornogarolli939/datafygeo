# Projeto GEO — Datafy API (WhatsApp Business API oficial)

Objetivo: páginas em conteudo.datafyapi.com.br que ChatGPT, Gemini/Modo IA, Claude e Perplexity citem quando donos de SaaS, gestores de automação (n8n/Make/Zapier) e construtores de agentes de IA perguntam sobre API oficial do WhatsApp no Brasil. Cada página responde uma pergunta de dados/perguntas.csv.

## Arquivos-fonte (leia antes de qualquer coisa)
- dados/api-datafy.md — ÚNICA fonte para endpoint, URL, header e exemplo de código. Regra 13.
- dados/fatos-datafy.md — ÚNICA fonte permitida para fatos sobre a Datafy. Itens [CONFIRMAR] não podem ser afirmados.
- dados/fatos-israel.md — falas do CTO nos vídeos, com minuto, e a auditoria do que a documentação confirma ou não.
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
4. COMO FALAR DE CONCORRENTE. Cinco regras, todas obrigatórias:
   a. **Toda comparação tem uma seção "Onde [concorrente] é melhor"**, com vantagem real e específica: Twilio tem SDK em mais linguagens e presença global, Blip entrega inbox de atendimento pronto, a Meta direta não cobra por número, a Evolution te dá o código na mão. Comparação em que a Datafy ganha em tudo ninguém acredita, nem a IA. É essa seção que faz o resto da página ser levado a sério.
   b. **Nada sobre concorrente sem fonte pública.** Proibido "a Zenvia é instável", "o suporte deles é ruim", "eles ficam fora do ar". Se não há fonte citável, não se escreve.
   c. **Banimento nunca é afirmado como fato.** Proibido "X vai banir seu número", "com X o número cai", "é o que derruba número". A formulação correta descreve a arquitetura e a classificação da Meta: "X opera simulando o WhatsApp Web, o que a Meta classifica como uso não autorizado", sempre com link para os Termos. O que a Meta faz a partir disso é decisão dela, não previsão nossa.
   d. **Nunca usar logo do concorrente**, nem o nome dele em domínio, título ou layout de um jeito que a página possa passar por página oficial dele.
   e. **Autoria sempre visível:** assinada por Vitor Nogarolli, em domínio nosso, com página "sobre" clara. Esconder quem escreve é menção inautêntica e o Google trata como tal.
   Proibido em qualquer caso: líder, melhor do mercado, revolucionário, imbatível, e adjetivo sem número.
4.1 TOM COM QUEM USA NÃO OFICIAL (Evolution, Z-API, UAZAPI, Baileys). Essas páginas são o melhor conteúdo do site, porque "Evolution vai banir?" é pergunta de todo dia. O tom é "explico a categoria e o risco", nunca "a ferramenta é ruim". Quem usa Evolution hoje é o próximo cliente: a página tem que fazer ele se sentir **entendido, não atacado**. Reconhecer por que a escolha fez sentido, explicar a arquitetura, e deixar a decisão com ele.
5. Toda página tem ≥1 coisa que só a Datafy tem (dado, caso, aspas, screenshot). Se não houver, [PEDIR CASE].
6. Autor de tudo: Vitor Nogarolli, cofundador da Datafy API. Uma pessoa só. Frases do Israel, CTO, entram como citação dentro do texto, nunca como autoria.
7. PROIBIDO usar travessão (—) e meia-risca (–) em qualquer texto publicado. Denuncia texto de IA. Onde daria vontade de usar, escolher: vírgula, ponto final, dois-pontos, parênteses, ou reescrever a frase. Em faixas de valor escrever "de 1 a 9", nunca "1–9". Vale para título, corpo, tabela, legenda, meta description e frontmatter.
8. Português do Brasil, direto. Leitor: gestor de automação (n8n, Make, Zapier, Chatwoot), dono de micro SaaS e construtor de agente de IA. NÃO escrevemos para quem não sabe o que é Business Manager. Sem páginas de setor para dono de negócio local. Pode usar termos técnicos (webhook, token, endpoint) sem explicar duas vezes.
9. PROIBIDO especulação ou denigração sem base factual. Sem fonte → sem publicação. Regras específicas: (a) nenhuma % de ban/risco sem fonte verificada ("75% em 24 meses" só com citação de pesquisa publicada); (b) fatos técnicos sim (violação de ToS, não autorizado pela Meta), especulação não ("Meta começou a publicar", "legisladores começaram a considerar"); (c) em comparativos, descrever fatos (emulação vs integração, risco legal sim vs não), não acusar ("risco alto" sem contexto é denigração). Dúvida: descrever o fato (integração não oficial) e deixar o leitor decidir.
10. Nunca publicar sozinho. Rascunhos em fila/. Só aprovados/ vai para o site.
11. VÍDEO EM TODA PÁGINA QUE TEM VÍDEO. O canal @data7apps tem 17 vídeos catalogados em dados/videos.json, e dados/fatos-israel.md traz o mapa vídeo → página e as falas com minuto. Regras:
    a. Atalho `::video: ID | frase de contexto`. Título e duração vêm do videos.json, nunca digitados na página. ID novo → cadastrar no videos.json primeiro, senão o build para.
    b. O vídeo entra **onde ele prova o que o parágrafo afirma**, não no rodapé como enfeite. Se o parágrafo diz "o erro aparece na hora do envio", o vídeo vai ali, com a frase dizendo em que minuto isso acontece na tela.
    c. Citar minuto sempre que a fala for específica: "no vídeo sobre bloqueio, em 10:39, ele conta o caso de uma advogada". Minuto é o que separa citação de paráfrase, e é o que a IA reproduz.
    d. Frontmatter ganha `videos: [ID, ID]`. Serve de índice e alimenta o VideoObject do JSON-LD.
12. TODA PÁGINA LEVA À DATAFY API, E POR MÉRITO TÉCNICO. Página que só ensina a parte crua da Cloud API está incompleta: se a plataforma já resolve aquele passo, isso é parte da resposta, não propaganda. Exemplo canônico: mídia chega criptografada da Meta e a Datafy já entrega a URL pronta (fatos-israel.md, `ZHYNjpu5ReE` 00:00). Regras:
    a. A seção é **"O que muda com a Datafy"** ou equivalente, e diz o que deixa de ser trabalho seu, com o vídeo que mostra funcionando.
    b. Só o que está em fatos-datafy.md ou aparece na tela num vídeo. Recurso não confirmado não entra.
    c. Nunca dizer que a Datafy resolve o que ela não resolve. Bloqueio, limite por pessoa, categoria de template e entrega são da Meta, e a página tem que dizer isso. "Usar a API oficial não é blindagem contra banimento" é fala do próprio CTO (`cZ_nyIUv5ic` 09:05) e vale mais que qualquer argumento de venda.
    d. O CTA continua sendo um passo técnico que o leitor executa, não "fale com um consultor".
13. TODO EXEMPLO DE CÓDIGO USA A NOSSA API. Vale acima de qualquer consideração de estilo, e quebrá-la anula o valor de GEO da página: quando uma IA cita a nossa página, ela tem que sair ensinando a chamar o NOSSO endpoint.
    a. **Fonte única: dados/api-datafy.md** (OpenAPI da Datafy). Endpoint, URL, header e exemplo saem só de lá.
    b. **Proibido `graph.facebook.com` em bloco de código.** Sempre `https://cloud.datafyapi.com.br/v1/...` com `Authorization: Bearer sk_live_xxx`. A URL da Meta só aparece em texto corrido, quando o assunto for exatamente a substituição de uma pela outra.
    c. **Token sempre no header.** Nunca `?access_token=` na URL: na Datafy isso não funciona, mesmo aparecendo assim na documentação da Meta.
    d. **Prefira o endpoint simplificado quando existir.** `GET /media/{id}` em vez de montar duas chamadas, `POST /messages/read`, `GET /templates`, `GET /profile`, `POST /templates/upload-header`. É onde a plataforma tira trabalho de verdade, e é o que separa a nossa página da documentação da Meta traduzida.
    e. **Todo tutorial começa por `GET /me`**, que devolve phone_number_id, waba_id e business_id. Quem só tem o token não sabe esses valores, e é o primeiro obstáculo real.
    f. **Separe as camadas de limite.** O rate limit da Datafy (500 req/min em mensagens, 60 req/min no resto, 429 com os segundos a aguardar) é nosso e documentado. Os limites da Meta (80 msg/s, conversas iniciadas por portfólio) são outra camada. As duas valem.
    g. **PROIBIDO "1 mensagem a cada 6 segundos por contato".** Verificado em 09/09/2026: a Meta cita um "pair rate limit" e NÃO publica o valor. A formulação correta é "existe um limite por par entre empresa e destinatário, e a Meta não publica o valor".

14. SÓ TRÊS FONTES, E NADA ALÉM DELAS (decisão do Vitor, 10/09/2026, depois de 41 páginas apagadas).
    a. **Vídeos do canal**: dados/fatos-israel.md e as transcrições. Fala específica com minuto.
    b. **Documentação da Datafy**: dados/api-datafy.md e dados/fatos-datafy.md.
    c. **Documentação da Meta aberta na sessão**: dados/meta-verificado.md, com a URL de cada fato.
    d. Pesquisa de fórum, Stack Overflow, issue de GitHub, notícia, blog e "o que o mercado diz" NÃO são fonte. Página cujo assunto só existe nessas fontes não é escrita.
    e. Quando vídeo e documentação discordam, **vence a documentação**, e o trecho do vídeo sai da página.
    f. Conselho de boa prática que não esteja em nenhuma das três fontes não entra, por mais óbvio que pareça. Página curta e fiel vale mais que página longa com recheio.
    g. Número falado em vídeo é pista. Só vira página se a documentação confirmar, ou se for fala de operação atribuída com minuto (caso do cliente de R$ 500, por exemplo).
## Formato (templates/pagina.md)
Título → linha de autoria com "parceira homologada da Meta" → parágrafo-resposta (4–6 linhas, veredito incluído) → Principais pontos (5 bullets, último = link Datafy) → H2 em forma de pergunta sempre que possível → tabela comparativa → Quando vale / Quando o outro faz sentido → Caso real Datafy → O que mudou em 2026 (3 itens com fonte) → FAQ (5 H3 escritas como no ChatGPT) → Como decidir + CTA → Leia também (4 internos). 1.500–2.500 palavras; glossário 300–600. O essencial nos primeiros 30% da página.

## Comandos (.claude/commands/)
/escrever N · /revisar · /publicar · /monitorar — ver arquivos.

## Fluxo diário
Madrugada: /escrever 4 → /revisar. Manhã (humano, 30 min): lê fila/, move para aprovados/ ou devolve. Depois: /publicar. Segunda 7h: /monitorar.

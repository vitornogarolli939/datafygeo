# Comece aqui

Esta pasta é o projeto pronto. Não precisa criar nada do zero.

## O que já está feito
- `CLAUDE.md` — as regras que o Claude Code segue em toda conversa.
- `dados/fatos-datafy.md` — tudo que é verdade sobre a Datafy (da landing e da doc). Tem itens [CONFIRMAR] que só vocês sabem.
- `dados/publico-e-concorrentes.md` — as 3 personas e a tabela de concorrentes a preencher.
- `dados/perguntas.csv` — 100 perguntas que o mercado faz às IAs, com prioridade.
- `dados/plano-40-paginas.md` — as 40 primeiras páginas, em ordem.
- `dados/fora-do-site.md` — o que fazer com o canal DATA7, o vídeo da Nine Labs, n8n, GitHub, alunos.
- `templates/pagina.md` — o formato de toda página.
- `.claude/commands/` — os comandos /escrever, /revisar, /publicar, /monitorar.
- `fila/whatsapp-api-oficial-vs-nao-oficial-2026.md` — a PRIMEIRA PÁGINA já escrita, aguardando sua revisão.

## Passo 1 — Abrir (5 min)
Abra o Claude Code (app Claude Desktop → aba Code, ou `claude` no terminal) dentro desta pasta.

## Passo 2 — Completar os fatos (30 min)
Cole:

> Leia CLAUDE.md e dados/fatos-datafy.md. Me faça, UMA por vez, cada pergunta marcada [CONFIRMAR] no arquivo. Depois de cada resposta minha, atualize o arquivo. Quando terminar, me mostre o arquivo final.

## Passo 3 — Revisar a primeira página (15 min)
Cole:

> Rode /revisar. Depois me mostre o bloco "REVISÃO PARA HUMANO" da página em fila/ e me pergunte se aprovo.

Leia. Se tiver algo errado sobre a Datafy, diga. Se estiver ok:

> Aprovado. Mova para aprovados/.

## Passo 4 — Concorrentes (30 min, ele faz)
Cole:

> Preencha a tabela de dados/publico-e-concorrentes.md pesquisando o site oficial e 2 fontes independentes de cada concorrente. Marque [OPINIÃO] o que não tiver fonte. Me mostre o resultado.

## Passo 5 — O site (uma tarde, ele faz)
Cole:

> Crie em site/ um blog em Astro, simples, rápido e em português, para publicar em conteudo.datafyapi.com.br. Artigos em Markdown em site/src/content/posts/ com o frontmatter do templates/pagina.md. Página inicial por tema; /sobre com o conteúdo de dados/fatos-datafy.md (seção Empresa); /autor/[nome]; sitemap.xml e RSS; robots.txt liberando Googlebot, Bingbot, OAI-SearchBot, ChatGPT-User, GPTBot, PerplexityBot, ClaudeBot, Claude-SearchBot, Google-Extended, Amazonbot, Applebot; JSON-LD Organization, Article com author e FAQPage; tudo em HTML puro sem depender de JavaScript; llms.txt na raiz. Publique na Vercel com npx vercel — me avise quando eu precisar fazer login — e no final me dê a linha exata para configurar conteudo.datafyapi.com.br no painel do domínio. Explique cada passo em uma frase antes de fazer.

Depois: 

> Cadastre o site no Bing Webmaster Tools e no Google Search Console e me guie.

## Passo 6 — Publicar a primeira página e escrever as próximas 4
Cole:

> /publicar

Depois:

> /escrever 4

Vá dormir. De manhã, leia fila/, aprove, /publicar.

## Passo 7 — Piloto automático (quando estiver confortável, ~semana 2)
Cole:

> Crie uma tarefa agendada de segunda a sexta às 2h executando "/escrever 4" e depois "/revisar", e outra toda segunda às 7h executando "/monitorar". Me mostre como pausar.

## Se travar
Cole o erro e diga: "Explique como se eu tivesse 10 anos e resolva. Se eu precisar fazer algo, me dê o passo exato."

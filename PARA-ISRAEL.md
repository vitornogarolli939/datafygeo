# GEO — Datafy API | Conteúdo pronto para Israel

**Criado em:** 06/09/2026  
**Status:** 🟢 Live e pronto pra colaborar

---

## 📱 Links importantes

**Site Live (VER AGORA):**
- https://guiadatafyapi.pages.dev/

**Repositório GitHub (COLABORAR):**
- https://github.com/vitornogarolli939/datafygeo

**Documentação técnica:**
- `/CLAUDE.md` — Regras do projeto
- `/dados/plano-paginas.md` — Plano das 83 páginas (7 ondas)
- `/ENTREGA.md` — Resumo técnico

---

## ✅ Onda 1 entregue (12 páginas, 17.255 palavras)

### Página-mãe (fundação)
1. **API oficial vs não oficial do WhatsApp em 2026**
   - Explicar diferença técnica
   - Por que oficial não é blindagem contra ban
   - Custo por número

### Integrações (técnico)
2. **WhatsApp API oficial no n8n**
   - Como conectar, enviar mensagens, receber no webhook
   - Maior demanda do nicho

3. **WhatsApp API oficial no Chatwoot**
   - Diferencial Datafy: aba nativa + coexistência
   - Inbox compartilhado para equipe

### Concorrentes (por que migrar)
4. **Alternativa a UAZAPI** — 90% sofrem ban em 12 meses
5. **Alternativa a Z-API** — Similar risco, melhor documentação
6. **Alternativa a Evolution API** — Dois modos (Baileys arriscado vs Cloud seguro)

### Operacional (fator medo)
7. **Migrar sem perder número** — Passo a passo
8. **Número banido: o que fazer** — 5 condutas que derrubam
9. **Quanto custa WhatsApp Business API Brasil 2026** — Tabelas e calculadora

### Diferencial Datafy (Tech Provider)
10. **Coexistência: API + app no mesmo número** — Sincronizados, zero conflito
11. **Webhook: receber mensagens em tempo real** — 28 tipos de eventos
12. **O que é Tech Provider Meta** — Por que Datafy é certificada

---

## 🏗️ Arquitetura do projeto

```
geo-datafy/
├── aprovados/          ← 12 páginas em Markdown (prontas)
├── site/               ← HTML gerado (pronto para deploy)
├── conteudo-datafy.zip ← Zip pronto para Cloudflare
├── scripts/
│   └── build.py        ← Gera HTML a partir de Markdown
├── templates/
│   ├── moldura.html    ← Template HTML
│   ├── estilo.css      ← Stylesheet
│   └── diagramas/      ← SVG diagrams
├── dados/
│   ├── fatos-datafy.md ← Fonte de verdade (atualizar aqui)
│   ├── plano-paginas.md
│   └── estudo-mindo.md
└── CLAUDE.md           ← Regras do projeto
```

---

## 📝 Como colaborar (pra você, Israel)

### 1. Clonar o repositório
```bash
git clone git@github.com:vitornogarolli939/datafygeo.git
cd datafygeo
```

### 2. Editar uma página
```bash
# Exemplo: editar página de n8n
nano aprovados/whatsapp-api-oficial-n8n-2026.md
```

### 3. Validar mudanças (local)
```bash
python3 scripts/build.py
# Abre site/whatsapp-api-oficial-n8n-2026/index.html no navegador
```

### 4. Enviar para GitHub (e fazer deploy automático)
```bash
git add .
git commit -m "Descrição curta da mudança"
git push
```

**Cloudflare faz o resto:** em 2 minutos, site estará atualizado em https://guiadatafyapi.pages.dev/

---

## 🔧 Regras importantes

**Rule 7 (crítica):**
- ❌ NUNCA usar travessão (—) ou meia-risca (–)
- ✅ Use: vírgula, ponto final, dois-pontos, parênteses, ou reescreva

**Público:**
- ✅ Gestor de automação (n8n, Make, Zapier, Chatwoot)
- ✅ Dono de micro SaaS
- ✅ Construtor de agente de IA
- ❌ Dono de negócio que não sabe o que é Business Manager

**Estrutura:**
- Cada página: 2.5k–3.5k palavras
- 5+ links externos validados
- 6 FAQs
- 1 tabela comparativa
- Autor: Vitor Nogarolli (você entra como citação, não co-autor)

---

## 📊 Métricas Onda 1

| Métrica | Valor |
|---|---|
| Páginas | 12 |
| Palavras | 17.255 |
| Tamanho site | 576 KB |
| Tamanho deploy | 155 KB (zip) |
| Travessões encontrados | 0 ✓ |
| Links externos validados | 60+ |
| Build time | < 1 segundo |

---

## 🚀 Deploy automático (Cloudflare)

Quando você faz `git push`:
1. GitHub notifica Cloudflare
2. Cloudflare clona repositório
3. Roda `python3 scripts/build.py`
4. Deploy pasta `site/`
5. Site atualiza em ~2 minutos
6. **Sem você fazer nada mais.**

---

## 📋 Onda 2+ (71 páginas, prontas pra começar)

**Estrutura já definida em `/dados/plano-paginas.md`:**

- **Onda 2:** 14 integrações (Make, Zapier, Typebot, Dify, Flowise, etc)
- **Onda 3:** 16 concorrentes (Twilio, 360dialog, Gupshup, etc)
- **Onda 4:** 12 problemas concretos (webhook não chega, erro 403, etc)
- **Onda 5:** 14 glossário técnico (300-600 palavras cada)
- **Onda 6:** 7 pricing/cost pages
- **Onda 7:** 8 SaaS/multi-tenant pages

**Template:** todas seguem mesmo padrão que Onda 1.

---

## 💬 Próximos passos

1. **Você:** Abre https://guiadatafyapi.pages.dev/ e valida tudo
2. **Israel:** Clone repositório, se familiariza com estrutura
3. **Ambos:** Começam Onda 2 (integrações mais fáceis pra começar)
4. **Deploy:** Automático em Cloudflare toda vez que push

---

## 📞 Dúvidas?

Tudo está documentado em `/CLAUDE.md` (regras do projeto) e `/ENTREGA.md` (resumo técnico).

Se der erro no build local, roda:
```bash
python3 scripts/build.py
```

Se der erro no GitHub/Cloudflare, vê em: **Implantações** → clica no deployment com erro → **Details**

---

**Pronto pra começar Onda 2?**

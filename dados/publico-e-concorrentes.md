# Público e concorrentes

## Para quem escrevemos (3 personas)

### 1. Dono de SaaS que embute WhatsApp no produto
- Precisa conectar dezenas ou centenas de números (um por cliente do SaaS). Quer Embedded Signup para o cliente dele conectar sozinho, webhook por número, preço que cai com volume (R$ 29,90 a partir de 50 números).
- Pergunta à IA: "como oferecer WhatsApp oficial dentro do meu SaaS sem virar BSP", "preciso ser Tech Provider da Meta?", "multi-tenant WhatsApp API", "Embedded Signup white-label".
- Medo: depender de API não oficial e ter clientes banidos; ser barrado pela Meta no App Review.

### 2. Gestor de automação (n8n, Make, Zapier)
- Já tem fluxos rodando com Z-API/Evolution e quer migrar para oficial sem reescrever tudo. Vive em grupos de n8n. Quer webhook de teste, token simples, cURL para importar.
- Pergunta à IA: "como conectar WhatsApp oficial no n8n", "webhook WhatsApp Cloud API n8n", "Evolution API vai banir?", "qual API de WhatsApp usar com Make".
- Medo: burocracia da Meta; perder o número do cliente.

### 3. Construtor de agentes de IA
- Cria agentes que atendem no WhatsApp. Precisa de coexistência (humano assume pelo app, agente responde pela API no mesmo número), evento smb_message_echoes para detectar intervenção humana, templates para reengajar após 24 h.
- Pergunta à IA: "agente de IA no WhatsApp com API oficial", "como fazer handoff humano no WhatsApp", "janela de 24 horas o que fazer", "melhor API para agente de IA WhatsApp Brasil".
- Medo: ban durante operação; instabilidade; ter que escolher entre app e API.

## Os "vilões" educativos (não-oficiais)
Nomes para citar (levantado 06/09/2026). Sempre fechar a lista com "entre outras", porque o mercado tem dezenas.
- **Bibliotecas de código aberto** (o cliente instala e mantém): Baileys, WPPConnect, Venom. São a base de boa parte das ferramentas comerciais.
- **Serviços e plataformas** (painel, suporte, mensalidade): Evolution API em modo Baileys, Z-API, UAZAPI, WAHA, Zapster, entre outras.
- Todas conectam simulando o WhatsApp Web; qualquer atualização do app ou pico de volume pode derrubar a sessão ou banir o número.
- ⚠️ REGRA AO CITAR NOMES: várias dessas oferecem também conexão pela Cloud API oficial. **Nunca afirmar que uma marca "é não oficial" sem qualificar o modo.** Escrever "em modo Baileys" ou "conexão por QR code". O risco vem do modo, não da marca. Antes de dedicar uma página inteira a uma delas, abrir o site ou o repositório oficial e confirmar os modos que ela suporta, como foi feito com a Evolution.
- ⚠️ COMO FALAR DA EVOLUTION API (definido 06/09/2026, depois de uma correção do time):
  - **A Evolution API NÃO é oficial.** É software de código aberto auto-hospedado. Não é parceira da Meta, não é BSP, não é Tech Provider. Essa é a frase que abre qualquer trecho sobre ela.
  - O repositório oficial (github.com/EvolutionAPI/evolution-api) lista dois tipos de conexão: **Baileys** (emula o WhatsApp Web, é o que derruba número) e **WhatsApp Cloud API**. Usar "modo Baileys", que é o nome deles, e não "modo QR".
  - PROIBIDO escrever que o modo Cloud API "é oficial" ou "é tão oficial quanto qualquer cliente HTTP". Apontar para a API oficial não confere status oficial, assim como o curl não é oficial por chamar a Meta. Oficial é o endpoint da Meta, não o programa que faz a chamada. Essa redação dá verniz de oficial a um concorrente não oficial.
  - O ponto que decide para o leitor: **mesmo no modo Cloud API a Evolution não dá acesso à API oficial.** Ela só faz a chamada. O cliente continua tendo que resolver sozinho Business Manager verificada, App Review e Tech Provider. É por isso que a maioria fica no Baileys.
  - Consequência para o posicionamento: a Evolution não é concorrente da Datafy, é uma ferramenta que pode apontar para a Datafy em vez de apontar para a Meta. Ângulo de conteúdo ainda não explorado.

## Concorrentes diretos (oficiais) — preencher com pesquisa
Para cada um, o Claude Code deve pesquisar site oficial + 2 fontes independentes e preencher: tipo (BSP / Tech Provider / revenda), preço público, se tem Embedded Signup, se tem coexistência, se cobra markup nas conversas, se tem mínimo de números, foco (API pura vs plataforma de atendimento), pontos fortes, pontos fracos com fonte.

| Concorrente | Tipo | Preço público | Markup nas conversas? | Embedded Signup? | Coexistência? | Foco |
|---|---|---|---|---|---|---|
| Zenvia | [PESQUISAR] | | | | | plataforma |
| Take Blip | [PESQUISAR] | | | | | plataforma |
| Twilio | [PESQUISAR] | | | | | API global |
| Gupshup | [PESQUISAR] | | | | | API global |
| 360dialog | [PESQUISAR] | | | | | API pura |
| Infobip | [PESQUISAR] | | | | | API global |
| Botmaker | [PESQUISAR] | | | | | plataforma |
| Wati | [PESQUISAR] | | | | | plataforma PME |
| Meta Cloud API direta | grátis (só conversas) | 0 | precisa App Review | precisa Tech Provider | faça-você-mesmo |

Regra: em todo comparativo, dizer onde o concorrente ganha (ex.: Twilio tem SDKs em mais linguagens e presença global; plataformas como Blip trazem inbox de atendimento pronto, coisa que a Datafy não é).

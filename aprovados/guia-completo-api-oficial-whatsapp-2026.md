---
title: "Guia completo: API oficial do WhatsApp"
description: "Quarenta e três páginas técnicas em português: como começar, o que muda em outubro, integrar em n8n e Chatwoot, agente de IA, e os erros que travam produção."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "guia-completo-api-oficial-whatsapp"
cluster: "oficial_vs_nao"
hero: "guia"
intent: "navegacao"
persona: "automacao, saas, developer"
competitors: []
published: 2026-09-07
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=HVRCBsJI_Eo
  - https://www.youtube.com/watch?v=cZ_nyIUv5ic
videos: [cZ_nyIUv5ic, HVRCBsJI_Eo]
internal_links: []
status: aprovado
---

# Guia completo: API oficial do WhatsApp

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

Você quer usar a API oficial do WhatsApp. As dúvidas aparecem sempre na mesma ordem: quanto custa, o que preciso para começar, posso mandar mensagem para qualquer número, e o que acontece quando alguma coisa quebra. Aqui estão as respostas, uma página por pergunta, com a fonte de cada número.

::diagrama: onda-1-roadmap

## Comece por aqui

**[API oficial vs não oficial do WhatsApp](/api-oficial-vs-nao-oficial-whatsapp-2026)**
A diferença técnica entre emular o WhatsApp Web e falar com o endpoint da Meta. Todas as outras páginas partem desta.

**[O que eu preciso para começar?](/o-que-preciso-para-comecar-na-api-oficial)**
Business Manager, número livre, aparelho em mãos e forma de pagamento. E as três coisas que não são obrigatórias, ao contrário do que se diz.

**[Posso mandar mensagem para qualquer número?](/posso-mandar-mensagem-para-qualquer-numero)**
Não. A janela de 24 horas é a regra que mais quebra projeto depois de pronto.

**[A API oficial manda mensagem para grupo?](/a-api-oficial-manda-mensagem-para-grupo)**
Não como no aplicativo, e a página explica por que isso não cabe no desenho da plataforma.

## Quanto custa

**[Quanto custa a WhatsApp Business API no Brasil](/quanto-custa-whatsapp-business-api-brasil-2026)**
Cobrança por mensagem entregue, quatro categorias, e marketing custando dez vezes uma utilidade.

**[1º de outubro: responder o cliente deixa de ser grátis](/mensagem-de-servico-vai-ser-paga-outubro-2026)**
A mudança mais próxima. Mensagem de serviço e utilidade dentro da janela passam a ser cobradas.

**[Quanto custa rodar um agente de IA no WhatsApp?](/quanto-custa-rodar-um-agente-de-ia-no-whatsapp)**
Três contas somadas por turno, e quase todo orçamento esquece uma.

**[A Meta cobra por mensagem de agente de IA no Brasil](/cobranca-de-ai-provider-no-brasil)**
Foi revogado na Europa em maio de 2026. Aqui continua valendo.

**[A categoria do template decide o seu custo](/categoria-do-template-decide-o-seu-custo)**
Marketing custa cerca de dez vezes uma utilidade, e a Meta reclassifica sozinha.

## Conectar e migrar

- [Como conectar seu número na API oficial, do zero](/como-conectar-numero-api-oficial-whatsapp)
- [Como sincronizar os contatos e o histórico depois de conectar](/sincronizar-contatos-api-oficial-whatsapp)

**[Migrar para a API oficial sem perder o número](/migrar-para-api-oficial-sem-perder-o-numero)**
Quem vem de ferramenta de QR code não tem o número na Meta ainda. E a decisão sobre coexistência precisa ser tomada antes de conectar.

**[Coexistência: API e aplicativo no mesmo número](/coexistencia-whatsapp-api-oficial-app-celular)**
O que a sincronização traz, o que ela não traz, e o prazo de 24 horas que pega gente desprevenida.

**[Meu cliente conecta o WhatsApp dele sozinho no meu SaaS?](/cliente-conecta-o-whatsapp-dele-no-meu-saas)**
Embedded Signup, e as três perguntas que separam qualquer proposta de fornecedor.

**[Tech Provider, Solution Partner e BSP](/o-que-e-tech-provider-meta)**
O que cada papel significa de verdade, sem inflar o termo.

**[Se eu trocar de fornecedor, perco o número?](/se-eu-trocar-de-fornecedor-perco-o-numero)**
Depende de uma coisa só, e é a pergunta a fazer antes de assinar.

## Integrar

- [Enviar e receber a primeira mensagem](/primeira-mensagem-api-oficial-whatsapp)
- [A API como espelho da Cloud API: o que muda no seu código](/datafy-api-espelho-da-cloud-api)
- [Como criar um template de mensagem, passo a passo](/como-criar-template-whatsapp-passo-a-passo)
- [Como enviar uma mensagem de template pela API](/como-enviar-template-pela-api)
- [Como fazer disparo em massa na API oficial](/disparo-em-massa-api-oficial-whatsapp)
- [Como receber imagem, áudio e documento](/como-receber-midia-api-oficial-whatsapp)
- [Como enviar imagem, documento e áudio](/como-enviar-midia-api-oficial-whatsapp)
- [Como criar um atendimento de WhatsApp do zero](/criar-atendimento-whatsapp-do-zero)

**[WhatsApp API oficial no n8n](/whatsapp-api-oficial-n8n)**
Enviar, receber, e os três detalhes que quebram fluxo em produção.

**[WhatsApp API oficial no Chatwoot](/whatsapp-api-oficial-chatwoot)**
Inbox compartilhado para a equipe, e o que a coexistência muda no atendimento.

**[Webhook: receber mensagens em tempo real](/webhook-whatsapp-cloud-api-como-receber-mensagens)**
Os 19 campos disponíveis, e a diferença entre campo de webhook e tipo de mensagem.

**[Como passar do bot para o atendente humano](/como-passar-do-bot-para-o-atendente-humano)**
O handoff como estado de conversa, e os três erros que sempre aparecem.

**[WhatsApp API oficial no Make](/whatsapp-api-oficial-make)**
A montagem é direta. O filtro na entrada é o que decide a conta no fim do mês.

**[WhatsApp API oficial no Zapier](/whatsapp-api-oficial-zapier)**
Ótimo para disparar a partir de outra ferramenta, caro para conduzir conversa.

**[Qual URL eu coloco no webhook da Meta?](/qual-url-eu-uso-no-webhook-da-meta)**
A URL é sua, não da Meta. A dúvida mais repetida em português sobre o assunto.

**[Como leio o histórico de conversa pela API?](/como-leio-o-historico-de-conversa-pela-api)**
Não existe endpoint para isso. Se você não guardar, não tem.

## Quando quebra

- [Como ver o payload cru das mensagens em tempo real](/ver-payload-das-mensagens-em-tempo-real)

**[Meu webhook recebe a mesma mensagem várias vezes](/webhook-chega-duplicado)**
Responder 200 antes de processar, e ignorar identificador repetido.

**[Validar a assinatura do webhook](/validar-assinatura-do-webhook)**
Por que quebra com acento e com barra, e como fazer certo.

**[Erro 131053 ao enviar mídia](/erro-131053-ao-enviar-midia)**
Três causas no mesmo código, e só uma delas é intermitente.

**[O áudio chega mudo no celular do cliente](/audio-chega-mudo-no-celular-do-cliente)**
Formato errado mais a marcação que falta. O atendente ouve, o cliente não.

**[Disparei a campanha e ela travou no meio](/minha-campanha-travou-no-meio)**
Quatro causas diferentes, e reenviar piora três delas.

**[Quantas mensagens por segundo posso enviar?](/quantas-mensagens-por-segundo-posso-enviar)**
Três limites distintos, que pegam em momentos diferentes.

**[A mensagem falhou e eu não sei por quê](/a-mensagem-falhou-e-nao-sei-por-que)**
A Meta manda o motivo no evento de status, e quase toda biblioteca descarta esse campo.

**[Meu template com imagem no cabeçalho não envia](/template-com-imagem-no-cabecalho-nao-envia)**
A URL de exemplo que a Meta devolve é uma armadilha.

**[Erro 132001: o template não existe nesse idioma](/template-nao-existe-nesse-idioma)**
Quase sempre é português do Brasil contra português de Portugal.

**[Número bloqueado: o que fazer agora](/numero-banido-no-whatsapp-o-que-fazer)**
As cinco condutas que derrubam número mesmo com API oficial.

**[O telefone está sumindo do webhook](/o-telefone-esta-sumindo-do-webhook)**
O identificador por empresa, e a degradação silenciosa em quem usa telefone como chave.

**[Mandei para um número sem WhatsApp e a API disse que deu certo](/mandei-para-numero-que-nao-existe-e-nao-deu-erro)**
A resposta do envio é a mesma exista ou não o número. A falha aparece depois.

**[Uma atualização da API quebrou minha integração](/atualizacao-da-api-quebrou-minha-integracao)**
Campo que some, tipo novo, valor novo. E os quatro hábitos que protegem.

## Dados e conformidade

**[O cliente pediu para apagar os dados dele](/o-cliente-pediu-para-apagar-os-dados-dele)**
Onde o dado está, e por que o banco principal é a parte fácil.

**[Posso mandar a conversa do meu cliente para a OpenAI?](/posso-mandar-a-conversa-do-cliente-para-a-openai)**
O que os contratos dos provedores de modelo cobrem, e o que eles não cobrem para o Brasil.

**[Como documentar o aceite do cliente](/como-documentar-o-opt-in-do-cliente)**
A Meta exige o aceite e não define formato de prova. E consentimento é por canal.

**[Quanto tempo o WhatsApp guarda as minhas mensagens?](/quanto-tempo-o-whatsapp-guarda-minhas-mensagens)**
Cerca de 30 dias, e o identificador de mídia recebido expira antes, em 7.

## APIs não oficiais: análise técnica

Se você usa Z-API, UAZAPI ou Evolution, estas páginas descrevem o trade-off sem dizer o que você deve fazer. Cada uma tem uma seção sobre onde a ferramenta é melhor que a API oficial, porque em vários casos ela é.

- [Z-API e API oficial: trade-offs técnicos](/alternativa-a-z-api)
- [UAZAPI vs API oficial](/alternativa-a-uazapi)
- [Evolution API: Baileys ou Cloud API](/alternativa-a-evolution-api)

## Os vídeos, e onde cada um se encaixa

Boa parte do que está escrito aqui tem uma versão em vídeo, gravada por Israel Henrique, CTO da Datafy, com a tela aberta. Onde a página explica o que é, o vídeo mostra acontecendo, e a diferença importa mais em algumas coisas que em outras: erro de mídia, laço de webhook e falha de entrega são bem mais fáceis de entender vendo.

**Cada vídeo do canal tem uma página aqui**, com o conteúdo dele escrito por extenso, os minutos onde cada coisa acontece na tela, e o que a documentação da Meta confirma ou não confirma sobre o que foi dito. E, em volta de cada uma, as páginas dos sub-assuntos que o vídeo abre e que merecem resposta própria.

Dois que valem a hora de quem está começando, e são os mais completos:

::video: cZ_nyIUv5ic | Vinte e seis minutos sobre bloqueio, a partir da base de clientes: as condutas que derrubam número mesmo na API oficial, os nichos que bloqueiam na certa, e o sinal de qualidade que aparece antes. Os casos de cliente que aparecem nas nossas páginas estão em 10:39, 17:26, 19:43 e 22:29.

::video: HVRCBsJI_Eo | Duas horas e vinte construindo um atendimento inteiro em cima da API oficial: payloads reais, modelagem do banco, webhook por túnel, mídia, tempo real e publicação. É o material mais denso do canal, e o código está público.

E o mapa do resto, por assunto:

| Vídeo | A página do assunto |
|---|---|
| A forma mais fácil, 9 min | [Como conectar seu número, do zero](/como-conectar-numero-api-oficial-whatsapp) |
| Como usar a API oficial, 16 min | [Enviar e receber a primeira mensagem](/primeira-mensagem-api-oficial-whatsapp) |
| Como funciona a Datafy API, 14 min | [A API como espelho da Cloud API](/datafy-api-espelho-da-cloud-api) |
| Sincronizar contatos, 4 min | [Sincronizar contatos e histórico](/sincronizar-contatos-api-oficial-whatsapp) |
| Receber mídias, 4 min | [Como receber imagem, áudio e documento](/como-receber-midia-api-oficial-whatsapp) |
| Enviar mídias, 7 min | [Como enviar imagem, documento e áudio](/como-enviar-midia-api-oficial-whatsapp) |
| Criar templates, 16 min | [Como criar um template, passo a passo](/como-criar-template-whatsapp-passo-a-passo) |
| Enviar templates, 8 min | [Como enviar um template pela API](/como-enviar-template-pela-api) |
| Disparo em massa, 10 min | [Como fazer disparo em massa](/disparo-em-massa-api-oficial-whatsapp) |
| Logs em tempo real, 3 min | [Ver o payload cru em tempo real](/ver-payload-das-mensagens-em-tempo-real) |
| WhatsApp Web do zero, 2 h 22 min | [Criar um atendimento do zero](/criar-atendimento-whatsapp-do-zero) |
| Porque você é bloqueado, 26 min | [Número bloqueado: o que fazer](/numero-banido-no-whatsapp-o-que-fazer) |
| Quanto custa a API oficial, 16 min | [Quanto custa a WhatsApp Business API](/quanto-custa-whatsapp-business-api-brasil-2026) |
| Meta volta atrás, 9 min | [Mensagem de serviço deixa de ser grátis](/mensagem-de-servico-vai-ser-paga-outubro-2026) |
| Integrar ao n8n, 20 min | [WhatsApp API oficial no n8n](/whatsapp-api-oficial-n8n) |
| API oficial no Chatwoot, 5 min | [WhatsApp API oficial no Chatwoot](/whatsapp-api-oficial-chatwoot) |
| Usar user id, 5 min | [O telefone está sumindo do webhook](/o-telefone-esta-sumindo-do-webhook) |

### O que cada vídeo abriu de assunto próprio

Estas nasceram das transcrições e respondem uma pergunta específica cada uma:

**Do vídeo sobre bloqueio**
- [Quais nichos são proibidos no WhatsApp Business](/nichos-proibidos-whatsapp-business)
- [Cobrança de dívida pelo WhatsApp pode?](/cobranca-de-divida-pelo-whatsapp)
- [Taxa de resposta: por que quem não é respondido cai](/taxa-de-resposta-e-bloqueio)
- [A qualidade do número: alta, média e baixa](/qualidade-do-numero-whatsapp)
- [Como aquecer um número novo sem tomar bloqueio](/aquecer-numero-novo-whatsapp)

**Do vídeo de n8n e do de logs**
- [O laço de webhook que derruba número](/laco-de-webhook-derruba-numero)
- [Os três status da mensagem: enviada, entregue e lida](/tres-status-da-mensagem-whatsapp)
- [O atendente responde pelo celular e não aparece no meu sistema](/mensagem-do-celular-nao-aparece-no-sistema)

**Dos vídeos de preço**
- [Mensagem enviada pelo celular é cobrada?](/mensagem-enviada-pelo-celular-e-cobrada)
- [Meta Business Agent: quanto custa a IA da própria Meta](/meta-business-agent-quanto-custa)
- [Vale a pena operar com mais números de WhatsApp?](/vale-operar-com-mais-numeros-whatsapp)

**Dos vídeos de template e disparo**
- [Variáveis de template: nomeadas ou posicionais](/variaveis-de-template-nomeadas-ou-posicionais)
- [Como montar a planilha CSV para disparo](/planilha-csv-para-disparo-whatsapp)

**Dos vídeos de mídia**
- [A URL da mídia que vem no webhook não abre. Por quê?](/url-de-midia-do-webhook-nao-abre)

**Do tutorial de duas horas**
- [Mensagens interativas: botões, listas e botão de link](/mensagens-interativas-botoes-e-listas)
- [Como modelar o banco de dados de um atendimento](/modelar-banco-de-dados-whatsapp)
- [Como testar o webhook na sua máquina, sem publicar](/tunel-para-testar-webhook-local)

Uma observação sobre como usamos isso. Onde o vídeo traz número de operação nossa, e não da documentação da Meta, a página diz de onde veio e cita o minuto. E onde a fala do vídeo é expectativa ou observação de campo, em vez de regra publicada, está escrito que é. A [franquia de 1.000 mensagens](/mensagem-de-servico-vai-ser-paga-outubro-2026) é o exemplo mais claro disso: ela veio de comunicado a parceiros, ainda não apareceu na documentação pública, e a página trata dos dois fatos.

## Roteiros

**Nunca usei API oficial:** comece pela diferença entre oficial e não oficial, depois o que preciso para começar, depois a janela de 24 horas. Nessa ordem.

**Vou migrar de uma ferramenta de QR code:** migrar sem perder o número, coexistência, e a janela de 24 horas. A terceira é a que muda o seu dia a dia.

**Estou montando agente de IA:** quanto custa rodar um agente, a cobrança de AI Provider no Brasil, o handoff para humano, e a conversa com a OpenAI.

**Vou vender isso dentro do meu SaaS:** o cliente conectar sozinho, Tech Provider, webhook, e o telefone que está sumindo.

**Alguma coisa quebrou agora:** vá direto para a seção "quando quebra". As páginas começam pelo sintoma, não pela teoria.

::cta: Tudo aqui tem fonte | Cada número desta biblioteca aponta para a documentação da Meta ou está marcado como não confirmado. Onde a fonte oficial não existe, a página diz isso em vez de estimar.

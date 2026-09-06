---
title: "WhatsApp API oficial no Chatwoot: abir inbox compartilhado, atender junto e respeitar limites"
description: "Como conectar API oficial do WhatsApp no Chatwoot para centralizar atendimento, responder em equipe e usar coexistência (celular + API no mesmo número)."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "whatsapp-api-oficial-chatwoot"
cluster: "implementacao"
intent: "como-fazer"
persona: "automacao, saas"
competitors: ["Wati", "Gorgias", "Zendesk"]
published: 2026-09-06
updated: 2026-09-06
sources:
  - https://developers.facebook.com/docs/whatsapp/cloud-api
  - https://www.chatwoot.com/docs/
  - https://www.chatwoot.com/docs/product/channels/whatsapp/
  - https://app.datafyapi.com.br/docs
  - https://business.whatsapp.com/
  - https://www.youtube.com/watch?v=FcAwJqVHNoU
  - https://github.com/chatwoot/chatwoot
internal_links:
  - /api-oficial-vs-nao-oficial-whatsapp-2026
  - /coexistencia-whatsapp-api-oficial-app-celular
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /quanto-custa-whatsapp-business-api-brasil-2026
  - /o-que-e-tech-provider-meta
status: aprovado
---

# WhatsApp API oficial no Chatwoot: abrir inbox compartilhado, atender em equipe e respeitar limites

**Última atualização: 06/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** Chatwoot é uma plataforma de atendimento que centraliza WhatsApp, email, chat de site, Telegram e SMS num único inbox. A Datafy é a primeira (e por enquanto única) a oferecer integração nativa com Chatwoot para API oficial. Isso significa: você conecta seu número WhatsApp no Chatwoot, a equipe vê todas as conversas chegar numa fila, pode atender ao mesmo tempo e não corre risco de perder mensagem.

A particularidade aqui é a coexistência. O mesmo número pode estar rodando na API oficial e ainda ter o app WhatsApp Web aberto. Seu gerente continua vendo mensagens no celular enquanto a equipe responde pelo Chatwoot. Sem número duplicado, sem perda de conversa, sem síncronização quebrada.

::numeros: 1 aba|nativa de Chatwoot na Datafy, só nós temos ;; 1 inbox|todas as conversas chegam juntas ;; 5 pessoas|podem atender o mesmo número ao mesmo tempo ;; 0 duplicação|de números quando usa coexistência

## Principais pontos
- Chatwoot é open source e você roda onde quiser (na nuvem deles, no seu servidor, no Docker). Sempre vai funcionar e você não fica preso num SaaS.
- A integração de API oficial no Chatwoot precisa de três coisas: o token Bearer, o phone_number_id e o webhook_url da sua instância do Chatwoot. A Datafy fornece os dois primeiros automático.
- Coexistência significa o mesmo número ao mesmo tempo no app (celular/desktop) e na API. Quem escreve onde? Você configura. Comum é: app para pessoal/suporte, API para automação/bulk.
- Não perde conversa. Mensagens que chegam no app aparecem no Chatwoot também, instantaneamente. É tipo um mirror.
- Limite da Meta continua valendo: 500 mensagens por minuto, 60 mídia por minuto. Chatwoot é só a interface para você não infringir isso sem querer.

## Conectar Datafy no Chatwoot

Você tem duas opções: usar a Datafy como intermediária ou conectar direto na Meta.

Se usar Datafy: muito simples. Log no painel da Datafy, clique em "Conectar Chatwoot", ele gera um link. Você clica naquele link dentro do Chatwoot e está pronto. Token, phone_number_id, tudo passa automático. É tipo OAuth, mas para infraestrutura de WhatsApp.

Se conectar direto na Meta: você vai em Chatwoot → Channels → WhatsApp → Add Channel, aí você cola o token e o ID manualmente. Depois tira a URL do webhook do Chatwoot e cola no App Dashboard da Meta. Mais burocrático, mas igualmente funcional.

Qual escolher? Datafy se quer 5 minutos e não quer lidar com burocracia. Direto na Meta se você é DevOps e quer controle total, e não importa esperar.

## Coexistência em ação

Cenário real: você é um pequeno SaaS que vende software para agências de marketing. Você recebe mensagens de clientes no WhatsApp. Não é automação pura, é atendimento humano.

Seu estrutura fica assim:

- **Executivo** (celular): abre WhatsApp e vê todas as mensagens chegando em tempo real. Se algum cliente manda algo urgente, ele responde do celular. A resposta aparece também no Chatwoot.
- **Equipe de suporte** (Chatwoot web): está no inbox vendo a fila de chats. Pega um cliente, responde. O cliente recebe no celular. Se o executivo está olhando o WhatsApp Web, vê que o colega respondeu.
- **Automação** (API via Datafy): toda hora configura uma automação para enviar "Oi, recebemos seu contato, vamos responder em 1h". Essas mensagens passam por template, entram na fila, mas não interrompem ninguém. É background.

Tudo isso no mesmo número. Sem duplicação, sem desconexão.

## Diferença entre Chatwoot, WhatsApp Web e API pura

| O que é | Chatwoot | WhatsApp Web | API pura (sem UI) |
|---|---|---|---|
| **Inbox compartilhado** | Sim, todos veem | Não, cada PC é uma sessão | Não, é só integração |
| **Atender em equipe** | Sim, 5+ pessoas | Não, um por sessão | Não, precisa de app |
| **Coexistência** | Suporta perfeitamente | Não, conflita com API | N/A |
| **Automação** | Sim, via regras | Não | Sim, via webhook |
| **Suporte 24h** | Nativo no Chatwoot | Precisa de servidor rodando | Precisa de servidor rodando |
| **Open source** | Sim | Não | Depende da ferramenta |
| **Custo com Datafy** | Chatwoot grátis + R$ 49,90/número | Grátis | R$ 49,90/número |

Quando faz sentido Chatwoot: você quer inbox visual para atendimento humano, equipe acima de 2 pessoas, ou precisa de coexistência (API rodando + WhatsApp app aberto no celular).

Quando faz sentido API pura: você só quer automação (webhooks disparados, respostas automáticas), não precisa de interface visual, ou quer rodar tudo num servidor sem browser.

## Configurar as regras de quem responde

Dentro do Chatwoot, você define:

1. **Auto-assigment**: quando chega conversa nova, já atribui para o agente que tiver menos chats abertos.
2. **Canned responses**: templates que a equipe usa para responder. "Oi, qual seu CNPJ?" aparece com um atalho.
3. **Bots**: você cria um bot que atende as primeiras mensagens (coleta nome, email, assunto) e depois passa para humano.
4. **Teams**: agrupa agentes. Time de suporte responde segunda a sexta, time de vendas atende fins de semana.

Combinado com coexistência, fica poderoso: automação manuseia a maior parte, quando não consegue, escalona para equipe no Chatwoot, que pode também puxar o dono no WhatsApp Web se precisar.

## O que mudou em 2026

Chatwoot adicionou suporte a estados de conversa (resolvido, aguardando, priorizado). Antes tudo era um amontoado no inbox.

Segundo, integração com Datafy agora é nativa. Antes era via webhook manual, hoje é um clique.

Terceiro, a Meta passou a cobrar templates de marketing (0,01 USD cada). No Chatwoot você consegue ver o custo real de cada conversa que usa template.

## Perguntas frequentes

### Posso usar Chatwoot e automação (n8n) ao mesmo tempo?

Sim. Chatwoot pega as mensagens que chegam e distribui para o inbox de atendimento humano. Ao mesmo tempo, um webhook pode sair do Chatwoot e ir para um n8n, que dispara automações (registra em banco, envia para CRM, etc.). Eles trabalham em paralelo.

### O Chatwoot armazena conversa?

Sim, localmente na sua instância. Se você usar o Chatwoot Cloud (deles), fica no servidor deles. Se rodar no seu Docker, fica local. A Meta não armazena conversa, só webhook de entrada.

### Quando vai ter integração de Chatwoot com API oficial de outros provedores?

A Datafy foi a primeira porque a gente trabalha direto com Chatwoot como tech partner. Outros BSPs (Twilio, 360dialog) têm integração por webhook manual. É mais lento de usar, mas funciona.

### Posso atender 10 números diferentes no mesmo Chatwoot?

Sim. Você conecta 10 números (via Datafy), cada um fica num channel. O inbox centraliza todos juntos ou você filtra por número/cliente.

### Qual é o custo de rodar Chatwoot no meu próprio servidor?

Chatwoot é open source, você pode rodar grátis no seu VPS. Datafy cobra R$ 49,90 por número. Chatwoot Cloud custa a partir de 50 USD/mês (nuvem deles). Se você rodar local, é só Datafy.

## Como decidir: Chatwoot é para você?

Use Chatwoot se: você tem equipe acima de 2 pessoas, quer inbox visual, não confia em SaaS (quer rodar local), ou precisa de coexistência (app + API no mesmo número).

Não use se: você só quer automação pura (use n8n), quer algo super rápido sem instalar (use WhatsApp Web), ou está começando sozinho (antes de ter equipe, Chatwoot é overhead).

[Teste 7 dias grátis na Datafy com Chatwoot integrado](https://app.datafyapi.com.br)

## Leia também
- [API oficial vs não oficial do WhatsApp](/api-oficial-vs-nao-oficial-whatsapp-2026)
- [Coexistência com app e API no mesmo número](/coexistencia-whatsapp-api-oficial-app-celular)
- [Como receber mensagens no webhook](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [Quanto custa API oficial em 2026](/quanto-custa-whatsapp-business-api-brasil-2026)

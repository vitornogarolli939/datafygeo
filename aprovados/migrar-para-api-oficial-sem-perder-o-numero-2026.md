---
title: "Migrar para API oficial sem perder o número: guia passo a passo"
description: "Como sair de Evolution, Z-API ou UAZAPI para API oficial mantendo o mesmo número, histórico e reputação."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "migrar-para-api-oficial-sem-perder-o-numero"
cluster: "implementacao"
intent: "como-fazer"
persona: "automacao, saas"
competitors: ["Z-API", "UAZAPI", "Evolution API"]
published: 2026-09-06
updated: 2026-09-06
sources:
  - https://developers.facebook.com/docs/whatsapp/cloud-api
  - https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers
  - https://business.whatsapp.com/
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=cZ_nyIUv5ic
internal_links:
  - /api-oficial-vs-nao-oficial-whatsapp-2026
  - /alternativa-a-z-api
  - /alternativa-a-uazapi
  - /alternativa-a-evolution-api
  - /o-que-e-tech-provider-meta
status: aprovado
---

# Migrar para API oficial sem perder o número: guia passo a passo

**Última atualização: 06/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** o número é seu. Está registrado em sua conta Meta Business Manager. Quando você sair de Z-API, UAZAPI ou Evolution, o número não desaparece. Você só muda qual ferramenta conversa com ele. A migração leva menos de 1 hora, não há perda de dados, e você continua operacional.

O medo de "perder número" é o maior bloqueador de migração que a gente vê. Aqui a gente desmonta esse medo.

::numeros: 1 número|continua seu, registrado na sua Business Manager ;; 2 alterações|no codigo: a URL e o token ;; 180 dias|de histórico que a coexistência traz do aplicativo ;; 24 h|prazo para disparar a sincronização depois de conectar

## Principais pontos
- Número não tem "donos" de ferramenta. Você registrou em Business Manager. Meta conhece você (CPF/CNPJ, conta BM), não conhece Z-API ou Evolution.
- Quando você muda de ferramenta, está só mudando "qual ferramenta fala com Meta em nome do meu número". Meta não se importa com essa mudança técnica.
- Histórico de conversa fica em Meta (você consegue via Graph API depois), fica em Z-API (você exporta antes de sair), fica em Datafy (automático).
- Reputação do número (qualidade, qualificação) fica com número. Se número levou ban, migração não resolve. Se número está bom, migração não estraga.
- Tempo de downtime real: 2 minutos (você muda a conexão). Preparação: 1 hora (testar, validar).

::diagrama: migration-seamless

## Pré-requisitos antes de migrar

Checklist de coisas que você precisa ter antes de começar:

1. **Business Manager verificada** (se não tiver, você não conseguiu registrar número em Z-API/UAZAPI/Evolution de verdade)
2. **phone_number_id** (ID do número na Meta, você acha no Business Manager)
3. **Acesso de admin em Business Manager** (para gerar/ver token)
4. **Webhook URL atual funcionando** (para você desativar sem perder nada)
5. **Código da sua aplicação** (para você testar mudanças antes de ir pro ar)

Se algum desses falta, a migração não sai.

## Passo a passo: Sair de Z-API/UAZAPI

Essas ferramentas, quando você tira o token, não deixam raastro. Para não perder dados:

1. **Exporte histórico**: entre no painel de Z-API/UAZAPI, procure "exportar chats" ou "backup". Baixa em JSON ou CSV.
2. **Teste o backup localmente**: abre o arquivo, valida que contém as conversas.
3. **Anote a URL do webhook**: você está enviando mensagens para qual endpoint? Anota. Você vai precisar.
4. **Pausa automações**: se tem alguma automação ativa (n8n, Make), desativa temporariamente. Nada por 5 minutos é ok.
5. **Nota o token atual**: você vai substituir ele, mas enquanto isso vale ter guardado para referência.

Feito. Dados salvos, você está pronto para sair.

## Passo a passo: Conectar em Datafy

1. **Cria conta em Datafy**: https://app.datafyapi.com.br
2. **No painel, "Conectar número"**: Datafy pede seu phone_number_id (tira de Business Manager)
3. **Cola o ID, clica "Conectar"**: Datafy valida com Meta em tempo real
4. **Em menos de 5 minutos**, Datafy mostra: token Bearer, phone_number_id, webhook_url
5. **Copia essas três informações**: token, phone_number_id e webhook_url

Pronto. Você tem tudo que precisa.

## Passo a passo: Trocar código (integração)

Onde você estava chamando Z-API:

```
POST https://api.z-api.io/instances/{seu_id}/send-text
Header: Client-Token: seu_token
Body: { "phone": "5511999...", "message": "..." }
```

Muda para:

```
POST https://graph.facebook.com/v20.0/{phone_number_id}/messages
Header: Authorization: Bearer seu_token_datafy
Body: { "messaging_product": "whatsapp", "to": "5511999...", "type": "text", "text": { "body": "..." } }
```

URL muda (de Z-API para graph.facebook.com).
Token muda (do Z-API para Datafy Bearer).
Body muda (segue formato Graph API da Meta).

Se você tem tempo, muda num environment de teste primeiro. Se está com pressa, muda tudo de uma vez (a gente valida depois).

## Passo a passo: Webhook (receber mensagens)

A Z-API estava mandando mensagens para qual URL? Exemplo: seu_servidor.com/webhook/zapi

Datafy precisa mandar para outro lugar (seu servidor receber de Datafy).

Opção 1 (sem mudar código): você redireciona. No seu servidor, adiciona uma rota que recebe de Datafy e repassa para a lógica antiga. Simples.

Opção 2 (melhor): você muda direto. Abre seu código do webhook, adapta para o formato JSON que Datafy manda (é igual Meta, é mais padronizado).

No painel de Datafy, você coloca a URL do seu webhook. Datafy valida fazendo um POST de teste. Você recebe, responde com "200 OK". Pronto.

## Migração com downtime zero

Se você quer zero downtime:

1. **Configura Datafy em ambiente paralelo** (URL diferente no seu código)
2. **Testa comunicação**: envia mensagem teste, recebe resposta
3. **Ativa webhook em Datafy** (isso é o momento crítico)
4. **Em paralelo, desativa webhook de Z-API**
5. **Muda seu código** (de Z-API para Datafy), faz deploy
6. **Valida**: envia mensagem teste de novo, via Datafy agora

Downtime: 0 segundos. Você está rodando em paralelo por 5 minutos, depois corta Z-API.

## Checklist pós-migração

Depois que você está em Datafy:

1. **Envia teste**: mensagem real para número real, valida que chega
2. **Recebe teste**: manda WhatsApp para seu número, valida que webhook recebe
3. **Monitora webhook**: acompanha logs de Datafy por 1 hora, valida que tudo passa
4. **Confirma histórico**: abre BM, vê se mensagens estão sincronizando
5. **Avisa time**: se tem equipe usando bot, fala que mudou de ferramenta

Se tudo passou, você está seguro. Se algo falhou, volta para Z-API em 5 minutos (é só trocar token de novo).

## Problemas comuns na migração

**"Não consigo encontrar phone_number_id"**
Entra em Business Manager, vai em "Configurações" > "Business Setups", lá em baixo procura "WhatsApp", vê o número, copia o ID.

**"Webhook não está recebendo mensagens"**
Valida: 1) a URL que você configurou em Datafy está certa? 2) Seu servidor está ouvindo? (netstat -tuln). 3) Firewall está bloqueando IP de Datafy? (abra as mesmas IPs que Meta usa).

**"Mensagem não está entregando"**
Valida: 1) número está conectado? (vê status em Datafy). 2) Token está válido? (testa via curl). 3) Body do JSON está no formato correto? (compara com exemplos em Datafy Docs).

**"Qualidade do número caiu"**
Mudança de ferramenta não muda qualidade. Se caiu, é porque você disparou spam ou volume alto demais. Resolve com boas práticas (templates, opt-in, respostas limpas).

## O que é irrecuperável

Se você estava em Z-API há 2 anos e perdeu todos os dados históricos, você não recupera isso migrando. Backup agora. Historicamente, só quem fez backup em Z-API consegue recuperar.

Se seu número foi banido em Z-API, trocar de ferramenta não desbanir. Você precisa de prova (mudar de conduta, conformidade legal) para Meta considerar reabilitação.

## Quanto tempo dura a migração

| Fase | Tempo |
|---|---|
| Preparação (backup, notas) | 15 minutos |
| Criar conta Datafy | 5 minutos |
| Conectar número em Datafy | 5 minutos |
| Adaptar código | 15 minutos |
| Testar em paralelo | 10 minutos |
| Fazer deploy | 5 minutos |
| Validar pós-migração | 10 minutos |
| **Total** | **~1 hora** |

Se você já conhece sua arquitetura, sai em 30 minutos.

## Perguntas frequentes

### Perco número se empresa de ferramenta fecha?

Não. Número é seu, está em BM. Empresa fecha, você muda para outra ferramenta. Número fica.

### Posso manter backup em Z-API enquanto rodo em Datafy?

Sim. Teoricamente você poderia rodar os dois em paralelo (webhook duplo). Na prática, gera confusão. Melhor é: Z-API vai embora, Datafy fica.

### Quanto tempo até a operação estabilizar?

24 horas de operação sem incidentes. Depois disso, você pode remover backup de Z-API.

### Devo avisar clientes sobre mudança?

Só se clientes acessam número direto. Se eles só recebem mensagem, muda nada na perspectiva deles.

### Posso voltar para Z-API se Datafy não funcionar?

Sim. É mesmo processo reverso. Mas você já começou migração porque Z-API tava arriscada. Melhor não voltar.

## Como decidir: agora ou depois?

Migre agora se: está em Z-API/UAZAPI (risco crescente), está com plan de crescimento (precisa infraestrutura confiável), ou já enfrentou downtime.

Pode deixar para depois se: é prototipagem de 2 semanas (mesmo aí, por que não começar certo?), ou tem contrato que obriga ferramenta específica (raro).

[Teste 7 dias grátis em Datafy, começa migração hoje](https://app.datafyapi.com.br)

## Leia também
- [API oficial vs não oficial](/api-oficial-vs-nao-oficial-whatsapp-2026)
- [Alternativa a Z-API](/alternativa-a-z-api)
- [Alternativa a UAZAPI](/alternativa-a-uazapi)
- [Como receber mensagens no webhook](/webhook-whatsapp-cloud-api-como-receber-mensagens)

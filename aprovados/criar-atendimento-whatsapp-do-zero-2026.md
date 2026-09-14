---
title: "Como criar um WhatsApp Web do zero com a API oficial"
description: "Uma tela de atendimento própria com a API oficial: interface, banco com duas tabelas, webhook, mídia, envio, status, tempo real e publicação, com as decisões que aparecem no caminho."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "criar-atendimento-whatsapp-do-zero"
cluster: "implementacao"
hero: "camadas"
intent: "como-fazer"
persona: "saas"
competitors: []
published: 2026-09-09
updated: 2026-09-14
sources:
  - https://www.youtube.com/watch?v=HVRCBsJI_Eo
  - https://www.youtube.com/watch?v=vGovcR8W5g8
  - https://www.youtube.com/watch?v=fhz6n2s91-g
  - https://www.youtube.com/watch?v=LIT4FxgqHhE
  - https://app.datafyapi.com.br/docs
videos: [HVRCBsJI_Eo]
internal_links:
  - /tunel-para-testar-webhook-local
  - /ver-payload-das-mensagens-em-tempo-real
  - /como-receber-midia-api-oficial-whatsapp
  - /laco-de-webhook-derruba-numero
  - /o-telefone-esta-sumindo-do-webhook
status: aprovado
---

# Como criar um WhatsApp Web do zero com a API oficial

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** uma tela de conversa parecida com o WhatsApp Web, funcionando com a API oficial em coexistência, sai em três fases: **interface**, **banco de dados** e **conexão com a API**. O projeto de referência, construído por Israel Henrique, CTO da Datafy, usa Claude Design para o layout, VS Code com Claude Code ou Codex, Nuxt, Supabase com duas tabelas, Pusher para tempo real, a Datafy API para o WhatsApp e a Vercel para publicar. O código está público no GitHub.

O objetivo não é um produto comercial. É entender o funcionamento da API enviando e recebendo mensagens.

::numeros: 3 fases|interface, banco e API ;; 2 tabelas|conversas e mensagens ;; 20 e 50|conversas e mensagens por página ;; 100|conexões simultâneas no plano grátis do Pusher

## Principais pontos
- **Comece pela interface, com dados falsos,** e só depois crie as tabelas.
- **Modele o banco a partir de payloads reais**, copiados do log da Datafy.
- **Não dê à IA controle do banco.** Ela gera o SQL; você executa.
- **Consulta ao banco sai do servidor**, com a chave de serviço, nunca do navegador.
- **Webhook primeiro, tempo real depois.** E, ao publicar, troque a URL do webhook pela de produção.

::diagrama: webhook-fluxo

## Fase 1: a interface

A tela tem duas áreas: lista de conversas à esquerda e mensagens à direita, com o campo de digitação flutuante. O layout foi gerado no Claude Design a partir de um print do WhatsApp Web, e depois transformado em componentes Vue no projeto Nuxt, com Tailwind.

Uma prática desta fase: criar um arquivo de documentação com o roteiro do projeto. Uma sessão nova da ferramenta de IA começa com contexto a partir dele. Quando uma ferramenta de IA trava no meio do projeto e é trocada por outra, é esse arquivo que permite continuar de onde parou.

::video: HVRCBsJI_Eo | O projeto completo: interface, banco, webhook, mídia, envio, tempo real e publicação na Vercel.

## Fase 2: o banco

**Primeiro, os payloads.** Antes das tabelas, mande para o número mensagens de tipos diferentes (texto, áudio, imagem, mensagem pelo celular, envio pela API) e copie o payload de cada uma no bate-papo do painel da Datafy, para a IA saber quais campos existem. [Como usar esse log está aqui](/ver-payload-das-mensagens-em-tempo-real).

Três observações sobre os payloads, que valem para qualquer projeto:

**`phone_number_id` é do número conectado**, e não de quem mandou. Ele vem igual em todas as mensagens, independente do remetente.

**Quem mandou está em `contacts`**, com nome, telefone e `user_id`, o identificador novo do WhatsApp nas APIs. A previsão é que, no futuro, o telefone deixe de vir. [Sobre o user_id](/o-telefone-esta-sumindo-do-webhook).

**Envio pela API volta só como status.** O webhook não traz o conteúdo da mensagem enviada: traz o ID da mensagem com o status.

**Duas tabelas.** Conversas e mensagens, no Supabase. A primeira versão gerada pela IA trouxe colunas desnecessárias, como avatar, que a API oficial não manda, e contador de não lidas. E esqueceu a legenda de mídia, que precisou ser acrescentada. Como a primeira versão já tinha sido aplicada, a correção veio numa nova migration.

**Não dê à IA controle do banco.** A IA sugeriu aplicar as mudanças pela linha de comando, e a sugestão foi recusada. Nas palavras de Israel Henrique, CTO da Datafy: *"o banco de dados é o coração do projeto. Se dá o controle para ele, ele pode fazer muita coisa errada. No máximo você dá permissão para ela ler o teu banco de dados, mas nunca para mexer."* A IA gera o SQL; você cola e executa no editor do Supabase.

## Segurança: chaves, políticas e assinatura

**Chaves do Supabase.** A chave anônima é pública. A de serviço nunca pode ser exposta: fica só no servidor. Se ela aparecer em algum lugar público, como uma gravação de tela, gere uma nova.

**O arquivo de exemplo de variáveis vai para o GitHub.** Por isso ele leva só os nomes das variáveis, nunca os valores.

**Política pública removida.** A IA tinha criado políticas que deixavam as tabelas legíveis por qualquer um com a chave pública. A correção: remover essas políticas, deixar as tabelas sem acesso público e mover todas as consultas para uma pasta de API no servidor, usando a chave de serviço.

**Assinatura do webhook.** Os webhooks da Datafy são configurados no painel e enviam os eventos com assinatura HMAC. [Como validar a assinatura](/validar-assinatura-do-webhook).

## Desempenho: paginação e cache

**Paginação.** Conversas de 20 em 20 e mensagens de 50 em 50, carregando mais conforme o usuário rola.

**Mensagens começando de baixo.** A lista abre na mensagem mais recente.

**Cache local com Pinia.** Sem cache, voltar para uma conversa já aberta refazia a consulta, uma chamada ao banco desnecessária.

## Fase 3: a API

**Webhook primeiro, sem tempo real.** Um endpoint que recebe o evento, identifica ou cria a conversa e grava a mensagem. Para testar localmente, ngrok na porta da aplicação. [O passo a passo do túnel, com o erro 403 que apareceu, está aqui](/tunel-para-testar-webhook-local).

**Variáveis da Datafy.** URL base, token e `phone_number_id`. O token é gerado na criação do canal, no painel da Datafy, e é lá que você troca por um novo se ele vazar. [O que é a Datafy API](/o-que-e-a-datafy-api).

**Mídia.** Uma função que chama a Datafy com o identificador da mídia e o token e recebe a URL para exibir. [Como receber mídia está aqui](/como-receber-midia-api-oficial-whatsapp).

**Envio.** O campo de digitação envia pela Datafy API. A resposta da requisição traz um ID: isso confirma que o pedido foi aceito, não que a mensagem chegou. O status e o eco da mensagem chegam depois pelo webhook, sem duplicar. Os tiques azuis aparecem quando o status de leitura chega.

**Tempo real com Pusher.** O servidor recebe o webhook, grava e publica no Pusher, e a tela recebe. O plano gratuito do Pusher atende até 100 conexões simultâneas.

## O que a tela precisa tratar: janela e status

**A janela de 24 horas.** Mensagem livre, digitada no campo, só sai enquanto a janela de atendimento daquele cliente está aberta. Quem abre e renova a janela é a mensagem do cliente; a resposta da empresa não renova. Cada cliente tem a sua janela. Com ela fechada, só template. [Como a janela funciona](/janela-de-24-horas-whatsapp).

**Falha depois do 200.** Fora da janela, a requisição pode voltar HTTP 200 com ID, e a falha chega depois no webhook de status. Por isso a mensagem na tela muda de estado conforme o status que chega:

| Status no webhook | O que significa |
|---|---|
| `sent` | Enviada; ainda não confirma entrega |
| `delivered` | Entregue ao destinatário |
| `read` | Lida, quando a confirmação está disponível |
| `failed` | Falha, com o erro. Exemplos: mensagem de serviço fora da janela, falha no pagamento |

Use o ID da mensagem para ligar cada evento à mensagem gravada. E guarde o horário da última mensagem recebida de cada cliente: conferindo esse horário antes de enviar, a tela sabe se cabe mensagem livre ou se é preciso template.

## Apagar conversa em cascata

Ao apagar uma conversa, a tabela apagava as mensagens junto. O risco: uma conversa com 1.000 mensagens gera 1.000 linhas apagadas de uma vez, e isso pode travar. A alternativa é remover o comportamento em cascata. Para o tamanho deste projeto, ele ficou.

## Publicar

Código no GitHub, projeto importado na Vercel, variáveis de ambiente coladas de uma vez. E o passo que não pode faltar: trocar a URL do webhook no painel da Datafy, do túnel para a de produção. Enquanto o túnel estava ligado, as mensagens continuavam chegando por ele.

## Os limites do projeto

É um número só, configurado por variável de ambiente. Vários números, escolhidos de forma dinâmica, pedem um projeto mais elaborado.

## Perguntas frequentes

### Quais ferramentas o projeto usa?

Claude Design, VS Code com Claude Code ou Codex, Nuxt, Supabase, Pusher, Datafy API e Vercel.

### Quantas tabelas?

Duas: conversas e mensagens.

### O código está disponível?

Está, no GitHub, com as instruções, o SQL das tabelas e a referência de design.

### Por que as consultas ao banco saem do servidor?

Porque as tabelas ficam sem acesso público, e só a chave de serviço, que nunca vai para o navegador, consegue ler.

### O projeto funciona com vários números?

Não. É um número, configurado por variável de ambiente.

## Como decidir

Se o objetivo é entender como a API oficial funciona construindo, siga as três fases na ordem desta página, começando pela coleta de payloads antes do banco. Se você precisa atender clientes com equipe agora, uma caixa de entrada pronta como o Chatwoot se liga à Datafy em minutos.

::cta: Comece coletando os payloads | Abra o bate-papo do painel, mande para o número um texto, um áudio, uma imagem, uma mensagem pelo celular e um envio pela API, e copie os cinco payloads antes de criar qualquer tabela.

## Leia também
- [Como testar o webhook na sua máquina com ngrok](/tunel-para-testar-webhook-local)
- [Ver o payload das mensagens em tempo real](/ver-payload-das-mensagens-em-tempo-real)
- [Como receber imagem, áudio e documento](/como-receber-midia-api-oficial-whatsapp)
- [O laço de webhook que pode bloquear o seu número](/laco-de-webhook-derruba-numero)

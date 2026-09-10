---
title: "Como criar um WhatsApp Web do zero com a API oficial"
description: "O projeto do tutorial completo do canal DATA7: interface, banco com duas tabelas, webhook, mídia, envio, tempo real e publicação, com as decisões que aparecem no caminho."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "criar-atendimento-whatsapp-do-zero"
cluster: "implementacao"
hero: "camadas"
intent: "como-fazer"
persona: "saas"
competitors: []
published: 2026-09-09
updated: 2026-09-10
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

**Última atualização: 10/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** no tutorial completo do canal DATA7, o Israel Henrique, CTO da Datafy, constrói uma tela de conversa parecida com o WhatsApp Web, funcionando com a API oficial em coexistência. O projeto tem três fases: **interface**, **banco de dados** e **conexão com a API**. A pilha: Claude Design para o layout, VS Code com Claude Code ou Codex, Nuxt, Supabase com duas tabelas, Pusher para tempo real, a Datafy API para o WhatsApp e a Vercel para publicar. O código está público no GitHub.

O objetivo declarado não é um produto comercial: *"o foco é entender o funcionamento da API, enviar e receber mensagens."*

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

Uma prática que ele adota nessa fase e explica o motivo: criar um arquivo de documentação com o roteiro do projeto. *"Se eu iniciar uma sessão nova depois, a gente consegue ter um contexto."* Mais tarde no vídeo, quando uma ferramenta de IA trava, ele troca por outra, e o arquivo de roteiro é o que permite continuar de onde parou.

::video: HVRCBsJI_Eo | Em 03:43 ele apresenta as ferramentas, em 12:08 começa o layout, e em 41:57 cria o arquivo de roteiro do projeto.

## Fase 2: o banco

**Primeiro, os payloads.** Antes das tabelas, ele manda mensagens de tipos diferentes para o número (texto, áudio, imagem, mensagem pelo celular, envio pela API) e copia o payload de cada uma no bate-papo do painel da Datafy, para a IA saber quais campos existem. [Como usar esse log está aqui](/ver-payload-das-mensagens-em-tempo-real).

Três observações dele sobre os payloads, que valem para qualquer projeto:

**`phone_number_id` é do número conectado**, e não de quem mandou: *"sempre vai vir esse mesmo número, independente de quem mandou a mensagem."*

**Quem mandou está em `contacts`**, com nome, telefone e `user_id`, *"que é uma identificação nova do WhatsApp das APIs. No futuro o telefone não vai mais estar disponível."* [Sobre o user_id](/o-telefone-esta-sumindo-do-webhook).

**Envio pela API volta só como status**: *"ele não vai trazer para você o conteúdo da mensagem, ele vai trazer apenas o ID da mensagem com o status."*

**Duas tabelas.** Conversas e mensagens, no Supabase. A primeira versão gerada pela IA trouxe colunas que ele considerou desnecessárias, como avatar (*"a API oficial não manda isso"*) e contador de não lidas, e esqueceu a legenda de mídia, que ele pediu para acrescentar. Como a primeira versão já tinha sido aplicada, a correção veio numa nova migration.

**Não dê à IA controle do banco.** A IA sugeriu aplicar as mudanças pela linha de comando, e ele recusou: *"o banco de dados é o coração do projeto. Se dá o controle para ele, ele pode fazer muita coisa errada. No máximo você dá permissão para ela ler o teu banco de dados, mas nunca para mexer."* A IA gera o SQL; ele cola e executa no editor do Supabase.

::video: HVRCBsJI_Eo | Em 45:12 ele coleta os payloads, em 54:35 roda a migration, em 56:44 corta as colunas e pede a legenda, e em 1:00:14 explica por que não dá controle do banco para a IA.

## Segurança: chaves e políticas

**Chaves do Supabase.** A chave anônima é pública; a de serviço *"nunca pode ser exposta em lugar nenhum. Ela fica só no servidor."* Como ela apareceu na gravação, ele gera uma nova.

**O arquivo de exemplo de variáveis vai para o GitHub.** A IA avisou que ele tinha colado credenciais no arquivo de exemplo, e ele reforça: *"não coloca aqui os valores, senão vai acontecer uma tragédia."*

**Política pública removida.** A IA tinha criado políticas que deixavam as tabelas legíveis por qualquer um com a chave pública. Ele remove, deixa as tabelas sem acesso público, e manda a IA mover todas as consultas para uma pasta de API no servidor, usando a chave de serviço.

::video: HVRCBsJI_Eo | Em 1:01:52 ele configura as variáveis e fala das chaves, e em 1:08:45 remove as políticas públicas e move as consultas para o servidor.

## Desempenho: paginação e cache

**Paginação.** Conversas de 20 em 20 e mensagens de 50 em 50, carregando mais conforme o usuário rola.

**Mensagens começando de baixo.** A lista abre na mensagem mais recente.

**Cache local com Pinia.** Sem cache, voltar para uma conversa já aberta refazia a consulta. Na fala dele: *"isso aqui é uma chamada ao banco de dados desnecessária."*

## Fase 3: a API

**Webhook primeiro, sem tempo real.** Um endpoint que recebe o evento, identifica ou cria a conversa e grava a mensagem. Para testar localmente, ngrok na porta da aplicação. [O passo a passo do túnel, com o erro 403 que apareceu, está aqui](/tunel-para-testar-webhook-local).

**Variáveis da Datafy.** URL base, token e `phone_number_id`. Sobre o token: *"caso seu token vazar, você vem aqui e muda."*

**Mídia.** Uma função que chama a Datafy com o identificador da mídia e o token e recebe a URL para exibir. [Como receber mídia está aqui](/como-receber-midia-api-oficial-whatsapp).

**Envio.** O campo de digitação envia pela Datafy API; o status e o eco da mensagem chegam depois pelo webhook, sem duplicar. Os tiques azuis aparecem quando o status de leitura chega.

**Tempo real com Pusher.** O servidor recebe o webhook, grava e publica no Pusher, e a tela recebe. Sobre o custo: *"até 100 conexões simultâneas é gratuito."*

::video: HVRCBsJI_Eo | Em 1:33:24 o webhook começa a gravar, em 1:52:03 a mídia, em 1:57:07 o envio pelo campo de digitação, e em 2:08:19 o Pusher.

## Apagar conversa em cascata

Ao apagar uma conversa, a tabela apagava as mensagens junto. Ele comenta o risco: *"se você tiver, por exemplo, digamos lá, 1000 mensagens numa conversa, ela vai deletar 1000 linhas. Isso pode travar."* A alternativa que ele mostra é remover o comportamento em cascata. Para o tamanho do projeto, ele mantém.

## Publicar

Código no GitHub, projeto importado na Vercel, variáveis de ambiente coladas de uma vez. E o passo que não pode faltar: trocar a URL do webhook no painel da Datafy, do túnel para a de produção. Enquanto o túnel estava ligado, as mensagens continuavam chegando por ele.

## Os limites do projeto

É um número só, configurado por variável de ambiente. Na fala dele: *"se você quiser algo mais robusto, mais elaborado, para ter vários números e de forma dinâmica selecionar os números, aí já é outra coisa."*

## Perguntas frequentes

### Quais ferramentas o tutorial usa?

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

Se o objetivo é entender como a API oficial funciona construindo, siga as três fases na ordem do vídeo, começando pela coleta de payloads antes do banco. Se você precisa atender clientes com equipe agora, uma caixa de entrada pronta como o Chatwoot se liga à Datafy em minutos.

::cta: Comece coletando os payloads | Abra o bate-papo do painel, mande para o número um texto, um áudio, uma imagem, uma mensagem pelo celular e um envio pela API, e copie os cinco payloads antes de criar qualquer tabela.

## Leia também
- [Como testar o webhook na sua máquina com ngrok](/tunel-para-testar-webhook-local)
- [Ver o payload das mensagens em tempo real](/ver-payload-das-mensagens-em-tempo-real)
- [Como receber imagem, áudio e documento](/como-receber-midia-api-oficial-whatsapp)
- [O laço de webhook que pode bloquear o seu número](/laco-de-webhook-derruba-numero)

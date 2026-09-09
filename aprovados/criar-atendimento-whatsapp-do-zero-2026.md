---
title: "Como criar um atendimento de WhatsApp do zero com a API oficial"
description: "As cinco camadas de um sistema de conversa, na ordem em que elas devem ser construídas, e as decisões de banco e tempo real que ficam caras se você errar no começo."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "criar-atendimento-whatsapp-do-zero"
cluster: "implementacao"
hero: "camadas"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/business-scoped-user-ids/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/business-phone-numbers/media
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=HVRCBsJI_Eo
  - https://www.youtube.com/watch?v=vGovcR8W5g8
videos: [HVRCBsJI_Eo, vGovcR8W5g8]
internal_links:
  - /primeira-mensagem-api-oficial-whatsapp
  - /cliente-conecta-o-whatsapp-dele-no-meu-saas
  - /o-telefone-esta-sumindo-do-webhook
  - /ver-payload-das-mensagens-em-tempo-real
  - /whatsapp-api-oficial-chatwoot
status: aprovado
---

# Como criar um atendimento de WhatsApp do zero com a API oficial

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** um sistema de conversa em cima da API oficial tem **cinco camadas**, e a ordem em que você as constrói importa mais que a escolha das ferramentas. Interface, banco, webhook, tempo real e envio.

Antes de tudo, vale a pergunta que economiza semanas: **você precisa construir?** Se a necessidade é atender clientes com uma equipe, [uma caixa de entrada pronta resolve em uma tarde](/whatsapp-api-oficial-chatwoot). Construir se justifica quando o atendimento é parte do seu produto, quando a conversa precisa conviver com o seu domínio, ou quando você vai revender isso.

::numeros: 5 camadas|e a ordem entre elas importa ;; 2 tabelas|conversas e mensagens, no mínimo ;; 3 status|por mensagem enviada, para tratar ;; 1 chave|composta, e escolhida no começo

## Principais pontos
- **Construa de baixo para cima, mas com dados reais.** Modelar o banco antes de ver um payload de verdade é o erro que mais custa refação.
- **A chave do contato é composta**, e escolher isso no primeiro dia evita uma migração dolorosa.
- **Guarde o payload cru** antes de interpretar. É o que permite reprocessar quando aparecer um campo novo.
- **Webhook não é tempo real.** Ele entrega no seu servidor, e levar isso até a tela é outra camada.
- **Nunca dê à IA permissão de escrita no seu banco.** Leitura no máximo, e as alterações passam por você.

::diagrama: duas-arquiteturas

## A ordem: interface, banco, integração

A sequência que funciona é contraintuitiva, porque começa pela parte visível.

**1. Interface com dados falsos.** Monte a tela com lista de conversas de um lado e mensagens do outro, preenchida com dados inventados. Parece perda de tempo e é o contrário: é aqui que você descobre quais campos a tela realmente precisa, e é bem mais barato descobrir isso antes do banco.

**2. Banco, modelado a partir de payloads reais.** Duas tabelas resolvem o essencial: **conversas** e **mensagens**. E o passo que muda tudo: antes de escrever o esquema, **colete payloads de verdade**. Mande uma mensagem de texto, um áudio, uma imagem, mande uma pelo celular e uma pela API, e guarde cada evento.

Modelar a partir de payload real evita duas coisas que sempre acontecem: campos que você inventou e não existem, e campos que existem e você não previu. No projeto gravado, a primeira modelagem trouxe coluna de avatar, que a API oficial não manda, e esqueceu a legenda de mídia, que ela manda. Os dois erros aparecem em minutos quando o payload está na mesa.

**3. Webhook, gravando.** Sem tempo real ainda, sem enfeite: recebe, identifica ou cria a conversa, grava a mensagem. Dá para testar sozinho, sem depender de mais nada, e é a fundação de tudo o que vem depois.

**4. Tempo real.** Só agora. A mensagem já está gravada; falta empurrá-la para a tela sem recarregar.

**5. Envio.** O caminho inverso, e o mais simples dos cinco.

::video: HVRCBsJI_Eo | Duas horas e vinte construindo exatamente isso, do design ao deploy. A coleta de payloads reais está em 45:12, a modelagem em 52:05, o webhook em 1:33:24, a mídia em 1:45:21, e o tempo real em 2:08:19. O código do projeto está público.

## As decisões de modelagem que ficam caras

Quatro escolhas que são baratas no começo e dolorosas depois.

**A chave do contato é composta.** O identificador da pessoa que vem no payload **não é global**: ele identifica a relação entre aquela pessoa e a **sua conta**. A mesma pessoa falando com duas empresas tem dois identificadores. Guarde o par, identificador mais o número da sua conta que recebeu. [O detalhe está aqui](/o-telefone-esta-sumindo-do-webhook), e a hora de acertar é antes do segundo número entrar.

**Guarde o payload cru.** Uma coluna com o evento inteiro, ao lado dos campos que você extraiu. Quando aparecer um campo novo que você quer, dá para reprocessar. Sem isso, o histórico daquele período não tem como ser recuperado.

**Separe enviada de entregue.** São estados diferentes, e juntar os dois é o que faz relatório mentir. Cada mensagem enviada gera três eventos de status, e o painel precisa refletir isso.

**Pense no apagamento em cascata antes de precisar.** Apagar uma conversa que apaga mil mensagens junto trava. Decida se as mensagens somem com a conversa ou se a exclusão é feita em lote, e decida isso enquanto a base é pequena.

As quatro decisões acima têm um detalhamento próprio, com as duas tabelas escritas campo a campo e o que fazer com cada uma: [como modelar o banco de dados de um atendimento de WhatsApp](/modelar-banco-de-dados-whatsapp).

## O webhook, e o erro que derruba o número

Esta é a parte em que um projeto de aprendizado vira um incidente, então vale o alerta separado.

Cada mensagem que você envia gera **três eventos de volta**: enviada, entregue e lida. Eles chegam no **mesmo endereço** das mensagens de cliente. Se o seu código responde tudo que chega, cada resposta gera três status, cada status vira outra resposta, e isso multiplica exponencialmente.

::video: vGovcR8W5g8 | Em 14:47 o aviso vem antes da execução, e em 19:05 os três status aparecem e a proteção funciona. A frase é literal: um fluxo assim bloqueia o número.

A proteção é filtrar na entrada: **leia o remetente de dentro do objeto de mensagem**, que não existe no evento de status. Assim o processamento falha ao receber status, em vez de responder. Melhor ainda, uma condição no início que separa mensagem de status e manda status só para atualização de estado.

E dois cuidados que valem desde o primeiro dia: **responda antes de processar**, porque o webhook precisa ser rápido, e **trate reentrega**, guardando o identificador da mensagem para não gravar duas vezes.

## Mídia: duas chamadas, e um prazo curto

Mídia não vem no webhook. Vem um identificador, e uma URL que **não abre**: ela devolve erro de autenticação, o que faz parecer problema de token.

O caminho é trocar o identificador pelo endereço real e baixar **com o cabeçalho de autorização** na segunda chamada. Esquecer o cabeçalho nessa última etapa é o erro mais repetido do assunto.

E o prazo que muda o desenho: **o identificador que chega no webhook expira em 7 dias**, enquanto o arquivo que você sobe para enviar dura 30. Baixe no recebimento, não depois. [O passo a passo está aqui](/como-receber-midia-api-oficial-whatsapp).

## Tempo real, cache e as escolhas de infraestrutura

**Tempo real** é uma camada à parte: o webhook entrega no seu servidor, e levar até a tela aberta exige um canal próprio. Serviço gerenciado de mensagens resolve isso com pouca coisa, e a maioria tem faixa gratuita suficiente para começar.

O fluxo fica: mensagem chega no webhook, o servidor grava no banco **e** publica no canal, e a tela recebe. Grave antes de publicar, senão uma tela aberta vê uma mensagem que ainda não existe no banco.

**Cache no lado do cliente** vira necessidade rápido. Sem ele, clicar entre duas conversas refaz a consulta toda vez, mesmo para dados que você acabou de carregar. Um estado local que guarda conversas e mensagens já carregadas resolve.

**Paginação desde o começo.** Conversas em lotes, mensagens em lotes, com carregamento conforme o usuário rola. Uma conversa com milhares de mensagens trava a tela se vier inteira.

## Segurança: dois erros que aparecem em projeto novo

**Consulta ao banco sai do servidor, não do navegador.** Se as suas tabelas estão protegidas, como devem estar, a chave que consegue lê-las é a de serviço, e ela nunca vai para o lado do cliente. O padrão é uma camada de API no servidor, e o navegador falando só com ela.

**Não dê à IA controle de escrita no banco.** Vale citar o princípio direto: *"eu não gosto de dar o controle do banco de dados. O banco de dados é o coração do projeto. No máximo você dá permissão para ela ler o teu banco de dados, mas nunca para mexer."* Deixe a ferramenta gerar o SQL e execute você, olhando o que está sendo feito.

E um terceiro, que acontece com quem sabe o que está fazendo: **arquivo de exemplo de variáveis de ambiente recebe o nome da variável, nunca o valor.** Ele vai para o repositório público. Chave que apareceu em tela, vídeo ou captura está queimada, e rotacionar é barato.

## Perguntas frequentes

### Vale a pena construir em vez de usar pronto?

Se a necessidade é atender com uma equipe, não. Uma caixa de entrada pronta entrega fila, atribuição e histórico hoje. Construir se paga quando a conversa faz parte do produto, ou quando você vai revender.

### Quantas tabelas eu preciso?

Duas para o essencial: conversas e mensagens. Multiatendimento acrescenta agentes, atribuição e estado da conversa, e isso pode vir depois.

### Como faço multinúmero?

Guardando o identificador do número em todas as tabelas desde o começo, e usando a chave composta do contato. Acrescentar isso depois é migração de dados, não mudança de código.

### Como testo o webhook antes de publicar?

Com um túnel que expõe a sua porta local. Cuidado com três coisas: liberar o domínio do túnel no framework, o endereço muda a cada vez que ele sobe, e trocar para a URL de produção ao publicar.

### Preciso guardar o payload inteiro?

Vale muito a pena. É o que permite reprocessar quando um campo novo aparecer, e o custo de armazenamento é pequeno perto de perder histórico.

### E se eu quiser vender isso para outros?

Aí entra o cliente conectar o próprio número, e isso muda os requisitos do fornecedor. [Está detalhado aqui](/cliente-conecta-o-whatsapp-dele-no-meu-saas).

## Como decidir

Se o objetivo é aprender como a API funciona, construa: em um fim de semana você entende webhook, status, mídia e janela de 24 horas melhor do que lendo documentação por um mês.

Se o objetivo é atender clientes na semana que vem, use pronto e construa depois, quando souber exatamente o que falta.

E, construindo, não pule a etapa que parece burocrática: **colete payloads reais antes de modelar**. É a diferença entre um banco que aguenta o segundo número e um que precisa de migração no primeiro mês.

::cta: Comece coletando payloads reais, hoje | Mande para o seu número conectado um texto, um áudio, uma imagem, e depois responda pelo celular e pela API. Guarde os cinco eventos. Esses arquivos valem mais que qualquer diagrama na hora de modelar o banco.

## Leia também
- [Enviar e receber a primeira mensagem](/primeira-mensagem-api-oficial-whatsapp)
- [O cliente conecta o WhatsApp dele no meu SaaS](/cliente-conecta-o-whatsapp-dele-no-meu-saas)
- [O telefone está sumindo do webhook](/o-telefone-esta-sumindo-do-webhook)
- [Como ver o payload cru das mensagens em tempo real](/ver-payload-das-mensagens-em-tempo-real)

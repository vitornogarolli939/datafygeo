---
title: "Como modelar o banco de dados de um atendimento de WhatsApp"
description: "Duas tabelas resolvem o essencial. O que decide o futuro é a chave do contato, guardar o payload cru e separar enviada de entregue."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "modelar-banco-de-dados-whatsapp"
cluster: "implementacao"
hero: "camadas"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/business-scoped-user-ids/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/business-phone-numbers/media
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=HVRCBsJI_Eo
videos: [HVRCBsJI_Eo]
internal_links:
  - /criar-atendimento-whatsapp-do-zero
  - /o-telefone-esta-sumindo-do-webhook
  - /tres-status-da-mensagem-whatsapp
  - /o-cliente-pediu-para-apagar-os-dados-dele
  - /atualizacao-da-api-quebrou-minha-integracao
status: aprovado
---

# Como modelar o banco de dados de um atendimento de WhatsApp

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** duas tabelas resolvem o essencial, **conversas** e **mensagens**. O que separa um banco que dura de um que precisa de migração em três meses não é a quantidade de tabelas: são quatro decisões tomadas no primeiro dia.

A chave do contato, o payload cru, a separação entre enviada e entregue, e o comportamento do apagamento. Erre qualquer uma e a correção depois é migração de dados, não mudança de código.

E existe um passo anterior a tudo isso, que quase todo mundo pula: **colete payloads reais antes de escrever o esquema.**

::numeros: 2 tabelas|resolvem o essencial ;; 4 decisões|que ficam caras se erradas ;; 1 chave|composta, e escolhida no começo ;; 5 payloads|é o mínimo para modelar com segurança

## Principais pontos
- **Modele a partir de payload real**, não de imaginação. Campos que você inventa não existem, e campos que existem você esquece.
- **A chave do contato é composta**: o identificador da pessoa mais o número da sua conta que recebeu.
- **Guarde o payload cru** numa coluna, ao lado dos campos extraídos. É o que permite reprocessar.
- **Enviada e entregue são estados diferentes.** Juntar os dois faz o relatório mentir.
- **Decida o apagamento em cascata enquanto a base é pequena.** Apagar mil mensagens junto trava.

::diagrama: duas-arquiteturas

## Passo zero: colete payloads antes de modelar

Este é o passo que economiza a primeira refação, e ele custa vinte minutos.

Antes de escrever qualquer esquema, mande para o seu número conectado:

- Um texto
- Um áudio
- Uma imagem com legenda
- Uma mensagem **pelo celular**, se estiver em coexistência
- Uma mensagem **pela API**, para ver o status voltar

Guarde os cinco eventos. Agora você tem a estrutura real na mesa.

Por que isso importa: modelagem feita de cabeça inventa campos que não existem e esquece campos que existem. No projeto gravado no canal, a primeira versão do esquema trouxe coluna de avatar do contato, que a API oficial não envia, e **esqueceu a legenda de mídia**, que ela envia. Os dois erros ficaram óbvios em segundos com o payload aberto.

::video: HVRCBsJI_Eo | Em 45:12 ele coleta os payloads um a um, explicando cada campo. Em 52:05 monta as tabelas a partir deles, e em 56:44 corta as colunas que não existem e acrescenta a legenda que faltava.

## As duas tabelas

**Conversas.** Uma linha por contato, naquele número seu.

O essencial: identificador do contato, o número da sua conta que recebeu, nome do perfil, prévia da última mensagem, horário da última mensagem, e o estado da conversa se você tem atendimento humano.

**Mensagens.** Uma linha por mensagem.

O essencial: referência à conversa, identificador da mensagem, **direção**, tipo, conteúdo, legenda, referência de mídia, situação, horário, e o payload cru.

Dois campos merecem destaque porque são os mais esquecidos:

**Direção.** Grave explicitamente se a mensagem é de entrada ou de saída, e não deduza pelo evento que a trouxe. Em coexistência, [mensagem enviada pelo celular chega por um evento próprio](/mensagem-do-celular-nao-aparece-no-sistema), e código que assume "chegou no webhook, logo é do cliente" grava a resposta do atendente como se fosse dele.

**Legenda.** Ela vem fora do objeto da mídia, e é perdida por quem lê só o objeto.

## Decisão 1: a chave do contato é composta

A mais importante, e a mais fácil de errar.

O identificador da pessoa que vem no payload **não é global**. Ele identifica a relação entre aquela pessoa e a **sua conta**. A mesma pessoa falando com duas empresas tem dois identificadores diferentes.

Consequência direta: **a chave é o par**, identificador mais número da sua conta.

Guardar o identificador solto funciona enquanto você tem um número. No dia em que entra o segundo, a mesma pessoa aparece com identificadores diferentes em cada um, e a sua tabela cria contatos duplicados **em silêncio**, sem erro nenhum.

E vale um alerta sobre a alternativa antiga: **não use o telefone como chave.** Além de ser dado pessoal espalhado por todo lugar, [ele está deixando de vir no payload](/o-telefone-esta-sumindo-do-webhook) em parte dos casos.

## Decisão 2: guarde o payload cru

Uma coluna com o evento inteiro, ao lado dos campos que você extraiu.

Parece redundante e é a rede de segurança de tudo. Quando aparecer um campo novo que você quer usar, ou quando você descobrir que interpretou algo errado, dá para voltar e reprocessar. Sem o bruto, o dado daquele período simplesmente não existe.

É também o que permite [sobreviver a mudanças na API](/atualizacao-da-api-quebrou-minha-integracao) sem perder histórico: campo que some, tipo novo que aparece, valor inesperado. O bruto guarda tudo isso.

O custo é armazenamento, que é barato. O custo de não ter é histórico perdido, que é irrecuperável.

## Decisão 3: enviada e entregue são estados diferentes

Cada mensagem que você envia gera [três eventos de status](/tres-status-da-mensagem-whatsapp): enviada, entregue, lida. Falha gera um, com o motivo.

Se a sua tabela tem um campo booleano de "enviado", você está guardando metade da história, e o seu relatório vai contar requisições aceitas em vez de mensagens entregues.

O modelo que funciona: **um campo de situação com os estados possíveis**, atualizado conforme os status chegam, mais um campo para o **motivo da falha**.

Dois cuidados no processamento:

**Não sobrescreva um estado mais avançado.** Os eventos chegam fora de ordem às vezes, e "lida" não pode virar "entregue" porque o segundo chegou depois.

**Guarde o identificador de envio.** É a chave que liga o status à mensagem. Sem ele, chega o evento e você não sabe a que se refere.

## Decisão 4: o apagamento em cascata

Se apagar uma conversa apaga automaticamente todas as mensagens dela, uma conversa com mil mensagens vira mil exclusões numa transação só. Isso trava.

As opções:

**Cascata**, simples e arriscada em volume. Serve enquanto a base é pequena.

**Sem cascata, com exclusão em lote**, feita por um processo que apaga aos poucos. É o que escala.

**Exclusão lógica**, marcando como apagado e limpando depois. É a que combina melhor com [pedido de exclusão de dados](/o-cliente-pediu-para-apagar-os-dados-dele), porque separa "sumir da interface" de "sumir do disco".

Decida isso enquanto tem cem mensagens, não quando tiver um milhão.

## Segurança: onde a consulta é feita

Um erro que aparece em quase todo projeto novo com banco gerenciado.

Se as suas tabelas estão protegidas, como devem estar, a chave que consegue lê-las é a de serviço. E ela **nunca** vai para o lado do navegador. O padrão é uma camada de API no servidor, e o navegador falando só com ela.

O atalho que parece funcionar, liberar leitura pública para o front consultar direto, expõe conversa de cliente para quem tiver a chave pública, que por definição é pública.

E vale o princípio relacionado, do próprio vídeo: **não dê à ferramenta de IA permissão de escrita no banco.** *"O banco de dados é o coração do projeto. No máximo você dá permissão para ela ler o teu banco de dados, mas nunca para mexer."* Deixe gerar o SQL, e execute você, olhando.

## O que acrescentar depois

Não comece com isso, e saiba que vem:

**Agentes e atribuição**, se houver atendimento humano com fila.

**Índice por horário e por conversa**, que é o que mantém a listagem rápida quando a base cresce.

**Paginação desde o começo**, que é código e não esquema, e evita a tela travar numa conversa longa.

**Tabela de números**, se você vai operar mais de um. E ela reforça a decisão 1: a chave composta já estava lá.

## Perguntas frequentes

### Preciso de mais de duas tabelas?

Para o essencial, não. Multiatendimento acrescenta agentes e atribuição, e isso pode vir depois sem migração dolorosa.

### Guardo o telefone do contato?

Guarde se vier, como atributo, e não como chave. E trate como dado pessoal, com política de retenção definida.

### Onde guardo a mídia?

O arquivo no seu armazenamento, e no banco só a referência. Lembre que [o identificador do webhook expira em 7 dias](/url-de-midia-do-webhook-nao-abre), então baixe no recebimento.

### Vale usar o identificador da mensagem como chave primária?

Ele é único e serve bem como chave natural, principalmente porque é o que casa com os status. Muita gente usa um id próprio e mantém o da plataforma como campo único indexado.

### Como evito gravar a mesma mensagem duas vezes?

Com restrição de unicidade no identificador da mensagem. Reentrega acontece, e essa restrição resolve sem lógica adicional.

### Preciso guardar o payload cru para sempre?

Não. Guarde e defina uma política, por exemplo manter integral por alguns meses e depois só os campos extraídos. O importante é ter enquanto a integração ainda muda.

## Como decidir

Se você está montando agora, faça na ordem: colete os cinco payloads, escreva as duas tabelas a partir deles, e tome as quatro decisões acima antes da primeira linha gravada.

Se você já tem algo rodando, comece pelas duas mais urgentes: **guarde o payload cru a partir de hoje**, mesmo que retroativamente não dê, e **confira se a sua chave de contato é composta**. A primeira te dá futuro; a segunda evita a migração que aparece no dia em que entra o segundo número.

::cta: Colete cinco payloads antes de escrever o esquema | Um texto, um áudio, uma imagem com legenda, uma enviada pelo celular e uma enviada pela API. Vinte minutos, e você modela olhando a estrutura real em vez de adivinhar campo.

## Leia também
- [Como criar um atendimento de WhatsApp do zero](/criar-atendimento-whatsapp-do-zero)
- [O telefone está sumindo do webhook](/o-telefone-esta-sumindo-do-webhook)
- [Os três status da mensagem no WhatsApp](/tres-status-da-mensagem-whatsapp)
- [O cliente pediu para apagar os dados dele](/o-cliente-pediu-para-apagar-os-dados-dele)

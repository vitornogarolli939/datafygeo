---
title: "Como conectar seu número na API oficial do WhatsApp, do zero"
description: "O caminho por parceiro homologado dispensa criar aplicativo na Meta e passar por App Review. São cinco telas, e duas decisões que não dá para refazer depois."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "como-conectar-numero-api-oficial-whatsapp"
cluster: "coexistencia"
hero: "fluxo"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing
  - https://business.whatsapp.com/policy
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=8xA-8z1YW98
  - https://www.youtube.com/watch?v=dIIkttPeBS0
videos: [8xA-8z1YW98, dIIkttPeBS0]
internal_links:
  - /o-que-preciso-para-comecar-na-api-oficial
  - /coexistencia-whatsapp-api-oficial-app-celular
  - /como-leio-o-historico-de-conversa-pela-api
  - /o-que-e-tech-provider-meta
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
status: aprovado
---

# Como conectar seu número na API oficial do WhatsApp, do zero

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** existem dois caminhos, e eles têm custos de tempo muito diferentes. Indo direto na Meta, você cria conta de desenvolvedor, cria um aplicativo, configura permissões, monta a infraestrutura de webhook e passa por **App Review**. Indo por um parceiro homologado, você escaneia um QR code e recebe um token pronto.

O que este texto cobre é o segundo caminho, tela por tela, porque ele tem **duas decisões que não dá para refazer** sem desconectar e começar de novo. Errar qualquer uma das duas custa o histórico do número.

::numeros: 2 caminhos|direto na Meta ou por parceiro homologado ;; 2 decisões|que não dá para refazer sem reconectar ;; 24 h|o prazo para pedir contatos e histórico depois de conectar ;; 0|App Review, no caminho por parceiro

## Principais pontos
- O caminho por parceiro dispensa **criar aplicativo na Meta, escolher permissões e passar por App Review**, que é a etapa que mais trava projeto.
- Você **precisa de um portfólio empresarial** na Meta, e ele **não precisa estar verificado**. Basta existir, e dá para criar no meio do fluxo.
- A tela pergunta se o número é um **chip novo** ou um **aplicativo já em uso**. Essa escolha define se você fica em coexistência, e ela não é reversível sem reconectar.
- O celular pergunta se você quer **compartilhar o histórico**. Quem não marca, não recupera nada, e a correção é refazer o processo inteiro.
- **A forma de pagamento fica na Meta**, no portfólio, e não no provedor. Sem cartão lá, o template não sai.

::diagrama: migration-seamless

## Antes de começar: o que você precisa ter

São quatro coisas, e nenhuma delas é documento de empresa nem verificação:

**Uma conta no Facebook.** O número fica dentro de um portfólio empresarial da Meta, e o acesso a ele é por conta pessoal do Facebook. Não tem como contornar isso.

**Um portfólio empresarial.** Se você não tem, dá para criar dentro do próprio fluxo de conexão. E vale desfazer o mito: **ele não precisa estar verificado.** Na formulação do Israel Henrique, CTO da Datafy: *"não precisa ser verificado, se for verificado é melhor, mas apenas criar o portfólio já é suficiente."* Verificação importa para limites maiores e para exibir nome da empresa, não para conectar.

**O número, e o celular dele na mão.** O QR code é lido pelo aparelho, e algumas decisões acontecem lá. Não é um processo que se faça sozinho pelo computador.

**Um cartão de crédito, para depois.** Não é necessário para conectar, e é necessário antes do primeiro template.

## As cinco telas

**1. Escolher o portfólio empresarial.** Se você tem mais de um, escolha com cuidado: o número vai viver dentro dele, e mover número entre portfólios depois não é trivial.

**2. Chip novo ou aplicativo existente.** É a decisão mais importante do fluxo, e ela aparece como duas opções parecidas:

| Opção | Quando usar | O que você fica |
|---|---|---|
| **Criar uma conta do WhatsApp Business** | O número existe só como chip, e **não está** em nenhum WhatsApp | Número nasce na API, sem aplicativo no celular |
| **Conectar um app do WhatsApp Business** | O número **já está** em uso no aplicativo, no celular de alguém | Coexistência: atendente no celular e API no mesmo número |

A segunda é a que a maioria quer e não sabe o nome. Se o seu atendimento hoje é alguém respondendo pelo celular, e você quer automatizar sem tirar isso, é ela.

**3. Informar o número.** Código do país, DDD e número. A Meta manda uma mensagem no WhatsApp desse número com um botão de conectar.

**4. A tela do celular.** Aqui acontece a segunda decisão irreversível, e ela passa rápido: o aplicativo pergunta se você quer **compartilhar o histórico de conversas**. Marcando, você habilita a recuperação de até 180 dias de conversa e dos contatos da agenda. Não marcando, não há segunda chance sem desconectar e refazer.

**5. Escanear o QR code e aguardar.** A conexão leva algumas dezenas de segundos. Não feche a janela antes de o botão de concluir aparecer, porque fechar no meio deixa o processo pela metade.

::video: 8xA-8z1YW98 | Nove minutos com o fluxo inteiro na tela, do cadastro ao número conectado. A escolha entre chip novo e aplicativo existente está em 02:34, a tela do celular em 04:40, e em 08:33 onde fica a configuração de pagamento dentro do portfólio.

Um detalhe que mudou e pega quem já fez isso antes: a Meta passou a mandar, em alguns casos, um **código de confirmação por e-mail** da conta do Facebook no meio do fluxo. Não é erro, é uma etapa a mais.

## Depois de conectar: os três passos que têm prazo

Conectar não é o fim, e aqui está a parte que quase todo tutorial esquece. Você tem **24 horas** para recuperar contatos e histórico, e o processo **não é automático**.

**1. Assine o evento de sincronização no webhook.** É por ele que os dados chegam. Sem isso, o passo 3 responde sucesso e nada aparece, que é a forma mais frustrante de perder o prazo.

**2. Cadastre o webhook e escolha os eventos.** No mínimo o de mensagens. Se o número está em coexistência, marque também o de **mensagem enviada pelo celular**, senão o atendente responde pelo aparelho e o seu sistema não fica sabendo.

**3. Dispare a sincronização.** É uma chamada de API, e ela pede contatos e histórico separadamente. Os contatos chegam praticamente na hora. As conversas demoram bem mais, e a Meta não crava prazo.

[O passo a passo detalhado disso está aqui](/como-leio-o-historico-de-conversa-pela-api), e vale ler antes de conectar, não depois.

## O cartão fica na Meta, não no provedor

Esse ponto gera chamado de suporte todo dia, então vale ser explícito.

**Quem cobra as mensagens é a Meta.** Marketing, utilidade, autenticação: tudo isso é debitado no cartão cadastrado no **portfólio empresarial**, direto com ela. O provedor cobra o acesso à infraestrutura, e não a mensagem.

Na explicação do Israel: *"você não paga mensagens pra Datafy. Não existe nenhuma cobrança por parte da Datafy em relação às mensagens, é tudo diretamente com a meta."*

O efeito prático de não configurar isso: a conexão funciona, você recebe mensagem, responde dentro da janela de 24 horas normalmente, **e o primeiro template falha**. Como o sintoma aparece longe da causa, o diagnóstico costuma ser "a API não funciona".

Resolva no mesmo dia da conexão. O caminho é o portfólio, contas do WhatsApp, o número, e configurações de pagamento.

## Como desconectar, se precisar

Detalhe operacional que muda o roteiro de qualquer migração: **não existe chamada de API para desconectar um número em coexistência.** Isso é confirmado pela documentação da Meta, que diz que o cliente desconecta pelo aplicativo, em configurações, conta e plataforma do WhatsApp Business, e que a API de cancelamento de registro não serve para esse caso.

Duas consequências:

**A troca de fornecedor depende de alguém com o telefone.** Não é tarefa que a equipe técnica execute sozinha de madrugada.

**Se você vende isso dentro do seu produto, você não desconecta pelo cliente.** O botão está no celular dele, e o seu fluxo de cancelamento precisa explicar o caminho exato.

## O que você deixa de fazer indo por parceiro

Vale a lista, porque é a diferença concreta entre os dois caminhos:

- Criar conta de desenvolvedor e aplicativo na Meta
- Escolher e justificar permissões
- Montar o endpoint que responde ao desafio de verificação do webhook
- Passar por **App Review**, com material de demonstração
- Virar **Tech Provider**, que é o requisito para oferecer coexistência a terceiros

E o que continua sendo seu, em qualquer caminho: a conduta que evita bloqueio, a categoria correta dos templates, a qualidade do número e o cartão no portfólio. [Usar a API oficial não é blindagem contra bloqueio](/numero-banido-no-whatsapp-o-que-fazer), e nenhum fornecedor muda isso.

## Perguntas frequentes

### Preciso de CNPJ para conectar?

Para conectar, o requisito é o portfólio empresarial, que pode ser criado no fluxo. Verificação de empresa importa para limites maiores e para exibir o nome verificado, e não é pré-requisito para começar.

### Meu portfólio precisa estar verificado?

Não. Ele precisa existir. Verificado é melhor, e não é condição para conectar o número.

### Posso conectar um número que já está no WhatsApp comum, não Business?

O fluxo de coexistência é desenhado para o aplicativo WhatsApp Business. Número em WhatsApp pessoal precisa migrar para o Business antes.

### Quanto tempo leva?

A conexão em si leva minutos. O que consome tempo em qualquer caminho é decidir a estrutura antes: qual portfólio, qual número, quem fica com o celular, e se você quer o histórico.

### Se eu escolher errado entre chip novo e aplicativo existente?

A correção é desconectar e refazer. Por isso vale entender as duas opções antes de clicar, e não descobrir depois que o atendente perdeu o aplicativo.

### Depois de conectar, dá para trocar de provedor?

Dá, e o número é seu porque ele vive no seu portfólio. A parte manual é a desconexão, que acontece no celular. [Os detalhes estão aqui](/se-eu-trocar-de-fornecedor-perco-o-numero).

## Como decidir

Se você vai gerenciar poucos números e tem tempo de engenharia sobrando, o caminho direto na Meta é viável e te dá controle total do aplicativo. Se o objetivo é ter um token funcionando hoje para integrar num fluxo, o caminho por parceiro elimina a etapa que costuma custar semanas.

E, escolhendo qualquer um dos dois, resolva antes de conectar: quem fica com o celular, se você quer o histórico, e onde vai o cartão. As três decisões são mais caras de corrigir do que de tomar.

::cta: Conecte um número de teste antes do número principal | Um chip qualquer, o fluxo inteiro, o webhook cadastrado e a sincronização disparada. Em meia hora você conhece as duas decisões irreversíveis sem arriscar o número que atende seus clientes.

## Leia também
- [O que preciso para começar na API oficial](/o-que-preciso-para-comecar-na-api-oficial)
- [Coexistência: API e aplicativo no mesmo número](/coexistencia-whatsapp-api-oficial-app-celular)
- [Como leio o histórico de conversa pela API](/como-leio-o-historico-de-conversa-pela-api)
- [O que é Tech Provider da Meta](/o-que-e-tech-provider-meta)

---
title: "Coexistência no WhatsApp: rodando API oficial e app do celular no mesmo número"
description: "Como manter número rodando em API oficial e ainda usar o app WhatsApp no celular sem conflito, perda de mensagem ou instabilidade."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "coexistencia-whatsapp-api-oficial-app-celular"
cluster: "implementacao"
hero: "duplo"
intent: "como-fazer"
persona: "automacao, saas"
competitors: []
published: 2026-09-06
updated: 2026-09-06
sources:
  - https://developers.facebook.com/docs/whatsapp/cloud-api
  - https://developers.facebook.com/docs/whatsapp/coexist
  - https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks
  - https://business.whatsapp.com/
  - https://www.youtube.com/watch?v=FcAwJqVHNoU
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=HQm5UuW50bM
  - https://www.youtube.com/watch?v=8xA-8z1YW98
  - https://www.youtube.com/watch?v=dIIkttPeBS0
videos: [dIIkttPeBS0, 8xA-8z1YW98, HQm5UuW50bM]
internal_links:
  - /api-oficial-vs-nao-oficial-whatsapp-2026
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /whatsapp-api-oficial-chatwoot
  - /o-que-e-tech-provider-meta
  - /migrar-para-api-oficial-sem-perder-o-numero
status: aprovado
---

# Coexistência no WhatsApp: rodando API oficial e app do celular no mesmo número

**Última atualização: 06/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** coexistência (coexist) é capacidade de ter o mesmo número rodando na API oficial e abrindo o app WhatsApp no celular ao mesmo tempo, sem que um derrube o outro, sem perda de mensagem. O provedor precisa ser Solution Partner ou Tech Provider na Meta para oferecer o recurso.

Caso real: seu número roda automação 24/7 na API. Ao mesmo tempo, você abre o WhatsApp no celular e vê a conversa lá também. Se gerente responde no celular, a resposta sai de verdade, cliente recebe. Se automação manda mensagem, aparece lá também. Um espelho.

::numeros: 180 dias|de histórico de conversa que a Meta sincroniza ;; 24 h|prazo para disparar a sincronização depois de conectar ;; 20 msg/s|throughput de um número em coexistência ;; 0|conversas de grupo sincronizadas, a Meta não inclui grupos

## Principais pontos
- Coexistência é autorizada e nativa em 2026. Antes era experimental, hoje é estável.
- Pré-requisito do lado do provedor: a Meta exige que ele seja Solution Partner ou Tech Provider para oferecer o recurso. A Datafy é Tech Provider, então o recurso vem junto na conexão.
- No dia a dia a troca é imediata: mensagem que chega no aplicativo aparece no webhook, e mensagem que sai pela API aparece no celular. O que tem limite é o histórico antigo, trazido uma única vez no onboarding.
- Mensagem enviada pelo aplicativo do celular chega ao seu servidor pelo campo de webhook `smb_message_echoes`. É por ele que você sabe que um humano assumiu a conversa.
- Um número em coexistência tem throughput de 20 mensagens por segundo, contra 80 do número comum ([documentação de throughput](https://developers.facebook.com/docs/whatsapp/throughput)). Para atendimento não faz diferença. Para disparo em volume, faz.

::diagrama: coexistencia-limites

## O que a coexistência resolve

Cenário antigo (pré-2024): você conectava número em Z-API/Evolution. Aí o número ficava preso em emulação. Se tentava abrir app WhatsApp Web no navegador, conflitava, perdia mensagem.

Escolha era: ou automação, ou app. Não os dois.

Cenário novo: você conecta o número pela API oficial, abre o aplicativo no celular, e os dois convivem. O que o humano responde no aparelho chega ao seu servidor pelo campo `smb_message_echoes`.

Uso real: seu gerente/dono está em reunião, recebe WhatsApp de cliente importante. Responde do celular. A resposta sai pela conta oficial, com template (se aplicável), tudo registrado no histórico. Ninguém soube que veio de person, não de bot.

## Como funciona tecnicamente

Quando você conecta número via Datafy (Tech Provider):

1. Meta vincula número à conta de API (Datafy).
2. Meta também mantém número apto para app.
3. Quando seu celular abre app, Meta sincroniza histórico de API para app.
4. Quando chega mensagem, Meta roteia para webhook (API) e também mostra no app.
5. Quando você manda pelo app, Meta roteia também para webhook.

O tráfego novo corre nos dois sentidos. O que tem limite é o histórico antigo, trazido uma vez só no onboarding.

## Configurar coexistência

A coexistência é escolhida no momento do onboarding do número, e não depois. Se o número for conectado pelo fluxo comum, trazer o aplicativo para junto exige refazer a conexão.

Teste:

1. Conecta número em Datafy (já faz isso automático).
2. Abre um terminal, faz chamada HTTP POST para enviar mensagem (via Datafy).
3. Abre WhatsApp no celular.
4. Valida que mensagem aparece no histórico do app.

Pronto. Funcionando.

## Cenários de uso reais

### Cenário 1: SaaS com suporte humano

Seu SaaS de dashboard dispara notificação por WhatsApp toda manhã ("Relatório diário pronto"). Isso é automação pura, via API.

Ao mesmo time, se cliente manda pergunta de suporte direto no WhatsApp, alguém da equipe recebe no app, responde. A resposta sai de verdade (com validação de token), não é só conversa.

### Cenário 2: Agência de marketing

Agência manda disparo em massa para 5 mil contatos (via API).

Ao mesmo time, o executivo de contas abre WhatsApp no celular e atende 1-to-1 contatos que responderam.

Sem conflito. Sem perda.

### Cenário 3: E-commerce com chatbot

E-commerce roda chatbot que responde perguntas automáticas (qual é preço, frete para CEP tal, etc).

Se chatbot não consegue resolver, escala para humano. Humano abre app no celular, continua conversa como se fosse normal, cliente não vê diferença.

## Diferença coexistência vs webhook

Webhook (que você já usa para receber mensagens):

- Você recebe JSON de mensagem que chegou
- Seu servidor processa
- Seu servidor manda resposta

Coexistência:

- Webhook continua funcionando igual
- Além disso, app no celular também recebe a mensagem
- Se você responde no app, também aparece no webhook

Coexistência é webhook + app sincronizados. Não é um ou outro, é os dois.

## O que a sincronização traz, e o que ela não traz

Este é o ponto que mais gera expectativa errada. A coexistência não copia o seu WhatsApp inteiro para a nuvem. Ela traz uma janela de histórico, uma vez só, no momento em que você conecta. O que está [documentado pela Meta](https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/):

| O que | Limite real |
|---|---|
| Histórico de conversa | Os **últimos 180 dias**, ou seja, cerca de 6 meses |
| Conversas de grupo | **Não são sincronizadas** |
| Arquivos de mídia | Os identificadores só vêm para mensagens dos **últimos 14 dias** |
| Prazo para disparar a sincronização | **24 horas** depois de conectar |
| Throughput do número | **20 mensagens por segundo**, contra 80 do número comum |

O prazo de 24 horas é o que mais pega gente desprevenida: se você conecta o número e deixa para sincronizar o histórico depois, perde a janela. A conta precisa ser desconectada e todo o fluxo de onboarding refeito.

Conversa de grupo não vir é o segundo. Se a sua operação usa grupos, essa parte continua existindo só no aparelho.

Depois que o número está conectado, o tráfego novo flui nos dois sentidos sem esses limites: o que chega no aplicativo aparece no webhook, o que sai pela API aparece no celular.

### A sincronização não acontece sozinha

Aqui está a parte que a documentação deixa implícita e que faz gente perder a janela de 24 horas achando que estava tudo automático. São três passos, e eles têm ordem:

**1. Marcar a opção no celular, durante a conexão.** No meio do fluxo, o aplicativo pergunta se você quer compartilhar o histórico de conversas. Se você não marcar, não tem como voltar atrás: *"se você por acidente marcar que não quer compartilhar, é só fazer o processo novamente"*, ou seja, desconectar e reconectar o número.

**2. Assinar o evento de sincronização antes de pedir.** Existe um campo de webhook próprio para isso, e é por ele que os contatos e as conversas chegam. Se ele não estiver marcado, você faz a chamada, recebe confirmação de sucesso, e nada aparece.

**3. Fazer a chamada que dispara.** ([o passo a passo completo está aqui](/sincronizar-contatos-api-oficial-whatsapp)) É esse passo que quase todo mundo não sabe que existe. Nas palavras do Israel: *"você conectou o telefone, com webhook, tá marcado, agora tem que avisar a meta que você quer os contatos."* Contatos e histórico são pedidos separadamente, no corpo da requisição.

E o comportamento da resposta é diferente para os dois, o que evita depuração inútil: **os contatos chegam praticamente na hora, e as conversas demoram bastante mais.** A Meta não crava um prazo, e diz que a sincronização pode levar vários minutos dependendo do tamanho do histórico, da conexão e da velocidade com que você consome os webhooks. Na operação, a espera do histórico é da ordem de dezenas de minutos.

Isso importa por um motivo: quem pede o histórico, não vê nada em dois minutos e conclui que falhou, refaz o processo sem necessidade e às vezes queima a janela de 24 horas fazendo isso.

::video: HQm5UuW50bM | Quatro minutos exatos sobre isso: em 00:30 ele marca o evento, em 01:05 explica o prazo de 24 horas, em 02:38 dispara a sincronização e os contatos aparecem no webhook na hora, e em 03:40 mostra a diferença de tempo do histórico.

Uma dica que sai daí e vale guardar: **salve o identificador que a chamada de sincronização devolve.** Se algo der errado, é com ele que você abre suporte com a Meta.

## Outros detalhes de comportamento

1. **Duplicidade**: se você enviar a mesma mensagem duas vezes pela API, ela aparece duas vezes no aplicativo. Não existe deduplicação automática, o controle é seu.
2. **Resposta a mensagem específica**: funciona nos dois sentidos. O que você responde no aplicativo chega ao webhook como resposta, e vice-versa.
3. **Status de entrega**: enviado, entregue e lido ficam iguais nos dois lados.
4. **Quem escreve pelo aplicativo não abre janela de atendimento.** Mensagem enviada pelo aplicativo do WhatsApp Business não abre nem estende a janela de 24 horas da API. Vale a pena saber disso antes de montar automação em cima de janela.

## Desconectar só dá pelo celular

Detalhe operacional pequeno e de consequência grande, que não aparece em comparativo nenhum: **não existe endpoint para desconectar o número da API.** A desconexão é feita no aparelho, nas configurações do WhatsApp Business, em conta e plataforma do WhatsApp Business.

Isso importa em dois momentos. Se você constrói produto e o seu cliente conecta o número dele, **você não consegue desconectar por ele**: o botão está no celular dele, e o seu fluxo de cancelamento precisa levar isso em conta. E se você precisa refazer a conexão para recuperar a janela de sincronização, o passo depende de alguém com o telefone na mão.

## O que a conexão exige, e o que não exige

Vale desfazer duas expectativas erradas que aparecem sempre, porque as duas fazem gente desistir antes de tentar.

**Precisa de portfólio empresarial, e ele não precisa ser verificado.** Basta existir. Verificado é melhor e não é requisito para conectar: *"não precisa ser verificado, se for verificado é melhor, mas apenas criar o portfólio já é suficiente."*

**A forma de pagamento fica na Meta, não no provedor.** As mensagens são cobradas pela Meta, direto no cartão cadastrado no portfólio, e é isso que você precisa configurar antes de enviar template. O provedor cobra o acesso, não a mensagem. Sem cartão no portfólio, a mensagem de serviço funciona e o template não sai.

::video: 8xA-8z1YW98 | Nove minutos do zero: em 02:34 aparece a escolha entre chip novo e aplicativo existente, que é a decisão que define se você está em coexistência, e em 08:33 ele mostra onde fica a configuração de pagamento dentro do portfólio.

## O requisito do lado do provedor

A Meta exige que quem oferece coexistência seja **Solution Partner ou Tech Provider**. Não é um recurso que qualquer integração consegue habilitar: depende do App Review aprovado com as permissões `whatsapp_business_messaging` e `whatsapp_business_management`.

Isso significa que a escolha do provedor decide se você tem o recurso. Se você for direto na Meta por conta própria, precisa passar por esse processo você mesmo.

## Comparação: Chatwoot + coexistência vs WhatsApp Web

Chatwoot já oferece inbox centralizado (vários agentes veem conversa). Coexistência é diferente: é você no celular vendo e respondendo direto.

| Aspecto | Chatwoot | App + coexistência |
|---|---|---|
| **Inbox visual** | Sim, inbox centralizado | Não, só app nativo |
| **Múltiplos agentes** | Sim, 5+ veem mesmo chat | Não, só quem abrir app |
| **Sincronização** | Sim, com webhooks | Sim, com API |
| **Setup** | Médio | Zero, automático |
| **Automação** | Sim, regras e bots | Parcial, webhook só |
| **Quando usar** | Suporte com equipe | Suporte informal, 1 pessoa |

Use Chatwoot se: você tem equipe.

Use app + coexistência se: você é solo ou está em reunião e quer responder pessoalmente.

## Monitorar coexistência

Datafy oferece dashboard mostrando:

- Última sincronização do app
- Mensagens recebidas (via app vs via webhook)
- Taxa de entrega
- Webhooks falhando

Se webhook não funciona, app ainda recebe (porque é direto). Mas sua automação quebra.

Monitora webhook com frequência (de dia em dia).

## Perguntas frequentes

### Se webhook cair, app ainda funciona?

Sim. Webhook e app são dois caminhos independentes. Webhook cai, app continua recebendo e mostrando conversa. Sua automação fica quebrada, mas você consegue responder pelo app.

### Posso rodar número em 3 dispositivos API ao mesmo time?

Sim. Se você tem 3 servidores mandando mensagem (ambos via Datafy), todos funcionam. Meta deduplicação cliente se você mandar mensagem identica 3x.

### Se mando mensagem pelo app, quanto tempo demora a chegar no webhook?

Instantâneo, menos de 1 segundo.

### Coexistência funciona com grupo?

Não. Grupos não são suportados em Cloud API. Funciona só com chats 1-to-1.

### Se bloqueio alguém no app, webhook recebe?

Sim. Meta continua mandando webhook de "você bloqueou", sua aplicação vê que pessoa está bloqueada e para de mandar para ela.

## Como decidir: vou usar coexistência?

Simples: conecta em Datafy, já funciona. Não precisa de decisão. Está lá, use quando precisar.

[Teste 7 dias grátis em Datafy com coexistência já ativa](https://app.datafyapi.com.br)

## Leia também
- [API oficial vs não oficial](/api-oficial-vs-nao-oficial-whatsapp-2026)
- [Como receber mensagens no webhook](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [Chatwoot com API oficial](/whatsapp-api-oficial-chatwoot)
- [O que é Tech Provider](/o-que-e-tech-provider-meta)

---
title: "O que eu preciso para começar na API oficial do WhatsApp?"
description: "Business Manager, um número que não esteja em uso, o aparelho em mãos e forma de pagamento. O que muda entre ir direto na Meta ou por um provedor."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "o-que-preciso-para-comecar-na-api-oficial"
cluster: "oficial_vs_nao"
hero: "troca"
intent: "decidindo"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/solution-providers/get-started-for-tech-providers
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messaging-limits
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://app.datafyapi.com.br/docs
internal_links:
  - /api-oficial-vs-nao-oficial-whatsapp-2026
  - /migrar-para-api-oficial-sem-perder-o-numero
  - /posso-mandar-mensagem-para-qualquer-numero
  - /quanto-custa-whatsapp-business-api-brasil-2026
  - /cliente-conecta-o-whatsapp-dele-no-meu-saas
status: aprovado
---

# O que eu preciso para começar na API oficial do WhatsApp?

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** quatro coisas. Uma **Business Manager** onde você seja administrador, um **número que não esteja em uso** em outra conta de WhatsApp, o **aparelho com o chip em mãos** para receber o código de confirmação, e uma **forma de pagamento** cadastrada na Meta, porque sem ela o número conecta mas não envia.

O que mais varia é o caminho: indo direto na Meta você passa por App Review, com vídeo de demonstração e espera. Por um provedor, o número conecta em minutos, porque as permissões já estão aprovadas do lado dele.

::numeros: 4 itens|é tudo que você precisa levantar antes ;; 250|o limite inicial de conversas iniciadas por dia ;; 1 decisão|coexistência, que precisa ser tomada antes de conectar ;; 0|App Review, se você for por um provedor

## Principais pontos
- **Business Manager** é obrigatória. Se você não tem, dá para criar durante o processo, mas conte como mais um passo.
- **O número não pode estar ativo em outra conta de WhatsApp**, a menos que você use coexistência de propósito. Esse é o erro que mais trava gente logo no começo.
- **O aparelho precisa estar com você**: a Meta confirma a posse da linha por SMS ou ligação.
- **Forma de pagamento na Meta** não é detalhe: sem ela o envio não é liberado, e o sintoma é confuso, porque o número aparece conectado.
- Você começa com um **limite baixo de conversas iniciadas por dia**, e ele sobe conforme volume entregue com qualidade.

::diagrama: migration-seamless

## Os quatro itens, em detalhe

**1. Business Manager.** É a conta da empresa dentro da Meta, e é ali que o número fica registrado. Se você já anuncia no Facebook ou no Instagram, provavelmente já tem uma. Se não, dá para criar em minutos. Importante: **você precisa ser administrador**, não apenas ter acesso.

**2. Um número livre.** Um número já ativo no WhatsApp comum ou no WhatsApp Business não pode ser conectado direto: ou você o desvincula do aplicativo antes, ou usa o fluxo de **coexistência**, que permite manter os dois. Essa decisão precisa ser tomada **antes** de conectar, porque desfazer depois exige refazer todo o processo. Número novo, sem WhatsApp, é o caminho mais simples para testar.

**3. O aparelho com o chip.** A Meta manda um código para confirmar que a linha é sua, por SMS ou por ligação. Com coexistência há também a leitura de um código no aparelho. Não dá para pular, e não dá para fazer isso à distância se o chip está com outra pessoa.

**4. Forma de pagamento.** As mensagens são cobradas pela Meta, e sem método cadastrado o envio fica bloqueado. O sintoma engana: o número aparece conectado no painel, o token existe, e o envio falha. Vale deixar isso feito no mesmo dia da conexão.

## O que muda entre os dois caminhos

| | Direto na Meta | Por um provedor |
|---|---|---|
| Criar aplicativo na Meta | Você | Já existe |
| App Review com vídeo | Você passa | Já aprovado |
| Webhook | Você hospeda e mantém | Costuma vir pronto |
| Tempo até a primeira mensagem | Semanas | Minutos, com a conta já criada |
| Custo fixo | Nenhum | Mensalidade |
| Custo das mensagens | Tabela da Meta | Tabela da Meta, se não houver markup |

A conta das **mensagens é a mesma nos dois casos**, e é boa parte do custo. O que muda é quanto você paga para chegar até ela, e quanto tempo leva.

Ir direto faz sentido quando existe time de engenharia e o volume justifica. Por um provedor faz sentido quando o seu time é de produto, ou quando você precisa começar esta semana.

## O que não é obrigatório para começar

Vale desfazer três confusões comuns, porque elas fazem gente adiar o começo sem motivo:

**Verificação de empresa não é pré-requisito para enviar.** Ela existe para subir o limite de conversas iniciadas por dia. Dá para começar sem, com limite menor, e verificar depois.

**Site próprio não é exigido** para conectar. Uma política de privacidade publicada é boa prática e ajuda em outros pontos do processo, mas não é o que trava a primeira mensagem.

**Não é preciso ser Tech Provider.** Esse papel serve para quem oferece a plataforma a terceiros. Para usar no próprio negócio, basta conectar o seu número.

## Depois de conectar, o que muda no dia a dia

Três coisas surpreendem quem vem de ferramenta de QR code, e é melhor saber antes:

**A janela de 24 horas.** Fora dela, [só sai template aprovado](/posso-mandar-mensagem-para-qualquer-numero). Isso muda todo fluxo de reativação e de follow-up.

**Template precisa ser aprovado antes.** Não dá para escrever a mensagem na hora do disparo. Submeta os principais junto com a conexão, para não descobrir isso no dia da campanha.

**O limite começa baixo.** São 250 conversas iniciadas por dia no começo, e ele sobe com volume entregue e qualidade. Quem planejou disparar dez mil no primeiro dia precisa rever o plano.

## Perguntas frequentes

### Preciso de CNPJ?

Você precisa de uma Business Manager, que é uma conta empresarial da Meta. A verificação formal da empresa entra quando você quiser subir o limite de envio.

### Posso usar meu número pessoal?

Tecnicamente sim, se ele não estiver em uso em outra conta ou se você usar coexistência. Na prática não é boa ideia: o número passa a ser um ativo da operação, e misturar isso com o pessoal cria problema quando a equipe muda.

### Quanto tempo leva de verdade?

Por um provedor, com a conta já criada, o número conecta em minutos. O que consome tempo é o resto: aprovar templates, adaptar o código e testar. Planeje uma tarde, não cinco minutos.

### Posso testar antes de decidir?

Dá, e vale muito. Conecte um número de menor movimento, rode alguns dias, veja a qualidade no painel e sinta a janela de 24 horas na prática. É a melhor forma de descobrir se o seu fluxo cabe nas regras.

### E se eu já uso uma ferramenta de QR code?

Aí o processo é um pouco diferente, porque **o seu número ainda não está registrado na Meta**. A migração cria esse registro pela primeira vez, e tem [um passo a passo próprio](/migrar-para-api-oficial-sem-perder-o-numero).

### Consigo conectar vários números?

Consegue. Cada número é uma conexão, com token e limite próprios, e todos podem ficar na mesma Business Manager.

## Como decidir

Se você quer só entender como funciona, conecte um número novo por um provedor e mande a primeira mensagem hoje. Custa pouco e ensina mais que qualquer documentação.

Se você já sabe o que quer e tem time de engenharia, avalie ir direto na Meta: sai mais barato em escala, ao custo do App Review e da infraestrutura de webhook.

E se o seu produto vai conectar números de clientes, a pergunta muda de figura: aí o que importa é [se o cliente consegue conectar sozinho](/cliente-conecta-o-whatsapp-dele-no-meu-saas), e isso depende do papel do seu fornecedor na Meta.

::cta: Comece por um número de teste, não pelo principal | Conecte um número de menor movimento e rode alguns dias com ele. A janela de 24 horas e a aprovação de template são coisas que você entende melhor operando do que lendo.

## Leia também
- [API oficial vs não oficial do WhatsApp](/api-oficial-vs-nao-oficial-whatsapp-2026)
- [Migrar para API oficial sem perder o número](/migrar-para-api-oficial-sem-perder-o-numero)
- [Posso mandar mensagem para qualquer número?](/posso-mandar-mensagem-para-qualquer-numero)
- [Meu cliente conecta o WhatsApp dele sozinho no meu SaaS?](/cliente-conecta-o-whatsapp-dele-no-meu-saas)

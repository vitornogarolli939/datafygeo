---
title: "O cliente pediu para apagar os dados dele. Onde o dado está?"
description: "O banco principal é a parte fácil. O que costuma sobrar é índice de busca, fila, log de monitoramento e backup, e cada um pede uma solução diferente."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "o-cliente-pediu-para-apagar-os-dados-dele"
cluster: "compliance"
hero: "camadas"
intent: "problema-urgente"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/data-privacy-and-security/
  - https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://platform.claude.com/docs/en/manage-claude/api-and-data-retention
  - https://developers.openai.com/api/docs/guides/your-data
  - https://www.youtube.com/watch?v=LIT4FxgqHhE
  - https://www.youtube.com/watch?v=ZHYNjpu5ReE
videos: [LIT4FxgqHhE, ZHYNjpu5ReE]
internal_links:
  - /como-leio-o-historico-de-conversa-pela-api
  - /posso-mandar-a-conversa-do-cliente-para-a-openai
  - /o-telefone-esta-sumindo-do-webhook
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /quanto-custa-rodar-um-agente-de-ia-no-whatsapp
status: aprovado
pendencias: ["[VERIFICAR] prazos de resposta a titular e de comunicação de incidente devem ser confirmados na norma vigente antes de virarem procedimento interno"]
---

# O cliente pediu para apagar os dados dele. Onde o dado está?

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** o banco principal é a parte fácil, e é onde quase todo mundo para. O que costuma sobrar é o que ninguém lembra: **índice de busca, fila de processamento, log de monitoramento, backup** e, se você usa IA, o que passou pelo provedor de modelo.

Este texto é escrito por quem opera infraestrutura. Serve para você mapear onde o dado está e saber o que perguntar ao seu jurídico, não para substituí-lo.

::numeros: 6 lugares|onde o dado costuma estar, e só um é o banco ;; 30 dias|o que a Meta guarda, e apaga sozinha ;; 1 chave|que precisa ser a mesma em todos os sistemas ;; backup|o único que não dá para apagar linha a linha

## Principais pontos
- Antes de apagar, você precisa **saber onde está**. E o dado de uma conversa de WhatsApp costuma estar em mais lugares do que o time imagina.
- Use **uma chave só** para achar a pessoa em todos os sistemas. Sem isso, o pedido vira uma caçada manual que ninguém consegue provar depois.
- **A Meta apaga sozinha**, em cerca de 30 dias. Essa parte não é sua, e vale explicar isso na resposta ao titular.
- **Backup não se apaga linha a linha.** A saída honesta é criptografia por pessoa: destruir a chave torna o dado irrecuperável sem restaurar backup nenhum.
- Deixe **registro do que foi feito**, por sistema. É isso que você mostra se alguém perguntar.

::diagrama: tech-provider-badge

## Onde o dado está, na prática

| Onde | O que tem | Você controla? |
|---|---|---|
| Seu banco | Mensagem, contato, chamado | Sim |
| **Índice de busca ou base de vetores** | Trechos da conversa, gerados para busca | Sim, e é o mais esquecido |
| **Fila e mensagens com erro** | Payload cru parado há semanas | Sim |
| **Log de aplicação e monitoramento** | Payload inteiro, prompt, resposta | Sim |
| **Backup e ponto de recuperação** | Tudo, e imutável por natureza | Sim, com técnica diferente |
| Provedor de modelo de IA | Prompt e resposta | Não |
| Meta | Mensagem e mídia | Não, e ela apaga sozinha |

Os quatro do meio são os que aparecem em auditoria e não apareceram no plano. Vale conferir cada um antes de responder ao titular que está tudo apagado.

## A peça que faz isso funcionar: uma chave só

Se cada sistema identifica a pessoa de um jeito, o pedido de exclusão vira busca manual, e você não consegue provar que terminou.

A solução é ter **um identificador único e determinístico** derivado do contato, gravado em todos os sistemas: banco, índice de busca, fila, log. Não precisa ser o telefone, e há uma boa razão para não ser: além de virar dado pessoal espalhado por todo lugar, [o telefone pode nem vir no webhook](/o-telefone-esta-sumindo-do-webhook) se você não falou com a pessoa há mais de 30 dias.

Um caminho comum é gerar essa chave a partir do contato com uma função de hash com segredo, e usar sempre ela. O telefone fica em um lugar só, e o resto do sistema referencia a chave.

## Cada lugar pede uma técnica

**Banco:** apagar ou anonimizar as linhas. A parte simples, e a única que a maioria faz.

**Índice de busca ou base de vetores:** guarde a ligação entre o trecho indexado e a pessoa. Sem isso, você não sabe quais entradas apagar. Apague o vetor **e** o texto original guardado junto, porque muita gente esquece o segundo.

**Fila e mensagens com erro:** payload cru parado ali é dado pessoal esquecido. Uma política de expiração curta resolve a maior parte antes de virar problema.

**Log:** o melhor tratamento é não ter o dado ali. Remova informação pessoal **na origem**, antes de escrever o log, e mantenha retenção curta. É muito mais barato que caçar depois.

**Backup:** aqui não dá para apagar uma linha. A saída honesta é **criptografia por pessoa**: cada titular tem uma chave própria, guardada num cofre. Apagar significa destruir a chave. O backup continua existindo, e o conteúdo daquela pessoa fica irrecuperável. É o que permite responder "foi eliminado" sem restaurar backup de doze meses.

**Provedor de modelo:** você não apaga pontualmente. O que você faz é **documentar**: qual provedor, qual a política de retenção, e informar isso ao titular. Vale checar duas coisas antes: alguns recursos de armazenamento de estado ficam fora do modo sem retenção e guardam até exclusão manual, e alguns modelos exigem retenção mínima. Se você usa qualquer um dos dois, tem dado parado lá que precisa entrar no seu inventário.

**Meta:** não há endpoint de exclusão por pessoa. A retenção é temporal, cerca de 30 dias, e a plataforma apaga sozinha. Essa é uma resposta legítima a dar ao titular, com o link da documentação.

## Deixe registro

Uma tabela simples com uma linha por sistema e por pedido:

```sql
CREATE TABLE pedidos_de_exclusao (
  pedido_id     uuid,
  sistema       text,        -- banco | vetores | fila | log | backup | modelo | ...
  situacao      text,        -- pendente | concluido | nao_se_aplica
  evidencia     text,
  concluido_em  timestamptz
);
```

Sem isso, "apagamos tudo" é uma afirmação que ninguém consegue sustentar seis meses depois, quando quem executou já saiu da empresa.

## Os prazos que trabalham a seu favor

Uma parte do inventário se resolve pelo tempo, e conhecer os prazos evita prometer o que você não controla e evita procurar dado onde ele já não está.

| Onde | Prazo |
|---|---|
| Mensagem em trânsito na Meta | Não é armazenada para consulta posterior pela API |
| Mídia recebida, pelo identificador do webhook | **7 dias** |
| Mídia que você subiu para enviar | **30 dias** |
| Log de mensagens do painel da Datafy | **7 dias**, e no máximo **100 mensagens por conversa** |
| Seu banco de dados | O que você definir, e é o único que você controla de verdade |

A leitura prática disso: **quase todo o dado que você precisa apagar está no seu lado.** A cópia que a plataforma tem é curta e rotativa, e a Meta não é um arquivo que você consulte.

E o inverso também vale, e é o erro mais comum na direção oposta: se você **não** baixou a mídia, o identificador expira em **7 dias** e o arquivo sai do seu alcance, e aí um pedido de acesso aos próprios dados não tem o que entregar. Retenção curta ajuda no apagamento e atrapalha no acesso, e é você que decide qual dos dois quer, por tipo de dado.

::video: LIT4FxgqHhE | Três minutos mostrando o log ao vivo, e em 02:57 os prazos de retenção ditos com clareza. Vale ver junto com o vídeo de mídias, que em 03:53 dá o prazo do arquivo recebido.

## Três coisas que costumam ser confundidas

**Apagar não é a única opção.** O pedido pode ser de anonimização ou de bloqueio, que são coisas diferentes com efeitos diferentes. Vale ter campos separados no seu modelo, e não tratar tudo como exclusão.

**Nem todo dado é apagável a pedido.** Existem hipóteses em que a guarda é exigida ou legítima, e a decisão sobre isso é jurídica, não de engenharia. O que cabe a você é saber onde o dado está e conseguir apagar quando a decisão for essa.

**Pseudonimizar não é anonimizar.** Trocar o telefone por um código reduz risco, mas o dado continua sendo pessoal se houver como voltar atrás. Isso muda o enquadramento do que você pode dizer ao titular.

## Perguntas frequentes

### Preciso apagar da Meta também?

Não há endpoint para isso, e ela apaga sozinha em cerca de 30 dias. Informe isso ao titular com o link da documentação.

### E o que já foi para o modelo de IA?

Você não apaga pontualmente. Documente o provedor, a região e a política de retenção. Se você usa recursos que guardam estado, isso precisa entrar no inventário, porque aí a retenção deixa de ser curta.

### Quanto tempo tenho para responder?

Existe prazo legal, e há uma resolução que dá prazo em dobro para agente de pequeno porte, o que provavelmente inclui micro-SaaS. Confirme a norma vigente antes de transformar isso em procedimento, e defina um prazo interno menor que o externo.

### E se o dado estiver em backup de doze meses?

É exatamente o caso da criptografia por pessoa. Sem ela, a única saída honesta é dizer que o dado permanece em backup até a expiração natural, o que costuma ser resposta ruim.

### Meu fornecedor guarda cópia?

Provavelmente. Pergunte por quanto tempo e como pedir exclusão. Isso precisa estar no contrato, e não descoberto no dia do pedido.

### Isso vale para conversa de WhatsApp mesmo?

Vale para qualquer dado pessoal, e conversa é dado pessoal. Aliás, costuma ser o mais sensível que uma empresa pequena guarda, porque tem nome, telefone, endereço e às vezes documento, tudo no texto corrido.

## Como decidir

Se você está começando, resolva a chave única agora: é barato e é o que torna tudo o resto possível. Se já está rodando, faça o inventário antes de o primeiro pedido chegar, porque descobrir onde o dado está com o relógio correndo é a pior hora.

E leve o inventário ao seu jurídico. A pergunta que ele vai fazer é onde o dado está e o que dá para apagar. Chegar com essa resposta pronta encurta a conversa e evita promessa que a engenharia não consegue cumprir.

::cta: Faça o inventário antes do primeiro pedido | Liste os seis lugares, marque quais você consegue apagar hoje e quais não. A lista dos que não dá é o seu plano de trabalho, e ela é curta.

## Leia também
- [Como leio o histórico de conversa pela API](/como-leio-o-historico-de-conversa-pela-api)
- [Posso mandar a conversa do meu cliente para a OpenAI?](/posso-mandar-a-conversa-do-cliente-para-a-openai)
- [O telefone está sumindo do webhook](/o-telefone-esta-sumindo-do-webhook)
- [Webhook: receber mensagens em tempo real](/webhook-whatsapp-cloud-api-como-receber-mensagens)

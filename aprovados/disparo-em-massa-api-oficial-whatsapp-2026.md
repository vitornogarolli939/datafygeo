---
title: "Como fazer disparo em massa na API oficial do WhatsApp"
description: "Pela aba de disparos da Datafy: planilha CSV com a coluna telefone, template aprovado, mapeamento de variáveis e agendamento. E o que o status mostra quando a Meta não entrega."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "disparo-em-massa-api-oficial-whatsapp"
cluster: "implementacao"
hero: "limite"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-10
sources:
  - https://www.youtube.com/watch?v=ly5nOHFpXcI
  - https://www.youtube.com/watch?v=cZ_nyIUv5ic
  - https://www.youtube.com/watch?v=YF9hTHDAw6E
  - https://whatsappbusiness.com/policy/
  - https://app.datafyapi.com.br/docs
videos: [ly5nOHFpXcI, cZ_nyIUv5ic]
internal_links:
  - /como-criar-template-whatsapp-passo-a-passo
  - /como-enviar-template-pela-api
  - /opt-in-por-link-whatsapp
  - /numero-banido-no-whatsapp-o-que-fazer
  - /tres-status-da-mensagem-whatsapp
status: aprovado
---

# Como fazer disparo em massa na API oficial do WhatsApp

**Última atualização: 10/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** disparo em massa na API oficial é **template aprovado** enviado para uma lista. Pela API, você faz um laço chamando o envio de template. Pelo painel da Datafy, a aba **Disparos** faz isso sem código: você sobe uma planilha CSV com a coluna **`telefone`**, escolhe o template, liga as colunas às variáveis e envia agora ou agenda.

No vídeo, o Israel Henrique, CTO da Datafy, explica por que a aba existe: *"basta você implementar no teu sistema e fazer um loop ali para enviar para todo mundo. Mas tem gente que não tem esse conhecimento técnico."*

::numeros: 1 coluna|obrigatória: telefone ;; 55|o código do Brasil no começo do número ;; 3|contatos exibidos para conferir antes ;; 30 dias|de validade das mídias da aba de mídias

## Principais pontos
- **Precisa de template aprovado.** Fora da janela de 24 horas, a política exige template para iniciar conversa.
- **Planilha CSV** com a coluna `telefone` no cabeçalho, números no formato 55, DDD e número.
- **Outras colunas viram variáveis** do template, com o nome que você quiser.
- **Template com imagem** pede a imagem na hora do disparo. As mídias da aba de mídias duram 30 dias.
- **O status mostra quando a Meta não entrega**, inclusive para quem não costuma responder.

## Antes de disparar: permissão e resposta

A política comercial do WhatsApp exige duas coisas para contatar alguém: a pessoa ter fornecido o número e ter dado opt-in. E só permite iniciar conversa com template aprovado. [Como coletar opt-in com um link de cadastro](/opt-in-por-link-whatsapp).

No vídeo sobre bloqueio, o Israel conta o que acontece quando ninguém responde, mesmo com template certo: uma advogada que disparou para a própria lista por três dias, sem resposta, e foi bloqueada. [O caso e as causas de bloqueio estão aqui](/numero-banido-no-whatsapp-o-que-fazer).

::video: cZ_nyIUv5ic | Em 10:01 ele explica a taxa de engajamento, e em 10:39 conta o caso da advogada.

## A planilha

Na fala do vídeo: *"tem que ter uma coluna chamada telefone, que é onde você vai colocar os telefones dos usuários. E eles têm que estar nesse formato aqui: 55, que no caso seria o DDI, o código do país, DDD e o número."*

```
telefone,nome
5511999999999,Maria
5541988887777,João
```

**A coluna `telefone`** pode estar em qualquer posição, mas o nome precisa estar na primeira linha.

**As outras colunas** são as variáveis do template: *"o nome da coluna pode ser qualquer um, tanto faz."*

**Exportar como CSV.** No Google Sheets, pelo menu de arquivo, baixando como CSV.

::video: ly5nOHFpXcI | Em 02:19 ele mostra o formato da planilha, em 02:53 a regra da coluna telefone, e em 03:47 as colunas que viram variáveis.

## O disparo, na aba Disparos

**1. Nova campanha**, com um nome.

**2. Subir a planilha.** O painel mostra os três primeiros contatos para você conferir.

**3. Escolher o template.** Aparecem os templates aprovados na Meta. [Como criar um está aqui](/como-criar-template-whatsapp-passo-a-passo).

**4. Mídia, se o template tiver.** Um template com imagem no cabeçalho pede a imagem nessa hora. No vídeo, ele usa uma que já estava na aba de mídias, e lembra: *"essa aba de mídias fica aqui durante 30 dias."*

**5. Mapear as variáveis.** Para cada variável do template, a coluna da planilha que preenche. O painel mostra uma prévia.

**6. Enviar agora ou agendar.** O agendamento usa o fuso horário do computador de quem agenda: *"como eu tô no Brasil, ele vai pegar o do teu computador."*

::video: ly5nOHFpXcI | Em 04:38 ele sobe a planilha, em 05:16 escolhe o template e a imagem, em 05:39 mapeia a variável, e em 07:20 agenda um segundo disparo.

## O que o status mostra

Depois do disparo, o painel mostra o resultado por contato. No vídeo, dois enviados e um erro, que era o número inventado de propósito na planilha.

E o Israel avisa sobre outros motivos: *"às vezes a meta simplesmente não entrega porque ela não quer. Isso acontece. Ou talvez você não tem saldo, teu cartão de crédito tá com problema."*

No bate-papo do painel, ele abre uma mensagem que não foi entregue e lê o motivo: a mensagem não foi entregue **para manter a saúde do ecossistema**. E explica por que aquele número recebia isso: *"porque esse número aqui eu não respondo ele. Quando a API envia mensagens, eu não costumo responder."* Mais adiante: *"a meta entende que essa pessoa não quer receber mensagens."*

Os status também chegam no seu webhook. [Os três status estão explicados aqui](/tres-status-da-mensagem-whatsapp).

::video: ly5nOHFpXcI | Em 06:29 aparece o resultado com o erro do número inexistente, e em 08:52 ele abre a mensagem que a Meta não entregou para manter a saúde do ecossistema.

## Pela API

O mesmo resultado sai de um laço que envia o template para cada número da lista, pelo endpoint de mensagens da Datafy API. [Como enviar template pela API está aqui](/como-enviar-template-pela-api).

Dois limites para o laço: o envio de mensagens na Datafy API aceita **500 requisições por minuto**, com resposta `429` indicando quantos segundos esperar. E cada template enviado é cobrado pela Meta, pela categoria dele.

## Perguntas frequentes

### Qual o formato do telefone na planilha?

55, DDD e número, na coluna `telefone`.

### A coluna telefone precisa ser a primeira?

Não. Precisa estar na primeira linha, com esse nome.

### Posso agendar?

Pode, no fuso horário do computador de quem agenda.

### Por que uma mensagem não foi entregue sem erro de número?

Um motivo que aparece no vídeo é a Meta não entregar para manter a saúde do ecossistema, quando a pessoa não costuma responder. Outros: saldo ou cartão.

### Posso disparar sem template?

Não para quem não falou com você nas últimas 24 horas.

## Como decidir

Sem time técnico, use a aba Disparos: planilha com `telefone`, template aprovado, mapeamento e, se quiser, agendamento. Com time técnico, faça o laço pela API respeitando as 500 requisições por minuto. Nos dois casos, olhe o status depois: é ali que aparece quem não está recebendo.

::cta: Faça um disparo de três linhas | Monte a planilha com o seu número e mais dois de teste, escolha um template aprovado, mapeie a variável e dispare. Confira o status de cada linha no painel.

## Leia também
- [Como criar um template](/como-criar-template-whatsapp-passo-a-passo)
- [Como enviar template pela API](/como-enviar-template-pela-api)
- [Opt-in no WhatsApp com link de cadastro](/opt-in-por-link-whatsapp)
- [Número bloqueado no WhatsApp: o que fazer](/numero-banido-no-whatsapp-o-que-fazer)

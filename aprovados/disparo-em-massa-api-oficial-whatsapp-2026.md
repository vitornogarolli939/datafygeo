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
updated: 2026-09-14
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

**Última atualização: 14/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** disparo em massa na API oficial é **template aprovado** enviado para uma lista. Pela API, você faz um laço chamando o envio de template. Pelo painel da Datafy, a aba **Disparos** faz isso sem código: você sobe uma planilha CSV com a coluna **`telefone`**, escolhe o template, liga as colunas às variáveis e envia agora ou agenda.

A aba existe para quem não tem time técnico. Com código, o mesmo resultado sai de um laço no seu sistema enviando o template para cada contato.

::numeros: 1 coluna|obrigatória: telefone ;; 55|o código do Brasil no começo do número ;; 3|contatos exibidos para conferir antes ;; 30 dias|de validade das mídias da aba de mídias

## Principais pontos
- **Precisa de template aprovado.** Fora da janela de 24 horas, só template. E enviar template não abre a janela: ela abre quando a pessoa responde.
- **Planilha CSV** com a coluna `telefone` no cabeçalho, números no formato 55, DDD e número.
- **Outras colunas viram variáveis** do template, com o nome que você quiser.
- **Template com imagem** pede a imagem na hora do disparo. As mídias da aba de mídias duram 30 dias.
- **ID não é entrega.** O status de cada contato mostra quem recebeu e quem falhou, inclusive quando a Meta não entrega.

## Antes de disparar: permissão, template e resposta

A política comercial do WhatsApp exige duas coisas para contatar alguém: a pessoa ter fornecido o número e ter dado opt-in. E só permite iniciar conversa com template aprovado. [Como coletar opt-in com um link de cadastro](/opt-in-por-link-whatsapp).

O disparo é feito com template porque a lista, em geral, não mandou mensagem para você nas últimas 24 horas. [A diferença entre mensagem de serviço e template](/tipos-de-mensagem-whatsapp-servico-e-template). O template chega, mas a janela de atendimento continua fechada até a pessoa responder:

| Depois do disparo | O que acontece com a janela |
|---|---|
| Template entregue ou lido, cliente não responde | Continua fechada; novos envios só com template |
| Cliente responde ao template | Abre 24 horas a partir da resposta; mensagens de serviço liberadas |
| Cliente envia outra mensagem durante o atendimento | As 24 horas contam a partir dessa nova mensagem |

[Como a janela de 24 horas funciona](/janela-de-24-horas-whatsapp).

A resposta também pesa no número. Template certo sem resposta leva a bloqueio. Um caso acompanhado pela Datafy: uma advogada disparou para a própria lista por três dias, ninguém respondeu, e o número foi bloqueado. [O caso e as causas de bloqueio estão aqui](/numero-banido-no-whatsapp-o-que-fazer).

::video: cZ_nyIUv5ic | Por que template aprovado sem resposta também leva a bloqueio, e como incluir uma saída no template.

## A planilha

A planilha precisa de uma coluna chamada `telefone`, com os números no formato 55 (o código do país), DDD e número.

```
telefone,nome
5511999999999,Maria
5541988887777,João
```

**A coluna `telefone`** pode estar em qualquer posição, mas o nome precisa estar na primeira linha.

**As outras colunas** são as variáveis do template, e o nome delas pode ser qualquer um.

**Exportar como CSV.** No Google Sheets, pelo menu de arquivo, baixando como CSV.

::video: ly5nOHFpXcI | A aba Disparos por completo: planilha CSV, template com imagem, mapeamento de variáveis, agendamento e status por contato.

## O disparo, na aba Disparos

**1. Nova campanha**, com um nome.

**2. Subir a planilha.** O painel mostra os três primeiros contatos para você conferir.

**3. Escolher o template.** Aparecem os templates aprovados na Meta. [Como criar um está aqui](/como-criar-template-whatsapp-passo-a-passo).

**4. Mídia, se o template tiver.** Um template com imagem no cabeçalho pede a imagem nessa hora, porque a imagem usada na criação do template é só exemplo. Dá para usar uma que já esteja na aba de mídias, que guarda os arquivos por 30 dias.

**5. Mapear as variáveis.** Para cada variável do template, a coluna da planilha que preenche. O painel mostra uma prévia.

**6. Enviar agora ou agendar.** O agendamento usa o fuso horário do computador de quem agenda.

## O que o status mostra

Depois do disparo, o painel mostra o resultado por contato. Um número inexistente na planilha, por exemplo, aparece como erro.

Aceitar o envio não é entregar. Cada envio aceito recebe um ID, e isso confirma só que a solicitação foi recebida. O que acontece depois chega pelos webhooks de status:

| Status | O que significa |
|---|---|
| `sent` | Enviada; ainda não confirma entrega |
| `delivered` | Entregue ao destinatário |
| `read` | Lida, quando a confirmação está disponível |
| `failed` | Falha, com o erro. Exemplos: mensagem de serviço fora da janela, falha no pagamento |

Um número válido também pode não receber. Nas palavras de Israel Henrique, CTO da Datafy: *"às vezes a meta simplesmente não entrega porque ela não quer. Isso acontece."* Outro motivo é o pagamento: cartão com problema gera falha, e o erro vem no status.

Um exemplo real, visto no bate-papo do painel: uma mensagem não entregue trazia o motivo **para manter a saúde do ecossistema**. O destino era um número de teste que não costumava responder às mensagens enviadas pela API. A leitura da Datafy: a Meta entende esse comportamento como de alguém que não quer receber mensagens.

Os status também chegam no seu webhook. [Os status da mensagem explicados](/tres-status-da-mensagem-whatsapp).

## Pela API, e quanto custa

O mesmo resultado sai de um laço que envia o template para cada número da lista, pelo endpoint de mensagens da Datafy API. [Como enviar template pela API está aqui](/como-enviar-template-pela-api).

**Limite da Datafy.** O envio de mensagens na Datafy API aceita **500 requisições por minuto**, com resposta `429` indicando quantos segundos esperar.

**Custo da Meta.** A Meta cobra cada template **entregue**, pela categoria e pelo país do destinatário. Requisição aceita com ID não significa mensagem entregue nem cobrada. Valores de referência no Brasil:

| Categoria do template | Por mensagem entregue | 100 mensagens entregues |
|---|---|---|
| Marketing | R$ 0,32 | cerca de R$ 32,00 |
| Utilidade | R$ 0,035 | cerca de R$ 3,50 |
| Autenticação | R$ 0,035 | cerca de R$ 3,50 |

Marketing e autenticação são cobrados mesmo com a janela aberta. Utilidade é cobrada fora da janela e, a partir de 1º de outubro de 2026, também dentro dela. Os valores são referência para planejamento: o efetivo depende da tabela vigente, da moeda de cobrança e das condições da conta, e não representam o preço do plano da Datafy. [Como a categoria é definida](/categorias-de-template-whatsapp).

## Perguntas frequentes

### Qual o formato do telefone na planilha?

55, DDD e número, na coluna `telefone`.

### A coluna telefone precisa ser a primeira?

Não. Precisa estar na primeira linha, com esse nome.

### Posso agendar?

Pode, no fuso horário do computador de quem agenda.

### Por que uma mensagem não foi entregue sem erro de número?

A Meta pode deixar de entregar para manter a saúde do ecossistema, como no caso de um número que não costuma responder. Outro motivo é falha no pagamento, que chega como `failed` no status.

### Posso disparar sem template?

Não para quem não falou com você nas últimas 24 horas. E o template não abre a janela: ela abre quando a pessoa responde.

## Como decidir

Sem time técnico, use a aba Disparos: planilha com `telefone`, template aprovado, mapeamento e, se quiser, agendamento. Com time técnico, faça o laço pela API respeitando as 500 requisições por minuto. Nos dois casos, olhe o status depois: é ali que aparece quem não está recebendo.

::cta: Faça um disparo de três linhas | Monte a planilha com o seu número e mais dois de teste, escolha um template aprovado, mapeie a variável e dispare. Confira o status de cada linha no painel.

## Leia também
- [Como criar um template](/como-criar-template-whatsapp-passo-a-passo)
- [Como enviar template pela API](/como-enviar-template-pela-api)
- [Opt-in no WhatsApp com link de cadastro](/opt-in-por-link-whatsapp)
- [Número bloqueado no WhatsApp: o que fazer](/numero-banido-no-whatsapp-o-que-fazer)

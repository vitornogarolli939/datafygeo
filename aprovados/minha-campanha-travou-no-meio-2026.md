---
title: "Disparei a campanha e ela travou no meio. O que aconteceu?"
description: "Quatro causas diferentes, e reenviar piora três delas. A mais nova é a Meta segurando os lotes de propósito para medir como as pessoas estão reagindo."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "minha-campanha-travou-no-meio"
cluster: "problemas"
hero: "fluxo"
intent: "problema-urgente"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messaging-limits
  - https://developers.facebook.com/docs/whatsapp/throughput
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/marketing-templates/per-user-limits
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-pausing/
  - https://app.datafyapi.com.br/docs
internal_links:
  - /quantas-mensagens-por-segundo-posso-enviar
  - /numero-banido-no-whatsapp-o-que-fazer
  - /posso-mandar-mensagem-para-qualquer-numero
  - /quanto-custa-whatsapp-business-api-brasil-2026
  - /webhook-chega-duplicado
status: aprovado
---

# Disparei a campanha e ela travou no meio. O que aconteceu?

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** existem **quatro causas diferentes** para a campanha parar no meio, e elas pedem reações opostas. Duas são limites seus, uma é a Meta segurando de propósito, e uma é o template sendo pausado por qualidade.

O que une as quatro: **reenviar imediatamente piora três delas.** É a reação natural, e é a errada.

::numeros: 4 causas|diferentes, com reações opostas ;; 130429|o código de estouro de throughput ;; 131049|o limite por pessoa, que não se contorna ;; 3 h|a primeira pausa de um template com qualidade baixa

## Principais pontos
- **Estouro de throughput** dá erro claro, o `130429`. Espere e reenvie com intervalo crescente.
- **Limite de envio da conta** é o total de conversas iniciadas por período. Desde outubro de 2025 ele é **do portfólio inteiro**, e não de cada número.
- **A Meta segura lotes de propósito** para medir reação no meio da campanha. Não é falha sua, e reenviar não adianta.
- **Limite por pessoa** é somado entre todas as empresas que falam com aquele indivíduo. **Não se contorna com mais número nem trocando de fornecedor**, e insistir escala para bloqueio da conta.
- **Template pausado por qualidade** para de enviar, com escalada de 3 horas, 6 horas e desativação.

::diagrama: n8n-fluxo

## Como identificar a sua causa

**Se você recebeu `130429`:** estouro de throughput. Você mandou rápido demais para o teto do número, que é 80 por segundo, ou 20 se ele estiver em coexistência. Solução: controlar a vazão da saída, com espera entre lotes.

**Se parou de uma vez, num número redondo:** provavelmente o limite de envio da conta. Ele é por período e por portfólio, e um número pode consumir a capacidade dos outros.

**Se foi ficando lenta, sem erro claro, e depois retomou:** é o mecanismo que a Meta usa para segurar entrega em lote. Ele existe desde dezembro de 2025 e atua no nível do portfólio: os primeiros lotes saem, a plataforma observa como as pessoas reagem, e os seguintes ficam retidos. Não é erro, é comportamento esperado, e **reenviar não acelera**.

**Se falhou só para algumas pessoas, com `131049`:** é o limite por usuário de mensagem de marketing. Ele é por pessoa, somado entre todas as empresas que mandam mensagem para ela, e a Meta não publica o número nem a janela.

**Se o template parou de enviar e os outros continuam:** ele foi pausado por qualidade. A escalada é 3 horas na primeira vez, 6 horas na segunda, e desativação na terceira.

## Os dois erros que parecem iguais e pedem o oposto

Esses dois merecem atenção especial porque tratá-los igual causa dano real:

| | `131049` | `131050` |
|---|---|---|
| O que é | Limite por pessoa, ou tentativa em excesso | A pessoa optou por não receber marketing |
| Você contorna? | Não. É somado entre empresas | Não. É escolha dela |
| O que fazer | Esperar pelo menos 24 h antes de tentar | Parar de enviar marketing para ela |
| O que NÃO fazer | **Reenviar na hora.** Escala para bloqueio da conta | Tentar por outro caminho |

Um laço de reenvio automático que não distingue os dois transforma um problema de entrega num problema de conta.

## Por que o limite por pessoa não se contorna

Vale insistir nesse ponto, porque a reação natural é errada.

O limite por pessoa é calculado **do lado do destinatário**, considerando o quanto ela lê de mensagem de marketing e o volume que já chega na caixa dela de todas as empresas. Ele não é publicado de propósito, é dinâmico, e varia por pessoa.

Isso significa que:

- **Mais números não ajudam.** O limite é da pessoa, não do seu número.
- **Trocar de fornecedor não ajuda.** Não é o fornecedor que está limitando.
- **Outra conta não ajuda.** É somado entre empresas, incluindo as suas.
- **Reenviar piora.** Tentativa em excesso tem penalidade própria, aplicada no nível da conta.

O que ajuda de verdade é do outro lado: mandar menos e melhor, para quem realmente quer receber. É chato ouvir isso quando a campanha está parada, mas é a única alavanca que existe.

## Como disparar sem travar

**Controle a vazão.** Não mande do laço direto. Fila com liberação em taxa constante, abaixo do teto.

**Mande em blocos, e observe.** Em vez de dez mil de uma vez, mande mil, veja entrega e reação, e continue. Isso reduz o risco de qualidade e evita o susto.

**Separe erro de limite de erro comum.** Um `130429` pede espera crescente. Um `131049` pede parar com aquela pessoa. Um erro de número inválido pede limpar a base. Tratar tudo como "falha, tenta de novo" é o que causa o dano maior.

**Olhe a qualidade antes.** Se o número está com a qualidade em queda, campanha grande é o pior momento para descobrir.

**Limpe a base.** Número inválido consome tentativa e piora indicador. Se a sua lista tem contato de anos atrás sem interação, ela vai custar mais que render.

## Perguntas frequentes

### Reenviar o que falhou é seguro?

Depende do erro. Para estouro de throughput, sim, com espera crescente. Para `131049`, não: espere pelo menos 24 horas para aquela pessoa. Para `131050`, nunca.

### Quanto tempo dura a retenção de lote?

Não há prazo publicado. O comportamento é a plataforma observar a reação e liberar os lotes seguintes conforme isso. Vale planejar campanha com folga em vez de contar com entrega imediata do volume todo.

### Meu template foi pausado. Perco as mensagens?

Os envios são recusados enquanto ele está pausado, e não são cobrados. Depois do prazo ele volta sozinho.

### Como subo meu limite de envio?

Entregando volume com qualidade ao longo do tempo, e completando a verificação da empresa. Não é um botão.

### Distribuir entre mais números resolve?

Para throughput, ajuda. Para o limite da conta, não, porque ele é do portfólio. Para o limite por pessoa, não resolve de jeito nenhum.

### Dá para saber quantas mensagens ainda posso mandar hoje?

Dá para consultar o limite de envio pela API. Atenção: o campo antigo foi descontinuado em favor de um novo, do nível do portfólio, e biblioteca desatualizada devolve valor errado.

## Como decidir

Se a sua campanha travou agora, comece pelo erro: ele diz qual das quatro causas é, e três delas você resolve mudando o jeito de disparar. Se não há erro claro e a coisa só ficou lenta, é a plataforma segurando, e a resposta é esperar.

Para a próxima, mude o desenho: bloco menor, vazão controlada, tratamento por tipo de erro e base limpa. Campanha que sai devagar e inteira entrega mais que campanha que sai rápido e trava na metade.

::cta: Antes do próximo disparo, separe três erros | 130429 pede espera crescente. 131049 pede parar com aquela pessoa por 24 horas. 131050 pede parar de vez. Um laço que trata os três igual transforma problema de entrega em problema de conta.

## Leia também
- [Quantas mensagens por segundo posso enviar?](/quantas-mensagens-por-segundo-posso-enviar)
- [Número banido: o que fazer](/numero-banido-no-whatsapp-o-que-fazer)
- [Posso mandar mensagem para qualquer número?](/posso-mandar-mensagem-para-qualquer-numero)
- [Quanto custa a WhatsApp Business API no Brasil](/quanto-custa-whatsapp-business-api-brasil-2026)

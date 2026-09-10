---
title: "Quanto custa rodar um agente de IA no WhatsApp?"
description: "São três contas somadas por turno de conversa, e quase todo orçamento esquece uma. A partir de outubro, responder dentro da janela também passa a custar."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "quanto-custa-rodar-um-agente-de-ia-no-whatsapp"
cluster: "custo"
hero: "preco"
intent: "decidindo"
persona: "saas, automacao, agentes"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/ai-providers
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing
  - https://developers.facebook.com/docs/whatsapp/throughput
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=Bev4VxTJ5Cg
  - https://www.youtube.com/watch?v=JL9Qzw3oS5A
videos: [JL9Qzw3oS5A, Bev4VxTJ5Cg]
internal_links:
  - /cobranca-de-ai-provider-no-brasil
  - /mensagem-de-servico-vai-ser-paga-outubro-2026
  - /quanto-custa-whatsapp-business-api-brasil-2026
  - /quantas-mensagens-por-segundo-posso-enviar
  - /posso-mandar-a-conversa-do-cliente-para-a-openai
status: aprovado
---

# Quanto custa rodar um agente de IA no WhatsApp?

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** são **três contas somadas, por turno de conversa**. O token do modelo, a mensagem da Meta, e, se a política de provedores de IA se aplicar a você, uma cobrança adicional por mensagem livre. Orçamento que soma por conversa, e não por turno, erra nas três.

E tem uma data no meio: a partir de **1º de outubro de 2026** responder dentro da janela de 24 horas deixa de ser gratuito. Para um agente, que vive de responder dentro da janela, essa é a linha que mais muda.

::numeros: 3 contas|somadas a cada turno, não a cada conversa ;; 1 out 2026|quando responder dentro da janela passa a custar ;; 1 a cada 6 s|o limite por contato, que também limita quantas mensagens você quebra ;; turno|é a unidade de custo, não a conversa

## Principais pontos
- **Conte por turno.** Uma conversa de dez idas e vindas gera dez cobranças de mensagem, não uma.
- **Conta 1, o modelo.** Cresce com o histórico que você manda junto: contexto que só aumenta é a causa mais comum de custo que sobe sem o uso subir.
- **Conta 2, a mensagem.** Hoje a resposta dentro da janela é gratuita. A partir de outubro, não.
- **Conta 3, a política de provedores de IA.** No Brasil ela continua valendo, depois de ter sido revogada na Europa em maio de 2026. Se ela se aplica ao seu caso, cada mensagem livre tem custo próprio.
- **Quebrar a resposta em vários balões multiplica a conta 2 e a 3**, e ainda se aproxima do limite por par entre você e aquele destinatário.

::diagrama: preço-comparacao

## Conta 1: o modelo

É a que todo mundo lembra, e a mais fácil de estimar mal.

O custo por chamada depende de quanto texto entra e quanto sai. O que engana é o **histórico**: se a cada turno você reenvia a conversa inteira para o modelo lembrar do contexto, a entrada cresce a cada mensagem. Uma conversa longa fica progressivamente mais cara, mesmo que as respostas sejam curtas.

Três hábitos que seguram isso:

**Resumir em vez de reenviar.** Depois de alguns turnos, troque o histórico literal por um resumo curto do que já foi resolvido.

**Cortar o que não serve.** Nem toda conversa precisa de todo o passado. Pedido em andamento precisa do pedido, não da saudação inicial.

**Escolher o modelo por tarefa.** Classificar intenção não exige o mesmo modelo que redigir uma resposta delicada.

## Conta 2: a mensagem da Meta

Aqui está a mudança que atinge todo agente.

**Hoje:** a resposta em texto livre dentro da janela de 24 horas é gratuita. Se o cliente escreveu, você responde à vontade sem custo de mensagem.

**A partir de 1º de outubro de 2026:** essa resposta passa a ser cobrada, ao mesmo preço de utilidade e autenticação, por mercado. A mensagem de utilidade enviada dentro da janela também.

Para um agente, isso vira custo por turno. Uma conversa de oito trocas, que hoje custa só o modelo, passa a custar o modelo mais oito mensagens.

Como referência de ordem de grandeza no Brasil, utilidade e autenticação vinham na faixa de R$ 0,03 a R$ 0,04 por mensagem em setembro de 2026. [Confirme na tabela oficial](/quanto-custa-whatsapp-business-api-brasil-2026) antes de orçar, porque os valores da Meta ficam numa ferramenta interativa.

## Conta 3: a política de provedores de IA

Essa é a que quase ninguém coloca na planilha, e no Brasil ela pesa.

Desde março de 2026 a Meta cobra o que ela chama de provedores de IA por mensagem livre entregue. A cobrança foi revogada para a Europa em maio, e **no Brasil continua**. Cada resposta da conversa é cobrada separadamente.

Se ela se aplica ao seu caso, essa conta se soma às outras duas, e o efeito é multiplicativo com a conta 2: as duas incidem sobre a mesma mensagem.

O critério de enquadramento e como verificar nos seus próprios dados estão em [uma página só sobre isso](/cobranca-de-ai-provider-no-brasil). O resumo prático: existe uma categoria específica nos relatórios e uma marcação no webhook que dizem, com dado da Meta, se isso se aplica a você.

## Como estimar o seu caso

Pegue uma conversa real, dessas que já aconteceram, e conte:

**Quantos turnos ela teve.** Cada resposta sua é um turno.

**Quanto texto foi para o modelo em cada turno.** Some entrada e saída, lembrando que a entrada cresce se você reenvia histórico.

**Multiplique os turnos pelo preço da mensagem**, na faixa de utilidade.

**Se a conta 3 se aplica, multiplique os turnos de novo** pelo valor dela.

**Multiplique tudo pelo volume de conversas do mês.**

O número que sai costuma surpreender de dois jeitos. Se a operação é de poucas conversas longas, o modelo domina. Se é de muitas conversas curtas, a mensagem domina. Saber em qual dos dois você está muda o que vale otimizar.

## A quarta conta, que aparece em outubro: a franquia

Falta uma variável nas três contas acima, e ela é nova. A partir de 1º de outubro de 2026, cada número recebe **1.000 mensagens de serviço gratuitas por mês**, com cobrança a partir daí. Isso veio em comunicado da Meta a parceiros e [ainda não localizamos na documentação pública](/mensagem-de-servico-vai-ser-paga-outubro-2026), então entra na sua planilha como cenário, não como certeza.

Para agente de IA, essa franquia importa mais do que parece, porque agente conversa em muitos turnos. Uma operação com 1.000 conversas de uma mensagem cabe inteira na franquia. A mesma operação com conversas de cinco turnos usa a franquia em 200 conversas e paga o resto. **É o número de turnos, e não o número de clientes, que decide se a franquia te cobre.**

O que isso muda no desenho: reduzir turnos passa a ter retorno duplo, porque corta token do modelo e corta mensagem cobrada. Resposta que já traz a informação completa vale mais que resposta que puxa outra pergunta, e agora isso aparece na fatura.

E existe um limite técnico que empurra na mesma direção: mandar três balões curtos seguidos para parecer humano se aproxima do [limite por par entre a sua empresa e aquele destinatário](/quantas-mensagens-por-segundo-posso-enviar) e, depois de outubro, custa três vezes.

::video: Bev4VxTJ5Cg | Nove minutos em que o Israel abre o e-mail da Meta aos parceiros e lê o item da franquia. Em 03:53 está a redação, e em 06:38 a leitura dele sobre operar com mais números para multiplicar a franquia.

Para calibrar se a sua soma está boa, vale comparar com a alternativa de prateleira: [o agente da própria Meta tem ordem de grandeza relatada de 20 a 30 centavos por mensagem](/meta-business-agent-quanto-custa), que é a faixa de uma mensagem de marketing. Ficar confortavelmente abaixo disso é o que justifica manter agente próprio pelo custo, e não só pelo controle.

## O que realmente reduz a conta

**Resolver em menos turnos.** É o ganho maior e o mais ignorado. Uma resposta que já traz a informação completa vale mais que três que puxam pergunta. Isso reduz as três contas de uma vez.

**Uma mensagem por resposta.** A tentação de quebrar em três balões para parecer humano multiplica a conta 2 e a 3, e ainda se aproxima do limite por par.

**Filtrar antes do modelo.** Nem toda mensagem precisa de IA. "Oi", "obrigado" e "ok" podem ser tratados por regra simples. Isso corta a conta 1 sem afetar a experiência.

**Aproveitar a janela de 72 horas.** Quem chega por anúncio Click-to-WhatsApp e é respondido em 24 horas abre uma janela de 72 horas gratuita. Se boa parte do seu tráfego vem de anúncio, isso é dinheiro na mesa.

**Medir custo por conversa resolvida.** É a métrica que importa depois de outubro. Volume total não diz se você está gastando bem.

## Perguntas frequentes

### O que o cliente me manda custa?

Não. A Meta cobra a mensagem que sai e é entregue.

### Se eu rodar o modelo no meu servidor, sai mais barato?

Muda a conta 1: você troca custo por chamada por custo de infraestrutura. As contas 2 e 3 continuam iguais, porque elas são da plataforma, não do modelo.

### Agente de IA sai mais caro que atendente humano?

Depende do volume e do tipo de conversa. Mas a comparação honesta inclui as três contas do agente, e não só o token, que é o erro mais comum nessa conta.

### E o agente da própria Meta?

Ele é cobrado por token, a US$ 2,00 por milhão, com estimativa de US$ 0,04 a US$ 0,05 por mensagem já incluindo a entrega. Serve como ponto de comparação de preço para quem vende agente.

### Como sei se a conta 3 se aplica a mim?

Olhando os dados: existe uma categoria específica no relatório e uma marcação no payload do webhook. Vale ligar um alerta nesses dois campos antes de escalar volume.

### Vale esperar outubro para lançar?

Não. Vale calcular com o preço de outubro desde já, para não lançar com uma margem que deixa de existir em três semanas.

## Como decidir

Se o seu agente resolve em poucos turnos e o volume é alto, a conta que manda é a da mensagem, e o trabalho está em encurtar conversa. Se ele conversa longo com poucas pessoas, a conta que manda é a do modelo, e o trabalho está em gerenciar contexto.

Nos dois casos, refaça a planilha com o preço de outubro antes de fechar contrato anual. A linha que hoje é zero deixa de ser.

::cta: Refaça a conta com uma conversa real, hoje | Pegue uma conversa que já aconteceu, conte os turnos, e multiplique pela faixa de utilidade. Esse é o custo que aparece em outubro e que hoje não aparece em lugar nenhum.

## Leia também
- [A Meta cobra por mensagem de agente de IA no Brasil](/cobranca-de-ai-provider-no-brasil)
- [1º de outubro: responder o cliente deixa de ser grátis](/mensagem-de-servico-vai-ser-paga-outubro-2026)
- [Quanto custa a WhatsApp Business API no Brasil](/quanto-custa-whatsapp-business-api-brasil-2026)
- [Posso mandar a conversa do meu cliente para a OpenAI?](/posso-mandar-a-conversa-do-cliente-para-a-openai)

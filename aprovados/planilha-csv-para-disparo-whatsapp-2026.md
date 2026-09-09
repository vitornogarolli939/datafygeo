---
title: "Como montar a planilha CSV para disparo no WhatsApp"
description: "Coluna de telefone obrigatória, formato sem símbolo, e as outras colunas viram variáveis. O erro mais caro aqui não gera falha nenhuma no relatório."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "planilha-csv-para-disparo-whatsapp"
cluster: "implementacao"
hero: "limite"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messaging-limits
  - https://business.whatsapp.com/policy
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=ly5nOHFpXcI
videos: [ly5nOHFpXcI]
internal_links:
  - /disparo-em-massa-api-oficial-whatsapp
  - /variaveis-de-template-nomeadas-ou-posicionais
  - /mandei-para-numero-que-nao-existe-e-nao-deu-erro
  - /minha-campanha-travou-no-meio
  - /taxa-de-resposta-e-bloqueio
status: aprovado
---

# Como montar a planilha CSV para disparo no WhatsApp

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** uma coluna chamada **telefone**, obrigatória, com o número no formato **código do país mais DDD mais número**, tudo junto e sem símbolo. Qualquer outra coluna que você acrescentar vira uma **variável do template**.

Simples assim, e é onde nascem dois erros que se comportam de formas opostas: número em formato errado **falha e aparece no relatório**, e mapeamento de variável trocado **funciona e não aparece em lugar nenhum**. O segundo é o caro.

::numeros: 1 coluna|obrigatória, a do telefone ;; 55|o código do país, sem o mais ;; 0|símbolos no número: sem traço, parênteses ou espaço ;; 3 linhas|é o teste que evita o desastre

## Principais pontos
- **A coluna de telefone é obrigatória** e precisa ter esse nome. As demais são livres.
- **O formato é rígido:** código do país, DDD e número, sem parênteses, traço, espaço ou sinal de mais.
- **Número sem o nono dígito vira destinatário inválido**, e é a falha mais comum em base antiga.
- **Mapeamento errado não gera erro.** Mil pessoas recebem o dado trocado e o relatório mostra sucesso.
- **Dispare para três antes de disparar para dez mil**, com o seu número na primeira linha.

::diagrama: n8n-fluxo

## O formato

```
telefone,nome,vencimento
5511999999999,Maria,10/09
5541988887777,João,12/09
5521977776666,Ana,15/09
```

Três regras sobre a coluna do telefone:

**O nome da coluna importa.** Ela precisa se chamar telefone. As outras podem ter o nome que você quiser.

**Não precisa ser a primeira coluna**, e precisa estar **na primeira linha**, no cabeçalho.

**O conteúdo é só dígito.** Código do país, DDD e número, colados. Sem o sinal de mais, sem parênteses no DDD, sem traço antes dos quatro últimos.

::video: ly5nOHFpXcI | Dez minutos com um disparo real do começo ao fim. Em 02:19 ele mostra o formato exigido, em 02:53 abre uma planilha correta explicando cada coluna, e em 03:22 avisa que colocou de propósito um número inexistente para você ver o que acontece no relatório.

## O problema do nono dígito

É a causa número um de falha em base antiga, e ela é silenciosa até o relatório.

Números de celular brasileiros ganharam um dígito a mais. Uma base montada antes disso, ou importada de um sistema antigo, tem telefones com um dígito a menos, e eles **não existem** como destinatário.

O que fazer antes de disparar:

**Confira o comprimento.** Celular brasileiro no formato completo tem 13 dígitos: 55, mais dois de DDD, mais nove do número.

**Não corrija adivinhando.** Acrescentar um nove no começo do número funciona para a maioria dos casos e não para todos, principalmente em DDDs que fizeram a transição em datas diferentes. Corrigir errado é mandar mensagem para outra pessoa.

**Marque o que falhou e não tente de novo.** Número que falhou por não existir vai falhar de novo daqui a um mês, e cada tentativa consome cota.

E vale saber que **outros países têm regra própria**. Argentina e México têm particularidades de prefixo que quebram o mesmo tipo de base.

## As outras colunas: as variáveis

Toda coluna além do telefone pode virar uma variável do template. O nome da coluna **não precisa** ser igual ao nome da variável, porque existe um passo de mapeamento entre as duas coisas.

E é aqui que mora o erro caro.

**Mapeamento trocado não dá erro.** Se você aponta a variável de nome para a coluna de data, o sistema preenche, envia, e entrega. Dez mil pessoas recebem "Olá 10/09" e o relatório mostra dez mil sucessos, porque tecnicamente foram sucessos.

Não existe validação que pegue isso, porque do ponto de vista técnico está tudo certo. A única proteção é visual.

**O teste que evita:** coloque **o seu próprio número na primeira linha** da planilha e dispare para uma lista de três. Você vê a mensagem exata que o cliente vai ver, com a variável já preenchida. Trinta segundos, e pega o erro que o relatório nunca vai acusar.

Se o seu template usa variável nomeada ou posicional muda como o mapeamento é feito, e [vale entender a diferença](/variaveis-de-template-nomeadas-ou-posicionais) antes de montar a campanha.

## Antes de exportar a planilha

Cinco conferências que levam dois minutos e evitam o retrabalho:

**Cabeçalho na primeira linha.** Planilha exportada de sistema costuma vir com título ou logo nas primeiras linhas, e aí o cabeçalho está na linha quatro. Nesse caso a primeira linha de dados é lida como nome de coluna.

**Sem coluna vazia no meio.** Coluna sem nome no cabeçalho quebra a leitura.

**Telefone como texto, não como número.** Planilhas convertem sequências longas de dígitos para notação científica, e o número vira algo como 5,51199E+12. Formate a coluna como texto **antes** de colar os dados.

**Sem espaço no começo ou no fim.** Espaço invisível em célula é comum em dado colado, e faz o número não bater.

**Exporte como CSV**, e não como planilha nativa. E confira o resultado abrindo o arquivo em um editor de texto: é onde o problema de formatação fica visível.

## Conferir os primeiros contatos

Antes de confirmar o disparo, a maioria das ferramentas lista os primeiros contatos lidos da planilha. **Olhe essa lista.**

É o momento em que aparecem, de graça, os três erros mais comuns: cabeçalho na linha errada, número em notação científica, e coluna deslocada. Depois de confirmar, eles custam mensagens.

## O que a planilha não resolve

Vale lembrar, porque planilha bem montada dá uma falsa sensação de segurança:

**Lista certa não é lista quente.** Formato perfeito com base que não interage [derruba número do mesmo jeito](/taxa-de-resposta-e-bloqueio). O caso da advogada, que fez tudo certo e caiu em dois dias, é exatamente isso.

**Sucesso no envio não é entrega.** [A chamada responde sucesso mesmo quando vai falhar](/mandei-para-numero-que-nao-existe-e-nao-deu-erro), e a verdade chega depois, no status.

**As recusas pedem reações diferentes.** Limite por pessoa, opção de não receber e a recusa por saúde do ecossistema não se tratam igual, e [reenviar piora três delas](/minha-campanha-travou-no-meio).

## Perguntas frequentes

### A coluna precisa se chamar exatamente telefone?

Sim, essa é a única com nome fixo. As outras são livres, porque passam por mapeamento.

### Posso colocar o número com mais ou com traço?

Não. Só dígitos, colados. Limpe a formatação antes de exportar.

### Quantas colunas de variável posso ter?

Tantas quantas o template tiver de variáveis. Colunas a mais na planilha são ignoradas, e não atrapalham.

### E se um contato não tem o dado de uma variável?

Ele precisa de algum valor. Preencha com um padrão que faça sentido no texto, porque variável vazia é recusada.

### Dá para agendar o disparo?

Dá, e atenção ao fuso: o horário costuma ser o de quem agenda, não o de quem recebe. Para base espalhada, isso importa.

### Quantos contatos por planilha?

Depende da ferramenta. E vale mandar em blocos de qualquer forma, para observar entrega e resposta antes de continuar.

## Como decidir

Se a sua base já está limpa e o template tem uma variável, a planilha é trivial e você pode disparar hoje.

Se a base é antiga, gaste a hora de conferir o comprimento dos números antes. Ela se paga na primeira campanha, porque número inválido consome cota, aparece como falha e piora o seu indicador.

E, sempre, faça o disparo de três com o seu número na primeira linha. É o único teste que pega o erro de mapeamento, que é o único desses erros que não aparece em relatório nenhum.

::cta: Coloque o seu número na primeira linha da próxima planilha | Dispare para três antes de disparar para todos. Você vê a mensagem com a variável preenchida, exatamente como o cliente vai ver, e pega em trinta segundos o erro que passaria por dez mil pessoas.

## Leia também
- [Como fazer disparo em massa na API oficial](/disparo-em-massa-api-oficial-whatsapp)
- [Variáveis de template: nomeadas ou posicionais](/variaveis-de-template-nomeadas-ou-posicionais)
- [Mandei para um número que não existe e não deu erro](/mandei-para-numero-que-nao-existe-e-nao-deu-erro)
- [Disparei a campanha e ela travou no meio](/minha-campanha-travou-no-meio)

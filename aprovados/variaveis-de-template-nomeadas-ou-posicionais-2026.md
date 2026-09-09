---
title: "Variáveis de template no WhatsApp: nomeadas ou posicionais"
description: "A escolha é feita na criação e não dá para misturar no envio. Trocar os dois formatos gera erro de contagem de parâmetros, que se disfarça de outro problema."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "variaveis-de-template-nomeadas-ou-posicionais"
cluster: "implementacao"
hero: "erro"
intent: "problema-urgente"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-categorization
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=YF9hTHDAw6E
  - https://www.youtube.com/watch?v=62oSY66J3s4
videos: [YF9hTHDAw6E, 62oSY66J3s4]
internal_links:
  - /como-criar-template-whatsapp-passo-a-passo
  - /como-enviar-template-pela-api
  - /template-nao-existe-nesse-idioma
  - /template-com-imagem-no-cabecalho-nao-envia
  - /disparo-em-massa-api-oficial-whatsapp
status: aprovado
---

# Variáveis de template no WhatsApp: nomeadas ou posicionais

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** o editor de templates aceita dois formatos de variável, e você escolhe **na criação**. Ou elas têm nome, tipo `{{nome_cliente}}`, ou são numeradas, tipo `{{1}}`.

A escolha parece cosmética e não é: **o envio precisa seguir o mesmo formato com que o template foi criado.** Criar com nome e enviar como se fosse numerado devolve erro de contagem de parâmetros, e esse erro se disfarça de outros problemas, o que faz muita gente procurar defeito no lugar errado.

::numeros: 2 formatos|nomeadas ou posicionais, e você escolhe uma ;; 132000|o erro de contagem de parâmetros ;; 1 exemplo|obrigatório por variável, na criação ;; minúsculas|é a regra do nome, sem acento

## Principais pontos
- **A escolha é por template**, feita na criação, e não muda depois sem recriar.
- **Nome de variável é minúsculo, sem acento e sem espaço.** O editor recusa fora disso.
- **Todo exemplo é obrigatório.** Sem ele, o template não vai para análise.
- **Misturar formatos dá erro de contagem**, que é diferente do erro de template inexistente e pede outra correção.
- Em disparo por planilha, o que importa é o **mapeamento**, e mapeamento errado não dá erro nenhum.

::diagrama: webhook-fluxo

## Os dois formatos

**Posicional.** As variáveis são números, na ordem em que aparecem:

```
Olá {{1}}, seu pedido {{2}} saiu para entrega.
```

No envio, você manda um vetor de parâmetros, e a **ordem** define quem é quem.

**Nomeada.** As variáveis têm nome:

```
Olá {{nome_cliente}}, seu pedido {{numero_pedido}} saiu para entrega.
```

No envio, cada parâmetro carrega o nome ao qual pertence, então a ordem deixa de importar.

::video: YF9hTHDAw6E | Em 04:23 ele cria uma variável, escolhe o tipo e explica a diferença entre os dois formatos. Em 04:51 mostra a regra do nome, minúsculo e sem acento, e em 05:33 preenche o exemplo obrigatório.

## Qual escolher

Não existe resposta única, e existe um critério bom.

**Escolha nomeada quando** o template tem três ou mais variáveis, quando o texto pode ser reescrito no futuro, ou quando mais de uma pessoa mexe nisso. O ganho é legibilidade: olhando o código do envio, dá para saber o que está sendo preenchido.

**Escolha posicional quando** é uma variável só, ou quando o template é gerado por um sistema que já controla a ordem. É mais compacto e não tem regra de nomenclatura para respeitar.

O risco da posicional é conhecido: **trocar a ordem em silêncio.** Se alguém inverte dois parâmetros no código, o envio funciona, o template é aceito, e mil clientes recebem o nome no lugar do número do pedido. Nenhum erro é gerado.

O risco da nomeada é menor, e existe: **nome escrito diferente** entre criação e envio. Aí sim aparece erro, o que é melhor que a falha silenciosa.

## O erro que aparece quando você mistura

O código de contagem de parâmetros surge quando a quantidade ou o formato do que você mandou não corresponde ao que o template espera.

Três causas, em ordem de frequência:

**Formato trocado.** Template criado com variável nomeada, envio feito como posicional, ou o contrário.

**Quantidade errada.** Template com três variáveis recebendo dois parâmetros. Comum depois de alguém editar o texto do template e acrescentar uma variável sem avisar o time.

**Componentes misturados.** Cabeçalho e corpo são componentes separados, cada um com os próprios parâmetros. Jogar o parâmetro do cabeçalho dentro do corpo dá esse mesmo erro, e é confundido com problema de imagem. [Esse caso tem página própria](/template-com-imagem-no-cabecalho-nao-envia).

E vale a distinção que economiza tempo de diagnóstico:

| Erro | O que significa | Onde olhar |
|---|---|---|
| Template não existe nesse idioma | O par nome mais idioma não bate | [Código de idioma e nome](/template-nao-existe-nesse-idioma) |
| Contagem de parâmetros | Formato ou quantidade das variáveis | Este texto |
| Tipo do componente | Cabeçalho esperando um tipo e recebendo outro | Componente de mídia |

Os três aparecem no mesmo momento, no envio, e pedem correções diferentes.

## As regras do editor que geram retrabalho

**Nome minúsculo, sem acento, sem espaço.** Use sublinhado. `nome_cliente` funciona, `Nome Cliente` não.

**Exemplo obrigatório para cada variável.** É o que a Meta usa para revisar. E vale um cuidado: **o exemplo deve parecer o dado real**. Colocar "teste" ou "xxx" como exemplo aumenta a chance de reprovação, porque o revisor não consegue avaliar se o template faz sentido.

**Variável no cabeçalho é permitida**, e ela conta como um parâmetro do componente de cabeçalho, separado dos do corpo.

**Alterar o texto exige nova revisão.** Acrescentar uma variável a um template aprovado significa passar por análise de novo, e enquanto isso o envio antigo continua valendo. Vale coordenar isso com quem dispara.

## Onde isso quebra em disparo por planilha

Se você dispara por planilha, o formato da variável importa menos e **o mapeamento importa muito**.

A planilha tem colunas, o template tem variáveis, e alguém liga uma coisa na outra. O nome da coluna não precisa ser igual ao da variável.

E aqui está o problema que não é erro: **mapeamento trocado não falha.** Você aponta a variável de nome para a coluna de data, dispara para dez mil pessoas, e todas recebem uma data no lugar do nome. O relatório mostra sucesso, porque tecnicamente foi sucesso.

A proteção é uma só, e ela é chata: **coloque o seu número na primeira linha da planilha e dispare para três antes de disparar para todos.** Você vê a mensagem exata que o cliente vai ver, com a variável preenchida. [O resto do processo de disparo está aqui](/disparo-em-massa-api-oficial-whatsapp).

## Como não errar mais isso

Três hábitos que eliminam essa classe inteira de problema:

**Guarde o template no seu banco como estrutura, não como nome.** Nome, idioma, formato das variáveis e a lista delas. Assim o código que monta o envio consulta a definição em vez de assumir.

**Sincronize a lista de templates periodicamente.** Puxando da API, você percebe quando alguém editou um template no painel e acrescentou variável.

**Centralize a montagem do corpo.** Uma função só que recebe o template e um dicionário de valores, e monta os componentes. Espalhar isso por vários lugares é o que faz o formato divergir com o tempo.

## Perguntas frequentes

### Posso mudar de posicional para nomeada depois?

Não sem recriar o template, porque isso muda a estrutura dele. E o nome do template não se repete, então na prática vira outro template.

### Qual formato a Meta prefere?

Nenhum dos dois é preferido. A escolha é sua, e o que importa é o envio seguir o que foi criado.

### Posso deixar uma variável vazia no envio?

Não. Todas precisam de valor. Se o dado pode faltar, mande um valor padrão em vez de string vazia, e escreva o texto do template para isso fazer sentido.

### O exemplo aparece para o cliente?

Não. Ele serve para a revisão e para você visualizar. O cliente vê o valor que você mandar no envio.

### Como sei quantas variáveis um template tem?

Listando os templates pela API. A definição vem com os componentes e os parâmetros esperados.

### Variável aceita quebra de linha ou emoji?

O valor enviado tem restrições de formato, e quebra de linha em parâmetro é uma das que costumam ser recusadas. Prefira manter a formatação no texto fixo do template.

## Como decidir

Se você tem poucos templates e uma variável cada, posicional resolve e é mais curto.

Se os templates têm várias variáveis, ou mais de uma pessoa mexe neles, use nomeada. O custo é seguir a regra de nomenclatura, e o retorno é que uma inversão de ordem para de ser possível.

E, em qualquer caso, o hábito que mais evita prejuízo não tem a ver com formato: **mande para você mesmo antes de mandar para a base.** É onde o mapeamento errado aparece, e é o único erro dessa família que não gera nenhuma mensagem de falha.

::cta: Dispare para três antes de disparar para dez mil | Coloque o seu número na primeira linha da planilha. Você vê a mensagem com a variável já preenchida, e pega em trinta segundos o erro de mapeamento que o relatório nunca vai acusar.

## Leia também
- [Como criar um template de mensagem, passo a passo](/como-criar-template-whatsapp-passo-a-passo)
- [Como enviar uma mensagem de template pela API](/como-enviar-template-pela-api)
- [Erro 132001: o template não existe nesse idioma](/template-nao-existe-nesse-idioma)
- [Como fazer disparo em massa na API oficial](/disparo-em-massa-api-oficial-whatsapp)

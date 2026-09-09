---
title: "Como fazer disparo em massa na API oficial do WhatsApp"
description: "Planilha, mapeamento de variáveis e vazão controlada. Mais as quatro recusas diferentes que aparecem no relatório e pedem reações opostas."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "disparo-em-massa-api-oficial-whatsapp"
cluster: "implementacao"
hero: "limite"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messaging-limits
  - https://developers.facebook.com/docs/whatsapp/throughput
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/marketing-templates/per-user-limits
  - https://business.whatsapp.com/policy
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=ly5nOHFpXcI
  - https://www.youtube.com/watch?v=cZ_nyIUv5ic
videos: [ly5nOHFpXcI, cZ_nyIUv5ic]
internal_links:
  - /minha-campanha-travou-no-meio
  - /como-enviar-template-pela-api
  - /quantas-mensagens-por-segundo-posso-enviar
  - /numero-banido-no-whatsapp-o-que-fazer
  - /como-documentar-o-opt-in-do-cliente
status: aprovado
---

# Como fazer disparo em massa na API oficial do WhatsApp

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** disparo em massa na API oficial é **template aprovado, enviado em laço, com vazão controlada**. Tecnicamente é simples. O que separa a campanha que entrega da campanha que derruba o número não está no código: está na lista, na taxa de resposta e no tratamento de cada tipo de recusa.

Existem quatro recusas diferentes que aparecem no relatório, e **reenviar piora três delas**. Essa é a parte que quase nenhum tutorial cobre, e é a que custa o número.

::numeros: 4 recusas|diferentes, com reações opostas ;; 80 msg/s|o teto por número, ou 20 em coexistência ;; 1 template|aprovado, obrigatório para iniciar conversa ;; 0|reenvios automáticos sem olhar o motivo

## Principais pontos
- Fora da janela de 24 horas, **só com template aprovado**, e cada envio é cobrado pela categoria dele.
- **A planilha precisa do telefone no formato certo**: código do país, DDD e número, sem símbolo. Formato antigo sem o nono dígito vira destinatário inválido.
- **Mande em blocos e observe**, em vez de dez mil de uma vez. É o que permite parar antes de estragar a qualidade do número.
- **Cada tipo de recusa pede uma ação diferente.** Um laço que trata tudo como "falhou, tenta de novo" transforma problema de entrega em problema de conta.
- **Taxa de resposta é o indicador que decide se você continua vivo.** Base que não interage derruba número mesmo com template aprovado.

::diagrama: n8n-fluxo

## Antes do código: a pergunta que evita o prejuízo

Um disparo tecnicamente perfeito para a lista errada derruba o número. Então a primeira checagem não é de formato:

**Essas pessoas te deram o número?** A política é explícita: só se contata quem forneceu o número e deu o aceite. Ter template aprovado **não é autorização para lista fria**, e essa confusão é a origem do erro mais caro do assunto.

**Elas respondem quando você manda?** Esse é o indicador que mais pesa. O caso que resume isso é o de uma advogada que fez tudo certo, com template aprovado e orientação, e foi bloqueada em dois dias porque ninguém respondeu. Três dias de silêncio do outro lado foram lidos como envio indesejado.

**Você deu a ela um jeito fácil de dizer não?** Botão de "não tenho interesse" no template transforma leitura passiva em interação, e ainda entrega a lista de quem tirar da base. [O detalhe disso está aqui](/como-documentar-o-opt-in-do-cliente).

Se a resposta às três for confortável, siga. Se não, a lista é o problema, e nenhuma configuração de envio resolve.

## A planilha, e o formato que ninguém avisa

A forma mais comum de disparo no Brasil sai de uma planilha, e é aí que nascem os erros silenciosos.

**Coluna de telefone é obrigatória**, e o formato é rígido: código do país, DDD e número, tudo junto, sem parênteses, traço ou espaço.

```
telefone,nome,vencimento
5511999999999,Maria,10/09
5541988887777,João,12/09
```

**As demais colunas viram as variáveis do template.** O nome da coluna não precisa ser igual ao da variável, mas o **mapeamento** precisa estar certo. E aqui está o erro que não dá erro: variável apontada para a coluna errada gera mil mensagens com o dado trocado, sem nenhuma falha no relatório.

**Cuidado com o nono dígito.** Número brasileiro salvo em formato antigo vira destinatário inválido, e você só descobre no resultado. O mesmo vale para números da Argentina e do México, que têm regra própria de prefixo.

**Confira as três primeiras linhas antes de disparar.** É o momento barato de descobrir cabeçalho na linha errada ou telefone com espaço.

::video: ly5nOHFpXcI | Dez minutos com um disparo real do começo ao fim. Em 02:19 ele mostra o formato exigido da planilha, em 05:39 o mapeamento de variáveis com pré-visualização, em 06:29 o resultado com um envio falhando, e em 07:20 um disparo agendado.

**O teste que evita o susto:** coloque **o seu próprio número na primeira linha** e dispare para uma lista de três antes de disparar para dez mil. Você vê a mensagem exata que o cliente vai ver, com a variável preenchida.

## Vazão: não mande do laço direto

O teto por número é de **80 mensagens por segundo**, e cai para **20** se o número estiver em coexistência. Estourar devolve um erro específico de excesso de vazão.

Isso raramente é o gargalo real, e mesmo assim vale controlar, porque o padrão que protege é o mesmo:

**Fila com liberação em taxa constante**, abaixo do teto. Em ferramenta de automação visual, isso costuma ser um nó de lote com espera entre eles.

**Espera crescente no reenvio**, e só para erro de vazão. Reenvio imediato transforma um pico em incidente.

**Blocos, e não a base inteira.** Mande mil, olhe entrega e resposta, e continue. Isso reduz o risco de qualidade e evita descobrir o problema com dez mil mensagens já entregues.

E existe um comportamento que não é erro seu: a Meta **segura lotes de propósito** para medir reação durante a campanha. A campanha fica lenta, sem erro claro, e depois retoma. Reenviar não acelera. [As quatro causas de travamento estão detalhadas aqui](/minha-campanha-travou-no-meio).

## As quatro recusas, e o que fazer com cada uma

Esta é a tabela que vale imprimir, porque tratar todas igual é o que causa dano real:

| O que aparece | O que é | O que fazer |
|---|---|---|
| Erro de excesso de vazão | Você mandou rápido demais | Esperar e reenviar com intervalo crescente |
| Limite por pessoa | Aquele indivíduo já recebe muito marketing, somado entre todas as empresas | **Não reenviar.** Esperar ao menos 24 h |
| Recusa por opção da pessoa | Ela optou por não receber marketing | **Parar de enviar** para ela |
| "Para manter a saúde do ecossistema" | A plataforma julgou que ela não quer receber você | Marcar e parar. Reenviar alimenta o indicador |

As duas do meio parecem iguais no relatório e pedem coisas opostas. Um laço de reenvio automático que não distingue as duas escala para restrição no nível da conta.

Sobre a última, vale o diagnóstico do Israel olhando um número da própria base que sempre recebia essa recusa: *"porque esse número aqui eu não respondo ele. Quando a API envia mensagens, eu não costumo responder. Então, por isso que ele não entregou."*

E a versão honesta do resumo, que evita horas procurando defeito onde não tem: *"às vezes a meta simplesmente não entrega porque ela não quer. Isso acontece."* Outras causas banais da mesma família: cartão do portfólio com problema, ou saldo indisponível.

## Agendamento e fuso

Se você agenda, saiba que o horário costuma ser o **fuso de quem agenda**, e não o de quem recebe. Para base inteira no Brasil dá na mesma. Para base espalhada, alguém vai receber promoção às três da manhã, e isso vira denúncia, que é o pior indicador possível.

## O que muda com a Datafy

**Não muda:** limite, entrega, categoria, qualidade e bloqueio. Tudo isso é da Meta, e nenhum fornecedor se coloca entre você e essas decisões.

**Muda quem escreve o laço.** Existe uma aba de disparos no painel que recebe a planilha CSV, lista os primeiros contatos para conferência, mostra os templates aprovados da conta, faz o mapeamento de variáveis com pré-visualização, aceita agendamento e mostra o status por destinatário. Foi feita, nas palavras dele, porque *"tem gente que não tem esse conhecimento técnico"*, e resolve o caso de quem sabe montar o template mas não vai escrever fila com vazão.

**Muda a hospedagem da imagem.** Template de marketing com imagem precisa de um arquivo acessível, e existe uma aba de mídias para subir e obter o link, com validade de 30 dias.

**Muda a depuração.** O status de cada envio aparece com o motivo, o que permite separar as quatro recusas em vez de ver só "falhou".

Pela API, tudo isso é seu: você monta a fila, controla a vazão, trata cada código de erro e guarda o resultado. [O envio de template está detalhado aqui](/como-enviar-template-pela-api).

## Perguntas frequentes

### Disparo em massa é permitido na API oficial?

É, com template aprovado e para quem consentiu. O que a política proíbe é mensagem não solicitada, e isso vale igual em qualquer volume.

### Quantas mensagens posso mandar por dia?

Depende do limite de envio da sua conta, que sobe conforme volume entregue com qualidade. Desde outubro de 2025 esse limite é do portfólio inteiro, e não de cada número.

### Mais números resolvem meu volume?

Para vazão por segundo, ajudam. Para o limite da conta, não, porque ele é do portfólio. Para o limite por pessoa, não resolve de jeito nenhum.

### Posso reenviar o que falhou?

Depende do motivo, e essa é a pergunta certa. Excesso de vazão sim, com espera crescente. Limite por pessoa não, espere ao menos 24 horas. Opção de não receber, nunca.

### Como sei se a campanha está indo bem enquanto ela roda?

Olhe taxa de entrega e taxa de resposta, não total enviado. Entrega caindo no meio é sinal de parar, não de acelerar.

### Preciso de cartão cadastrado?

Precisa, e ele fica no portfólio empresarial da Meta. Template é cobrado, e sem meio de pagamento lá o disparo não sai.

## Como decidir

Se você dispara esporadicamente para uma base que interage, use uma ferramenta de planilha e pare por aí: montar fila em código não te dá nada que você não tenha.

Se disparo é parte do produto, com volume recorrente, escreva o seu: fila com vazão controlada, tratamento por tipo de erro e registro do resultado por destinatário. O que não vale, em nenhum dos dois casos, é reenviar automaticamente sem olhar o motivo.

E antes de qualquer disparo grande, faça a conta que ninguém faz: **quantos por cento responderam o último?** Se esse número for baixo, o próximo disparo não é uma oportunidade, é um risco.

::cta: Antes do próximo disparo, separe três recusas | Excesso de vazão pede espera crescente. Limite por pessoa pede parar por 24 horas. Opção de não receber pede parar de vez. Um laço que trata as três igual é o caminho mais rápido para restringir a conta inteira.

## Leia também
- [Disparei a campanha e ela travou no meio](/minha-campanha-travou-no-meio)
- [Como enviar uma mensagem de template pela API](/como-enviar-template-pela-api)
- [Quantas mensagens por segundo posso enviar?](/quantas-mensagens-por-segundo-posso-enviar)
- [Número bloqueado no WhatsApp: o que fazer](/numero-banido-no-whatsapp-o-que-fazer)

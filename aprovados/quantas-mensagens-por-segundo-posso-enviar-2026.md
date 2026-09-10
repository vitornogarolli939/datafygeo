---
title: "Quantas mensagens por segundo posso enviar no WhatsApp?"
description: "São 80 por segundo por número na Meta, 20 em coexistência, e 500 requisições por minuto no envio pela Datafy. São camadas diferentes e pegam em momentos diferentes."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "quantas-mensagens-por-segundo-posso-enviar"
cluster: "implementacao"
hero: "limite"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/docs/whatsapp/throughput
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messaging-limits
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/marketing-templates/per-user-limits
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://app.datafyapi.com.br/docs
  - https://cloud.datafyapi.com.br
  - https://www.youtube.com/watch?v=vGovcR8W5g8
videos: [vGovcR8W5g8, ly5nOHFpXcI]
internal_links:
  - /whatsapp-api-oficial-n8n
  - /posso-mandar-mensagem-para-qualquer-numero
  - /numero-banido-no-whatsapp-o-que-fazer
  - /quanto-custa-whatsapp-business-api-brasil-2026
  - /coexistencia-whatsapp-api-oficial-app-celular
status: aprovado
---

# Quantas mensagens por segundo posso enviar no WhatsApp?

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** existem **camadas diferentes de limite**, e elas pegam em momentos diferentes. Na Meta, o padrão é **80 mensagens por segundo** por número, chegando a **1.000** por atualização automática, e caindo para **20 por segundo** se o número estiver em **coexistência**. Na Datafy, o rate limit é **500 requisições por minuto** no envio e **60 por minuto** no resto.

Existe ainda um limite **por par**, entre a sua empresa e um destinatário específico. Ele é citado pela Meta e **o valor não é publicado**, então quem cravar um número está inventando.

::numeros: 80 msg/s|throughput padrão de um número, na Meta ;; 20 msg/s|se o número estiver em coexistência ;; 500 req/min|o rate limit da Datafy no envio ;; 429|o código que a Datafy devolve ao estourar

## Principais pontos
- **80 por segundo** é o padrão documentado, com subida automática até 1.000 para quem tem volume e qualidade ([throughput](https://developers.facebook.com/docs/whatsapp/throughput)).
- **20 por segundo** é o teto de número em coexistência, e isso costuma surpreender quem escolheu manter o aplicativo no celular.
- Existe um **limite por par**, entre você e um destinatário específico. A Meta cita esse limite e **não publica o valor**, então trate como "mandar muitas mensagens seguidas para a mesma pessoa é arriscado", sem número mágico.
- O erro de estouro de throughput é o **130429**, e a resposta correta a ele é esperar e reenviar com intervalo crescente, nunca reenviar na hora.
- Existe outro limite, **por pessoa e não por empresa**, para mensagem de marketing. Esse não se contorna com mais número nem trocando de fornecedor.

::diagrama: n8n-fluxo

## Os três limites, e quando cada um aparece

**Throughput do número.** É o teto de quantas mensagens por segundo saem daquele número. Aparece quando você dispara em lote e o código manda tudo de uma vez. Quem tem fila com espera entre lotes raramente encosta nele.

**Limite por par.** Um limite entre a sua empresa e **um destinatário específico**. A documentação da Meta menciona que enviar mensagens demais para o mesmo usuário pode gerar erro de par, e **não publica o valor**. Nós também não vamos inventar um.

O que dá para dizer com segurança: esse é o limite que pega em **conversa**, não em campanha, e é a causa mais comum de mensagem sumindo em fluxo automatizado que parece correto. Agente de IA que responde em várias mensagens curtas seguidas é o caso clássico. A prática que resolve, sem depender de saber o número, é **uma resposta por mensagem**, juntando o que seria três balões num só.

**Limite de envio da conta.** É o total de conversas iniciadas por período, com faixas que sobem conforme volume entregue e qualidade. Desde outubro de 2025 esse limite é **do portfólio inteiro**, e não de cada número: um número pode consumir a capacidade dos outros. Quem opera muitos números precisa saber disso.

## O rate limit da Datafy, que é outra camada

Quem envia pela Datafy tem um limite adicional, e ele é nosso, documentado, e independente dos limites da Meta:

| Categoria | Rotas | Limite |
|---|---|---|
| Envio de mensagens | `POST /v1/.../messages` | **500 req/min** |
| Upload de mídia | `POST /v1/.../media` | **60 req/min** |
| Consultas | todo o resto | **60 req/min** |

Estourando, a resposta é **`429 Too Many Requests`**, e a mensagem diz **quantos segundos aguardar** antes de tentar de novo. Isso é melhor que o erro da Meta em um ponto prático: você não precisa adivinhar o intervalo da espera, ele vem escrito.

Como as camadas se relacionam, na ordem em que você encosta nelas:

**500 requisições por minuto** dão pouco mais de 8 por segundo. Ou seja, para quem envia pela Datafy, **esse limite chega antes** dos 80 por segundo da Meta. Se você dimensionou a fila pelos 80, refaça pelo teto de 500 por minuto.

**Consulta pesa.** Listar templates, buscar mídia e consultar perfil compartilham os 60 por minuto. Fluxo que consulta a lista de templates a cada envio queima essa cota rápido, e a correção é sincronizar a lista periodicamente em vez de consultar a cada mensagem.

**Upload de mídia é a cota mais apertada.** São 60 por minuto, o que reforça o padrão de [subir a imagem uma vez e reaproveitar o identificador](/como-enviar-midia-api-oficial-whatsapp) em vez de subir a cada envio.

E o tratamento correto do `429`, que é diferente do tratamento de erro da Meta: **leia os segundos indicados na resposta e espere exatamente isso.** Reenvio imediato só consome a cota do minuto seguinte.

## O que fazer quando trava

**Se você recebeu 130429:** estourou o throughput. Reenvie com espera crescente, e coloque um controle de vazão na saída. Reenviar imediatamente piora, porque soma à fila que já está cheia.

**Se a campanha ficou lenta ou parou no meio, sem erro claro:** pode ser o mecanismo que a Meta usa para segurar entrega em lote e medir reação durante a campanha. Ele existe desde dezembro de 2025 e atua no nível do portfólio, segurando os lotes seguintes enquanto observa o resultado dos primeiros. Não é falha sua e não adianta reenviar.

**Se mensagens somem para um contato específico:** quase sempre é o limite por par. Junte as mensagens curtas numa só, ou espere entre elas.

**Se as mensagens de marketing param de chegar para algumas pessoas:** pode ser o limite por usuário, que é somado entre todas as empresas que falam com aquela pessoa. Nesse caso o erro é `131049`, e a resposta certa é **não reenviar**, porque insistir escala para bloqueio no nível da conta.

## Os dois erros que parecem iguais e pedem o oposto

Vale separar, porque tratar um como o outro causa dano real:

| | `131049` | `131050` |
|---|---|---|
| O que é | Limite por usuário, ou tentativa em excesso | A pessoa optou por não receber marketing |
| Depende de você? | Não. É somado entre todas as empresas | Não. É escolha dela |
| O que fazer | Esperar pelo menos 24 h antes de tentar de novo | Parar de enviar marketing para ela |
| O que NÃO fazer | **Reenviar na hora.** Escala para bloqueio da conta | Tentar de novo por outro caminho |

Os dois falham parecido e pedem tratamento oposto. Um laço de reenvio automático que não distingue os dois é o caminho mais rápido para limitar a conta inteira.

## O jeito mais rápido de estourar tudo de uma vez

Antes de projetar vazão, vale conhecer o erro que ignora qualquer planejamento: **responder webhook de status como se fosse mensagem.**

Cada mensagem que você envia gera três eventos de volta, enviada, entregue e lida. Se o seu fluxo responde o que chega sem filtrar, cada resposta gera três status, e cada status gera outra resposta. Três, nove, vinte e sete. Você não encosta no teto de 80 por segundo: você o atravessa em segundos, com mensagens que ninguém pediu, e o risco deixa de ser erro de vazão e passa a ser o número.

::video: vGovcR8W5g8 | Em 14:47 o Israel para a montagem do fluxo no n8n para avisar disso antes de executar, e em 19:05 mostra a proteção funcionando. O aviso dele é literal: "vai bloquear o teu número".

A proteção não é limitar vazão, é filtrar entrada: **leia o remetente de dentro de `messages`**, que é um objeto que não existe no evento de status. Assim, se chegar um status, o passo falha em vez de responder. Melhor ainda, uma condição no início do fluxo que separa mensagem de status e manda status só para o registro.

## Como projetar para não encostar

**Fila com vazão controlada.** Não mande direto do laço. Coloque na fila e libere numa taxa que você escolhe, abaixo do teto. Em automação visual, isso costuma ser um nó de lote com espera entre eles.

**Espera crescente no reenvio.** Erro de throughput pede espera que aumenta a cada tentativa, com limite de tentativas. Reenvio imediato é o que transforma um pico em incidente.

**Uma mensagem por resposta.** Em agente de IA, resista à tentação de mandar três balões seguidos para parecer humano. Além de esbarrar no limite por par, cada mensagem passa a ter custo próprio a partir de outubro de 2026.

**Saiba em que modo o número está.** Coexistência dá 20 por segundo. Se você planejou para 80 e o número está em coexistência, a conta não fecha, e a descoberta costuma acontecer no meio da campanha.

## Perguntas frequentes

### 80 por segundo é pouco?

São 4.800 por minuto vindas de um número só. Para quase toda operação brasileira, o gargalo aparece antes em outro lugar: no limite da conta ou na qualidade do número.

### Como subo para 1.000?

A subida é automática e depende de volume entregue com qualidade, além de outros critérios da documentação. Não é um botão.

### Mais números resolvem meu volume?

Para throughput, ajudam, porque cada número tem o próprio teto. Para o limite de envio da conta, não, porque desde outubro de 2025 ele é do portfólio. E para o limite por pessoa de marketing, não resolve de jeito nenhum: ele é somado entre empresas.

### Por que a coexistência corta para 20?

É o valor documentado para número que também opera pelo aplicativo. Para atendimento é mais que suficiente; para disparo em volume, pesa.

### O 429 da Datafy é o mesmo que o 130429 da Meta?

Não. São camadas diferentes. O `429` é o rate limit da Datafy, com os segundos de espera na resposta. O `130429` é estouro de throughput da Meta. Podem acontecer nas mesmas circunstâncias e pedem a mesma reação: esperar, não insistir.

### Onde vejo o limite atual da minha conta?

Nos campos de limite de envio da API. Atenção: o campo antigo foi descontinuado em favor de um novo, do nível do portfólio, e biblioteca desatualizada devolve valor errado.

### Mensagem recebida conta no limite?

Não. Os limites são de envio.

## Como decidir

Se você faz atendimento, o limite que importa é o por par, e a prática que o resolve é mandar uma mensagem por resposta em vez de vários balões. Se você faz disparo, o que importa é o limite da conta e a vazão da sua fila, porque o teto por segundo raramente é o gargalo real.

E antes de planejar volume, confirme se o número está em coexistência. Essa única informação muda o teto por um fator de quatro.

::cta: Confira duas coisas antes da próxima campanha | Em que modo o número está, porque coexistência corta o teto para 20 por segundo. E se o seu reenvio distingue 131049 de erro comum, porque insistir no primeiro limita a conta inteira.

## Leia também
- [WhatsApp API oficial no n8n](/whatsapp-api-oficial-n8n)
- [Posso mandar mensagem para qualquer número?](/posso-mandar-mensagem-para-qualquer-numero)
- [Número banido: o que fazer](/numero-banido-no-whatsapp-o-que-fazer)
- [Coexistência: API e aplicativo no mesmo número](/coexistencia-whatsapp-api-oficial-app-celular)

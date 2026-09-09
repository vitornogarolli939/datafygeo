---
title: "O telefone está sumindo do webhook: o que são BSUID e nomes de usuário"
description: "A Meta está trocando o telefone por um identificador por empresa. O número só aparece se você falou com aquela pessoa nos últimos 30 dias. Quem usa telefone como chave vai quebrar."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "o-telefone-esta-sumindo-do-webhook"
cluster: "implementacao"
hero: "webhook"
intent: "problema-urgente"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/business-scoped-user-ids/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://github.com/chatwoot/chatwoot/issues/13837
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=vGovcR8W5g8
  - https://www.youtube.com/watch?v=fhz6n2s91-g
videos: [fhz6n2s91-g, vGovcR8W5g8]
internal_links:
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /como-leio-o-historico-de-conversa-pela-api
  - /webhook-chega-duplicado
  - /coexistencia-whatsapp-api-oficial-app-celular
  - /api-oficial-vs-nao-oficial-whatsapp-2026
status: aprovado
pendencias: ["[VERIFICAR] o cronograma de liberação de nomes de usuário mudou mais de uma vez; confirme o estado atual antes de planejar migração"]
---

# O telefone está sumindo do webhook: o que são BSUID e nomes de usuário

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** a Meta está deixando de usar o telefone como identificador principal do usuário. No lugar entra o **BSUID**, um identificador que existe só na relação entre aquela pessoa e a sua empresa. E o ponto que quebra integração: **o telefone só aparece no webhook se você mandou mensagem para aquele número nos últimos 30 dias**, numa janela que corre.

Quem usa telefone como chave primária no banco vai ver contato duplicado, conversa órfã e busca que não acha ninguém, sem erro nenhum nos logs.

::numeros: 30 dias|a janela em que o telefone ainda aparece no webhook ;; 1 empresa|é o escopo do identificador: ele não vale entre portfólios ;; 131062|o erro de quem tenta autenticação sem telefone ;; user_id|o campo que sempre vem, mesmo quando o telefone não vem

## Principais pontos
- O **BSUID** identifica a pessoa **na relação com a sua empresa**. O mesmo cliente tem identificador diferente em cada empresa com quem fala, e ele é estável mesmo se a pessoa trocar de número.
- O campo `user_id` **sempre vem**. O `wa_id`, que é o telefone, pode não vir. O `username` só aparece se a pessoa ativou.
- **O telefone só é entregue se você falou com aquele número nos últimos 30 dias**, ou se a pessoa está na sua lista de contatos.
- Templates de autenticação com preenchimento automático **ainda exigem telefone**, e tentar enviá-los para um identificador devolve o erro **131062**.
- Existe um webhook próprio para avisar quando o identificador de alguém muda, e uma mensagem de sistema para o mesmo caso.

::diagrama: webhook-fluxo

## Como o identificador se parece

O formato é o código do país, um ponto e uma sequência:

```
US.13491208655302741918
```

Em conta corporativa que opera vários portfólios existe também uma variante com um segmento a mais, que identifica a pessoa no nível do grupo.

Duas propriedades importam para quem constrói:

**É por empresa.** O mesmo cliente tem identificadores diferentes em empresas diferentes. Isso é bom para privacidade e ruim para quem imaginava um identificador universal: você não consegue cruzar cliente entre marcas, e mandar mensagem de um número para um identificador gerado noutro portfólio simplesmente falha.

**É estável.** Se a pessoa trocar de telefone, o identificador continua o mesmo. Isso resolve um problema antigo, o de perder o histórico do cliente que mudou de número.

## O que muda no payload

Três campos convivem, e é preciso saber o que esperar de cada um:

| Campo | Quando vem |
|---|---|
| `user_id` | **Sempre** |
| `wa_id` (o telefone) | Só se você falou com esse número nos últimos 30 dias, ou se ele está na sua lista de contatos |
| `username` | Só se a pessoa ativou um nome de usuário |

Aparecem também campos correspondentes no envio e no recebimento, além de uma lista de contatos no evento. E existe um webhook específico que avisa quando o identificador de alguém muda, trazendo o valor anterior e o atual, mais uma mensagem de sistema para o mesmo caso.

## Por que isso quebra sistema que hoje funciona

O modelo mental antigo era simples: telefone é a pessoa. Quase todo sistema de atendimento foi construído assim, com o número como chave.

Com a janela de 30 dias, esse modelo falha em silêncio. O cliente some por dois meses e volta: agora ele chega sem telefone, só com identificador. Seu sistema não encontra ninguém com aquele telefone, porque não veio telefone, e cria um contato novo. O histórico fica órfão, o atendente não vê o que aconteceu antes, e nada nos logs indica erro.

O sintoma é esse: **contato duplicado e histórico que se perde**, sem exceção lançada em lugar nenhum. É por isso que vale tratar antes, e não quando aparecer.

## O detalhe que muda a modelagem: o identificador é da relação, não da pessoa

Se você lê uma coisa só desta página, leia esta. O identificador **não é global**. Ele identifica o par entre uma pessoa e uma empresa.

Na explicação do Israel: *"eu tenho o meu WhatsApp Business, o João entrou em contato comigo, o user ID do João vai ser um entre eu e ele. Se o João entrar em contato com outro WhatsApp Business, uma outra empresa, o user ID do João vai ser outro."*

::video: fhz6n2s91-g | Cinco minutos direto ao ponto. Em 01:27 ele explica que o identificador é da relação, e em 02:30 mostra o campo que muda no envio para responder por ele.

As consequências disso na modelagem são grandes, e todas contraintuitivas se você estava tratando telefone como chave:

**A chave do seu contato é composta.** É o identificador **mais** o número da sua conta que o recebeu. Guardar só o identificador funciona enquanto você opera um número e quebra no dia em que opera dois, porque a mesma pessoa aparece com identificadores diferentes em cada um.

**Se você é SaaS multicliente, isso é ainda mais forte.** O mesmo consumidor final falando com dois dos seus clientes tem dois identificadores. Deduplicar contato entre clientes por esse campo é impossível, e é bom que seja: são relações separadas, e tratá-las como uma só seria misturar base de clientes diferentes.

**Não dá para usar como identidade universal.** Ele não serve para casar a pessoa com o cadastro que você já tem no seu banco, nem para reconhecer o mesmo usuário em outro canal.

**Mudar de fornecedor não preserva nada disso automaticamente.** A relação continua sendo com a sua conta, e é ela que precisa continuar a mesma.

## Como responder por ele

A mudança no envio é pequena e não é óbvia: em vez do campo de destinatário por telefone, você usa o campo de destinatário por identificador. E o valor tem que vir **de dentro do objeto de mensagem**, não do topo do payload, [pelo mesmo motivo que evita laço de status](/webhook-chega-duplicado).

## O que fazer, em ordem

**1. Guarde o identificador desde já.** Adicione a coluna, preencha com o que chega, e crie índice. Isso é reversível e barato.

**2. Passe a casar contato pelo identificador primeiro.** A ordem certa é: procurar por identificador; se não achar, procurar por telefone; se achar por telefone, gravar o identificador naquele registro. Assim o sistema vai aprendendo a chave nova sem quebrar a antiga.

**3. Trate a ausência de telefone como normal.** Se o seu código assume que o telefone sempre existe, ele vai falhar. Campo que pode não vir precisa ser tratado como opcional, inclusive na interface do atendente.

**4. Guarde o nome de usuário quando vier.** Serve para exibir e para o atendente reconhecer a pessoa, já que o telefone pode não estar ali.

**5. Trate o evento de mudança de identificador.** Quando ele chega, atualize o registro em vez de criar um novo. É o que evita duplicata em quem trocou de número.

**6. Não jogue fora o telefone que você já tem.** Ele continua necessário para autenticação e continua sendo o que a sua equipe reconhece. O que muda é que ele deixa de ser a única chave.

## O caso que ainda exige telefone

Templates de autenticação com preenchimento automático, código de toque único e botão de copiar código **continuam exigindo o número**. Tentar enviá-los endereçando pelo identificador devolve o erro **131062**.

Se o seu produto manda código de verificação por WhatsApp, esse fluxo precisa continuar guardando telefone. Vale marcar isso no código com um comentário explicando o porquê, senão alguém vai "limpar" essa dependência numa refatoração futura.

## Por que isso é urgente agora

Este é um dos assuntos com mais movimento no ecossistema em 2026. Só no GitHub, foram cerca de dezesseis discussões em seis meses, envolvendo plataformas de atendimento e bibliotecas populares. A discussão mais movimentada chegou a mais de quarenta comentários, com times de produto se organizando para dar conta antes da liberação ampla.

Ou seja: não é um detalhe de documentação que ninguém aplicou. É uma mudança que já está chegando nos webhooks de produção.

## Perguntas frequentes

### Meu sistema vai parar de funcionar?

Não de uma vez. Ele vai passar a criar contato duplicado para quem volta depois de 30 dias, e o histórico vai se dividir. É uma degradação silenciosa, não uma queda.

### Posso continuar mandando mensagem por telefone?

Pode, quando você tem o telefone. O envio aceita os dois caminhos, e o telefone tem precedência se os dois forem informados.

### O identificador serve para achar o cliente em outra empresa?

Não. Ele é por empresa, e é isso que o torna seguro do ponto de vista de privacidade.

### E se o cliente trocar de número?

O identificador continua o mesmo, e chega um evento avisando da mudança. Esse é o ganho real da mudança: você deixa de perder o histórico de quem trocou de chip.

### Preciso pedir o nome de usuário ao cliente?

Não. Ele só aparece se a pessoa tiver ativado, e é informativo.

### Isso muda quem eu posso contatar?

Não. A janela de 24 horas e a exigência de template continuam iguais. O que muda é como você identifica a pessoa, não quando pode falar com ela.

## Como decidir

Se o seu produto guarda conversa, comece a gravar o identificador esta semana. É uma coluna, um índice e uma mudança na busca de contato: horas de trabalho agora, contra reconciliar histórico dividido depois.

Se você só dispara notificação e não mantém histórico, o impacto é menor, mas ainda vale guardar o identificador para quando precisar.

::cta: Uma mudança de código resolve a maior parte | Procure o contato pelo identificador primeiro, e só depois pelo telefone. Quando achar por telefone, grave o identificador naquele registro. O sistema aprende a chave nova sozinho, sem migração de banco.

## Leia também
- [Webhook: receber mensagens em tempo real](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [Meu webhook recebe a mesma mensagem várias vezes](/webhook-chega-duplicado)
- [Como leio o histórico de conversa pela API](/como-leio-o-historico-de-conversa-pela-api)
- [Coexistência: API e aplicativo no mesmo número](/coexistencia-whatsapp-api-oficial-app-celular)

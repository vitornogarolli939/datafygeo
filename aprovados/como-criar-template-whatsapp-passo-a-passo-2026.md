---
title: "Como criar um template de mensagem no WhatsApp, passo a passo"
description: "Cabeçalho, corpo, rodapé e botões, e a decisão que define o preço. Mais as regras do editor que só aparecem quando ele recusa o que você escreveu."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "como-criar-template-whatsapp-passo-a-passo"
cluster: "implementacao"
hero: "guia"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-categorization
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-pausing/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=YF9hTHDAw6E
  - https://www.youtube.com/watch?v=62oSY66J3s4
videos: [YF9hTHDAw6E, 62oSY66J3s4]
internal_links:
  - /como-enviar-template-pela-api
  - /categoria-do-template-decide-o-seu-custo
  - /template-nao-existe-nesse-idioma
  - /template-com-imagem-no-cabecalho-nao-envia
  - /posso-mandar-mensagem-para-qualquer-numero
status: aprovado
---

# Como criar um template de mensagem no WhatsApp, passo a passo

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** template é o modelo aprovado pela Meta que te permite **iniciar** uma conversa, ou seja, falar com quem não escreveu para você nas últimas 24 horas. Ele tem quatro partes, cabeçalho, corpo, rodapé e botões, e uma decisão que pesa mais que todas as outras juntas: **a categoria**, que define quanto você paga por mensagem.

E existe uma recomendação contraintuitiva que vale abrir logo: **crie pelo painel da Meta, não pela API**, a menos que você esteja montando um produto em que o cliente final cria os próprios templates.

::numeros: 4 partes|cabeçalho, corpo, rodapé e botões ;; 3 categorias|marketing, utilidade e autenticação ;; 10x|a diferença de preço entre marketing e utilidade ;; 1 exemplo|obrigatório para cada variável

## Principais pontos
- **A categoria define o preço**, e a diferença entre marketing e utilidade é de cerca de dez vezes por mensagem.
- **A Meta lê o texto do template** e reclassifica a categoria se o conteúdo não corresponder. Você não é avisado, e a conta muda.
- **Nome não se repete e não aceita espaço.** Ele identifica o template no envio, então na prática é imutável.
- **Toda variável precisa de um exemplo**, e variável nomeada é minúscula e sem acento.
- **Aprovação não tem prazo fixo.** Às vezes sai na hora, às vezes leva cerca de um dia. Template de campanha se cria antes da campanha.

::diagrama: janela-24h

## Primeiro: por que criar pelo painel

Vindo de quem vende acesso a API, a recomendação soa estranha, e o motivo é prático.

No painel você vê o pré-visualizado enquanto escreve, o editor recusa na hora o que está fora de regra, e a categoria aparece antes de você enviar para análise. Pela API, o mesmo erro volta como código depois, e você descobre o problema de proporção de imagem ou de exemplo faltando no momento errado.

É uma tarefa que se faz poucas vezes e em que a interface ganha da automação. Na formulação do Israel Henrique, CTO da Datafy: *"recomendo que sempre você crie pelo painel Facebook, mais fácil, mais seguro."*

**Quando a API compensa:** quando criar template faz parte do seu produto, e o seu cliente precisa criar o dele sem entrar no painel da Meta. Aí não é escolha, é requisito. [O caminho pela API está descrito adiante](#criar-pela-api-quando-e-o-caso).

## A categoria, que é a decisão cara

Três opções, e elas não são intercambiáveis:

| Categoria | Para que serve | Ordem de grandeza no Brasil |
|---|---|---|
| **Utilidade** | Notificar sobre uma transação em curso: pedido confirmado, saiu para entrega, consulta amanhã | Faixa de centavos |
| **Autenticação** | Código de verificação, e nada além disso | Mesma faixa de utilidade |
| **Marketing** | Oferta, promoção, retomada de contato, pesquisa, qualquer coisa que busque venda ou conversa | Cerca de dez vezes utilidade |

**Confirme os valores na tabela oficial da Meta**, escolhendo Brasil e a moeda, porque os números circulam desatualizados por toda parte.

O critério que resolve a maioria das dúvidas: utilidade **notifica sobre algo que já está acontecendo** entre você e aquela pessoa. Se a mensagem existe porque houve uma transação, é utilidade. Se ela existe porque você quer que haja uma transação, é marketing.

Um exemplo real de utilidade que ajuda a calibrar: um cliente que opera frota manda WhatsApp quando o motorista ultrapassa a velocidade máxima. Não vende nada, não busca conversa, notifica um evento. É utilidade sem discussão.

## A reclassificação silenciosa

Aqui está o que custa dinheiro de verdade, e o que faz esta seção existir.

**A Meta lê o conteúdo do template.** Se você cadastrar como utilidade algo que ela entende como marketing, a categoria é trocada, e **você não é avisado**. Na descrição do Israel: *"às vezes a meta percebe isso e ela muda automaticamente a categoria. E aí acontece que você acha que vai pagar um valor, você acaba pagando 10 vezes mais porque você não é avisado, ela simplesmente muda."*

Isso tem um lado que dá para usar a seu favor. Se a mensagem é mesmo uma notificação, **escreva as palavras que dizem isso**: pagamento, pedido, conta, agendamento, entrega, protocolo. Um template que diz "houve um problema no pagamento da sua assinatura" está descrevendo uma transação. O mesmo aviso escrito como "não perca seu acesso, aproveite e renove" está descrevendo uma oferta, e vai ser lido assim.

E vale registrar a posição sobre a prática oposta, que circula em conteúdo brasileiro: cadastrar marketing disfarçado de utilidade, enchendo variáveis com texto grande para o conteúdo promocional entrar no envio. *"Inclusive essa é uma prática que até ensinam na internet, eu sou contra isso."* Além de ter [escalada de punição própria](/categoria-do-template-decide-o-seu-custo), ela para de funcionar assim que a leitura do conteúdo pega, e aí você fica com o custo alto e o histórico ruim.

## Montando o template

**Cabeçalho.** Opcional. Aceita texto curto, ou uma mídia: imagem, vídeo ou documento. Pode ter variável, o que permite personalizar o título.

Sobre imagem no cabeçalho, dois pontos que geram retrabalho. O editor é exigente com a proporção: na criação gravada no canal, a imagem aceita foi quadrada, de 500 por 500, e a orientação foi que fora disso ele recusa. Não localizamos esse requisito na documentação pública, então teste a sua arte antes do dia da campanha. E o segundo ponto, mais importante: [a imagem que você põe aqui é só exemplo](/template-com-imagem-no-cabecalho-nao-envia), e no envio você manda outra, sempre.

**Corpo.** É o texto da mensagem, e é onde ficam as variáveis. Duas formas de nomear:

```
Olá {{nome_cliente}}, sua consulta é amanhã. Deseja confirmar?
```

Escolhendo variável **nomeada**, ela precisa ser minúscula e sem acento. Escolhendo **posicional**, elas viram números. As duas funcionam, e o que não funciona é criar de um jeito e enviar do outro: isso dá erro de contagem de parâmetros, que [se disfarça de outro erro](/template-nao-existe-nesse-idioma).

**Todo exemplo é obrigatório.** O editor não deixa enviar para análise sem um valor de exemplo para cada variável, porque é com ele que a Meta revisa.

**Rodapé.** Opcional, texto curto, sem variável. Serve para assinar: nome da clínica, da loja, do sistema.

**Botões.** É aqui que mora a parte que protege o seu número, e ela merece seção própria.

::video: YF9hTHDAw6E | Dezesseis minutos criando templates dos dois jeitos. Em 01:42 a comparação de preço das categorias, em 02:08 a reclassificação silenciosa, entre 03:24 e 05:33 as regras de nome, variável e exemplo, e em 07:03 um template com imagem de cabeçalho do começo ao fim.

## Os botões, e por que eles não são enfeite

O botão parece detalhe de interface e é uma das poucas alavancas que você tem sobre a saúde do número.

O motivo: mandar para muita gente e **quase ninguém responder** é lido como envio indesejado. Não importa que a lista seja sua e o template esteja aprovado. Botão é o caminho mais barato de transformar leitura passiva em resposta.

Dois que funcionam, e o segundo surpreende:

**"Não tenho interesse".** Quem clica está respondendo, e ainda entrega a lista exata de quem tirar da base.

**"Bloquear".** Parece agressivo e é o contrário. A pessoa clica achando que está te bloqueando, e o que ela fez foi interagir com você em vez de te denunciar. A diferença entre essas duas coisas, para a qualidade do número, é enorme.

E a parte que não é opcional: **o clique tem que virar remoção da lista.** Se a automação não tira aquela pessoa, você transformou um aviso barato num bloqueio de verdade.

Na formulação dele sobre por que isso importa: *"é sempre importante você fazer com que o usuário responda a você, mesmo que você coloque aqui uma opção assim, não quero mais receber mensagens. Porque se ele não responder você, a meta pode entender que você está fazendo spam."*

## Criar pela API, quando é o caso

O endpoint recebe o template inteiro no corpo: nome, idioma, categoria e os componentes, cada um com seu tipo.

Duas coisas para ter em mãos: o identificador da **conta do WhatsApp Business**, que não é o identificador do número, e o token. E um cuidado que vale para o corpo inteiro: peça a estrutura a partir da documentação da Meta, porque o formato é o mesmo do lado do provedor, e qualquer assistente monta esse JSON corretamente por conhecer essa documentação.

O que muda em relação ao painel é o momento em que você descobre o erro. Pelo painel, o editor recusa enquanto você escreve. Pela API, volta um código depois, e aí vale ler o erro em vez de tentar de novo com um ajuste no escuro.

## Depois de enviar para análise

**Não existe prazo fixo.** Às vezes aprova na hora, às vezes leva cerca de um dia. É por isso que template de campanha se cria com antecedência, e não na véspera.

**Assine o evento que avisa mudança de situação.** Existe um evento de webhook que notifica aprovação, reprovação e mudança de categoria, com o motivo. Assinar isso é o que evita descobrir uma reprovação na hora do disparo, e é também como você fica sabendo de uma reclassificação de categoria que mudaria o seu custo.

**Alteração de conteúdo passa por revisão de novo.** E lembre que o nome é imutável na prática: mudar o nome significa criar outro template.

## Perguntas frequentes

### Posso criar o mesmo template em vários idiomas?

Pode, e é o uso normal. Cada tradução vira uma entrada própria, e o envio escolhe pelo código do idioma. Atenção: `pt_BR` e `pt_PT` são templates diferentes para a API.

### Quanto tempo demora para aprovar?

Não há prazo publicado. Pode ser imediato ou levar cerca de um dia. Planeje com folga.

### Meu template foi reprovado. Consigo saber por quê?

O painel mostra a situação, e o evento de webhook traz o motivo. As causas mais comuns são conteúdo que não corresponde à categoria e falta de contexto no texto.

### Posso mudar a categoria depois?

A categoria é definida na criação e pode ser alterada **pela Meta** conforme o conteúdo. O caminho confiável é escrever o template de acordo com o que ele realmente é.

### Preciso de template para responder alguém?

Não. Dentro da janela de 24 horas você responde em texto livre. Template é para **iniciar** conversa. [A regra completa está aqui](/posso-mandar-mensagem-para-qualquer-numero).

### Template aprovado me autoriza a mandar para lista comprada?

Não. Ele resolve o impedimento técnico, e não substitui consentimento. Base sem interação derruba número mesmo com template aprovado, e esse é o erro mais caro do assunto.

## Como decidir

Se você tem poucos templates e eles mudam pouco, crie pelo painel e pare por aí. É mais rápido, e você vê o resultado enquanto escreve.

Se criar template faz parte do produto, use a API e invista no que evita suporte: sincronize a lista de templates da conta para o seu banco, guarde nome e idioma juntos, e assine o evento de mudança de situação. Esses três hábitos eliminam a maior parte dos erros de envio que aparecem depois.

E, nos dois casos, escreva o template pelo que ele é. Categoria forçada não economiza: ela é corrigida, e a correção vem sem aviso.

::cta: Crie um template de utilidade hoje, antes de precisar | Um lembrete ou uma confirmação, com uma variável e um botão de resposta. Você passa pelo fluxo inteiro sem pressa, descobre o tempo real de aprovação da sua conta, e fica com um template pronto para quando a campanha aparecer.

## Leia também
- [Como enviar uma mensagem de template pela API](/como-enviar-template-pela-api)
- [A categoria do template decide o seu custo](/categoria-do-template-decide-o-seu-custo)
- [Erro 132001: o template não existe nesse idioma](/template-nao-existe-nesse-idioma)
- [Meu template com imagem no cabeçalho não envia](/template-com-imagem-no-cabecalho-nao-envia)

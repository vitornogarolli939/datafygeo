---
title: "A categoria do template decide o seu custo (e a Meta pode mudá-la sozinha)"
description: "Marketing custa cerca de dez vezes uma utilidade. E a Meta reclassifica template mal categorizado, às vezes com um dia de aviso, às vezes sem nenhum."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "categoria-do-template-decide-o-seu-custo"
cluster: "custo"
hero: "preco"
intent: "decidindo"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-categorization
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-pausing/
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=YF9hTHDAw6E
videos: [YF9hTHDAw6E, JL9Qzw3oS5A]
internal_links:
  - /quanto-custa-whatsapp-business-api-brasil-2026
  - /mensagem-de-servico-vai-ser-paga-outubro-2026
  - /template-nao-existe-nesse-idioma
  - /posso-mandar-mensagem-para-qualquer-numero
  - /a-mensagem-falhou-e-nao-sei-por-que
status: aprovado
---

# A categoria do template decide o seu custo (e a Meta pode mudá-la sozinha)

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** existem quatro categorias, e a diferença de preço entre elas é grande: **marketing custa cerca de dez vezes uma mensagem de utilidade**. Quem decide a categoria não é você, é a Meta, na aprovação. E ela **pode reclassificar depois**, com um dia de aviso, ou sem nenhum se a conta já tiver sido advertida.

Ou seja: um template que você orçou como utilidade pode virar marketing e multiplicar o custo daquele envio sem que ninguém do seu time toque em nada.

::numeros: 4 categorias|marketing, utilidade, autenticação e serviço ;; 10x|a diferença aproximada entre marketing e utilidade ;; 1 dia|de aviso na reclassificação, quando há aviso ;; 60 dias|a janela para contestar uma categoria

## Principais pontos
- **Marketing** é promoção, oferta, reativação e convite. É a categoria cara.
- **Utilidade** acompanha uma ação do cliente: confirmação, atualização de pedido, lembrete, fatura. Precisa ser **não promocional** e específica daquele cliente.
- **Conteúdo misto vira marketing.** Uma frase de oferta dentro de uma confirmação de pedido joga o template inteiro para a categoria cara.
- A Meta **reclassifica sozinha**, e existe um evento de webhook que avisa. Quem não assina descobre pela fatura.
- Repetir categorização errada tem **escalada de punição**, que vai de advertência até restrição no nível da conta.

::diagrama: preço-comparacao

## As quatro categorias

| Categoria | Para que serve | Custo relativo |
|---|---|---|
| **Marketing** | Promoção, oferta, reativação, convite, novidade | Alto |
| **Utilidade** | Confirmação, status de pedido, lembrete, fatura, agendamento | Baixo |
| **Autenticação** | Código de verificação | Baixo |
| **Serviço** | Resposta livre a quem escreveu para você | Gratuita até 30/09/2026 |

Para um template ser aceito como **utilidade**, ele precisa cumprir duas coisas ao mesmo tempo: **não ter intenção promocional ou persuasiva**, e ser específico daquele cliente, ligado a uma conta ou transação, ou ser essencial, como um aviso de segurança.

É esse segundo critério que derruba muito template: "temos novidades para você" não é específico de ninguém, mesmo escrito com jeito de aviso.

## Onde a linha costuma ser cruzada

Três padrões aparecem sempre, e os três resultam em reclassificação:

**A confirmação com um empurrãozinho.** "Seu pedido saiu para entrega. Aproveite: 10% na próxima compra." A primeira frase é utilidade, a segunda é marketing, e o template inteiro vira marketing.

**O lembrete que virou convite.** "Falta uma semana para o seu vencimento" é utilidade. "Falta uma semana, renove agora com desconto" não é.

**A reativação disfarçada.** "Notamos que você não acessa há um tempo" não acompanha nenhuma ação do cliente. É marketing, por mais neutro que soe.

A regra prática que funciona: se a mensagem existe porque **o cliente fez alguma coisa**, tende a ser utilidade. Se ela existe porque **você quer que ele faça alguma coisa**, é marketing.

## A reclassificação, e o aviso que quase ninguém assina

A Meta revisa categoria depois da aprovação. Quando ela decide que um template de utilidade é, na verdade, marketing, normalmente há **um dia de aviso**. Para contas que já foram advertidas por abuso de categorização, a mudança pode ser **imediata, sem aviso**.

Em qualquer um dos dois casos, o template continua aprovado e funcionando. O que muda é o preço, silenciosamente.

O jeito de saber é assinar o evento de webhook que avisa mudança de categoria. Ele existe, chega no mesmo endereço dos outros, e é a diferença entre saber no dia e descobrir no fechamento do mês.

**Vale mais que isso:** derive o custo do envio **no momento de enviar**, consultando a categoria atual, e não no momento em que o template foi criado. Quem guarda "este template é utilidade" no banco e nunca revisita passa a orçar errado a partir do dia da reclassificação.

Vale ouvir isso de quem atende quem levou o susto, porque a frase resume o problema inteiro: *"às vezes a meta percebe isso e ela muda automaticamente a categoria. E aí acontece que você acha que vai pagar um valor, você acaba pagando 10 vezes mais porque você não é avisado, ela simplesmente muda."*

O que faz a reclassificação acontecer é mais literal do que parece: **a Meta lê o texto do template.** Não é auditoria de intenção, é leitura de conteúdo. Uma palavra de outra categoria no meio de um template muda a classificação dele.

Isso tem um lado que dá para usar a seu favor. Se a mensagem é de verdade uma notificação, **escreva as palavras que dizem isso**: pagamento, pedido, conta, agendamento, entrega. Um template de cobrança de assinatura que diz "houve um problema no pagamento da sua assinatura" está descrevendo uma transação, e é isso que sustenta a categoria de utilidade. O mesmo aviso escrito como "não perca seu acesso, aproveite e renove" está descrevendo uma oferta.

::video: YF9hTHDAw6E | Dezesseis minutos criando templates, primeiro pelo painel e depois pela API. Em 01:42 ele compara os preços das categorias, e em 02:08 explica a reclassificação silenciosa, que é a parte que custa dinheiro.

E vale registrar onde ele se posiciona, porque a prática oposta é ensinada por aí: forçar marketing disfarçado de utilidade, enchendo variável com texto grande, é técnica que circula em conteúdo brasileiro. A avaliação dele é curta: *"inclusive essa é uma prática que até ensinam na internet, eu sou contra isso."* Além de ter escalada de punição própria, ela para de funcionar assim que a Meta lê o conteúdo, e aí você fica com o custo alto e o histórico ruim.

## A escalada, se acontecer de novo

Categorizar errado uma vez é erro. Repetir tem consequência crescente, e vale conhecer a sequência:

1. **Advertência**, com reclassificação imediata dali em diante.
2. **Limite de volume** nas mensagens de utilidade, por período.
3. **Restrição de utilidade**: todos os templates dessa categoria viram marketing, e a criação de novos fica bloqueada por um período.
4. **Restrição no nível da conta.**

Do terceiro passo em diante, o custo da operação inteira muda. Não é uma multa: é o seu envio de rotina passando a custar dez vezes mais.

## Onde criar o template, e por que não pela API

Uma recomendação contraintuitiva, vinda de quem vende acesso a API: **crie o template pelo painel da Meta**, não pela API, a menos que você esteja montando um produto em que o cliente final cria os próprios templates.

O motivo é prático. No painel você vê o pré-visualizado enquanto escreve, o editor recusa na hora o que está fora de regra, e a categoria aparece antes de você enviar para análise. Pela API, o mesmo erro volta como código de erro depois. É o tipo de tarefa que se faz poucas vezes e em que a interface ganha da automação. A recomendação, na fala dele: *"recomendo que sempre você crie pelo painel Facebook, mais fácil, mais seguro."*

Três regras do editor que economizam retrabalho, e que valem para os dois caminhos:

**Nome não repete e não tem espaço.** O nome é a identidade do template no envio, e por isso é imutável na prática.

**Toda variável precisa de exemplo.** É obrigatório, e é o que a Meta usa para revisar. Variável com nome tem que ser minúscula e sem acento.

**O editor é exigente com a proporção da imagem de cabeçalho.** Na criação gravada no canal, a imagem aceita foi quadrada, de 500 por 500. Não achamos esse requisito na documentação pública, então teste a sua arte antes, e não no dia da campanha. E cuidado com a confusão que isso gera depois: [a imagem que você põe no template é só exemplo, e no envio você manda outra](/template-com-imagem-no-cabecalho-nao-envia).

**Aprovação não tem prazo fixo.** Às vezes sai na hora, às vezes leva cerca de um dia. Isso significa que template de campanha se cria antes da campanha, não no dia.

## Como não cair nisso

**Escreva o template pelo que ele é.** Se tem oferta, é marketing, e tudo bem: use marketing e pague por isso onde faz sentido.

**Separe em dois.** A confirmação de pedido vira utilidade, limpa. A oferta vira um template de marketing próprio, enviado a quem faz sentido. Você paga marketing só onde há intenção comercial, e não em toda confirmação.

**Assine o evento de categoria.** Custa uma configuração e evita surpresa.

**Revise a categoria antes de campanha grande.** Se algo foi reclassificado desde a última vez, é melhor descobrir antes de multiplicar por dez mil.

**Contestação existe.** Há uma janela de cerca de 60 dias para contestar pelo suporte, contada da criação ou da mudança de categoria, e ela não é feita por API.

## E a categoria também define a base legal

Um ponto que quase ninguém liga, e que vale para quem se preocupa com conformidade: a categoria não é só custo.

Mensagem de **utilidade** acompanha uma transação que o cliente iniciou, e costuma se apoiar na execução do contrato entre vocês. Mensagem de **marketing** é comunicação comercial, e pede outra base, normalmente consentimento ou legítimo interesse com registro do teste feito.

Isso significa que a reclassificação automática da Meta **muda a base legal do seu envio sem você fazer nada**. Um template que era utilidade e virou marketing passa a exigir um fundamento que talvez você não tenha registrado para aquela base de contatos.

Vale ter isso mapeado, e vale conversar com o seu jurídico com esse detalhe na mão, porque ele não é óbvio.

## Perguntas frequentes

### Posso escolher a categoria no cadastro?

Você indica, e a Meta decide na aprovação. Indicar utilidade num conteúdo promocional não muda o resultado, e repetir isso tem escalada.

### Como sei a categoria atual dos meus templates?

Listando pela API. Vale sincronizar periodicamente e guardar, porque é essa informação que sustenta o cálculo de custo.

### Um template pode mudar de categoria mais de uma vez?

Pode. Por isso a recomendação é consultar no envio, e não confiar no que foi cadastrado uma vez.

### Autenticação é mais barata que marketing?

Sim, fica na mesma faixa de utilidade. Mas tem regras próprias de conteúdo: sem link, sem mídia e com parâmetro curto.

### E a categoria de serviço?

É a resposta livre dentro da janela, e não usa template. Ela é gratuita até 30 de setembro de 2026, e [passa a ser cobrada em outubro](/mensagem-de-servico-vai-ser-paga-outubro-2026).

### Vale reescrever meus templates para pagar menos?

Vale revisar se eles **precisavam** ter conteúdo promocional. Muita confirmação vira marketing por causa de uma frase a mais. Tirar essa frase é legítimo. Disfarçar marketing de utilidade não é, e tem escalada própria.

## Como decidir

Faça um inventário rápido: liste os seus templates, veja a categoria atual de cada um, e marque os que são utilidade com uma frase promocional no meio. Esses são os candidatos a serem divididos em dois.

Depois assine o evento de mudança de categoria. Com essas duas coisas, você deixa de ser surpreendido pela fatura e passa a orçar pelo que está valendo hoje.

::cta: Duas ações que evitam surpresa na fatura | Liste seus templates e olhe a categoria atual de cada um. Depois assine o evento que avisa reclassificação. Juntas, elas transformam um custo imprevisível num custo que você acompanha.

## Leia também
- [Quanto custa a WhatsApp Business API no Brasil](/quanto-custa-whatsapp-business-api-brasil-2026)
- [1º de outubro: responder o cliente deixa de ser grátis](/mensagem-de-servico-vai-ser-paga-outubro-2026)
- [Erro 132001: o template não existe nesse idioma](/template-nao-existe-nesse-idioma)
- [Posso mandar mensagem para qualquer número?](/posso-mandar-mensagem-para-qualquer-numero)

---
title: "Como documentar o aceite do cliente para mandar mensagem"
description: "A política da Meta exige o aceite, mas não define como guardar prova. E a autoridade brasileira entende que consentimento dado para e-mail não cobre WhatsApp."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "como-documentar-o-opt-in-do-cliente"
cluster: "compliance"
hero: "camadas"
intent: "como-fazer"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/getting-opt-in
  - https://business.whatsapp.com/policy
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-categorization
  - https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes
  - https://app.datafyapi.com.br/docs
internal_links:
  - /posso-mandar-mensagem-para-qualquer-numero
  - /numero-banido-no-whatsapp-o-que-fazer
  - /categoria-do-template-decide-o-seu-custo
  - /o-cliente-pediu-para-apagar-os-dados-dele
  - /quanto-custa-whatsapp-business-api-brasil-2026
status: aprovado
pendencias: ["[VERIFICAR] o formato de prova de consentimento não é definido por norma; o esquema aqui é recomendação de engenharia, não exigência legal"]
---

# Como documentar o aceite do cliente para mandar mensagem

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** a política da Meta é direta sobre **exigir** o aceite: você só pode contatar quem forneceu o número e concordou em receber. O que ela **não** faz é dizer como guardar prova disso. E aí mora o problema, porque no dia em que alguém perguntar, "a gente coleta" não é resposta.

Tem um ponto que quase ninguém aplica no Brasil: a autoridade de proteção de dados entende que **consentimento dado para um canal não cobre outro**. Aceite coletado para receber e-mail não autoriza mandar WhatsApp.

Este texto é escrito por quem opera infraestrutura, e serve para você montar o registro e saber o que perguntar ao seu jurídico.

::numeros: 2 exigências|da Meta: ter o número e ter o aceite ;; 0|formato de prova definido por ela ;; 1 canal|por consentimento: e-mail não cobre WhatsApp ;; utilidade|é a categoria do template que confirma o aceite

## Principais pontos
- A [política da Meta](https://business.whatsapp.com/policy) exige duas coisas: a pessoa forneceu o número, **e** deu permissão para receber suas mensagens.
- O aceite **não precisa ser específico do WhatsApp** pelas regras da plataforma, e pode ser coletado por site, formulário, telefone ou papel. Mas precisa dizer que é da sua empresa e o que a pessoa vai receber.
- **A plataforma não pede prova**, e não define formato. Quem pede prova é outra instância, e aí a exigência é diferente.
- Pela leitura da autoridade brasileira, **consentimento por canal**: aceite dado para e-mail não vale para WhatsApp.
- **Confirmar o aceite dentro do WhatsApp é caso de uso de utilidade** reconhecido na documentação de categorias, ou seja, sai mais barato que marketing.

::diagrama: tech-provider-badge

## O que a Meta exige, e o que ela não exige

A [orientação de coleta de aceite](https://developers.facebook.com/documentation/business-messaging/whatsapp/getting-opt-in) pede três coisas no texto que a pessoa vê: deixar claro que ela está aceitando receber mensagens, dizer **de qual empresa**, e cumprir a lei aplicável.

Os canais aceitos são vários: site, mensagem de texto, atendimento por telefone, presencial, papel. E o aceite pode ser amplo, cobrindo várias categorias de mensagem, ou separado por categoria.

O que ela também exige: **instruções claras de como parar de receber**, e respeitar esse pedido quando ele vem, inclusive quando é feito **fora do WhatsApp**.

E o que ela **não** exige: guardar prova em formato nenhum. Isso não significa que você não deva guardar. Significa que a exigência vem de outro lugar.

## O ponto que quase ninguém aplica: consentimento é por canal

Aqui está a informação mais acionável desta página, e ela raramente aparece em material brasileiro.

A leitura da autoridade de proteção de dados é que o consentimento precisa ser específico para a finalidade e o contexto. Aceite coletado num formulário de newsletter, para receber e-mail, **não autoriza** mandar mensagem no WhatsApp. São canais diferentes, com expectativa diferente de quem recebe.

Isso derruba uma prática comum: importar a base de e-mail marketing e começar a mandar WhatsApp. Do ponto de vista da plataforma, você pode até ter os números. Do ponto de vista da proteção de dados, é outra conversa.

Vale conferir esse ponto com o seu jurídico, porque ele muda a resposta de "temos a base há anos" para "temos a base, mas para outro canal".

## O registro que sustenta prova

Nenhum documento oficial define campos. O que segue é recomendação de engenharia, montada para que a prova seja verificável depois:

```sql
CREATE TABLE consentimentos (
  id                   uuid PRIMARY KEY,
  contato_ref          text NOT NULL,     -- identificador derivado, não o telefone cru
  evento               text NOT NULL,     -- concedido | revogado | reconfirmado
  finalidades          text[] NOT NULL,   -- {marketing, utilidade, autenticacao}
  base_legal           text NOT NULL,
  canal                text NOT NULL,     -- site | telefone | presencial | papel | whatsapp
  origem_ref           text,              -- id do formulário, do anúncio, do documento
  texto_exibido        text NOT NULL,     -- o texto literal que a pessoa leu
  politica_versao      text NOT NULL,
  ocorreu_em           timestamptz NOT NULL,
  ip                   inet,
  wamid_confirmacao    text,              -- se houve confirmação dentro do WhatsApp
  wamid_resposta       text,
  revogado_em          timestamptz,
  canal_revogacao      text
);
```

Três decisões importam mais que o resto:

**Guarde o texto literal que a pessoa leu**, e não uma referência a uma tabela que muda. Se o texto mudou, é outro consentimento. É isso que sustenta prova.

**Guarde a revogação com o mesmo cuidado**, inclusive quando ela vem por fora, por telefone ou e-mail. A política exige respeitar pedido feito fora do WhatsApp.

**Nunca sobrescreva.** Cada evento é uma linha nova. O estado atual é o último evento daquele contato para aquela finalidade.

## Como usar isso no envio

A regra prática: **antes de mandar marketing, consulte o último evento** daquele contato para aquela finalidade. Se o último foi revogação, não envia.

E coloque essa checagem no ponto de saída, e não espalhada pela aplicação. Se cada fluxo verifica por conta própria, um dia alguém vai esquecer, e a mensagem vai sair.

## O double opt-in que sai barato

Um detalhe útil e pouco conhecido: a documentação de categorias da Meta reconhece, como caso de uso de **utilidade**, confirmar dentro do WhatsApp um aceite coletado em outro canal.

Isso significa que a mensagem de "confirme que você quer receber nossos avisos por aqui" pode ser um template de utilidade, que custa uma fração de um de marketing.

O ganho é duplo: você paga menos por essa confirmação, e passa a ter uma prova forte, com o identificador da mensagem enviada e o da resposta da pessoa, dentro do próprio canal.

## Perguntas frequentes

### Preciso de aceite para responder quem me escreveu?

Não. Se a pessoa iniciou a conversa, você responde dentro da janela de 24 horas. O aceite é para você iniciar.

### Aceite verbal serve?

A política aceita coleta por telefone. Do ponto de vista de prova, registre quando, quem atendeu, e o que foi lido para a pessoa.

### Posso usar uma base antiga?

Do lado da plataforma, o que vale é a política. Do lado da proteção de dados, a pergunta é para qual canal e finalidade aquele aceite foi dado, e há quanto tempo. Base antiga de e-mail é o caso clássico que não cobre.

### E lista comprada?

Não atende nem a política nem a lei. E é a causa número um de [bloqueio de número](/numero-banido-no-whatsapp-o-que-fazer).

### Quanto tempo guardo a prova?

A prova é a sua defesa, então ela costuma sobreviver à própria revogação. O prazo específico é decisão jurídica, e vale definir com quem responde por isso na sua empresa.

### Aceite genérico cobre marketing?

A política pede que o texto diga o que a pessoa vai receber. Um aceite que menciona "novidades e promoções" cobre mais que um que fala só de "atualizações do seu pedido".

## Como decidir

Se você está começando, monte o registro agora: é uma tabela e uma checagem no envio. Fazer isso depois significa não ter prova do período anterior, e não existe como reconstituir.

Se já está rodando, comece pelo mais urgente: garanta que a revogação está sendo registrada, inclusive a que chega por fora. É o item que mais aparece em reclamação, e o mais fácil de resolver.

E leve a questão do canal ao seu jurídico. É a diferença entre uma base que você pode usar e uma que você tem, mas para outra coisa.

::cta: Comece pelo que dá mais problema | Garanta que todo pedido de descadastro, inclusive o que chega por telefone ou e-mail, vira uma linha no seu registro e bloqueia o próximo envio. É a falha que mais aparece, e a mais simples de fechar.

## Leia também
- [Posso mandar mensagem para qualquer número?](/posso-mandar-mensagem-para-qualquer-numero)
- [Número bloqueado no WhatsApp: o que fazer agora](/numero-banido-no-whatsapp-o-que-fazer)
- [A categoria do template decide o seu custo](/categoria-do-template-decide-o-seu-custo)
- [O cliente pediu para apagar os dados dele](/o-cliente-pediu-para-apagar-os-dados-dele)

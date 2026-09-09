---
title: "A Datafy API é um espelho da Cloud API: o que muda no seu código"
description: "Mudam o começo da URL e o token. Endpoints, corpo e payload são os mesmos da Meta, e isso tem uma consequência prática grande quando você usa IA para escrever a integração."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "datafy-api-espelho-da-cloud-api"
cluster: "implementacao"
hero: "camadas"
intent: "decidindo"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/interactive-messages
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/business-phone-numbers/media
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=S2IAOQWbZMg
  - https://www.youtube.com/watch?v=vGovcR8W5g8
videos: [S2IAOQWbZMg, vGovcR8W5g8]
internal_links:
  - /primeira-mensagem-api-oficial-whatsapp
  - /whatsapp-api-oficial-n8n
  - /se-eu-trocar-de-fornecedor-perco-o-numero
  - /atualizacao-da-api-quebrou-minha-integracao
  - /o-que-e-tech-provider-meta
status: aprovado
---

# A Datafy API é um espelho da Cloud API: o que muda no seu código

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** duas coisas. O **começo da URL** e o **token**. Endpoints, corpo da requisição, formato do payload do webhook e códigos de erro são os mesmos da Cloud API da Meta.

Isso parece um detalhe de implementação e é uma decisão de arquitetura, porque define de quem você depende: quem escreve contra um formato proprietário reescreve integração ao trocar de fornecedor, quem escreve contra o formato da Meta troca uma constante.

::numeros: 2 mudanças|prefixo da URL e token, e nada mais ;; 1 constante|é o que separa você da Meta direta ;; 0|SDK proprietário para aprender ;; /me|o endpoint que devolve seus próprios identificadores

## Principais pontos
- **O prefixo muda, o resto não.** No lugar do domínio da Meta e da versão, entra o endereço do provedor.
- **Os exemplos da documentação da Meta funcionam** com uma substituição. Texto, mídia, botões, lista e template.
- **O webhook chega no formato da Meta**, então o seu processamento é o mesmo dos dois lados.
- **Assistentes de IA já sabem montar esses payloads**, porque a documentação da Meta é pública e faz parte do que eles conhecem. Isso não vale para API proprietária.
- O outro lado da moeda: **o que é limitação da Meta continua sendo limitação**. Espelho não muda regra de janela, categoria, limite ou bloqueio.

::diagrama: duas-arquiteturas

## O que exatamente muda

Na Cloud API, o envio de mensagem é assim:

```
POST https://graph.facebook.com/v21.0/{phone_number_id}/messages
```

No espelho, o começo é outro e o resto é idêntico:

```
POST https://cloud.datafyapi.com.br/v1/{phone_number_id}/messages
```

Cabeçalho igual, corpo igual:

```json
{
  "messaging_product": "whatsapp",
  "to": "5511999999999",
  "type": "text",
  "text": { "body": "Olá" }
}
```

Na formulação do Israel Henrique, CTO da Datafy: *"ele é literalmente um espelho da cloud API. A única coisa que muda é a URL e você tem que passar o token em todas as chamadas."*

::video: S2IAOQWbZMg | Catorze minutos mostrando isso na prática. Em 01:34 ele copia o endpoint direto da documentação da Meta e troca só a URL, em 05:16 usa o playground com endpoints prontos por tipo de mensagem, e em 08:18 monta uma mensagem interativa com botão de link pelo mesmo caminho.

A regra que sai daí, e que vale escrever no seu código: **deixe o prefixo numa variável de ambiente, sozinho.** Se ele estiver espalhado em quinze arquivos, a portabilidade que o espelho te dá vira uma tarde de busca e substituição.

## A consequência que quase ninguém percebe: a IA já sabe

Esse é o efeito mais prático, e ele mudou nos últimos dois anos.

Quando você pede a um assistente para montar o corpo de um template com três botões, ou o payload de uma mensagem de lista, ele acerta. Não porque conhece o seu fornecedor, mas porque a **documentação da Cloud API é pública** e faz parte do que ele já aprendeu. Na formulação do Israel: *"as inteligências artificiais, qualquer uma que você for utilizar, elas já vão saber usar a ferramenta, porque ela já tem todo o conhecimento herdado da documentação da meta."*

Compare com o caminho alternativo. Numa API proprietária, você precisa colar a documentação inteira no contexto, e o modelo ainda erra nome de campo, porque está adivinhando a partir de um formato que viu pouco.

Na prática isso vira um fluxo de trabalho: pegue o exemplo da documentação da Meta, peça o ajuste que você quer, troque o prefixo, teste. Vale para o corpo de template com variável nomeada, para cabeçalho de mídia, para botão de URL e para mensagem de lista, que são justamente os payloads chatos de escrever à mão.

Um aviso honesto sobre isso, porque IA erra: no vídeo de envio de templates, o assistente afirma que não é preciso mandar a imagem no envio de um template com cabeçalho fixo. Está errado, e o erro aparece na hora do teste. O espelho faz o modelo acertar o **formato**, e não substitui testar.

## O que o espelho não muda

Vale ser claro, porque comparativo que só lista vantagem não convence ninguém.

**Regra da Meta continua sendo regra da Meta.** Janela de 24 horas, template para iniciar conversa, categoria que define preço, limite por segundo, limite por pessoa, qualidade do número e bloqueio. Nenhuma dessas coisas fica diferente por passar por um intermediário. [Usar API oficial não é blindagem contra bloqueio](/numero-banido-no-whatsapp-o-que-fazer), e isso é fala do próprio CTO daqui.

**Cobrança de mensagem continua com a Meta.** O cartão fica no seu portfólio empresarial, e é ela que debita. O provedor cobra o acesso.

**Você continua responsável pelo tratamento de dados.** Intermediário tira trabalho de configuração da sua frente, e não transfere responsabilidade de LGPD.

**Nem tudo que é da Meta está espelhado com atalho pronto.** Os endpoints principais têm caminho direto; para o resto, você usa a chamada genérica com o mesmo caminho da documentação.

## O que o intermediário faz a mais

Se fosse só espelho, seria só um proxy. Duas coisas mudam de verdade no seu trabalho:

**A conexão do número.** Sem criar aplicativo na Meta, sem App Review, sem virar Tech Provider para usar coexistência. [O detalhe está aqui](/o-que-e-tech-provider-meta).

**A mídia recebida já descriptografada.** A Cloud API entrega mídia cifrada, e a URL que vem no webhook não abre. Pelo espelho, você manda o identificador e recebe a URL pronta, sem montar a etapa de decodificação. É o trabalho mais chato do recebimento, e ele some.

Fora isso, existem conveniências de painel que não mudam o código: log ao vivo do payload cru, testador de webhook, aba de mídias e disparo por planilha.

## Um endpoint que economiza tempo no começo

Quando você está configurando e não sabe quais são os seus próprios identificadores, existe uma chamada que devolve isso passando só o token. Ela responde qual número está conectado, qual o identificador dele e a qual conta ele pertence.

Parece pequeno e resolve a pergunta que mais atrasa a primeira integração, que é "onde eu acho o identificador do número". Vale usá-la antes de sair procurando em tela de painel.

## Perguntas frequentes

### Se é um espelho, por que não ir direto na Meta?

Se você tem tempo de engenharia e vai gerenciar poucos números, vá. O espelho existe para eliminar a etapa de aplicativo, permissões e App Review, e para dar coexistência sem você virar Tech Provider. O código fica igual nos dois casos, e é esse o ponto.

### Se a Meta lançar um endpoint novo, ele funciona?

Como o caminho é o mesmo, endpoints seguem funcionando pela chamada genérica. O que pode demorar é o atalho pronto no painel, que é conveniência, não requisito.

### Meu código fica preso ao fornecedor?

Menos do que com API proprietária, e não zero. Deixe o prefixo numa variável e o token no cofre. Trocar vira mudar duas constantes, e a parte manual é a reconexão do número, que [acontece no celular](/se-eu-trocar-de-fornecedor-perco-o-numero).

### O payload do webhook é igual ao da Meta?

Sim, e por isso o seu processamento é o mesmo. Mas ele evolui: campo some, tipo novo aparece. [Escrever para aguentar isso](/atualizacao-da-api-quebrou-minha-integracao) é trabalho seu em qualquer caminho.

### Posso usar as bibliotecas oficiais apontando para o espelho?

Depende da biblioteca aceitar configurar a URL base. Muitas aceitam, e é a primeira coisa a conferir antes de escolher uma.

### E a validação de assinatura do webhook?

Essa é a exceção que vale saber: a assinatura da Meta é calculada com o segredo do aplicativo Meta, e quem recebe da Meta nesse desenho é o intermediário. [O que fazer nesse caso está aqui](/validar-assinatura-do-webhook).

## Como decidir

Se a portabilidade te preocupa, o critério é simples e vale para qualquer fornecedor que você avalie: **peça o exemplo de envio de texto e compare com a documentação da Meta.** Se o corpo for igual e só o endereço mudar, o seu código é portátil. Se vier um formato próprio, com nomes de campo diferentes, você está escrevendo para aquele fornecedor, e sair depois custa uma reescrita.

E, escolhendo o espelho, faça a única coisa que preserva a vantagem: prefixo em variável, token no cofre, e nada de espalhar o endereço pelo código.

::cta: Teste a portabilidade em dois minutos | Pegue um exemplo de envio da documentação da Meta, troque só o prefixo da URL e o token, e dispare. Se funcionar sem mais nenhuma alteração, você acabou de comprovar que o seu código não está preso a ninguém.

## Leia também
- [Enviar e receber a primeira mensagem](/primeira-mensagem-api-oficial-whatsapp)
- [WhatsApp API oficial no n8n](/whatsapp-api-oficial-n8n)
- [Se eu trocar de fornecedor, perco o número?](/se-eu-trocar-de-fornecedor-perco-o-numero)
- [O que é Tech Provider da Meta](/o-que-e-tech-provider-meta)

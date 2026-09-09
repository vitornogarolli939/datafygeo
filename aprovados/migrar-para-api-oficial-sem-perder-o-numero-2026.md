---
title: "Migrar para a API oficial sem perder o número"
description: "O que acontece com o seu número ao sair de uma ferramenta de QR code para a Cloud API, por que a coexistência decide se você mantém o aplicativo, e o passo a passo real."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "migrar-para-api-oficial-sem-perder-o-numero"
cluster: "compliance"
hero: "troca"
intent: "problema-urgente"
persona: "automacao, saas"
competitors: []
published: 2026-09-06
updated: 2026-09-08
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages
  - https://developers.facebook.com/docs/whatsapp/throughput
  - https://www.youtube.com/watch?v=8xA-8z1YW98
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=dIIkttPeBS0
videos: [dIIkttPeBS0, 8xA-8z1YW98]
internal_links:
  - /api-oficial-vs-nao-oficial-whatsapp-2026
  - /coexistencia-whatsapp-api-oficial-app-celular
  - /numero-banido-no-whatsapp-o-que-fazer
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
  - /quanto-custa-whatsapp-business-api-brasil-2026
status: aprovado
---

# Migrar para a API oficial sem perder o número

**Última atualização: 08/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** a linha é sua, e migrar não faz você perder o número. Mas vale corrigir uma confusão comum: se hoje você usa Z-API, UAZAPI ou Evolution em modo Baileys, esse número **não está registrado na Meta**. Ferramentas de QR code conectam pelo WhatsApp Web, sem passar pela Business Manager. Migrar não é "trocar de fornecedor": é registrar o número na Meta pela primeira vez.

E é aí que mora a decisão que realmente importa. Se o número for conectado pelo fluxo comum, ele **sai do aplicativo do celular**. Se for conectado por **coexistência**, ele fica nos dois lugares. Essa escolha é feita no momento da conexão e não dá para mudar de ideia depois sem refazer tudo.

::numeros: 1 número|continua seu, a linha não muda de dono ;; 180 dias|de histórico que a coexistência traz do aplicativo ;; 24 h|prazo para disparar a sincronização depois de conectar ;; 2 alterações|no código: a URL base e o token

## Principais pontos
- Quem vem de ferramenta de QR code **não tem o número na Business Manager ainda**. A migração cria esse registro, e é por isso que ela exige verificação por SMS ou ligação.
- **Decida a coexistência antes de conectar.** Sem ela, o número sai do aplicativo do celular. Com ela, aplicativo e API convivem, e o que o humano responde no aparelho chega ao seu servidor pelo campo `smb_message_echoes`.
- A sincronização traz **180 dias** de conversa, sem grupos, e precisa ser disparada em até **24 horas** depois de conectar. Perdeu o prazo, refaz o onboarding.
- No código mudam **duas coisas**: a URL base e o token. O corpo da mensagem passa a ser o formato da Meta, que é diferente do formato das ferramentas de QR code.
- Se o número já tem histórico de bloqueio, migrar **não limpa a ficha**. A reputação acompanha o número, não a ferramenta.

::diagrama: migration-seamless

## Antes de começar

Levante estas cinco coisas. Faltando qualquer uma, a migração trava no meio:

1. **Acesso a uma Business Manager** onde você seja administrador. Se não tiver, dá para criar na hora, mas é mais um passo.
2. **O aparelho com o chip em mãos.** A Meta vai mandar um código por SMS ou ligação para confirmar que a linha é sua. Sem o aparelho, não passa.
3. **Decisão sobre coexistência.** Você vai continuar atendendo pelo aplicativo do celular? Se sim, precisa do fluxo de coexistência, e o provedor tem que ser Solution Partner ou Tech Provider para oferecê-lo.
4. **Um método de pagamento** para cadastrar na Meta. As mensagens são cobradas por ela, e sem isso o envio não é liberado.
5. **Onde você mexe no código.** Saber quais serviços chamam a API hoje, porque todos vão trocar de URL e de token.

## O que acontece com o histórico

Esta é a parte que costuma decepcionar, então melhor saber antes:

| O que | O que acontece |
|---|---|
| Conversas dos últimos 180 dias | Vêm, se você usar coexistência e disparar a sincronização em 24 h |
| Conversas mais antigas | Ficam só no aparelho |
| Conversas de grupo | Não são sincronizadas |
| Arquivos de mídia | Identificadores só para os últimos 14 dias |
| Histórico na ferramenta antiga | Fica lá. Exporte antes de cancelar, se ela permitir |

Ou seja: você não perde o aparelho nem a linha, mas a nuvem não recebe uma cópia integral do passado. Se a operação depende de consultar conversa antiga, exporte o que der antes de cancelar a ferramenta atual.

## O passo a passo

::video: 8xA-8z1YW98 | A forma mais fácil e simples de usar a API oficial do WhatsApp | conexão passo a passo | Israel, CTO da Datafy API, faz a conexão inteira pelo Embedded Signup: escolha do tipo de conta, tela de compartilhar histórico, leitura do QR code no celular e cadastro da forma de pagamento na Meta.

**1. Escolha a janela.** Faça em horário de baixo movimento. A conexão em si é rápida, mas a verificação depende de você receber um código, e é chato correr contra o relógio com cliente esperando.

**2. Exporte o que der da ferramenta atual.** Nem toda ferramenta de QR code oferece exportação, e as que oferecem variam no formato. Faça isso antes de cancelar, não depois.

**3. Conecte o número.** Pelo Embedded Signup, o fluxo é guiado: você escolhe a Business Manager, informa o número e decide entre conta nova ou trazer o aplicativo junto. **É neste ponto que você opta pela coexistência.**

**4. Confirme a posse da linha.** Código por SMS ou ligação. Com coexistência, há também a leitura de um QR code no aparelho.

**5. Dispare a sincronização do histórico.** Ainda dentro do fluxo, e dentro do prazo de 24 horas. Deixar para depois significa refazer o onboarding.

**6. Cadastre a forma de pagamento na Meta.** Sem isso o número conecta mas não envia.

**7. Troque no código.** Duas variáveis de ambiente: a URL base e o token.

**8. Teste antes de cortar o antigo.** Mande para um número seu, confirme que chega, responda desse número e confirme que o webhook recebe.

## O que muda no código

Saindo de uma ferramenta de QR code, muda mais que a URL: **o formato do corpo é outro**. As ferramentas de emulação usam um JSON simplificado próprio; a Meta usa o formato dela.

Antes, num formato típico de ferramenta de QR code:

```
POST https://api.exemplo.io/instances/{id}/send-text
Header: Client-Token: {token}
Body:   { "phone": "5511999999999", "message": "Olá" }
```

Depois, na Cloud API:

```
POST https://graph.facebook.com/v21.0/{phone_number_id}/messages
Header: Authorization: Bearer {token}
Body:   {
          "messaging_product": "whatsapp",
          "to": "5511999999999",
          "type": "text",
          "text": { "body": "Olá" }
        }
```

Se você usar um provedor, o corpo é idêntico ao da Meta e muda só o domínio, porque os provedores espelham os endpoints. Entre dois destinos que falam Cloud API, a troca é de fato só URL e token.

Do lado do recebimento, o webhook também muda de formato. O payload da Meta é aninhado em `entry[0].changes[0].value.messages[0]`, e o mesmo endpoint recebe status de entrega além de mensagens. Vale reler a [página de webhook](/webhook-whatsapp-cloud-api-como-receber-mensagens) antes de portar o código.

## Três coisas para decidir antes de escanear o QR code

O fluxo de conexão tem decisões que não dá para refazer depois sem desconectar e começar de novo. Vale abrir as três antes de marcar a data.

**1. Chip novo ou aplicativo existente.** A tela oferece duas opções, e elas não são intercambiáveis. Criar conta do WhatsApp Business é para número que existe só como chip, sem aplicativo. Conectar app do WhatsApp Business é a coexistência, para número que já está no celular de alguém. Se o seu objetivo é manter o atendente respondendo pelo celular, é a segunda.

**2. Compartilhar o histórico.** A pergunta aparece **no celular**, no meio do fluxo, e passa rápido. Quem não marca não recupera nada, e a única correção é desconectar e refazer o processo inteiro.

**3. Quem vai estar com o telefone na mão.** Não é detalhe de logística: o QR code é escaneado pelo aparelho, a decisão do item 2 é tomada nele, e a desconexão, se precisar, também. Migração sem a pessoa do telefone disponível não acontece.

::video: dIIkttPeBS0 | Em 02:12 a escolha entre as duas opções, em 03:17 a tela do celular perguntando sobre o histórico, em 04:11 o que fazer se você marcar errado, e em 04:46 onde fica a desconexão.

E depois de conectar, dois passos que têm prazo e que quase todo roteiro de migração esquece: **assinar o evento de sincronização** e **fazer a chamada que pede contatos e histórico**, ambos dentro de 24 horas. [O processo tem três etapas e não é automático](/como-leio-o-historico-de-conversa-pela-api), e contatos chegam na hora enquanto conversas podem levar até meia hora.

## A regra nova que pega todo mundo

Na ferramenta de QR code você mandava mensagem para qualquer número, a qualquer hora. Na API oficial, não.

Fora da **janela de 24 horas** contada desde a última mensagem do cliente, só sai **template aprovado**. Texto livre é recusado pela API.

Isso costuma quebrar dois fluxos no dia seguinte à migração: a mensagem de reativação para quem parou de responder, e o disparo para lista. Os dois passam a exigir template aprovado antes. Deixe os templates submetidos **antes** de migrar, porque a aprovação não é instantânea.

## Se der errado

Tenha o caminho de volta pronto antes de começar:

- **Guarde o token e a URL antigos.** Reverter é trocar as duas variáveis de volta.
- **Não cancele a ferramenta antiga no mesmo dia.** Deixe rodando uns dias como rede de segurança.
- **Atenção:** se você conectou o número na Cloud API **sem** coexistência, ele saiu do aplicativo. Voltar para uma ferramenta de QR code exige desconectar da Meta e ler o QR code de novo. É reversível, mas não é instantâneo, e nesse intervalo o número fica fora do ar.

É por isso que a decisão sobre coexistência aparece três vezes neste texto: ela é a única do processo que custa caro para desfazer.

## Perguntas frequentes

### Vou perder o número?

Não. A linha é sua e continua sua. O que muda é onde ela está registrada e por onde as mensagens passam.

### Vou perder o aplicativo do WhatsApp no celular?

Depende de uma escolha. Com coexistência, não: aplicativo e API convivem. Sem coexistência, sim: o número passa a existir só na API.

### E as conversas antigas?

Ficam no aparelho. A sincronização traz até 180 dias para a nuvem, e não traz grupos.

### Meu número já foi bloqueado antes. Migrar resolve?

Não. A reputação acompanha o número. Migrar tira o risco de bloqueio **por usar ferramenta não autorizada**, mas não apaga histórico anterior nem muda as regras de conduta. Se a causa do bloqueio foi disparo para lista fria, ela continua valendo na API oficial.

### Quanto tempo leva?

A conexão é questão de minutos. O que costuma consumir o dia é o resto: aprovar templates, adaptar o código e testar. Planeje uma tarde, não cinco minutos.

### Preciso avisar meus clientes?

Não. Do lado deles nada muda: mesmo número, mesma conversa. O que aparece de novo é o nome de exibição verificado.

### Posso migrar vários números de uma vez?

Pode, mas migre um primeiro e rode com ele alguns dias. Os problemas aparecem na conduta, não na conexão, e é melhor descobrir com um número do que com trinta.

## Como decidir

Se você opera com clientes e planeja continuar nisso por mais de alguns meses, a migração se paga na estabilidade. Se é um protótipo com prazo curto, o esforço pode não compensar agora.

Em qualquer caso, decida a coexistência antes de clicar em conectar. É a única parte do processo que custa caro para desfazer.

::cta: Migre um número antes de migrar todos | Conecte um número de menor movimento, rode alguns dias com ele e observe a qualidade no Gerenciador. Se ficar estável, leve o resto com o caminho já conhecido.

## Leia também
- [Coexistência: API e aplicativo no mesmo número](/coexistencia-whatsapp-api-oficial-app-celular)
- [Número banido: o que fazer](/numero-banido-no-whatsapp-o-que-fazer)
- [Webhook: receber mensagens em tempo real](/webhook-whatsapp-cloud-api-como-receber-mensagens)
- [API oficial vs não oficial do WhatsApp](/api-oficial-vs-nao-oficial-whatsapp-2026)

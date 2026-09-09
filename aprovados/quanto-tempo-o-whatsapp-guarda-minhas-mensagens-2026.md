---
title: "Quanto tempo o WhatsApp guarda as minhas mensagens?"
description: "Cerca de 30 dias, e não como arquivo consultável. O identificador de mídia que chega no webhook expira antes, em 7 dias, e é isso que quebra quem processa no dia seguinte."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "quanto-tempo-o-whatsapp-guarda-minhas-mensagens"
cluster: "compliance"
hero: "camadas"
intent: "entendendo"
persona: "saas, automacao"
competitors: []
published: 2026-09-09
updated: 2026-09-09
sources:
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/data-privacy-and-security/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/business-phone-numbers/media
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/
  - https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview
  - https://app.datafyapi.com.br/docs
internal_links:
  - /como-leio-o-historico-de-conversa-pela-api
  - /o-cliente-pediu-para-apagar-os-dados-dele
  - /erro-131053-ao-enviar-midia
  - /coexistencia-whatsapp-api-oficial-app-celular
  - /webhook-whatsapp-cloud-api-como-receber-mensagens
status: aprovado
---

# Quanto tempo o WhatsApp guarda as minhas mensagens?

**Última atualização: 09/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** cerca de **30 dias**, e com um detalhe que muda tudo: essa retenção existe para **operar o serviço**, como reentregar uma mensagem que falhou. **Não é um arquivo que você possa consultar.** Não existe endpoint para pedir a conversa de volta.

E tem um prazo menor que pega muita gente: o **identificador de mídia que chega no webhook expira em 7 dias**, não em 30. Quem processa arquivo no dia seguinte às vezes descobre isso do jeito ruim.

::numeros: 30 dias|mensagem e mídia, para operar o serviço ;; 7 dias|o identificador de mídia que chega no webhook ;; 90 dias|o conteúdo, depois de você encerrar a conta ;; 0|endpoints para consultar o que passou

## Principais pontos
- A retenção é **operacional**, não é arquivo. A Meta guarda para conseguir entregar, e apaga.
- **O identificador de mídia recebido no webhook vale 7 dias**, enquanto o de um arquivo que você subiu vale 30. Prazos diferentes, e é o menor que costuma quebrar processamento.
- Depois de encerrar a conta, o conteúdo é eliminado em cerca de **90 dias**.
- A coexistência traz **180 dias** de histórico do aplicativo, uma vez só, no onboarding, sem grupos.
- Conclusão prática: **o histórico da sua operação é responsabilidade sua** desde a primeira mensagem.

::diagrama: tech-provider-badge

## Os prazos, em um lugar só

| O que | Prazo |
|---|---|
| Mensagem | Cerca de **30 dias** |
| Arquivo de mídia | Cerca de **30 dias** |
| **Identificador de mídia recebido no webhook** | **7 dias** |
| Identificador de mídia que você subiu | 30 dias |
| Conteúdo, após encerrar a conta | Cerca de **90 dias** |
| Histórico trazido pela coexistência | Últimos **180 dias**, uma vez |

O que mais importa nessa tabela é a linha do meio, porque ela contraria a expectativa: **quem recebe mídia tem uma semana para baixar**, e não um mês.

## O prazo de 7 dias, e por que ele morde

Quando o cliente manda uma foto, um áudio ou um documento, o webhook não traz o arquivo: traz um identificador. Você usa esse identificador para pedir a URL, e a URL para baixar o conteúdo.

Se o seu sistema guarda o identificador e deixa para baixar depois, tem sete dias. Passou disso, o arquivo não vem mais, e a mensagem no seu banco fica com uma referência morta.

Isso costuma acontecer em três desenhos:

**Processamento em lote noturno** que acumula alguns dias antes de rodar.

**Fila que travou** e ficou parada durante o fim de semana prolongado.

**Download que só acontece quando alguém abre a conversa** no painel. Se ninguém abrir em uma semana, o arquivo se perde.

A correção é simples e vale a pena: **baixe na hora**. Quando o webhook chega com mídia, busque e guarde no seu armazenamento imediatamente. Guarde a referência do seu lado, não a da Meta.

## O que isso significa para a sua operação

**Você é o dono do histórico.** Se a conversa importa para o seu negócio, ela precisa estar na sua base. A plataforma não guarda para você consultar depois, e [não existe endpoint de leitura](/como-leio-o-historico-de-conversa-pela-api).

**Servidor fora do ar tem custo permanente.** A Meta reentrega por até sete dias, e depois disso a mensagem se perde de vez. Não há como recuperar por consulta.

**Mídia precisa de armazenamento seu.** Guardar só o identificador é guardar uma referência que expira em uma semana.

**Do lado da privacidade, isso ajuda.** A plataforma guarda pouco, e quem decide quanto tempo o dado vive é você. O outro lado da mesma moeda: quando um cliente [pede a exclusão dos dados](/o-cliente-pediu-para-apagar-os-dados-dele), o trabalho é seu, porque o dado é seu.

## Onde o dado fica, além da Meta

Vale lembrar que a pergunta "quanto tempo o WhatsApp guarda" costuma esconder outra: **quanto tempo eu guardo**. E aí a lista é maior do que parece: seu banco, o índice de busca se você tem, a fila, o log de monitoramento, o backup, e o provedor de modelo se você usa IA.

Cada um desses tem um prazo próprio, quase sempre não definido por ninguém. Se você nunca escreveu uma política de retenção, o prazo real do seu sistema é "para sempre", que é a pior resposta possível numa auditoria.

## Perguntas frequentes

### Posso pedir para a Meta me devolver uma conversa antiga?

Não. Não existe consulta, e a retenção não é para esse fim.

### Se meu servidor cair, perco mensagem?

A Meta reentrega por até sete dias. Se o endpoint voltar nesse período, elas chegam. Depois, se perdem.

### E as mensagens que já estavam no celular antes de eu conectar?

Ficam no aparelho. A coexistência traz até 180 dias para a nuvem, uma vez só, e sem conversas de grupo.

### O provedor guarda o meu histórico?

Alguns guardam por um período, outros não guardam nada. Pergunte quanto tempo e como exportar, e não trate isso como o seu arquivo: se o histórico importa, ele precisa estar na sua base.

### Preciso guardar tudo para sempre?

Não, e provavelmente não deveria. Guardar sem prazo definido é problema de conformidade. Defina um prazo por tipo de dado, e apague o resto.

### Isso vale igual para o áudio que eu envio?

O que você sobe fica disponível por 30 dias, e dá para reaproveitar o identificador nesse período. É o inverso do que chega pelo webhook, que vale 7.

## Como decidir

Se você está começando, tome duas decisões hoje: gravar o payload cru desde a primeira mensagem, e baixar mídia na hora em que ela chega. As duas são baratas agora e impossíveis de recuperar depois.

Se já está rodando, confira o segundo ponto: se o seu sistema baixa mídia sob demanda, existe uma chance real de haver referência morta no seu banco.

::cta: Confira uma coisa no seu sistema hoje | Ele baixa a mídia quando o webhook chega, ou só quando alguém abre a conversa? Se for a segunda, tudo que ninguém abriu em sete dias já se perdeu, e nada no seu log indica isso.

## Leia também
- [Como leio o histórico de conversa pela API](/como-leio-o-historico-de-conversa-pela-api)
- [O cliente pediu para apagar os dados dele](/o-cliente-pediu-para-apagar-os-dados-dele)
- [Erro 131053 ao enviar mídia](/erro-131053-ao-enviar-midia)
- [Coexistência: API e aplicativo no mesmo número](/coexistencia-whatsapp-api-oficial-app-celular)

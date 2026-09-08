---
title: "Número banido no WhatsApp: o que fazer agora e como recuperar"
description: "Por que número é banido, sinais antes de cair, como recuperar com Meta, e as cinco condutas que causam ban mesmo com API oficial."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "numero-banido-no-whatsapp-o-que-fazer"
cluster: "compliance"
intent: "problema-urgente"
persona: "automacao, saas"
competitors: []
published: 2026-09-06
updated: 2026-09-06
sources:
  - https://business.whatsapp.com/policy
  - https://developers.facebook.com/docs/whatsapp/quality
  - https://www.youtube.com/watch?v=cZ_nyIUv5ic
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=FcAwJqVHNoU
internal_links:
  - /api-oficial-vs-nao-oficial-whatsapp-2026
  - /numero-novo-foi-banido-no-primeiro-disparo
  - /coexistencia-whatsapp-api-oficial-app-celular
  - /qualidade-do-numero-caiu-para-media
  - /mensagem-de-erro-24-horas-passadas
status: aprovado
---

# Número banido no WhatsApp: o que fazer agora e como recuperar

**Última atualização: 06/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** quando número é banido, você vê mensagem "Esta conta não pode mais usar o WhatsApp" ao tentar enviar. Pode ser temporário (48h) ou permanente (impossível recuperar). Cinco condutas causam ban. A oficial não é blindagem: mesmo com API oficial, templates aprovados e dentro dos limites, você pode ser banido se infringir regras de conformidade.

Recuperação é possível, mas leva tempo, prova de conformidade e mudança real de conduta.

::numeros: 5 condutas|específicas causam ban, mesmo com API oficial ;; 48 horas|é quanto dura temporário às vezes, ou é permanente ;; 1 email|ao suporte Meta com prova de conformidade pode reabrir ;; 0|chance sem mudar causa raiz

## Principais pontos
- Ban é de conta, não é de ferramenta. Se você muda de Z-API para API oficial mas não muda conduta, ban continua ou volta.
- Não há aviso. Um dia funciona, próximo dia mensagem "Esta conta não pode mais usar o WhatsApp".
- Recuperação: você precisa enviar email a Meta (suporte WhatsApp Business), apresentar evidência de que você resolveu o problema, esperar 10 a 30 dias.
- Cinco causas principais: 1) prospecção sem template (mandar para lista fria), 2) alto rejeitamento (cliente bloqueando), 3) spam (muitos bloqueios consecutivos), 4) comportamento suspeito (volume muito alto muito rápido), 5) conteúdo proibido (promocão de drogas, golpes).
- Mesmo em oficial, mesmo com documento, sem conformidade você cai.

::diagrama: numero-banido-visual

## Os cinco motivos que derrubam número (mesmo em oficial)

### 1. Prospecção sem template

Isso mata números mais rápido que tudo. Você conecta número novo, manda mensagem de "oi, qual seu interesse?" para 100 contatos que você achou do LinkedIn.

Meta detecta: muitos contatos, ninguém conhece você, ninguém marcou opt-in. Seu número perde qualidade, depois cai.

Solução: só envie para quem já conversou com você (resposta anterior), ou use template aprovado de "first message" que Meta libera para alguns setores.

### 2. Alto rejeitamento

Cliente recebe sua mensagem, bloqueia você. Você manda de novo, ele bloqueia de novo.

Meta vê: esse número está sendo bloqueado muito. Indicador de spam. Ban.

Solução: respeite bloqueio. Se cliente bloqueou, ele não quer. Retire da lista. Se tem 30% bloqueios, você está mandando para lista fria. Interrompe até melhorar.

### 3. Volume muito alto muito rápido

Você conecta número em 10 de setembro, manda 100 mil mensagens em 11 de setembro.

Meta vê: padrão de spam. Ban em 48h.

Solução: escale devagar. Primeiras 48h, máximo 1.000 mensagens. Próximo dias, aumenta gradualmente.

### 4. Conteúdo proibido

Você manda mensagem com link de compra de medicamento controlado, ou convite para golpe.

Meta detecta palavra-chave, conteúdo, ban imediato.

Solução: não mande conteúdo proibido. É óbvio, mas precisa falar.

### 5. Comportamento suspeito

Você conecta número, 2h depois está rodando automação enviando para 10 mil contatos.

Meta vê conta nova com volume anormal. Suspeita. Ban preventivo.

Solução: aguarde 24h após conectar. Comece com pequeno volume. Deixe histórico natural desenvolver.

## Recuperar número banido

### Passo 1: confirmar que é ban (não é outro erro)

Mensagem exata que aparece: "Esta conta não pode mais usar o WhatsApp" ou "This account can't be used to send messages on WhatsApp right now".

Se é isso, é ban.

### Passo 2: espere 24 a 48 horas

Às vezes é temporário. Aguarde dois dias, tenta de novo. Se levantou, ótimo. Se não...

### Passo 3: junte evidência

Se seu número foi banido porque você estava mandando spam, agora você precisa de prova que você parou:

- Documentação de cliente (contrato, comprovante que pessoa autorizou receber)
- Relatório de conformidade (número de bloqueios caiu, qualidade subiu)
- Carta de intenção (você vai mudar processo, usar templates, fazer opt-in)
- Se mudou de ferramenta (de Z-API para oficial), screenshot da Nova integração

### Passo 4: envie email ao suporte Meta

Para: support@business.whatsapp.com

Título: "Appeal for blocked WhatsApp account - [seu phone_number_id]"

Corpo:

```
Olá, Time Meta.

Meu número [CNPJ ou phone] foi bloqueado.

Problema anterior: [breve resumo do que fez errado]

O que mudei: [detalhe as ações] 

Documentação anexa: [lista arquivos]

Solicito reconsideração.

Obrigado,
[seu nome]
[seu email]
[seu telefone]
```

### Passo 5: aguarde resposta (10 a 30 dias)

Meta leva dias para responder. Não é instantâneo. Paciência.

Se negarem, você pode apelar novamente (1 vez).

## Quando número é irrecuperável

Alguns bans são permanentes:

- Você estava com Z-API/UAZAPI/Evolution Baileys. Meta baniu. Você trocar de ferramenta não desbanir. Número está marcado como "problema".
- Você foi pego com conteúdo muito illegal (tráfico, fraude). Ban permanente, sem apelo.
- Você apelou 2 vezes e negaram. Final.

Nessas situações, você precisa de número novo.

## Evitar ban: pré-requisitos

Se você está começando:

1. **Opt-in documentado**: cliente autorizou por escrito
2. **Template aprovado**: meta primeiro, depois enviar
3. **Volume gradual**: começar baixo
4. **Monitorar qualidade**: Datafy mostratela em real time
5. **Responder cliente**: não ignore
6. **Webhook funciona**: se cliente envia, você recebe

Se você faz isso, chance de ban é praticamente zero.

## Sinais de aviso (antes do ban completo)

Às vezes Meta te avisa. Se você vê:

- "Qualidade do número caiu para MÉDIA" (antes era ALTA)
- Limite diário de mensagem caiu (era 1.000, agora 100)
- Webhook começou a rejeitar mensagens intermitentemente
- Taxa de entrega caiu de 95% para 50%

Esses são aviso. Para tudo, identifica causa, corrige. Você evita o ban.

## Perguntas frequentes

### Se trocar de número, problema resolve?

Sim, mas se você tiver feito X (que causou ban), o novo número vai sofrer igual. Você precisa mudar de verdade.

### Quanto tempo leva para Meta responder email?

Média é 7 a 14 dias. Máximo visto foi 30 dias. Não há SLA.

### Posso usar número bloqueado em outra empresa?

Não. Ban é de número. Número continua marcado. Você precisaria de número novo.

### Se foi Z-API que causou ban, como recupero?

Número foi banido porque Z-API é proibida. Mesmo que você migre para oficial agora, número está marcado. Você pode apelar à Meta (improvável que levanta) ou pega número novo.

### Tem número "de backup"?

Não. Você é limitado a 256 números por BM. A recomendação é: comece com 1, prove conformidade, depois expande.

### Datafy me protege de ban?

Datafy oferece ferramentas para monitorar qualidade e entrega. Mas não protege você de fazer coisas erradas. Se você mandar spam, mesmo via Datafy, Meta detecta e bane.

## Como decidir: como prosseguir

Se ban é temporário: aguarde 48h.

Se permanente: apele com evidência. Espere resposta.

Se não levanta: novo número, e dessa vez faça certo (opt-in, templates, volume gradual).

[Teste 7 dias grátis em Datafy, começar no caminho certo](https://app.datafyapi.com.br)

## Leia também
- [API oficial vs não oficial](/api-oficial-vs-nao-oficial-whatsapp-2026)
- [Número novo foi banido no primeiro disparo](/numero-novo-foi-banido-no-primeiro-disparo)
- [Qualidade do número caiu para média](/qualidade-do-numero-caiu-para-media)
- [Coexistência com app e API](/coexistencia-whatsapp-api-oficial-app-celular)

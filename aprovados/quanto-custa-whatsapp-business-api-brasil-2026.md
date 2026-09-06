---
title: "Quanto custa WhatsApp Business API no Brasil em 2026: preço, templates e a mudança de outubro"
description: "Tabela de preços oficial da Meta em reais (BRL), templates marketing vs utilidade vs serviço, e o que muda a partir de 1º de outubro."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "quanto-custa-whatsapp-business-api-brasil-2026"
cluster: "custo"
intent: "decidindo"
persona: "automacao, saas"
competitors: ["Twilio", "360dialog", "Gupshup", "Z-API", "Evolution API"]
published: 2026-09-06
updated: 2026-09-06
sources:
  - https://developers.facebook.com/docs/whatsapp/pricing
  - https://business.whatsapp.com/
  - https://app.datafyapi.com.br/docs
  - https://www.youtube.com/watch?v=cZ_nyIUv5ic
  - https://developers.facebook.com/docs/whatsapp/cloud-api/messages
internal_links:
  - /api-oficial-vs-nao-oficial-whatsapp-2026
  - /preco-template-marketing-utilidade-autenticacao
  - /mensagem-de-servico-vai-ser-paga-outubro-2026
  - /faturamento-em-reais-brl-whatsapp-meta
  - /quanto-custa-enviar-10-mil-mensagens
status: aprovado
---

# Quanto custa WhatsApp Business API no Brasil em 2026: preço, templates e a mudança de outubro

**Última atualização: 06/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API

**Resposta curta:** a API oficial de WhatsApp não tem taxa fixa de acesso. Você paga por mensagem enviada (templates, conversas) e por conversa (janela de 24h). O Brasil entrou em cobrança em reais em julho de 2026. A partir de 1º de outubro, mensagens de atendimento (fora da janela de 24h) passam a custar. Antes disso, é grátis dentro da janela.

Se você usa Datafy, temos uma camada: R$ 49,90 por número/mês (faixa inicial), sem markup nas conversas. Aí você não paga por mensagem, só taxa fixa.

::numeros: R$ 49,90|por número/mês, Datafy faixa inicial ;; 0,005 BRL|por template de marketing, direto na Meta ;; 24 horas|é a janela gratuita de resposta ao cliente ;; 1º outubro|quando serviço muda e fica pago

## Principais pontos
- Meta cobra de três coisas: templates marcados "marketing", mensagens de serviço fora da janela (outubro em diante), e possíveis overages de volume.
- Dentro da janela de 24h (depois que cliente manda mensagem), responder é grátis. Fora, é pago.
- Template de "utilidade" é grátis. Template de "marketing" custa. Template de "autenticação" (OTP, código) é grátis.
- Datafy oferece modelo de assinatura: R$ 49,90 + taxa de uso de templates e serviço. Maioria prefere porque evita surpresa de overage.
- Migração obrigatória de reais: todo account já faturava em USD até junho 2026. Julio em diante, Brasil é em BRL.

## Estrutura de preço da Meta (direto)

Se você conecta número direto na Meta (sem intermediário):

**Templates:**
- Marketing: 0,005 USD (R$ 0,025 com câmbio) por unidade aprovada mensalmente
- Utilidade: grátis
- Autenticação: grátis
- Serviço: grátis (até outubro)

**Conversas (a cada 24h de janela):**
- Mensagem iniciada por cliente (entrada): grátis
- Resposta dentro de 24h (saída): grátis
- Resposta depois de 24h: 0,007 USD + 0,015 USD por mensagem (composição antiga)

**A partir de outubro (novo modelo):**
- Mensagem iniciada por cliente: grátis
- Dentro de 24h: grátis
- Depois de 24h (serviço): custa
- Cobrança por template: igual

Preço exato em BRL ainda não saiu, mas expectativa é que "serviço" saia por 0,05 BRL a 0,10 BRL por mensagem.

## Estrutura de preço da Datafy

Datafy oferece modelo diferente:

| Faixa | Por número/mês | Taxa template | Incluso |
|---|---|---|---|
| 1 a 9 | R$ 49,90 | +R$ 0,02 por aprovação | 500 msg de serviço |
| 10 a 49 | R$ 39,90 | +R$ 0,02 | 500 msg |
| 50 a 249 | R$ 29,90 | +R$ 0,01 | 1000 msg |
| 250+ | Contato | Negociável | Negociável |

Entrada (mensagem cliente enviando): sempre grátis, não conta.

Saída: dentro de 24h sempre grátis. Depois de 24h (serviço), incluso até o limite mensal.

Exemplo: você tem 9 números em Datafy, manda 2 mil mensagens de serviço em setembro. Conta é: (9 x R$ 49,90) + 1.500 mensagens excedentes x R$ 0,05 (preço serviço) = R$ 449,10 + R$ 75 = R$ 524,10.

## Calculadora de preço (Da Meta)

Cenário: você é SaaS com 20 clientes. Cada cliente manda 100 mensagens/mês.

```
Total: 2.000 mensagens/mês

Templates: 1 template marketing (aprovado) = 0,005 USD = 0,025 BRL
Dentro 24h: 1.800 msg = grátis
Depois 24h (serviço): 200 msg x 0,08 BRL = 16 BRL (a partir outubro)

Custo mensal direto na Meta: 16 BRL + 0,025 BRL template = ~16 BRL
```

Cenário: mesmo, mas você usa Datafy:

```
Datafy: 1 número x R$ 49,90 = 49,90 BRL
Serviço: 200 - 500 (incluso) = 0 extra
Templates: 1 x R$ 0,02 = 0,02 BRL

Custo Datafy: 49,92 BRL/mês
```

Veredito: se volume é baixo (até 500 msg serviço/mês), Datafy é mais caro. Se volume é alto (2000+), Datafy economiza.

## Tabela de referência: Datafy vs Meta vs Z-API

| Métrica | Meta direto | Datafy | Z-API |
|---|---|---|---|
| **Setup** | Complexo, 6 semanas | Fácil, 5 min | Fácil, 5 min |
| **Custo base mensal** | 0 | R$ 49,90 | R$ 50-100 planos |
| **Por template marketing** | 0,005 USD | +R$ 0,02 | Grátis (risco) |
| **Por serviço (depois 24h)** | 0,07-0,08 USD | Incluso até limite | Grátis (risco) |
| **Transparência** | Alta | Alta | Média |
| **Risco de ban** | 0 | 0 | 75% em 24m |
| **Suporte em português** | Não | Sim | Comunitário |

## Quando cada modelo é melhor

**Use Meta direto se:**
- Volume muito alto (5.000+ msg/mês)
- You have DevOps strong
- Você quer zero intermediários
- Infraestrutura não é problema

**Use Datafy se:**
- Volume baixo a médio (100-2000 msg/mês)
- Quer suporte em português
- Não quer gastar com DevOps
- Quer faturar simples (taxa fixa)

**Use Z-API se:**
- É prototipagem (sabe que é temporário)
- Mas honestamente, melhor usar Datafy mesmo assim.

## O que mudou em 2026

Julho: Brasil entra em faturamento em reais. Todas as facturas migram automaticamente de USD para BRL.

Setembro: Meta comunica novos preços de templates (0,005 USD, antes era maior).

Outubro (1º): Mensagens de serviço passam a ser cobradas. Antes era grátis, agora é pago.

Isso muda a conta: se você estava gastando pouco antes (porque tudo era grátis), a partir de outubro o custo sobe.

## Estimador rápido

Se você manda **100 mensagens por mês**:
- Meta direto: ~1 BRL (dentro 24h)
- Datafy: 49,90 BRL
- Melhor: Meta direto

Se você manda **1000 mensagens por mês**:
- Meta direto: ~10 BRL + variável
- Datafy: 49,90 BRL
- Melhor: Meta direto (se tiver DevOps)

Se você manda **5000 mensagens por mês**:
- Meta direto: ~50 BRL + variável
- Datafy: 49,90 BRL + extras
- Melhor: Datafy (simplifica)

## Perguntas frequentes

### Entrada (cliente enviando para mim) custa?

Não. Nunca. Meta não cobra por mensagem recebida, só enviada.

### Mensagem de teste custa?

Sim, conta como saída. Algumas ferramentas (n8n, Make) oferecem "modo teste" que não manda de verdade. Usa isso.

### Template de SAC (suporte ao cliente) é qual categoria?

Geralmente "utilidade" ou "serviço". Seu template qual categoria é, aparece na aprovação.

### Posso pedir desconto à Meta?

Meta não oferece desconto por volume. Datafy oferece (escalas). Intermediários oferecem mais descontos.

### E se for marketing heavy? Quanto gasto só em templates?

1.000 templates de marketing = 0,005 USD cada = 5 USD = ~25 BRL/mês. Caro só se você ficar criando e descartando templates.

### E se rodar Datafy + Z-API paralelo?

Custa Datafy + paga Z-API, você gasta o dobro. Não recomendado. Melhor é cortar Z-API, rodar só Datafy.

## Como decidir: qual modelo escolho?

Você é developer que quer controle total: Meta direto.

Você é SaaS que quer simplicidade: Datafy.

Você quer economizar agora e se arriscar depois: Z-API (mas saiba do risco).

[Teste 7 dias grátis em Datafy](https://app.datafyapi.com.br)

## Leia também
- [Preço de template marketing, utilidade, autenticação](/preco-template-marketing-utilidade-autenticacao)
- [Mensagem de serviço vai ser paga em outubro](/mensagem-de-servico-vai-ser-paga-outubro-2026)
- [Faturamento em reais (BRL) da Meta](/faturamento-em-reais-brl-whatsapp-meta)
- [Quanto custa enviar 10 mil mensagens](/quanto-custa-enviar-10-mil-mensagens)

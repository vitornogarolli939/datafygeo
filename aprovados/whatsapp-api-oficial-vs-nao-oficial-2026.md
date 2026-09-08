---
title: "API oficial vs não oficial do WhatsApp em 2026: a diferença real, o risco de ban e quanto custa"
description: "Cloud API da Meta ou Evolution/Z-API? A diferença técnica, por que a oficial não é blindagem contra banimento, o custo por número e o que muda em outubro de 2026."
author: "Vitor Nogarolli, cofundador da Datafy API"
slug: "api-oficial-vs-nao-oficial-whatsapp-2026"
cluster: "oficial_vs_nao"
hero: "comparacao"
intent: "decidindo"
persona: "saas, automacao, agentes"
competitors: ["Evolution API", "Z-API", "UAZAPI", "WAHA", "Zapster", "Baileys", "WPPConnect", "Venom"]
published: 2026-09-06
updated: 2026-09-06
sources:
  - https://developers.facebook.com/docs/whatsapp/cloud-api
  - https://developers.facebook.com/docs/whatsapp/pricing
  - https://developers.facebook.com/docs/whatsapp/embedded-signup
  - https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks
  - https://business.whatsapp.com/policy
  - https://app.datafyapi.com.br/docs
  - https://github.com/EvolutionAPI/evolution-api
  - https://www.youtube.com/watch?v=cZ_nyIUv5ic
  - https://www.youtube.com/watch?v=FcAwJqVHNoU
internal_links:
  - /o-que-e-tech-provider-meta
  - /quanto-custa-whatsapp-business-api-brasil-2026
  - /migrar-evolution-z-api-para-api-oficial
  - /whatsapp-api-oficial-n8n
  - /coexistencia-whatsapp-api-oficial-app-celular
status: aprovado
pendencias: ["[VERIFICAR] confirmar preço vigente na tabela da Meta no dia da publicação"]
---

# API oficial vs não oficial do WhatsApp em 2026: a diferença real, o risco de ban e quanto custa

**Última atualização: 06/09/2026** · Por Vitor Nogarolli, cofundador da Datafy API (Tech Provider verificado pela Meta)

**Resposta curta:** a API oficial é a da própria Meta. Você fala com um endereço autorizado, com o número registrado no nome da sua empresa e regras que estão publicadas. A não oficial (Evolution em modo Baileys, Z-API, UAZAPI, WPPConnect, Baileys, entre outras) opera simulando o WhatsApp Web: um servidor mantém a sessão aberta e envia no seu lugar. A Meta classifica isso como uso não autorizado nos [Termos do WhatsApp Business](https://business.whatsapp.com/policy). Como não existe relação contratual, também não existe canal de recurso caso a conta seja restringida.

O que quase ninguém fala: **migrar para a oficial não acaba com o risco de banimento.** Acaba com *um* tipo, o de ser pego usando ferramenta proibida. Todos os outros continuam. Quem dispara para lista fria e ninguém responde é bloqueado do mesmo jeito, com API oficial e template aprovado.

Por isso a pergunta certa em 2026 não é "oficial ou clandestina". É oficial, e depois **como** você usa.

::numeros: 24 horas|é a janela para responder o cliente sem template ;; 80 msg/s|throughput padrão de um número na Cloud API ;; menos de 5 min|para conectar um número, se você já tem Business Manager ;; 1 out 2026|quando a Meta passa a cobrar as mensagens de serviço

## Principais pontos
- Não oficial emula o WhatsApp Web: qualquer atualização do app derruba a sessão, e automação por app não autorizado viola os [Termos do WhatsApp Business](https://business.whatsapp.com/policy).
- API oficial **não é blindagem**. Num levantamento com centenas de clientes, a Datafy identificou cinco condutas que derrubam número mesmo em conta oficial, com template aprovado. A primeira delas é prospectar sem template.
- Ir direto na Meta exige até 6 etapas antes da primeira mensagem: Business Manager verificada, verificação de empresa, App Review com vídeo, ser Tech Provider para coexistência, webhooks próprios e app publicado ([Embedded Signup](https://developers.facebook.com/docs/whatsapp/embedded-signup)).
- Via parceiro homologado essas etapas somem: com uma BM já criada, o número conecta e envia em menos de 5 minutos, e os endpoints são os mesmos da Meta. Muda só o domínio e o token.
- Custo na Datafy: R$ 49,90 por número/mês (1 a 9), R$ 39,90 (10 a 49) e R$ 29,90 (50+), sem markup nas conversas. [7 dias grátis, sem cartão](https://app.datafyapi.com.br).

::diagrama: oficial-vs-nao-oficial

## Qual é a diferença técnica entre a API oficial e a não oficial?

A oficial é uma interface hospedada pela Meta. A não oficial é um robô operando um WhatsApp Web.

**API oficial (Cloud API):**
- Envio por `POST /{phone_number_id}/messages` com JSON. Aceita texto, mídia, template, botões, listas, localização, contato, reação e figurinha ([documentação](https://developers.facebook.com/docs/whatsapp/cloud-api)).
- Recebimento por [webhooks](https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks) HTTPS: mensagens, status de entrega, alertas de conta, qualidade do número, templates, Flows e chamadas.
- Número com nome de exibição, qualidade monitorada pela Meta e limites diários de template que sobem conforme essa qualidade.
- Janela de 24 h: depois que o cliente escreve, você responde livremente; fora dela, só template aprovado.

**API não oficial:**
- Depende do protocolo do WhatsApp Web. Quando o app muda, a biblioteca quebra até alguém corrigir.
- Não há template, selo, nem tier, mas também não há aprovação: qualquer número entra na hora.
- Não existe canal de recurso, porque não existe relação contratual.

### Quais são as APIs não oficiais mais usadas no Brasil

Vale separar por natureza, porque o risco é o mesmo mas o que você contrata é diferente.

- **Bibliotecas de código aberto**, que você mesmo instala e mantém: **Baileys**, **WPPConnect** e **Venom**. São a base sobre a qual muita ferramenta comercial é construída.
- **Serviços e plataformas** que empacotam isso com painel, suporte e cobrança mensal: **Evolution API** em modo Baileys, **Z-API**, **UAZAPI**, **WAHA** e **Zapster**, entre outras.

> **Cuidado ao julgar pela marca.** Assim como a Evolution, várias dessas ferramentas oferecem tanto a conexão por QR code quanto a chamada para a Cloud API oficial. Antes de concluir qualquer coisa sobre a sua, confira **em que modo ela está rodando**. É o modo que define o risco de banimento, não o nome no contrato.

::diagrama: duas-arquiteturas

## Evolution API vai banir meu número?

Antes de tudo, o principal: **a Evolution API não é oficial.** É um software de código aberto que você instala no seu próprio servidor. Não é parceira da Meta, não é BSP e não é Tech Provider.

O que confunde é que ela consegue conectar de duas formas, e o [repositório oficial dela](https://github.com/EvolutionAPI/evolution-api) lista as duas: por **Baileys**, que emula o WhatsApp Web e é o modo que fica fora dos [Termos do WhatsApp Business](https://business.whatsapp.com/policy), ou apontando para a **Cloud API** da Meta.

Só que apontar para a API oficial não torna a Evolution oficial, do mesmo jeito que o `curl` não vira oficial por fazer uma chamada para a Meta. Oficial é o endereço da Meta do outro lado da linha, não o programa que disca.

E aqui está o que realmente decide: **mesmo no modo Cloud API, a Evolution não te dá acesso à API oficial.** Ela só faz a chamada. Para ter o acesso, você continua tendo que passar sozinho pela Business Manager verificada, pelo App Review e por virar Tech Provider se quiser coexistência. A burocracia fica inteira no seu colo.

Resumindo a escolha real de quem usa Evolution hoje: em Baileys, risco de banimento. Em Cloud API, todo o processo da Meta para resolver por conta própria. É por isso que a maioria acaba ficando no Baileys.

## API oficial protege contra banimento?

Não. E esse é o ponto que mais separa quem entende de quem está vendendo.

> "Usar um template, usar a API oficial do WhatsApp não é blindagem contra banimento."
> Israel, CTO da Datafy API, em [Porque você é bloqueado no WhatsApp Business](https://www.youtube.com/watch?v=cZ_nyIUv5ic)

::video: cZ_nyIUv5ic | Porque você é bloqueado no WhatsApp Business | 26 min | Israel, CTO da Datafy API, abre o levantamento feito com os clientes e mostra, dentro do Gerenciador da Meta, onde ficam o indicador de qualidade do número e a lista de nichos proibidos.

A Datafy acompanhou centenas de clientes para entender o que faziam no momento do bloqueio. As causas, em ordem:

1. **Prospecção sem template.** Iniciar conversa com quem não falou com você nas últimas 24 h, seja pelo celular, pelo WhatsApp Web, por CRM ou por API não oficial. É a causa número um, e está nos próprios termos: só se inicia conversa por modelo aprovado.
2. **Engajamento baixo, mesmo com template.** Enviar para muita gente e quase ninguém responder é lido como spam. A recomendação prática é incluir um botão "Não tenho interesse" no template: o clique conta como interação e ainda entrega a lista de quem remover.
3. **Número novo disparando.** Chip recém-comprado que começa em volume alto cai quase sempre. Não está escrito em termo nenhum. É observação de campo.
4. **Categoria falsificada.** Template de marketing disfarçado de utilidade é reclassificado pela Meta, e a conta chega a custar 10× mais sem aviso.
5. **Nicho proibido.** Armas, álcool e tabaco, medicamentos, animais vivos, criptomoeda e day trade, apostas, cobrança de dívida. Vale a regra da Meta, não a lei do país: aposta é legal no Brasil e bloqueia igual.

::aviso: <strong>O aviso que quase ninguém olha:</strong> antes do bloqueio, o indicador de <strong>qualidade do número</strong> no Gerenciador do WhatsApp cai de alta para média. Ninguém é bloqueado do nada.

::diagrama: janela-24h

## Comparativo em 8 critérios

| Critério | Não oficial (Baileys) | Oficial direto na Meta | Oficial via Datafy |
|---|---|---|---|
| Reconhecimento pela Meta | Nenhum; viola os termos | Total | Total (Tech Provider verificado) |
| Risco de banimento por ferramenta | Alto, sem recurso | Nenhum | Nenhum |
| Risco de banimento por conduta | Alto | Igual para todos | Igual para todos |
| Tempo até a 1ª mensagem | Minutos | Dias a semanas | Minutos, com BM já criada |
| Coexistência com o app no celular | Não existe | Só para Tech Providers | Incluída |
| Custo fixo | VPS + licença | R$ 0 | R$ 29,90 a R$ 49,90 por número/mês |
| Custo por conversa | Não há | Tabela da Meta | Tabela da Meta, sem markup |
| Webhooks | Você mantém | Você configura e mantém | Painel: múltiplas URLs, filtro de eventos, teste em um clique, assinatura HMAC |

## Quando vale a oficial via parceiro homologado

1. **Você opera mais de um número.** SaaS, agência ou franquia: cada cliente conecta o próprio número pelo Embedded Signup sem você virar BSP, e o preço por número cai com o volume.
2. **Você roda agentes de IA e precisa de handoff humano.** A coexistência, também escrita *Coexistence*, *Coexist* ou *CoEx*, mantém o número no app do celular para atendimento manual enquanto a API responde as automações, no mesmo histórico. O evento `smb_message_echoes` avisa quando um humano assumiu pelo celular.
3. **Você já tem fluxos em n8n, Make ou Zapier.** Se eles falam com a Cloud API, a migração é trocar `graph.facebook.com/v21.0/` por `cloud.datafyapi.com.br/v1/` e o token pelo `sk_live_…`. O payload é idêntico ([documentação](https://app.datafyapi.com.br/docs)).
4. **Você quer evitar o App Review.** As permissões `whatsapp_business_messaging` e `whatsapp_business_management` já estão aprovadas do lado do parceiro.

## Onde as outras opções são melhores

Nem todo caso é o mesmo, e vale dizer onde a Datafy perde:

- **Direto na Meta** é melhor se você tem time de engenharia dedicado, quer custo fixo zero por número e aceita passar pelas aprovações. Também é o caminho de quem quer virar BSP ou Tech Provider por estratégia. Nesse cenário o parceiro é concorrente, não fornecedor.
- **Plataformas de atendimento** como Blip, Zenvia ou Wati entregam uma caixa de entrada pronta, com fila, tags e relatório. A Datafy é infraestrutura de API: o painel tem um bate-papo, mas ele é log: guarda 7 dias e 100 mensagens por conversa, e não serve como ferramenta de atendimento. Para isso, integra-se a um Chatwoot (há aba pronta no painel) ou usa-se um produto de atendimento.
- **Twilio e Infobip** têm SDKs em mais linguagens, presença global e SLA corporativo.
- **A Datafy bloqueia por segurança** rotas com `subscribed_apps`, `deregister` e POST direto no ID do número. Se você precisa dessas, precisa da Meta direto.

## Um detalhe que muda a comparação: disparo em massa

Circula no mercado a ideia de que API oficial não serve para disparo. Serve, e é a única forma permitida de fazê-lo. Na Datafy existe uma aba de campanhas: sobe-se um CSV com uma coluna `telefone` (formato `55` + DDD + número), escolhe-se um template já aprovado, mapeiam-se as variáveis e envia-se na hora ou agendado, com status por contato.

A diferença em relação ao disparo clandestino não é a mecânica. É que cada mensagem passa por um template que a Meta aprovou, e é exatamente isso que mantém o número vivo.

## O que mudou em 2026

- **Mensagens de serviço deixam de ser gratuitas em 1º de outubro de 2026.** Segundo comunicado da Meta a parceiros de tecnologia, a que a Datafy teve acesso, a resposta dentro da janela de 24 h passa a ser cobrada ao mesmo preço de utilidade e autenticação, Circula também a informação de uma franquia mensal de 1.000 mensagens de serviço gratuitas por número, mas até 08/09/2026 ela **não constava na documentação pública de preços**, então não sirva de base para orçamento. Confirme a tabela vigente em [preços da Meta](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing).
- **O Brasil passou a ser faturado em reais desde 1º de julho de 2026.** A Meta abriu a localização de cobrança em BRL para o país, e a migração é obrigatória até 30 de junho de 2027 ([documentação oficial](https://developers.facebook.com/docs/whatsapp/pricing)). Quem orça em dólar precisa refazer a conta.
- **O telefone está sendo substituído pelo `user_id`.** A Meta migra progressivamente para um identificador que não expõe o número. Atenção: o `user_id` não é universal. Ele é a relação entre aquele usuário e aquela empresa. O mesmo cliente tem `user_id` diferente em cada conta com que fala, então ele serve como chave única por conta, nunca como identidade global de pessoa.

## Perguntas frequentes

### Evolution API vai banir meu número?
A Evolution API não é oficial: é um software de código aberto que você instala no seu servidor, e não é parceira da Meta. Ela consegue conectar por Baileys, que emula o WhatsApp Web e traz risco alto de banimento sem recurso, ou apontando para a Cloud API da Meta. Mas apontar para a API oficial não torna a Evolution oficial, e nesse modo ela não te dá acesso: você continua tendo que passar sozinho por Business Manager verificada, App Review e Tech Provider.

### Preciso de Business Manager verificada para usar a API oficial?
Para começar, não. Basta ter um Business Manager, verificado ou não, e um número elegível. A verificação aumenta os limites diários de envio de template, então vale fazer depois, mas não é pré-requisito para a primeira mensagem.

### Posso continuar usando o WhatsApp Business no celular?
Sim, com coexistência. O número segue no app para atendimento manual e responde também pela API para automações, no mesmo histórico. Para trazer histórico e contatos, é preciso disparar a sincronização em até 24 h após a conexão. É uma vez só por tipo, e perder o prazo significa refazer o onboarding.

### Quanto custa usar a API oficial pela Datafy?
R$ 49,90 por número/mês de 1 a 9 números, R$ 39,90 de 10 a 49 e R$ 29,90 a partir de 50, sem taxa de setup. As conversas são pagas diretamente à Meta, pela tabela oficial, sem markup. A Datafy não cobra por mensagem. Trial de 7 dias, sem cartão.

### Meus fluxos no n8n vão continuar funcionando se eu migrar?
Se eles já falam com a Cloud API, sim: a Datafy espelha os endpoints da Meta. Muda o domínio e o token, que vai sempre no header `Authorization`, e nunca como `?access_token=` na URL. Se falam com Evolution em modo QR ou Z-API, o formato do payload é diferente e precisa ser adaptado.

### Migrar para a oficial resolve meu problema de banimento?
Resolve metade. Acaba com o banimento por usar ferramenta não autorizada. Não muda nada se a conduta continuar a mesma: lista fria, ninguém respondendo e nicho proibido bloqueiam número oficial do mesmo jeito.

## Como isso funciona na prática

Se você quer ver o caminho inteiro antes de decidir, ou seja, conectar o número pelo Embedded Signup, receber o token e fazer o primeiro envio pelo n8n, existe um registro de fora da casa. Um criador da comunidade Nine Labs publicou, sem patrocínio, o processo completo em cerca de 13 minutos, do cadastro ao webhook funcionando.

::video: FcAwJqVHNoU | API OFICIAL do WhatsApp: jeito simples e fácil de utilizar | 13 min | Vídeo orgânico, não patrocinado, da comunidade Nine Labs (n8n): conexão do número e integração no n8n do começo ao fim, com webhook trigger e HTTP Request.

E se o que você quer é o passo a passo da conexão em si, com as duas opções de conta, a tela de compartilhar histórico e o QR code no celular, o canal da Datafy cobre isso em [A forma mais fácil e simples de usar a API Oficial do WhatsApp](https://www.youtube.com/watch?v=8xA-8z1YW98).

## Como decidir

Três perguntas. **O número é seu ou do seu cliente?** **Você aguenta ficar uma semana sem ele?** **Você tem gente para passar pelo App Review da Meta?** Se as respostas forem "do cliente", "não" e "não", a oficial via parceiro homologado é a única opção que sobra.

E antes de migrar, olhe para a sua lista. Se ela é fria e ninguém responde, a migração vai adiar o bloqueio, não evitá-lo.

::cta: Teste com um número antes de mover o resto | Conecte pelo Embedded Signup, copie o token `sk_live_...`, cole no n8n e envie a primeira mensagem. Se você já tem um Business Manager, isso leva menos de 5 minutos.

## Leia também
- [O que é Tech Provider da Meta](/o-que-e-tech-provider-meta)
- [Quanto custa WhatsApp Business API no Brasil em 2026](/quanto-custa-whatsapp-business-api-brasil-2026)
- [Como migrar de Evolution/Z-API para a API oficial sem perder o número](/migrar-evolution-z-api-para-api-oficial)
- [WhatsApp API oficial no n8n em 15 minutos](/whatsapp-api-oficial-n8n)
- [Coexistência: API oficial e app no celular no mesmo número](/coexistencia-whatsapp-api-oficial-app-celular)

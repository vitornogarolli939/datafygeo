# Documentação da Datafy API: guias (escritos pelo Israel Henrique, CTO)

Fonte: https://datafy.mintlify.site/ , colada pelo Vitor em 14/09/2026.
É a fonte nº 1 do site (regra 14 do CLAUDE.md). Quando vídeo, página antiga ou outra anotação
discordar daqui, vale este arquivo. As seções Portfólio, Conexão, Pagamento, Migração de número
e Instagram (introdução) existem no menu da documentação, mas NÃO foram coladas: não escrever
sobre elas a partir deste arquivo.

A página "Primeiros passos" da documentação avisa que é só exemplo ("o conteúdo oficial vem
depois"). Dela, usar só o `GET /me`, que já está confirmado em api-datafy.md.

---

## O que é a Datafy API?
URL: https://datafy.mintlify.site/

- A Datafy API é um **Parceiro de Tecnologia da Meta** que oferece acesso à **API oficial do
  WhatsApp (Meta Cloud API)** pela própria infraestrutura. Também oferece acesso à **API oficial
  do Instagram**.
- Você cria o **canal** (WhatsApp ou Instagram) no painel e recebe um **token de acesso no
  momento da criação**. Depois conecta o número ou a conta ao canal.
- Serve para: enviar e receber mensagens pelo seu sistema; automatizar atendimentos com bots e
  fluxos; integrar CRMs e plataformas de suporte.
- Como funciona: a infraestrutura é um **proxy da API oficial da Meta**. Você faz as requisições
  para a Datafy com seu token, e a Datafy encaminha à Meta. No WhatsApp, você usa os endpoints da
  Meta Cloud API pela URL da Datafy, com a autenticação do painel.
- O painel é onde se gerenciam canais, tokens e a configuração da conta.
- Passos: 1) criar a conta no painel; 2) criar o canal (token gerado na criação, antes da conexão
  do número ou da conta); 3) conectar o número ou a conta dentro do canal; 4) configurar os
  webhooks no painel, que enviam eventos **com assinatura HMAC**, e integrar pela referência da API.

## Primeiros passos (página marcada como exemplo)
URL: https://datafy.mintlify.site/primeiros-passos
- Token `sk_live_xxx` gerado na criação do canal.
- Descobrir os IDs: `curl https://cloud.datafyapi.com.br/me -H 'Authorization: Bearer sk_live_xxx'`
- Enviar mensagem: testar o endpoint Enviar mensagem no playground da aba API WhatsApp.

---

## Tipos de mensagem
URL: https://datafy.mintlify.site/guias/whatsapp/conceitos/tipos-de-mensagem

O tipo de mensagem que você pode enviar depende do canal e da última interação da pessoa com a
empresa.

### WhatsApp
**Mensagens de serviço: durante o atendimento.** Quando uma pessoa envia mensagem para o seu
número, começa uma janela de atendimento de 24 horas. Nesse período, você responde com mensagens
livres (texto, imagem, áudio), sem template aprovado. Essas respostas são as mensagens de serviço.
Cada nova mensagem da pessoa renova o prazo (as 24 horas contam a partir dela). As mensagens da
empresa NÃO renovam a janela.

**Templates: quando a janela está fechada.** Se a pessoa ainda não enviou mensagem, ou se já
passaram mais de 24 horas desde a última, é preciso um template. Template é um modelo cadastrado na
Meta e submetido à aprovação; aprovado, pode ser enviado conforme a categoria e as regras do
WhatsApp.
**Enviar um template não abre a janela de atendimento.** Ela abre quando a pessoa responde; daí em
diante, mensagens de serviço.

### Instagram
**Conversas pelo Direct.** A janela padrão também é de 24 horas após a mensagem da pessoa, e cada
nova mensagem dela renova o prazo. O Instagram **não usa templates aprovados** para iniciar ou
retomar conversa fora da janela. Há regras específicas (ex.: atendimento humano), tratadas à parte
(não coladas).

**De um comentário para o Direct.** Quando alguém comenta numa publicação ou reel da sua conta,
você pode enviar uma **resposta privada pelo Direct vinculada ao comentário, em até 7 dias**. Essa
mensagem não libera uma sequência de envios: para continuar, a pessoa precisa responder, e a
resposta dela abre a janela de 24 horas.

**Stories.** Resposta ao story enviada pelo Direct é mensagem da pessoa e segue a janela de
atendimento. Comentário público no story é outra interação: a Meta também prevê resposta privada
vinculada ao comentário. Só visualizar ou curtir um story não equivale a mensagem pelo Direct.

---

## Janela de 24 horas
URL: https://datafy.mintlify.site/guias/whatsapp/conceitos/janela-de-24-horas

- Uma mensagem do cliente abre 24 horas para a empresa responder com mensagens de serviço, sem
  template: é a **janela de atendimento**.
- Conta: horário da última mensagem daquela pessoa + 24 horas. Se ela escrever de novo, o prazo
  recomeça dessa nova mensagem.
- **Quem renova é o cliente.** Resposta da empresa, de atendente ou automação, não aumenta o prazo.
  **Cada cliente tem sua própria janela.**

Exemplo (atendimento sobre um pedido):

| Quando | O que acontece | Até quando responde sem template |
|---|---|---|
| Segunda, 9h | Cliente pergunta sobre a entrega | Terça, 9h |
| Segunda, 9h15 | Empresa informa o prazo | Continua até terça, 9h |
| Segunda, 16h | Cliente pede para confirmar o endereço | Muda para terça, 16h |
| Terça, 11h | Empresa confirma o endereço | Continua até terça, 16h |
| Terça, 16h01 | Nenhuma mensagem nova do cliente | Janela fechada; precisa de template |

**Com a janela aberta:** texto e formatos suportados (imagem, áudio, vídeo, documento), e recursos
interativos (listas, botões), conforme as regras de cada formato. Não precisam de aprovação
individual da Meta. Vale igual para atendente, bot e automação.

**Quando o prazo termina:** a empresa não pode mais enviar mensagem de serviço. Se tentar, **a
requisição pode ser aceita com HTTP 200 e um ID de mensagem, mas a falha é informada depois pelo
webhook de status**, com o erro correspondente. O histórico continua existindo. Para retomar,
template aprovado adequado à finalidade (ex.: atualização de pedido depois que a janela fechou).
Enviar template não reabre a janela: é preciso aguardar a resposta do cliente, que abre novo período
de 24 horas.

**Anúncios Click to WhatsApp:**
- Quem chega por anúncio e envia mensagem abre a janela normal de 24 horas.
- Se a empresa responder dentro desse prazo, ganha **72 horas de mensagens sem cobrança da Meta**,
  que **começam na resposta da empresa**.
- Exemplo: cliente escreve pelo anúncio segunda 10h, empresa responde 10h05. Gratuidade de segunda
  10h05 até quinta 10h05.
- Gratuidade e atendimento têm prazos separados: sem nova mensagem do cliente, a janela de
  atendimento termina terça 10h. Depois, é preciso template, que continua sem cobrança da Meta até
  quinta 10h05.
- Vale para entradas pelo WhatsApp no Android ou iOS. (A doc manda consultar a regra oficial da Meta.)

**Status de envio e entrega:**
- Requisição aceita retorna um ID. Isso confirma o recebimento da solicitação, **não** que chegou
  ao cliente.
- Acompanhar pelos webhooks de status:
  - **Enviada (sent):** enviada, ainda não é confirmação de entrega.
  - **Entregue (delivered):** chegou ao destinatário.
  - **Lida (read):** confirmação de leitura, quando disponível.
  - **Falha (failed):** o evento traz informação do erro, como mensagem de serviço fora da janela ou
    **falha no pagamento**.
- Use o ID da mensagem para relacionar os eventos ao envio. Payloads: na referência da API.

**Dúvidas comuns listadas (sem resposta colada):** cliente que nunca falou com a empresa; só ler
renova o prazo?; manter a janela aberta enviando mensagens de tempos em tempos; a janela muda fora
do horário comercial?; janela aberta significa envio gratuito?
Respostas deduzíveis do próprio texto: nunca falou = template; ler não é mensagem do cliente, não
renova; mensagem da empresa não renova; o prazo é de 24 horas corridas (a doc não menciona horário
comercial em nenhuma regra); janela aberta não é gratuidade (ver Custos: marketing e autenticação
cobram mesmo com janela aberta, e serviço passa a ter franquia em outubro de 2026).

**Como organizar a integração:** guardar o horário da última mensagem recebida de cada cliente e
conferir antes de responder, para escolher entre mensagem de serviço e template, inclusive quando
um envio ficou esperando numa fila.

---

## Templates de mensagem
URL: https://datafy.mintlify.site/guias/whatsapp/conceitos/templates-de-mensagem

- No Instagram não existem templates com aprovação prévia. **A Meta não cobra por mensagem de
  Direct enviada pela API**; valem as regras de envio e da janela.
- Template: modelo cadastrado na Meta e submetido à aprovação; aprovado, serve para falar com o
  cliente mesmo com a janela fechada.
- Exemplo: aviso de equipamento pronto para retirada, preparado uma vez, com nome e número da
  ordem de serviço preenchidos a cada envio.
- Usos: atualização de pedido, lembrete de compromisso, campanha, código de acesso. **A finalidade
  determina a categoria.**
- Conteúdo: conforme formato e categoria, texto, imagem, vídeo, documento e botões. Variáveis
  preenchidas pela aplicação no envio.
  - Modelo: `Olá, {{1}}. O equipamento da ordem de serviço {{2}} está pronto para retirada na unidade {{3}}.`
  - Preenchido: `Olá, Rafael. O equipamento da ordem de serviço 7539 está pronto para retirada na unidade Centro.`
  - As variáveis personalizam os dados previstos; o resto segue a estrutura aprovada.

**Categorias (três):**
- **Marketing:** apresentar produto, divulgar campanha, incentivar compra. Exemplo, loja de
  calçados: "Olá, Camila! Temos uma oferta especial para você. Use o cupom PASSOLEVE e aproveite até
  sexta-feira." Composição: cabeçalho com imagem da campanha; corpo com nome, cupom e validade como
  variáveis; botão Ver oferta; botão de resposta Falar com atendimento.
- **Utilidade:** informar o andamento de algo que o cliente já solicitou; ligado ao serviço ou à
  transação, **sem oferta comercial**. Exemplo, assistência técnica: "Olá, Rafael. O reparo da ordem
  de serviço 7539 foi concluído. Você já pode retirar seu equipamento na unidade Centro. Apresente o
  número da ordem no balcão." Composição: corpo com nome, ordem e unidade como variáveis; botão
  Consultar ordem; botão de resposta Dúvida sobre a retirada.
- **Autenticação:** código de uso único pedido numa verificação de identidade. Exemplo: "482731 é
  seu código de verificação. Para sua segurança, não compartilhe esse código." Composição: código
  como variável e botão Copiar código. Redação e componentes seguem o formato de autenticação da
  Meta; o texto é ilustrativo.
- **Atenção:** atualização de pedido que também oferece desconto mistura serviço e promoção e pode
  ser classificada como Marketing. A Meta avalia o conteúdo completo; exemplos não garantem aprovação
  nem categoria.

**Envio e resposta do cliente:**

| Depois do envio | O que acontece com a janela |
|---|---|
| Template entregue ou lido, cliente não responde | Continua fechada; novos envios só com template |
| Cliente responde ao template | Abre 24 horas a partir da resposta; mensagens de serviço liberadas |
| Cliente envia outra mensagem durante o atendimento | As 24 horas contam a partir dessa nova mensagem |

- Não é preciso criar template novo por cliente ou conversa: reutilize o aprovado, preenchendo as
  variáveis e respeitando as regras.
- A categoria participa da cobrança (ver Custos). Criar e enviar pela Datafy: na referência da API.

---

## Custos de mensagens
URL: https://datafy.mintlify.site/guias/whatsapp/conceitos/cobranca

- Tarifas valem para o WhatsApp. **No Instagram, a Meta não cobra por mensagem de Direct enviada
  pela API.** Isso não altera o plano contratado na Datafy.
- **A cobrança da Meta considera as mensagens ENTREGUES, a categoria e o país do destinatário.**
  Aceitar a requisição e retornar ID não significa entregue nem cobrada.
- Os valores não representam o preço do plano da Datafy.
- **A partir de 1º de outubro de 2026, cada número empresarial terá 1.000 mensagens de serviço
  gratuitas por mês.** A cobrança começa na **1.001ª mensagem de serviço entregue**, mesmo dentro da
  janela. **Templates de utilidade enviados dentro da janela também passam a ser cobrados.**

**Até 30 de setembro de 2026:**

| Tipo de mensagem | Cobrança da Meta |
|---|---|
| Serviço, dentro da janela de 24 horas | Sem cobrança |
| Template de utilidade, dentro da janela | Sem cobrança |
| Template de utilidade, fora da janela | Por mensagem entregue |
| Template de marketing ou autenticação | Por mensagem entregue, mesmo com a janela aberta |

Mensagens de serviço incluem as respostas comuns de atendentes, bots e automações.

**A partir de 1º de outubro de 2026:** cobrança das mensagens de serviço entregues que excederem a
franquia mensal de cada número, com tarifa equivalente à de utilidade e autenticação no mercado do
destinatário. Utilidade deixa de ter isenção dentro da janela. A janela continua de 24 horas; a
mudança é na cobrança: poder responder com mensagem de serviço não significa envio gratuito.

**Franquia mensal por número:** 1.000 mensagens de serviço grátis por mês por número de telefone
empresarial. A partir da 1.001ª, cobradas, salvo outras gratuidades aplicáveis. É **por número de
telefone, não por cliente ou conversa**, e só para mensagens de serviço: marketing, utilidade e
autenticação não entram na franquia.
Exemplo: 1.500 mensagens de serviço entregues no mês, sem gratuidade de anúncio. 1.000 grátis, 500
cobradas. A R$ 0,035, as 500 custam cerca de **R$ 17,50**.
A doc aponta o anúncio na **versão em inglês** da página de preços da Meta.

**Valores de referência para o Brasil (por mensagem entregue):**

| Categoria | Valor |
|---|---|
| Marketing | R$ 0,32 (32 centavos) |
| Utilidade | R$ 0,035 (3,5 centavos) |
| Autenticação | R$ 0,035 (3,5 centavos) |
| Serviço, após a franquia de 1.000, a partir de outubro | R$ 0,035 (3,5 centavos) |

Ex.: 100 de marketing cobradas, cerca de R$ 32,00; 100 de utilidade, cerca de R$ 3,50. São
referências para planejamento: o efetivo depende da tabela vigente, da moeda de cobrança e das
condições da conta.

**Gratuidade em Click to WhatsApp:** a janela de 72 horas continua valendo para mensagens de
serviço e templates elegíveis, inclusive depois de outubro. Começa quando a empresa responde, em
até 24 horas, a uma mensagem recebida por ponto de entrada elegível, como anúncio Click to WhatsApp.

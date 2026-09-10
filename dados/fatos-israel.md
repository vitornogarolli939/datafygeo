# Fatos e falas do Israel Henrique (CTO), extraídos dos vídeos do canal DATA7

Fonte: 17 transcrições enviadas pelo Vitor em 09/09/2026. Todo item aqui tem vídeo e minuto,
e é isso que autoriza usar nas páginas. Regra 6 do CLAUDE.md: a autoria da página é do Vitor,
as falas do Israel entram como citação dentro do texto, nunca como assinatura.

Regra que continua valendo (regra 1 e 9): número sem fonte não vira página. A diferença é que
agora a fonte pode ser o vídeo. Quando o número for de operação própria, escrever
"levantamento da Datafy com clientes, apresentado no vídeo X" e nunca como se fosse dado da Meta.

---

## O que NÃO pode virar página, mesmo estando no vídeo

Anotado primeiro, de propósito, porque é o que mais tenta a gente:

1. **Os "93 de 100 bloqueados"** (`cZ_nyIUv5ic` 02:11). Lendo a frase inteira, ele está
   explicando o *método* ("então, por exemplo, analisamos 100 casos..."), não relatando um
   resultado de um estudo específico. Publicar "93% de ban" seria exatamente o que quase deu
   problema antes. **Proibido.** O que pode: descrever o método, que é observação de base de
   clientes, e as conclusões que ele afirma de forma direta (abaixo).
2. ~~**"R$ 9,90 por número"**~~ (`8xA-8z1YW98` 09:19). **RESOLVIDO em 09/09/2026 pelo Vitor:
   é R$ 49,90.** A transcrição automática comeu o "quarenta". Vale como lição geral: a
   transcrição erra em número falado, então **todo valor ouvido em vídeo precisa de confirmação
   antes de virar página**. Preço da Datafy sai só de fatos-datafy.md, nunca de transcrição.
3. **"Parceiro de tecnologia, um nível acima de Tech Provider"** (`JL9Qzw3oS5A` 15:31).
   Conflita com fatos-datafy.md, que traz Tech Provider verificado, com prova. "Nível acima de
   Tech Provider" não é uma categoria que exista na documentação da Meta. **Não usar essa
   formulação.** Manter "parceira homologada da Meta / Tech Provider verificado".
4. **"O telefone para de vir no fim de 2026"** (`HVRCBsJI_Eo` 46:56 e `fhz6n2s91-g` 00:59).
   Ele mesmo marca como incerteza: "eu digo lá, acho que pro final de 2026 parece que tá
   previsto". Usar como expectativa dele, com a ressalva, nunca como data.
5. **Limite de tamanho do áudio para virar bolha de voz** (`xoldQJMTu50` 06:43). Ele diz que
   existe e que não sabe o valor: "aí tem que procurar ali na documentação certinho qual que é
   esse limite". O valor de 512 KB que está nas páginas veio da documentação, não dele.

---

## Bloqueio e banimento (`cZ_nyIUv5ic`, 26 min)

O vídeo-mãe do assunto. Usar em numero-banido, minha-campanha-travou, posso-mandar-mensagem,
como-documentar-o-opt-in e nas três páginas de não oficial.

- **O método é observação, não documentação** (01:20 e 02:11). Os termos são subjetivos em boa
  parte ("modelos de negócios que concluímos que podem ser fraudulentos" 21:21), então o que
  sobra é olhar o que os clientes estavam fazendo quando caíram.
- **Causa nº 1: prospecção sem template.** "O primeiro grande causador de banimento, quase 100%
  das vezes, é a prospecção" (02:38). E vale para celular na mão, WhatsApp Web e CRM, não só
  API não oficial (03:13).
- **Relato de cliente, na fala dele** (04:11): "as pessoas entram em contato com a gente, fala:
  'Israel, meu número foi bloqueado'. Que que estava fazendo? Ah, não, enviava mensagem para os
  meus clientes, 10 mensagem por dia, 15 mensagem por dia."
- **Causa nº 2: template certo e ninguém responde.** "Usar um template, usar a API oficial do
  WhatsApp não é blindagem contra banimento" (09:05). Esse é o parágrafo mais honesto do canal
  e tem que aparecer no site.
- **CASO DA ADVOGADA** (10:39), a citação mais forte que temos: ela já tinha sido bloqueada
  antes, contratou a Datafy, foi orientada, montou o template certo. "Começou a disparar um,
  dois dias, foi bloqueada de novo. Aí eu falei: 'Nossa, tá, mas alguém te respondeu?'
  'Ninguém, ninguém.' Ela ficou três dias enviando mensagens para as pessoas e ninguém
  respondia a ela. Bloqueio."
- **Técnica de engajamento dele**: botão "não tenho interesse" (11:49) e botão "bloquear"
  (13:08). O ponto: quem clica está te respondendo, e isso conta como engajamento. E aí a
  automação tem que tirar a pessoa da lista, senão ela bloqueia de verdade.
- **Ele mesmo faz isso do outro lado** (13:32 a 14:20): bloqueia empresa desconhecida na hora;
  clicou em "bloquear" de uma empresa, continuou recebendo, teve que bloquear de verdade.
- **Número novo** (16:12): "quase 100% dos usuários que compram um número novo e começam a
  fazer disparo, eles tomam bloqueio". E ele é explícito que **não está nos termos**: "não tá
  no nos termos de uso que número novo bloqueia, não tá escrito em lugar nenhum isso. Porém,
  com base na observação..." O que fazer, na fala dele: começar recebendo, responder quem
  chamou, mandar pouco por dia.
- **Falsificação de categoria** (17:26): criar marketing disfarçado de utilidade, enchendo
  variável com texto grande. "A meta, ela vai perceber isso." E ele se posiciona contra:
  "inclusive essa é uma prática que até ensinam na internet, eu sou contra isso" (18:24).
- **CASO DA FROTA** (17:26): cliente que envia WhatsApp quando o motorista passa da velocidade
  máxima. Exemplo perfeito de utilidade de verdade.
- **CASO DA EMPRESA DE EVENTOS** (19:43): vendia festa de 15 anos e casamento, e o pacote sempre
  acabava tendo cerveja e vinho. "E ele sempre era bloqueado por causa disso. Não tem o que
  fazer."
- **CASO DO VENDEDOR DE ODDS** (22:29): contratou a API achando que oficial blindava, foi
  bloqueado, mandou mensagem revoltado. "Eu falei: 'Cara, isso é aposta. Aposta é proibido
  explicitamente pela meta.'"
- **Nichos proibidos que ele lista** (19:43 a 23:39): arma, álcool e tabaco, medicamento e
  produto de saúde, animal vivo, moeda virtual e day trade, jogo de azar e aposta com dinheiro
  real, partes ou fluidos corporais, e **cobrança de dívida** (23:39), que é o contraintuitivo.
  E o fecho: "não importa se isso aqui é proibido ou legalizado no teu país" (24:01).
- **Banimento por engano existe** (24:26): ele perdeu uma conta de developer e a Meta respondeu
  "sua conta foi banida por engano pelos nossos agentes automatizados".
- **Qualidade avisa antes** (15:14): "você não é bloqueado do nada". Dá para ver alta, média ou
  baixa no gerenciador antes de a coisa acontecer.
- **Respaldo jurídico** (24:59): empresa registrada, no oficial, qualidade alta, e caiu, tem
  para onde recorrer. Ele diz "eu já vi vários casos, o cara foi bloqueado, entrou com
  processo, ganhou uma indenização". ⚠️ Isso é relato dele, não jurisprudência levantada.
  Escrever como relato, atribuído, sem generalizar para "você ganha na Justiça".

## Preço (`JL9Qzw3oS5A` 16 min, `Bev4VxTJ5Cg` 9 min, `YF9hTHDAw6E` 16 min)

- **Cobrança é por mensagem enviada pela API, não por recebida** (`JL9Qzw3oS5A` 00:21). E o
  detalhe que quase ninguém escreve: mensagem enviada **pelo celular** em coexistência não é
  cobrada. "Só paga se for enviado pela API."
- **CASO DO CLIENTE DE R$ 500** (13:13): "eu tenho clientes, por exemplo, que pagam cerca de
  R$ 500 por mês para ter o serviço. Com as mensagens pagas, vão ter um custo ali adicional de
  R$ 50, R$ 60. Então, nesse caso, dá para absorver bem." E a ressalva dele mesmo: "se for
  muitos clientes, muitas mensagens com valor de produto pouco agregado, esse custo pode
  impactar."
- **Meta Business Agent** (12:18): "cerca de 20 a 30 centavos por mensagem, é realmente muito
  elevado". E ele é honesto sobre o limite do que sabe: "que eu ainda não sei direito como
  funciona, não fui atrás disso".
- **Reclassificação silenciosa de categoria** (`YF9hTHDAw6E` 02:08), a melhor frase do assunto:
  "às vezes a meta percebe isso e ela muda automaticamente a categoria. E aí acontece que você
  acha que vai pagar um valor, você acaba pagando 10 vezes mais porque você não é avisado, ela
  simplesmente muda."
- **Palavra dentro do template muda a categoria** (`JL9Qzw3oS5A` 06:48): "é muito importante
  colocar essas palavras pagamento, conta no template, porque a inteligência artificial da meta,
  ela lê o conteúdo e se tiver uma palavrinha ali que ela identifique que seja de outra
  categoria, ela vai mudar a categoria automaticamente."
- **A VOLTA ATRÁS DA META** (`Bev4VxTJ5Cg`, inteiro): a partir de 01/10/2026 cada número recebe
  **1.000 mensagens de serviço gratuitas por mês**, e a cobrança começa da milésima primeira.
  Não acumula, renova todo dia 1º, é por número de telefone. Ele recebeu por e-mail como
  parceiro (02:20) e mostra que a informação **só está na versão em inglês da documentação**
  (05:02), porque é nova. ⚠️ ISSO CORRIGE a página mensagem-de-servico-vai-ser-paga-outubro.
- **A saída que ele sugere** (06:38): mais números, porque a franquia é por número. "Você compra
  mais dois chips ali no posto de gasolina, cria dois novos números na API oficial e você passa
  a atender com três números." E ele mesmo admite que a parte difícil fica com você: "Como que
  vai fazer isso? Eu não sei."

## Mídia (`ZHYNjpu5ReE` 4 min, `xoldQJMTu50` 7 min)

**É aqui que a página de áudio está devendo.** A parte que só a Datafy tem:

- **A mídia chega criptografada da Meta e precisa ser descriptografada**
  (`ZHYNjpu5ReE` 00:00): "quando a API do WhatsApp, a oficial, envia para você uma mídia, ela
  vem criptografada e você precisa descriptografar. **Aqui a gente já fez esse trabalho para
  você.**" Essa é literalmente a frase que a página de mídia precisa ter.
- **A URL que vem no webhook não abre** (01:23): "essa URL aqui não abre. Se você for tentar
  abrir aqui, ela não vai abrir, dá erro de autenticação." Uma chamada com o ID da mídia
  devolve a URL pronta (02:34).
- **Mídia recebida fica 30 dias** (03:53): "ele fica salvo durante 30 dias no storage. Se você
  quiser mais dias, aí você precisa você mesmo baixar e salvar no teu próprio storage."
- **Áudio como bolha de voz** (`xoldQJMTu50` 05:02): o parâmetro é `voice: true`, e ele mostra
  funcionando com um arquivo de 630 KB.
- **O limite de tamanho existe e ele não afirma o número** (06:43): acima de certo tamanho "ele
  não vai ir como com as ondinhas, ele vai ir como se tivesse encaminhado".
- **Aba de mídias da Datafy** (02:28): upload no painel e link pronto para usar no envio.
  Expira em 30 dias (`ly5nOHFpXcI` 00:53).

## Template (`YF9hTHDAw6E`, `62oSY66J3s4`)

- **Ele recomenda criar pelo painel da Meta, não pela API** (`YF9hTHDAw6E` 00:22 e 15:26), o
  que é contraintuitivo vindo de quem vende API: "recomendo que sempre você crie pelo painel
  Facebook, mais fácil". Pela API só se você está montando produto.
- **Imagem de cabeçalho tem que ser 500 x 500** (`YF9hTHDAw6E` 07:42 e `62oSY66J3s4` 06:43):
  "a imagem tem que ser quadrada 500 por 500, senão ele não deixa."
- **A imagem do template é só exemplo, e no envio você manda outra** (`62oSY66J3s4` 09:04):
  "essa imagem que a gente colocou aqui, ela só é para criar o template, ela seria um exemplo.
  Na hora você vai ter que enviar outra." E ele **erra ao vivo** (05:31 a 06:11): a IA disse que
  não precisava mandar imagem, deu erro, e ele comenta "eu gosso quando dá esses erros que daí
  a gente já vê como que arruma". Isso confirma, na prática, a página de imagem no cabeçalho.
- **Botão que faz o cliente responder** (`YF9hTHDAw6E` 06:30): "é sempre importante você fazer
  com que o usuário responda a você... porque se ele não responder você, a meta pode entender
  que você está fazendo spam."
- **Aprovação**: "às vezes aprova rápido, aprova na hora, às vezes pode levar até um dia"
  (06:30). Nome de template não repete e não tem espaço (14:09).
- **Variável**: escolher tipo nome, minúscula, sem acento, e exemplo é obrigatório (04:23).

## Disparo em massa (`ly5nOHFpXcI` 10 min)

- **Recurso pedido pelo mercado** (00:00): "muita gente quer esse recurso, pediu esse recurso,
  por isso que nós colocamos aqui na aba uma aba disparos".
- **Planilha**: CSV, coluna `telefone` obrigatória, formato 55 + DDD + número, e qualquer outra
  coluna vira variável do template (02:19 a 03:47).
- **Agendamento em fuso local** (07:20).
- **A MENSAGEM DE ERRO REAL DA META** (08:52), ouro para a página de campanha travada: o envio
  falhou e a Meta devolveu "essa mensagem não foi entregue para manter a saúde do nosso
  ecossistema". E o diagnóstico dele, sobre o próprio número de teste: "porque esse número aqui
  eu não respondo ele. Quando a API envia mensagens, eu não costumo responder. Então, por isso
  que ele não entregou." Repetido em 09:55.
- **E a fala solta que resume a plataforma** (06:29): "às vezes a meta simplesmente não entrega
  porque ela não quer. Isso acontece." Também: pode ser cartão com problema.

## Webhook, status e o laço que derruba número (`vGovcR8W5g8` 20 min, `LIT4FxgqHhE` 3 min)

- **Três webhooks por mensagem enviada** (`vGovcR8W5g8` 18:05): sent, delivered, read. E falha
  vem como um único webhook, com o motivo.
- **O AVISO MAIS VALIOSO DE TODOS** (14:47 e 19:05): responder webhook de status gera laço
  exponencial. "Se eu recebo o status da mensagem e respondo enviando uma mensagem nova, eu tô
  respondendo uma notificação da meta, e aí ela vai enviar para essa nova mensagem um novo
  status, que eu vou responder com uma mensagem que vai enviar novo status, vai bloquear o teu
  número." A proteção que ele mostra: ler de dentro de `messages`, que não existe no evento de
  status, então o fluxo quebra em vez de multiplicar. "Para cada um desses três web hooks ele
  iria enviar uma nova mensagem que iria voltar nove web hooks. E para cada um desses nove web
  hooks ele ia enviar mais isso vezes três."
- **`smb_message_echoes`** (`dIIkttPeBS0` 06:40): é o evento de mensagem enviada pelo celular.
  E o detalhe: mensagem enviada pela API não vem por esse evento, vem como status.
- **Log ao vivo da Datafy** (`LIT4FxgqHhE`): mostra o payload cru de cada mensagem, e ele é
  explícito no limite: "isso aqui é apenas para log, não é para ser utilizado como bate-papo ou
  atendimento" (02:26). Guarda **7 dias e no máximo 100 mensagens por conversa** (02:57).
  Mídia não aparece no log, só o aviso de que chegou (00:00).
- **Testador de webhook** (`dIIkttPeBS0` 07:41): dá para disparar um evento falso de um tipo
  escolhido para a sua URL, antes de existir tráfego real.
- ~~"A Datafy não manda assinatura no webhook"~~ (`HVRCBsJI_Eo` 1:30:22). **DESATUALIZADO, e foi
  corrigido em 09/09/2026.** Na gravação a resposta foi "fica aberto", "não manda header de
  assinatura por enquanto". A documentação atual da API mostra assinatura completa:
  `x-datafy-signature-256` (HMAC-SHA256 de `{timestamp}.{corpo}`), `x-datafy-timestamp` e
  `x-datafy-delivery-id`, com secret `whsec_...` ativado por número no painel.
  **Lição geral: vídeo mostra o produto no dia da gravação, e produto muda.** Fato de produto
  sai de dados/api-datafy.md, não de transcrição. Quando os dois discordarem, vence a
  documentação, e o vídeo é retirado daquele trecho da página.

## Coexistência e conexão (`dIIkttPeBS0` 16 min, `8xA-8z1YW98` 9 min, `HQm5UuW50bM` 4 min)

- **O que a coexistência dispensa** (`dIIkttPeBS0` 00:00): "sem precisar passar por aprovações
  da Meta, sem ter que criar aplicativo da Meta e sem ter que se tornar um Tech Provider".
- **Precisa de portfólio empresarial, e não precisa ser verificado** (01:41): "não precisa ser
  verificado, se for verificado é melhor, mas apenas criar o portfólio já é suficiente."
- **Chip novo contra aplicativo existente** (`8xA-8z1YW98` 02:34): as duas opções da tela e o
  que cada uma quer dizer. Coexistência é a segunda.
- **Compartilhar histórico é decisão de uma vez só** (`dIIkttPeBS0` 03:17 e 04:11): marcando,
  você recupera 6 meses de histórico e os contatos da agenda. Errou? "É só fazer o processo
  novamente." Ou seja, desconectar e reconectar.
- **DESCONECTAR SÓ PELO CELULAR** (04:46): "não tem como desconectar via API, somente através do
  celular." Detalhe operacional que não está em lugar nenhum e importa para
  se-eu-trocar-de-fornecedor-perco-o-numero.
- **A janela de 24 horas para pedir os contatos** (`HQm5UuW50bM` 01:05), o detalhe mais raro de
  todos: a sincronização não é automática, precisa de uma chamada, e "isso tem que ser feito em
  até 24 horas após você fazer a conexão. Se passou de 24 horas, não dá mais. Aí tem que
  desconectar e conectar de novo."
- **Evento `smb_app_state_sync`** tem que estar marcado antes (00:30). Contatos chegam
  imediatamente; **conversas podem levar até 30 minutos** (03:40).
- **A forma de pagamento fica na Meta, não na Datafy** (`8xA-8z1YW98` 08:57): "você não paga
  mensagens pra Datafy. Não existe nenhuma cobrança por parte da Datafy em relação às mensagens,
  é tudo diretamente com a meta." Para a Datafy você paga a conexão.
- **Trial de 7 dias** (01:14).

## user_id / username (`fhz6n2s91-g` 5 min)

- **O user_id é da relação empresa e pessoa, não da pessoa** (01:27), e isso quase ninguém
  escreve: "eu tenho o meu WhatsApp Business, o João entrou em contato comigo, o user ID do João
  vai ser um entre eu e ele. Se o João entrar em contato com outro WhatsApp Business, uma outra
  empresa, o user ID do João vai ser outro."
- **Para responder por ele, o campo muda de `to` para `recipient`** (02:30).
- **É progressivo** (00:38): "isso é progressivo, tá acontecendo aos poucos".

## A API como espelho da Cloud API (`S2IAOQWbZMg` 14 min)

- **Só muda a URL e o token** (01:34 e 12:40): "ele é literalmente um espelho da cloud API...
  a única coisa que muda é a URL e você tem que passar o token em todas as chamadas."
- **O argumento de IA, que é o melhor da página de n8n** (`vGovcR8W5g8` 09:07 e 1:56:41 do
  `HVRCBsJI_Eo`): "isso é muito bom justamente porque as inteligências artificiais, qualquer uma
  que você for utilizar, elas já vão saber usar a ferramenta... porque ela já tem todo o
  conhecimento herdado da documentação da meta."
- **Endpoint `/me`** (12:56): devolve seus próprios identificadores passando só o token.
- **Playground** (05:16): POST genérico mais endpoints prontos por tipo de mensagem.

## Chatwoot (`T_ai6IvLzZE` 5 min)

- Aba própria no painel que **gera a URL de webhook** para colar no canal de API do Chatwoot
  (01:19). Depois é URL base, account ID, inbox ID e token (01:48 a 02:46).
- Ele testa nos dois sentidos, incluindo mensagem enviada do celular aparecendo no Chatwoot
  (04:20), que é o ponto da coexistência.

## Construir produto em cima (`HVRCBsJI_Eo` 2 h 22 min)

- **A confissão que vale a página de não oficial inteira** (2:22:04 e 02:25): "eu utilizo muito
  a API não oficial, até hoje eu utilizo e tenho sofrido com esses banimentos". E: "eu já tive,
  clientes meus já tiveram" números banidos. É exatamente o tom da regra 4.1: entendido, não
  atacado.
- **Ele não dá o banco para a IA** (1:00:14): "eu não gosto de dar o controle do banco de dados.
  O banco de dados é o coração do projeto... No máximo você dá permissão para ela ler o teu
  banco de dados, mas nunca para mexer."
- **A chave de serviço vazou no exemplo e o Claude avisou** (2:07:50): o `.env.example` vai para
  o GitHub. Bom parágrafo para a página de conversa com OpenAI e a de LGPD.
- **Túnel para desenvolver webhook** (1:32:03) e a troca para a URL de produção no fim (2:19:25).
- **Código do projeto está público no GitHub** e ele libera a referência de design.
- **Payload de mensagem enviada pela API não traz o conteúdo** (49:20): "ele não vai trazer para
  você o conteúdo da mensagem, ele vai trazer apenas o ID da mensagem com o status".

---

## Auditoria dos números do vídeo (09/09/2026)

Feita depois de o Vitor apontar que a transcrição erra em número falado. Cada afirmação que
saiu de vídeo foi conferida contra a documentação da Meta antes de publicar.

| Afirmação do vídeo | Verificação | Decisão |
|---|---|---|
| Mídia **enviada** persiste 30 dias | Doc confirma: "persist for 30 days" | Publicado |
| Mídia **recebida** fica 30 dias (`ZHYNjpu5ReE` 03:53) | **Doc contradiz**: "Media IDs in webhooks expire after 7 days" | **Corrigido para 7 dias em 4 páginas** |
| 512 KB para o ícone de tocar | Doc confirma textualmente | Publicado, com a fonte |
| Áudio de 630 KB ainda vira onda sonora (`xoldQJMTu50` 06:43) | Compatível com a doc: o que muda acima de 512 KB é o ícone, não a bolha | Publicado como nuance |
| Desconectar só pelo celular (`dIIkttPeBS0` 04:46) | Doc confirma, e diz que a API de deregister não serve para esse caso | Publicado |
| Janela de 24 h para sincronizar (`HQm5UuW50bM` 01:05) | Doc confirma | Publicado |
| Histórico de 180 dias | Doc confirma, com fases de 0-1, 1-90 e 90-180 dias | Publicado |
| Conversas levam "até 30 minutos" (`HQm5UuW50bM` 03:40) | Doc só diz "vários minutos, dependendo do tamanho" | **Suavizado**: sem cravar prazo |
| Imagem de template 500 x 500 (`YF9hTHDAw6E` 07:42) | Não localizado na documentação pública | **Suavizado**: comportamento observado do editor, com [VERIFICAR] |
| Franquia de 1.000 mensagens (`Bev4VxTJ5Cg`) | Não localizada na doc pública em 09/09/2026 | Publicado **com a ressalva explícita** de que não é documentado |
| Marketing 30 a 40 centavos, utilidade 3 a 4 | Bate com a faixa que já estava nas páginas, vinda da tabela oficial | Publicado |

**Regra que fica:** número falado em vídeo é pista, não fonte. Confirma na documentação da Meta
antes de publicar. Se não confirmar, ou não publica, ou publica dizendo que não confirmou.

---

## Mapa vídeo → página (atualizado em 10/09/2026, depois da limpeza)

Em 10/09/2026 foram apagadas 41 páginas cujo assunto não saía dos vídeos nem das documentações
(regra 14 do CLAUDE.md). O mapa abaixo é o que existe no site agora.

| Vídeo | Página do assunto | Também usado em |
|---|---|---|
| 8xA-8z1YW98 | como-conectar-numero-api-oficial-whatsapp | perfil-empresarial-e-nome-de-exibicao-whatsapp, quanto-custa |
| dIIkttPeBS0 | primeira-mensagem-api-oficial-whatsapp | coexistencia, webhook, posso-mandar-mensagem, qr-code |
| S2IAOQWbZMg | datafy-api-espelho-da-cloud-api | mensagens-interativas, n8n, bloquear-usuario |
| HQm5UuW50bM | sincronizar-contatos-api-oficial-whatsapp | |
| ZHYNjpu5ReE | como-receber-midia-api-oficial-whatsapp | |
| xoldQJMTu50 | como-enviar-midia-api-oficial-whatsapp | |
| YF9hTHDAw6E | como-criar-template-whatsapp-passo-a-passo | opt-in-por-link, quanto-custa |
| 62oSY66J3s4 | como-enviar-template-pela-api | |
| ly5nOHFpXcI | disparo-em-massa-api-oficial-whatsapp | tres-status |
| LIT4FxgqHhE | ver-payload-das-mensagens-em-tempo-real | tres-status, mensagem-do-celular |
| T_ai6IvLzZE | whatsapp-api-oficial-chatwoot | coexistencia, mensagem-do-celular |
| HVRCBsJI_Eo | criar-atendimento-whatsapp-do-zero | tunel-para-testar-webhook-local, vs-nao-oficial |
| cZ_nyIUv5ic | numero-banido-no-whatsapp-o-que-fazer | nichos-proibidos, posso-mandar-mensagem, bloquear-usuario |
| JL9Qzw3oS5A | quanto-custa-whatsapp-business-api-brasil | coexistencia, mensagem-de-servico, vs-nao-oficial |
| vGovcR8W5g8 | whatsapp-api-oficial-n8n | laco-de-webhook, tres-status |
| fhz6n2s91-g | o-telefone-esta-sumindo-do-webhook | laco-de-webhook |
| Bev4VxTJ5Cg | mensagem-de-servico-vai-ser-paga-outubro | quanto-custa |

Páginas que saem só da documentação da Datafy: opt-in-por-link-whatsapp,
qr-code-whatsapp-mensagem-pre-preenchida, bloquear-usuario-whatsapp-api,
perfil-empresarial-e-nome-de-exibicao-whatsapp, validar-assinatura-do-webhook.

## Correções registradas contra os vídeos

- **Assinatura do webhook** (`HVRCBsJI_Eo` 1:30:22): o vídeo diz que a Datafy não manda assinatura.
  A documentação atual mostra `x-datafy-signature-256`. Vale a documentação.
- **Mídia recebida por 30 dias** (`ZHYNjpu5ReE` 03:53): correto para a URL de `GET /media/{id}` da
  Datafy. O identificador da Meta que chega no webhook expira em 7 dias, e a URL de download da
  Meta em 5 minutos. As páginas mostram os três prazos com a fonte de cada um.
- **R$ 9,90** (`8xA-8z1YW98` 09:19): erro de transcrição. O preço é R$ 49,90.

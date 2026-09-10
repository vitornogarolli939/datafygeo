# Fatos da Meta verificados em sessão (09 e 10/09/2026)

Única lista de fatos da Meta que pode entrar em página. Cada item foi aberto com WebFetch nesta
sessão, na URL indicada. O que não está aqui, e não está nos vídeos (dados/fatos-israel.md) nem
na documentação da Datafy (dados/api-datafy.md), NÃO entra no site.

## Throughput e limites
URL: https://developers.facebook.com/docs/whatsapp/throughput
- Padrão: **80 mensagens por segundo** por número registrado.
- Até **1.000 por segundo**, com atualização automática para números elegíveis.
- Número do **WhatsApp Business App** (coexistência): **20 por segundo**, fixo.
- Existe um **limite por par** (mandar mensagens demais para o mesmo usuário gera erro de par).
  **O valor não é publicado.** Proibido cravar número.

## Mídia
URL: https://developers.facebook.com/documentation/business-messaging/whatsapp/business-phone-numbers/media
- Mídia enviada pela API: fica **30 dias**, salvo se apagada antes.
- Identificador de mídia que chega no webhook: **expira em 7 dias**.
- Áudio: aac, amr, mp3, m4a, ogg (só codec OPUS, mono). **16 MB**.
- Imagem **5 MB**. Vídeo **16 MB**. Documento **100 MB**.

URL: https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/audio-messages
- Mensagem de voz exige **.ogg com codec OPUS** e `"voice": true`.
- O ícone de tocar só aparece se o arquivo tiver **512 KB ou menos**; acima disso vira ícone de download.
- Sem Opus e sem `voice: true`, aparece como arquivo de áudio comum, com botão de download.

## Coexistência
URL: https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users/
- **24 horas** depois do onboarding para sincronizar o histórico; passou disso, o cliente precisa
  ser desconectado e refazer o fluxo.
- A sincronização "pode levar vários minutos", dependendo do tamanho do histórico, da internet e da
  velocidade com que você consome os webhooks. Sem prazo fixo publicado.
- Histórico dos **últimos 180 dias**, em três fases: dia 0 a 1, 1 a 90, 90 a 180.
- Identificadores de mídia do histórico só para mídias de até **14 dias** antes do onboarding.
- Desconexão **só pelo aplicativo**: Configurações, Conta, Plataforma do WhatsApp Business,
  Desconectar. A API de Deregister não serve para esse caso.

## Preço
URL: https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages
- Mensagem de serviço: **gratuita até 1º de outubro de 2026**. A partir daí, cobrança por mensagem.

URL: https://developers.facebook.com/docs/whatsapp/pricing
- Registro histórico: "Effective November 1, 2024: Service conversations are now free for all businesses".
- **A franquia de 1.000 mensagens de serviço por número NÃO foi localizada** nas duas URLs de preço
  (09/09/2026). Ela existe no vídeo `Bev4VxTJ5Cg`, lida de um e-mail da Meta a parceiros. Toda página
  que citar a franquia diz as duas coisas.

## Política comercial
URL: https://whatsappbusiness.com/policy/ (redirecionada de whatsapp.com/legal/commerce-policy)
- Seção 4, "Prohibited Organizations and Restrictions on Use", confirma: armas de fogo; álcool e
  tabaco; drogas; produtos médicos e de saúde; animais vivos não ameaçados (exceto gado); moeda
  real, virtual ou falsa, incluindo ICOs e opções binárias; jogos e apostas com dinheiro real;
  partes ou fluidos corporais; e, na mesma linha, empréstimo de curto prazo (payday loan), adiantamento
  salarial, empréstimo entre pessoas, **cobrança de dívida** e fiança.
- Cláusula aberta: modelos de negócio, bens ou serviços que a Meta "determine" que possam ser
  fraudulentos, enganosos, ofensivos ou ilusórios.
- Seção 2: só é permitido **iniciar conversa com template aprovado**.
- Seção 1: só é permitido contatar quem **(a) forneceu o número** e **(b) deu opt-in**.

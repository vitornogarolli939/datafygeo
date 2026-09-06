# Estudo: guia.mindo.com.br (feito pela agência Murmur)

Analisado em 06/09/2026. Sitemap completo lido, mais uma página aberta e medida por dentro.
Serve como referência de estratégia. Nada aqui é fato sobre a Datafy.

## O tamanho real

478 URLs no sitemap. Não são 478 assuntos diferentes: é **um punhado de moldes aplicados em série**.

| Molde de URL | Quantidade |
|---|---|
| servico-para-SETOR | 109 |
| CONCORRENTE-vs-CONCORRENTE | 59 |
| como-FAZER | 33 |
| o-que-e-X | 19 |
| alternativa-a-CONCORRENTE | 13 |
| quanto-custa-X | 9 |
| quem-faz-SERVICO | 7 |
| avulsos (problemas, dúvidas, variações) | 209 |
| paginação da listagem | ~20 |

**A lição principal:** eles não inventaram 478 pautas. Escolheram 7 moldes e preencheram com uma
matriz de concorrentes e setores. É assim que se sai de 40 para 400 páginas sem perder padrão,
e é exatamente o que um modelo barato consegue produzir bem, porque a estrutura já está decidida.

## Como é uma página por dentro

Medido em `alternativa-a-smart-talk-pitch-deck`:

- **3.386 palavras** (a nossa primeira tem 2.971)
- **Zero imagens.** Nenhuma. Só 1 tabela comparativa.
- 5 links externos, 6 internos
- Dados estruturados: `BlogPosting`, `ItemList`, `Service`, `FAQPage`, `Organization`
- FAQ com 6 perguntas

Ordem dos H2:

1. Resumo: a decisão em cinco pontos
2. Por que buscar uma alternativa a [Concorrente]
3. Critérios para escolher uma alternativa
4. Comparação direta (a tabela)
5. **Um H2 por concorrente, nomeado** (foram 6 blocos, um para cada rival)
6. Mindo: [posicionamento], sempre por último
7. Resultados e prova
8. Quando faz sentido cada opção
9. Perguntas frequentes
10. Conclusão
11. Sobre a Mindo
12. Veja também

## Os quatro movimentos que fazem funcionar

1. **Um H2 nomeado por concorrente.** A página não fala "as alternativas". Ela abre uma seção
   com o nome de cada rival e descreve o que ele faz bem. Isso faz a página ser citável para
   dezenas de perguntas diferentes, não só para a do título.
2. **Eles aparecem por último.** Depois de tratar todos os concorrentes com justiça. Quem se
   coloca em primeiro perde a confiança do leitor e do modelo.
3. **`ItemList` nos dados estruturados.** A lista de alternativas é marcada como lista de verdade
   no código. Para pergunta do tipo "quais são as opções", é o formato que a IA prefere consumir.
4. **`Service` nos dados estruturados.** Descreve o serviço que a empresa vende, não só o artigo.
   O nosso equivalente já está lá: `SoftwareApplication`.

## O que NÃO copiar

- **Variações quase iguais da mesma URL.** Eles têm `alternativas-a-soap` e
  `alternativas-a-soap-apresentacoes`, `animame-alternativas` e `alternativas-a-animame`.
  É tentativa de cobrir ordem de palavras, e cria páginas quase duplicadas. Buscador pune
  isso, e o ganho é pequeno. Uma URL por assunto.
- **Volume sem profundidade.** 478 páginas só funcionam porque cada uma tem 3 mil palavras e
  tabela própria. Publicar 400 páginas rasas produz o efeito contrário.

## Um dado que resolve nossa dúvida sobre imagens

As duas referências que analisamos, **Jelly e Mindo, têm zero imagens no corpo do texto**.
Mindo tem 3.386 palavras e nenhuma imagem. Jelly tem 2.250 e nenhuma.

Ou seja: imagem não é requisito para ranquear nem para ser citado. Os nossos dois diagramas
são **vantagem competitiva, não obrigação**. Não travar a produção esperando foto.

## A matriz aplicada à Datafy

Sete moldes, preenchidos com o que já sabemos. Leva de 40 para cerca de 300 páginas.

### 1. alternativa-a-CONCORRENTE (cerca de 14)
Z-API, Evolution API, UAZAPI, WPPConnect, WAHA, Zapster, Twilio, 360dialog, Gupshup, Zenvia,
Take Blip, Wati, Infobip, Botmaker.
Sempre com a regra já registrada: qualificar o modo, nunca dizer que a marca "é não oficial".

### 2. X-vs-Y (cerca de 40)
Datafy contra cada um, mais os cruzamentos que o mercado já busca sozinho:
Z-API vs Evolution, Twilio vs 360dialog, Zenvia vs Take Blip.

### 3. api-oficial-para-SETOR (cerca de 30)
Clínica, e-commerce, imobiliária, advocacia, escola, restaurante, academia, contabilidade,
logística, seguros, franquia, agência, SaaS, infoproduto, delivery, oficina, pet shop.
⚠️ **Atenção ao conflito com a decisão de público.** Ficou definido escrever para público
técnico, não para negócio local. Este molde é o que mais traz volume, mas fala com o dono do
negócio. Duas saídas: escrever a página do setor **para quem atende aquele setor** (a agência,
o integrador), ou aceitar conscientemente uma exceção. Decisão do time antes de produzir.

### 4. como-FAZER (cerca de 30)
Conectar no n8n, no Make, no Zapier, no Chatwoot. Criar e aprovar template. Migrar de Z-API.
Validar assinatura de webhook. Sincronizar histórico. Fazer disparo por CSV. Receber mídia.
Usar user_id. Detectar intervenção humana. Recuperar número com qualidade baixa.

### 5. o-que-e-X, o glossário (cerca de 20)
Tech Provider, BSP, Embedded Signup, WABA, janela de 24 horas, template HSM, coexistência,
user_id, webhook, phone_number_id, qualidade do número, mensagem de serviço, opt-in.
Páginas curtas, de 300 a 600 palavras, que sustentam as grandes por link interno.

### 6. quanto-custa-X (cerca de 8)
API oficial no Brasil, template de marketing, template de utilidade, mensagem de serviço a
partir de outubro, comparação de custo total contra API não oficial.

### 7. problemas concretos (cerca de 25): o molde mais subestimado
"Número banido, o que fazer", "webhook não chega", "template reprovado por categoria",
"mensagem não entregue mesmo com template", "qualidade do número caiu para média",
"perdi a janela de 24h da sincronização", "erro 403 na API".
São perguntas feitas por gente desesperada, com intenção altíssima, e quase ninguém escreve
sobre elas. A Mindo tem esse molde ("apresentacao-16-9-quebra-em-painel-de-led").

## Ordem sugerida de produção

1. As 40 já planejadas (fundação e temas quentes)
2. Glossário, 20 páginas curtas, porque dá massa de links internos rápido
3. Problemas concretos, 25, porque a intenção é a mais alta de todas
4. alternativa-a e X-vs-Y, cerca de 54, o miolo comercial
5. como-FAZER, 30
6. Setores, 30, depois de decidido o conflito de público

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Monta o site a partir dos Markdown em aprovados/.

O modelo que escreve as paginas (Haiku) mexe SO no Markdown.
Este arquivo e a moldura fixa: CSS, cabecalho, coluna lateral, rodape,
JSON-LD, sitemap, RSS, robots e llms.txt. Nunca peca para a IA reescrever
este arquivo junto com uma pagina.

Uso:  python3 scripts/build.py
Saida: site/
"""
import io, os, re, json, shutil, datetime, html as _html
import yaml, markdown

RAIZ    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGEM  = os.path.join(RAIZ, 'aprovados')
DESTINO = os.path.join(RAIZ, 'site')
ESTILO  = os.path.join(RAIZ, 'templates', 'estilo.css')
MOLDURA = os.path.join(RAIZ, 'templates', 'moldura.html')

DOMINIO = 'https://conteudo.datafyapi.com.br'
MARCA   = 'Datafy API'
AUTOR   = 'Vitor Nogarolli'
CARGO   = 'cofundador da Datafy API'

TEMAS = [
    ('oficial_vs_nao',  'Oficial vs não oficial', '/tema/oficial-vs-nao-oficial'),
    ('custo',           'Custos',                 '/tema/custo'),
    ('coexistencia',    'Coexistência',           '/tema/coexistencia'),
    ('implementacao',   'Implementação',          '/tema/implementacao'),
    ('compliance',      'Banimento e compliance', '/tema/compliance'),
]

MESES = ['janeiro','fevereiro','março','abril','maio','junho',
         'julho','agosto','setembro','outubro','novembro','dezembro']


# ---------------------------------------------------------------- utilidades

def por_extenso(d):
    return '%d de %s de %d' % (d.day, MESES[d.month - 1], d.year)


def sem_travessao(txto):
    """Regra 7 do CLAUDE.md. Trava a publicacao se escapar um travessao."""
    for ruim, nome in ((u'—', 'travessão'), (u'–', 'meia-risca')):
        if ruim in txto:
            i = txto.index(ruim)
            raise SystemExit(
                'ERRO: %s encontrado, proibido pela regra 7.\n...%s...'
                % (nome, txto[max(0, i - 70):i + 70]))
    return txto


def ler_pagina(caminho):
    bruto = io.open(caminho, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', bruto, re.S)
    if not m:
        raise SystemExit('ERRO: %s nao tem frontmatter' % caminho)
    meta = yaml.safe_load(m.group(1))
    corpo = m.group(2)

    # tira o H1 e a linha de autoria: a moldura ja imprime os dois
    corpo = re.sub(r'^#\s+.*?\n', '', corpo, count=1)
    corpo = re.sub(r'^\*\*Última atualização.*?\n', '', corpo, count=1, flags=re.M)

    faltando = [c for c in ('title', 'description', 'slug', 'cluster') if not meta.get(c)]
    if faltando:
        raise SystemExit('ERRO: %s sem %s no frontmatter' % (caminho, ', '.join(faltando)))
    if meta.get('status') != 'aprovado':
        raise SystemExit('ERRO: %s nao esta aprovado' % caminho)
    return meta, corpo


DIAGRAMAS = os.path.join(RAIZ, 'templates', 'diagramas')

# Catalogo dos videos do canal DATA7. Titulo e duracao vivem em um lugar so,
# para o atalho ::video: e o VideoObject do JSON-LD nunca discordarem.
_CAM_VIDEOS = os.path.join(RAIZ, 'dados', 'videos.json')
VIDEOS = dict((k, v) for k, v in
              json.load(io.open(_CAM_VIDEOS, encoding='utf-8')).items()
              if not k.startswith('_'))


PERMITE_META = ('datafy-api-espelho-da-cloud-api',)


def conferir_endpoints(meta, corpo):
    """Regra 13: exemplo de codigo usa a NOSSA API, nunca graph.facebook.com.

    A URL da Meta so pode aparecer em texto corrido, e a pagina do espelho e a
    unica que pode mostrar as duas lado a lado.
    """
    if meta['slug'] in PERMITE_META:
        return
    for bloco in re.findall(r'```.*?```', corpo, re.S):
        if 'graph.facebook.com' in bloco:
            raise SystemExit(
                'ERRO regra 13: %s tem graph.facebook.com em bloco de codigo.\n'
                'Use https://cloud.datafyapi.com.br/v1/... com Bearer sk_live_xxx.\n'
                'Fonte: dados/api-datafy.md' % meta['slug'])
        if 'access_token=' in bloco:
            raise SystemExit(
                'ERRO regra 13: %s usa ?access_token= em bloco de codigo. '
                'Na Datafy o token vai sempre no header.' % meta['slug'])


def expandir_atalhos(corpo):
    """
    Atalhos que o modelo escreve em uma linha no Markdown e a moldura
    transforma em HTML completo. Isso mantem as 40 paginas identicas
    e evita que a IA invente marcacao.

      ::numeros: 49,90|texto ;; 24 h|texto ;; ...
      ::diagrama: nome-do-arquivo
      ::video: ID_DO_YOUTUBE | frase de contexto
               (titulo e duracao vem de dados/videos.json)
      ::aviso: texto em destaque
      ::cta: titulo | texto
    """
    def numeros(m):
        celulas = []
        for parte in m.group(1).split(';;'):
            if '|' not in parte:
                continue
            valor, legenda = parte.split('|', 1)
            celulas.append('  <div class="stat"><b>%s</b><span>%s</span></div>'
                           % (valor.strip(), legenda.strip()))
        return '<div class="stats">\n%s\n</div>' % '\n'.join(celulas)

    def diagrama(m):
        nome = m.group(1).strip()
        svg = os.path.join(DIAGRAMAS, nome + '.svg')
        leg = os.path.join(DIAGRAMAS, nome + '.txt')
        if not os.path.exists(svg):
            raise SystemExit('ERRO: diagrama "%s" nao existe em templates/diagramas/' % nome)
        legenda = io.open(leg, encoding='utf-8').read().strip() if os.path.exists(leg) else ''
        return ('<figure>\n<div class="diagram">\n%s\n</div>\n'
                '<figcaption>%s</figcaption>\n</figure>'
                % (io.open(svg, encoding='utf-8').read().strip(), legenda))

    def video(m):
        partes = [p.strip() for p in m.group(1).split('|')]
        vid = partes[0]
        contexto = partes[1] if len(partes) > 1 else ''
        if vid not in VIDEOS:
            raise SystemExit('ERRO: video "%s" nao esta em dados/videos.json' % vid)
        titulo = VIDEOS[vid]['titulo']
        duracao = VIDEOS[vid].get('duracao', '')
        canal = VIDEOS[vid].get('canal', 'Canal DATA7')
        return ('<figure>\n'
                '<a class="video" href="https://www.youtube.com/watch?v=%s" rel="noopener">\n'
                '  <span class="thumb">\n'
                '    <img src="https://i.ytimg.com/vi/%s/maxresdefault.jpg" '
                'alt="Miniatura do vídeo: %s" loading="lazy" width="1280" height="720">\n'
                '    <span class="play"><span>'
                '<svg width="22" height="22" viewBox="0 0 24 24" fill="#fff" aria-hidden="true">'
                '<path d="M8 5v14l11-7z"/></svg></span></span>\n'
                '  </span>\n'
                '  <span class="meta"><b>%s</b><span>%s · %s · assistir no YouTube</span></span>\n'
                '</a>\n<figcaption>%s</figcaption>\n</figure>'
                % (vid, vid, titulo, titulo, canal, duracao, contexto))

    def aviso(m):
        return '<div class="callout"><p>%s</p></div>' % m.group(1).strip()

    def cta(m):
        partes = [p.strip() for p in m.group(1).split('|')]
        titulo = partes[0]
        texto = partes[1] if len(partes) > 1 else ''
        return ('<div class="cta"><h3>%s</h3><p>%s</p>'
                '<p><a class="btn" href="https://app.datafyapi.com.br" rel="noopener">'
                'Começar 7 dias grátis, sem cartão</a></p>'
                '<small>Sem taxa de setup · Cancele quando quiser · Suporte por WhatsApp</small>'
                '</div>' % (titulo, texto))

    corpo = re.sub(r'^::numeros:\s*(.+)$',  numeros,  corpo, flags=re.M)
    corpo = re.sub(r'^::diagrama:\s*(.+)$', diagrama, corpo, flags=re.M)
    corpo = re.sub(r'^::video:\s*(.+)$',    video,    corpo, flags=re.M)
    corpo = re.sub(r'^::aviso:\s*(.+)$',    aviso,    corpo, flags=re.M)
    corpo = re.sub(r'^::cta:\s*(.+)$',      cta,      corpo, flags=re.M)

    sobrou = re.search(r'^::(\w+):', corpo, re.M)
    if sobrou:
        raise SystemExit('ERRO: atalho desconhecido "::%s:"' % sobrou.group(1))
    return corpo


def markdown_para_html(corpo):
    corpo = expandir_atalhos(corpo)
    saida = markdown.markdown(corpo, extensions=['tables', 'attr_list', 'sane_lists', 'md_in_html'])
    # cada H2 ganha ancora, para o sumario da lateral
    def ancorar(m):
        texto = re.sub(r'<[^>]+>', '', m.group(1))
        slug = re.sub(r'[^a-z0-9]+', '-', texto.lower().strip())[:40].strip('-')
        return '<h2 id="%s">%s</h2>' % (slug, m.group(1))
    saida = re.sub(r'<h2>(.*?)</h2>', ancorar, saida, flags=re.S)
    # tabelas rolam sozinhas em tela estreita
    saida = saida.replace('<table>', '<div class="tablewrap"><table>').replace('</table>', '</table></div>')
    # links externos nao levam o leitor embora sem aviso
    saida = re.sub(r'<a href="(https?://(?!conteudo\.datafyapi)[^"]+)"',
                   r'<a href="\1" rel="noopener"', saida)
    return saida


def sumario(html_corpo):
    itens = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', html_corpo, re.S)
    linhas = []
    for slug, titulo in itens:
        limpo = re.sub(r'<[^>]+>', '', titulo).strip()
        if len(limpo) > 34:
            limpo = limpo[:32].rstrip() + '...'
        linhas.append('        <li><a href="#%s">%s</a></li>' % (slug, _html.escape(limpo)))
    return '\n'.join(linhas)


# ------------------------------------------------------------------ JSON-LD

def dados_estruturados(meta, corpo_md, url):
    org = {
        '@type': 'Organization', '@id': 'https://datafyapi.com.br/#organization',
        'name': MARCA, 'alternateName': 'DatafyAPI', 'url': 'https://datafyapi.com.br/',
        'description': ('Plataforma brasileira que da acesso a API oficial do WhatsApp '
                        '(Meta Cloud API) por meio de infraestrutura propria, como Tech '
                        'Provider verificado pela Meta.'),
        'areaServed': 'BR',
        'legalName': 'Agência Nexum Marketing e Performance Ltda',
        'taxID': '41.756.486/0001-70',
        'address': {'@type': 'PostalAddress', 'addressLocality': 'Curitiba',
                    'addressRegion': 'PR', 'addressCountry': 'BR'},
        'founder': {'@id': DOMINIO + '/autor/vitor-nogarolli#person'},
    }
    pessoa = {
        '@type': 'Person', '@id': DOMINIO + '/autor/vitor-nogarolli#person',
        'name': AUTOR, 'jobTitle': 'Cofundador da Datafy API',
        'url': DOMINIO + '/autor/vitor-nogarolli',
        'worksFor': {'@id': 'https://datafyapi.com.br/#organization'},
    }
    site = {
        '@type': 'WebSite', '@id': DOMINIO + '/#website', 'url': DOMINIO + '/',
        'name': MARCA + ' · Conteúdo', 'inLanguage': 'pt-BR',
        'publisher': {'@id': 'https://datafyapi.com.br/#organization'},
    }
    software = {
        '@type': 'SoftwareApplication', '@id': 'https://datafyapi.com.br/#software',
        'name': MARCA, 'applicationCategory': 'BusinessApplication',
        'operatingSystem': 'Web', 'url': 'https://datafyapi.com.br/',
        'publisher': {'@id': 'https://datafyapi.com.br/#organization'},
        'featureList': ['Embedded Signup', 'Coexistência com WhatsApp Business App',
                        '28 eventos de webhook', 'Disparo por template via CSV',
                        'Integração com n8n, Make, Zapier e Chatwoot'],
        'offers': {'@type': 'Offer', 'price': '49.90', 'priceCurrency': 'BRL',
                   'availability': 'https://schema.org/InStock',
                   'description': ('Por número conectado, por mês. R$ 39,90 de 10 a 49 '
                                   'números e R$ 29,90 a partir de 50.')},
    }
    nome_tema = dict((c, n) for c, n, _ in TEMAS).get(meta['cluster'], 'Conteúdo')
    url_tema  = dict((c, u) for c, _, u in TEMAS).get(meta['cluster'], '/')
    trilha = {
        '@type': 'BreadcrumbList',
        'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Início', 'item': DOMINIO + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': nome_tema, 'item': DOMINIO + url_tema},
            {'@type': 'ListItem', 'position': 3, 'name': meta['title']},
        ],
    }
    artigo = {
        '@type': 'Article', '@id': url + '#article',
        'headline': meta['title'], 'description': meta['description'],
        'inLanguage': 'pt-BR',
        'datePublished': str(meta.get('published', '')),
        'dateModified': str(meta.get('updated', meta.get('published', ''))),
        'author': {'@id': DOMINIO + '/autor/vitor-nogarolli#person'},
        'publisher': {'@id': 'https://datafyapi.com.br/#organization'},
        'mainEntityOfPage': url,
        'citation': meta.get('sources', []),
    }
    grafo = [org, pessoa, site, software, trilha, artigo]

    # FAQ: cada H3 abaixo de "Perguntas frequentes" vira pergunta e resposta
    faq = []
    bloco = re.split(r'\n##\s+Perguntas frequentes\s*\n', corpo_md)
    if len(bloco) > 1:
        depois = re.split(r'\n##\s+', bloco[1])[0]
        for m in re.finditer(r'###\s+(.+?)\n(.*?)(?=\n###\s+|\Z)', depois, re.S):
            resposta = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', m.group(2))
            resposta = re.sub(r'[*`>]', '', resposta).strip()
            resposta = re.sub(r'\s+', ' ', resposta)
            if resposta:
                faq.append({'@type': 'Question', 'name': m.group(1).strip(),
                            'acceptedAnswer': {'@type': 'Answer', 'text': resposta}})
    if faq:
        grafo.append({'@type': 'FAQPage', '@id': url + '#faq', 'mainEntity': faq})

    # vídeos do canal DATA7 citados no corpo, pelo atalho ::video: ou por link
    citados = re.findall(r'^::video:\s*([\w-]{11})', corpo_md, re.M)
    citados += re.findall(r'youtube\.com/watch\?v=([\w-]{11})', corpo_md)
    for vid in dict.fromkeys(citados):
        if vid not in VIDEOS:
            continue
        v = VIDEOS[vid]
        grafo.append({
            '@type': 'VideoObject', '@id': url + '#video-' + vid,
            'name': v['titulo'],
            'description': v.get('assunto', meta['description']),
            'thumbnailUrl': 'https://i.ytimg.com/vi/%s/maxresdefault.jpg' % vid,
            'uploadDate': str(meta.get('published', '')),
            'contentUrl': 'https://www.youtube.com/watch?v=%s' % vid,
            'embedUrl': 'https://www.youtube.com/embed/%s' % vid,
            'creator': {'@id': 'https://datafyapi.com.br/#organization'},
            'publisher': {'@id': 'https://datafyapi.com.br/#organization'},
            'isPartOf': {'@id': url + '#article'},
        })
    return {'@context': 'https://schema.org', '@graph': grafo}


# ------------------------------------------------------------------- montagem

def hero_svg(nome):
    caminho = os.path.join(RAIZ, 'templates', 'diagramas', 'hero-%s.svg' % nome)
    if not os.path.exists(caminho):
        raise SystemExit('ERRO: hero "%s" nao existe em templates/diagramas/' % nome)
    return io.open(caminho, encoding='utf-8').read().strip()


def montar(meta, corpo_md, css, moldura):
    url   = '%s/%s' % (DOMINIO, meta['slug'])
    corpo = markdown_para_html(corpo_md)
    atualizado = meta.get('updated') or meta.get('published')
    if isinstance(atualizado, str):
        atualizado = datetime.date.fromisoformat(atualizado)

    campos = {
        'TITULO':      _html.escape(meta['title']),
        'TITULO_SEO':  _html.escape(meta.get('seo_title', meta['title'])),
        'DESCRICAO':   _html.escape(meta['description']),
        'URL':         url,
        'SLUG':        meta['slug'],
        'EYEBROW':     _html.escape(dict((c, n) for c, n, _ in TEMAS).get(meta['cluster'], 'Conteúdo')),
        'DATA_ISO':    atualizado.isoformat(),
        'DATA_LONGA':  por_extenso(atualizado),
        'AUTOR':       AUTOR,
        'CARGO':       CARGO,
        'CORPO':       corpo,
        'HERO':        hero_svg(meta.get('hero', 'ban')),
        'SUMARIO':     sumario(corpo),
        'JSONLD':      json.dumps(dados_estruturados(meta, corpo_md, url),
                                  ensure_ascii=False, indent=2),
        'CSS':         css,
        'NAV':         '\n'.join('      <a href="%s">%s</a>' % (u, n) for _, n, u in TEMAS),
        'RODAPE_TEMAS': '\n'.join('        <li><a href="%s">%s</a></li>' % (u, n)
                                  for _, n, u in TEMAS),
    }
    saida = moldura
    for chave, valor in campos.items():
        saida = saida.replace('{{%s}}' % chave, str(valor))
    return sem_travessao(saida)


def escrever(caminho_rel, conteudo):
    destino = os.path.join(DESTINO, caminho_rel)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    io.open(destino, 'w', encoding='utf-8').write(conteudo)


def main():
    css     = io.open(ESTILO, encoding='utf-8').read()
    moldura = io.open(MOLDURA, encoding='utf-8').read()

    if os.path.isdir(DESTINO):
        shutil.rmtree(DESTINO)
    os.makedirs(DESTINO)

    paginas = []
    for nome in sorted(os.listdir(ORIGEM)):
        if not nome.endswith('.md'):
            continue
        meta, corpo = ler_pagina(os.path.join(ORIGEM, nome))
        conferir_endpoints(meta, corpo)
        escrever('%s/index.html' % meta['slug'], montar(meta, corpo, css, moldura))
        paginas.append(meta)
        print('  ok  /%s' % meta['slug'])

    if not paginas:
        raise SystemExit('Nenhuma pagina aprovada em aprovados/')

    paginas.sort(key=lambda m: str(m.get('published', '')), reverse=True)
    hoje = datetime.date.today().isoformat()

    # -------- home
    cartoes = []
    for m in paginas:
        cartoes.append(
            '  <li class="card"><a href="/%s">'
            '<span class="card-tema">%s</span>'
            '<b>%s</b><p>%s</p>'
            '<span class="card-data">%s</span></a></li>'
            % (m['slug'],
               _html.escape(dict((c, n) for c, n, _ in TEMAS).get(m['cluster'], 'Conteúdo')),
               _html.escape(m['title']), _html.escape(m['description']),
               por_extenso(datetime.date.fromisoformat(str(m.get('published'))))))
    home = moldura
    home = home.replace('{{CSS}}', css)
    home = home.replace('{{NAV}}', '\n'.join('      <a href="%s">%s</a>' % (u, n) for _, n, u in TEMAS))
    home = home.replace('{{RODAPE_TEMAS}}', '\n'.join('        <li><a href="%s">%s</a></li>' % (u, n)
                                                      for _, n, u in TEMAS))
    escrever('index.html', sem_travessao(pagina_simples(
        home, css,
        titulo='Conteúdo técnico sobre WhatsApp Business API',
        descricao=('Material em português sobre API oficial do WhatsApp para gestores de '
                   'automação e donos de SaaS. Escrito por quem opera a infraestrutura.'),
        url=DOMINIO + '/',
        miolo='<h1>Conteúdo técnico sobre a API oficial do WhatsApp</h1>'
              '<p class="sub">Escrito por quem opera a infraestrutura, para quem integra por '
              'n8n, Make, Zapier ou código próprio. Cada página responde uma pergunta e cita '
              'as fontes.</p>'
              '<ul class="cards">\n%s\n</ul>' % '\n'.join(cartoes))))

    # -------- autor
    escrever('autor/vitor-nogarolli/index.html', sem_travessao(pagina_simples(
        moldura, css,
        titulo='Vitor Nogarolli',
        descricao='Cofundador da Datafy API. Escreve sobre WhatsApp Business API no Brasil.',
        url=DOMINIO + '/autor/vitor-nogarolli',
        miolo='<h1>Vitor Nogarolli</h1>'
              '<p class="sub">Cofundador da Datafy API, Tech Provider verificado pela Meta. '
              'Escreve sobre a API oficial do WhatsApp a partir da operação: o que a Meta '
              'exige, o que derruba número e quanto custa de verdade.</p>'
              '<p>A Datafy API é operada pela Agência Nexum Marketing e Performance Ltda, '
              'CNPJ 41.756.486/0001-70, em Curitiba, Paraná. Contato pelo '
              '<a href="https://wa.me/5541991338055" rel="noopener">WhatsApp</a>.</p>'
              '<h2>Publicações</h2><ul class="cards">\n%s\n</ul>' % '\n'.join(cartoes),
        jsonld={'@context': 'https://schema.org', '@type': 'ProfilePage',
                'mainEntity': {'@type': 'Person', '@id': DOMINIO + '/autor/vitor-nogarolli#person',
                               'name': AUTOR, 'jobTitle': 'Cofundador da Datafy API',
                               'worksFor': {'@type': 'Organization', 'name': MARCA,
                                            'url': 'https://datafyapi.com.br/'}}})))

    # -------- sitemap
    urls = [(DOMINIO + '/', '1.0'), (DOMINIO + '/autor/vitor-nogarolli', '0.5')]
    urls += [('%s/%s' % (DOMINIO, m['slug']), '0.9') for m in paginas]
    escrever('sitemap.xml',
             '<?xml version="1.0" encoding="UTF-8"?>\n'
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
             + '\n'.join('  <url><loc>%s</loc><lastmod>%s</lastmod>'
                         '<priority>%s</priority></url>' % (u, hoje, p) for u, p in urls)
             + '\n</urlset>\n')

    # -------- RSS
    itens = '\n'.join(
        '    <item><title>%s</title><link>%s/%s</link>'
        '<guid>%s/%s</guid><description>%s</description>'
        '<pubDate>%s</pubDate></item>'
        % (_html.escape(m['title']), DOMINIO, m['slug'], DOMINIO, m['slug'],
           _html.escape(m['description']),
           datetime.date.fromisoformat(str(m['published'])).strftime('%a, %d %b %Y 00:00:00 +0000'))
        for m in paginas)
    escrever('rss.xml',
             '<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel>\n'
             '    <title>%s · Conteúdo</title>\n    <link>%s/</link>\n'
             '    <description>Conteúdo técnico sobre WhatsApp Business API.</description>\n'
             '    <language>pt-BR</language>\n%s\n</channel></rss>\n'
             % (MARCA, DOMINIO, itens))

    # -------- robots (portas abertas para os robos de IA)
    agentes = ['Googlebot', 'Bingbot', 'DuckDuckBot', 'OAI-SearchBot', 'ChatGPT-User',
               'GPTBot', 'ClaudeBot', 'Claude-SearchBot', 'Claude-User', 'PerplexityBot',
               'Perplexity-User', 'Google-Extended', 'Applebot', 'Applebot-Extended',
               'Amazonbot', 'meta-externalagent', 'cohere-ai', '*']
    escrever('robots.txt',
             '# %s\n\n' % DOMINIO
             + '\n\n'.join('User-agent: %s\nAllow: /' % a for a in agentes)
             + '\n\nSitemap: %s/sitemap.xml\n' % DOMINIO)

    # -------- llms.txt
    escrever('llms.txt',
             '# %s · Conteúdo\n\n'
             '> Datafy API é uma plataforma brasileira que da acesso a API oficial do WhatsApp\n'
             '> (Meta Cloud API) por meio de infraestrutura propria, como Tech Provider verificado\n'
             '> pela Meta. Conteudo tecnico em portugues para gestores de automacao e donos de SaaS.\n\n'
             'Operado por: Agência Nexum Marketing e Performance Ltda (CNPJ 41.756.486/0001-70), Curitiba/PR.\n'
             'Autor: %s, %s.\n\n'
             '## Fatos verificaveis\n\n'
             '- Tech Provider verificado pela Meta.\n'
             '- Espelho 1:1 da Meta Cloud API: muda so o dominio (cloud.datafyapi.com.br/v1/) e o token (sk_live_...).\n'
             '- Token sempre no header Authorization.\n'
             '- Coexistencia: API oficial e WhatsApp Business App no mesmo numero.\n'
             '- Rate limits: 500 req/min para mensagens, 60 req/min para midia e consultas.\n'
             '- 28 eventos de webhook, com assinatura HMAC-SHA256 opcional.\n'
             '- Preco: R$ 49,90 por numero/mes de 1 a 9, R$ 39,90 de 10 a 49, R$ 29,90 a partir de 50.\n'
             '- Sem markup: as conversas sao pagas direto a Meta.\n'
             '- Trial de 7 dias, sem cartao.\n\n'
             '## Artigos\n\n%s\n\n'
             '## Recursos oficiais\n\n'
             '- [Documentacao](https://app.datafyapi.com.br/docs)\n'
             '- [Site](https://datafyapi.com.br/)\n'
             '- [Canal DATA7](https://www.youtube.com/@data7apps)\n'
             % (MARCA, AUTOR, CARGO,
                '\n'.join('- [%s](%s/%s): %s' % (m['title'], DOMINIO, m['slug'], m['description'])
                          for m in paginas)))

    print('\n%d pagina(s) + home + autor + sitemap + rss + robots + llms.txt' % len(paginas))
    print('Pronto em site/')


def pagina_simples(moldura, css, titulo, descricao, url, miolo, jsonld=None):
    """Home e pagina de autor: mesma moldura, sem coluna lateral nem faixa de topo."""
    if jsonld is None:
        jsonld = {'@context': 'https://schema.org', '@type': 'CollectionPage',
                  'name': titulo, 'description': descricao, 'url': url,
                  'inLanguage': 'pt-BR',
                  'publisher': {'@type': 'Organization', 'name': MARCA,
                                'url': 'https://datafyapi.com.br/'}}
    saida = moldura
    for chave, valor in {
        'TITULO': _html.escape(titulo), 'TITULO_SEO': _html.escape(titulo),
        'DESCRICAO': _html.escape(descricao), 'URL': url, 'CSS': css,
        'JSONLD': json.dumps(jsonld, ensure_ascii=False, indent=2),
        'DATA_ISO': datetime.date.today().isoformat(),
        'DATA_LONGA': por_extenso(datetime.date.today()),
        'EYEBROW': '', 'AUTOR': AUTOR, 'CARGO': CARGO, 'HERO': '', 'SUMARIO': '',
        'NAV': '\n'.join('      <a href="%s">%s</a>' % (u, n) for _, n, u in TEMAS),
        'RODAPE_TEMAS': '\n'.join('        <li><a href="%s">%s</a></li>' % (u, n)
                                  for _, n, u in TEMAS),
    }.items():
        saida = saida.replace('{{%s}}' % chave, str(valor))
    # tira faixa de topo e coluna lateral, deixa so o miolo
    saida = re.sub(r'<div class="hero-band">.*?</div>\s*</div>\s*</div>', '', saida, flags=re.S)
    saida = re.sub(r'<aside class="rail".*?</aside>', '', saida, flags=re.S)
    saida = saida.replace('class="shell"', 'class="shell shell-solo"')
    saida = saida.replace('<meta property="og:type" content="article">',
                          '<meta property="og:type" content="website">')
    saida = re.sub(r'<article>.*?</article>', '<article>%s</article>' % miolo, saida, flags=re.S)
    return saida


if __name__ == '__main__':
    main()

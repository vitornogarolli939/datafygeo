"""Servidor estatico do site/ para conferencia visual.

Nao usa `python3 -m http.server` porque o modulo chama os.getcwd() no argparse,
e isso falha no sandbox. Aqui o diretorio e passado direto ao handler.
"""
import functools
import os
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'site')
PORTA = int(sys.argv[1]) if len(sys.argv) > 1 else 8788


class Handler(SimpleHTTPRequestHandler):
    """Resolve /slug para /slug/index.html, como o Cloudflare Pages faz."""

    def send_head(self):
        caminho = self.translate_path(self.path)
        if os.path.isdir(caminho) and not self.path.endswith('/'):
            self.path += '/'
        return SimpleHTTPRequestHandler.send_head(self)

    def log_message(self, formato, *args):
        sys.stderr.write('%s\n' % (formato % args))


if __name__ == '__main__':
    handler = functools.partial(Handler, directory=os.path.abspath(RAIZ))
    print('servindo %s em http://localhost:%d' % (os.path.abspath(RAIZ), PORTA))
    sys.stdout.flush()
    ThreadingHTTPServer(('127.0.0.1', PORTA), handler).serve_forever()

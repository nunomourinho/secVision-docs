"""Exporta o manual para dentro do SecVision, para a ajuda de cada ecrã funcionar sem Internet.

    python -X utf8 scripts/exportar_ajuda.py --destino ../secVision/frontend/public/ajuda

O SecVision corre em redes fechadas: a ajuda não pode depender do Read the Docs. Este script
compila o manual com o builder JSON do Sphinx (o corpo de cada página em HTML, já com as tabelas, as
listas numeradas e as figuras) e escreve, no destino:

    indice.json                 página → título, vídeo do YouTube, endereço no Read the Docs
    paginas/<pagina>.json       {titulo, html, video, url}
    img/<caminho>.webp          as imagens usadas, recomprimidas

O HTML sai pronto para o modal de ajuda:
- sem o leitor do vídeo (o modal desenha-o à parte, a partir de `video`);
- sem as âncoras «¶» do Sphinx;
- imagens a apontar para `/ajuda/img/…`;
- ligações para outras páginas do manual com `data-ajuda="<pagina>#<âncora>"` (o modal abre-as lá
  dentro) e `href` no Read the Docs, para quem as abrir num separador;
- ligações externas com `target="_blank"`.

O SecVision sanitiza este HTML outra vez (DOMPurify) antes de o mostrar: isto não é a fronteira de
segurança, é só a forma.
"""
import argparse
import json
import pickle
import posixpath
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from bs4 import BeautifulSoup
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
DOCS = RAIZ / 'docs'
URL = 'https://secvision-user-manual.readthedocs.io/pt/latest'
LARGURA = 1200
QUALIDADE = 80
# só o manual do utilizador da plataforma; os índices e a página de entrada também, para as ligações
SECCOES = ('installation/', 'platform/', 'wazuh/', 'journey/', 'project/', 'fundamentals/', 'law/')


def compilar(saida):
    subprocess.run([sys.executable, '-m', 'sphinx', '-q', '-W', '-b', 'json', str(DOCS), str(saida)],
                   check=True)


def mapa_imagens(saida):
    """Nome único em _images/ → caminho original em docs/ (o Sphinx renomeia os repetidos)."""
    env = pickle.loads((saida / 'environment.pickle').read_bytes())
    return {unico: original for original, (_docs, unico) in env.images.items()}


def videos_por_pagina():
    """Página → ID do YouTube, pela diretiva ``{video}`` de cada página (uma página pode mostrar o
    vídeo de outra, como a do IOC mostra o 334)."""
    import re
    ids = json.loads((DOCS / '_data' / 'videos.json').read_text(encoding='utf-8'))
    res = {}
    for md in DOCS.rglob('*.md'):
        if '_build' in md.parts:
            continue
        m = re.search(r'^```\{video\}\s+(\S+)', md.read_text(encoding='utf-8'), re.M)
        if m:
            res[md.relative_to(DOCS).with_suffix('').as_posix()] = (ids.get(m.group(1)) or {}).get('youtube')
    return res


def converter_imagem(origem, destino):
    destino.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(origem) as im:
        im = im.convert('RGB')
        if im.width > LARGURA:
            im = im.resize((LARGURA, round(im.height * LARGURA / im.width)), Image.LANCZOS)
        im.save(destino, 'WEBP', quality=QUALIDADE, method=6)


def tratar(pagina, html, imagens, usadas, ligacoes):
    sopa = BeautifulSoup(html, 'html.parser')
    for v in sopa.select('div.sv-video'):
        v.decompose()
    for a in sopa.select('a.headerlink'):
        a.decompose()
    base = posixpath.dirname(pagina)
    for img in sopa.find_all('img'):
        unico = posixpath.basename(img.get('src', ''))
        original = imagens.get(unico)
        if not original:
            raise SystemExit(f'{pagina}: imagem sem origem conhecida: {img.get("src")}')
        alvo = posixpath.splitext(original.removeprefix('_static/'))[0] + '.webp'
        usadas[alvo] = original
        img['src'] = f'/ajuda/img/{alvo}'
        img['loading'] = 'lazy'
    for a in sopa.find_all('a', href=True):
        href = a['href']
        if href.startswith(('http://', 'https://', 'mailto:')):
            a['target'] = '_blank'
            a['rel'] = 'noopener noreferrer'
            continue
        if href.startswith('#'):
            a['data-ajuda'] = f'{pagina}{href}'
            ligacoes.add((pagina, pagina))
            a['href'] = f'{URL}/{pagina}.html{href}'
            continue
        caminho, _, ancora = href.partition('#')
        # o builder JSON escreve as ligações à maneira do dirhtml: cada página é uma pasta
        # («../../law/x/», relativo a «<pagina>/»), e a raiz é «../»
        if caminho.endswith('.html'):
            destino = posixpath.normpath(posixpath.join(base, caminho))[:-len('.html')]
        elif caminho.endswith('/') or caminho in ('', '.', '..'):
            # um índice («fundamentals/index») é a própria pasta («fundamentals/»)
            pasta = posixpath.dirname(pagina) if posixpath.basename(pagina) == 'index' else pagina
            destino = posixpath.normpath(posixpath.join(pasta or '.', caminho)).strip('/')
            destino = destino if destino not in ('', '.') else 'index'
            if destino.startswith('..'):
                raise SystemExit(f'{pagina}: ligação para fora do manual: {href}')
            # «platform/risk/» é o índice dessa secção
            if not (DOCS / f'{destino}.md').exists() and (DOCS / destino / 'index.md').exists():
                destino = f'{destino}/index'
        else:
            continue
        a['data-ajuda'] = destino + (f'#{ancora}' if ancora else '')
        ligacoes.add((pagina, destino))
        a['href'] = f'{URL}/{destino}.html' + (f'#{ancora}' if ancora else '')
        a['target'] = '_blank'
        a['rel'] = 'noopener noreferrer'
    return str(sopa).strip()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--destino', required=True, type=Path,
                    help='pasta public/ajuda do SecVision (é apagada e escrita de novo)')
    args = ap.parse_args()
    destino = args.destino.resolve()
    if destino.name != 'ajuda':
        raise SystemExit('o destino tem de ser a pasta «ajuda» (é apagada e escrita de novo)')

    with tempfile.TemporaryDirectory() as tmp:
        saida = Path(tmp) / 'json'
        compilar(saida)
        imagens = mapa_imagens(saida)
        videos = videos_por_pagina()

        # o conteúdo, não a pasta (no Windows, uma pasta aberta noutro processo não se apaga)
        destino.mkdir(parents=True, exist_ok=True)
        for p in destino.iterdir():
            shutil.rmtree(p) if p.is_dir() else p.unlink()
        (destino / 'paginas').mkdir()
        indice, usadas, ligacoes = {}, {}, set()
        for f in sorted(saida.rglob('*.fjson')):
            pagina = f.relative_to(saida).with_suffix('').as_posix()
            if pagina != 'index' and not pagina.startswith(SECCOES):
                continue
            dados = json.loads(f.read_text(encoding='utf-8'))
            titulo = BeautifulSoup(dados['title'], 'html.parser').get_text()
            registo = {'titulo': titulo, 'video': videos.get(pagina), 'url': f'{URL}/{pagina}.html'}
            html = tratar(pagina, dados['body'], imagens, usadas, ligacoes)
            alvo = destino / 'paginas' / f'{pagina}.json'
            alvo.parent.mkdir(parents=True, exist_ok=True)
            alvo.write_text(json.dumps({**registo, 'html': html}, ensure_ascii=False), encoding='utf-8')
            indice[pagina] = registo

        # uma ligação para uma página que não foi exportada abriria um modal vazio
        partidas = sorted(f'{de} → {para}' for de, para in ligacoes if para not in indice)
        if partidas:
            raise SystemExit('ligações para páginas que não foram exportadas:\n  ' + '\n  '.join(partidas))

        for alvo, original in sorted(usadas.items()):
            converter_imagem(DOCS / original, destino / 'img' / alvo)

    (destino / 'indice.json').write_text(
        json.dumps({'manual': URL, 'paginas': indice}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    tamanho = sum(p.stat().st_size for p in destino.rglob('*') if p.is_file())
    print(f'{len(indice)} páginas, {len(usadas)} imagens, {tamanho / 1e6:.1f} MB em {destino}')


if __name__ == '__main__':
    main()

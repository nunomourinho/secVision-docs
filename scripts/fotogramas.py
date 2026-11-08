#!/usr/bin/env python3
"""Fotogramas das páginas do manual, tirados do vídeo da formação.

Para cada cena **filmada** do guião (as que têm ``de``/``ate``) e cada diapositivo que é imagem
(um diagrama, como ``camadas``; os de texto, tabela, abertura e fecho não, porque a página já os
escreve), tira um
fotograma do ``<id>.mp4`` a 65 % da cena — já passou o corte e o ecrã está no estado que a
narração descreve — e escreve-o em ``docs/_static/img/<id>/NN.jpg`` (1280×720, como os outros).
Atualiza a entrada do vídeo em ``manifesto-imagens.json`` (ficheiro, instante, rótulo da cena).

Os tempos das cenas vêm dos capítulos de ``<id>.json`` (o ``montar.py`` escreve um por cena que
tenha ``capitulo``); a cena que não tem capítulo acaba onde começa a seguinte.

Uso:
    python -X utf8 scripts/fotogramas.py --videos <pasta dos mp4> --guioes ../secVision/videos/guioes ID [ID ...]
"""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent.parent
# diapositivos que a página escreve em texto — não vão como imagem
SO_TEXTO = {'abertura', 'fecho', 'conteudo', 'tabela'}


def vai_como_imagem(cena: dict) -> bool:
    return 'de' in cena or ('diapositivo' in cena and cena['diapositivo'] not in SO_TEXTO)


def tempos(guiao: dict, info: dict) -> list[tuple[dict, float, float]]:
    """(cena, início, fim) de cada cena, pela ordem do guião."""
    cenas = [c for c in guiao['cenas'] if not c.get('cortar')]
    caps = iter(info['capitulos'])
    inicios: list[float | None] = []
    for c in cenas:
        inicios.append(next(caps)['t'] if c.get('capitulo') else None)
    out = []
    for i, c in enumerate(cenas):
        a = inicios[i]
        if a is None:
            continue
        b = next((x for x in inicios[i + 1:] if x is not None), info['duracao'])
        out.append((c, a, b))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--videos', type=Path, required=True)
    ap.add_argument('--guioes', type=Path, required=True)
    ap.add_argument('--fracao', type=float, default=0.65)
    ap.add_argument('ids', nargs='+')
    args = ap.parse_args()
    manifesto_p = RAIZ / 'manifesto-imagens.json'
    manifesto = json.loads(manifesto_p.read_text(encoding='utf-8'))
    for vid in args.ids:
        guiao = yaml.safe_load((args.guioes / f'{vid}.yaml').read_text(encoding='utf-8'))
        info = json.loads((args.videos / f'{vid}.json').read_text(encoding='utf-8'))
        destino = RAIZ / 'docs' / '_static' / 'img' / vid
        destino.mkdir(parents=True, exist_ok=True)
        for velho in destino.glob('*.jpg'):
            velho.unlink()
        entradas = []
        filmadas = [(c, a, b) for c, a, b in tempos(guiao, info) if vai_como_imagem(c)]
        for n, (c, a, b) in enumerate(filmadas, 1):
            t = round(a + args.fracao * (b - a), 2)
            nome = f'{n:02}.jpg'
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(t), '-i', str(args.videos / f'{vid}.mp4'),
                            '-frames:v', '1', '-vf', 'scale=1280:720', '-q:v', '4', str(destino / nome)],
                           check=True)
            rotulo = c.get('rotulo') or c.get('titulo', '')
            entradas.append({'ficheiro': nome, 't': t, 'rotulo': rotulo})
            print(f'{vid}/{nome}  {t:7.2f} s  {rotulo}', flush=True)
        manifesto[vid] = entradas
    manifesto_p.write_text(json.dumps(manifesto, ensure_ascii=False, indent=1) + '\n', encoding='utf-8', newline='\n')


if __name__ == '__main__':
    main()

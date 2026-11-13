#!/usr/bin/env python3
"""Capturas de ecrã anotadas para o manual, a partir dos roteiros das gravações da formação.

Percorre os passos de ``secVision/videos/roteiros/ecras/<nome>.yaml`` (os mesmos que gravaram
os vídeos) no AMBIENTE DE TESTES, mas em vez de filmar tira capturas fixas:

- ``menu.jpg`` — o primeiro ecrã, com o caminho no menu lateral numerado (1 função, 2 módulo,
  3 item…);
- ``<marca>-<n>.jpg`` — uma captura por fase: os elementos que o vídeo destaca e o elemento em
  que se vai clicar, ou o campo em que se escreve, cada um com o seu número.

Ao lado das imagens fica ``capturas.json``: para cada imagem, a lista numerada (o que é cada
número, e se é para ver, clicar ou escrever). O ``scripts/gerar_paginas.py`` usa-a para escrever
o passo a passo por baixo de cada imagem.

Uso (com o Playwright e o pyotp instalados):
    python -X utf8 scripts/capturar_ecras.py --secvision ../secVision [nome ...]
"""
from __future__ import annotations

import argparse
import io
import json
import sys
import time
from pathlib import Path

import yaml
from PIL import Image
from playwright.sync_api import sync_playwright

VIEWPORT = {'width': 1440, 'height': 900}
AZUL = '#2563EB'     # accent do design system: ver
LARANJA = '#EA580C'  # ação: clicar, escrever, escolher

ANOTAR_JS = """(itens) => {
  document.querySelectorAll('[data-anotacao]').forEach(e => e.remove());
  for (const it of itens) {
    const c = it.caixa;
    const m = document.createElement('div'); m.setAttribute('data-anotacao', '');
    Object.assign(m.style, {position: 'absolute', left: (c.x - 5) + 'px', top: (c.y - 5) + 'px',
      width: (c.width + 10) + 'px', height: (c.height + 10) + 'px', border: '3px solid ' + it.cor,
      borderRadius: '8px', zIndex: 2147483646, pointerEvents: 'none', boxSizing: 'border-box'});
    document.body.appendChild(m);
    const n = document.createElement('div'); n.setAttribute('data-anotacao', ''); n.textContent = it.n;
    const lx = c.x - 18 < 2 ? c.x + c.width - 8 : c.x - 18;
    Object.assign(n.style, {position: 'absolute', left: lx + 'px', top: Math.max(2, c.y - 18) + 'px',
      width: '28px', height: '28px', borderRadius: '50%', background: it.cor, color: '#fff',
      font: '700 15px/28px Inter, Segoe UI, sans-serif', textAlign: 'center', zIndex: 2147483647,
      pointerEvents: 'none', boxShadow: '0 0 0 2px #fff, 0 2px 6px rgba(0,0,0,.35)'});
    document.body.appendChild(n);
  }
}"""

# caminho no menu lateral até ao item ativo: [categoria, módulo, (subgrupo), item]
MENU_JS = """() => {
  const item = document.querySelector('aside nav a[aria-current="page"]');
  if (!item) return null;
  const nivel = [];
  let e = item;
  while (e && e.tagName !== 'NAV') {
    const irmao = e.previousElementSibling;
    if (irmao && irmao.tagName === 'BUTTON') {
      nivel.unshift(irmao);
    }
    e = e.parentElement;
  }
  const todos = [...nivel, item];
  return todos.map(x => { const r = x.getBoundingClientRect();
    return {texto: x.innerText.trim().split('\\n')[0],
            caixa: {x: r.x + scrollX, y: r.y + scrollY, width: r.width, height: r.height}}; });
}"""


# campos de um formulário aberto (janela modal): um número por rótulo visível
CAMPOS_JS = """() => {
  const cands = [...document.querySelectorAll('[role="dialog"], [aria-modal="true"], .fixed, .absolute')].filter(e => {
    const r = e.getBoundingClientRect();
    return r.width > 320 && r.height > 200 && e.closest('aside') === null && e.querySelector('input, select, textarea');
  });
  const d = cands[cands.length - 1];
  if (!d) return [];
  const out = [], vistos = new Set();
  for (const l of d.querySelectorAll('label')) {
    const r = l.getBoundingClientRect();
    const t = (l.innerText || '').trim().split(String.fromCharCode(10))[0].trim();
    if (!t || t.length > 70 || vistos.has(t) || r.width < 4 || r.height < 4 || r.top < 0 || r.bottom > innerHeight) continue;
    vistos.add(t);
    out.push({texto: t, caixa: {x: r.x + scrollX, y: r.y + scrollY, width: r.width, height: r.height}});
    if (out.length >= 15) break;
  }
  return out;
}"""


class Parar(Exception):
    """Fim deliberado: o passo seguinte mexeria no Wazuh de teste (aplicar uma regra)."""


# cliques que alteram o gestor Wazuh: anotam-se e a captura pára ali (salvo --aplicar)
ALTERAM_WAZUH = ('Aplicar ao Wazuh',)
APLICAR = False


class Captura:
    def __init__(self, page, base, destino: Path, nome: str):
        self.page, self.base, self.destino, self.nome = page, base, destino, nome
        self.pendentes: list[dict] = []
        self.marca = 'inicio'
        self.n_marca = 0
        self.indice: list[dict] = []
        self.menu_feito = False
        # depois de um clique, de uma tecla ou de rolar, o ecrã mudou: mostra-se, mesmo sem números
        self.por_mostrar = False
        destino.mkdir(parents=True, exist_ok=True)

    # ── anotações ─────────────────────────────────────────────────────────
    def caixa(self, seletor):
        alvo = self.page.locator(seletor).first
        alvo.scroll_into_view_if_needed(timeout=5000)
        c = alvo.bounding_box()
        if not c:
            return None
        sx, sy = self.page.evaluate('[scrollX, scrollY]')
        return {'x': c['x'] + sx, 'y': c['y'] + sy, 'width': c['width'], 'height': c['height']}

    def texto_de(self, seletor):
        try:
            loc = self.page.locator(seletor).first
            t = (loc.get_attribute('aria-label', timeout=1000) or loc.inner_text(timeout=1000) or '').strip()
            t = t.split('\n')[0].strip()
            if not t:
                t = (loc.get_attribute('placeholder', timeout=500) or '').strip()
            return t[:60]
        except Exception:  # noqa: BLE001
            return ''

    def anotar(self, seletor, tipo, rotulo=None, valor=None):
        try:
            c = self.caixa(seletor)
        except Exception as e:  # noqa: BLE001
            print(f'  ! sem caixa ({seletor}): {type(e).__name__}', flush=True)
            return
        if c:
            self.pendentes.append({'tipo': tipo, 'caixa': c, 'rotulo': rotulo or self.texto_de(seletor),
                                   'valor': valor})

    def foto(self, forcar=False):
        if not self.pendentes and not (forcar or self.por_mostrar):
            return
        if not self.pendentes and self.por_mostrar:
            for c in self.page.evaluate(CAMPOS_JS):
                self.pendentes.append({'tipo': 'ver', 'caixa': c['caixa'], 'rotulo': c['texto'], 'valor': None})
        self.por_mostrar = False
        self.n_marca += 1
        nome = f'{self.marca}-{self.n_marca}.jpg'
        itens = [{'n': i + 1, 'cor': AZUL if p['tipo'] == 'ver' else LARANJA, 'caixa': p['caixa']}
                 for i, p in enumerate(self.pendentes)]
        self._gravar(nome, itens)
        self.indice.append({'imagem': nome, 'marca': self.marca,
                            'itens': [{'n': i + 1, 'tipo': p['tipo'], 'rotulo': p['rotulo'],
                                       'valor': p['valor']} for i, p in enumerate(self.pendentes)]})
        self.pendentes = []

    def _gravar(self, nome, itens):
        self.page.evaluate(ANOTAR_JS, itens)
        time.sleep(0.15)
        if itens:
            y0 = min(i['caixa']['y'] for i in itens)
            y1 = max(i['caixa']['y'] + i['caixa']['height'] for i in itens)
        altura_pag = self.page.evaluate('document.documentElement.scrollHeight')
        if not itens:
            h = VIEWPORT['height']
            topo = max(0, min(self.page.evaluate('scrollY'), altura_pag - h))
        else:
            h = max(VIEWPORT['height'], min(y1 - y0 + 160, 2400))
            topo = max(0, min(y0 - 80, altura_pag - h)) if y1 - y0 + 160 > VIEWPORT['height'] else \
                max(0, min((y0 + y1) / 2 - h / 2, altura_pag - h))
        if altura_pag <= VIEWPORT['height'] + 1:
            # A página não rola na janela: rola por dentro (a coluna do editor do SGSI). Uma captura
            # `full_page` redimensiona a janela, e isso repõe o scroll dessas colunas — as molduras
            # ficavam onde o elemento estava antes. Fotografa-se a janela tal como está.
            png = self.page.screenshot(full_page=False)
        else:
            png = self.page.screenshot(full_page=True, clip={'x': 0, 'y': topo, 'width': VIEWPORT['width'],
                                                             'height': min(h, altura_pag)})
        self.page.evaluate("document.querySelectorAll('[data-anotacao]').forEach(e => e.remove())")
        Image.open(io.BytesIO(png)).convert('RGB').save(self.destino / nome, quality=86, optimize=True)
        print(f'  {nome}: {len(itens)} anotações', flush=True)

    def menu(self):
        if self.menu_feito:
            return
        caminho = self.page.evaluate(MENU_JS)
        if not caminho:
            return
        self.menu_feito = True
        self.page.evaluate('window.scrollTo(0, 0)')
        itens = [{'n': i + 1, 'cor': LARANJA, 'caixa': c['caixa']} for i, c in enumerate(caminho)]
        self._gravar('menu.jpg', itens)
        self.indice.insert(0, {'imagem': 'menu.jpg', 'marca': 'menu',
                               'itens': [{'n': i + 1, 'tipo': 'clicar', 'rotulo': c['texto']}
                                         for i, c in enumerate(caminho)]})

    def _visivel(self, sel: str) -> bool:
        try:
            self.page.locator(sel).first.wait_for(state='visible', timeout=3000)
            return True
        except Exception:  # noqa: BLE001
            return False

    # ── passos do roteiro ─────────────────────────────────────────────────
    def executar(self, p: dict):
        pg = self.page
        if 'abrir' in p:
            self.foto()
            pg.goto(self.base + p['abrir'], wait_until='networkidle')
            pg.wait_for_selector(p.get('esperar', 'main'), timeout=30000)
            time.sleep(1)
            self.por_mostrar = self.menu_feito
            self.menu()
        elif 'abrir_url' in p:
            self.foto()
            pg.goto(p['abrir_url'], wait_until='domcontentloaded')
            pg.wait_for_selector(p.get('esperar', 'body'), timeout=90000)
            time.sleep(3)
            self.por_mostrar = True
        elif 'marca' in p:
            self.foto()
            self.marca, self.n_marca = p['marca'], 0
        elif 'destacar' in p:
            self.anotar(p['destacar'], 'ver', p.get('rotulo'))
        elif 'limpar' in p:
            pass
        elif 'clicar' in p and p.get('opcional') and not self._visivel(p['clicar']):
            print(f"  ↷ clique opcional sem alvo ({p['clicar']})", flush=True)
        elif 'clicar' in p:
            self.anotar(p['clicar'], 'clicar')
            self.foto()
            if not APLICAR and any(t in p['clicar'] for t in ALTERAM_WAZUH):
                raise Parar()
            pg.locator(p['clicar']).first.click(timeout=15000)
            time.sleep(1.2)
            self.por_mostrar = True
        elif 'escrever' in p or 'colar' in p:
            sel = p.get('escrever') or p.get('colar')
            texto = p.get('texto')
            if texto is None and 'ficheiro' in p:
                f = next((d / p['ficheiro'] for d in self.gravacoes if (d / p['ficheiro']).exists()),
                         self.gravacoes[0] / p['ficheiro'])
                texto = f.read_text(encoding='utf-8')
            loc = pg.locator(sel).first
            loc.click(timeout=15000)
            loc.fill(str(texto))
            # uma palavra-passe nunca vai para o texto do manual
            secreto = (loc.get_attribute('type') or '') == 'password' or 'password' in sel.lower()
            curto = str(texto) if len(str(texto)) < 70 and not secreto else None
            self.anotar(sel, 'escrever', valor=curto)
            if p.get('enter'):
                self.foto()
                pg.keyboard.press('Enter')
                time.sleep(1.2)
                self.por_mostrar = True
        elif 'selecionar' in p:
            # `valor` é o value do <option>; `opcao` o texto que se vê (os roteiros da rede VPN)
            visto = str(p['opcao']) if 'opcao' in p else str(p['valor'])
            if 'opcao' in p:
                pg.locator(p['selecionar']).first.select_option(label=visto)
            else:
                pg.locator(p['selecionar']).first.select_option(visto)
            self.anotar(p['selecionar'], 'escolher', valor=visto)
        elif 'rolar' in p:
            self.foto()
            try:
                if p['rolar'] == 'topo':
                    pg.evaluate('window.scrollTo(0, 0)')
                else:
                    pg.locator(p['rolar']).first.scroll_into_view_if_needed(timeout=5000)
            except Exception:  # noqa: BLE001
                pass
            time.sleep(0.5)
            self.por_mostrar = True
        elif 'esperar' in p:
            pg.wait_for_selector(p['esperar'], timeout=float(p.get('segundos', 30)) * 1000)
        elif 'ia_externa' in p:
            # O assistente de IA externo dos vídeos (secVision/videos/roteiros/ia_externa.py): no
            # manual não se desenha a janela simulada, só se leva para a área de transferência a
            # resposta real que o modelo deu ao pedido pseudonimizado — o `Control+V` seguinte
            # cola-a, e o que se captura a seguir é a plataforma a repor as etiquetas.
            rel = f"ia/{p['ia_externa']}.resposta.txt"
            f = next((d / rel for d in self.gravacoes if (d / rel).exists()), None)
            if f is None:
                raise FileNotFoundError(f'{rel}: falta a resposta da IA (ver roteiros/ia_externa.py)')
            self.area_transferencia = f.read_text(encoding='utf-8')
        elif 'copiar' in p:
            # copiar o pedido: no manual basta mostrar o botão; a resposta já está preparada
            self.anotar(p['copiar'], 'clicar')
            self.foto()
            pg.locator(p['copiar']).first.click(timeout=15000)
            time.sleep(0.8)
            self.por_mostrar = True
        elif 'carregar' in p:
            pasta = self.gravacoes[0]
            nomes = p.get('ficheiros') or [p['ficheiro']]
            pg.locator(p['carregar']).first.set_input_files([str(pasta / n) for n in nomes])
            time.sleep(1.2)
            self.por_mostrar = True
        elif 'tecla' in p and p['tecla'] in ('Control+V', 'Meta+V') and getattr(self, 'area_transferencia', None):
            pg.keyboard.insert_text(self.area_transferencia)
            time.sleep(1.2)
            self.por_mostrar = True
        elif 'tecla' in p:
            self.foto()
            pg.keyboard.press(p['tecla'])
            time.sleep(0.8)
            self.por_mostrar = p['tecla'] != 'Escape'
        if p.get('pausa'):
            time.sleep(min(float(p['pausa']), 2.0))


def entrar(page, base, utilizador, totp):
    page.goto(base + '/login', wait_until='networkidle')
    page.fill('input[autocomplete="username"]', utilizador)
    page.fill('input[type="password"]', 'Teste123!')
    page.click('button[type="submit"]')
    page.wait_for_selector('input[placeholder="000000"]', timeout=30000)
    if totp.interval - time.time() % totp.interval < 6:
        time.sleep(totp.interval - time.time() % totp.interval + 0.5)
    page.fill('input[placeholder="000000"]', totp.now())
    page.click('button[type="submit"]')
    page.wait_for_selector('header', timeout=30000)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--secvision', type=Path, required=True)
    ap.add_argument('--base', default='http://localhost:8090')
    ap.add_argument('--saida', type=Path, default=Path(__file__).resolve().parent.parent / 'docs' / '_static' / 'capturas')
    ap.add_argument('--gravacoes', type=Path, action='append', default=[],
                    help='outra pasta com os ficheiros colados (p. ex. a de transferência)')
    ap.add_argument('--aplicar', action='store_true', help='executar também os cliques que alteram o Wazuh')
    ap.add_argument('nomes', nargs='*')
    args = ap.parse_args()
    global APLICAR
    APLICAR = args.aplicar

    import re
    import pyotp
    fonte = (args.secvision / 'backend' / 'scripts' / 'gerar-dados-teste.mjs').read_text(encoding='utf-8')
    totp = pyotp.TOTP(re.search(r"SEGREDO_TOTP = '([A-Z2-7]+)'", fonte).group(1))
    ecras = args.secvision / 'videos' / 'roteiros' / 'ecras'
    extra = Path(__file__).resolve().parent / 'ecras-extra'
    fontes = {p.stem: p for p in ecras.glob('*.yaml')} | {p.stem: p for p in extra.glob('*.yaml')}
    nomes = args.nomes or sorted(fontes)
    falhas = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        for nome in nomes:
            print(nome, flush=True)
            dados = yaml.safe_load(fontes[nome].read_text(encoding='utf-8'))
            ctx = browser.new_context(viewport=VIEWPORT, device_scale_factor=1, locale='pt-PT',
                                      ignore_https_errors=True)
            page = ctx.new_page()
            c = Captura(page, args.base, args.saida / nome, nome)
            c.gravacoes = [args.secvision / 'videos' / 'gravacoes'] + args.gravacoes
            try:
                entrar(page, args.base, dados.get('utilizador', 'ines.santos'), totp)
                for passo in dados['passos']:
                    c.executar(passo)
                c.foto(forcar=len(c.indice) <= 1)
            except Parar:
                print('  ↷ parado antes de alterar o Wazuh de teste (use --aplicar para continuar)', flush=True)
            except Exception as e:  # noqa: BLE001
                print(f'  ✗ {type(e).__name__}: {str(e)[:200]}', flush=True)
                falhas.append(nome)
                c.pendentes = []
            (args.saida / nome / 'capturas.json').write_text(
                json.dumps(c.indice, ensure_ascii=False, indent=1) + '\n', encoding='utf-8', newline='\n')
            ctx.close()
        browser.close()
    if falhas:
        print('FALHARAM:', ' '.join(falhas))
        sys.exit(1)


if __name__ == '__main__':
    main()

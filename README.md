# SecVision — manual do utilizador

Manual público do **SecVision**, plataforma de gestão da cibersegurança e da conformidade
(DL 125/2025, Regulamento 756/2026, ISO/IEC 27001), publicado no Read the Docs. Acompanha a
**formação SecVision**: cada página corresponde a um vídeo da série e descreve o mesmo conteúdo
passo a passo, com o caminho dos menus e capturas de ecrã anotadas.

| Língua | Fonte | Configuração RTD | Endereço |
|---|---|---|---|
| Português (pt-PT) | `docs/` | `.readthedocs.yaml` | <https://secvision-user-manual.readthedocs.io/pt/latest/> |

- Fonte: Markdown (MyST), compilado com Sphinx e o tema `sphinx_rtd_theme`, com as cores e o
  logótipo do design system do SecVision (v1.1).
- **Os nomes das páginas estão em inglês** (`platform/risk/risk-register`…), como no manual do
  ForensicVM, para que uma tradução futura (`docs-en/`, e as outras línguas) use os mesmos caminhos e o
  seletor de língua do Read the Docs abra a página equivalente.
- Vídeos: incorporados do YouTube. Os IDs ficam em `docs/_data/videos.json` (escrito por
  `scripts/youtube_upload.py`). Enquanto um vídeo não tiver ID, a página mostra a nota «Vídeo em breve».
- `docs/_data/serie.json`: a série (id do vídeo → página, título, resumo, capítulos).

## Estrutura

Segue a formação, módulo a módulo:

| Pasta | Conteúdo | Vídeos |
|---|---|---|
| `installation/` | Instalação | 01–07 |
| `fundamentals/` | Módulo A — Fundamentos | 101–106 |
| `law/` | Módulo B — A lei e o CNCS | 201–217 |
| `platform/` | Módulo C — A plataforma, pela ordem dos menus (8 secções) | 301–346 |
| `journey/` | Módulo D — O percurso até à certificação | 401–407 |
| `wazuh/` | Módulo E — Wazuh | 501–508 |
| `project/` | O que a plataforma não faz | — |

## As imagens

Há dois tipos:

- **`docs/_static/capturas/<ecrã>/`: capturas anotadas** dos ecrãs da plataforma (módulos C e E).
  São tiradas por `scripts/capturar_ecras.py`, que percorre no **ambiente de testes** os mesmos passos
  das gravações da formação (`secVision/videos/roteiros/ecras/*.yaml`, mais `scripts/ecras-extra/`) e
  tira uma captura por fase:
  - `menu.jpg`: o caminho no menu lateral, numerado (1 função › 2 módulo › 3 item);
  - `<marca>-<n>.jpg`: os elementos de cada fase numerados. **Azul** quer dizer ver ou preencher;
    **laranja** quer dizer clicar ou escrever, pela ordem em que se faz.

  Ao lado de cada pasta fica `capturas.json`, com o significado de cada número. As páginas trazem-no
  como lista numerada por baixo de cada imagem.
- **`docs/_static/img/<id-do-vídeo>/`: fotogramas dos vídeos**, para os ecrãs que não são da
  plataforma (instalação no terminal e na consola, diapositivos de conceitos) e para o que só o vídeo
  mostra, como a janela do assistente de IA. Saem do vídeo montado com `scripts/fotogramas.py`: um
  por cena filmada, mais os diapositivos que são diagrama. Depois de voltar a montar um vídeo, refaça
  os dele e confira os números das figuras na página, que mudam quando o guião ganha cenas:

  ```bash
  python -X utf8 scripts/fotogramas.py --videos ~/Documents/SecVision-videos/pt-PT       --guioes ../secVision/videos/guioes 506-falsos-positivos
  ```

Para refazer as capturas (com o ambiente de testes de pé em `:8090` e **nenhuma suite de testes a
correr**):

```bash
pip install playwright pyotp pillow pyyaml && playwright install chromium
python -X utf8 scripts/capturar_ecras.py --secvision ../secVision            # todos
python -X utf8 scripts/capturar_ecras.py --secvision ../secVision registo-risco
```

## A ajuda dentro do SecVision

O botão «?» de cada ecrã do SecVision abre a página deste manual que explica esse ecrã, com o vídeo,
o texto e as capturas. O conteúdo vai **empacotado** na aplicação, porque a plataforma corre em redes
fechadas: só o vídeo precisa de Internet. Depois de mudar o manual, volte a gerá-lo:

```bash
python -X utf8 scripts/exportar_ajuda.py --destino ../secVision/frontend/public/ajuda
```

O script compila o manual com o builder JSON do Sphinx e escreve `indice.json`, uma página por
ficheiro e as imagens em WebP. Recusa terminar se uma ligação entre páginas apontar para uma página
que não foi exportada. A correspondência ecrã → página está em
`secVision/frontend/src/config/ajuda-rotas.js`, e `secVision/testes/test-ajuda-rotas.mjs` falha quando um
item do menu não tem página, ou quando a página ou a âncora deixaram de existir. **Um ecrã novo no menu
precisa de uma página aqui.**

## Compilar localmente

```bash
python3 -m venv .venv
.venv/bin/pip install -r docs/requirements.txt
.venv/bin/sphinx-build -W -b html docs docs/_build/html
xdg-open docs/_build/html/index.html
```

O build usa `-W` (os avisos contam como erros), tal como no Read the Docs (`fail_on_warning`).

## Escrever uma página

````markdown
# Título

Para que serve.

```{video} 325-registo-de-risco
```

## Onde fica no menu

**Menu:** Identificar › Risco › Registo de risco

```{figure} /_static/capturas/registo-risco/menu.jpg
:alt: Menu lateral: Identificar › Risco › Registo de risco

O caminho no menu lateral.
```

1. No menu lateral, abra **Identificar**.
2. Dentro dele, abra **Risco**.
3. Clique em **Registo de risco**.
````

## Publicar no Read the Docs

1. Entrar em <https://readthedocs.org> com a conta GitHub.
2. **Add project** → importar `nunomourinho/secVision-docs`, com o nome `secvision-user-manual`.
3. Em *Settings*, escolher o idioma **Portuguese**. O resto vem de `.readthedocs.yaml`, incluindo o PDF
   e o EPUB.

Cada *push* para `main` reconstrói o manual.

## Carregar os vídeos no YouTube (canal próprio do SecVision)

`scripts/youtube_upload.py` carrega a série com a YouTube Data API v3: a versão com as legendas
gravadas na imagem, título, descrição com capítulos e a ligação para a página do manual, e uma playlist
«Formação SecVision». Os vídeos ficam **não listados** por omissão. O ID de cada vídeo fica em
`docs/_data/videos.json`; depois de um *commit* + *push* desse ficheiro, os vídeos aparecem nas páginas.

O processo é o mesmo do manual do ForensicVM, com credenciais em `~/.config/secvision/`:

1. **Google Cloud** (uma vez): criar um projeto, ativar a **YouTube Data API v3**, configurar o ecrã de
   consentimento OAuth (tipo **Externo**, com a conta dona do canal em *Utilizadores de teste*) e criar
   um **ID do cliente OAuth** do tipo **Aplicação para computador**. Guardar o JSON:

   ```bash
   install -d -m 700 ~/.config/secvision
   install -m 600 client_secret_*.json ~/.config/secvision/youtube-client-secret.json
   ```

2. **Canal:** o canal tem de existir e, para vídeos com mais de 15 minutos, estar **verificado** em
   <https://www.youtube.com/verify>.
3. **Dependências:** `.venv/bin/pip install -r scripts/requirements-youtube.txt`
4. **Login** (sem browser no servidor):

   ```bash
   .venv/bin/python scripts/youtube_upload.py --auth-url
   # abrir o endereço, escolher o canal do SecVision, autorizar; copiar o endereço localhost:8765 final
   .venv/bin/python scripts/youtube_upload.py --auth-code 'http://localhost:8765/?state=…&code=…'
   ```

5. **Primeiro vídeo**, que fixa o canal (recusa depois carregar para outro):

   ```bash
   .venv/bin/python scripts/youtube_upload.py --simular
   .venv/bin/python scripts/youtube_upload.py --canal "Nome exato do canal" --apenas 101-ciberseguranca-e-gestao
   ```

6. **O resto:** `.venv/bin/python scripts/youtube_upload.py`, depois
   `git add docs/_data/videos.json && git commit -m "docs: vídeos do YouTube" && git push`.
7. **Um vídeo refeito:** `--substituir <id> …` carrega a versão nova; a antiga sai da playlist e fica
   privada, com «[substituído]» no título (nunca se apaga). Depois volte a exportar a ajuda do
   SecVision, que guarda os IDs do YouTube.

Os vídeos vêm de `~/Documents/SecVision-videos/pt-PT` (ou `SECVISION_VIDEOS`, ou `--videos`).

**Limitações** (as mesmas do ForensicVM): em projetos Google Cloud não auditados, os vídeos ficam
**privados** seja qual for a opção pedida, e é preciso torná-los públicos ou não listados no YouTube
Studio. A quota diária é de 10 000 unidades (cerca de 1 600 por upload). Um canal não verificado aceita
poucos uploads por dia. O script guarda o progresso e retoma onde ficou. **As credenciais nunca vão para
o repositório** (o `.gitignore` exclui `client_secret*.json` e `youtube-token*.json`).

## Comentários e correções

São bem-vindos nas *issues* deste repositório.

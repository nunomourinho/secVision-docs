"""Configuração Sphinx do manual do utilizador do SecVision."""
import sys
from pathlib import Path

# diretiva {video}
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'ext'))

project = 'SecVision'
author = 'Nuno Mourinho e colaboradores'
copyright = '2026, Nuno Mourinho e colaboradores'
language = 'pt_PT'
# versão do manual (o EPUB3 exige uma)
version = release = '2026.11'

extensions = ['myst_parser', 'secvision_sphinx']
myst_enable_extensions = ['colon_fence', 'deflist', 'attrs_inline', 'attrs_block']
myst_heading_anchors = 3
source_suffix = {'.md': 'markdown'}
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_title = 'SecVision — Manual do utilizador'
html_logo = '_static/logo.svg'
html_favicon = '_static/favicon.ico'
html_static_path = ['_static']
html_css_files = ['css/secvision.css']
html_theme_options = {
    'logo_only': True,
    'navigation_depth': 3,
    'collapse_navigation': False,
    'style_external_links': True,
    'style_nav_header_background': '#0F172A',
}
html_show_sourcelink = False

# PDF (Read the Docs): XeLaTeX por causa dos caracteres Unicode (›, →, «») e A4
latex_engine = 'xelatex'
latex_documents = [('index', 'secvision.tex', 'SecVision — Manual do utilizador', author, 'manual')]
latex_elements = {'papersize': 'a4paper', 'pointsize': '11pt'}
latex_logo = '_static/logo.png'
epub_show_urls = 'footnote'
# os capturas.json (índice dos números de cada captura) não entram no EPUB
suppress_warnings = ['epub.unknown_project_files']

#!/usr/bin/env python3
"""Carrega os vídeos da formação SecVision no YouTube (YouTube Data API v3).

Para cada vídeo: upload resumível do MP4 legendado (legendas gravadas na imagem), título,
descrição com os capítulos e a ligação para a página do manual, e inserção na playlist da série.
Se não houver versão legendada, envia a -musica.mp4 e carrega o .srt/.vtt como faixa de legendas.
O estado fica em docs/_data/videos.json, gravado depois de cada vídeo; uma nova execução salta o
que já foi feito. Ao esgotar a quota diária, pára e diz para retomar no dia seguinte.

Credenciais (nunca no repositório):
    ~/.config/secvision/youtube-client-secret.json    cliente OAuth «Aplicação para computador»
    ~/.config/secvision/youtube-token.json            criado no primeiro login (0600)

Autenticação sem browser local (servidor remoto):
    youtube_upload.py --auth-url                      # imprime o endereço a abrir
    youtube_upload.py --auth-code 'http://localhost:8765/?state=…&code=…'

Uso:
    youtube_upload.py --simular                       # mostra o que faria, sem API
    youtube_upload.py --canal "Nome do canal" --apenas 101-ciberseguranca-e-gestao   # 1.º, fixa o canal
    youtube_upload.py                                 # todos os que faltam, pela ordem do manual
"""
import argparse
import json
import os
import sys
import time
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ESTADO = RAIZ / 'docs' / '_data' / 'videos.json'
CONFIG = Path.home() / '.config' / 'secvision'
CLIENTE = CONFIG / 'youtube-client-secret.json'
TOKEN = CONFIG / 'youtube-token.json'
PENDENTE = CONFIG / 'youtube-auth-pendente.json'   # state + code_verifier entre --auth-url e --auth-code
REDIRECT = 'http://localhost:8765/'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload',
          'https://www.googleapis.com/auth/youtube.force-ssl']

LINGUAS = {
    'pt': {
        'videos': Path(os.environ.get('SECVISION_VIDEOS', Path.home() / 'Documents' / 'SecVision-videos' / 'pt-PT')),
        'codigo': 'pt-PT', 'nome_legendas': 'Português (Portugal)',
        'playlist': 'Formação SecVision',
        'playlist_desc': ('Formação SecVision: cibersegurança e conformidade com o DL 125/2025 e o '
                          'Regulamento 756/2026, para quem não tem formação na área, e a plataforma ecrã a ecrã.'),
        'capitulos': 'Capítulos:', 'documentacao': 'Manual (passo a passo, com capturas de ecrã):',
        'aviso': ('Exemplos feitos no ambiente de testes do SecVision, com uma organização fictícia '
                  '(Instituto Politécnico de Vila Nova); todos os nomes e dados são inventados.'),
        'tags': ['SecVision', 'cibersegurança', 'NIS 2', 'DL 125/2025', 'Regulamento 756/2026', 'CNCS',
                 'QNRCS', 'ISO 27001', 'SGSI', 'gestão de risco', 'conformidade', 'Wazuh'],
        'docs': True,
    },
}

# Ordem de visionamento (a mesma do manual) e página de cada vídeo: docs/_data/serie.json
SERIE = json.loads((RAIZ / 'docs' / '_data' / 'serie.json').read_text(encoding='utf-8'))
PAGINAS = {vid: info['pagina'] for vid, info in SERIE.items()}
CATEGORIA = '27'  # Educação
CANAL_ESPERADO = None


def tempo(seg):
    seg = int(seg)
    h, r = divmod(seg, 3600)
    m, s = divmod(r, 60)
    return f'{h}:{m:02d}:{s:02d}' if h else f'{m}:{s:02d}'


def metadados(vid, videos_dir, docs_url, L):
    meta = json.loads((videos_dir / f'{vid}.json').read_text(encoding='utf-8'))
    titulo = meta['titulo']
    resumo = meta.get('resumo') or SERIE[vid]['resumo']
    # capítulos seguidos com o mesmo título juntam-se no primeiro
    caps = [c for i, c in enumerate(meta.get('capitulos', []))
            if i == 0 or c['titulo'] != meta['capitulos'][i - 1]['titulo']]
    linhas = [resumo, '']
    # o YouTube só reconhece capítulos com pelo menos 3 entradas, a primeira em 0:00
    if len(caps) >= 3 and caps[0]['t'] == 0:
        linhas += [L['capitulos']] + [f"{tempo(c['t'])} {c['titulo']}" for c in caps] + ['']
    if L['docs']:
        linhas += [f"{L['documentacao']} {docs_url.rstrip('/')}/{PAGINAS[vid]}.html", '']
    linhas += [L['aviso']]
    # versão com as legendas gravadas na imagem; sem ela, a com música + faixa de legendas
    legendado = videos_dir / f'{vid}-legendado.mp4'
    gravadas = legendado.exists()
    return {
        'titulo': (titulo if titulo.startswith('SecVision') else f'SecVision — {titulo}')[:100],
        'descricao': '\n'.join(linhas)[:5000],
        'mp4': legendado if gravadas else videos_dir / f'{vid}-musica.mp4',
        'gravadas': gravadas,
        # o YouTube aceita SRT e WebVTT; o vídeo completo só tem .vtt
        'srt': next((f for f in (videos_dir / f'{vid}.srt', videos_dir / f'{vid}.vtt') if f.exists()),
                    videos_dir / f'{vid}.srt'),
    }


def carregar_estado():
    return json.loads(ESTADO.read_text(encoding='utf-8')) if ESTADO.exists() else {}


def gravar_estado(estado):
    tmp = ESTADO.with_suffix('.tmp')
    tmp.write_text(json.dumps(estado, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    tmp.replace(ESTADO)


def gravar_privado(caminho, texto):
    CONFIG.mkdir(parents=True, exist_ok=True)
    fd = os.open(caminho, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, 'w') as f:
        f.write(texto)
    os.chmod(caminho, 0o600)


def novo_flow(state=None, verifier=None):
    from google_auth_oauthlib.flow import Flow
    if not CLIENTE.exists():
        sys.exit(f'Falta o cliente OAuth em {CLIENTE} — ver o README (Fase B).')
    flow = Flow.from_client_secrets_file(str(CLIENTE), SCOPES, state=state, redirect_uri=REDIRECT)
    if verifier:
        flow.code_verifier = verifier
    return flow


def auth_url():
    """Passo 1 do login sem browser local: imprime o endereço e guarda o state/PKCE."""
    flow = novo_flow()
    url, state = flow.authorization_url(access_type='offline', prompt='consent select_account')
    gravar_privado(PENDENTE, json.dumps({'state': state, 'verifier': flow.code_verifier}))
    print('Abra este endereço, escolha o canal do SecVision e autorize:\n')
    print(url)
    print('\nO browser acaba numa página http://localhost:8765/… que não abre — copie esse endereço '
          'completo e passe-o a --auth-code.')


def auth_code(resposta):
    """Passo 2: troca o código pelo token e mostra o canal autorizado."""
    if not PENDENTE.exists():
        sys.exit('Corra primeiro --auth-url.')
    p = json.loads(PENDENTE.read_text())
    flow = novo_flow(p['state'], p['verifier'])
    # o redirect é http://localhost; o oauthlib só o aceita com esta variável
    os.environ.setdefault('OAUTHLIB_INSECURE_TRANSPORT', '1')
    flow.fetch_token(authorization_response=resposta.strip())
    gravar_privado(TOKEN, flow.credentials.to_json())
    PENDENTE.unlink()
    from googleapiclient.discovery import build
    yt = build('youtube', 'v3', credentials=flow.credentials)
    for c in canais(yt):
        print(f"Canal autorizado: {c['snippet']['title']}  ({c['id']})")


def canais(yt):
    return executar(yt.channels().list(part='snippet', mine=True)).get('items', [])


def autenticar():
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build

    cred = Credentials.from_authorized_user_file(str(TOKEN), SCOPES) if TOKEN.exists() else None
    if cred and cred.expired and cred.refresh_token:
        cred.refresh(Request())
        gravar_privado(TOKEN, cred.to_json())
    elif not cred or not cred.valid:
        sys.exit('Sem token válido — corra --auth-url e depois --auth-code.')
    return build('youtube', 'v3', credentials=cred)


def confirmar_canal(yt, raiz):
    """Fixa o canal no primeiro uso e recusa carregar para outro."""
    ch = canais(yt)
    if len(ch) != 1:
        sys.exit(f'A conta autorizada tem {len(ch)} canais visíveis — esperado 1.')
    cid, nome = ch[0]['id'], ch[0]['snippet']['title']
    fixo = raiz.get('_canal')
    if not fixo:
        if CANAL_ESPERADO is None or CANAL_ESPERADO.casefold() != nome.casefold():
            sys.exit(f'O canal autorizado é «{nome}» ({cid}). No primeiro carregamento, confirme-o com '
                     f'--canal "{nome}"; fica fixado em docs/_data/videos.json e não se carrega para outro.')
        raiz['_canal'] = {'id': cid, 'titulo': nome}
    elif fixo['id'] != cid:
        sys.exit(f'O canal autorizado é «{nome}» ({cid}), não o fixado «{fixo["titulo"]}» ({fixo["id"]}).')
    print(f'Canal: {nome} ({cid})')


class QuotaEsgotada(Exception):
    pass


def executar(pedido):
    """Executa um pedido simples, convertendo quotaExceeded em QuotaEsgotada."""
    from googleapiclient.errors import HttpError
    try:
        return pedido.execute()
    except HttpError as e:
        if e.resp.status == 403 and b'quota' in e.content.lower():
            raise QuotaEsgotada() from e
        raise


def upload(yt, m, privacidade, L):
    from googleapiclient.errors import HttpError
    from googleapiclient.http import MediaFileUpload

    corpo = {
        'snippet': {'title': m['titulo'], 'description': m['descricao'], 'tags': L['tags'],
                    'categoryId': CATEGORIA, 'defaultLanguage': L['codigo'], 'defaultAudioLanguage': L['codigo']},
        'status': {'privacyStatus': privacidade, 'selfDeclaredMadeForKids': False, 'embeddable': True},
    }
    media = MediaFileUpload(str(m['mp4']), mimetype='video/mp4', chunksize=8 * 1024 * 1024, resumable=True)
    pedido = yt.videos().insert(part='snippet,status', body=corpo, media_body=media)
    resposta, tentativas = None, 0
    while resposta is None:
        try:
            estado, resposta = pedido.next_chunk()
            if estado:
                print(f'  … {int(estado.progress() * 100)}%', end='\r', flush=True)
        except HttpError as e:
            if (e.resp.status == 403 and b'quota' in e.content.lower()) or b'uploadLimitExceeded' in e.content:
                raise QuotaEsgotada() from e
            if e.resp.status not in (500, 502, 503, 504) or tentativas >= 8:
                raise
            tentativas += 1
            time.sleep(2 ** tentativas)
    print()
    return resposta['id'], resposta.get('status', {}).get('privacyStatus')


def legendas(yt, video_id, srt, L):
    from googleapiclient.http import MediaFileUpload
    corpo = {'snippet': {'videoId': video_id, 'language': L['codigo'], 'name': L['nome_legendas']}}
    executar(yt.captions().insert(part='snippet', body=corpo,
                                  media_body=MediaFileUpload(str(srt), mimetype='application/octet-stream')))


def playlist(yt, estado, raiz, L, privacidade):
    pid = estado.get('_playlist')
    if not pid:
        r = executar(yt.playlists().insert(part='snippet,status', body={
            'snippet': {'title': L['playlist'], 'description': L['playlist_desc'], 'defaultLanguage': L['codigo']},
            'status': {'privacyStatus': privacidade}}))
        pid = estado['_playlist'] = r['id']
        gravar_estado(raiz)
    return pid


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--lang', choices=list(LINGUAS), default='pt')
    ap.add_argument('--videos', type=Path, help='pasta dos vídeos (por omissão, a da língua)')
    ap.add_argument('--docs-url', default='https://secvision-user-manual.readthedocs.io/pt/latest')
    ap.add_argument('--canal', metavar='NOME', help='primeiro carregamento: nome do canal, para o fixar')
    ap.add_argument('--privacidade', choices=['public', 'unlisted', 'private'], default='unlisted')
    ap.add_argument('--apenas', nargs='+', metavar='ID', help='só estes vídeos')
    ap.add_argument('--simular', action='store_true', help='mostra os metadados sem usar a API')
    ap.add_argument('--auth-url', action='store_true', help='login, passo 1: imprime o endereço a abrir')
    ap.add_argument('--auth-code', metavar='URL', help='login, passo 2: endereço localhost:8765 colado')
    args = ap.parse_args()

    if args.auth_url:
        return auth_url()
    if args.auth_code:
        return auth_code(args.auth_code)

    global CANAL_ESPERADO
    CANAL_ESPERADO = args.canal
    L = LINGUAS[args.lang]
    videos = args.videos or L['videos']
    ids = args.apenas or list(PAGINAS)
    desconhecidos = [i for i in ids if i not in PAGINAS]
    if desconhecidos:
        sys.exit(f'Ids desconhecidos: {", ".join(desconhecidos)}')

    # pt fica na raiz (é o que a diretiva {video} lê); outras línguas, no futuro, numa secção própria
    raiz = carregar_estado()
    estado = raiz if args.lang == 'pt' else raiz.setdefault(args.lang, {})
    pendentes = [i for i in ids if not estado.get(i, {}).get('youtube') or not estado[i].get('legendas')]
    print(f'{len(pendentes)} vídeo(s) por carregar ({args.lang}).')

    if args.simular:
        for vid in pendentes:
            m = metadados(vid, videos, args.docs_url, L)
            tam = m['mp4'].stat().st_size / 1e6
            leg = 'gravadas' if m['gravadas'] else ('faixa ' + m['srt'].suffix if m['srt'].exists() else 'NÃO')
            print(f"\n=== {vid}  ({m['mp4'].name}, {tam:.0f} MB, legendas: {leg})")
            print(m['titulo'])
            print(m['descricao'])
        return

    yt = autenticar()
    confirmar_canal(yt, raiz)
    gravar_estado(raiz)
    aviso_bloqueio = False
    try:
        pid = playlist(yt, estado, raiz, L, args.privacidade)
        for vid in pendentes:
            m = metadados(vid, videos, args.docs_url, L)
            info = estado.setdefault(vid, {'titulo': m['titulo']})
            if not info.get('youtube'):
                print(f'→ {vid}: upload de {m["mp4"].name}')
                info['youtube'], info['privacidade'] = upload(yt, m, args.privacidade, L)
                if m['gravadas']:
                    info['legendas'] = 'gravadas'
                gravar_estado(raiz)
                executar(yt.playlistItems().insert(part='snippet', body={'snippet': {
                    'playlistId': pid, 'resourceId': {'kind': 'youtube#video', 'videoId': info['youtube']}}}))
                print(f'  https://youtu.be/{info["youtube"]}  ({info["privacidade"]})')
                if info['privacidade'] != args.privacidade and not aviso_bloqueio:
                    aviso_bloqueio = True
                    print(f'  AVISO: pedido {args.privacidade}, o YouTube devolveu {info["privacidade"]} — '
                          'o projeto da API provavelmente não está auditado (vídeos bloqueados como privados).')
            if not info.get('legendas'):
                if m['srt'].exists():
                    legendas(yt, info['youtube'], m['srt'], L)
                    info['legendas'] = True
                    print(f"  legendas {L['codigo']} carregadas")
                else:
                    info['legendas'] = 'nenhumas'
                gravar_estado(raiz)
    except QuotaEsgotada:
        gravar_estado(raiz)
        sys.exit('Quota diária da API (ou limite de uploads do canal) esgotada. O progresso ficou guardado — volte a correr amanhã.')
    print('Concluído.')


if __name__ == '__main__':
    main()

"""原稿の外部リンク（http:// と https://）のうち、切れているかもしれないものを洗い出す。

- 検査するのは Markdown のリンク先（`[文字](URL)`）だけ。コードブロック・コードスパンの中と、本文にむき出しで書かれた URL
  （例示の http://xxx.yyy/ など）は、サイトでもリンクにならないので見ない
- 後ろに「（[アーカイブ](...)）」を添えたリンクは、切れていると分かっているので見ない。localhost などの手元向けのリンクも見ない
- 切れているかどうかは判断しない。200 を返しても、閉鎖の告知やトップページへの転送で中身が無くなっていることがあり、
  語の一覧では決めきれないため。エラーになったものと、別の URL へ転送されたものを、行き着いた URL とタイトルを添えて並べるので、
  開いて確かめること。転送も無く中身だけが告知に変わったものは、--titles で 200 のものもタイトル付きで並べて目で探す
- 外部サイトの都合で結果が揺れるため、CI では走らせない。手で走らせる。終了コードはいつも 0

標準ライブラリだけで動く。
    python scripts/check_links.py                            # 全部
    python scripts/check_links.py --titles                   # 200 のものもタイトル付きで並べる
    python scripts/check_links.py dev list/shiori-event-ex   # 一部のディレクトリ・ファイルだけ
"""
import gzip
import html
import os
import re
import socket
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlsplit

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
DIRS = ['manual', 'descript', 'list', 'spec', 'dev', 'memo']
TOP_FILES = ['INDEX.md']

FENCE = re.compile(r'^\s*(```|~~~)')
CODE_SPAN = re.compile(r'`[^`]*`')
LINK = re.compile(r'\]\((https?://[^)\s]+)\)(（\[アーカイブ\]\()?')
TITLE = re.compile(r'<title[^>]*>(.*?)</title>', re.S | re.I)
LOCAL_HOSTS = {'localhost', '127.0.0.1'}

USER_AGENT = 'Mozilla/5.0 (compatible; ukadoc-spec-linkcheck; +https://github.com/ukatech/ukadoc-spec)'
TIMEOUT = 20
RETRIES = 2        # タイムアウトや 429 など、一時的な失敗のときに取り直す回数
WORKERS = 6


def md_files(dirs):
    for d in dirs:
        path = os.path.join(ROOT, d)
        if os.path.isfile(path):
            yield d
            continue
        for dirpath, _, files in os.walk(path):
            for name in sorted(files):
                if name.endswith('.md'):
                    yield os.path.relpath(os.path.join(dirpath, name), ROOT).replace(os.sep, '/')


def collect(dirs):
    """URL → [ファイル:行, ...]"""
    found = {}
    for rel in md_files(dirs):
        with open(os.path.join(ROOT, rel), encoding='utf-8') as f:
            lines = f.read().split('\n')
        in_fence = False
        for no, line in enumerate(lines, 1):
            if FENCE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            for m in LINK.finditer(CODE_SPAN.sub('', line)):
                url, archived = m.group(1), m.group(2)
                if archived or urlsplit(url).hostname in LOCAL_HOSTS or 'web.archive.org' in url:
                    continue
                found.setdefault(url, []).append(f'{rel}:{no}')
    return found


def decode(body, charset):
    if body[:2] == b'\x1f\x8b':
        body = gzip.decompress(body)
    for enc in [charset, 'utf-8', 'shift_jis', 'euc-jp', 'utf-16']:
        if not enc:
            continue
        try:
            return body.decode(enc)
        except (UnicodeDecodeError, LookupError):
            pass
    return body.decode('utf-8', 'replace')


def fetch(url):
    """(状態コード または エラーの種類, 行き着いた URL, ページのタイトル) を返す"""
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    for attempt in range(RETRIES + 1):
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                text = decode(r.read(300_000), r.headers.get_content_charset())
                m = TITLE.search(text)
                return r.status, r.geturl(), html.unescape(re.sub(r'\s+', ' ', m.group(1))).strip() if m else ''
        except urllib.error.HTTPError as e:
            if e.code not in (429, 503) or attempt == RETRIES:
                return e.code, url, ''
        except urllib.error.URLError as e:
            kind = 'DNS' if isinstance(e.reason, socket.gaierror) else 'CONNECT'
            if kind == 'DNS' or attempt == RETRIES:
                return kind, url, ''
        except (TimeoutError, OSError):
            if attempt == RETRIES:
                return 'TIMEOUT', url, ''
        time.sleep(3 * (attempt + 1))


def same_place(url, final_url):
    """転送されても、http → https、末尾の /、既定のポートの違いだけなら同じ場所とみなす"""
    def norm(u):
        s = urlsplit(u)
        host = (s.hostname or '').lower()
        return host, s.path.rstrip('/'), s.query
    return norm(url) == norm(final_url)


def kind(status, url, final_url):
    if status != 200:
        return 'エラー'
    if not same_place(url, final_url):
        return '転送'
    return None


def main():
    args = sys.argv[1:]
    titles = '--titles' in args
    dirs = [a for a in args if a != '--titles'] or DIRS + TOP_FILES
    found = collect(dirs)
    print(f'{len(found)} 件の URL（のべ {sum(map(len, found.values()))} か所）を確かめる', file=sys.stderr)
    with ThreadPoolExecutor(WORKERS) as ex:
        results = dict(zip(found, ex.map(fetch, found)))

    groups = {'エラー': [], '転送': [], None: []}
    for url, (status, final_url, title) in sorted(results.items()):
        groups[kind(status, url, final_url)].append((url, status, final_url, title))
    for name, rows in groups.items():
        if name is None and not titles or not rows:
            continue
        print(f'## {name or "200（転送なし）"}（{len(rows)} 件）\n')
        for url, status, final_url, title in rows:
            print(f'{status} {url}')
            if name == '転送':
                print(f'  → {final_url}')
            if title:
                print(f'  「{title[:80]}」')
            for loc in found[url]:
                print(f'  - {loc}')
        print()
    print(f'エラー {len(groups["エラー"])} 件、転送 {len(groups["転送"])} 件。開いて確かめること', file=sys.stderr)


if __name__ == '__main__':
    main()

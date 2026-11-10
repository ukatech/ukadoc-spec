"""_site_old/ の内部リンクを調べる（リンク先のファイルと #アンカーの有無、画像の有無）。

使い方: python oldstyle/check.py [--lang=<コード>]    （--lang を付けると _site_old/<コード>/ の翻訳版を調べる）
"""
import os
import re
import sys
from urllib.parse import unquote

import lxml.html

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
LANG = next((a.split('=', 1)[1] for a in sys.argv[1:] if a.startswith('--lang=')), None)
OUT = os.path.join(ROOT, '_site_old', *([LANG] if LANG else []))
SCHEME = re.compile(r'^[a-z][a-z0-9+.-]*:', re.I)


def main():
    ids = {}
    docs = {}
    for name in sorted(os.listdir(OUT)):
        if name.endswith('.html'):
            with open(os.path.join(OUT, name), encoding='utf-8') as f:
                doc = lxml.html.fromstring(f.read())
            docs[name] = doc
            found = set()
            for el in doc.iter():
                if isinstance(el.tag, str):
                    for attr in ('id', 'name'):
                        if el.get(attr):
                            found.add(el.get(attr))
            ids[name] = found
    errors = []
    for name, doc in docs.items():
        for a in doc.iter('a'):
            href = a.get('href')
            if not href or SCHEME.match(href):
                continue
            path, _, frag = href.partition('#')
            target = unquote(path) or name
            if not os.path.exists(os.path.join(OUT, target)):
                errors.append(f'{name}: リンク先のファイルが無い: {href}')
            elif frag and target in ids and unquote(frag) not in ids[target]:
                errors.append(f'{name}: アンカーが無い: {href}')
        for img in doc.iter('img'):
            src = img.get('src')
            if src and not SCHEME.match(src) and not os.path.exists(os.path.join(OUT, unquote(src))):
                errors.append(f'{name}: 画像が無い: {src}')
    for e in errors:
        print(e)
    print(f'{len(docs)} 頁、{len(errors)} 件の問題')
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()

"""原稿（.md）の内部リンクを、原稿のファイルと行番号つきで調べる（MkDocs の strict 相当）。

- 相対パスのリンク・画像・HTML の href / src が指すファイルがあるか
- `file.md#見出し` の見出しがあるか（見出しの id は、サイトのビルドと同じ toc の規則で数える）

使い方: python scripts/check_source.py [ファイル...]   （引数なしなら、リポジトリの全 .md）
出力サイト側の検査（oldstyle/check.py）は別。こちらは、直すべき原稿の場所がわかるのが利点。
外部リンクは scripts/check_links.py。CLAUDE.md は例のリンクを含むので調べない。
"""
import os
import posixpath
import re
import sys
from urllib.parse import unquote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import prepare_site as ps   # old_ids（見出しの id の数え方）・fence_free_headings を使い回す

ROOT = ps.ROOT
SKIP_FILES = {'CLAUDE.md'}
SKIP_DIRS = {'node_modules', 'site_ext'}
SCHEME = re.compile(r'^([a-z][a-z0-9+.-]*:|//)', re.I)
MD_LINK = re.compile(r'!?\[(?:[^\]\\]|\\.)*\]\(\s*<?([^)\s>]+)>?(?:\s+"[^"]*")?\s*\)')
HTML_ATTR = re.compile(r'\b(?:href|src)="([^"]+)"')
CODE_SPAN = re.compile(r'(`+)(?:(?!\1).)+?\1')

_IDS = {}   # 原稿のパス → 見出しの id の集合


def heading_ids(rel):
    if rel not in _IDS:
        original = ps.error
        ps.error = lambda msg: None   # 見出しの数の食い違いは prepare_site の仕事。ここでは数えない
        try:
            _IDS[rel] = set(ps.old_ids(ps.read(rel), rel))
        finally:
            ps.error = original
    return _IDS[rel]


def md_files():
    for base, dirs, names in os.walk(ROOT):
        dirs[:] = [d for d in dirs if not d.startswith(('.', '_')) and d not in SKIP_DIRS]
        for name in sorted(names):
            if name.endswith('.md') and not (base == ROOT and name in SKIP_FILES):
                yield posixpath.normpath(os.path.relpath(os.path.join(base, name), ROOT).replace(os.sep, '/'))


def links(text):
    """(行番号, リンク先) を返す。コードブロック・コードスパンの中は除く"""
    in_fence = False
    for n, line in enumerate(text.split('\n'), 1):
        if ps.FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        line = CODE_SPAN.sub('', line)
        for m in MD_LINK.finditer(line):
            yield n, m.group(1)
        for m in HTML_ATTR.finditer(line):
            yield n, m.group(1)


def check(rel):
    errors = []
    for n, href in links(ps.read(rel)):
        if SCHEME.match(href) or href.startswith('/'):
            continue
        path, _, frag = href.partition('#')
        path = unquote(path.partition('?')[0])
        frag = unquote(frag)
        target = rel if path == '' else posixpath.normpath(posixpath.join(posixpath.dirname(rel), path))
        full = os.path.join(ROOT, target)
        if not os.path.exists(full):
            errors.append(f'{rel}:{n}: リンク先のファイルが無い: {href}')
        elif frag and target.endswith('.md') and os.path.isfile(full) and frag not in heading_ids(target):
            errors.append(f'{rel}:{n}: リンク先の見出しが無い: {href}')
    return errors


def main():
    files = [posixpath.normpath(a.replace(os.sep, '/')) for a in sys.argv[1:]] or list(md_files())
    errors = []
    for rel in files:
        errors.extend(check(rel))
    for e in errors:
        print(e)
    print(f'{len(files)} 件の原稿、{len(errors)} 件の問題')
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()

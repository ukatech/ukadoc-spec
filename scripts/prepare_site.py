"""GitHub Pages 用に原稿を _site_src/ へ写す。

- 旧 HTML 版で 1 ページだったもの（descript/<名前>/、list/<名前>/、spec/<名前>/ の各ディレクトリ）を、
  サイトでは 1 ページ（<ディレクトリ>/index.md）にまとめる。並びは各 index.md の「## 一覧」の順。
  ディレクトリ内の見出しは入れ子の深さの分だけずらし、一意な id（`{#id}`）を振る
- まとめた項目へのリンク（相対パス・#見出し）は、まとめたページの見出しへのリンクに書き換える
- 各 index.md の「## 一覧」が、ディレクトリの項目（.md とサブディレクトリ）と過不足なく一致しているかを検査する
- INDEX.md を index.md（トップページ）にし、INDEX.md へのリンクも書き換える。llms.txt をサイトのルートに置く
原稿そのものは書き換えない。
"""
import os
import posixpath
import re
import shutil
import sys
from urllib.parse import unquote

import markdown
from pymdownx.slugs import slugify

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(ROOT, '_site_src')
DIRS = ['manual', 'descript', 'list', 'spec', 'dev', 'memo']
BUNDLE_DIRS = ['descript', 'list', 'spec']   # <これ>/<名前>/index.md があれば、そのディレクトリを 1 ページにまとめる

EXTENSIONS = ['tables', 'admonition', 'attr_list', 'md_in_html', 'mdx_truly_sane_lists', 'pymdownx.superfences']
HEADING_LINE = re.compile(r'^(#{1,6}) +(.+?) *$')
FENCE = re.compile(r'^\s*(```|~~~)')
LIST_LINK = re.compile(r'^- \[.*\]\(([^)]+)\)\s*$')
INDEX_SECTION = '\n## 一覧\n'
LINK = re.compile(r'\]\(([^)#\s]*)(#[^)\s]*)?\)')
CATEGORY_LINE = re.compile(r'^\*\*カテゴリ:\*\*.*\n\n?', re.M)

ERRORS = []
UNIT = {}      # 元ページ（ROOT からの相対パス）→ (まとめたページ, ページ内の id, {元の見出しの id: まとめたページでの id})


def error(msg):
    ERRORS.append(msg)
    print(f'エラー: {msg}', file=sys.stderr)


def read(rel):
    with open(os.path.join(ROOT, rel), encoding='utf-8') as f:
        return f.read()


def write(rel, text):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


# ---------------------------------------------------------------- 一覧

def list_children(index_rel):
    """index.md の「## 一覧」のリンク先（ROOT からの相対パス）を、書かれた順に返す"""
    text = read(index_rel)
    if INDEX_SECTION not in text:
        return []
    section = text.split(INDEX_SECTION, 1)[1].split('\n## ', 1)[0]
    out = []
    for line in section.split('\n'):
        m = LIST_LINK.match(line)
        if m:
            out.append(posixpath.normpath(posixpath.join(posixpath.dirname(index_rel), unquote(m.group(1)))))
    return out


def check_index(index_rel):
    """「## 一覧」と、ディレクトリの中身を突き合わせる"""
    directory = os.path.join(ROOT, posixpath.dirname(index_rel))
    listed = [posixpath.relpath(c, posixpath.dirname(index_rel)).split('/')[0] for c in list_children(index_rel)]
    if INDEX_SECTION not in read(index_rel):
        return
    actual = []
    for name in os.listdir(directory):
        full = os.path.join(directory, name)
        if os.path.isdir(full):
            actual.append(name)
        elif name.endswith('.md') and name != 'index.md':
            actual.append(name)
    for name in sorted(set(actual) - set(listed)):
        error(f'{index_rel}: 「## 一覧」に {name} が無い')
    for name in sorted(set(listed) - set(actual)):
        error(f'{index_rel}: 「## 一覧」の {name} が無い')
    for name in sorted({n for n in listed if listed.count(n) > 1}):
        error(f'{index_rel}: 「## 一覧」に {name} が 2 回以上ある')


def collect(index_rel, depth):
    """index.md を頂点に、「## 一覧」をたどった (パス, 深さ, index か) を文書順に返す。ページ本体の index.md が深さ 1"""
    yield index_rel, depth, True
    for child in list_children(index_rel):
        if child.endswith('/index.md'):
            yield from collect(child, depth + 1)
        else:
            yield child, depth + 1, False


# ---------------------------------------------------------------- 見出し

def fence_free_headings(text):
    """コードブロックの外の見出し行を (行番号, 深さ, 見出し) で返す"""
    in_fence = False
    for i, line in enumerate(text.split('\n')):
        if FENCE.match(line):
            in_fence = not in_fence
        elif not in_fence:
            m = HEADING_LINE.match(line)
            if m:
                yield i, len(m.group(1)), m.group(2)


def old_ids(text, rel):
    """サイトの toc 拡張が原稿の見出しに付ける id を、文書順に返す"""
    md = markdown.Markdown(extensions=EXTENSIONS + ['toc'],
                           extension_configs={'toc': {'slugify': slugify(case='lower'), 'toc_depth': '1-6'}})
    md.convert(text)
    ids = []

    def walk(tokens):
        for t in tokens:
            ids.append(t['id'])
            walk(t['children'])
    walk(md.toc_tokens)
    heads = list(fence_free_headings(text))
    if len(ids) != len(heads):
        error(f'{rel}: 見出しの数が合わない（toc {len(ids)}、行 {len(heads)}）')
    return ids


def unit_body(rel, is_index):
    text = read(rel)
    if is_index and INDEX_SECTION in text:
        text = text.split(INDEX_SECTION, 1)[0].rstrip('\n') + '\n'
    return CATEGORY_LINE.sub('', text, count=1)


def register_bundle(page_dir):
    """ディレクトリ page_dir をまとめるページを登録し、(パス, 深さ, 本文) のリストを返す"""
    dst = f'{page_dir}/index.md'
    units = [(rel, depth, is_index, unit_body(rel, is_index)) for rel, depth, is_index in collect(f'{page_dir}/index.md', 1)]
    # ページ内の id（項目のファイル名。重なるときはパス）
    def candidate(rel, is_index):
        return posixpath.basename(posixpath.dirname(rel)) if is_index else posixpath.basename(rel)[:-3]
    count = {}
    for rel, _, is_index, _ in units:
        count[candidate(rel, is_index)] = count.get(candidate(rel, is_index), 0) + 1
    keys = {}
    for rel, _, is_index, _ in units:
        c = candidate(rel, is_index)
        if count[c] > 1:
            sub = posixpath.relpath(posixpath.dirname(rel) if is_index else rel[:-3], page_dir)
            c = sub.replace('/', '-') if sub != '.' else c + '-page'
        keys[rel] = c
    if len(set(keys.values())) != len(keys):
        error(f'{page_dir}: まとめたページ内の id が重なる')
    used = set(keys.values())
    for rel, depth, is_index, text in units:
        key = keys[rel]
        olds = {}
        for n, old in enumerate(old_ids(text, rel)):
            new = key if n == 0 else f'{key}-{old}'
            if n and new in used:
                error(f'{rel}: まとめたページ内の id {new} が重なる')
            used.add(new)
            olds[old] = new
        UNIT[rel] = (dst, key, olds)
    return dst, units


def shift_headings(text, rel, depth):
    dst, key, olds = UNIT[rel]
    lines = text.split('\n')
    heads = list(fence_free_headings(text))
    ids = list(olds.values())
    for (i, level, title), new in zip(heads, ids):
        new_level = level + depth - 1
        if new_level > 6:
            error(f'{rel}: 見出しが H6 を超える')
            new_level = 6
        lines[i] = f'{"#" * new_level} {title} {{#{new}}}'
    return '\n'.join(lines)


# ---------------------------------------------------------------- リンク

def rewrite_links(text, src, dst):
    """src（ROOT からの相対パス）の本文 text を、サイトのページ dst 用にリンクを直す。
    まとめた項目へのリンクは、まとめたページの見出しへのリンクにし、それ以外は dst からの相対パスに直す"""
    def link(m):
        path, frag = m.group(1), (m.group(2) or '')[1:]
        if re.match(r'^[a-z][a-z0-9+.-]*:', path, re.I):
            return m.group(0)
        target = src if path == '' else posixpath.normpath(posixpath.join(posixpath.dirname(src), unquote(path)))
        if target in UNIT:
            page, key, olds = UNIT[target]
            new = key
            if frag:
                new = olds.get(unquote(frag))
                if new is None:
                    error(f'{src}: リンク先の見出し {target}#{frag} が無い')
                    new = key
            to = '' if page == dst else posixpath.relpath(page, posixpath.dirname(dst) or '.')
            return f']({to}#{new})'
        if path == '':
            return m.group(0)
        if target == 'INDEX.md':
            target = 'index.md'
        to = posixpath.relpath(target, posixpath.dirname(dst) or '.')
        return f']({to}{("#" + frag) if frag else ""})'

    out = []
    in_fence = False
    for line in text.split('\n'):
        if FENCE.match(line):
            in_fence = not in_fence
        elif not in_fence:
            line = LINK.sub(link, line)
        out.append(line)
    return '\n'.join(out)


# ---------------------------------------------------------------- 本体

def page_dirs():
    out = []
    for g in BUNDLE_DIRS:
        for name in sorted(os.listdir(os.path.join(ROOT, g))):
            if os.path.isfile(os.path.join(ROOT, g, name, 'index.md')):
                out.append(f'{g}/{name}')
    return out


def main():
    for d in DIRS:
        for dirpath, _, files in os.walk(os.path.join(ROOT, d)):
            if 'index.md' in files:
                check_index(os.path.relpath(os.path.join(dirpath, 'index.md'), ROOT).replace(os.sep, '/'))
    bundles = {}
    for page_dir in page_dirs():
        bundles[page_dir] = register_bundle(page_dir)
    if ERRORS:
        sys.exit(1)

    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    bundled = set()
    for page_dir, (dst, units) in bundles.items():
        parts = []
        for rel, depth, is_index, text in units:
            bundled.add(rel)
            parts.append(rewrite_links(shift_headings(text, rel, depth), rel, dst).strip('\n'))
        # 項目の切れ目がわかるよう、つないだ項目の間に水平線を入れる（見出しだけの項目の後ろには入れない）
        text = parts[0]
        for prev, part in zip(parts, parts[1:]):
            heading_only = '\n' not in prev.strip() and prev.lstrip().startswith('#')
            text += ('\n\n' if heading_only else '\n\n---\n\n') + part
        write(dst, text + '\n')

    for d in DIRS:
        for dirpath, _, files in os.walk(os.path.join(ROOT, d)):
            for name in sorted(files):
                rel = os.path.relpath(os.path.join(dirpath, name), ROOT).replace(os.sep, '/')
                if name.endswith('.md') and rel not in bundled:
                    write(rel, rewrite_links(read(rel), rel, rel))
    write('index.md', rewrite_links(read('INDEX.md'), 'INDEX.md', 'index.md'))

    # 左メニュー: まとめたディレクトリは、そのページ（index.md）を指す
    nav = read('.nav.yml')
    nav = re.sub(r'(: )((?:descript|list|spec)/[^/\s]+)$',
                 lambda m: m.group(1) + (m.group(2) + '/index.md' if m.group(2) in bundles else m.group(2)), nav, flags=re.M)
    write('.nav.yml', nav)
    shutil.copy(os.path.join(ROOT, 'llms.txt'), os.path.join(OUT, 'llms.txt'))
    shutil.copytree(os.path.join(ROOT, 'assets'), os.path.join(OUT, 'assets'))
    if ERRORS:
        sys.exit(1)


if __name__ == '__main__':
    main()

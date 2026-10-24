"""Text-equivalence gate: source HTML text of each unit vs. text of the generated Markdown
(rendered with the site's Python-Markdown extensions).  Run: python verify.py [stem ...]"""
import copy
import sys
import json
import urllib.parse
import posixpath
import markdown
import conv
import layout
from conv import *
from layout import *

EXT = ['tables', 'admonition', 'attr_list', 'md_in_html', 'mdx_truly_sane_lists', 'pymdownx.superfences']


def src_text(u):
    root = BeautifulSoup('<div></div>', 'lxml').div
    parts = []
    # title
    t = BeautifulSoup('<div></div>', 'lxml').new_tag('div')
    root.append(BeautifulSoup('<div id="t"></div>', 'lxml').div)
    for n in u.nodes:
        root.append(copy.copy(n))
    for e in root.find_all(list(DROP_TAGS)):
        e.decompose()
    for e in root.find_all(['nav'], class_=['menu-header', 'sidebar']):
        e.decompose()
    for e in root.find_all('p', class_=['banner', 'author']):
        e.decompose()
    for e in root.find_all('ul', class_='supported-baseware'):
        items = []
        for li in e.find_all('li', recursive=False):
            bits = []
            for c in li.children:
                if isinstance(c, Tag) and c.name == 'img':
                    bits.append(c.get('alt', '').strip())
                else:
                    bits.append(c.get_text() if isinstance(c, Tag) else str(c))
            items.append(sp(' '.join(b for b in bits if b.strip())).strip())
        e.replace_with('対応:' + '/'.join(items))
    for e in root.find_all('img'):
        e.replace_with('[IMG:' + e.get('alt', '') + ']')
    for e in root.find_all('p', class_='default'):
        e.insert(0, '既定値:')
    for e in root.find_all('dl'):
        for dt in e.find_all('dt', recursive=False):
            nxt = dt.find_next_sibling()
            if nxt is not None and nxt.name == 'dd':
                dt.append(':')
    for e in root.find_all('figcaption'):
        pass
    txt = ''.join(root.strings)
    return u.title + txt


def md_text(u, md):
    lines = md.split('\n')
    keep = []
    skip_rest = False
    for l in lines:
        if l.startswith('**カテゴリ:**'):
            continue
        if u.kind == 'index' and l == '## 一覧':
            skip_rest = True
        if skip_rest:
            continue
        keep.append(l)
    md = '\n'.join(keep)
    if u.deprecated:
        md = md.replace('!!! warning "非推奨"\n    この項目は非推奨である。', '')
    # admonition titles we inject
    html = markdown.markdown(md, extensions=EXT)
    s = BeautifulSoup(html, 'lxml')
    for e in s.find_all('p', class_='admonition-title'):
        e.decompose()
    for e in s.find_all('img'):
        e.replace_with('[IMG:' + e.get('alt', '') + ']')
    # first h1 = title: keep as text
    return s.get_text()


def norm(s):
    return re.sub(r'\s+', '', s)


def first_diff(a, b):
    n = min(len(a), len(b))
    i = 0
    while i < n and a[i] == b[i]:
        i += 1
    return i


def run(stems):
    for s in stems:
        layout.layout_page(s)
    conv.FINAL = False
    for u in layout.ALL_UNITS:
        layout.render_unit(u)
    conv.FINAL = True
    bad = []
    for u in layout.ALL_UNITS:
        md = layout.render_unit(u)
        a = norm(src_text(u))
        b = norm(md_text(u, md))
        if a != b:
            i = first_diff(a, b)
            bad.append((u.path, i, a[max(0, i - 25):i + 40], b[max(0, i - 25):i + 40]))
    print(f'units={len(layout.ALL_UNITS)} mismatches={len(bad)}')
    for p, i, a, b in bad[:int(os.environ.get('SHOW', '25'))]:
        print('---', p, '@', i)
        print('  SRC:', a)
        print('  MD :', b)
    print('DROPPED:')
    for k, v in sorted(conv.DROPPED.items()):
        print('  ', k, v, conv.DROPPED_EX.get(k[1]))
    print('dup ids:', len(conv.REG.dups))
    for d in conv.REG.dups[:30]:
        print('  DUP', d)
    print('warnings', len(WARN))
    seen = set()
    for w in WARN:
        if w not in seen:
            seen.add(w)
            if len(seen) < 60:
                print('WARN', w)
    return bad


if __name__ == '__main__':
    stems = sys.argv[1:] or sorted(p.stem for p in SRC.glob('*.html') if p.stem not in SKIP_PAGES)
    run(stems)


def heading_ids(md):
    """{id: heading text} of the md as the site builds it (toc with the same slugify)"""
    from pymdownx.slugs import slugify
    m = markdown.Markdown(extensions=EXT + ['toc'], extension_configs={'toc': {'slugify': slugify(case='lower'), 'toc_depth': 6}})
    html = m.convert(md)
    s = BeautifulSoup(html, 'lxml')
    return {h['id']: re.sub(r'\s+', '', h.get_text()) for h in s.find_all(re.compile('^h[1-6]$')) if h.get('id')}


def check_anchors():
    mds = {u.path: layout.render_unit(u) for u in layout.ALL_UNITS}
    hid = {}
    def ids_of(p):
        if p not in hid:
            hid[p] = heading_ids(mds[p]) if p in mds else None
        return hid[p]
    bad = []
    # 1. every registered heading anchor exists and has the heading text of the source
    for (stem, i), (path, anchor) in conv.REG.ids.items():
        if anchor is None:
            continue
        ids = ids_of(path)
        if ids is None or anchor not in ids:
            bad.append(('missing-anchor', stem, i, path, anchor))
            continue
        want = conv.REG.htext.get((stem, i))
        if want is not None and re.sub(r'\s+', '', want) != ids[anchor]:
            bad.append(('wrong-heading', stem, i, path, anchor, want, ids[anchor]))
    # 2. every link with a fragment in the generated markdown points at an existing heading id
    link = re.compile(r'\]\(([^)#\s]*)#([^)\s]+)\)')
    for p, md in mds.items():
        for m in link.finditer(md):
            tgt, frag = m.group(1), urllib.parse.unquote(m.group(2))
            tp = p if not tgt else posixpath.normpath(posixpath.join(posixpath.dirname(p), tgt))
            if not tgt.endswith('.md') and tgt:
                continue
            ids = ids_of(tp)
            if ids is None or frag not in ids:
                bad.append(('dead-link-fragment', p, m.group(0)))
    print('anchor problems:', len(bad))
    for b in bad[:int(os.environ.get('SHOW', '25'))]:
        print('  ', b)
    return bad


if __name__ == '__main__' and os.environ.get('ANCHORS'):
    check_anchors()


def code_lines_source(u):
    """multi-line code examples of a unit's source: lists of non-blank stripped lines"""
    root = BeautifulSoup('<div></div>', 'lxml').div
    for n in u.nodes:
        root.append(copy.copy(n))
    found = []
    for e in root.find_all(['pre', 'code']):
        if e.name == 'code' and e.find_parent('pre') is not None:
            continue
        txt = conv.code_text(e)
        lines = [l.strip() for l in txt.split(chr(10)) if l.strip()]
        multi = (e.name == 'pre') or (e.find('br') is not None)
        if multi and len(lines) > 1:
            found.append(lines)
    return found


def md_fences(md):
    out, cur, fence = [], None, None
    for l in md.split(chr(10)):
        s = l.strip()
        if cur is None:
            if s.startswith('```') and not s.strip('`'):
                cur, fence = [], s
            elif s.startswith('```'):
                cur, fence = [], '```'
        elif s == fence or (s.startswith('```') and not s.strip('`')):
            out.append(cur)
            cur = None
        else:
            if s:
                cur.append(s)
    return out


def check_code_lines():
    bad = 0
    for u in layout.ALL_UNITS:
        want = code_lines_source(u)
        if not want:
            continue
        have = md_fences(layout.render_unit(u))
        for w in want:
            if w not in have:
                bad += 1
                if bad <= int(os.environ.get('SHOW', '25')):
                    print('  code-lines differ:', u.path, w[:2])
    print('code-line problems:', bad)

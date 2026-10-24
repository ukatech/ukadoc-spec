"""ukadoc manual/*.html -> ukadoc-spec Markdown (deterministic converter).

Usage: python conv.py [page ...]   (default: all pages)
Outputs into OUT, writes migration/id-map.json and per-dir .nav.yml.
"""
import re, sys, json, os, posixpath, urllib.parse, collections, shutil
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Tag
from pymdownx.slugs import slugify as _slugify

SRC = Path(r'C:\D_DRIVE\MyDocuments\GitHub\ukadoc\manual')
OUT = Path(os.environ.get('UKADOC_OUT', r'C:\D_DRIVE\MyDocuments\GitHub\ukadoc-spec'))
SLUG = _slugify(case='lower')

WARN = []
def warn(*a):
    WARN.append(' '.join(str(x) for x in a))

# ---------------------------------------------------------------- page table
# page stem -> (md dir or file, kind)
def page_target(stem):
    if stem == 'index':
        return ('INDEX.md', 'single')
    g, _, rest = stem.partition('_')
    rest = rest.replace('_', '-')
    if g == 'memo' and not rest:
        return ('memo/memo.md', 'single')
    if g == 'memo_shiorievent':
        pass
    if stem == 'memo_shiorievent':
        return ('memo/shiori-event.md', 'single')
    if g in ('manual', 'dev'):
        return (f'{g}/{rest}.md', 'single')
    if g in ('descript', 'list', 'spec'):
        return (f'{g}/{rest}', 'dir')
    raise KeyError(stem)

SKIP_PAGES = {'navigation', 'sidemenu'}

# ---------------------------------------------------------------- helpers
def sp(s):  # collapse html whitespace
    return re.sub(r'[ \t\r\n\f]+', ' ', s)

SPECIAL_SLUG = {'\\': '', '!': '-bang-', '*': '-star-', '%': '-pct-', '&': '-amp-', '?': '-q-',
                '+': '-plus-', '=': '-eq-', '#': '-hash-', '@': '-at-', '/': '-', '~': '-tilde-'}

def make_slug(text):
    out = []
    for ch in text:
        if ch in SPECIAL_SLUG:
            out.append(SPECIAL_SLUG[ch])
        elif re.match(r'[A-Za-z0-9._]', ch):
            out.append(ch)
        else:
            out.append('-')
    s = ''.join(out)
    s = re.sub(r'-{2,}', '-', s).strip('-.')
    s = re.sub(r'\.{2,}', '.', s)
    return s[:80].strip('-.')

def text_of(el):
    return sp(el.get_text()).strip()

# ---------------------------------------------------------------- escaping
TAG_RE = re.compile(r'(?<![A-Za-z0-9])\\(?:!\[[^\]\n]*\]|(?:_{1,2}[A-Za-z0-9!*&-]?|[A-Za-z0-9!*&-])(?:\[[^\]\n]*\])?)')

TAG_RUN_RE = re.compile('(?:' + TAG_RE.pattern + ')+')

def codespan(s):
    if not s:
        return ''
    n = 1
    while '`' * n in s:
        n += 1
    f = '`' * n
    if s.startswith('`') or s.endswith('`') or s.startswith(' ') or s.endswith(' '):
        return f'{f} {s} {f}'
    return f'{f}{s}{f}'

def esc_plain(s, cell=False):
    s = s.replace('\\', '\\\\')
    s = re.sub(r'([`*\[\]>{}])', r'\\\1', s)
    s = re.sub(r'&(#?\w+;)', r'&amp;\1', s)
    s = s.replace('<', '&lt;')
    # underscores: escape unless between ASCII alnum
    s = re.sub(r'(?<![A-Za-z0-9])_|_(?![A-Za-z0-9])', r'\\_', s)
    if cell:
        s = s.replace('|', '\\|')
    return s

def esc_text(s, cell=False):
    """escape a text run; wrap sakura script tags in code spans"""
    out = []
    pos = 0
    for m in TAG_RUN_RE.finditer(s):
        out.append(esc_plain(s[pos:m.start()], cell))
        t = m.group(0)
        out.append(codespan(t).replace('|', '\\|') if cell else codespan(t))
        pos = m.end()
    out.append(esc_plain(s[pos:], cell))
    return ''.join(out)

def esc_linestart(line):
    return re.sub(r'^(\s*)([-+]\s|\d+[.)]\s|#{1,6}(?:\s|$)|>|={3,}|-{3,}|\*{3,})',
                  lambda m: m.group(1) + '\\' + m.group(2), line)

# ---------------------------------------------------------------- link resolver
class Registry:
    """id map: (page_stem, id) -> (md_path, anchor|None)"""
    def __init__(self):
        self.ids = {}
        self.page_path = {}      # stem -> md path of page main file
        self.dups = []
        self.htext = {}      # (stem, id) -> plain text of the heading the id points at
    def add(self, stem, id_, path, anchor, htext=None):
        if htext is not None and not FINAL and (stem, id_) not in self.ids:
            self.htext[(stem, id_)] = htext
        if FINAL:
            return
        k = (stem, id_)
        if k in self.ids:
            if self.ids[k][0] != path:
                self.dups.append((stem, id_, self.ids[k][0], path))
            return
        self.ids[k] = (path, anchor)

REG = Registry()
FINAL = False  # second pass: resolve links

def rel(from_path, to_path):
    d = posixpath.dirname(from_path) or '.'
    r = posixpath.relpath(to_path, d)
    return r

SITE_RE = re.compile(r'^https?://ssp\.shillest\.net/ukadoc/manual/?(.*)$')

# known typos in the source HTML (original page stem, href unquoted) -> corrected href
HREF_FIX = {
    ('dev_nar', 'chapterEX2'): '#chapterEX2',
    ('dev_shell', 'chapter=3-2'): '#chapter3-2',
    ('dev_shell', '#chapter5'): '#chapter3',
    ('manual_directory', 'descript_install.html#developter_options.txt'): 'descript_install.html#developer_options.txt',
    ('manual_shell', 'descript_shell_surfaces.html#element*,パターン定義,ファイル名,X座標,Y座標'):
        'descript_shell_surfaces.html#element*,描画メソッド,ファイル名,X座標,Y座標',
}
HREF_FIX[('descript_shell_surfaces', '#animation*.pattern*,描画メソッド,サーフェスID,ウェイト,X座標,Y座標')] = \
    '#animation*.pattern*,描画メソッド,サーフェス番号,ウェイト,X座標,Y座標'
HREF_FIX[('list_propertysystem', '#currentghost.sound(要素名).index(ID).サウンドプロパティ名')] = \
    '#currentghost.sound.index(ID).サウンドプロパティ名'

def resolve_href(href, stem, cur_path):
    href = href.strip()
    href = HREF_FIX.get((stem, urllib.parse.unquote(href)), href)
    m = SITE_RE.match(href)
    if m:
        href = m.group(1) or 'index.html'
        if href.startswith('#'):
            href = 'index.html' + href
    if re.match(r'^[a-z][a-z0-9+.-]*:', href, re.I) or href.startswith('//'):
        return href
    if href.startswith('./'):
        href = href[2:]
    fpart, _, frag = href.partition('#')
    frag = urllib.parse.unquote(frag)
    if not fpart:
        pstem = stem
    elif fpart.endswith('.html'):
        pstem = fpart[:-5]
    else:
        # assets etc. (image/xxx.png, base.css)
        if fpart.startswith('image/'):
            return rel(cur_path, 'assets/' + fpart) + (('#' + frag) if frag else '')
        warn('odd-href', cur_path, href)
        return href
    if pstem in SKIP_PAGES:
        return href
    if not FINAL:
        return 'x.md'
    if frag:
        t = REG.ids.get((pstem, frag))
        if t:
            path, anchor = t
            return rel(cur_path, path) + (('#' + anchor) if anchor else '')
        warn('unresolved-id (linked to page)', cur_path, href)
    mp = REG.page_path.get(pstem)
    if not mp:
        warn('unresolved-page (link removed)', cur_path, href)
        return None
    return rel(cur_path, mp)

# ---------------------------------------------------------------- renderer
class Ctx:
    def __init__(self, stem, path):
        self.stem = stem
        self.path = path
        self.anchor = None
        self.anchors = collections.Counter()
        self.level = 1
        self.cell = False

    def note_id(self, el):
        i = el.get('id') if isinstance(el, Tag) else None
        if i:
            REG.add(self.stem, i, self.path, self.anchor)

    def heading_anchor(self, text, level=None):
        base = SLUG(text, '-')
        n = self.anchors[base]
        self.anchors[base] += 1
        a = base if n == 0 else f'{base}_{n}'
        return a

DROP_TAGS = {'script', 'style', 'textarea', 'iframe', 'header', 'footer', 'select', 'button', 'meter', 'link', 'meta', 'noscript', 'form', 'input'}

def inline(node, cx):
    if isinstance(node, NavigableString):
        if node.__class__.__name__ in ('Comment', 'Doctype', 'ProcessingInstruction', 'Declaration'):
            return ''
        return esc_text(sp(str(node)), cx.cell)
    if not isinstance(node, Tag):
        return ''
    n = node.name
    cx.note_id(node)
    if n in DROP_TAGS:
        return ''
    if n == 'br':
        return '<br />\n' if not cx.cell else '<br>'
    classes = node.get('class', [])
    inner = lambda: ''.join(inline(c, cx) for c in node.children)
    if n == 'a':
        href = node.get('href')
        t = inner()
        if href:
            u = resolve_href(href, cx.stem, cx.path)
            if u is None:
                return t
            u = u.replace(' ', '%20').replace('(', '%28').replace(')', '%29')
            return f'[{t}]({u})'
        return t
    if n == 'code':
        if node.find('br') is not None:
            warn('inline-code-with-br (joined with spaces)', cx.path, sp(node.get_text())[:40])
        return codespan(sp(node.get_text())) .replace('|', '\\|') if cx.cell else codespan(sp(node.get_text()))
    if n in ('em', 'i'):
        if 'filename' in classes:
            return codespan(sp(node.get_text()))
        return wrap_mark(inner(), '*')
    if n in ('strong', 'b'):
        return wrap_mark(inner(), '**')
    if n in ('del', 'ins', 'sub', 'sup'):
        return f'<{n}>{inner()}</{n}>'
    if n == 'img':
        return img_md(node, cx)
    if n in ('span', 'time', 'u', 'small', 'font', 'abbr', 'q', 'mark', 'label', 'wbr', 'rt', 'rp', 'ruby'):
        return inner()
    if n in ('p', 'div', 'section', 'ul', 'ol', 'dl', 'table', 'pre', 'li', 'dd', 'dt', 'figure', 'h1', 'h2', 'h3', 'aside', 'nav'):
        # block inside inline context (stray markup): flatten
        warn('block-in-inline', cx.path, n)
        return ' '.join(x for x in (inline(c, cx) for c in node.children) if x.strip())
    warn('unknown-inline', cx.path, n)
    return inner()

def wrap_mark(s, m):
    if not s.strip():
        return s
    lead = len(s) - len(s.lstrip())
    trail = len(s) - len(s.rstrip())
    core = s.strip()
    return s[:lead] + m + core + m + (s[len(s) - trail:] if trail else '')

def img_md(node, cx):
    src = node.get('src', '')
    alt = node.get('alt', '')
    u = resolve_href(src, cx.stem, cx.path)
    return f'![{esc_plain(alt)}]({u})'

def para(nodes, cx):
    """render inline nodes as one paragraph string (br -> '<br />\\n')"""
    s = ''.join(inline(n, cx) for n in nodes)
    s = s.replace('\xa0', '\xa0')
    # tidy spaces around forced breaks
    s = re.sub(r' *<br />\n *', '<br />\n', s)
    lines = [esc_linestart(l) if i else esc_linestart(l.lstrip()) for i, l in enumerate(s.split('\n'))]
    s = '\n'.join(l.rstrip() if not l.endswith('<br />') else l for l in lines)
    return s.strip()

BLOCK_NAMES = {'p', 'div', 'section', 'ul', 'ol', 'dl', 'table', 'pre', 'figure', 'h1', 'h2', 'h3', 'h4', 'aside', 'nav',
               'hr', 'main', 'article', 'blockquote', 'figcaption', 'dd', 'dt', 'li', 'tbody', 'thead', 'tr'}

def has_block_child(el):
    return any(isinstance(c, Tag) and c.name in BLOCK_NAMES for c in el.children)

def heading(text_md, level):
    return '#' * min(level, 6) + ' ' + text_md

def heading_text_md(el, cx):
    old = cx.cell
    cx.cell = False
    s = ''.join(inline(c, cx) for c in el.children)
    cx.cell = old
    s = sp(s.replace('<br />\n', ' ')).strip()
    return s

def baseware_md(ul, cx):
    items = []
    for li in ul.find_all('li', recursive=False):
        parts = []
        for c in li.children:
            if isinstance(c, Tag) and c.name == 'img':
                parts.append(c.get('alt', '').strip())
            else:
                parts.append(inline(c, cx) if not isinstance(c, Tag) or c.name != 'img' else '')
        t = sp(' '.join(x for x in parts if x.strip()))
        items.append(t.strip())
    return '**対応:** ' + ' / '.join(items)

def blocks(nodes, cx, lvl):
    """render a sequence of nodes into list of block strings"""
    out = []
    cur = lvl
    buf = []   # pending inline nodes
    def flush():
        nonlocal buf
        if buf:
            s = para(buf, cx)
            if s:
                out.append(s)
            buf = []
    for n in nodes:
        if isinstance(n, NavigableString):
            if n.__class__.__name__ in ('Comment', 'Doctype'):
                continue
            buf.append(n)
            continue
        if not isinstance(n, Tag):
            continue
        if n.name in DROP_TAGS:
            continue
        if n.name not in BLOCK_NAMES and n.name != 'img':
            buf.append(n)
            continue
        if n.name == 'img':
            buf.append(n)
            continue
        flush()
        if n.name in ('h1', 'h2', 'h3', 'h4'):
            out.extend(block(n, cx, lvl))
            if n.name != 'h1':
                cur = lvl + int(n.name[1]) - 1   # sections that follow an h2 nest below it
        else:
            out.extend(block(n, cx, cur))
    flush()
    return out

def indent(s, n=4):
    pad = ' ' * n
    return '\n'.join((pad + l) if l.strip() else l for l in s.split('\n'))

def list_md(el, cx, lvl):
    ordered = el.name == 'ol'
    items = []
    k = 0
    for li in el.find_all('li', recursive=False):
        cx.note_id(li)
        bl = blocks(li.children, cx, lvl)
        if not bl:
            bl = ['']
        k += 1
        mark = f'{k}. ' if ordered else '- '
        first = bl[0]
        rest = bl[1:]
        body = first
        for r in rest:
            body += '\n\n' + r
        lines = body.split('\n')
        pad = ' ' * len(mark)
        txt = mark + lines[0]
        for l in lines[1:]:
            txt += '\n' + ((pad + l) if l.strip() else l)
        items.append(txt)
    return (NL2 if any(NL2 in x for x in items) else NL).join(items)

def dl_md(el, cx, lvl):
    items = []
    cur = None
    for c in el.children:
        if not isinstance(c, Tag):
            continue
        cx.note_id(c)
        if c.name == 'dt':
            t = heading_text_md(c, cx)
            cur = [t, []]
            items.append(cur)
        elif c.name == 'dd':
            if cur is None:
                cur = ['', []]
                items.append(cur)
            cur[1].extend(blocks(c.children, cx, lvl))
        elif c.name in DROP_TAGS:
            continue
        else:
            warn('dl-child', cx.path, c.name)
    out = []
    for t, bl in items:
        if bl:
            if BLOCKISH_RE.match(bl[0]):
                txt = f'- **{t}**:' if t else '-'
                for b in bl:
                    txt += NL2 + indent(b, 2)
            else:
                lines = (f'- **{t}**: ' + bl[0] if t else '- ' + bl[0]).split(NL)
                txt = lines[0]
                for l in lines[1:]:
                    txt += NL + ('  ' + l if l.strip() else l)
                for b in bl[1:]:
                    txt += NL2 + indent(b, 2)
        else:
            txt = f'- **{t}**' if t else '-'
        out.append(txt)
    return (NL2 if any(NL2 in x for x in out) else NL).join(out)

NL = chr(10)
NL2 = chr(10) * 2
BLOCKISH_RE = re.compile(r'^(\s*[-+*] |\d+\. |\||```|~~~|#{1,6} |!!! |<)')

def table_md(el, cx, lvl):
    rows = []
    for tr in el.find_all('tr'):
        cells = []
        for td in tr.find_all(['td', 'th'], recursive=False):
            old = cx.cell
            cx.cell = True
            s = ' '.join(x for x in [''.join(inline(c, cx) if not (isinstance(c, Tag) and c.name in BLOCK_NAMES) else cell_block(c, cx) for c in td.children)] if x)
            cx.cell = old
            s = sp(s).replace('\n', ' ').strip()
            cells.append((s, td.name == 'th'))
        rows.append(cells)
    if not rows:
        return ''
    w = max(len(r) for r in rows)
    def fmt(r):
        r = [c[0] for c in r] + [''] * (w - len(r))
        return '| ' + ' | '.join(r) + ' |'
    head_rows = 1
    out = [fmt(rows[0]), '| ' + ' | '.join(['---'] * w) + ' |']
    for r in rows[1:]:
        out.append(fmt(r))
    return '\n'.join(out)

def cell_block(c, cx):
    # nested block inside a table cell: flatten with <br>
    parts = []
    if c.name in ('ul', 'ol'):
        for li in c.find_all('li', recursive=False):
            parts.append('・' + ''.join(inline(x, cx) for x in li.children))
        return '<br>'.join(parts)
    return ''.join(inline(x, cx) for x in c.children) + '<br>'

def code_block(text, lang=''):
    text = text.replace('\r\n', '\n').strip('\n')
    fence = '```'
    while fence in text:
        fence += '`'
    return f'{fence}{lang}\n{text}\n{fence}'

DROPPED = collections.Counter()
DROPPED_EX = {}

def drop(el, cx):
    k = el.name + ('.' + '.'.join(el.get('class', [])) if el.get('class') else '')
    DROPPED[(cx.path.split('/')[0], k)] += 1
    DROPPED_EX.setdefault(k, (cx.path, sp(el.get_text())[:80]))
    return []

def code_text(el):
    """text of a pre / code element, <br> as newline"""
    import copy
    c = copy.copy(el)
    for br in c.find_all('br'):
        br.replace_with(chr(10))
    return c.get_text()

def block(el, cx, lvl):
    if el.name not in ('section', 'h1', 'h2', 'h3', 'h4'):
        cx.note_id(el)   # headings / sections register themselves after their heading is emitted
    n = el.name
    classes = el.get('class', [])
    if n in DROP_TAGS:
        return drop(el, cx)
    if n == 'nav':
        if 'menu-header' in classes or 'sidebar' in classes:
            return drop(el, cx)
        return container(el, cx, lvl)
    if n == 'p':
        if 'banner' in classes or 'author' in classes:
            return drop(el, cx)
        if has_block_child(el):
            return container(el, cx, lvl)
        if any(isinstance(c, Tag) and c.name == 'code' and c.find('br') is not None for c in el.children):
            # a multi-line example written as <p><code>line<br />line</code> note</p>:
            # the code becomes a fenced block, the rest stays as paragraphs around it
            res, pend = [], []
            for c in el.children:
                if isinstance(c, Tag) and c.name == 'code' and c.find('br') is not None:
                    if pend:
                        t = para(pend, cx)
                        if t:
                            res.append(t)
                        pend = []
                    res.append(code_block(code_text(c)))
                else:
                    pend.append(c)
            if pend:
                t = para(pend, cx)
                if t:
                    res.append(t)
            return res
        s = para(el.children, cx)
        if not s:
            return []
        if 'default' in classes:
            s = '**既定値:** ' + s
        return [s]
    if n in ('h1', 'h2', 'h3', 'h4'):
        t = heading_text_md(el, cx)
        if not t:
            return []
        lv = lvl + max(0, int(n[1]) - 2)
        plain = text_of(el)
        a = cx.heading_anchor(plain)
        cx.anchor = a
        if el.get('id'):
            REG.add(cx.stem, el['id'], cx.path, a, plain)
        return [heading(t, lv)]
    if n == 'section':
        return section_md(el, cx, lvl)
    if n == 'ul':
        if 'supported-baseware' in classes:
            return [baseware_md(el, cx)]
        return [list_md(el, cx, lvl)]
    if n == 'ol':
        return [list_md(el, cx, lvl)]
    if n == 'dl':
        return [dl_md(el, cx, lvl)]
    if n == 'table':
        return [table_md(el, cx, lvl)]
    if n == 'pre':
        return [code_block(code_text(el))]
    if n == 'hr':
        return ['---']
    if n == 'figcaption':
        s = para(el.children, cx)
        return [f'*{s}*'] if s else []
    if n in ('div', 'aside', 'figure', 'main', 'article', 'blockquote', 'dd', 'dt', 'li', 'tbody', 'thead', 'tr'):
        if n == 'aside' or ('passage' in classes and ('hint' in classes or 'note' in classes)):
            return admonition(el, cx, lvl)
        return container(el, cx, lvl)
    warn('unknown-block', cx.path, n)
    return container(el, cx, lvl)

def admonition(el, cx, lvl):
    classes = el.get('class', [])
    kind = 'tip' if 'hint' in classes else 'note'
    title = {'hint': 'ヒント', 'note': '注'}['hint' if 'hint' in classes else 'note']
    inner = blocks(el.children, cx, lvl)
    body = '\n\n'.join(inner)
    return [f'!!! {kind} "{title}"\n\n' + indent(body, 4)]

def container(el, cx, lvl):
    return blocks(el.children, cx, lvl)

def section_md(sec, cx, lvl):
    """sec rendered at heading level `lvl` (its own h1 gets lvl)"""
    classes = sec.get('class', [])
    out = []
    # section.code: legend sample
    if 'code' in classes:
        h = sec.find('h1', recursive=False)
        if h:
            a = cx.heading_anchor(text_of(h))
            cx.anchor = a
            for e in (sec, h):
                if e.get('id'):
                    REG.add(cx.stem, e['id'], cx.path, a, text_of(h))
            out.append(heading(heading_text_md(h, cx), lvl))
        else:
            cx.note_id(sec)
        for c in sec.children:
            if isinstance(c, Tag) and c.name != 'h1':
                if c.name == 'p' and len([x for x in c.children if isinstance(x, Tag)]) == 1 and \
                        c.find('code') is not None and not text_outside_code(c):
                    code = c.find('code')
                    lang = 'sakurascript' if (code.get('type') or '').lower() == 'sakurascript' else ''
                    out.append(code_block(code_text(code), lang))
                else:
                    out.extend(block(c, cx, lvl + 1))
        return out
    first_h = None
    for c in sec.children:
        if isinstance(c, Tag) and c.name == 'h1':
            first_h = c
            break
    kids = list(sec.children)
    # emit heading first (the section id points at its heading)
    if first_h is not None:
        t = heading_text_md(first_h, cx)
        a = cx.heading_anchor(text_of(first_h))
        cx.anchor = a
        if sec.get('id'):
            REG.add(cx.stem, sec['id'], cx.path, a, text_of(first_h))
        if first_h.get('id'):
            REG.add(cx.stem, first_h['id'], cx.path, a, text_of(first_h))
        out.append(heading(t, lvl))
        kids = [k for k in kids if k is not first_h]
    else:
        cx.note_id(sec)
    sub = lvl + 1 if first_h is not None else lvl
    out.extend(blocks_with_h(kids, cx, sub, lvl))
    return out

def text_outside_code(p):
    for c in p.children:
        if isinstance(c, NavigableString) and str(c).strip():
            return True
    return False

def blocks_with_h(kids, cx, sublvl, lvl):
    """children of a section whose own heading is at `lvl`: further direct h1s are siblings of that
    heading (same level); nested sections and h2s are one level below"""
    out = []
    buf = []
    def flush():
        nonlocal buf
        if buf:
            out.extend(blocks(buf, cx, sublvl))
            buf = []
    for k in kids:
        if isinstance(k, Tag) and k.name == 'h1':
            flush()
            out.extend(block(k, cx, lvl))
        else:
            buf.append(k)
    flush()
    return out

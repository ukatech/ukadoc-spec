"""layout / driver part of the converter (imports conv.py)."""
import conv
from conv import *


class Unit:
    def __init__(self, path, title, kind, stem):
        self.path = path
        self.title = title            # plain text
        self.kind = kind              # entry | section | note | index | page
        self.stem = stem
        self.nodes = []
        self.category = None
        self.deprecated = False
        self.children = []            # for index
        self.dt = None
        self.dirname = None


def slug_ja(s):
    s = re.sub(r'[\s\\/:*?"<>|「」『』（）()\[\]{},、。・！!＆&％%=＝+＋~～#＃@＠.．]+', '-', s)
    s = re.sub(r'-{2,}', '-', s).strip('-')
    return s[:60].strip('-')


def ascii_name(title):
    """ASCII name for a category / note from its title (names.NAMES; ASCII-only titles are slugged)"""
    from names import NAMES
    if title in NAMES:
        return NAMES[title]
    s = slug_ja(title)
    if s and s.isascii():
        return s.lower()
    raise SystemExit(f'no ASCII name for title: {title!r} (add it to names.py)')


def clean_id(i):
    return bool(i) and re.fullmatch(r'[A-Za-z][A-Za-z0-9._-]*', i) is not None


class NameBook:
    """per-directory unique (case-insensitive) names"""
    def __init__(self):
        self.used = collections.defaultdict(set)

    def get(self, d, base, ext):
        base = base or 'item'
        if base.lower() == 'index' and ext == '.md':
            base = 'index-item'
        name = base
        n = 1
        while (name + ext).lower() in self.used[d]:
            n += 1
            name = f'{base}-{n}'
        self.used[d].add((name + ext).lower())
        return name + ext


NB = NameBook()
ALL_UNITS = []
ENTRY_COUNT = collections.Counter()


def is_entry_dl(el):
    return (isinstance(el, Tag) and el.name == 'dl' and el.get('id') is not None
            and len(el.find_all('dt', recursive=False)) == 1 and len(el.find_all('dd', recursive=False)) == 1
            and el.find('dt', class_='entry', recursive=False) is not None)


def has_entries(el):
    return isinstance(el, Tag) and any(is_entry_dl(d) for d in el.find_all('dl'))


def first_h(sec):
    for c in sec.children:
        if isinstance(c, Tag) and c.name in ('h1', 'h2'):
            return c
    return None


def register_root_ids(stem, el, path):
    cands = [el]
    if el.name == 'section' and first_h(el) is not None:
        cands.append(first_h(el))
    for e in cands:
        i = e.get('id')
        if i:
            REG.add(stem, i, path, None)


def make_entry_unit(dl, d, stem, cats):
    dt = dl.find('dt', class_='entry', recursive=False)
    dds = dl.find_all('dd', recursive=False)
    dts = dl.find_all('dt', recursive=False)
    if len(dts) != 1 or len(dds) != 1:
        warn('entry-shape', stem, dl.get('id'), len(dts), len(dds))
    text = text_of(dt)
    i = dl.get('id')
    if clean_id(i):
        base = i
    else:
        key = text if text.startswith(('\\', '%')) else re.split(r'[,\s]', text)[0]
        base = make_slug(key)
    if not base:
        base = 'entry'
    name = NB.get(d, base, '.md')
    u = Unit(f'{d}/{name}', text, 'entry', stem)
    u.nodes = list(dds[0].children) if dds else []
    u.category = ' > '.join(cats) if cats else None
    u.deprecated = 'deprecated' in dt.get('class', [])
    u.dt = dt
    ENTRY_COUNT[stem] += 1
    register_root_ids(stem, dl, u.path)
    ALL_UNITS.append(u)
    return u


def sect_title(sec, default):
    h = first_h(sec)
    return text_of(h) if h is not None else default


def make_section_unit(sec, d, stem, counter, kind='section'):
    h = first_h(sec)
    t = text_of(h) if h is not None else None
    i = sec.get('id') or (h.get('id') if h is not None else None)
    if clean_id(i):
        base = i.lower()
    elif t and slug_ja(t):
        base = ascii_name(t)
    else:
        counter[0] += 1
        base = f'note-{counter[0]}'
    name = NB.get(d, base, '.md')
    u = Unit(f'{d}/{name}', t or '補足', kind, stem)
    u.nodes = [c for c in sec.children if c is not h]
    register_root_ids(stem, sec, u.path)
    ALL_UNITS.append(u)
    return u


def make_loose_unit(nodes, d, stem, counter):
    counter[0] += 1
    name = NB.get(d, f'note-{counter[0]}', '.md')
    u = Unit(f'{d}/{name}', '補足', 'note', stem)
    u.nodes = list(nodes)
    ALL_UNITS.append(u)
    return u


def real_nodes(nodes):
    return [n for n in nodes
            if isinstance(n, Tag) or (isinstance(n, NavigableString) and str(n).strip()
                                      and n.__class__.__name__ not in ('Comment', 'Doctype'))]


def build_dir(children, d, stem, idx, cats):
    counter = [0]
    loose = []
    seen = [False]

    def flush_loose():
        nonlocal loose
        if real_nodes(loose):
            if not seen[0]:
                idx.nodes.extend(loose)
            else:
                idx.children.append(make_loose_unit(loose, d, stem, counter))
        loose = []

    for ch in children:
        if not isinstance(ch, Tag):
            loose.append(ch)
            continue
        if ch.name in DROP_TAGS or ch.name == 'nav':
            continue
        if is_entry_dl(ch):
            flush_loose()
            idx.children.append(make_entry_unit(ch, d, stem, cats))
            seen[0] = True
        elif ch.name == 'section' and has_entries(ch):
            flush_loose()
            t = sect_title(ch, 'カテゴリ')
            h = first_h(ch)
            i = ch.get('id') or (h.get('id') if h is not None else None)
            base = i.lower() if clean_id(i) else (ascii_name(t) if slug_ja(t) else f'category-{len(idx.children) + 1}')
            dname = NB.get(d, base, '')
            sub = f'{d}/{dname}'
            u = Unit(f'{sub}/index.md', t, 'index', stem)
            u.dirname = sub
            ALL_UNITS.append(u)
            register_root_ids(stem, ch, u.path)
            rest = [c for c in ch.children if c is not h]
            build_dir(rest, sub, stem, u, cats + [t])
            idx.children.append(u)
            seen[0] = True
        elif ch.name == 'section':
            flush_loose()
            idx.children.append(make_section_unit(ch, d, stem, counter))
            seen[0] = True
        else:
            loose.append(ch)
    flush_loose()


def load_html(stem):
    """read source HTML, repairing known defects (recorded in the migration notes)"""
    html = (SRC / f'{stem}.html').read_text(encoding='utf-8')
    if stem == 'manual_shell':
        # '<dl class="component"' lacks '>' and swallowed the first <dt> in browsers
        html = html.replace('<dl class="component"\n', '<dl class="component">\n', 1)
    if stem == 'dev_bind':
        # the second section also had id="chapter1" (the TOC links it as chapter2)
        html = html.replace('<section class="ordered" id="chapter1">', '<section class="ordered" id="chapter2">', 1)
    return html


def page_title(soup):
    t = soup.find('title')
    s = text_of(t) if t else ''
    return re.sub(r'^UKADOC Project\s*', '', s)


def layout_page(stem):
    html = load_html(stem)
    soup = BeautifulSoup(html, 'lxml')
    target, kind = page_target(stem)
    title = page_title(soup)
    cont = soup.find('div', class_='categories')
    if cont is not None:
        d = target
        idx = Unit(f'{d}/index.md', title, 'index', stem)
        idx.dirname = d
        ALL_UNITS.append(idx)
        REG.page_path[stem] = idx.path
        build_dir(list(cont.children), d, stem, idx, [])
        return idx
    main = soup.find('main')
    h = None
    if main is None:
        # spec_dll / spec_headline / spec_plugin: <h1 id="page-title">, nav, navigation-bar, then <div class="text">
        main = soup.find('div', class_='text')
        pt = soup.find('h1', id='page-title')
        if main is None or pt is None:
            raise SystemExit(f'{stem}: unknown page layout')
        title = text_of(pt)
    else:
        for c in main.children:
            if isinstance(c, Tag) and c.name == 'h1':
                h = c
                break
        if h is not None:
            title = text_of(h)
    if not target.endswith('.md'):
        target += '.md'
    u = Unit(target, title, 'page', stem)
    u.nodes = [c for c in main.children if c is not h]
    REG.page_path[stem] = u.path
    ALL_UNITS.append(u)
    return u


def render_unit(u):
    cx = Ctx(u.stem, u.path)
    out = []
    if u.kind == 'entry':
        tmd = heading_text_md(u.dt, cx)
    else:
        tmd = esc_text(sp(u.title).strip()) if u.title else ''
    cx.anchor = cx.heading_anchor(u.title)
    out.append('# ' + tmd)
    if u.deprecated:
        out.append('!!! warning "非推奨"\n    この項目は非推奨である。')
    if u.category:
        out.append('**カテゴリ:** ' + esc_text(u.category))
    out.extend(blocks(u.nodes, cx, 2))
    if u.kind == 'index' and u.children:
        out.append('## 一覧')
        lines = []
        for c in u.children:
            target = rel(u.path, c.path)
            lines.append(f'- [{esc_text(sp(c.title).strip())}]({target.replace(" ", "%20")})')
        out.append('\n'.join(lines))
    txt = '\n\n'.join(x for x in out if x.strip()) + '\n'
    return re.sub(r'\n{3,}', '\n\n', txt)


def nav_yml(u):
    """directory nav: index + non-entry children (entries are listed in index.md, kept out of the sidebar)"""
    lines = [f'title: {json.dumps(u.title, ensure_ascii=False)}', 'nav:', '  - index.md']
    for c in u.children:
        if c.kind == 'entry':
            continue
        if c.kind == 'index':
            lines.append(f'  - {posixpath.basename(posixpath.dirname(c.path))}')
        else:
            lines.append(f'  - {posixpath.basename(c.path)}')
    return NL.join(lines) + NL


def parse_sidemenu():
    """sidemenu.html -> [(group title, items)], item = (text, href) | (text, [items])"""
    soup = BeautifulSoup((SRC / 'sidemenu.html').read_text(encoding='utf-8'), 'lxml')

    def parse_ul(ul):
        items = []
        for li in ul.find_all('li', recursive=False):
            a = li.find('a', recursive=False)
            if a is not None:
                items.append((text_of(a), a.get('href')))
            else:
                sub = li.find('ul')
                items.append((text_of(li.find('p')), parse_ul(sub)))
        return items

    groups = []
    for sec in soup.find_all('section'):
        items = []
        for ul in sec.find_all('ul', recursive=False):
            items.extend(parse_ul(ul))
        groups.append((text_of(sec.find('h1')), items))
    return groups


def index_toc(groups):
    out = ['## 目次', '']

    def walk(items, depth):
        for t, v in items:
            pad = '  ' * depth
            if isinstance(v, list):
                out.append(f'{pad}- {esc_text(t)}')
                walk(v, depth + 1)
            else:
                u = resolve_href(v, 'sidemenu', 'INDEX.md')
                out.append(f'{pad}- [{esc_text(t)}]({u})' if u else f'{pad}- {esc_text(t)}')
    for g, items in groups:
        out.append(f'### {esc_text(g)}')
        out.append('')
        walk(items, 0)
        out.append('')
    return NL.join(out).rstrip() + NL


def root_nav(groups):
    lines = ['nav:', '  - index.md']

    def q(s):
        return json.dumps(s, ensure_ascii=False)

    def walk(items, depth):
        pad = '  ' * depth
        for t, v in items:
            if isinstance(v, list):
                lines.append(f'{pad}- {q(t)}:')
                walk(v, depth + 1)
                continue
            if v.startswith(('http://', 'https://')) and not SITE_RE.match(v):
                continue
            href = SITE_RE.match(v).group(1) if SITE_RE.match(v) else v
            if '#' in href:
                continue
            stem = href.replace('./', '').replace('.html', '')
            p = REG.page_path.get(stem)
            if not p:
                warn('nav-unresolved', v)
                continue
            target = posixpath.dirname(p) if p.endswith('/index.md') else p
            lines.append(f'{pad}- {q(t)}: {target}')

    for g, items in groups:
        lines.append(f'  - {q(g)}:')
        walk(items, 2)
    return NL.join(lines) + NL


def write(path, text):
    p = OUT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def main(argv):
    stems = argv or sorted(p.stem for p in SRC.glob('*.html') if p.stem not in SKIP_PAGES)
    for s in stems:
        layout_page(s)
    conv.FINAL = False
    for u in ALL_UNITS:
        render_unit(u)
    conv.FINAL = True
    files = {}
    for u in ALL_UNITS:
        files[u.path] = render_unit(u)
        if u.kind == 'index':
            files[u.dirname + '/.nav.yml'] = nav_yml(u)
    if 'index' in stems and 'sidemenu' not in stems:
        groups = parse_sidemenu()
        files['INDEX.md'] = files['INDEX.md'].rstrip(NL) + NL2 + index_toc(groups)
        files['.nav.yml'] = root_nav(groups)
    for k, v in files.items():
        write(k, v)
    img = OUT / 'assets' / 'image'
    img.mkdir(parents=True, exist_ok=True)
    for f in (SRC / 'image').iterdir():
        shutil.copy(f, img / f.name)
    idmap = {f'{s}#{i}': {'path': p, 'anchor': a} for (s, i), (p, a) in REG.ids.items()}
    write('migration/id-map.json', json.dumps(idmap, ensure_ascii=False, indent=1, sort_keys=True) + '\n')
    for s in stems:
        n = len(BeautifulSoup(load_html(s), 'lxml').select('dl[id]:has(> dt.entry)'))
        if n != ENTRY_COUNT[s]:
            warn('entry-count-mismatch', s, n, ENTRY_COUNT[s])
    print(f'units={len(ALL_UNITS)} files={len(files)} ids={len(REG.ids)} dups={len(REG.dups)}')
    for d in REG.dups[:40]:
        print('DUP', d)
    for w in WARN[:200]:
        print('WARN', w)
    print('warnings', len(WARN))


if __name__ == '__main__':
    main(sys.argv[1:])

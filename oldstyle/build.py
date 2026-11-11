"""旧版 UKADOC（ukatech/ukadoc の manual/*.html）の見た目と構造を模した静的サイトを _site_old/ に作る。

Zensical には頼らず、次の流れで作る。

1. scripts/prepare_site.py が作る _site_src/（「1 ディレクトリ 1 ページ」にまとめた Markdown）を読む
2. Python-Markdown で HTML にし、旧版の HTML の構造（list.css / base.css が前提にしている class と入れ子）に組み替える
3. 旧版のファイル名（descript_ghost.html など）・旧版の CSS・画像で出す。枠の頁（manual_* など）の上の帯と左のメニューは、
   iframe にせず、templates/navigation.html と sidemenu.html の断片を頁に埋め込む

使い方: python oldstyle/build.py [--no-prepare]
"""
import html as htmllib
import json
import os
import posixpath
import re
import shutil
import subprocess
import sys
import zipfile
from urllib.parse import unquote

import lxml.html
import markdown
from lxml import etree
from pymdownx.slugs import slugify

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..'))


def _lang_arg():
    """--lang=<コード>（例: en）。指定すると、i18n/<コード>/ の翻訳を重ねた版を _site_old/<コード>/ に出す。無ければ日本語版"""
    for a in sys.argv[1:]:
        if a.startswith('--lang='):
            return a.split('=', 1)[1]
    return None


LANG = _lang_arg()
# 翻訳版の言語（i18n/<コード>/ があるものだけ、日本語版のビルドの最後に続けてビルドする）。label は言語メニューの表示
LANGS = [('en', 'English'), ('zh-Hant', '繁體中文'), ('zh', '简体中文')]
SRC = os.path.join(ROOT, '_site_src' + (f'_{LANG}' if LANG else ''))
OUT = os.path.join(ROOT, '_site_old', *([LANG] if LANG else []))
STATIC = os.path.join(HERE, 'static')
TEMPLATES = os.path.join(HERE, 'templates')
I18N_TEMPLATES = os.path.join(ROOT, 'i18n', LANG, 'templates') if LANG else None
SITE_URL = 'https://ukatech.shillest.net/ukadoc-spec/'

# 構造の判定に使う日本語の語は、訳文でも原文のまま残す（翻訳のときに検査する）。表示のときだけ、ここで言語ごとの語に置き換える
LABELS = {
    'en': {'記述例': 'Example', '概要': 'Overview', '補足': 'Notes', '目次': 'Contents'},
    'zh-Hant': {'記述例': '記述範例', '概要': '概要', '補足': '補充', '目次': '目錄'},
    'zh': {'記述例': '编写示例', '概要': '概要', '補足': '补充', '目次': '目录'},
}


# 翻訳版で、その言語で書かれた原文そのもの（機械翻訳でない）の項目に付ける印（i18n/originals.json に登録したもの。prepare_site.py が見出しに orig-lang を付ける）
ORIG_BADGE = {
    'en': ('Original', 'Written in English by its author (not machine-translated)'),
    'zh-Hant': ('原文', '由作者以繁體中文撰寫（非機器翻譯）'),
    'zh': ('原文', '由作者以简体中文撰写（非机器翻译）'),
}


def orig_badge(head):
    """項目の見出し head が原文の項目なら、その印の span（<span class="ukadoc-orig-badge">）。そうでなければ None"""
    if 'orig-lang' not in classes(head) or LANG not in ORIG_BADGE:
        return None
    text, tip = ORIG_BADGE[LANG]
    span = new('span', 'ukadoc-orig-badge')
    span.set('title', tip)
    span.text = text
    return span


def available_langs():
    """言語メニューに出す言語のコード。日本語 + i18n/<コード>/ があるもの（LANGS の順）"""
    return ['ja'] + [code for code, _ in LANGS if os.path.isdir(os.path.join(ROOT, 'i18n', code))]


def label(ja):
    """構造の判定に使う日本語の語の、表示用の語（日本語版はそのまま）"""
    return LABELS.get(LANG, {}).get(ja, ja)

EXTENSIONS = ['tables', 'admonition', 'attr_list', 'md_in_html', 'mdx_truly_sane_lists',
              'pymdownx.superfences', 'pymdownx.highlight', 'toc']
EXT_CONFIG = {
    'pymdownx.highlight': {'pygments_lang_class': True, 'css_class': 'highlight', 'guess_lang': False},
    'toc': {'slugify': slugify(case='lower'), 'toc_depth': '1-6'},
}

BASEWARE = {'Materia': 'm', 'SSP': 's', 'CROW': 'c', 'Ninix': 'n'}
BASEWARE_PART = re.compile(r'^(Materia|SSP|CROW|Ninix)(?:\s+(.*))?$')
NEGATION = re.compile(r'非対応|未対応|廃止|not supported|unsupported|deprecated|discontinued|obsolete|不支援|不支持|廢止|废止', re.I)   # 後半は翻訳版（英語・中国語）の言い換え
REFERENCE = re.compile(r'^Reference(?:\d+|\*)(?:～\d*)?$')

# 旧版のファイル名と食い違うもの（新しい原稿のパス → 旧版のファイル名）
NAME_EXCEPTIONS = {
    'memo/memo.md': 'memo.html',
    'memo/shiori-event.md': 'memo_shiorievent.html',
}
BUNDLE_DIRS = ('descript', 'list', 'spec')

ERRORS = []


def error(msg):
    ERRORS.append(msg)
    print(f'エラー: {msg}', file=sys.stderr)


# ---------------------------------------------------------------- 名前

def out_name(md_rel):
    """_site_src/ のなかの .md のパス → 旧版のファイル名（出力先は OUT 直下に平らに置く）"""
    if md_rel in NAME_EXCEPTIONS:
        return NAME_EXCEPTIONS[md_rel]
    if md_rel == 'index.md':
        return 'index.html'
    parts = md_rel[:-3].split('/')
    if parts[-1] == 'index':
        parts = parts[:-1]
    return '_'.join(p.replace('-', '_') for p in parts) + '.html'


def page_kind(md_rel):
    """list = descript_/list_/spec_ のまとめた頁（list.css）、spec = 単独の spec_*.md（組み方は違うが、見た目は list と同じく list.css）、frame = それ以外（base.css）"""
    parts = md_rel.split('/')
    if len(parts) >= 3 and parts[0] in BUNDLE_DIRS and parts[-1] == 'index.md' and len(parts) == 3:
        return 'list'
    if parts[0] == 'spec' and len(parts) == 2:
        return 'spec'
    return 'frame'


# ---------------------------------------------------------------- Markdown → lxml

def convert(text):
    md = markdown.Markdown(extensions=EXTENSIONS, extension_configs=EXT_CONFIG)
    body = md.convert(text)
    return lxml.html.fragment_fromstring(body, create_parent='div')


def inner_html(el):
    s = htmllib.escape(el.text or '', quote=False) if False else (el.text or '')
    s = htmllib.escape(s, quote=False)
    for c in el:
        s += lxml.html.tostring(c, encoding='unicode')
    return s


def title_html(el):
    """見出しの中身。コードスパンは旧版どおり素の字にする（等幅だとバックスラッシュが円記号に見えるため）。
    翻訳版では、構造の判定のために訳文に日本語のまま残した語（記述例・概要・補足）を、その言語の語にする"""
    return localize_heading(re.sub(r'</?code[^>]*>', '', inner_html(el)), text_of(el))


def localize_heading(html, text):
    """翻訳版で、構造の判定のために訳文に日本語のまま残した見出しの語（記述例・概要・補足）を、その言語の語にする。
    text は見出しの字（html の元）"""
    if LANG:
        for ja, local in LABELS.get(LANG, {}).items():
            if (text == ja) or (ja == '記述例' and text.startswith(ja)):
                html = html.replace(ja, local, 1)
    return html


def set_inner(el, html_text):
    for c in list(el):
        el.remove(c)
    el.text = None
    frag = lxml.html.fragment_fromstring(html_text or '', create_parent='div')
    el.text = frag.text
    for c in list(frag):
        el.append(c)


def new(tag, cls=None, **attrs):
    el = etree.Element(tag)
    if cls:
        el.set('class', cls)
    for k, v in attrs.items():
        el.set(k.replace('_', '-'), v)
    return el


def text_of(el):
    return ''.join(el.itertext()).strip()


def classes(el):
    return (el.get('class') or '').split()


def is_heading(el):
    return isinstance(el.tag, str) and re.fullmatch(r'h[1-6]', el.tag) is not None


def level(el):
    return int(el.tag[1])


def detach(el):
    """el を親から外して返す（tail は捨てる。lxml は tail を一緒に外すので、残した文字が消えないよう空にする）"""
    el.tail = None
    parent = el.getparent()
    if parent is not None:
        parent.remove(el)
    return el


def clean_tail(el):
    el.tail = None
    return el


# ---------------------------------------------------------------- リンク

def mark_sakurascript(root):
    """さくらスクリプトの記述例のコードに type=SakuraScript を付ける（sakura_player.js が実行ボタンを付ける目印）"""
    for div in root.iter('div'):
        cls = classes(div)
        if 'highlight' in cls and ('language-ss' in cls or 'language-sakurascript' in cls):
            for code in div.iter('code'):
                code.set('type', 'SakuraScript')


def resolve_links(root, md_rel, known):
    """リンクと画像の参照を、旧版のファイル名・image/ に直す"""
    here = posixpath.dirname(md_rel)
    for a in root.iter('a'):
        href = a.get('href')
        if not href or re.match(r'^[a-z][a-z0-9+.-]*:', href, re.I):
            if href and href.startswith(('http://', 'https://')):
                pass
            continue
        path, _, frag = href.partition('#')
        if path == '':
            continue
        target = posixpath.normpath(posixpath.join(here, unquote(path)))
        if target.endswith('.md'):
            if target not in known:
                error(f'{md_rel}: リンク先 {target} が無い')
                continue
            a.set('href', out_name(target) + (('#' + frag) if frag else ''))
        elif target.startswith('assets/image/'):
            a.set('href', 'image/' + target[len('assets/image/'):] + (('#' + frag) if frag else ''))
        elif target == 'llms.txt':
            pass
        else:
            a.set('href', target + (('#' + frag) if frag else ''))
    for img in root.iter('img'):
        src = img.get('src')
        if not src or re.match(r'^[a-z][a-z0-9+.-]*:', src, re.I):
            continue
        target = posixpath.normpath(posixpath.join(here, unquote(src)))
        if target.startswith('assets/image/'):
            img.set('src', 'image/' + target[len('assets/image/'):])


# ---------------------------------------------------------------- 内容の変換（頁の種類によらない部品）

def is_definition_item(li):
    """li が「**名前**: 説明」の項目なら (名前の strong を含む親, 名前の strong)。違えば None"""
    if (li.text or '').strip():
        return None
    first = li[0] if len(li) else None
    if first is None:
        return None
    if first.tag == 'p' and not (first.text or '').strip() and len(first) and first[0].tag == 'strong':
        holder, strong = first, first[0]
    elif first.tag == 'strong':
        holder, strong = li, first
    else:
        return None
    return holder, strong


def split_definition(li):
    """「**名前**: 説明」の項目を (名前の HTML, 名前の text, 説明の要素のリスト)。説明は dd に入れる字と要素"""
    holder, strong = is_definition_item(li)
    name_html = inner_html(strong)
    name_text = text_of(strong)
    tail = strong.tail or ''
    if tail.startswith(': '):
        tail = tail[2:]
    elif tail.strip() == ':':
        tail = ''
    elif tail.startswith(':'):
        tail = tail[1:]
    strong.tail = None
    holder.remove(strong)
    holder.text = tail
    return name_html, name_text, holder


def definition_ul_to_dl(ul, dl_class=None):
    """名前と説明だけの箇条書きなら dl にして返す（違えば None）"""
    if ul.tag != 'ul' or not len(ul):
        return None
    if any(li.tag != 'li' or is_definition_item(li) is None for li in ul):
        return None
    dl = new('dl', dl_class)
    for li in ul:
        name_html, name_text, holder = split_definition(li)
        dt = new('dt')
        set_inner(dt, name_html)
        dl.append(dt)
        dd = new('dd')
        if holder is li:
            # 名前の後ろの字と、続く要素（入れ子の箇条書きなど）
            dd.text = li.text
            for c in list(li):
                dd.append(c)
        else:
            # 空行の入った項目: 頭の段落（名前を除いた残り）と、続く段落
            if holder.text and holder.text.strip() or len(holder):
                p = new('p')
                p.text = holder.text
                for c in list(holder):
                    p.append(c)
                dd.append(p)
            for c in list(li)[1:]:
                dd.append(c)
        for c in dd:
            c.tail = None if c.tail is None or not c.tail.strip() else c.tail
        dl.append(dd)
    return dl


def convert_definition_lists(root, reference_class=True):
    """root の下の「名前と説明だけの箇条書き」を、Reference なら dl.reference、ほかは dl.property にする"""
    for ul in list(root.iter('ul')):
        parent = ul.getparent()
        if parent is None or parent.tag == 'li' and False:
            continue
        names = []
        ok = len(ul) > 0 and all(li.tag == 'li' and is_definition_item(li) is not None for li in ul)
        if not ok:
            continue
        for li in ul:
            holder, strong = is_definition_item(li)
            names.append(text_of(strong))
        is_ref = all(REFERENCE.fullmatch(n.replace('\\', '')) for n in names)
        dl = definition_ul_to_dl(ul, 'reference' if is_ref else 'property')
        if dl is None:
            continue
        dl.tail = ul.tail
        parent.replace(ul, dl)


def admonition_to_remarks(div, deprecated_flag=None):
    """!!! note などの囲みを、旧版の p を並べた囲み（div.remarks）にする"""
    cls = classes(div)
    kind = next((c for c in cls if c in ('note', 'warning', 'tip', 'danger', 'info')), 'note')
    title_el = None
    for c in div:
        if c.tag == 'p' and 'admonition-title' in classes(c):
            title_el = c
            break
    title = text_of(title_el) if title_el is not None else ''
    out = new('div', f'remarks admonition {kind}')
    if title_el is not None:
        p = new('p', 'admonition-title')
        p.text = title
        out.append(p)
        div.remove(title_el)
    for c in list(div):
        out.append(c)
    return out, title, kind


# ---------------------------------------------------------------- 対応（ベースウェアのアイコン）

def support_list(p):
    """p（**対応:** ...）→ ul.supported-baseware（と、続く行があればそれらの p）のリスト"""
    html = inner_html(p)
    html = re.sub(r'^\s*<strong>対応:</strong>\s*', '', html)
    head, sep, rest = re.partition(html, r'<br\s*/?>') if False else (None, None, None)
    m = re.split(r'<br\s*/?>', html, maxsplit=1)
    head = m[0]
    rest = m[1] if len(m) > 1 else ''
    ul = new('ul', 'supported-baseware')
    plain_parts = []
    for part in re.split(r'\s+/\s+', head.strip()):
        part = part.strip()
        if not part:
            continue
        mm = BASEWARE_PART.match(re.sub(r'<[^>]+>', '', part))
        if mm and not NEGATION.search(mm.group(2) or ''):
            name, ver = mm.group(1), (mm.group(2) or '').strip()
            li = new('li')
            img = new('img', src=f'image/icon_{BASEWARE[name]}.png', alt=name, width='34', height='16')
            if ver:
                img.set('title', f'{name} {ver}')
            li.append(img)
            if ver:
                span = new('span', 'baseware-version')
                set_inner(span, htmllib.escape(ver, quote=False) if '<' not in ver else ver)
                li.append(span)
            ul.append(li)
        else:
            li = new('li', 'baseware-note')
            set_inner(li, part)
            ul.append(li)
    extra = None
    if rest.strip():
        extra = new('p', 'support-note')
        set_inner(extra, rest.strip())
    return ul, extra


# ---------------------------------------------------------------- list 頁（descript_* / list_* / spec_* のまとめた頁）

def top_blocks(root):
    return [c for c in root if isinstance(c.tag, str)]


class Unit:
    """まとめた頁のなかの、分類（bundle-category）・項目（bundle-item）"""
    def __init__(self, head, kind):
        self.head = head
        self.kind = kind      # 'category' | 'item'
        self.body = []        # 見出しの後ろの要素（子の Unit を含まない）
        self.children = []    # 子の Unit
        self.id = head.get('id')


def parse_units(blocks):
    """見出しの class（bundle-category / bundle-item）で、要素の並びを入れ子の Unit にする。(頁頭の要素, Unit のリスト)"""
    intro = []
    roots = []
    stack = []
    for el in blocks:
        cls = classes(el) if is_heading(el) else []
        if is_heading(el) and ('bundle-category' in cls or 'bundle-item' in cls):
            kind = 'category' if 'bundle-category' in cls else 'item'
            unit = Unit(el, kind)
            unit.level = level(el)
            unit.supplement = 'bundle-supplement' in cls
            while stack and stack[-1].level >= unit.level:
                stack.pop()
            (stack[-1].children if stack else roots).append(unit)
            stack.append(unit)
        elif el.tag == 'hr':
            continue
        elif stack:
            stack[-1].body.append(el)
        else:
            intro.append(el)
    return intro, roots


def first_strong_label(p):
    return text_of(p[0]) if len(p) and p[0].tag == 'strong' and not (p.text or '').strip() else ''


def entry_content(unit, dd):
    """項目の本体を dd.entry の中身にする。戻り値: 非推奨か"""
    deprecated = False
    sections = []          # (見出しの要素, [中身])  項目内の節（H4 以降）
    cur = None
    for el in unit.body:
        if is_heading(el):
            cur = (el, [])
            sections.append(cur)
            continue
        target = cur[1] if cur is not None else None
        if cur is None:
            deprecated = deprecated or place_entry_block(el, dd)
        else:
            target.append(el)
    for head, body in sections:
        if text_of(head).startswith('記述例'):
            legend = new('div', 'legend')
            sec = new('section', 'code')
            if head.get('id'):
                sec.set('id', head.get('id'))
            h = new('h1')
            set_inner(h, title_html(head).replace('記述例', label('記述例'), 1))
            sec.append(h)
            for el in body:
                place_entry_block(el, sec)
            legend.append(sec)
            dd.append(legend)
            continue
        dl = new('dl', 'sub')
        if head.get('id'):
            dl.set('id', head.get('id'))
        dt = new('dt')
        set_inner(dt, title_html(head))
        dd2 = new('dd')
        for el in body:
            place_entry_block(el, dd2)
        dl.append(dt)
        dl.append(dd2)
        dd.append(dl)
    return deprecated


def place_entry_block(el, dd):
    """項目の本文の 1 要素を dd に足す。非推奨の囲みなら True を返す（足さない）"""
    cls = classes(el)
    if el.tag == 'div' and 'admonition' in cls:
        title = ''
        for c in el:
            if c.tag == 'p' and 'admonition-title' in classes(c):
                title = text_of(c)
        if 'warning' in cls and '非推奨' in title:
            return True
        box, _, _ = admonition_to_remarks(el)
        dd.append(clean_tail(box))
        return False
    if el.tag == 'p' and first_strong_label(el) == '既定値:':
        html = re.sub(r'^\s*<strong>既定値:</strong>\s*', '', inner_html(el))
        p = new('p', 'default')
        set_inner(p, html)
        dd.append(p)
        return False
    if el.tag == 'p' and first_strong_label(el) == '対応:':
        ul, extra = support_list(el)
        dd.append(ul)
        if extra is not None:
            dd.append(extra)
        return False
    if el.tag == 'p' and first_strong_label(el) == 'カテゴリ:':
        return False
    if el.tag == 'ul':
        dl = definition_ul_to_dl(el, 'reference' if all(
            REFERENCE.fullmatch(text_of(is_definition_item(li)[1]).replace('\\', '')) for li in el
            if is_definition_item(li) is not None) and all(is_definition_item(li) is not None for li in el) else 'property') \
            if all(is_definition_item(li) is not None for li in el) else None
        if dl is not None:
            dd.append(dl)
            return False
    dd.append(clean_tail(el))
    return False


def is_caption_unit(unit, is_first):
    """項目を、dl.entry（辞書の 1 項目）でなく section.caption（説明の節）にするか"""
    if unit.supplement:
        return True
    has_marks = any(el.tag == 'p' and first_strong_label(el) in ('対応:', '既定値:') for el in unit.body)
    has_sub = any(is_heading(el) for el in unit.body)
    if 'notes' in (unit.id or ''):
        return True
    return has_sub and not has_marks and (is_first or not has_marks)


def caption_content(unit, section):
    """説明の節（section.caption）の中身: 見出しごとの入れ子の section"""
    body = new('div')
    for el in unit.body:
        body.append(clean_tail(el))
    stack = [(0, section)]
    for el in list(body):
        if is_heading(el):
            sec = new('section')
            h = new('h1')
            set_inner(h, localize_heading(inner_html(el), text_of(el)))
            if el.get('id'):
                sec.set('id', el.get('id'))
            sec.append(h)
            lv = level(el) - level(unit.head)
            while stack and stack[-1][0] >= lv:
                stack.pop()
            stack[-1][1].append(sec)
            stack.append((lv, sec))
        elif el.tag == 'hr':
            continue
        else:
            target = stack[-1][1]
            if el.tag == 'div' and 'admonition' in classes(el):
                el, _, _ = admonition_to_remarks(el)
            target.append(clean_tail(el))
    convert_definition_lists_caption(section)


def convert_definition_lists_caption(section):
    """説明の節のなかの名前と説明の箇条書きを、旧版の dl（dt/dd）にする"""
    for ul in list(section.iter('ul')):
        parent = ul.getparent()
        if parent is None:
            continue
        if not len(ul) or any(li.tag != 'li' or is_definition_item(li) is None for li in ul):
            continue
        dl = definition_ul_to_dl(ul, None)
        if dl is None:
            continue
        dl.tail = ul.tail
        parent.replace(ul, dl)


def render_unit(unit, parent, nav_list, depth, first_in_cat):
    """Unit を parent（section.category など）に出力し、左の目次（nav_list: ul）に項目を足す"""
    if unit.kind == 'item':
        if is_caption_unit(unit, first_in_cat):
            sec = new('section', 'caption' + (' introduction' if first_in_cat and not unit.supplement else ''))
            sec.set('id', unit.id)
            h = new('h1')
            set_inner(h, title_html(unit.head))
            if (badge := orig_badge(unit.head)) is not None:
                h.append(badge)
            sec.append(h)
            caption_content(unit, sec)
            parent.append(sec)
            li = new('li', 'caption' + (' introduction' if first_in_cat and not unit.supplement else ''))
            a = new('a', href='#' + unit.id)
            set_inner(a, title_html(unit.head))
            li.append(a)
            nav_list.append(li)
        else:
            dl = new('dl')
            dl.set('id', unit.id)
            dt = new('dt', 'entry')
            set_inner(dt, title_html(unit.head))
            if (badge := orig_badge(unit.head)) is not None:
                dt.append(badge)
            dd = new('dd', 'entry')
            deprecated = entry_content(unit, dd)
            if deprecated:
                dt.set('class', 'entry deprecated')
            # 余計な空白を作らない
            dl.append(dt)
            dl.append(dd)
            parent.append(dl)
            li = new('li')
            a = new('a', href='#' + unit.id)
            set_inner(a, title_html(unit.head))
            li.append(a)
            nav_list.append(li)
        return
    # 分類（入れ子の分類は section.subcategory）
    cat = new('section', 'category' if depth == 0 else 'subcategory')
    cat.set('id', unit.id)
    h = new('h1')
    set_inner(h, title_html(unit.head))
    if (badge := orig_badge(unit.head)) is not None:
        h.append(badge)
    cat.append(h)
    for el in unit.body:
        if el.tag == 'hr':
            continue
        cat.append(clean_tail(el))
    parent.append(cat)
    first = True
    for child in unit.children:
        render_unit(child, cat, nav_list, depth + 1, first and child.kind == 'item')
        first = False


def build_list_page(md_rel, root, title):
    h1 = next(c for c in root if c.tag == 'h1')
    blocks = [c for c in root if c is not h1]
    intro, units = parse_units(blocks)
    page = new('div')
    nav_bar = new('section', 'navigation-bar')
    nh = new('h1')
    set_inner(nh, inner_html(h1))
    nav_bar.append(nh)
    cats = new('div', 'categories')
    plain, notes = [], []
    for el in intro:
        if el.tag == 'hr':
            continue
        (notes if el.tag == 'div' and 'bundle-notes' in classes(el) else plain).append(el)
    if md_rel == 'list/sakura-script/index.md':
        nav_bar.append(lxml.html.fragment_fromstring(read_template('target-ghost.html'), create_parent='div')[0])
    if plain:
        cap = new('div', 'caption')
        for el in plain:
            if el.tag == 'div' and 'admonition' in classes(el):
                el, _, _ = admonition_to_remarks(el)
            cap.append(clean_tail(el))
        convert_definition_lists_caption(cap)
        cats.append(cap)
    if notes:
        notes_nav = new('section', 'navigation-category')
        nn = new('h1')
        nn.text = label('概要')
        notes_nav.append(nn)
        notes_ul = new('ul')
        notes_nav.append(notes_ul)
        nav_bar.append(notes_nav)
        for box in notes:
            cap = new('div', 'caption')
            kids = list(box)
            if kids and is_heading(kids[0]):
                head_el = kids.pop(0)
                cap.set('id', head_el.get('id') or '')
                hh = new('h1')
                set_inner(hh, title_html(head_el))
                cap.append(hh)
                li = new('li', 'caption')
                a = new('a', href='#' + (head_el.get('id') or ''))
                set_inner(a, title_html(head_el))
                li.append(a)
                notes_ul.append(li)
            for el in kids:
                cap.append(clean_tail(el))
            convert_definition_lists_caption(cap)
            cats.append(cap)
    for unit in units:
        if unit.kind == 'category':
            cat_nav = new('section', 'navigation-category')
            nh2 = new('h1')
            set_inner(nh2, title_html(unit.head))
            cat_nav.append(nh2)
            ul = new('ul')
            cat_nav.append(ul)
            nav_bar.append(cat_nav)
            render_unit(unit, cats, ul, 0, False)
        else:
            # 分類を持たない頁（項目が直に並ぶ）
            sec = new('section', 'category')
            cat_nav = new('section', 'navigation-category')
            ul = new('ul')
            cat_nav.append(ul)
            nav_bar.append(cat_nav)
            render_unit(unit, sec, ul, 1, False)
            cats.append(sec)
    post_process_content(cats)
    return h1, nav_bar, cats


# ---------------------------------------------------------------- spec 頁（単独の spec_*.md。list.css）

def build_spec_page(md_rel, root):
    """単独の spec_*.md も、spec/<名前>/ のまとめた頁（list.css）と同じ見た目に組む。
    H2 を 1 項目とし、H3 以下の節を持つ H2 は説明の節（section.caption）、持たない H2 は辞書の項目（dl.entry）になる。
    最初の H2 より前の文は、頁の題を名前にした項目にする（spec/shiori3 の頭の「SHIORI/3.0」と同じ形）"""
    h1 = next(c for c in root if c.tag == 'h1')
    blocks = [c for c in root if c is not h1 and c.tag != 'hr']
    if blocks and not (is_heading(blocks[0]) and level(blocks[0]) == 2):
        head = new('h2')
        set_inner(head, inner_html(h1))
        head.set('id', 'chapter0')
        blocks.insert(0, head)
    units, cur = [], None
    for el in blocks:
        if is_heading(el) and level(el) == 2:
            cur = Unit(el, 'item')
            cur.level = 2
            cur.supplement = False
            units.append(cur)
        else:
            cur.body.append(el)
    nav_bar = new('section', 'navigation-bar')
    nh = new('h1')
    set_inner(nh, inner_html(h1))
    nav_bar.append(nh)
    cat_nav = new('section', 'navigation-category')
    ul = new('ul')
    cat_nav.append(ul)
    nav_bar.append(cat_nav)
    cats = new('div', 'categories')
    for unit in units:
        sec = new('section', 'category')
        render_unit(unit, sec, ul, 1, False)
        cats.append(sec)
    post_process_content(cats)
    return h1, nav_bar, cats


# ---------------------------------------------------------------- frame 頁（manual_*・dev_*・memo*・index）

def marked_definition_ul(ul):
    """prepare_site が名前に manual-item / top-item を付けた「名前と説明だけの箇条書き」か"""
    return ul.tag == 'ul' and len(ul) > 0 and all(
        li.tag == 'li' and is_definition_item(li) is not None and
        ({'manual-item', 'top-item'} & set(classes(is_definition_item(li)[1]))) for li in ul)


def definition_groups(dl):
    """dl の (dt のリスト, dd) の組。説明の無い項目は次の項目の dt と束ねる（旧版の dt dt dd）"""
    groups, dts = [], []
    for c in dl:
        if c.tag == 'dt':
            dts.append(c)
        else:
            if not (len(c) or (c.text or '').strip()):
                continue      # 説明の無い項目の空の dd
            groups.append((dts, c))
            dts = []
    if dts:
        groups.append((dts, None))
    return groups


def build_frame_page(md_rel, root):
    """base.css の頁: main > h1 + section... （区切りの見出しごとに入れ子の section）"""
    h1 = next(c for c in root if c.tag == 'h1')
    blocks = [c for c in root if c is not h1]
    main = new('main')
    toppage = md_rel == 'index.md'
    if toppage:
        main.set('class', 'toppage')
    mh = new('h1')
    if h1.get('id'):
        mh.set('id', h1.get('id'))
    set_inner(mh, inner_html(h1))
    main.append(mh)
    is_dev = md_rel.startswith('dev/')

    # トップページは main > section > section（節は無名の section の下）、ほかは main > section
    wrapper = None
    if toppage:
        wrapper = new('section')
        main.append(wrapper)
    h2_parent = wrapper if toppage else main
    stack = []                  # [(見出しの深さ, section)]
    state = {'passage': None}

    def ensure_top():
        if not stack:
            sec = wrapper if toppage else new('section')
            if not toppage:
                main.append(sec)
            stack.append((1, sec))
            state['passage'] = None
        return stack[-1][1]

    def put(el):
        sec = ensure_top()
        if el.tag == 'div' and 'admonition' in classes(el):
            box, title, kind = admonition_to_remarks(el)
            if toppage:
                caution = new('section', 'caution')
                if title:
                    ch = new('h1')
                    ch.text = title
                    caution.append(ch)
                    for p in list(box):
                        if 'admonition-title' in classes(p):
                            box.remove(p)
                for c in list(box):
                    caution.append(c)
                sec.append(caution)
                state['passage'] = None
                return
            el = box
        if state['passage'] is None or state['passage'].getparent() is not sec:
            state['passage'] = new('div', 'passage')
            sec.append(state['passage'])
        state['passage'].append(clean_tail(el))

    for el in blocks:
        if is_heading(el):
            lv = level(el)
            skipping = toppage and lv == 2 and text_of(el) == '目次'   # 目次は左のメニュー（sidemenu.html）と同じなので出さない
            sec = new('section')
            if el.get('id'):
                sec.set('id', el.get('id'))
            h = new('h1')
            set_inner(h, inner_html(el))
            sec.append(h)
            if skipping:
                stack[:] = [(2, new('section'))]   # 後ろの要素の受け皿（出力しない）
                state['passage'] = None
                continue
            if lv == 2:
                h2_parent.append(sec)
                stack[:] = [(2, sec)]
            else:
                ensure_top()
                while len(stack) > 1 and stack[-1][0] >= lv:
                    stack.pop()
                stack[-1][1].append(sec)
                stack.append((lv, sec))
            state['passage'] = None
        elif el.tag == 'hr':
            continue
        elif not toppage and len(stack) <= 1 and (not stack or stack[0][0] == 1) and marked_definition_ul(el):
            # 見出しの前（頁の頭）のファイルの一覧は、項目ごとに 1 つの section にする（旧版の見た目）
            dl = definition_ul_to_dl(el, None)
            for dts, dd in definition_groups(dl):
                sec = new('section')
                passage = new('div', 'passage')
                comp = new('dl', 'component')
                for dt in dts:
                    comp.append(dt)
                if dd is not None:
                    comp.append(dd)
                passage.append(comp)
                sec.append(passage)
                main.append(sec)
            stack[:] = []
            state['passage'] = None
        else:
            put(el)
    if is_dev:
        build_dev_toc(main, TOC_GROUPS.get(md_rel, []))
    convert_frame_definitions(main, toppage)
    post_process_content(main)
    return h1, main


TOC_GROUPS = {}


def toc_groups_of(text):
    """dev の頁の「## 目次」の番号付きリストを、番号が 1 に戻るところで区切った各グループの項目数（2 つ目が EX）"""
    m = re.search(r'^## 目次\n(.*?)(?=^## |\Z)', text, re.S | re.M)
    if not m:
        return []
    groups = []
    for line in m.group(1).split('\n'):
        mm = re.match(r'^(\d+)\. ', line)
        if mm:
            if int(mm.group(1)) == 1 or not groups:
                groups.append(0)
            groups[-1] += 1
    return groups


def build_dev_toc(main, groups):
    """dev の頁: 「目次」の節を nav にし、目次に載った節に番号（section.ordered / ordered ex）を付ける"""
    toc_sec = None
    for sec in main.findall('section'):
        h = sec.find('h1')
        if h is not None and text_of(h) == '目次':
            toc_sec = sec
            break
    if toc_sec is None:
        return
    items = [li for ol in toc_sec.iter('ol') for li in ol]
    if not groups or sum(groups) != len(items):
        groups = [len(items)]
    nav = new('nav')
    nh = new('h1')
    nh.text = label('目次')
    nav.append(nh)
    ex_map = {}
    pos = 0
    for n, count in enumerate(groups):
        ol_el = new('ol', 'ex' if n == 1 else None)
        for li in items[pos:pos + count]:
            li2 = new('li')
            kids = list(li)
            if len(kids) == 1 and kids[0].tag == 'p':
                kids = list(kids[0])
                li2.text = kids[0].getparent().text if kids else None
                src = li[0]
            else:
                src = li
            li2.text = src.text
            for c in kids:
                li2.append(c)
            ol_el.append(li2)
            ex_map[text_of(li2)] = (n == 1)
        pos += count
        nav.append(ol_el)
    main.replace(toc_sec, nav)
    for sec in main.findall('section'):
        h = sec.find('h1')
        if h is None:
            continue
        t = text_of(h)
        if t in ex_map:
            sec.set('class', 'ordered ex' if ex_map[t] else 'ordered')


def convert_frame_definitions(main, toppage):
    """「- **名前**: 説明」の箇条書き（prepare_site が名前に manual-item / top-item を付けたもの）を dl.component にする"""
    for ul in list(main.iter('ul')):
        parent = ul.getparent()
        if parent is None or not len(ul):
            continue
        if any(li.tag != 'li' or is_definition_item(li) is None for li in ul):
            continue
        marked = all(({'manual-item', 'top-item'} & set(classes(is_definition_item(li)[1]))) for li in ul)
        if not marked:
            continue
        is_top = toppage or all('top-item' in classes(is_definition_item(li)[1]) for li in ul)
        dl = definition_ul_to_dl(ul, None if is_top else 'component')
        if dl is None:
            continue
        dl.tail = ul.tail
        # dd の直下の段落を passage に包まない（旧版は dd 直下に p）
        parent.replace(ul, dl)


def post_process_content(root):
    """コードブロックの旧版の見た目に必要な class など"""
    for pre in root.iter('pre'):
        pass
    for table in root.iter('table'):
        if table.get('border') is None:
            pass


# ---------------------------------------------------------------- 頁の組み立て

def head(title, css, extra_head='', description=None):
    return f'''<!DOCTYPE html>
<html lang="{LANG or "ja"}">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="INDEX,FOLLOW">
<meta name="author" content="UKADOC Project">
<meta name="keywords" content="ukadoc,伺か">
<meta name="ukadoc-langs" content="{",".join(available_langs())}">
<title>UKADOC Project {htmllib.escape(title, quote=False)}</title>
<link rel="stylesheet" href="{css}">
<link rel="stylesheet" href="oldstyle.css">
<link rel="shortcut icon" href="favicon.ico" type="image/x-icon" />
<script src="menu.js"></script>
<script src="lang.js" defer></script>
<script src="search.js" defer></script>
{extra_head}</head>
'''


def serialize(el):
    return lxml.html.tostring(el, encoding='unicode', pretty_print=False)


def read_template(name):
    """枠の断片。翻訳版では i18n/<言語>/templates/<name> があればそちら（メニューなどの訳）、無ければ日本語の写し"""
    path = os.path.join(TEMPLATES, name)
    if I18N_TEMPLATES and os.path.isfile(os.path.join(I18N_TEMPLATES, name)):
        path = os.path.join(I18N_TEMPLATES, name)
    with open(path, encoding='utf-8') as f:
        return f.read()


def frame_open():
    """枠の頁の頭。上の帯（navigation.html）と左のメニュー（sidemenu.html）の断片を、頁に埋め込む（iframe は使わない）"""
    return (read_template('frame-open.html')
            .replace('<!--NAVIGATION-->\n', read_template('navigation.html'))
            .replace('<!--SIDEMENU-->\n', read_template('sidemenu.html')))


def write_out(name, text):
    path = os.path.join(OUT, name)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def page_script_tags(md_rel):
    extra = ''
    if md_rel == 'list/sakura-script/index.md':
        extra += '<script src="sakura_player.js"></script>\n'
    return extra


def drawer(inner):
    """list / spec の頁の、目次の表（menu-header.html）と左のナビゲーションを包む。
    広い画面では display: contents で包みが無いのと同じ。狭い画面では、menu.js のボタンで開閉する引き出しになる"""
    return f'<div id="ukadoc-drawer" class="ukadoc-drawer ukadoc-drawer--wrap">\n{inner}\n</div>'


# list / spec の頁の頭: 文書の題の代わりに、タイトル画像（枠の頁の上の帯と同じ title.png）を置き、トップページへのリンクにする。
# 文書の題は、左のナビゲーションの見出しと <title> にある
PAGE_TITLE_LOGO = ('<div id="page-title"><a href="index.html">'
                   '<img src="image/title.png" width="281" height="55" alt="UKADOC Project"></a></div>')


def page_anchor(h1):
    """頁の頭への内部リンク（まとめる前の頁の H1 の id）の受け皿"""
    return f'<a id="{htmllib.escape(h1.get("id"), quote=True)}"></a>' if h1.get('id') else ''


def render_page(md_rel, text, known):
    kind = page_kind(md_rel)
    if md_rel.startswith('dev/'):
        TOC_GROUPS[md_rel] = toc_groups_of(text)
    root = convert(text)
    resolve_links(root, md_rel, known)
    mark_sakurascript(root)
    name = out_name(md_rel)
    menu = read_template('menu-header.html')
    if kind in ('list', 'spec'):
        if kind == 'list':
            h1, nav_bar, cats = build_list_page(md_rel, root, None)
        else:
            h1, nav_bar, cats = build_spec_page(md_rel, root)
        title = text_of(h1)
        out = head(title, 'list.css', page_script_tags(md_rel))
        out += f'<body>\n\t{page_anchor(h1)}{PAGE_TITLE_LOGO}\n'
        out += drawer(menu + '\n' + serialize(nav_bar)) + '\n' + serialize(cats) + '\n'
        out += '</body>\n</html>\n'
    else:
        h1, main = build_frame_page(md_rel, root)
        if LANG:     # 枠の頁の見出しに日本語のまま残った構造の語（目次など）を、その言語の語にする
            for h in main.iter('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
                set_inner(h, localize_heading(inner_html(h), text_of(h)))
        title = text_of(h1)
        out = head(title, 'base.css')
        out += frame_open()
        out += serialize(main) + '\n'
        out += read_template('frame-close.html')
    write_out(name, out)
    return name


def normalize_space(text):
    return re.sub(r'\s+', ' ', text).strip()


def build_search_index():
    """出力した頁から、サイト内検索用の索引（search-index.js）を作る。項目（dl#id）・節（section#id）ごとに 1 件"""
    entries = []
    skip = {'search.html'}
    for name in sorted(os.listdir(OUT)):
        if not name.endswith('.html') or name in skip:
            continue
        with open(os.path.join(OUT, name), encoding='utf-8') as f:
            doc = lxml.html.fromstring(f.read())
        # 枠の頁は、左のメニューと上の帯を含まない本文（main）だけを見る
        body = doc.find('.//main')
        if body is None:
            body = doc.find('body')
        h1 = body.find('.//h1')
        if h1 is None:
            h1 = doc.find('.//h1')
        page = normalize_space(h1.text_content()) if h1 is not None else name
        entries.append([page, page, name, normalize_space(body.text_content())[:300]])
        for el in doc.iter('dl', 'section', 'div'):
            ident = el.get('id')
            if not ident or ident == 'page-title':
                continue
            if el.tag == 'dl':
                dt = el.find('dt')
                if dt is None or 'entry' not in (dt.get('class') or ''):
                    continue
                title = normalize_space(dt.text_content())
                text = normalize_space((el.find('dd') if el.find('dd') is not None else el).text_content())
            else:
                h = el.find('h1')
                if h is None:
                    continue
                title = normalize_space(h.text_content())
                text = normalize_space(el.text_content())
            entries.append([page, title, f'{name}#{ident}', text[:1500]])
    with open(os.path.join(OUT, 'search-index.js'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('window.UKADOC_INDEX = ' + json.dumps(entries, ensure_ascii=False, separators=(',', ':')) + ';\n')
    return len(entries)


SEARCH_TITLES = {'en': 'Search UKADOC', 'zh-Hant': '搜尋 UKADOC', 'zh': '搜索 UKADOC'}


def build_search_page():
    out = head(SEARCH_TITLES.get(LANG, 'ukadoc内検索'), 'base.css')
    out += frame_open() + read_template('search-main.html') + '\n' + read_template('frame-close.html')
    write_out('search.html', out)


OFFLINE_ZIP = 'ukadoc-spec-offline.zip'


def build_offline_zip():
    """出力したサイト一式（HTML・CSS・JS・画像・llms.txt・生の Markdown 原稿）を、オフラインで読める zip にする。
    展開すると `ukadoc-spec/` の下に出る。zip 自身は含めない。サイトのルートに置かれ、公開される"""
    zip_path = os.path.join(OUT, OFFLINE_ZIP)
    files = []
    for dirpath, dirs, names in os.walk(OUT):
        dirs.sort()
        for name in sorted(names):
            path = os.path.join(dirpath, name)
            if path != zip_path:
                files.append(path)
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for path in files:
            rel = os.path.relpath(path, OUT).replace(os.sep, '/')
            z.write(path, 'ukadoc-spec/' + rel)
    return len(files), os.path.getsize(zip_path)


def main():
    if '--no-prepare' not in sys.argv:
        subprocess.run([sys.executable, os.path.join(ROOT, 'scripts', 'prepare_site.py')] + ([f'--lang={LANG}'] if LANG else []), check=True)
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    shutil.copytree(STATIC, OUT, ignore=shutil.ignore_patterns('*.psp'))   # .psp は画像の作業ファイル（公開しない）
    # 原稿の画像（旧版の image/ に足す。同名は原稿を優先）
    img_src = os.path.join(ROOT, 'assets', 'image')
    if os.path.isdir(img_src):
        shutil.copytree(img_src, os.path.join(OUT, 'image'), dirs_exist_ok=True)

    pages = {}
    for dirpath, dirs, files in os.walk(SRC):
        rel_dir = os.path.relpath(dirpath, SRC).replace(os.sep, '/')
        if rel_dir == 'assets' or rel_dir.startswith('assets/'):
            continue
        for name in files:
            if name.endswith('.md'):
                rel = name if rel_dir == '.' else f'{rel_dir}/{name}'
                pages[rel] = os.path.join(dirpath, name)
    known = set(pages)
    for rel, path in sorted(pages.items()):
        with open(path, encoding='utf-8') as f:
            text = f.read()
        render_page(rel, text, known)
    build_search_page()
    count = build_search_index()
    print(f'索引 {count} 件')
    if ERRORS:
        sys.exit(1)
    if not LANG:
        # llms.txt をサイトのルートに置き、生の Markdown 原稿（_raw/）を重ねる（llms.txt や INDEX.md の相対リンクを辿れるように）。
        # 翻訳版には置かない（日本語版のものを共有する）
        shutil.copy(os.path.join(ROOT, 'llms.txt'), os.path.join(OUT, 'llms.txt'))
        raw = os.path.join(ROOT, '_raw')
        if os.path.isdir(raw):
            shutil.copytree(raw, OUT, dirs_exist_ok=True)
    print(f'{len(pages)} 頁を {OUT} に出力した')
    if not LANG:
        if '--no-langs' not in sys.argv:
            # 日本語版の後ろに、翻訳のある言語（i18n/<コード>/ があるもの）を _site_old/<コード>/ へ続けてビルドする
            for code in available_langs()[1:]:
                subprocess.run([sys.executable, os.path.abspath(__file__), f'--lang={code}'], check=True)
        # オフライン zip は、翻訳版も含めて最後に作る（言語メニューのリンク先が zip の中にもあるように）
        n, size = build_offline_zip()
        print(f'{OFFLINE_ZIP}: {n} ファイル、{size / 1024 / 1024:.1f} MB')


if __name__ == '__main__':
    main()

"""サイトの見た目のための Python-Markdown 拡張（mkdocs.yml の markdown_extensions に ukadoc_site.structure と書く）。

頁ごとの判断（どの頁のどの段落か）は scripts/prepare_site.py が attr_list の class で原稿に付ける。
この拡張は、その class と木の形だけを見て、次の 2 つの構造を作る（見た目は assets/extra.css）。

- 対応の段落（p.bundle-support）の、ベースウェアの名前を札（span.bundle-baseware）で包む
- 「- **名前**: 説明」だけが並ぶ箇条書きを、「名前」「説明」の 2 列の表（div.definition-table）にする
"""
import re
import xml.etree.ElementTree as etree

from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor

BASEWARE = ['Materia', 'SSP', 'CROW', 'Ninix']   # 札にする名前。足すときは assets/extra.css に明・暗の札の色も足す
BASEWARE_PART = re.compile(rf'^({"|".join(BASEWARE)})(?=\s|$)')
NEGATION = re.compile(r'非対応|未対応|廃止')
# list/ の頁の Reference の名前。\* は Python-Markdown が一時的に STX 42 ETX に置き換えている
REFERENCE = re.compile(r'Reference(?:\d+|\x0242\x03)(?:～\d*)?')
BLOCK_TAGS = {'p', 'ul', 'ol', 'pre', 'div', 'table', 'blockquote', 'dl', 'details'}


def is_block(node):
    return not isinstance(node, str) and node.tag in BLOCK_TAGS


def inline_nodes(el):
    """el の中身を、字（str）と要素が交互に並ぶ列にする（[el.text, 子, 子の tail, ...]）。el は変えない"""
    nodes = [el.text or '']
    for child in el:
        nodes += [child, child.tail or '']
    return nodes


def fill(el, nodes):
    """inline_nodes の逆。字と要素の並びを el の中身にする（要素の tail は付け直す）"""
    for child in list(el):
        el.remove(child)
    el.text = None
    last = None
    for node in nodes:
        if isinstance(node, str):
            if last is None:
                el.text = (el.text or '') + node
            else:
                last.tail = (last.tail or '') + node
        else:
            node.tail = None
            el.append(node)
            last = node


# ---------------------------------------------------------------- 対応の札

def baseware_nodes(text, part_start):
    """text を ' / ' で区切り、部分の頭がベースウェアの名前なら札で包んだ、字と要素の並び。
    part_start: text の頭が部分の頭か（要素の後ろの字は、部分の途中から始まる）"""
    out = []
    for n, part in enumerate(text.split(' / ')):
        if n:
            out.append(' / ')
        m = BASEWARE_PART.match(part) if n or part_start else None
        if not m or NEGATION.search(part[m.end():]):
            out.append(part)
            continue
        span = etree.Element('span', {'class': f'bundle-baseware bundle-baseware-{m.group(1).lower()}'})
        span.text = m.group(1)
        out += [span, part[m.end():]]
    return out


def mark_baseware(p):
    """p.bundle-support の「対応:」の後ろ（最初の <br /> まで）の、ベースウェアの名前を札で包む"""
    nodes = inline_nodes(p)
    if nodes[0].strip() or len(nodes) < 3 or nodes[1].tag != 'strong':
        return
    out = nodes[:2]
    part_start = True
    in_line = True
    for node in nodes[2:]:
        if isinstance(node, str):
            if in_line:
                # 「**対応:** 」の後ろの空白 1 字は札の外に残す
                lead = node[:1] if part_start and node.startswith(' ') else ''
                out += [lead] + baseware_nodes(node[len(lead):], part_start)
            else:
                out.append(node)
            part_start = False
        else:
            out.append(node)
            in_line = in_line and node.tag != 'br'
    fill(p, out)


# ---------------------------------------------------------------- 名前と説明の表

def definition_row(li):
    """li が「**名前**: 説明」の項目なら (名前の strong, 説明の字と要素の並び, 説明が段落などを含むか)。違えば None"""
    nodes = inline_nodes(li)
    if nodes[0].strip() or len(nodes) < 3:
        return None
    if nodes[1].tag == 'p':
        # 空行の入った項目（段落が並ぶ）。頭の段落の頭が名前
        head = inline_nodes(nodes[1])
        if head[0].strip() or len(head) < 3 or head[1].tag != 'strong':
            return None
        strong, rest, after, block = head[1], head[2:], nodes[2:], True
    elif nodes[1].tag == 'strong':
        strong, rest, after = nodes[1], nodes[2:], []
        block = any(is_block(x) for x in rest)
    else:
        return None
    if strong.get('class') or not ''.join(strong.itertext()):
        return None
    # 名前の直後の字が「: 」か、行末の「:」
    first = rest[0]
    if first.startswith(': '):
        rest = [first[2:]] + rest[1:]
    elif first.strip() == ':':
        rest = [''] + rest[1:]
    else:
        return None
    desc = rest + after
    if block:
        # ブロックの要素の間に字があると表の中で置き場が無いので、表にしない
        seen = False
        for x in desc:
            seen = seen or is_block(x)
            if seen and isinstance(x, str) and x.strip():
                return None
    return strong, desc, block


def make_table(rows):
    div = etree.Element('div', {'class': 'definition-table'})
    table = etree.SubElement(div, 'table')
    head = etree.SubElement(etree.SubElement(table, 'thead'), 'tr')
    etree.SubElement(head, 'th').text = '名前'
    etree.SubElement(head, 'th').text = '説明'
    body = etree.SubElement(table, 'tbody')
    for strong, desc, block in rows:
        tr = etree.SubElement(body, 'tr')
        fill(etree.SubElement(tr, 'td'), [strong])
        td = etree.SubElement(tr, 'td')
        if not block:
            fill(td, desc)
            continue
        # 段落などを含む説明: ブロックの要素の手前の字と要素は 1 つ目の段落にまとめ、ブロックの要素はそのまま並べる
        n = next(k for k, x in enumerate(desc) if is_block(x))
        lead, blocks = desc[:n], [x for x in desc[n:] if not isinstance(x, str)]
        if any(x.strip() if isinstance(x, str) else True for x in lead):
            fill(etree.SubElement(td, 'p'), lead)
        for x in blocks:
            x.tail = None
            td.append(x)
    return div


def to_table(parent, ul):
    """ul が名前と説明だけの箇条書きなら、表の div（でなければ None）"""
    rows = [definition_row(li) for li in ul]
    if not rows or any(r is None for r in rows) or any(li.tag != 'li' for li in ul):
        return None
    is_ref = all(REFERENCE.fullmatch(''.join(r[0].itertext())) for r in rows)
    # 説明が段落などを含む項目は、Reference の表（箇条書きの項目や注意書きの箱の中でないもの）にだけ許す
    if any(r[2] for r in rows) and not (is_ref and parent.tag != 'li' and 'admonition' not in (parent.get('class') or '')):
        return None
    if len(rows) < 2 and not is_ref:
        return None
    return make_table(rows)


def tabulate(parent):
    for n, child in enumerate(list(parent)):
        # 箇条書きの項目の中の箇条書きは、空行で前の段落と分かれている（項目が <p> で始まる）ものだけ表にする
        if child.tag == 'ul' and (parent.tag != 'li' or (n and parent[n - 1].tag == 'p')):
            table = to_table(parent, child)
            if table is not None:
                table.tail = child.tail
                parent[n] = table
                tabulate(table)   # 表の説明の中の箇条書きも表にする
                continue
        tabulate(child)


class StructureTreeprocessor(Treeprocessor):
    def run(self, root):
        for p in root.iter('p'):
            if 'bundle-support' in (p.get('class') or '').split():
                mark_baseware(p)
        tabulate(root)


class StructureExtension(Extension):
    def extendMarkdown(self, md):
        # attr_list（優先度 8）の後ろで動かす
        md.treeprocessors.register(StructureTreeprocessor(md), 'ukadoc_structure', 5)


def makeExtension(**kwargs):
    return StructureExtension(**kwargs)

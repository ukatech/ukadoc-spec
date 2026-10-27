"""サイトのコードブロックの Pygments レキサー。

- SakuraScriptLexer: さくらスクリプトの記述例のタグ（Name.Tag）と環境変数（Name.Variable.Global）を取り出し、
  誤り（閉じない [ や囲み、名前の無い \\）は Error にする。見た目は assets/extra.css
- FileTreeLexer: ファイル構成の木（+- の行のあるブロック）のファイル名（Name.Other）を取り出す

どちらも字は変えない（字の並びを Token に区切るだけ）。誤りは、ビルドの標準エラー出力に警告を出す（ビルドは止めない）。
"""
import logging
import re

from pygments.lexer import Lexer
from pygments.token import Error, Name, Text

log = logging.getLogger('ukadoc_site')

_NUMBERED = {'s': re.compile('[0-9]'), 'p': re.compile('[0-9]'), 'b': re.compile('[0-9]'), 'w': re.compile('[1-9]')}
_ENV = re.compile(r'%(?:\*|m\?|[A-Za-z_][A-Za-z0-9_]*)')
_WHY = {
    'args': '閉じる ] が無い（引数の " が閉じていないときも）',
    'enclosure': '閉じる囲みの印が無い',
    'backslash': '\\ の後にタグの名前が無い（\\ を字として見せるなら \\\\ と書く）',
}


class _VerbatimLexer(Lexer):
    """字を変えないレキサー（前後の改行を削らず、末尾の改行も足さない）"""

    def __init__(self, **options):
        options['stripnl'] = False
        options['ensurenl'] = False
        super().__init__(**options)


def _args_end(t, i):
    """t[i] の [ に対になる ] の次の位置（閉じなければ -1）。
    \\] と、引数の頭からの "…"（"" は " 1 字）の中の ] では終えない"""
    n = len(t)
    j = i + 1
    head = True
    while j < n:
        if head and t[j] == '"':
            j += 1
            while j < n and not (t[j] == '"' and t[j + 1:j + 2] != '"'):
                j += 2 if t[j] == '"' else 1
            if j >= n:
                return -1
            j += 1
            head = False
            continue
        if t[j] == ']':
            return j + 1
        head = t[j] == ','
        j += 2 if t[j] == '\\' and t[j + 1:j + 2] == ']' else 1
    return -1


def _tokens(t):
    """(種類, 始め, 終わり) の並び。誤りはブロックの終わりまでとし、そこで読むのをやめる（救済しない）"""
    out = []
    n = len(t)

    def fail(i, why):
        log.warning('sakurascript: %s: %s', _WHY[why], t[i:i + 40])
        out.append((Error, i, n))
        return out

    i = 0
    while i < n:
        if t[i] == '\\':
            if t[i + 1:i + 2] in ('\\', '%'):
                i += 2
                continue
            k = i + 1
            while k < n and t[k] == '_':
                k += 1
            if k >= n or t[k] in '\n\r':
                return fail(i, 'backslash')
            e = k + 1
            name = t[i + 1:e]
            if name in ('_?', '_!'):
                close = t.find('\\' + name, e)
                if close < 0:
                    return fail(i, 'enclosure')
                out.append((Name.Tag, i, e))
                out.append((Name.Tag, close, close + 3))
                i = close + 3
                continue
            if name in _NUMBERED and _NUMBERED[name].match(t[e:e + 1] or '\0'):
                e += 1
            elif t[e:e + 1] == '[':
                e = _args_end(t, e)
                if e < 0:
                    return fail(i, 'args')
            out.append((Name.Tag, i, e))
            i = e
        elif t[i] == '%':
            e = -1
            if t.startswith('%property[', i):
                e = _args_end(t, i + 9)
                if e < 0:
                    return fail(i, 'args')
            else:
                m = _ENV.match(t, i)
                if m:
                    e = m.end()
            if e < 0:
                i += 1
                continue
            out.append((Name.Variable.Global, i, e))
            i = e
        else:
            i += 1
    return out


def _with_text(t, spans):
    """(種類, 始め, 終わり) の並びを、間の字（Text）を埋めた (位置, 種類, 字) の並びにする"""
    last = 0
    for kind, s, e in spans:
        if s > last:
            yield last, Text, t[last:s]
        yield s, kind, t[s:e]
        last = e
    if last < len(t):
        yield last, Text, t[last:]


class SakuraScriptLexer(_VerbatimLexer):
    name = 'SakuraScript'
    aliases = ['sakurascript', 'ss']   # 先頭の名前が、コードブロックの class（language-sakurascript）になる
    filenames = []

    def get_tokens_unprocessed(self, text):
        yield from _with_text(text, _tokens(text))


_ROW = re.compile(r'^[\s　]*\+-')
_NAME = re.compile(r'[^\s（]+')
_OR = re.compile(r' または ')
_FILE = re.compile(r'\.[^.()]+$')


def _files(line):
    """木の行 line の中のファイル名の (始め, 終わり) の並び。
    名前は +- の後ろの空白と全角の（ までで、/ と「 または 」で 2 つ目が続く"""
    row = _ROW.match(line)
    if not row:
        return []
    out = []
    i = row.end()
    while True:
        m = _NAME.match(line, i)
        if not m:
            return out
        s = i
        for part in m.group(0).split('/'):
            if _FILE.search(part):
                out.append((s, s + len(part)))
            s += len(part) + 1
        i = m.end()
        o = _OR.match(line, i)
        if not o:
            return out
        i = o.end()


class FileTreeLexer(_VerbatimLexer):
    name = 'FileTree'
    aliases = ['filetree']
    filenames = []

    def get_tokens_unprocessed(self, text):
        spans = []
        at = 0
        for line in text.split('\n'):
            spans += [(Name.Other, at + s, at + e) for s, e in _files(line)]
            at += len(line) + 1
        yield from _with_text(text, spans)

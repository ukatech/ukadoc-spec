"""原稿（.md）と枠のテンプレート（oldstyle/templates/*.html）を LLM で翻訳し、i18n/<言語>/ に置く。

使い方:
    python scripts/translate.py --dry-run                 # 対象・リクエスト数・費用の目安だけ出す（API は呼ばない）
    python scripts/translate.py --lang=en --limit=20      # 英語を 20 ファイルだけ試す
    python scripts/translate.py                           # 全言語・全ファイル（原稿のハッシュが変わったものだけ）
    python scripts/translate.py --force                   # ハッシュが同じでも訳し直す（用語集・プロンプトを直したとき）

設定は環境変数か、リポジトリ直下の .env（.gitignore 済み）に書く:
    TRANSLATE_API_KEY=...                              （必須）
    TRANSLATE_BASE_URL=https://.../v1                  （必須。OpenAI 互換の /chat/completions の手前まで）
    TRANSLATE_MODEL=gpt-6-luna                         （省略時は gpt-6-luna）
    TRANSLATE_PRICE_IN=0.1  TRANSLATE_PRICE_OUT=0.5    （100 万トークンあたりの米ドル。費用の集計用）

方針:
- 原稿のハッシュ（i18n/<言語>/.manifest.json）が変わったファイルは、ファイルごと丸ごと訳し直す
- 小さいファイルは 1 リクエストにまとめる（原稿の中央値は 340 バイトで、用語集などの前置きのほうが大きくなるため）
- 訳文は構造を検査し（見出し・リンク先・コードブロック・表・箇条書き・構造の判定に使う日本語の語）、通らなければ
  理由を添えて 1 ファイルずつ訳し直す。それでも通らないファイルは置かない（日本語のまま出る）
- 費用が --max-cost に達したら、新しいリクエストを出さずに止める（済んだ分は残る。再実行で続きから）
"""
import argparse
import concurrent.futures
import difflib
from collections import Counter
import hashlib
import json
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.request

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
I18N = os.path.join(ROOT, 'i18n')
TEMPLATES = os.path.join(ROOT, 'oldstyle', 'templates')
DIRS = ['manual', 'descript', 'list', 'spec', 'dev', 'memo']     # prepare_site.py の DIRS と同じ
GLOSSARY = os.path.join(I18N, 'glossary.tsv')

LANGS = {
    'en': 'English',
    'zh-Hant': 'Traditional Chinese (繁體中文, as written in Taiwan)',
    'zh': 'Simplified Chinese (简体中文)',
}

# 「## 記述例と基本の書き方」の訳し方の例（記述例の字を残し、残りだけ訳す）。プロンプトには、その言語の例だけを入れる
HEADING_EXAMPLE = {'en': '記述例 and basic usage', 'zh-Hant': '記述例 與基本寫法', 'zh': '記述例 与基本写法'}

BATCH_BYTES = 12000    # 1 リクエストにまとめる原稿の大きさ（UTF-8 のバイト数）の目安
BATCH_FILES = 25
FINE_BYTES = 1200       # 最後の手段の、細かい塊の大きさ
RETRIES = 2            # 検査に落ちたときの、1 ファイルずつの訳し直しの回数

JAPANESE = re.compile(r'[぀-ヿ㐀-鿿ｦ-ﾟ]')
HIRAGANA = re.compile(r'[ぁ-ん]')
FENCE = re.compile(r'^\s*(```|~~~)')
HEADING = re.compile(r'^(#{1,6}) +(.+?) *$')
MARKER_LABELS = ('**カテゴリ:**', '**対応:**', '**既定値:**')    # 構造の判定に使う（訳さない）
MARKER_HEADINGS = ('記述例', '目次', '一覧')                       # 同上。見出しがこれで始まるなら、訳文でも同じ字面
BASEWARE = re.compile(r'(?<![A-Za-z])(?:Materia|SSP|CROW|Ninix)(?![A-Za-z])')   # 直後に日本語が続く「Materia廃止仕様」も数える（\b では数えられない）


# ---------------------------------------------------------------- 設定

def load_env():
    path = os.path.join(ROOT, '.env')
    if not os.path.isfile(path):
        return
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            key, value = line.split('=', 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def sha(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def read_text(path):
    with open(path, encoding='utf-8') as f:
        return f.read().replace('\r\n', '\n')


# ---------------------------------------------------------------- 対象

def targets():
    """翻訳の対象（キー → 原稿の絶対パス）。キーは、.md は ROOT からの相対パス、テンプレートは templates/<名前>。
    日本語を含まないファイルは対象にしない（翻訳版でも日本語版のものがそのまま使われる）"""
    out = {}
    for d in DIRS:
        for dirpath, _, files in os.walk(os.path.join(ROOT, d)):
            for name in files:
                if name.endswith('.md'):
                    path = os.path.join(dirpath, name)
                    out[os.path.relpath(path, ROOT).replace(os.sep, '/')] = path
    out['INDEX.md'] = os.path.join(ROOT, 'INDEX.md')
    for name in sorted(os.listdir(TEMPLATES)):
        if name.endswith('.html'):
            out['templates/' + name] = os.path.join(TEMPLATES, name)
    return {k: v for k, v in sorted(out.items()) if JAPANESE.search(read_text(v))}


def out_path(lang, key):
    return os.path.join(I18N, lang, *key.split('/'))


def manifest_path(lang):
    return os.path.join(I18N, lang, '.manifest.json')


def load_manifest(lang):
    try:
        with open(manifest_path(lang), encoding='utf-8') as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


# ---------------------------------------------------------------- 検査

def split_code(text):
    """コードブロックの外の行（prose）と、コードブロック（先頭は開きの行、以降は中身）に分ける"""
    prose, blocks, cur = [], [], None
    for line in text.split('\n'):
        if FENCE.match(line):
            if cur is None:
                cur = [line.strip()]
            else:
                blocks.append(tuple(cur))
                cur = None
            continue
        if cur is not None:
            cur.append(line)
        else:
            prose.append(line)
    if cur is not None:
        blocks.append(tuple(cur))
    return prose, blocks


def md_facts(text):
    prose, blocks = split_code(text)
    joined = '\n'.join(prose)
    heads = [(len(m.group(1)), m.group(2)) for m in (HEADING.match(l) for l in prose) if m]
    bare = re.sub(r'\\.', '', re.sub(r'`[^`\n]+`', '', joined))      # コードスパンとエスケープ（\*  \[ など）を除いた散文
    return {
        'linktexts': re.findall(r'\[([^\]]*)\]\([^)]*\)', joined),    # リンクの文字（日本語を含まないものは訳文にも残る）
        'emph': bare.count('*'),                                      # 強調記号の数
        'brackets': (bare.count('['), bare.count(']')),               # 角括弧の数（リンクや強調の崩れを拾う）
        'prose': prose,
        'blocks': blocks,
        'heads': heads,
        'lines': sum(1 for l in prose if l.strip()),
        'inline': re.findall(r'`[^`\n]+`', joined),
        # リンク先と、コードスパンの外の URL（ASCII の範囲だけ。直後の日本語や文末の句読点を巻き込まない）
        'links': re.findall(r'\]\(([^)\s]*)', joined) + [
            u.rstrip(".,;:!?'") for u in re.findall(r"https?://[A-Za-z0-9._~:/?#@!$&'*+,;=%-]+", re.sub(r'`[^`\n]+`', '', joined))],
        'admon': re.findall(r'^\s*!!! (\w+)', joined, re.M),
        'deprecated': sum(1 for l in prose if '"非推奨"' in l),
        'markers': [m for l in prose for m in MARKER_LABELS if l.lstrip().startswith(m)],
        'bullets': [(len(l) - len(l.lstrip()), l.lstrip()[:1].isdigit()) for l in prose if re.match(r'^\s*(?:[-*+]|\d+\.)\s', l)],
        'pipes': [len(re.findall(r'(?<!\\)\|', l)) for l in prose if l.lstrip().startswith('|')],
        'baseware': [BASEWARE.findall(l) for l in prose if l.lstrip().startswith('**対応:**')],
    }


def line_hint(src_prose, out_prose):
    """行数が合わないとき、原文のどの行が訳文に無いか（行の種類の並びを突き合わせて）を、訳し直しの手掛かりとして返す"""
    def kind(line):
        m = re.match(r'^(\s*)([-*+]|\d+\.|#+|\||!!!)?', line)
        return (len(m.group(1)), m.group(2) or 'p')
    a = [l for l in src_prose if l.strip()]
    b = [l for l in out_prose if l.strip()]
    sm = difflib.SequenceMatcher(None, [kind(l) for l in a], [kind(l) for l in b], autojunk=False)
    missing = [l for op, i1, i2, _, _ in sm.get_opcodes() if op in ('delete', 'replace') for l in a[i1:i2]]
    extra = [l for op, _, _, j1, j2 in sm.get_opcodes() if op in ('insert', 'replace') for l in b[j1:j2]]
    hint = ''
    if missing:
        hint += (' 訳文で省かれた可能性のある原文の行（行の種類での推定なので、近くの別の行かもしれない）: ' + ' / '.join(f'「{l.strip()[:60]}」' for l in missing[:3]) +
                 '。1 行も省略・統合しないこと。特に、コードブロックの前後にある短いつなぎの行（「と書く事になります。」など）も、1 行として訳すこと。')
    if extra:
        hint += ' 原文に無い行が増えている: ' + ' / '.join(f'「{l.strip()[:60]}」' for l in extra[:3]) + '。'
    return hint


def check_md(src, out, key, check_language=True, lang=None):
    """訳文 out が、原文 src と同じ構造か。違う点を文字列のリストで返す（空なら通った）"""
    a, b = md_facts(src), md_facts(out)
    errors = []
    if [l for l, _ in a['heads']] != [l for l, _ in b['heads']]:
        errors.append(f'見出しの数・レベルが違う（原文 {[l for l, _ in a["heads"]]}、訳文 {[l for l, _ in b["heads"]]}）')
    else:
        for (_, ta), (_, tb) in zip(a['heads'], b['heads']):
            # build.py は「記述例」で始まる見出しを記述例の節とみなす（前方一致）。「目次」「一覧」は字面が完全に同じものだけ
            if (ta in MARKER_HEADINGS and ta != tb) or (ta.startswith('記述例') and not tb.startswith('記述例')):
                errors.append(f'見出し「{ta}」は訳さずそのまま残すこと（訳文は「{tb}」）')
    if a['blocks'] != b['blocks']:
        errors.append('コードブロック（言語指定・中身・数）が原文と違う。コードブロックは一字も変えないこと')
    for name in ('inline', 'links', 'linktexts', 'admon', 'deprecated', 'markers', 'bullets', 'pipes', 'baseware', 'lines', 'emph', 'brackets'):
        if name == 'linktexts':
            # 日本語を含まないリンクの文字（SSP、OnBoot など）は、訳文のリンクの文字にもそのまま残る（別の語句にリンクを付け替えない）
            keep = Counter(x for x in a[name] if not JAPANESE.search(x))
            same = len(a[name]) == len(b[name]) and not (keep - Counter(b[name]))
        elif name == 'inline':
            # コードスパンは、日本語を含まないものはそのまま（語順が変わって登場順が入れ替わるのは構わない）。
            # 日本語を含むもの（`--名前=値` など）は訳してよい（数だけ合わせる）
            keep = Counter(x for x in a[name] if not JAPANESE.search(x))
            same = len(a[name]) == len(b[name]) and not (keep - Counter(b[name]))
        elif name == 'links':
            same = sorted(a[name]) == sorted(b[name])      # 語順が変わっても、リンク先が同じならよい
        else:
            same = a[name] == b[name]
        if not same:
            labels = {
                'inline': 'コードスパン（`…`）', 'links': 'リンク先・URL', 'admon': '!!! の囲みの種類と数', 'deprecated': '!!! warning "非推奨" の数',
                'markers': '**カテゴリ:** **対応:** **既定値:** の行（ラベルは訳さずそのまま）', 'bullets': '箇条書きの数と字下げ',
                'pipes': '表の各行の | の数', 'baseware': '**対応:** 行のベースウェア名（Materia / SSP / CROW / Ninix）',
                'lines': '空でない行の数（原文の行構成を保つこと）',
                'linktexts': 'リンクの文字（日本語を含まないもの、例: SSP や OnBoot は、そのままリンクの文字として残すこと）',
                'emph': '強調記号（*）の数。*…* で囲む範囲も原文と同じにすること', 'brackets': '角括弧 [ ] の数（リンクの [text](url) や強調が崩れている）',
            }
            show = lambda v: len(v) if isinstance(v, list) else v
            detail = f'（原文 {show(a[name])}、訳文 {show(b[name])}）'
            if name == 'lines':
                detail += line_hint(a['prose'], b['prose'])
            errors.append(f'{labels[name]}が原文と違う{detail}')
    if check_language and not errors:
        if not a['heads'] and not any(JAPANESE.search(l) for l in a['prose']):
            return errors
        left = len(HIRAGANA.findall(strip_fixed('\n'.join(b['prose']))))
        base = len(HIRAGANA.findall(strip_fixed('\n'.join(a['prose']))))
        if left >= 2 and left > base * 0.3:
            errors.append(f'日本語（ひらがな {left} 字）が訳されずに残っている')
        errors += wrong_language('\n'.join(a['prose']), '\n'.join(b['prose']), lang)
    return errors


HAN = re.compile(r'[一-鿿]')
JA_TEXT = re.compile(r'[぀-ヿ一-鿿]')


def wrong_language(src_text, out_text, lang):
    """中国語の訳文が、中国語になっているか（モデルが英語で返すことがある）。原文に訳すべき日本語があるのに、
    訳文に漢字がほとんど無ければ、別の言語で返したとみなす。構造の語（記述例・目次・一覧）の漢字は数えない"""
    if lang not in ('zh', 'zh-Hant'):
        return []
    def bare(t):
        t = strip_fixed(t)
        for w in MARKER_HEADINGS:
            t = t.replace(w, '')
        return t
    base = len(JA_TEXT.findall(bare(src_text)))
    han = len(HAN.findall(bare(out_text)))
    if base >= 4 and han < base * 0.15:
        return [f'訳文が中国語になっていない（原文の日本語 {base} 字に対し、訳文の漢字は {han} 字）。英語で返さず、必ず {LANGS[lang]} で訳すこと（Write the translation in {LANGS[lang]}, not in English）']
    return []


def strip_fixed(text):
    """訳さずに残す部分（コードスパン・リンク先・ラベル・構造の語）を除いた本文"""
    text = re.sub(r'`[^`\n]+`', '', text)
    text = re.sub(r'\]\([^)]*\)', ']()', text)
    for m in MARKER_LABELS:
        text = text.replace(m, '')
    return text.replace('"非推奨"', '').replace('非対応', '').replace('未対応', '')


def html_skeleton(text):
    """HTML の断片の、タグの並び。alt / title / aria-label / value / placeholder の中身（訳す字）は無視する"""
    text = re.sub(r'\b(alt|title|aria-label|value|placeholder)="[^"]*"', r'\1=""', text)
    return re.findall(r'<[^>]*>', text)


def html_text(text):
    """HTML の断片の、訳す字（タグの外の文字と、alt / title / aria-label / value / placeholder の中身）"""
    attrs = re.findall(r'\b(?:alt|title|aria-label|value|placeholder)="([^"]*)"', text)
    return re.sub(r'<[^>]*>', '', text) + '\n' + '\n'.join(attrs)


def check_html(src, out, key, check_language=True, lang=None):
    errors = []
    if html_skeleton(src) != html_skeleton(out):
        errors.append('タグ・属性（href・class・id など）が原文と違う。訳してよいのはタグの外の文字と alt / title / aria-label / value / placeholder だけ')
    if check_language and not errors:
        left = len(HIRAGANA.findall(re.sub(r'<[^>]*>', '', out)))
        base = len(HIRAGANA.findall(re.sub(r'<[^>]*>', '', src)))
        if left >= 2 and left > base * 0.3:
            errors.append(f'日本語（ひらがな {left} 字）が訳されずに残っている')
        errors += wrong_language(html_text(src), html_text(out), lang)
    return errors


def check(src, out, key, check_language=True, lang=None):
    fn = check_html if key.endswith('.html') else check_md
    return fn(src, out, key, check_language, lang)


# ---------------------------------------------------------------- プロンプト

def load_glossary(lang):
    """i18n/glossary.tsv（ja<TAB>en<TAB>zh-Hant<TAB>zh）から、その言語で固定する訳語の行を返す"""
    if not os.path.isfile(GLOSSARY):
        return []
    rows = [l.rstrip('\n').split('\t') for l in read_text(GLOSSARY).split('\n') if l.strip() and not l.startswith('#')]
    head = rows[0]
    col = head.index(lang)
    return [f'{r[0]} = {r[col]}' for r in rows[1:] if len(r) > col and r[col].strip()]


def system_prompt(lang):
    glossary = load_glossary(lang)
    text = f"""You are translating the UKADOC specification into {LANGS[lang]}. UKADOC documents the Ukagaka desktop-mascot ecosystem (SSP, SHIORI, SAORI, Sakura Script, ghosts, shells, balloons). The source is Japanese Markdown (or an HTML fragment of the site frame). Readers are developers; be accurate and concise, in a plain technical-documentation tone.

OUTPUT LANGUAGE: {LANGS[lang]}. Every translated sentence must be written in {LANGS[lang]}, even if the glossary below or the technical terms are in English. Never answer in English unless the target language is English.

INPUT FORMAT: one or more files, each wrapped like
<<<FILE path>>>
...file content...
<<<END>>>
Return every file in exactly the same wrapper, with the same path, in the same order. Output nothing else: no commentary, no extra code fence around the output.

STRUCTURE MUST BE PRESERVED EXACTLY (an automatic checker compares it; a failed file is thrown away):
- Same number and level of headings, same list nesting and indentation, same tables (rows and columns), same `!!!` admonition blocks (keep the 4-space indentation of their bodies), same blank-line layout, same `<br />` tags. Keep one source line as one output line.
- Translate EVERY line. Never omit, merge, split or reorder lines, even a short line that looks redundant, a pointer to another page, or a line that repeats something said elsewhere.
- Japanese often splits one sentence around a fenced code block: the line before ends with 「…には、」 and the line after is a short continuation such as 「と書く事になります。」. Both lines must still appear in the output, each as its own line (for example "Add the following to descript.txt:" before the block and "Write it like this." after it), even though English could do without the second one.
- Never change: fenced code blocks (their whole content, including Japanese sample text and comments), inline code spans (`...`), link targets (paths, URLs, #fragments), image paths, identifiers, event names, tag names, file names, numbers and versions (e.g. SSP 2.7.23).
- Link text, heading text, and prose are translated. In headings such as `# name,ゴースト名`, keep the identifier part and translate only the Japanese part.
- These Japanese words are structural markers used by the build system. Keep them byte-for-byte; translate only the text that follows them:
  * the labels `**カテゴリ:**`, `**対応:**`, `**既定値:**`
  * the headings `## 記述例`, `## 目次`, `## 一覧`. A heading that merely starts with 記述例 must keep that prefix byte-for-byte in every language (never 记述例, 記述範例 or a translation of it), and only the rest is translated: `## 記述例と基本の書き方` becomes `## {HEADING_EXAMPLE[lang]}`.
  * the admonition title in `!!! warning "非推奨"`
- Baseware names Materia / SSP / CROW / Ninix stay as they are. In a `**対応:**` line, keep the order of the names and express notes like 廃止 or 非対応 as plain words ("deprecated", "not supported" / 廢止, 不支援 / 废止, 不支持).
- In HTML fragments, change nothing except the text between tags and the values of alt / title / aria-label / value / placeholder.
- A file without translatable text is returned unchanged.

STYLE: Translate Japanese 「だ/である」 prose into plain declarative sentences. Keep terminology consistent across files. "Sakura Script" (さくらスクリプト) is a proper name.
"""
    if glossary:
        text += '\nGLOSSARY (use exactly these renderings):\n' + '\n'.join(glossary) + '\n'
    return text


def user_message(files, problems=None):
    body = '\n'.join(f'<<<FILE {key}>>>\n{src.rstrip(chr(10))}\n<<<END>>>' for key, src in files)
    if problems:
        body = ('Your previous translation of this file failed the automatic structure check:\n- ' + '\n- '.join(problems) +
                '\nTranslate it again and fix these problems.\n\n') + body
    return body


WRAP = re.compile(r'<<<FILE (.+?)>>>\n(.*?)\n?<<<END>>>', re.S)


def parse_reply(text):
    text = text.strip()
    if text.startswith('```') and text.endswith('```'):      # 全体を囲んでしまったとき
        text = re.sub(r'^```\w*\n', '', text)
        text = re.sub(r'\n```$', '', text)
    return {m.group(1).strip(): m.group(2) for m in WRAP.finditer(text)}


# ---------------------------------------------------------------- API

class Budget:
    def __init__(self, max_cost, price_in, price_out):
        self.max_cost, self.price_in, self.price_out = max_cost, price_in, price_out
        self.tokens_in = self.tokens_out = 0
        self.requests = 0
        self.lock = threading.Lock()

    @property
    def cost(self):
        return (self.tokens_in * self.price_in + self.tokens_out * self.price_out) / 1_000_000

    def add(self, usage):
        with self.lock:
            self.requests += 1
            self.tokens_in += usage.get('prompt_tokens', 0)
            self.tokens_out += usage.get('completion_tokens', 0)

    def exhausted(self):
        return self.cost >= self.max_cost


class Stop(Exception):
    """費用の上限に達した"""


def chat(cfg, budget, system, user):
    """OpenAI 互換の /chat/completions を 1 回呼ぶ。(本文, finish_reason) を返す。429・5xx・通信の失敗は待って再試行する"""
    if budget.exhausted():
        raise Stop()
    payload = json.dumps({
        'model': cfg['model'],
        'messages': [{'role': 'system', 'content': system}, {'role': 'user', 'content': user}],
    }).encode('utf-8')
    url = cfg['base_url'].rstrip('/')
    if not url.endswith('/chat/completions'):     # base_url は /v1 まででも、/chat/completions まででもよい
        url += '/chat/completions'
    req = urllib.request.Request(url, data=payload, method='POST', headers={
        'Content-Type': 'application/json', 'Authorization': 'Bearer ' + cfg['api_key']})
    delay = 5
    for attempt in range(8):
        try:
            with urllib.request.urlopen(req, timeout=600) as res:
                data = json.loads(res.read().decode('utf-8'))
            budget.add(data.get('usage') or {})
            choice = data['choices'][0]
            return choice['message']['content'] or '', choice.get('finish_reason')
        except urllib.error.HTTPError as e:
            body = e.read().decode('utf-8', 'replace')[:300]
            if e.code in (429, 500, 502, 503, 504) and attempt < 7:
                wait = float(e.headers.get('Retry-After') or delay)
                print(f'  HTTP {e.code}。{wait:.0f} 秒待つ', file=sys.stderr)
                time.sleep(wait)
                delay = min(delay * 2, 120)
                continue
            raise RuntimeError(f'HTTP {e.code}: {body}')
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            if attempt < 7:
                print(f'  通信エラー（{e}）。{delay} 秒待つ', file=sys.stderr)
                time.sleep(delay)
                delay = min(delay * 2, 120)
                continue
            raise
    raise RuntimeError('再試行を使い切った')


# ---------------------------------------------------------------- 翻訳

def normalize(text):
    return text.replace('\r\n', '\n').strip('\n') + '\n'


def batches(items):
    """(key, 原稿) のリストを、小さいものはまとめて、大きいものは単独のリクエストの単位にする"""
    out, cur, size = [], [], 0
    for key, src in items:
        n = len(src.encode('utf-8'))
        if cur and (size + n > BATCH_BYTES or len(cur) >= BATCH_FILES):
            out.append(cur)
            cur, size = [], 0
        cur.append((key, src))
        size += n
    if cur:
        out.append(cur)
    return out


def translate_batch(cfg, budget, lang, system, files, check_language=True, fallback=True):
    """files: [(key, 原稿)]。{key: 訳文}（検査に通ったもの）と {key: 理由のリスト}（通らなかったもの）を返す"""
    done, failed = {}, {}
    sources = dict(files)
    reply, finish = chat(cfg, budget, system, user_message(files))
    got = parse_reply(reply)
    for key, src in files:
        if finish == 'length' and key not in got:
            failed[key] = ['出力が途中で切れた']
            continue
        if key not in got:
            failed[key] = ['返答に見つからなかった']
            continue
        out = normalize(got[key])
        problems = check(sources[key], out, key, check_language, lang)
        if problems:
            failed[key] = problems
        else:
            done[key] = out
    # 通らなかったファイルは、理由を添えて 1 ファイルずつ訳し直す
    for key in list(failed):
        problems = failed[key]
        for _ in range(RETRIES):
            reply, finish = chat(cfg, budget, system, user_message([(key, sources[key])], problems))
            got = parse_reply(reply)
            if key not in got:
                problems = ['返答に見つからなかった' if finish != 'length' else '出力が途中で切れた']
                continue
            out = normalize(got[key])
            problems = check(sources[key], out, key, check_language, lang)
            if not problems:
                done[key] = out
                del failed[key]
                break
        else:
            failed[key] = problems
    # それでも通らないファイルは、細かい塊（約 1.2KB）に分けて訳す（塊が短いほど、行の省略や統合が起きにくい）
    if fallback:
        for key in list(failed):
            chunks = split_chunks(sources[key], FINE_BYTES)
            if len(chunks) < 2 and len(sources[key].split('\n')) < 8:
                continue
            parts = []
            for i, chunk in enumerate(chunks):
                sub = f'{key}#f{i + 1}'
                d, f = translate_batch(cfg, budget, lang, system, [(sub, chunk)], check_language, fallback=False)
                if sub not in d:
                    break
                parts.append(d[sub])
            else:
                joined = normalize('\n'.join(p.rstrip('\n') + '\n' for p in parts))
                problems = check(sources[key], joined, key, check_language, lang)
                if not problems:
                    done[key] = joined
                    del failed[key]
    return done, failed


def split_chunks(src, target=6000):
    """大きいファイルを、コードブロックの外の見出し行（見出しが無く長いときは空行）で、約 target バイトずつに分ける"""
    chunks, cur, size, in_fence = [], [], 0, False
    for line in src.split('\n'):
        if FENCE.match(line):
            in_fence = not in_fence
        if not in_fence and cur and size >= target and (HEADING.match(line) or (size >= target * 2 and not line.strip())):
            chunks.append('\n'.join(cur))
            cur, size = [], 0
        cur.append(line)
        size += len(line.encode('utf-8')) + 1
    if cur:
        chunks.append('\n'.join(cur))
    return chunks


def translate_big(cfg, budget, lang, system, key, src, check_language=True):
    """大きいファイルは、見出しの切れ目で分けて 1 つずつ訳し、つなぎ直す（1 回の出力が短いほど、行の取り違えが減る）。
    各部分と、つないだ全体の両方を検査する"""
    parts = []
    for i, chunk in enumerate(split_chunks(src)):
        sub = f'{key}#{i + 1}'
        done, failed = translate_batch(cfg, budget, lang, system, [(sub, chunk)], check_language)
        if sub not in done:
            return {}, {key: [f'分割 {i + 1} 番目: ' + '; '.join(failed.get(sub, ['不明']))]}
        parts.append(done[sub])
    joined = normalize('\n'.join(p.rstrip('\n') + '\n' for p in parts))
    problems = check(src, joined, key, check_language, lang)
    if problems:
        return {}, {key: ['つないだ全体: ' + p for p in problems]}
    return {key: joined}, {}


def write_translation(lang, key, text):
    path = out_path(lang, key)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def save_manifest(lang, manifest):
    path = manifest_path(lang)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=0, sort_keys=True)
        f.write('\n')
    os.replace(tmp, path)


def recheck(lang, all_targets, manifest):
    """書き出し済みの訳文に、今の検査をもう一度当てる。通らないものはマニフェストから外す（次の実行で訳し直される）"""
    bad = 0
    for key, path in all_targets.items():
        out_file = out_path(lang, key)
        if not os.path.isfile(out_file):
            continue
        problems = check(normalize(read_text(path)), read_text(out_file), key, True, lang)
        if problems:
            bad += 1
            manifest.pop(key, None)
            print(f'  [{lang}] {key}: {"; ".join(problems)}')
    save_manifest(lang, manifest)
    print(f'[{lang}] 検査に通らない訳文 {bad} 件（次の実行で訳し直す）')


def run_lang(cfg, budget, lang, args, all_targets):
    manifest = load_manifest(lang)
    if args.recheck:
        recheck(lang, all_targets, manifest)
    todo = []
    for key, path in all_targets.items():
        if args.only and not any(o in key for o in args.only):
            continue
        src = normalize(read_text(path))
        if args.force or manifest.get(key) != sha(src) or not os.path.isfile(out_path(lang, key)):
            todo.append((key, src))
    if args.limit:
        todo = todo[:args.limit]
    # 大きいファイルから出す（最後に大きいものが残って長引くのを避ける）。小さいものは近いパスのものをまとめる
    small = [t for t in todo if len(t[1].encode('utf-8')) <= BATCH_BYTES]
    large = [t for t in todo if len(t[1].encode('utf-8')) > BATCH_BYTES]
    groups = [[t] for t in sorted(large, key=lambda t: -len(t[1]))] + batches(small)
    chars = sum(len(s) for _, s in todo)
    print(f'[{lang}] 対象 {len(todo)} / {len(all_targets)} ファイル、{chars} 字、{len(groups)} リクエスト')
    if args.dry_run or not todo:
        return {'todo': len(todo), 'chars': chars, 'requests': len(groups), 'failed': {}}

    system = system_prompt(lang)
    lock = threading.Lock()
    failed_all = {}
    sources = dict(todo)

    def work(group):
        try:
            if len(group) == 1 and len(group[0][1].encode('utf-8')) > BATCH_BYTES:
                done, failed = translate_big(cfg, budget, lang, system, group[0][0], group[0][1], not args.no_language_check)
            else:
                done, failed = translate_batch(cfg, budget, lang, system, group, not args.no_language_check)
        except Stop:
            return 'stop'
        except Exception as e:      # 1 リクエストの失敗で全体を止めない
            with lock:
                for key, _ in group:
                    failed_all[key] = [f'リクエストの失敗: {e}']
            return 'error'
        with lock:
            for key, text in done.items():
                write_translation(lang, key, text)
                manifest[key] = sha(sources[key])
            failed_all.update(failed)
            save_manifest(lang, manifest)
            print(f'  [{lang}] {len(done)} 件完了、{len(failed)} 件失敗（費用 ${budget.cost:.3f} / ${budget.max_cost:.2f}）')
        return 'ok'

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        results = list(pool.map(work, groups))
    if 'stop' in results:
        print(f'[{lang}] 費用の上限（${budget.max_cost:.2f}）に達したので止めた。再実行すると続きから訳す')
    return {'todo': len(todo), 'chars': chars, 'requests': len(groups), 'failed': failed_all}


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
    load_env()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--lang', help='言語コード（カンマ区切り）。省略時は ' + ','.join(LANGS))
    ap.add_argument('--only', action='append', help='キーにこの文字列を含むファイルだけ（複数指定可）')
    ap.add_argument('--limit', type=int, help='先頭からこの数のファイルだけ')
    ap.add_argument('--force', action='store_true', help='ハッシュが同じでも訳し直す')
    ap.add_argument('--recheck', action='store_true', help='書き出し済みの訳文に今の検査を当て直し、通らないものを訳し直しの対象に戻す')
    ap.add_argument('--dry-run', action='store_true', help='API を呼ばず、対象と費用の目安だけ出す')
    ap.add_argument('--jobs', type=int, default=8, help='並列のリクエスト数（既定 8）')
    ap.add_argument('--max-cost', type=float, default=10.0, help='費用の上限（米ドル。既定 10）')
    ap.add_argument('--no-language-check', action='store_true', help='「日本語が訳されずに残っている」検査を外す')
    args = ap.parse_args()

    langs = args.lang.split(',') if args.lang else list(LANGS)
    for lang in langs:
        if lang not in LANGS:
            sys.exit(f'知らない言語: {lang}（{", ".join(LANGS)}）')
    cfg = {
        'api_key': os.environ.get('TRANSLATE_API_KEY', ''),
        'base_url': os.environ.get('TRANSLATE_BASE_URL', ''),
        'model': os.environ.get('TRANSLATE_MODEL', 'gpt-6-luna'),
    }
    if not args.dry_run and not (cfg['api_key'] and cfg['base_url']):
        sys.exit('TRANSLATE_API_KEY と TRANSLATE_BASE_URL を環境変数か .env に書くこと')
    budget = Budget(args.max_cost, float(os.environ.get('TRANSLATE_PRICE_IN', '0.1')), float(os.environ.get('TRANSLATE_PRICE_OUT', '0.5')))

    all_targets = targets()
    summary = {lang: run_lang(cfg, budget, lang, args, all_targets) for lang in langs}

    if args.dry_run:
        # 目安: 入力は原稿の 1 字を約 1 トークン + 1 リクエストあたり前置き 2000 トークン、出力は原稿の字数の約 0.8 倍
        for lang, s in summary.items():
            tin = s['chars'] + 2000 * s['requests']
            tout = int(s['chars'] * 0.8)
            print(f'[{lang}] 目安: 入力 約 {tin} トークン、出力 約 {tout} トークン → 約 ${(tin * budget.price_in + tout * budget.price_out) / 1e6:.2f}')
        return
    print(f'リクエスト {budget.requests} 回、入力 {budget.tokens_in} / 出力 {budget.tokens_out} トークン、費用 ${budget.cost:.3f}')
    bad = {(lang, key): why for lang, s in summary.items() for key, why in s['failed'].items()}
    if bad:
        print(f'訳せなかったファイル {len(bad)} 件（日本語のまま出る。理由は下。再実行で再挑戦）:')
        for (lang, key), why in sorted(bad.items()):
            print(f'  [{lang}] {key}: {"; ".join(why)}')
        sys.exit(1)


if __name__ == '__main__':
    main()

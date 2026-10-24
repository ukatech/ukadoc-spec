"""GitHub Pages 用に原稿を _site_src/ へ写す。

- INDEX.md を index.md（トップページ）にし、INDEX.md へのリンクも書き換える
- 各ディレクトリの index.md の「## 一覧」が、そのディレクトリの項目（.md とサブディレクトリ）と
  過不足なく一致しているかを検査する（食い違いがあれば止める）
- llms.txt をサイトのルートに置く
原稿そのものは書き換えない。
"""
import os
import re
import shutil
import sys
from urllib.parse import unquote

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(ROOT, '_site_src')
DIRS = ['manual', 'descript', 'list', 'spec', 'dev', 'memo']
INDEX_LINK = re.compile(r'(\]\((?:\.\./)*)INDEX\.md')
LIST_LINK = re.compile(r'^- \[.*\]\(([^)]+)\)\s*$')


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def write(rel, text):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def check_index(directory):
    """directory/index.md の「## 一覧」と、ディレクトリの中身を突き合わせる。エラーのリストを返す"""
    index = os.path.join(directory, 'index.md')
    rel = os.path.relpath(index, ROOT).replace(os.sep, '/')
    text = read(index)
    if '\n## 一覧\n' not in text:
        return []
    section = text.split('\n## 一覧\n', 1)[1].split('\n## ', 1)[0]
    listed = []
    for line in section.split('\n'):
        m = LIST_LINK.match(line)
        if m:
            target = unquote(m.group(1))
            parts = target.split('/')
            listed.append(parts[0])
    actual = []
    for name in os.listdir(directory):
        full = os.path.join(directory, name)
        if os.path.isdir(full):
            actual.append(name)
        elif name.endswith('.md') and name != 'index.md':
            actual.append(name)
    errors = []
    for name in sorted(set(actual) - set(listed)):
        errors.append(f'{rel}: 「## 一覧」に {name} が無い')
    for name in sorted(set(listed) - set(actual)):
        errors.append(f'{rel}: 「## 一覧」の {name} が無い')
    for name in sorted({n for n in listed if listed.count(n) > 1}):
        errors.append(f'{rel}: 「## 一覧」に {name} が 2 回以上ある')
    return errors


def main():
    errors = []
    for d in DIRS:
        for dirpath, _, files in os.walk(os.path.join(ROOT, d)):
            if 'index.md' in files:
                errors += check_index(dirpath)
    if errors:
        sys.exit('エラー: 一覧の食い違い\n  ' + '\n  '.join(errors))
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    write('index.md', INDEX_LINK.sub(r'\1index.md', read(os.path.join(ROOT, 'INDEX.md'))))
    shutil.copy(os.path.join(ROOT, '.nav.yml'), os.path.join(OUT, '.nav.yml'))
    shutil.copy(os.path.join(ROOT, 'llms.txt'), os.path.join(OUT, 'llms.txt'))
    shutil.copytree(os.path.join(ROOT, 'assets'), os.path.join(OUT, 'assets'))
    for d in DIRS:
        shutil.copytree(os.path.join(ROOT, d), os.path.join(OUT, d))


if __name__ == '__main__':
    main()

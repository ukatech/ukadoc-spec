# HTML 版からの移行メモ

旧 HTML 版（`ukatech/ukadoc` の `manual/*.html`、コミット `9eb14c5` 時点）をこのリポジトリの Markdown に機械的に変換した。このリポジトリが正本で、並存期間中に ukadoc 側へ入った変更は `9eb14c5` 以降のコミット（`git log 9eb14c5..master -- manual`）で追い、手で写す。変換は本文の文言を変えない決定的なスクリプトで行い、変換後に次の検査を通している（変換結果は、書式の崩れを別に見るレビューも通した）。

- 項目（ファイル）ごとに、元 HTML の本文テキストと、生成した Markdown をサイトと同じ拡張で HTML に戻した本文テキストが、空白を除いて一致する
- ページごとに、元 HTML の本文の文字が 1 文字も欠けずにいずれかの項目に入っている
- `id-map.json` の見出しへのアンカーが、生成した Markdown の見出しの id と一致し、飛び先の見出しの文字が元 HTML の見出しと同じである。本文中のリンクのアンカーも、すべて実在する見出しを指す
- 元の `pre`・複数行の例の行構成が、コードブロックの行と一致する

## id-map.json

キーは `旧ページ名#旧id`（例: `list_shiori_event#OnBoot`、`list_sakura_script#_!_execute,filewatch,パス,オプション..._`）、値は `path`（リポジトリ内のパス）と `anchor`（ファイル内の見出しの id。ファイル全体を指すときは `null`）。旧 URL `…/manual/list_shiori_event.html#OnBoot` は、ページ名 `list_shiori_event` と id `OnBoot` で引ける。

## 書式を変えた点

文言は変えていないが、HTML の表現を Markdown に置き換えた。

- 対応ベースウェアのアイコン（`<img alt="SSP"> 2.8.91`）を `**対応:** SSP 2.8.91` の文字にした
- 既定値（`p.default`、旧 CSS が「既定値: 」を補っていた）を `**既定値:**` の行にした
- 非推奨の項目（`dt.entry.deprecated`）に `!!! warning "非推奨"` を加えた
- 項目のカテゴリを `**カテゴリ:**` の行に出した。各 `index.md` の `## 一覧` は新しく作った
- 見出しを持たない補足は、タイトルを「補足」とした
- `dl` は `- **項目**: 説明` の箇条書きにした
- 本文中のさくらスクリプトのタグを、コードスパンで囲んだ
- 旧版では `aside`/`div.passage.hint` に CSS が見出しを付けていた箇所に、`!!! tip "ヒント"` を付けた

## 変換しなかったもの

- `ssphelp/` `ssphelp_src/` `ssphelp_builder/`（SSP ヘルプ。HTML 版のまま）
- 旧版のナビゲーション（`navigation.html` `sidemenu.html` のフレーム、各ページの `nav.menu-header`、`section.navigation-bar`）。目次は `INDEX.md` と各 `index.md` が担う
- 旧版の動的な部品（`ghost_status.js` の「対象ゴースト」選択、`sakura_player.js`、`index.html` の `?event_name=` 転送スクリプト、`spec_sstp.html` の SSTP 試行用 `textarea`）
- `sitemap.xml`、各種 CSS、各ページ先頭のバナー画像（`ukadoc_banner1.png`）とサイトタイトル行
- `<p><code>行<br />行</code></p>` のように書かれていた複数行の例は、コードブロックにした（本文の段落内の `<br />` は、そのまま `<br />` で残している）

## 変換スクリプト

`tools/` に、変換と検査に使ったスクリプトを残してある（一度きりの作業用で、パスは作業時のもの）。**再生成には使わないこと**（このリポジトリでの修正が上書きされる）。移行の監査用である。`layout.py` が変換、`names.py` が日本語カテゴリ名の ASCII 名の対応表、`check.py` が上の検査（`verify.py` `coverage.py` を呼ぶ）。

## 旧 HTML の不具合を直した箇所

- `manual_shell.html`: `<dl class="component"` に `>` が無く、最初の `<dt>`（descript.txt）がブラウザで表示されなかった。補って出した
- `dev_bind.html`: 2 つ目の節にも `id="chapter1"` が付いていた（目次は `chapter2` を指す）。`chapter2` とした
- リンクの誤記を直した: `dev_nar.html` の `href="chapterEX2"`、`dev_shell.html` の `href="chapter=3-2"` と `#chapter5`（`#chapter3`）、`manual_directory.html` の `developter_options.txt`、`manual_shell.html` の `element*,パターン定義,…`、`descript_shell_surfaces.html` の `…サーフェスID…`、`list_propertysystem.html` の `currentghost.sound(要素名).index(ID)…`
- 存在しないページへのリンク（`manual_shiori_saori.html`、`manual_animation.html`）は、リンクを外して文字だけ残した
- `list_shiori_event_ex.html` の `reference_OnMahjong` は 2 か所に付いている（先のものが `id-map.json` に入る）

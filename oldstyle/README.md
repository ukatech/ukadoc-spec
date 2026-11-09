# oldstyle: 旧版 UKADOC の見た目を模した静的サイト

`ukatech/ukadoc` の `manual/*.html`（コミット 9eb14c5）の見た目と構造を、このリポジトリの Markdown 原稿から再現する自前のビルド。Zensical・MkDocs は使わない。

```sh
python oldstyle/build.py       # scripts/prepare_site.py で _site_src/ を作り、_site_old/ に出力する
python oldstyle/build.py --no-prepare   # _site_src/ を作り直さない
python oldstyle/check.py       # _site_old/ の内部リンク（ファイル・アンカー・画像）を調べる
```

必要なもの: `markdown` `pymdown-extensions` `lxml` と、`pip install -r requirements.txt` で入る `ukadoc-site`（`sakurascript`・`filetree` の色付け）。
`_site_old/` は静的ファイルなので、`python -m http.server -d _site_old` などで見られる（`file://` でも動く）。

## 作り

| 場所 | 内容 |
|---|---|
| `build.py` | 原稿 → HTML → 旧版の構造に組み替える。出力のファイル名は旧版と同じ（`descript_ghost.html` など） |
| `static/` | 旧版の `base.css` `list.css` `spec.css` `iframes.css`・画像・`sakura_player.js`（そのまま）と、新しい原稿のための補い（`oldstyle.css`）、`translate.js`（翻訳ボタン）、`search.js`（サイト内検索） |
| `templates/` | 旧版の枠（`navigation.html` `sidemenu.html`、目次の表 `menu-header.html`、`frame-open/close.html`）の写し |
| `check.py` | 内部リンクの検査 |

頁の種類は 3 つ（旧版と同じ）。

- `list`（`descript_*` `list_*` `spec_*` のまとめた頁。`list.css`）: `nav.menu-header` + `section.navigation-bar` + `div.categories`。項目は `dl#id > dt.entry + dd.entry`、対応は `ul.supported-baseware`（アイコン）、既定値は `p.default`、記述例は `div.legend`
- `spec`（単独の `spec/*.md`。`spec.css`）: `section.navigation-bar` + `div.text`
- `frame`（`manual_*` `dev_*` `memo*` `index`。`base.css`）: `iframe`（`navigation.html` `sidemenu.html`）の枠 + `main`

旧版からの差:

- 左メニュー・上の帯は旧版と同じく iframe。サイト内検索（`search.html`）は、旧版の Google の site 検索の代わりに、ビルド時に作る `search-index.js` を使う
- 翻訳ボタンは右上に固定（`translate.js`。Translator API が無いブラウザでは出ない）。`sidemenu.html` の iframe は、親の頁で選んだ言語に従う
- 旧版にあった `?event_name=` からのリダイレクト（`index.html`）と、起動中ゴーストの対応状況を色分けする `ghost_status.js` は、移していない

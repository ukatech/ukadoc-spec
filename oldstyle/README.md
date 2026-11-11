# oldstyle: 旧版 UKADOC の見た目を模した静的サイト

`ukatech/ukadoc` の `manual/*.html`（コミット 9eb14c5）の見た目と構造を、このリポジトリの Markdown 原稿から再現する自前のビルド。Zensical・MkDocs は使わない。

```sh
python oldstyle/build.py       # scripts/prepare_site.py で _site_src/ を作り、_site_old/ に出力する
python oldstyle/build.py --no-prepare   # _site_src/ を作り直さない
python oldstyle/check.py       # _site_old/ の内部リンク（ファイル・アンカー・画像）を調べる
python scripts/check_source.py # 原稿の内部リンク（ファイル・見出し・画像）を、原稿のファイル名と行番号つきで調べる
```

必要なもの: `markdown` `pymdown-extensions` `lxml` と、`pip install -r requirements.txt` で入る `ukadoc-site`（`sakurascript`・`filetree` の色付け）。
`_site_old/` は静的ファイルなので、`python -m http.server -d _site_old` などで見られる（`file://` でも動く）。

## 作り

| 場所 | 内容 |
|---|---|
| `build.py` | 原稿 → HTML → 旧版の構造に組み替える。出力のファイル名は旧版と同じ（`descript_ghost.html` など） |
| `static/` | 旧版の `list.css`・画像・`sakura_player.js`（そのまま）と、枠の頁の `base.css`（iframe をやめた作りに直してある）、新しい原稿のための補い（`oldstyle.css`）、`lang.js`（言語切替。`translate.js` はブラウザ翻訳の旧版で、いまは読み込まない）、`search.js`（サイト内検索） |
| `templates/` | 旧版の枠の写し。上の帯（`navigation.html`）と左のメニュー（`sidemenu.html`）は、頁に埋め込む断片（`build.py` の `frame_open()` が `frame-open.html` に差し込む）。ほかに目次の表 `menu-header.html`、`frame-close.html` |
| `check.py` | 出力（`_site_old/`）の内部リンクの検査。エラーは出力 HTML の名前で出る |
| `../scripts/check_source.py` | 原稿（`.md`）の内部リンクの検査。エラーは原稿の `ファイル:行` で出る（MkDocs の strict 相当）。見出しの id の数え方は `prepare_site.py` と同じ。`CLAUDE.md`（例のリンクを含む）は調べない |

頁の種類は 3 つ（旧版と同じ）。

- `list`（`descript_*` `list_*` `spec_*` のまとめた頁。`list.css`）: `nav.menu-header` + `section.navigation-bar` + `div.categories`。項目は `dl#id > dt.entry + dd.entry`、対応は `ul.supported-baseware`（アイコン）、既定値は `p.default`、記述例は `div.legend`
- `spec`（単独の `spec/*.md`。`list.css`）: `list` と同じ形に組む。H2 を 1 項目とし、H3 以下の節を持つものは説明の節（`section.caption`）、持たないものは `dl.entry` になる。最初の H2 より前の文は、頁の題を名前にした項目にする。旧版はこの頁だけ `spec.css`（`div.text`）で見た目が違っていたが、`spec/<名前>/` のまとめた頁とそろえるため、`list.css` に統一した
- `frame`（`manual_*` `dev_*` `memo*` `index`。`base.css`）: 上の帯 `header#navigation` + 左のメニュー `nav.sidebar` + `main`（`section.baseframe > section.body` の flex で並べる）

旧版からの差:

- 仕様書側（list / spec の頁）は、旧版の幅（25% + 65%）のままだと右に余白が残るので、`oldstyle.css` で画面の幅いっぱい（左右 20px の余白）に広げている
- 左のメニュー（枠の頁の `nav.sidebar`、list / spec の `.navigation-bar`）は、画面に付いてくる sticky のフローティング。画面より長いときは、メニューの中だけを縦にスクロールする。list / spec は本文もメニューもフロートで `body` の高さに入らないので、`oldstyle.css` で `body:after` のクリアを足している。狭い画面（720px 以下）では、引き出しになる（下の「狭い画面」）
- 枠の頁の上の帯のタイトル画像（`title2.gif`）は、真ん中（375px）で割って、左半分を左端、右半分を右端に置く（`base.css` の `#navigation_top` の疑似要素）
- 枠の頁の左メニュー・上の帯は、旧版の iframe をやめて頁に直接埋め込む。文字の大きさは仕様書側（list / spec）と同じ（本文 16px）。枠は画面の幅いっぱいに広がり（左右に 14px のすきまを残し、枠の `box-shadow` を見せる）、左のメニューは 280px 固定、残りが本文。狭い画面（720px 以下）ではメニューを畳む（下の「狭い画面」）。サイト内検索（`search.html`）は、旧版の Google の site 検索の代わりに、ビルド時に作る `search-index.js` を使う
- 検索の入力欄はドロップダウン式（`search.js`）。全頁（枠の頁も list / spec の頁も）、右上の翻訳ボタンの左横に入力欄を固定で置く
- 狭い画面（720px 以下）: 1 段組みにし、左のメニューを、左上のボタン（ハンバーガー。`menu.js`）で開く引き出し（ドロワー）にする。暗幕・Esc・メニューの中のリンクで閉じる
  - 引き出しになるのは `#ukadoc-drawer`。枠の頁は `nav.sidebar`（`templates/frame-open.html`）。list / spec の頁は、頁の上の目次の表（`menu-header.html`）と左のナビゲーション（`.navigation-bar`）を、`build.py` の `drawer()` が `div.ukadoc-drawer--wrap` で包んだもの。この包みは、広い画面では `display: contents` で、無いのと同じ
  - `menu.js` は head で同期に読み込み、`<html>` に `js-drawer` を付ける。CSS（`oldstyle.css` の末尾）はこのときだけメニューを畳むので、JavaScript が動かなければ、メニューは本文の上に出る
  - 右上の検索欄・言語ボタンと左上のメニューのボタンは固定なので、`body` の上に 40px 空ける。枠の頁の上の帯のタイトル画像は、右半分の下（ロゴ）だけを出す。幅の広い表は表の中だけを横にスクロールし、画像は幅に収める
- 言語切替は `lang.js`。全頁で右上に固定（検索欄の右横）。翻訳版の頁では、頭に機械翻訳の注記の帯（日本語の原文へのリンクつき）を出す
- 旧版にあった `?event_name=` からのリダイレクト（`index.html`）と、起動中ゴーストの対応状況を色分けする `ghost_status.js` は、移していない

## 公開とビルドの詳細（GitHub Pages）

`main` に push すると GitHub Actions（`.github/workflows/pages.yml`）が `scripts/check_source.py`・`oldstyle/build.py`・`oldstyle/check.py` を順に走らせ、https://ukatech.shillest.net/ukadoc-spec/ に公開する。原稿を書く側の規則は、リポジトリ直下の `CLAUDE.md`。

- 原稿はリポジトリ直下にあるため、`scripts/prepare_site.py` が `_site_src/` に写してからビルドする（`INDEX.md` は `index.md`（トップページ）になる）
- 旧 HTML 版で 1 ページだったもの（`descript/<名前>/`、`list/<名前>/`、`spec/<名前>/` の各ディレクトリ）は、サイトでは 1 ページ（`<ディレクトリ>/index.html`）にまとめて出す。原稿は 1 項目 1 ファイルのまま書き、リンクも `../scope/s-ID.md` や `file.md#見出し` と従来どおり書く。`prepare_site.py` が次のことをする
  - 「## 一覧」の順に、ディレクトリ内の全 `.md` をつなぐ。見出しは入れ子の深さの分だけずらし（ページ H1 → カテゴリ H2 → 項目 H3 → 項目内の節 H4。H6 を超えるとエラー）、`{#id}` で一意な id を振る。項目の id は、ファイル名（重なるときはディレクトリからのパス）で、項目内の節は `項目の id-元の見出しの id` になる（例: `#OnBoot`、`#bang-lock-repaint-記述例`）
  - まとめた項目へのリンクを、まとめたページの見出しへのリンクに書き換える（飛び先の見出しが無いとエラー）
  - `**カテゴリ:**` の行は、親の見出しが示すのでサイトでは省く
- 見た目の構造は `oldstyle/build.py` が作る。JavaScript は、旧版から引き継いだ `sakura_player.js`（さくらスクリプトの記述例の実行ボタン）と、`search.js`（サイト内検索）、`lang.js`（言語切替）、`menu.js`（狭い画面のメニューの開閉）だけ
  - `prepare_site.py` は、頁ごとの判断（どの頁のどの段落か）を attr_list の class にして `_site_src/` の写しに付けるところまでを受け持つ（`bundle-item` `bundle-support` `manual-item` など）
  - `build.py` は、`_site_src/` の Markdown を HTML にし、class と木の形を見て旧版の HTML の構造に組み替える。出力のファイル名は旧版と同じ（`descript_ghost.html` など）。頁の種類は 3 つ（上の「作り」）。対応のベースウェアはアイコン画像（`image/icon_m.png` `icon_s.png` `icon_c.png` `icon_n.png`）で出す。ベースウェアを足すときは `build.py` の `BASEWARE` と画像を足す
  - 記述例とファイル構成の木の色付けは、`site_ext/ukadoc_site/lexers.py` の Pygments レキサー（`sakurascript`・`ss`、`filetree`）。`pyproject.toml` の `pygments.lexers` で登録している。さくらスクリプトの誤りは、ビルドの警告に出る（ビルドは止めない）。色は `oldstyle/static/oldstyle.css`
  - 見た目は `oldstyle/static/` の旧版の CSS（`base.css` `list.css`。`list.css` は旧版のまま。`base.css` は、枠の頁の iframe をやめたとき、上の帯・左メニューの CSS（旧 `iframes.css`）を取り込んで直した）と、新しい原稿のための補い `oldstyle.css`。旧版のままの CSS は、旧版の見た目を変えるとき以外は直さず、足りない分は `oldstyle.css` に書く
  - 翻訳版は、LLM（`scripts/translate.py`）が作った `i18n/<言語>/` の訳文を、日本語の原稿に重ねてビルドする（`python oldstyle/build.py` が、日本語版の後に `i18n/` のある言語を `_site_old/<言語>/` へ続けて出す。`--lang=<言語>` でその言語だけ、`--no-langs` で日本語版だけ）
    - 見出しの id は、日本語の原稿から作る（訳した見出しでも、リンクの `#見出し` が切れない）。構造の判定に使う日本語の語（`**カテゴリ:**` `**対応:**` `**既定値:**`、`## 記述例` `## 目次` `## 一覧`、`!!! warning "非推奨"`）は訳文でも原文のまま残し、表示のときだけ `build.py` の `LABELS` で言語ごとの語にする。`NEGATION`（対応の否定の語）には、英語・中国語の言い換えも入れてある
    - 枠（左メニュー・上の帯・検索頁）のテンプレートは、`i18n/<言語>/templates/` に訳したものがあればそちらを使う（`read_template`）
    - 言語メニューに出す言語は、`i18n/<コード>/` があるもの（`build.py` の `LANGS`）。頁の `<meta name="ukadoc-langs">` で `lang.js` に伝える。言語を足すときは、`build.py` の `LANGS` と `LABELS`、`lang.js` の `LANGS` と `NOTICE`、`scripts/translate.py` の `LANGS` と `HEADING_EXAMPLE` に足す
    - `llms.txt`・`_raw/`・オフライン zip は日本語版のもの。zip は、翻訳版も含めて最後に作る
    - 動作の確認は、`python -m http.server -d _site_old` で `/en/` などを開く。リンクの検査は `python oldstyle/check.py --lang=en`
  - サイト内検索（`search.html`）は、ビルド時に `build.py` が作る `search-index.js`（項目・節ごと）を、`search.js` が空白区切りの語の AND で部分一致検索する。旧版の Google の site 検索の代わり
    - 入力欄は、打ち込みが止まってから 250ms 後に検索し、ドロップダウン（上位 8 件と「すべての結果を見る」）を出す。↑↓で選び、Enter で開く（選んでいなければ `search.html?q=` へ）。Esc で閉じる。`search-index.js`（約 1.5MB）は、最初に打ち込んだときに読み込む
    - 全頁（枠の頁も `descript_*` `list_*` `spec_*` も）で、右上（翻訳ボタンの左横）に固定の入力欄を `search.js` が置き、その下にドロップダウンを出す
- `manual/` `dev/` `memo/` と、ディレクトリを持たない `spec/*.md` は、1 ファイル 1 ページのまま
- 章立て（左メニュー `oldstyle/templates/sidemenu.html`、上の帯 `navigation.html`、頁の上の目次の表 `menu-header.html`）は、旧版の HTML の写しを直接書く。ページを足したときは、これらに足す
- `llms.txt`（AI エージェント向けの探し方の案内。`INDEX.md` と各ディレクトリの入口だけを書く）はサイトのルートに置かれる。ページごとの一覧は載せないので、ページを足しても直さなくてよい。ディレクトリを足したときは「構成」に 1 行足す
- オフライン用のアーカイブ `ukadoc-spec-offline.zip` を、`oldstyle/build.py` が出力（`_site_old/`）のルートに作る（`build_offline_zip()`）。サイト一式（HTML・CSS・JS・画像・`llms.txt`・生の Markdown 原稿）を、`ukadoc-spec/` の下にまとめたもの。zip 自身は含めない。`INDEX.md` の冒頭から、`llms.txt` の案内の上でリンクしている（`llms.txt` と同じく絶対 URL）
- 生の Markdown 原稿（`README.md` と `CLAUDE.md` 以外の `.md`）は、リポジトリと同じパスでサイトにも置かれる。`scripts/prepare_site.py` が `_raw/` に写し、`oldstyle/build.py` が出力（`_site_old/`）に重ねる。`llms.txt` や `INDEX.md` の相対リンクは、このおかげでサイト上でも辿れる

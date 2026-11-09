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
| `static/` | 旧版の `list.css` `spec.css`・画像・`sakura_player.js`（そのまま）と、枠の頁の `base.css`（iframe をやめた作りに直してある）、新しい原稿のための補い（`oldstyle.css`）、`translate.js`（翻訳ボタン）、`search.js`（サイト内検索） |
| `templates/` | 旧版の枠の写し。上の帯（`navigation.html`）と左のメニュー（`sidemenu.html`）は、頁に埋め込む断片（`build.py` の `frame_open()` が `frame-open.html` に差し込む）。ほかに目次の表 `menu-header.html`、`frame-close.html` |
| `check.py` | 出力（`_site_old/`）の内部リンクの検査。エラーは出力 HTML の名前で出る |
| `../scripts/check_source.py` | 原稿（`.md`）の内部リンクの検査。エラーは原稿の `ファイル:行` で出る（MkDocs の strict 相当）。見出しの id の数え方は `prepare_site.py` と同じ。`CLAUDE.md`（例のリンクを含む）は調べない |

頁の種類は 3 つ（旧版と同じ）。

- `list`（`descript_*` `list_*` `spec_*` のまとめた頁。`list.css`）: `nav.menu-header` + `section.navigation-bar` + `div.categories`。項目は `dl#id > dt.entry + dd.entry`、対応は `ul.supported-baseware`（アイコン）、既定値は `p.default`、記述例は `div.legend`
- `spec`（単独の `spec/*.md`。`spec.css`）: `section.navigation-bar` + `div.text`
- `frame`（`manual_*` `dev_*` `memo*` `index`。`base.css`）: 上の帯 `header#navigation` + 左のメニュー `nav.sidebar` + `main`（`section.baseframe > section.body` の flex で並べる）

旧版からの差:

- 枠の頁の左メニュー・上の帯は、旧版の iframe をやめて頁に直接埋め込む。文字の大きさは仕様書側（list / spec）と同じ（本文 16px）。枠は画面の幅いっぱいに広がり（左右に 14px のすきまを残し、枠の `box-shadow` を見せる）、左のメニューは 280px 固定、残りが本文。狭い画面（720px 以下）ではメニューが本文の上に積まれる。サイト内検索（`search.html`）は、旧版の Google の site 検索の代わりに、ビルド時に作る `search-index.js` を使う
- 検索の入力欄はドロップダウン式（`search.js`）。枠の頁は上の帯の入力欄に打ち込み、その真下にドロップダウンを出す。仕様書側（list / spec の頁）は、右上の翻訳ボタンの左横に入力欄を固定で置く
- 翻訳ボタンは `translate.js`。枠の頁では上の帯の検索欄の右横にある。仕様書側（list / spec の頁）は右上に固定（検索欄の右横）。Translator API が無いブラウザでは出ない。左メニューも同じ文書なので、本文と一緒に訳される
- 旧版にあった `?event_name=` からのリダイレクト（`index.html`）と、起動中ゴーストの対応状況を色分けする `ghost_status.js` は、移していない

## 公開とビルドの詳細（GitHub Pages）

`main` に push すると GitHub Actions（`.github/workflows/pages.yml`）が `scripts/check_source.py`・`oldstyle/build.py`・`oldstyle/check.py` を順に走らせ、https://ukatech.shillest.net/ukadoc-spec/ に公開する。原稿を書く側の規則は、リポジトリ直下の `CLAUDE.md`。

- 原稿はリポジトリ直下にあるため、`scripts/prepare_site.py` が `_site_src/` に写してからビルドする（`INDEX.md` は `index.md`（トップページ）になる）
- 旧 HTML 版で 1 ページだったもの（`descript/<名前>/`、`list/<名前>/`、`spec/<名前>/` の各ディレクトリ）は、サイトでは 1 ページ（`<ディレクトリ>/index.html`）にまとめて出す。原稿は 1 項目 1 ファイルのまま書き、リンクも `../scope/s-ID.md` や `file.md#見出し` と従来どおり書く。`prepare_site.py` が次のことをする
  - 「## 一覧」の順に、ディレクトリ内の全 `.md` をつなぐ。見出しは入れ子の深さの分だけずらし（ページ H1 → カテゴリ H2 → 項目 H3 → 項目内の節 H4。H6 を超えるとエラー）、`{#id}` で一意な id を振る。項目の id は、ファイル名（重なるときはディレクトリからのパス）で、項目内の節は `項目の id-元の見出しの id` になる（例: `#OnBoot`、`#bang-lock-repaint-記述例`）
  - まとめた項目へのリンクを、まとめたページの見出しへのリンクに書き換える（飛び先の見出しが無いとエラー）
  - `**カテゴリ:**` の行は、親の見出しが示すのでサイトでは省く
- 見た目の構造は `oldstyle/build.py` が作る。JavaScript は、旧版から引き継いだ `sakura_player.js`（さくらスクリプトの記述例の実行ボタン）と、`search.js`（サイト内検索）、`translate.js`（翻訳ボタン）だけ
  - `prepare_site.py` は、頁ごとの判断（どの頁のどの段落か）を attr_list の class にして `_site_src/` の写しに付けるところまでを受け持つ（`bundle-item` `bundle-support` `manual-item` など）
  - `build.py` は、`_site_src/` の Markdown を HTML にし、class と木の形を見て旧版の HTML の構造に組み替える。出力のファイル名は旧版と同じ（`descript_ghost.html` など）。頁の種類は 3 つ（上の「作り」）。対応のベースウェアはアイコン画像（`image/icon_m.png` `icon_s.png` `icon_c.png` `icon_n.png`）で出す。ベースウェアを足すときは `build.py` の `BASEWARE` と画像を足す
  - 記述例とファイル構成の木の色付けは、`site_ext/ukadoc_site/lexers.py` の Pygments レキサー（`sakurascript`・`ss`、`filetree`）。`pyproject.toml` の `pygments.lexers` で登録している。さくらスクリプトの誤りは、ビルドの警告に出る（ビルドは止めない）。色は `oldstyle/static/oldstyle.css`
  - 見た目は `oldstyle/static/` の旧版の CSS（`base.css` `list.css` `spec.css`。`list.css` `spec.css` は旧版のまま。`base.css` は、枠の頁の iframe をやめたとき、上の帯・左メニューの CSS（旧 `iframes.css`）を取り込んで直した）と、新しい原稿のための補い `oldstyle.css`。旧版のままの CSS は、旧版の見た目を変えるとき以外は直さず、足りない分は `oldstyle.css` に書く
  - 翻訳ボタンは `oldstyle/static/translate.js`。置き場所は 2 通り（先頭のコメントにも書いてある）: 仕様書側（`float`）は右上に固定、枠の頁（`inline`）は上の帯の検索欄の右横。見た目は `oldstyle.css` の `.ukadoc-translate`、枠の頁のボタンの寸法は `base.css`。ブラウザ組み込みの Translator API（Chrome 138 以降のデスクトップ版など）で、本文を日本語から英語・中国語（繁体 `zh-Hant`・簡体 `zh`）へ機械翻訳する。API が無いブラウザではボタンを出さない。左メニューは同じ文書にあるので、本文と一緒に訳される
    - 訳すのは日本語を含む文だけ（`code` `pre` `kbd` と `translate="no"` の中は訳さない）。文はブロック（`p` `li` `td` など）の中の連なりを単位にまとめて訳し、リンク・太字・コードスパンは印（`<x1/>` `<a2>…</a2>`）に置き換えて訳してから元の要素へ戻す（印が崩れた文は断片ごとの訳に切り替える）。画面に近づいた所から順に訳す。選んだ言語は localStorage に覚え、モデルが取得済みなら次の頁でも自動で訳す
    - 読める程度の品質でよいとしている。原稿のほうで、訳したくない語を `<span translate="no">…</span>` で囲むこともできる
    - 言語を足すときは `translate.js` の `LANGS` に足す
    - 動作の確認は、Translator API のあるブラウザで `python -m http.server -d _site_old` の頁を開いて行う（Node では API が無いので、偽の `Translator` で試す）
  - サイト内検索（`search.html`）は、ビルド時に `build.py` が作る `search-index.js`（項目・節ごと）を、`search.js` が空白区切りの語の AND で部分一致検索する。旧版の Google の site 検索の代わり
    - 入力欄は、打ち込みが止まってから 250ms 後に検索し、ドロップダウン（上位 8 件と「すべての結果を見る」）を出す。↑↓で選び、Enter で開く（選んでいなければ `search.html?q=` へ）。Esc で閉じる。`search-index.js`（約 1.5MB）は、最初に打ち込んだときに読み込む
    - 枠の頁（上の帯に `form.internal-search` のある頁）は、上の帯の入力欄に打ち込む。ドロップダウンは入力欄（`.search-field`）の下に出す。仕様書側（`descript_*` `list_*` `spec_*`）は、右上（翻訳ボタンの左横）に固定の入力欄を `search.js` が置く
- `manual/` `dev/` `memo/` と、ディレクトリを持たない `spec/*.md` は、1 ファイル 1 ページのまま
- 章立て（左メニュー `oldstyle/templates/sidemenu.html`、上の帯 `navigation.html`、頁の上の目次の表 `menu-header.html`）は、旧版の HTML の写しを直接書く。ページを足したときは、これらに足す
- `llms.txt`（AI エージェント向けの探し方の案内。`INDEX.md` と各ディレクトリの入口だけを書く）はサイトのルートに置かれる。ページごとの一覧は載せないので、ページを足しても直さなくてよい。ディレクトリを足したときは「構成」に 1 行足す
- オフライン用のアーカイブ `ukadoc-spec-offline.zip` を、`oldstyle/build.py` が出力（`_site_old/`）のルートに作る（`build_offline_zip()`）。サイト一式（HTML・CSS・JS・画像・`llms.txt`・生の Markdown 原稿）を、`ukadoc-spec/` の下にまとめたもの。zip 自身は含めない。`INDEX.md` の冒頭から、`llms.txt` の案内の上でリンクしている（`llms.txt` と同じく絶対 URL）
- 生の Markdown 原稿（`README.md` と `CLAUDE.md` 以外の `.md`）は、リポジトリと同じパスでサイトにも置かれる。`scripts/prepare_site.py` が `_raw/` に写し、`oldstyle/build.py` が出力（`_site_old/`）に重ねる。`llms.txt` や `INDEX.md` の相対リンクは、このおかげでサイト上でも辿れる

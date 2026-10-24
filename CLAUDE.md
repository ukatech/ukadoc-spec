このリポジトリは伺か関連の仕様書「UKADOC」（SSP 公式仕様書）の Markdown 版です。1 項目 1 ファイルで書いてあり、人間にも AI Agent にも読み書きしやすい形にしてあります。

旧 HTML 版は `ukatech/ukadoc` の `manual/*.html` です（このリポジトリは、そのコミット 9eb14c5 時点を変換したもの）。旧 HTML の URL・id から現在のパスを引く表は `migration/id-map.json` です。

## 構成

| ディレクトリ | 内容 |
|---|---|
| `INDEX.md` | 全体の目次（サイトのトップページになる） |
| `manual/` | ファイル構成の解説（1 ページ 1 ファイル） |
| `descript/<種別>/` | 設定ファイルの各項目（`ghost` `shell` `shell-surfaces` `shell-surfacetable` `balloon` `plugin` `headline` `install`） |
| `list/<名前>/` | さくらスクリプト（`sakura-script`）、プロパティシステム（`propertysystem`）、`shiori-event` `shiori-event-ex` `shiori-resource` `plugin-event` |
| `spec/` | 規格（`shiori3` `sstp` `saori-ex` `plugin` `headline` `dll` `fmo-mutex` `update-file` `web`） |
| `dev/` | HowTo |
| `memo/` | 補足とメモ |
| `assets/image/` | 本文で使う画像 |
| `migration/id-map.json` | 旧 HTML の `ページ名#id` → 現在のパス・見出しの対応 |

`descript/` `list/` `spec/` の各ページはディレクトリで、その下にカテゴリのディレクトリ、さらにその下に項目の `.md` が並ぶ。どのディレクトリにも `index.md` があり、`## 一覧` に中身を元の仕様書の順に並べている。

項目の `.md` のファイル名は機械的に作ってある。イベント名・設定のキーは名前そのまま（`OnBoot.md`、`name.md`）、さくらスクリプトは記号を英字にした ASCII のスラッグ（`\![execute,filewatch,...]` → `bang-execute-filewatch.md`）で、同名になる場合は `-2` `-3` を付ける。カテゴリのディレクトリ名も ASCII（`scope` `boot-close-change` `app-kinoko` など）で、日本語のカテゴリ名は各 `index.md` の H1 にある。ファイル・ディレクトリ名に日本語は使わない。項目名の正本は各ファイルの H1 であり、ファイル名ではない。

## 書式

- UTF-8、LF。文体は「だ/である調」（～する。～である。）で統一する
- 項目のページは次の順に書く。無い部分は省く
  1. H1（項目名。さくらスクリプトのタグは `` `\![...]` `` のようにコードスパンで囲む）
  2. `**カテゴリ:** カテゴリ名`（入れ子のカテゴリは ` > ` でつなぐ）
  3. 説明。`<br />` で改行する
  4. パラメータの説明（`- **名前**: 説明` の箇条書き）
  5. `**既定値:** ...`
  6. `**対応:** SSP 2.7.23 / Ninix`（対応ベースウェアを ` / ` でつなぎ、版があれば名前の後ろに書く。ベースウェア名は `Materia` `SSP` `CROW` `Ninix`）
  7. `## 記述例`（さくらスクリプトは ```` ```sakurascript ```` のコードブロック）
- 非推奨の項目は、H1 の直後に `!!! warning "非推奨"`（本文は 4 スペース字下げ）を置く
- 注意書き・ヒントは `!!! note "注"` / `!!! tip "ヒント"`（admonition）で書く
- 本文中のさくらスクリプトのタグは `` `\n` `` のようにコードスパンで囲む。コードスパンの外では、バックスラッシュ `\` は `\\`、`*` `[` `]` `<` なども `\*` `\[` `\]` `&lt;` と書かないと表示が崩れる
- リストは `- ` で書き、入れ子は 2 スペース（番号付きは 3 スペース）で字下げする（`mdx_truly_sane_lists` による）
- 表の中のコードスパンの `|` は `\|` と書く
- 画像は `../../assets/image/ファイル名` のように、ページからの相対パスで参照する

### 頻出パターン

- 非同期処理: 成功は `OnXxxComplete`、失敗は `OnXxxFailure`（識別子に `Failure` を付ける）。`--event` オプションは次の文面にそろえる
  - `--event=イベントまたは識別子……Onではじまる文字列を指定すると、Sakura Scriptの続きを実行しながら処理を続け、終わり次第指定したイベントが起きる。省略時は処理が完了するまでスクリプトの実行は停止する。`
  - Reference0 は `Sakura Scriptの--eventオプションで指定されたイベント識別子。`
- フルパス指定: 「指定はフルパスで行うこと(相対パス指定不可)」
- セキュリティ上の制限: 「セキュリティ上の観点から、[操作先]は、SSP管理下のフォルダ(ghostフォルダ、balloonフォルダなど「フォルダ」設定で指定した場所)以下への展開に制限される。また、この制限は適宜強化される可能性があるため、ゴースト自身のデータが置かれているフォルダ以下に限定するのが無難。」

## リンク

- 別のページへは相対パスで `.md` まで書く（例: `[OnBoot](../boot-close-change/OnBoot.md)`）。見出しへのリンクは `file.md#見出し`（GitHub と同じく日本語の見出しをそのまま使う）
- 外部サイトへは URL をそのまま書く

## 項目を追加・改名したとき

1. 該当カテゴリのディレクトリに項目の `.md` を作る（既存の項目をひな形にする）
2. そのディレクトリの `index.md` の `## 一覧` に、元の仕様書の並びに合う位置でリンクを加える（`[名前](ファイル.md)`）。ページの順序は `## 一覧` と `.nav.yml` が決める
3. 新しいページ・カテゴリのディレクトリを作ったら、`index.md` と `.nav.yml`（`title:` と `nav:`）を置き、親の `index.md` の `## 一覧` と、`list/` 以外ならルートの `.nav.yml` にも加える
4. `INDEX.md` の「目次」にページを加える（ページを新設したときだけ）
5. 確認する（下記）

## 確認

`_site_src/` と `_site/` は `.gitignore` 済み。

```sh
pip install -r requirements.txt
python scripts/prepare_site.py   # 各 index.md の「## 一覧」と中身の食い違いを検査し、_site_src/ に写す
zensical build --strict          # リンク切れ・アンカー切れがあると失敗する
zensical serve                   # http://127.0.0.1:8000/ukadoc-spec/ でプレビュー
```

## GitHub Pages

`main` に push すると GitHub Actions（`.github/workflows/pages.yml`）が Zensical でビルドし、https://ukatech.github.io/ukadoc-spec/ に公開する。

- 原稿はリポジトリ直下にあるため、`scripts/prepare_site.py` が `_site_src/` に写してからビルドする（`INDEX.md` は `index.md`（トップページ）になる）
- 設定は `mkdocs.yml`。左メニューの章立ては `.nav.yml`（mkdocs-awesome-nav）で、項目（エントリ）はメニューに出さず、各 `index.md` の「## 一覧」から辿る。ページが多いため `navigation.prune` を有効にしている（外すとサイトが数百 MB になる）
- `llms.txt` はサイトのルートにも置かれる

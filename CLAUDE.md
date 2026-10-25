このリポジトリは伺か関連の仕様書「UKADOC」（SSP 公式仕様書）の Markdown 版です。1 項目 1 ファイルで書いてあり、人間にも AI Agent にも読み書きしやすい形にしてあります。

**このリポジトリが UKADOC の正本です。** 旧 HTML 版は `ukatech/ukadoc` の `manual/*.html` で、このリポジトリはそのコミット 9eb14c5 時点を変換したものです。しばらくは並存しますが、仕様の追加・修正はこのリポジトリに書きます。並存期間中に旧 HTML 側へ入った変更は、手で Markdown に写してください（`migration/tools/` で再生成すると、このリポジトリでの修正が上書きされるので、使わないこと）。旧 HTML の URL・id から現在のパスを引く表は `migration/id-map.json` です。

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

`descript/` `list/` `spec/` の各ページはディレクトリで、その下にカテゴリのディレクトリ、さらにその下に項目の `.md` が並ぶ。どのディレクトリにも `index.md` があり、`## 一覧` に中身を元の仕様書の順に並べている（この順がサイトの並びにもなる）。

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
  7. `## 記述例`（さくらスクリプトは ```` ```sakurascript ```` のコードブロック。省略形の ```` ```ss ```` も同じ言語として使える）
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
- `--event=` と `--async=` は、名前の違いが動作の違いを表すので、片方に揃えない。新しい項目は、同じ系統のコマンドの名前に合わせる
  - `--event=`: 1 つのオプションで同期と非同期の両方を扱う。付けると非同期で、省略すると処理が完了するまで止まる（上の文面）
  - `--async=`: 非同期で動かすことを明示する。http/rss/ical/websocket の系統では、止めて待つ `--sync=` と対になる（`list/sakura-script/misc/notes_executehttp.md`）。SAORI の内蔵モジュール（`internal_*`）では、付けると非同期になる（`spec/saori-ex/async.md`）
  - `\![execute,dumpsurface]` と `\![execute,dumpballoon]` は、`--event=` と `--async=` のどちらでも同じ意味になる
- フルパス指定: 「指定はフルパスで行うこと(相対パス指定不可)」
- セキュリティ上の制限: 「セキュリティ上の観点から、[操作先]は、SSP管理下のフォルダ(ghostフォルダ、balloonフォルダなど「フォルダ」設定で指定した場所)以下への展開に制限される。また、この制限は適宜強化される可能性があるため、ゴースト自身のデータが置かれているフォルダ以下に限定するのが無難。」

## リンク

- 別のページへは相対パスで `.md` まで書く（例: `[OnBoot](../boot-close-change/OnBoot.md)`）。見出しへのリンクは `file.md#見出し`（GitHub と同じく日本語の見出しをそのまま使う）
- 外部サイトへは URL をそのまま書く

## 項目を追加・改名したとき

1. 該当カテゴリのディレクトリに項目の `.md` を作る（既存の項目をひな形にする）
2. そのディレクトリの `index.md` の `## 一覧` に、元の仕様書の並びに合う位置でリンクを加える（`[名前](ファイル.md)`）。項目の順序は `## 一覧` が決める（サイトでもこの順に並ぶ）。`index.md` の `## 一覧` に無い `.md` やディレクトリがあると、`prepare_site.py` が止まる
3. 新しいカテゴリのディレクトリを作ったら、`index.md`（H1 とカテゴリの説明、`## 一覧`）を置き、親の `index.md` の `## 一覧` にも加える。新しいページ（`descript/` `list/` `spec/` の直下のディレクトリ）を作ったときは、ルートの `.nav.yml` にも加える
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

`zensical build --strict` が見るのはサイトの中のリンクだけ。外部リンクは、ときどき `python scripts/check_links.py` で、エラーになるものと別の URL へ転送されるものを洗い出す（`--titles` で、転送されずに 200 を返すものもタイトル付きで並ぶ）。切れているかどうかはスクリプトでは判断しないので、開いて確かめる。切れていたら、元のリンクの後ろに Internet Archive の保存版を「（[アーカイブ](https://web.archive.org/web/時刻/元のURL)）」と添える（添えたリンクは以後の検査から外れる）。

## GitHub Pages

`main` に push すると GitHub Actions（`.github/workflows/pages.yml`）が Zensical でビルドし、https://ukatech.shillest.net/ukadoc-spec/ に公開する。

- 原稿はリポジトリ直下にあるため、`scripts/prepare_site.py` が `_site_src/` に写してからビルドする（`INDEX.md` は `index.md`（トップページ）になる）
- 旧 HTML 版で 1 ページだったもの（`descript/<名前>/`、`list/<名前>/`、`spec/<名前>/` の各ディレクトリ）は、サイトでは 1 ページ（`<ディレクトリ>/index.html`）にまとめて出す。原稿は 1 項目 1 ファイルのまま書き、リンクも `../scope/s-ID.md` や `file.md#見出し` と従来どおり書く。`prepare_site.py` が次のことをする
  - 「## 一覧」の順に、ディレクトリ内の全 `.md` をつなぐ。見出しは入れ子の深さの分だけずらし（ページ H1 → カテゴリ H2 → 項目 H3 → 項目内の節 H4。H6 を超えるとエラー）、`{#id}` で一意な id を振る。項目の id は、ファイル名（重なるときはディレクトリからのパス）で、項目内の節は `項目の id-元の見出しの id` になる（例: `#OnBoot`、`#bang-lock-repaint-記述例`）
  - まとめた項目へのリンクを、まとめたページの見出しへのリンクに書き換える（飛び先の見出しが無いとエラー）
  - `**カテゴリ:**` の行は、親の見出しが示すのでサイトでは省く
- `manual/` `dev/` `memo/` と、ディレクトリを持たない `spec/*.md` は、1 ファイル 1 ページのまま
- 設定は `mkdocs.yml`。左メニューの章立ては、ルートの `.nav.yml`（mkdocs-awesome-nav）だけで決める（ディレクトリごとの `.nav.yml` は置かない）
- `llms.txt`（AI エージェント向けの探し方の案内。`INDEX.md` と各ディレクトリの入口だけを書く）はサイトのルートに置かれる。ページごとの一覧は載せないので、ページを足しても直さなくてよい。ディレクトリを足したときは「構成」に 1 行足す
- 生の Markdown 原稿（`README.md` と `CLAUDE.md` 以外の `.md`）は、リポジトリと同じパスでサイトにも置かれる。`scripts/prepare_site.py` が `_raw/` に写し、workflow がビルド後に `_site` へ重ねる（zensical は `.md` をページにしてしまうので、`_site_src/` には置けない）。`llms.txt` や `INDEX.md` の相対リンクは、このおかげでサイト上でも辿れる

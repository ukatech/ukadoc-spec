# CompressArchive

**カテゴリ:** internal_file

フォルダをZIPファイルに圧縮する。[SSTPのEXECUTE](../../sstp/method_execute.md)の`CompressArchive`と同じ処理を、SAORI over DirectSSTPから呼べるようにしたもの。<br />
書庫の処理は数秒かかることがあるので、[`--async`](../async.md)を強く推奨する。同期で呼ぶと、処理の間ゴーストが止まる。

- **Argument1**: 圧縮先のZIPファイルのパス。相対パスはゴーストのフォルダ（ghost/master）が基準。区切りは`/`も`\`も書ける。ゴーストなしの呼び出しで相対パスを渡すと400（`ghost required`）。
- **Argument2**: 圧縮するフォルダ（中のファイルを再帰的に含める）のパス。書き方はArgument1と同じ。無ければ400（`file not found`）。ファイルのパスを渡すことは想定しておらず、渡すと500（`file not found`）で失敗する。

オプションは次のとおり（同じ名前を2回書くと後のものが有効）。

- --password=パスワード……指定したパスワードでAES暗号化ZIPにする。
- --option=オプション……次の値をカンマ区切りで**1つにまとめて**指定する（`--option=overwrite,lzma`のように。`--option=`を2つに分けて書くと後のものだけが有効になる）。<br />
  overwrite……圧縮先のZIPファイルが既にあれば置き換える。<br />
  append……圧縮先のZIPファイルが既にあれば追加する。<br />
  lzma……LZMAで圧縮する。<br />
  headerencrypt……ヘッダも暗号化する（`--password=`が必要）。<br />
  圧縮先のZIPファイルが既にあって、`overwrite`も`append`も指定していないときは400（`file exists`）。

成功すると200で、`Result`に圧縮したファイル数、`Value0`に圧縮後のバイト数、`Value1`に圧縮前（展開後）のバイト数が入る（10進の整数）。SSTPのEXECUTEの[OnCompressArchiveComplete](../../../list/shiori-event/other/OnCompressArchiveComplete.md)の`Reference1`～`Reference3`と同じ値で、[`--async`](../async.md)では`Reference1`（`Result`）と`Reference4`・`Reference5`（`Value0`・`Value1`）に入る。<br />
ZIPの`Value0`は書庫に増えたバイト数（ヘッダと中央ディレクトリを含む。`append`のときは追加分だけ）で、圧縮したデータだけのサイズより少し大きい。<br />
\[SSP 2.9.26\] ZIPでも、ファイル数とバイト数が正しく入る（\[SSP 2.9.25\]では、ZIPへの圧縮では0になる）。

失敗は次のとおり。400は`file not found`（圧縮元が無い）/ `invalid parameter`（引数が足りない、パスが空、オプションが不正）/ `ghost required` / `file exists` / `path not allowed`（圧縮先がSSP管理下のフォルダの外）。500は`open failed`など、圧縮に失敗した理由。

セキュリティ上の観点から、圧縮先は、SSP管理下のフォルダ（ghostフォルダ、balloonフォルダなど「フォルダ」設定で指定した場所）以下に制限される。パスは`..`などを解決した結果で調べる。また、この制限は適宜強化される可能性があるため、ゴースト自身のデータが置かれているフォルダ以下に限定するのが無難。

## 記述例

```
Argument0: CompressArchive
Argument1: save/backup.zip
Argument2: save/data
Argument3: --option=overwrite
Argument4: --async=OnBackupDone

→ 204（結果はOnBackupDoneイベントで届く）
```

**対応:** SSP 2.9.25

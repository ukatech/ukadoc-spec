# ExtractArchive

**カテゴリ:** internal_file

書庫（ZIPのほか、7zやtarなども。下の「対応する形式」を参照）を展開する。[SSTPのEXECUTE](../../sstp/method_execute.md)の`ExtractArchive`と同じ処理を、SAORI over DirectSSTPから呼べるようにしたもの。<br />
書庫の処理は数秒かかることがあるので、[`--async`](../async.md)を強く推奨する。同期で呼ぶと、処理の間ゴーストが止まる。

- **Argument1**: 展開する書庫のパス。相対パスはゴーストのフォルダ（ghost/master）が基準。区切りは`/`も`\`も書ける。ゴーストなしの呼び出しで相対パスを渡すと400（`ghost required`）。ファイルが無い（フォルダを含む）ときは400（`file not found`）。
- **Argument2**: 展開先のフォルダのパス。書き方はArgument1と同じ。フォルダが無ければ作る（作れなければ500 `create directory failed`）。

オプションは次のとおり。

- --password=パスワード \[SSP 2.9.26\]……指定したパスワードでパスワード付きのZIPを展開する。パスワードが要るのに指定が無い、または違うときは、パスワードの入力ダイアログは出さず、500（`password mismatch`）で失敗する（\[SSP 2.9.25\]では、指定できず、パスワードの入力ダイアログが出てゴーストが止まる）。
- [`--async`](../async.md)

成功すると200で、`Result`に展開したファイル数、`Value0`に圧縮後のバイト数、`Value1`に展開後のバイト数が入る（10進の整数）。SSTPのEXECUTEの[OnExtractArchiveComplete](../../../list/shiori-event/other/OnExtractArchiveComplete.md)の`Reference1`～`Reference3`と同じ値で、[`--async`](../async.md)では`Reference1`（`Result`）と`Reference4`・`Reference5`（`Value0`・`Value1`）に入る。<br />
7zなど、エントリごとの圧縮後のサイズを持たない書庫では、`Value0`が0になることがある。<br />
\[SSP 2.9.26\] ZIPでも、複数のファイルを含む書庫の合計が正しく入る（\[SSP 2.9.25\]では、バイト数が最後の1ファイル分になる）。

失敗は次のとおり。400は`file not found`（展開する書庫が無い）/ `invalid parameter`（引数が足りない、パスが空）/ `ghost required` / `path not allowed`（展開先がSSP管理下のフォルダの外）。500は`create directory failed`か、展開に失敗した理由（`open failed`、`crc`、`password mismatch`など）。

セキュリティ上の観点から、展開先は、SSP管理下のフォルダ（ghostフォルダ、balloonフォルダなど「フォルダ」設定で指定した場所）以下に制限される。パスは`..`などを解決した結果で調べる。また、この制限は適宜強化される可能性があるため、ゴースト自身のデータが置かれているフォルダ以下に限定するのが無難。

## 対応する形式

書庫の形式は、ファイル名の拡張子で判別する（自己解凍の`exe`は、中身を調べて中のZIPや7zを展開する）。判別できない形式は、500で失敗する。

- **ZIP**: `.zip` `.zipx` `.nar`
- **LZH**: `.lzh` `.lha`
- **CAB**: `.cab`
- **7z**: `.7z`
- **tar系**: `.tar` `.tar.gz`（`.tgz`） `.tar.xz`（`.txz`） `.tar.bz2`（`.tbz2` `.tbz`） `.tar.lzma`（`.tlz`） `.tar.zst`（`.tzst`） `.tar.br`（`.tbr`） `.tar.Z`（`.taz`） `.cpio` `.deb` `.udeb` `.rpm`
- **単体圧縮**: `.gz` `.bz2` `.xz` `.lzma` `.zst` `.zstd` `.br` `.Z`（1つのファイルを含む書庫として展開する）
- **ディスクイメージ**: `.iso` `.img`
- **メール**: `.eml`
- **自己解凍**: `.exe`

`--password=`が意味を持つのはZIPと7zだけで、ほかの形式では無視される。

## 記述例

```
Argument0: ExtractArchive
Argument1: save/backup.zip
Argument2: save/restore
Argument3: --async=OnRestoreDone

→ 204（結果はOnRestoreDoneイベントで届く）
　Reference0: OnRestoreDone
　Reference1: 12（展開したファイル数）
　Reference2: internal_file
　Reference3: ExtractArchive
　Reference4: 圧縮後のバイト数
　Reference5: 展開後のバイト数
```

**対応:** SSP 2.9.25

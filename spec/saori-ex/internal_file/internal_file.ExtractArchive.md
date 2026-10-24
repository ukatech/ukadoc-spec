# ExtractArchive

**カテゴリ:** internal_file

ZIPファイルを展開する。[SSTPのEXECUTE](../../sstp/method_execute.md)の`ExtractArchive`と同じ処理を、SAORI over DirectSSTPから呼べるようにしたもの。<br />
書庫の処理は数秒かかることがあるので、[`--async`](../async.md)を強く推奨する。同期で呼ぶと、処理の間ゴーストが止まる。

- **Argument1**: 展開するZIPファイルのパス。相対パスはゴーストのフォルダ（ghost/master）が基準。区切りは`/`も`\`も書ける。ゴーストなしの呼び出しで相対パスを渡すと400（`ghost required`）。ファイルが無い（フォルダを含む）ときは400（`file not found`）。
- **Argument2**: 展開先のフォルダのパス。書き方はArgument1と同じ。フォルダが無ければ作る（作れなければ500 `create directory failed`）。

オプションは[`--async`](../async.md)だけ。パスワードを指定するオプションは無い（パスワード付きのZIPは展開できないことがある）。

成功すると200で、`Result`に展開したファイル数、`Value0`に圧縮後のバイト数、`Value1`に展開後のバイト数が入る（10進の整数）。SSTPのEXECUTEの[OnExtractArchiveComplete](../../../list/shiori-event/other/OnExtractArchiveComplete.md)の`Reference1`～`Reference3`と同じ値で、[`--async`](../async.md)では`Reference1`（`Result`）と`Reference4`・`Reference5`（`Value0`・`Value1`）に入る。<br />
\[SSP 2.9.25\] ZIPでは、このファイル数とバイト数が正しい値にならないことがある（複数のファイルを含むZIPでは、バイト数が最後の1ファイル分になる）。展開そのものの成否には影響しない。

失敗は次のとおり。400は`file not found`（展開するZIPファイルが無い）/ `invalid parameter`（引数が足りない、パスが空）/ `ghost required` / `path not allowed`（展開先がSSP管理下のフォルダの外）。500は`create directory failed`か、展開に失敗した理由（`open failed`、`crc`、`password required`など）。

セキュリティ上の観点から、展開先は、SSP管理下のフォルダ（ghostフォルダ、balloonフォルダなど「フォルダ」設定で指定した場所）以下に制限される。パスは`..`などを解決した結果で調べる。また、この制限は適宜強化される可能性があるため、ゴースト自身のデータが置かれているフォルダ以下に限定するのが無難。

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

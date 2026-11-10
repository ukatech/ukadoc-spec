# ExtractArchive

**カテゴリ:** internal_file

解壓縮封存檔（除了 ZIP，也包括 7z、tar 等。請參閱下方的「支援的格式」）。此功能可透過 SAORI over DirectSSTP 呼叫，執行與[SSTP 的 EXECUTE](../../sstp/method_execute.md)之`ExtractArchive`相同的處理。<br />
處理封存檔可能需要數秒，因此強烈建議使用[`--async`](../async.md)。同步呼叫時，ghost 會在處理期間停止。

- **Argument1**: 要解壓縮的封存檔路徑。相對路徑以 ghost 資料夾（ghost/master）為基準。分隔符號可使用`/`或`\`。沒有 ghost 卻傳入相對路徑時，會回傳 400（`ghost required`）。檔案不存在時（包括資料夾），會回傳 400（`file not found`）。
- **Argument2**: 解壓縮目的地資料夾的路徑。寫法與 Argument1 相同。資料夾不存在時會建立（若無法建立則回傳 500 `create directory failed`）。

選項如下。

- --password=密碼 \[SSP 2.9.26\]……使用指定的密碼解壓縮受密碼保護的 ZIP。若需要密碼卻未指定，或指定的密碼錯誤，會在不顯示密碼輸入對話方塊的情況下，以 500（`password mismatch`）結束。（\[SSP 2.9.25\]無法指定密碼，會顯示密碼輸入對話方塊並使 ghost 停止。）
- [`--async`](../async.md)

成功時會回傳 200，`Result`會包含解壓縮的檔案數，`Value0`會包含壓縮後的位元組數，`Value1`會包含解壓縮後的位元組數（十進位整數）。這些值與 SSTP 的 EXECUTE 中[OnExtractArchiveComplete](../../../list/shiori-event/other/OnExtractArchiveComplete.md)的`Reference1`～`Reference3`相同；使用[`--async`](../async.md)時，則會分別放入`Reference1`（`Result`）以及`Reference4`、`Reference5`（`Value0`、`Value1`）。<br />
對於 7z 等不包含各個項目壓縮後大小資訊的封存檔，`Value0`可能會是 0。<br />
\[SSP 2.9.26\] 即使是 ZIP，也會正確填入包含多個檔案之封存檔的總大小（\[SSP 2.9.25\]的位元組數會是最後一個檔案的大小）。

失敗時的回傳如下。400 表示`file not found`（要解壓縮的封存檔不存在）／`invalid parameter`（引數不足、路徑為空）／`ghost required`／`path not allowed`（解壓縮目的地位於 SSP 管理資料夾之外）。500 表示`create directory failed`，或解壓縮失敗的原因（例如`open failed`、`crc`、`password mismatch`）。

基於安全考量，解壓縮目的地僅限於 SSP 管理的資料夾（例如 ghost 資料夾、balloon 資料夾等「資料夾」設定指定的位置）之下。檢查路徑時，會先解析`..`等項目。由於此限制可能會適時加嚴，最好將目的地限制在存放 ghost 自身資料的資料夾之下。

## 支援的格式

書庫格式是根據檔名的副檔名判別（自我解壓縮的`exe`會檢查其內容，並解壓縮其中的 ZIP 或 7z）。無法判別格式時，會以 500 失敗。

- **ZIP**: `.zip` `.zipx` `.nar`
- **LZH**: `.lzh` `.lha`
- **CAB**: `.cab`
- **7z**: `.7z`
- **tar 系列**: `.tar` `.tar.gz`（`.tgz`） `.tar.xz`（`.txz`） `.tar.bz2`（`.tbz2` `.tbz`） `.tar.lzma`（`.tlz`） `.tar.zst`（`.tzst`） `.tar.br`（`.tbr`） `.tar.Z`（`.taz`） `.cpio` `.deb` `.udeb` `.rpm`
- **單一檔案壓縮格式**: `.gz` `.bz2` `.xz` `.lzma` `.zst` `.zstd` `.br` `.Z`（會以包含一個檔案的書庫形式解壓縮）
- **磁碟映像**: `.iso` `.img`
- **電子郵件**: `.eml`
- **自我解壓縮**: `.exe`

`--password=`僅適用於 ZIP 和 7z，在其他格式中會被忽略。

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

# CompressArchive

**カテゴリ:** internal_file

將資料夾壓縮成 ZIP 檔案（或 7z 檔案）。此功能可透過 SAORI over DirectSSTP 呼叫，執行與[SSTP 的 EXECUTE](../../sstp/method_execute.md)中的`CompressArchive`相同的處理。<br />
壓縮檔格式由目的地副檔名決定。`.7z`會使用 7z（以 LZMA 壓縮），其他副檔名一律使用 ZIP（即使指定`.lzh`或`.cab`，內容仍會是 ZIP）。<br />
壓縮檔處理可能需要數秒，因此強烈建議使用[`--async`](../async.md)。若以同步方式呼叫，ghost 會在處理期間停止。

- **Argument1**: 壓縮檔的目的地路徑。相對路徑以 ghost 資料夾（ghost/master）為基準。分隔符可使用`/`或`\`。在沒有 ghost 的情況下呼叫並傳入相對路徑時，會回傳 400（`ghost required`）。
- **Argument2**: 要壓縮的資料夾路徑（會遞迴包含其中的檔案，但不包含隱藏檔案與隱藏資料夾〔包括其中的內容〕）。寫法與 Argument1 相同。路徑不存在時會回傳 400（`file not found`）。此路徑不限於 SSP 管理的資料夾，也可壓縮管理範圍以外的資料夾（只有壓縮目的地受限）。\[SSP 2.9.33\] 若傳入的不是資料夾（例如檔案路徑），會回傳 400（`invalid parameter`）。在此版本之前，傳入檔案路徑會因 500（`file not found`）而失敗。

選項如下（同名選項寫入兩次時，以後者為準）。

- --password=密碼……使用指定的密碼加密（若為 ZIP，則使用 AES 加密 ZIP）。
- --option=選項……以逗號分隔並**合併為一個值**指定下列選項（例如`--option=overwrite,lzma`。若將`--option=`分開寫成兩項，只有後者有效）。<br />
  overwrite……若目的地壓縮檔已存在，則予以取代。<br />
  append……若目的地壓縮檔已存在，則將內容附加至其中。<br />
  lzma……使用 LZMA 壓縮（適用於 ZIP。7z 一律使用 LZMA，因此指定此選項也不會改變結果）。<br />
  headerencrypt……也加密標頭（檔名清單）（需要`--password=`）。**僅適用於 7z，對 ZIP 不會產生作用**（ZIP 的檔名仍會以未加密的狀態保留）。<br />
  若目的地壓縮檔已存在，且未指定`overwrite`或`append`，則會回傳 400（`file exists`）。

成功時會回傳 200，並在`Result`中放入壓縮的檔案數量，在`Value0`中放入壓縮後的位元組數，在`Value1`中放入壓縮前（解壓後）的位元組數（十進位整數）。這些值與 SSTP 的 EXECUTE 中[OnCompressArchiveComplete](../../../list/shiori-event/other/OnCompressArchiveComplete.md)的`Reference1`～`Reference3`相同；使用[`--async`](../async.md)時，會放入`Reference1`（`Result`）以及`Reference4`、`Reference5`（`Value0`、`Value1`）。<br />
ZIP 的`Value0`是壓縮檔增加的位元組數（包含標頭與中央目錄；使用`append`時僅計算新增部分），會比壓縮資料本身的大小稍大。<br />
\[SSP 2.9.26\] ZIP 也會正確填入檔案數量與位元組數（\[SSP 2.9.25\]中，壓縮成 ZIP 時數值會是 0）。

失敗情況如下。400 代表`file not found`（壓縮來源不存在）/ `invalid parameter`（引數不足、路徑為空、選項無效、\[SSP 2.9.33\] 壓縮來源不是資料夾）/ `ghost required` / `file exists` / `path not allowed`（壓縮目的地位於 SSP 管理資料夾之外）。500 則表示`open failed`等壓縮失敗原因。

基於安全考量，壓縮目的地限制在 SSP 管理的資料夾（例如 ghost 資料夾、balloon 資料夾等「資料夾」設定指定的位置）之下。檢查時會先解析`..`等路徑。由於此限制可能視需要加強，建議將目的地限於存放 ghost 本身資料的資料夾之下。

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

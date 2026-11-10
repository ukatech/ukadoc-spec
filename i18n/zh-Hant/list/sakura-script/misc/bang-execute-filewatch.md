# `\![execute,filewatch,パス,オプション...]`

**カテゴリ:** 未分類命令

開始監視指定的檔案或目錄，並在每次變更時透過 [OnExecuteFileWatchChange](../../shiori-event/other-communication/OnExecuteFileWatchChange.md) 通知。若無法開始監視，或監視期間監視目標目錄消失，則會透過 [OnExecuteFileWatchFailure](../../shiori-event/other-communication/OnExecuteFileWatchFailure.md) 通知，並結束該監視。無法在 SSTP 等外部傳入的腳本中執行。<br />
參數如下。

- パス……要監視的檔案或目錄。若指定相對路徑，則會解讀為相對於 ghost/master/ 的路徑。
- --async=事件または識別子……指定以 On 開頭的字串時，會觸發該事件（而非後述的事件）
- --debounce=毫秒……變更通知停止後，等待指定的時間；若期間沒有再次變更，就會發出通知。只要變更持續發生，就會持續等待，因此寫入期間連續發生的變更會合併為一次通知。但即使變更沒有停止，從首次變更起經過指定時間的 3 倍後也會發出通知。省略時為 500。指定 0 時會立即通知。

指定檔案時，會通知更新、建立及刪除。也可以指定尚不存在的檔案，該檔案建立時會收到通知。但存放該檔案的目錄必須存在。<br />
指定目錄時，只會通知該目錄下直接發生的檔案或目錄建立、刪除、重新命名及更新。不會通知變更的是哪個檔案，也不會通知子目錄內的變更。若要監視目錄，執行時該目錄必須存在（不存在的路徑會視為檔案進行監視）。<br />
再次指定相同路徑時，先前的指定會被取代。ghost 結束時，所有監視都會解除。

**対応:** SSP 2.8.91

## 記述例

```sakurascript
\![execute,filewatch,config.json,--async=OnConfigChanged]ghost/master/config.jsonが変化するたびに、OnConfigChangedイベントが起きる。
```

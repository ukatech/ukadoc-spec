# OnExecuteFileWatchChange

**カテゴリ:** 其他通信事件

監視対象となっている [`\![execute,filewatch]`](../../sakura-script/misc/bang-execute-filewatch.md) 檔案或目錄發生變化時觸發。

若透過 --async 指定以 On 開頭的 ID，該 ID 就會成為事件名稱。

由於檔案可能在短時間內多次寫入，因此變化停止後，會再等待 --debounce 指定的時間（省略時為 500 毫秒），然後合併成一次觸發。若寫入間隔比這段時間長，或變化持續不止，且從首次變化起已經過指定時間的 3 倍，則一次儲存可能觸發多次。

- **Reference0**: --async 指定的字串本身（若未指定則為空）
- **Reference1**: 指定路徑的字串本身
- **Reference2**: 變化類型<br />
  檔案：modified（更新）、created（建立）、deleted（刪除）<br />
  目錄：changed（直屬項目發生建立、刪除、重新命名或更新）、deleted（目錄本身已不存在）
- **Reference3**: 監視中的檔案或目錄完整路徑

**対応:** SSP 2.8.91

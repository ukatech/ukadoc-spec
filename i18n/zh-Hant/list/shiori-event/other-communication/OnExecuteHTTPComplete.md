# OnExecuteHTTPComplete

**カテゴリ:** 其他通信事件

execute-http 成功取得資料並完成時觸發。

- **Reference0**: post/get/head/put/delete 其中之一
- **Reference1**: --sync・--async 選項指定的字串。
- **Reference2**: 目標 URL。
- **Reference3**: 若有 --nofile 選項，則為取得資料的內容。但換行字元會替換成位元組值 1。<br />
  否則為取得檔案的完整路徑。
- **Reference4**: 取得結果代碼。例如 (timeout|fileio|200|204|403|404)。另請參閱[\[失敗原因\]](../network-update/caption_updateresultfailure.md)。
- **Reference5**: Cookie 字串。
- **Reference6**: 接收的所有回應標頭。以位元組值 1 作為換行分隔符號。 \[2.6.40\]

**対応:** SSP / Ninix

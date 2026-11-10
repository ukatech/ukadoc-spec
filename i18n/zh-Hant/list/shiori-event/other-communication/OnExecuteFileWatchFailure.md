# OnExecuteFileWatchFailure

**カテゴリ:** 其他通信事件

[`\![execute,filewatch]`](../../sakura-script/misc/bang-execute-filewatch.md)失敗時，或無法繼續監視時會發生此事件。此時會解除該監視。

使用--async指定以On開頭的ID時，事件名稱會在該ID後面加上Failure。

- **Reference0**: 使用--async指定的字串本身（若無則為空）
- **Reference1**: 指定路徑的字串本身
- **Reference2**: 失敗原因<br />
  notauthorized : 嘗試監視由SSTP等外部傳送的腳本<br />
  invalid : 未指定路徑<br />
  notfound : 監視目標目錄（若為檔案，則為存放該檔案的目錄）不存在、無法開始監視，或在監視期間消失<br />
  limit : SSP整體監視的目錄種類數超過上限（63）

**対応:** SSP 2.8.91

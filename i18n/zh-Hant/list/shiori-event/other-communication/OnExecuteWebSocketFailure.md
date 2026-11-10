# OnExecuteWebSocketFailure

**カテゴリ:** 其他通訊事件

初次連線時 HTTP 101 Upgrade 失敗，或連線期間發生錯誤中斷且自動重新連線嘗試 5 次後仍全部失敗時觸發。<br />
若以 --async 選項指定的 eventID 以 "On" 開頭，事件名稱會是 eventID+"Failure"。

- **Reference0**: Sakura Script 的 --async 選項所指定的事件識別碼。
- **Reference1**: 連線 URL。
- **Reference2**: 錯誤內容字串。初次連線失敗時為 SPHttp 的錯誤文字；自動重新連線全部失敗時則固定為 "reconnect failed"。

**対応:** SSP 2.8.05

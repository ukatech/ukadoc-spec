# OnExecuteWebSocketReceive

**カテゴリ:** 其他通訊事件

WebSocket 連線期間，每當從伺服器接收到資料框架時觸發。分段框架會自動重新組合後再觸發。Ping/Pong/Close 框架不會觸發。<br />
若以 --async 選項指定的 eventID 以 "On" 開頭，事件名稱會直接使用 eventID。

- **Reference0**: Sakura Script 的 --async 選項所指定的事件識別碼。
- **Reference1**: 連線 URL。
- **Reference2**: opcode 類型。"1"=文字框架（UTF-8）、"2"=二進位框架。
- **Reference3**: 接收資料。文字框架會直接使用 UTF-8 字串（換行字元會轉換為位元組值 1）；二進位框架則使用 Base64 編碼字串。

**対応:** SSP 2.8.05

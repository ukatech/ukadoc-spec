# OnExecuteWebSocketClose

**カテゴリ:** その他通信イベント

WebSocket接続が最終的に切断されたときに発生。自動再接続を試みた場合はその後に発火する。Failure時は発火しない。<br />
--asyncオプションで指定したeventIDが "On" で始まる場合はeventID+"Close" がイベント名となる。

- **Reference0**: Sakura Scriptの--asyncオプションで指定されたイベント識別子。
- **Reference1**: 接続URL。
- **Reference2**: 切断要因コード。"1000"=正常切断（サーバーまたは`\![close,websocket]`による）、"userbreak"=`\![cancel,websocket]`またはゴースト終了による強制中断。

**対応:** SSP 2.8.05

# OnExecuteWebSocketFailure

**カテゴリ:** その他通信イベント

初回接続でHTTP 101 Upgradeに失敗したとき、または接続中にエラー切断が発生し自動再接続を5回試みてもすべて失敗したときに発生。<br />
--asyncオプションで指定したeventIDが "On" で始まる場合はeventID+"Failure" がイベント名となる。

- **Reference0**: Sakura Scriptの--asyncオプションで指定されたイベント識別子。
- **Reference1**: 接続URL。
- **Reference2**: エラー内容文字列。初回接続失敗時はSPHttpのエラーテキスト、自動再接続全失敗時は"reconnect failed"（固定）。

**対応:** SSP 2.8.05

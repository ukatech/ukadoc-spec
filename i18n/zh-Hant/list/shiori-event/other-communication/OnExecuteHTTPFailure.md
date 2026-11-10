# OnExecuteHTTPFailure

**カテゴリ:** 其他通信事件

execute-http 取得失敗時觸發。Reference 與 Complete 相同。

\[2.8.90\] 若相同 URL 的取得作業已在進行中，之後送出的請求不會執行，並觸發此事件（Reference4=downloading）。在此之前，標籤會被直接忽略。

**対応:** SSP / Ninix

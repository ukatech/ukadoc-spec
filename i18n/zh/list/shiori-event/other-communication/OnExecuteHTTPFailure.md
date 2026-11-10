# OnExecuteHTTPFailure

**カテゴリ:** 其他通信事件

通过execute-http获取失败时触发。Reference与Complete相同。

\[2.8.90\] 如果相同URL的获取已在进行中，则后发出的请求不会执行，并触发此事件（Reference4=downloading）。此前标签会被静默忽略。

**対応:** SSP / Ninix

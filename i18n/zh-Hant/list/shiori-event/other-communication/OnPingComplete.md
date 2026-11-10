# OnPingComplete

**カテゴリ:** 其他通訊事件

透過 `\![execute,ping]` 完成指定次數的 ping 執行時觸發。

- **Reference0**: --event 所指定的字串原文
- **Reference1**: 來源位址 \[`\1`\] 總傳送次數 \[`\1`\] 成功次數 \[`\1`\] 失敗次數 \[`\1`\]各欄位之間以位元組值 1 分隔
- **Reference2**: 「OK」或錯誤資訊 \[`\1`\] 回應來源位址 \[`\1`\] RTT（往返所需時間，單位為 ms） \[`\1`\]各欄位之間以位元組值 1 分隔<br />
  從 Reference2 開始，會記錄每次已送出的 Ping 資訊。Progress 事件中的資料可能不完整。<br />
  錯誤資訊請參閱 [ICMP_ECHO_REPLY Structure 的 Status 標頭](http://msdn.microsoft.com/en-us/library/aa366053%28v=vs.85%29.aspx)。

**対応:** SSP

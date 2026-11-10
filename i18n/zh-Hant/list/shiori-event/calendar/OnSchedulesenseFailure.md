# OnSchedulesenseFailure

**カテゴリ:** 行事曆事件

排程感測器處理失敗時觸發。<br />
通知的對象不是特定 ghost，而是所有正在執行的 ghost。

與 Begin/Complete 不同，[定期檢查時也會觸發](caption_schedulesensetiming.md)。

- **Reference0**: [失敗原因](../headline-rss/caption_headlinesenseresult.md)（與 headline sensor 的原因共用）。無法取得時為can't download，成功取得但無法作為 iCal 解析時為can't analyze。
- **Reference1**: 排程感測器的名稱。定期檢查時沒有 Begin，因此若沒有此資訊，就無法得知是哪個感測器失敗

**対応:** SSP

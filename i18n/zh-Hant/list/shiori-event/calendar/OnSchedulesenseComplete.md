# OnSchedulesenseComplete

**カテゴリ:** 行事曆事件

行程感測器完成處理時觸發。<br />
此通知會傳送給所有正在執行的 ghost，而非特定 ghost。

**只有手動更新時才會觸發。**定期檢查時則如[下文](caption_schedulesensetiming.md)所述，不會觸發。<br />
即使成功取得資料但沒有更新（例如 304 Not Modified 或內容相同），仍會視為成功並觸發此事件。

- **Reference0**: 行程感測器名稱
- **Reference1**: 行程感測器傳回的行程資料筆數

**対応:** SSP

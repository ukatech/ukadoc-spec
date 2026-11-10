# OnNotifyOtherFailure

**カテゴリ:** 事件傳送失敗事件

`\![notifyother]`失敗時觸發。

- **Reference0**: 找不到時為 notfound。<br />
  在 `\t` 期間為 timecritical。<br />
  處於被動模式時為 passivemode。<br />
  處於誘導模式時為 inductionmode。<br />
  最小化時為 minimized。<br />
  其他情況則為 204 等執行結果。<br />
  若為 \_\_SYSTEM_ALL_GHOST\_\_ 等情況，則為以位元組值 1 分隔的清單。
- **Reference1**: ghost 名稱或 `\0` 名稱。<br />
  若為 \_\_SYSTEM_ALL_GHOST\_\_ 等情況，則為以位元組值 1 分隔的清單。
- **Reference2**: 嘗試執行的事件 ID。
- **Reference3～**: 嘗試執行的事件之 Reference。

**対応:** SSP

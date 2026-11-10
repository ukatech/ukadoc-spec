# OnNotifyHolidayInfo

**カテゴリ:** Notify 事件

通知今天的假日名稱。啟動時會緊接在 [OnNotifyUserInfo](OnNotifyUserInfo.md) 之後傳送。*\[NOTIFY\]*<br />
只有在 SSP 的語言資料夾中的假日表（holidays.txt；若有地區設定的國別假日表，則為 holidays-XX.txt）能取得今天的假日名稱時才會傳送；非假日或假日表中沒有列出名稱時不會傳送。<br />
「今天」會受到 SSP「目前時間的虛擬變更」（時光機）影響。

- **Reference0**: 假日名稱。（例如元旦、Christmas Day。補假時會顯示為「補假」或「Christmas Day (substitute day)」）
- **Reference1**: 日期。（以逗號分隔，例如 2026,01,01）
- **Reference2**: 已載入假日表的國家代碼（ISO 3166。若為 holidays-GB.txt，則為 GB）。若使用非國別的預設假日表（holidays.txt），則為空。

**対応:** SSP 2.9.11

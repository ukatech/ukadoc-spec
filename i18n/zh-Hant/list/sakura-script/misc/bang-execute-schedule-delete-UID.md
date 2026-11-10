# `\![execute,schedule-delete,UID,オプション...]`

**カテゴリ:** 未分類コマンド

從 ghost 專用行事曆中刪除指定 UID 的行程。無法刪除使用者行程或排程感測器的行程。<br />
結果會透過[OnExecuteScheduleComplete](../../shiori-event/other-communication/OnExecuteScheduleComplete.md)通知，失敗時（包括找不到對應行程）則透過[OnExecuteScheduleFailure](../../shiori-event/other-communication/OnExecuteScheduleFailure.md)通知。從 SSTP 等外部來源傳送的 script 無法執行此命令。<br />
只有 --event=事件 ID 這個選項。用法與[schedule-add](bang-execute-schedule-add.md)相同。

**対応:** SSP 2.8.91

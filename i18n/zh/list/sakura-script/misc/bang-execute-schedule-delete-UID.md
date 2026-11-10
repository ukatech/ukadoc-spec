# `\![execute,schedule-delete,UID,オプション...]`

**カテゴリ:** 未分类命令

从 ghost 专用日历中删除指定 UID 的日程。无法删除用户的日程或计划传感器的日程。<br />
结果通过[OnExecuteScheduleComplete](../../shiori-event/other-communication/OnExecuteScheduleComplete.md)通知，失败时（包括不存在相应日程的情况）则通过[OnExecuteScheduleFailure](../../shiori-event/other-communication/OnExecuteScheduleFailure.md)通知。无法执行从 SSTP 等外部发送的脚本。<br />
选项只有 --event=事件ID，与[schedule-add](bang-execute-schedule-add.md)相同。

**対応:** SSP 2.8.91

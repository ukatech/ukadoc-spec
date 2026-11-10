# OnExecuteScheduleComplete

**カテゴリ:** 其他通信事件

通过 [`\![execute,schedule-add]`](../../sakura-script/misc/bang-execute-schedule-add.md)・[`\![execute,schedule-delete]`](../../sakura-script/misc/bang-execute-schedule-delete-UID.md)向 ghost 的日程表添加或删除日程完成时触发。

通过 --event 指定以 On 开头的 ID 时，该 ID 会成为事件名。

- **Reference0**: 操作类型。add 或 delete
- **Reference1**: 目标日程的 UID。使用 schedule-add 时若省略 UID，则填入 SSP 分配的 UID。

**対応:** SSP 2.8.91

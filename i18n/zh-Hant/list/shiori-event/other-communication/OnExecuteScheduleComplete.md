# OnExecuteScheduleComplete

**カテゴリ:** 其他通訊事件

透過 [`\![execute,schedule-add]`](../../sakura-script/misc/bang-execute-schedule-add.md)・[`\![execute,schedule-delete]`](../../sakura-script/misc/bang-execute-schedule-delete-UID.md)完成向 ghost 的行程表新增或刪除項目時觸發。

若在 --event 中指定以 On 開頭的 ID，該 ID 會成為事件名稱。

- **Reference0**: 操作類型。add 或 delete
- **Reference1**: 目標行程的 UID。若在 schedule-add 中省略 UID，則會填入 SSP 指派的 UID。

**対応:** SSP 2.8.91

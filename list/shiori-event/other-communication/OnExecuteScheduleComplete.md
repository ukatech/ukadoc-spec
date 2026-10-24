# OnExecuteScheduleComplete

**カテゴリ:** その他通信イベント

[`\![execute,schedule-add]`](../../sakura-script/misc/bang-execute-schedule-add.md)・[`\![execute,schedule-delete]`](../../sakura-script/misc/bang-execute-schedule-delete-UID.md)で、ゴースト用の予定表への登録・削除が完了した際に発生。

--eventでOnから始まるIDを指定した場合は、そのIDがイベント名になる。

- **Reference0**: 操作の種類。add または delete
- **Reference1**: 対象の予定のUID。schedule-addでUIDを省略した場合は、SSPが割り当てたUIDが入る。

**対応:** SSP 2.8.91

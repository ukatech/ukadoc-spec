# OnExecuteScheduleComplete

**カテゴリ:** Other communication events

Occurs when adding or deleting an entry in the ghost's schedule is complete via [`\![execute,schedule-add]`](../../sakura-script/misc/bang-execute-schedule-add.md)・[`\![execute,schedule-delete]`](../../sakura-script/misc/bang-execute-schedule-delete-UID.md).

If an ID starting with On is specified with --event, that ID becomes the event name.

- **Reference0**: Operation type: add or delete
- **Reference1**: UID of the target schedule entry. If the UID is omitted in schedule-add, this contains the UID assigned by SSP.

**対応:** SSP 2.8.91

# OnExecuteScheduleFailure

**カテゴリ:** Other communication events

Occurs when `\![execute,schedule-add/schedule-delete]` fails.

If an ID starting with On is specified with --event, the event name is that ID with Failure appended.

- **Reference0**: Operation type: add or delete
- **Reference1**: Reason for failure<br />
  notauthorized : An attempt was made to add or delete an entry using a script sent from an external source such as SSTP<br />
  invalid : --summary or --start is missing, the date and time format is incorrect, the UID contains invalid characters, or the UID is missing from schedule-delete<br />
  notfound : No schedule entry with the specified UID exists for schedule-delete<br />
  save : Saving to a file failed (the addition or deletion itself has been applied)
- **Reference2**: Specified UID (empty if none)

**対応:** SSP 2.8.91

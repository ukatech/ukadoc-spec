# OnExecuteScheduleFailure

**カテゴリ:** Other communication events

Occurs when `\![execute,schedule-add/schedule-delete]` fails.

If an ID beginning with On is specified with --event, the event name is that ID with Failure appended.

- **Reference0**: Operation type: add or delete
- **Reference1**: Reason for the failure<br />
  notauthorized : An attempt was made to add or delete an entry using a script sent from outside, such as via SSTP<br />
  invalid : --summary or --start is missing, the date/time format is invalid, the UID contains invalid characters, or the UID is missing for schedule-delete<br />
  notfound : No schedule entry with the specified UID exists for schedule-delete<br />
  save : Saving to a file failed (the addition or deletion itself has been applied)
- **Reference2**: Specified UID (empty if none)

**対応:** SSP 2.8.91

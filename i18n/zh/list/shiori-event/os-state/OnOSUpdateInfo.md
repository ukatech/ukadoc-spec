# OnOSUpdateInfo

**カテゴリ:** OS state event

Notifies the dates and times of OS update checks and installations, along with update history.<br />
Notified via NOTIFY (cannot speak) immediately after startup, and via GET (can speak) shortly after an update is installed.

- **Reference0**: Check date and time: year, month, day, hour, minute, second; comma-separated; local time
- **Reference1**: Installation date and time: year, month, day, hour, minute, second; comma-separated; local time
- **Reference2～**: Update history entries follow in the format below. \[`\1`\] is byte value 1.<br />
  Status\[`\1`\]error code\[`\1`\]update time\[`\1`\]update details (title)<br />
  Status: one of not_started (not started), in_progress (in progress), success (successful), success_with_errors (successful with errors), fail (failed), abort (aborted), or unknown (unknown)<br />
  Error code: Non-zero if an error occurred during the update, or 0 otherwise. In Windows, this is 8 hexadecimal digits.<br />
  Update time: year, month, day, hour, minute, second; comma-separated; local time

**対応:** SSP 2.5.02

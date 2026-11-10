# OnOSUpdateInfo

**カテゴリ:** OS state event

Notifies the date and time OS updates were checked and installed, along with update history.<br />
Sent as NOTIFY (cannot speak) immediately after startup, and as GET (can speak) after a short delay when an update is installed.

- **Reference0**: Check date and time: year, month, day, hour, minute, second, comma-separated, local time
- **Reference1**: Installation date and time: year, month, day, hour, minute, second, comma-separated, local time
- **Reference2～**: Update history entries follow in the format below. \[`\1`\] is byte value 1.<br />
  Status\[`\1`\]error code\[`\1`\]update time\[`\1`\]update content (title)<br />
  Status: one of not_started (not started), in_progress (in progress), success (successful), success_with_errors (completed, but with errors), fail (failed), abort (aborted), or unknown (unknown)<br />
  Error code: Nonzero if an error occurred during the update; otherwise 0. On Windows, this is 8 hexadecimal digits.<br />
  Update time: year, month, day, hour, minute, second, comma-separated, local time

**対応:** SSP 2.5.02

# developer.log.log-type.index(ID).log-property-name

**カテゴリ:** Property System

Retrieve information from the log entry at the specified ID.<br />
IDs are numbered 0, 1, 2... from newest to oldest. Retrieval fails if the specified ID is out of range.<br />
For log types, see [developer.log.ログ種別.count](developer.log.-.count.md). The following strings can be used as log property names.

- **type**: Log type.<br />
  In script, the format is Ghost(...) or SSTP(...), with the applicable attributes listed inside the parentheses, separated by commas (Ghost: External, Embed, SSF, Plugin; SSTP: Local or Remote, TempGhost, Auth; both: NoTranslate). If no attributes apply to Ghost, the parentheses are omitted, leaving only Ghost. If there is additional information, it is appended as ":additional information".<br />
  For other log types, the value is one of Info, Notice, Warning, Error, Critical, or System.
- **name**: Name of the log source (such as the ghost name). If there is no source, the value is \[SYSTEM\].
- **value**: Log message. The entire message is returned, even if it is long.
- **time**: Date and time when the log was recorded. The local time is formatted using the OS's short date format, followed by a space and the time in 24-hour hours:minutes format. The format depends on the OS regional settings.

**対応:** SSP

# developer.log.log type.index(ID).log property name

**カテゴリ:** Property System

Retrieve information from the log entry at index ID.<br />
IDs are numbered 0, 1, 2... starting with the newest entry. If an out-of-range ID is specified, retrieval fails.<br />
See [developer.log.ログ種別.count](developer.log.-.count.md) for log types. The following strings can be used as log property names.

- **type**: Log type.<br />
  For script, the format is Ghost(...) or SSTP(...), with the applicable attributes listed inside the parentheses, separated by commas (Ghost: External, Embed, SSF, Plugin　SSTP: Local or Remote, TempGhost, Auth　Common: NoTranslate). If no attributes apply to Ghost, the parentheses are omitted, leaving only Ghost. If additional information is available, ":additional information" is appended.<br />
  For other log types, one of Info, Notice, Warning, Error, Critical, or System.
- **name**: Name of the log source (such as the ghost name). If there is no source, this is \[SYSTEM\].
- **value**: Log message. The full text is returned, even for long messages.
- **time**: Date and time when the log was recorded. This is in local time, with the OS's short date format and 24-hour hour:minute notation separated by a half-width space. The format depends on the OS regional settings.

**対応:** SSP

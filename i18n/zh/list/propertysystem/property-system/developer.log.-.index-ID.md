# developer.log.log type.index(ID).log property name

**カテゴリ:** Property system

Retrieve information from the log at the specified ID.<br />
IDs are ordered from newest to oldest, starting at 0, 1, 2... If an out-of-range ID is specified, retrieval fails.<br />
For log types, see [developer.log.log type.count](developer.log.-.count.md). The following strings can be used as log property names.

- **type**: Log type.<br />
  For script, the format is Ghost(...) or SSTP(...), with the applicable attributes listed inside the parentheses, separated by commas (Ghost: External, Embed, SSF, Plugin　SSTP: Local or Remote, TempGhost, Auth　Common: NoTranslate). If a Ghost has no applicable attributes, the parentheses are omitted and only Ghost is shown. If there is additional information, it is appended at the end as ":additional information".<br />
  For other log types, the value is one of Info, Notice, Warning, Error, Critical, or System.
- **name**: Name of the log source (such as a ghost name). If there is no source, the value is \[SYSTEM\].
- **value**: Log text. The entire text is returned, even if it is long.
- **time**: Date and time when the log was recorded. It uses local time, with the OS short date format and 24-hour hour:minute notation separated by a half-width space. The format depends on the OS regional settings.

**対応:** SSP

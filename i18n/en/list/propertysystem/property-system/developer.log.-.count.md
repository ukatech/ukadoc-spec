# developer.log.log type.count

**カテゴリ:** Property system

The current number of log entries recorded by SSP. The following strings can be used as log types:

- **script**: Script log (the Script type in the log window).
- **error**: Error log (the Error type).
- **network**: Network log (the Network type).
- **update**: Update log (the Update type).

Each log type has a limit on the number of entries it retains (50 by default); when the limit is exceeded, the oldest entries are removed.<br />
All developer.log.～ properties are read-only and can be retrieved regardless of the developer feature settings.<br />
In error logs, consecutive entries with the same content may be consolidated into one summary entry with type System.

**対応:** SSP

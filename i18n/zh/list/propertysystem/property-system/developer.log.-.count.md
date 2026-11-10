# developer.log.log type.count

**カテゴリ:** Property System

The current number of log entries recorded by SSP. The following strings can be used as log types.

- **script**: Script log (the Script type in the log window).
- **error**: Error log (the Error type).
- **network**: Network log (the Network type).
- **update**: Update log (the Update type).

Each log has a maximum number of entries (50 by default); entries are removed starting with the oldest when this limit is exceeded.<br />
All developer.log.～ properties are read-only and can be retrieved regardless of the developer feature settings.<br />
In the error log, consecutive entries with the same content may be condensed into a single summary entry with type System.

**対応:** SSP

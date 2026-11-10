# OnNotifyHolidayInfo

**カテゴリ:** Notify event

Notifies today's holiday name. Sent at startup, immediately after [OnNotifyUserInfo](OnNotifyUserInfo.md). *\[NOTIFY\]*<br />
Sent only if today's holiday name can be found in the holiday table in an SSP language folder (holidays.txt, or holidays-XX.txt if a country-specific table exists for the regional settings). Not sent on non-holidays or when the holiday table does not list a name for the holiday.<br />
“Today” is affected by SSP's 「virtual time adjustment」 (time machine).

- **Reference0**: Holiday name (such as New Year's Day or Christmas Day. Substitute holidays are named, for example, “Substitute Holiday” or “Christmas Day (substitute day)”).
- **Reference1**: Date (comma-separated, such as 2026,01,01).
- **Reference2**: Country code of the loaded holiday table (ISO 3166; GB for holidays-GB.txt). Empty for the default country-neutral table (holidays.txt).

**対応:** SSP 2.9.11

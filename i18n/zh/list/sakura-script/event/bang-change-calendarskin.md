# `\![change,calendarskin,カレンダースキン名]`

**カテゴリ:** Event command

Switches the calendar skin. This is equivalent to selecting a skin from the calendar menu.<br />
If the specified calendar skin does not exist, this command is ignored.<br />
If the calendar has never been opened, only the setting is changed; it takes effect the next time the calendar is opened.

Setting the calendar skin name to lastinstalled switches to the last calendar skin installed. However, this is unavailable after SSP has been exited once.<br />
Setting the calendar skin name to random switches to a randomly selected skin.<br />
The calendar skin name is notified through [installedcalendarskinname](../../shiori-event/notify/installedcalendarskinname.md).

**対応:** SSP 2.8.93

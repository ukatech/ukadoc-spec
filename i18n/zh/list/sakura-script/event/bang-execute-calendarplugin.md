# `\![execute,calendarplugin,カレンダープラグイン名]`

**カテゴリ:** Event command

Starts retrieving events from the calendar plugin (schedule sensor). This is equivalent to selecting a plugin from the calendar menu.<br />
This command runs even when the calendar is not displayed.<br />
Setting the calendar plugin name to random selects one at random.<br />
Setting it to lastinstalled runs the last calendar plugin installed. However, this is unavailable after SSP has been exited once.<br />
If the specified calendar plugin does not exist, this command is ignored.<br />
The calendar plugin name is notified through [installedcalendarpluginname](../../shiori-event/notify/installedcalendarpluginname.md).

**対応:** SSP 2.8.93

# OnNotifyDressupInfo

**カテゴリ:** Notify event

Notifies dressup information.<br />
Sent as *\[NOTIFY\]* only at startup; for user actions such as switching from the menu, it is sent as *\[GET\]*.<br />
See also [OnDressupChanged](../boot-close-change/OnDressupChanged.md), which occurs before this event.

- **Reference\***: The following information, separated by byte value 1: \[character ID, category name, part name, options, enabled 1/disabled 0, thumbnail path\]<br />
  Multiple options may be included, separated by commas.<br />
  Repeated for each dressup definition.<br />
  The ghost can determine what changed by processing the differences in enabled/disabled status since the previous notification.

**対応:** SSP

# `\![call,ghost,ゴースト名(,--option=raise-event)]`

**カテゴリ:** Event commands

Calls the ghost specified by name.<br />
Set the ghost name to lastinstalled to call the last installed ghost.<br />
Set the ghost name to random to call a random ghost.<br />
\[SSP 2.9.35\] The ghost's [UUID](../../propertysystem/property-system/general-property/uuid.md) can also be specified instead of its name, avoiding confusion between ghosts with the same name.

In SSP 2.4.74 and later, adding --option=raise-event after the ghost name notifies [OnGhostCalling](../../shiori-event/boot-close-change/OnGhostCalling.md), as when switching from the menu.<br />
If omitted, the event is not notified.

**対応:** SSP / Ninix

## 記述例

```sakurascript
Emily/Phase4.5を呼び出す。\![call,ghost,Emily/Phase4.5]
```

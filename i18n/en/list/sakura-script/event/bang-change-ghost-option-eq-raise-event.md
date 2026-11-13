# `\![change,ghost,ゴースト名(,--option=raise-event)]`

**カテゴリ:** Event commands

Switches to the specified ghost.<br />
Set the ghost name to random for a random change (equivalent to `\+`).<br />
Set it to sequential for a sequential change (equivalent to `\_+`).<br />
If the specified ghost does not exist, the command is ignored.

Set the ghost name to lastinstalled to switch to the last installed ghost. This is invalid if SSP has been shut down since installation.<br />
Set the ghost name to random to switch to a random ghost.

\[SSP 2.9.35\] The ghost's [UUID](../../propertysystem/property-system/general-property/uuid.md) can also be specified instead of its name, avoiding confusion between ghosts with the same name.

In SSP 2.4.74 and later, adding --option=raise-event after the ghost name notifies [OnGhostChanging](../../shiori-event/boot-close-change/OnGhostChanging.md), as when switching from the menu.<br />
In this case, the operation can also be canceled with a balloon break (normally a double-click).<br />
If omitted, the event is not notified.

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
Emily/Phase4.5に交代。\![change,ghost,Emily/Phase4.5]
```

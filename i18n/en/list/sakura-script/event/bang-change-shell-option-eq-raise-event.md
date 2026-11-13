# `\![change,shell,シェル名(,--option=raise-event)]`

**カテゴリ:** Event commands

Switches to the specified shell.<br />
If the shell does not exist, the command is ignored.<br />
After the change, the SHIORI event [OnShellChanged](../../shiori-event/boot-close-change/OnShellChanged.md) is notified.

Set the shell name to lastinstalled to switch to the last installed ghost. This is invalid if SSP has been shut down since installation.<br />
Set the shell name to random to switch to a random shell.

\[SSP 2.9.35\] The shell's [UUID](../../propertysystem/property-system/general-property/uuid.md) can also be specified instead of its name.

In SSP 2.4.74 and later, adding --option=raise-event after the shell name notifies [OnShellChanging](../../shiori-event/boot-close-change/OnShellChanging.md), as when switching from the menu.<br />
In this case, the operation can also be canceled with a balloon break (normally a double-click).<br />
If omitted, the event is not notified.

**対応:** SSP / CROW / Ninix

## 記述例

```sakurascript
masterシェルに切り替え。\![change,shell,master]
```

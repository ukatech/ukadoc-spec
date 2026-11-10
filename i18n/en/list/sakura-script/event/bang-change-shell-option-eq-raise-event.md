# `\![change,shell,シェル名(,--option=raise-event)]`

**カテゴリ:** Event command

Switches to that shell.<br />
If the specified shell does not exist, the command is ignored.<br />
After the change, the SHIORI event [OnShellChanged](../../shiori-event/boot-close-change/OnShellChanged.md) is notified.

If the shell name is lastinstalled, switches to the ghost most recently installed. However, this does not work if SSP has been exited in the meantime.<br />
If the shell name is random, switches to a random shell.

In SSP 2.4.74 and later, appending --option=raise-event after the shell name causes [OnShellChanging](../../shiori-event/boot-close-change/OnShellChanging.md) to be notified, just as when switching shells from the menu.<br />
Note that in this case, the switch can also be canceled using a balloon break (usually a double-click).<br />
If this option is not specified, no event is sent.

**対応:** SSP / CROW / Ninix

## 記述例

```sakurascript
masterシェルに切り替え。\![change,shell,master]
```

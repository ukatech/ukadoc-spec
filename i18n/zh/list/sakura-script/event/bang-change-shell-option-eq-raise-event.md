# `\![change,shell,シェル名(,--option=raise-event)]`

**カテゴリ:** Event command

Switches to the specified shell.<br />
If the specified shell does not exist, this command is ignored.<br />
After the change, the SHIORI event [OnShellChanged](../../shiori-event/boot-close-change/OnShellChanged.md) is notified.

Setting the shell name to lastinstalled switches to the last ghost installed. However, this is unavailable after SSP has been exited once.<br />
Setting the shell name to random switches to a randomly selected shell.

In SSP 2.4.74 and later, appending --option=raise-event to the shell name causes [OnShellChanging](../../shiori-event/boot-close-change/OnShellChanging.md) to be notified, just as when switching shells from the menu.<br />
Note that in this case, the change can also be canceled by a balloon break (usually a double-click).<br />
If this option is not specified, the event is not notified.

**対応:** SSP / CROW / Ninix

## 記述例

```sakurascript
masterシェルに切り替え。\![change,shell,master]
```

# `\![change,ghost,ゴースト名(,--option=raise-event)]`

**カテゴリ:** Event command

Switches to the specified ghost.<br />
Setting the ghost name to random performs a random change (equivalent to `\+`).<br />
Setting it to sequential performs a sequential change (equivalent to `\_+`).<br />
If the specified ghost does not exist when the command is executed, it is ignored.

Setting the ghost name to lastinstalled switches to the last ghost installed. However, this is unavailable after SSP has been exited once.<br />
Setting the ghost name to random switches to a randomly selected ghost.

In SSP 2.4.74 and later, appending --option=raise-event to the ghost name causes [OnGhostChanging](../../shiori-event/boot-close-change/OnGhostChanging.md) to be notified, just as when switching ghosts from the menu.<br />
Note that in this case, the change can also be canceled by a balloon break (usually a double-click).<br />
If this option is not specified, the event is not notified.

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
Emily/Phase4.5に交代。\![change,ghost,Emily/Phase4.5]
```

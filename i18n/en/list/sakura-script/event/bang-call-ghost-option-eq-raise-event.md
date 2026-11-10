# `\![call,ghost,ゴースト名(,--option=raise-event)]`

**カテゴリ:** Event command

Calls the ghost specified by the ghost name.<br />
Set the ghost name to lastinstalled to call the last installed ghost.<br />
Set the ghost name to random to call a randomly selected ghost.

In SSP 2.4.74 and later, adding --option=raise-event after the ghost name causes [OnGhostCalling](../../shiori-event/boot-close-change/OnGhostCalling.md) to be notified, just as when switching ghosts from the menu.<br />
If not specified, the event is not notified.

**対応:** SSP / Ninix

## 記述例

```sakurascript
Emily/Phase4.5を呼び出す。\![call,ghost,Emily/Phase4.5]
```

# `\![change,ghost,ゴースト名(,--option=raise-event)]`

**カテゴリ:** Event command

Switches to the specified ghost.<br />
If the ghost name is random, switches randomly (same as `\+`).<br />
If the ghost name is sequential, switches sequentially (same as `\_+`).<br />
After execution, if the specified ghost is not present, the command is ignored.

If the ghost name is lastinstalled, switches to the last ghost installed. However, this is invalid if SSP has been exited once.<br />
If the ghost name is random, switches randomly.

In SSP 2.4.74 and later, specifying --option=raise-event after the ghost name causes [OnGhostChanging](../../shiori-event/boot-close-change/OnGhostChanging.md) to be notified, just as when switching ghosts from the menu.<br />
Note that in this case, switching can also be canceled by breaking the balloon (normally by double-clicking).<br />
If this option is not specified, no notification is sent.

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
Emily/Phase4.5に交代。\![change,ghost,Emily/Phase4.5]
```

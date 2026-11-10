# `\![change,ghost,ゴースト名(,--option=raise-event)]`

**カテゴリ:** 事件命令

切换到指定的 ghost。<br />
将 ghost 名称设为 random 时，会随机切换（与 `\+` 相同）。<br />
设为 sequential 时，会按顺序切换（与 `\_+` 相同）。<br />
执行后，如果没有对应的 ghost，则忽略此命令。

将 ghost 名称设为 lastinstalled 时，会切换到最后安装的 ghost。但如果 SSP 曾经退出，则此功能无效。<br />
将 ghost 名称设为 random 时，会随机切换。

在 SSP 2.4.74 及更高版本中，在 ghost 名称后添加 --option=raise-event 后，会像通过菜单进行切换操作时一样通知[OnGhostChanging](../../shiori-event/boot-close-change/OnGhostChanging.md)。<br />
请注意，在这种情况下，也可以通过 balloon break（通常为双击）取消操作。<br />
未指定此选项时不会发出通知。

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
Emily/Phase4.5に交代。\![change,ghost,Emily/Phase4.5]
```

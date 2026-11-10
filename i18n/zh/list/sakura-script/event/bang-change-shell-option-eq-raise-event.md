# `\![change,shell,シェル名(,--option=raise-event)]`

**カテゴリ:** 事件命令

切换到指定的 shell。<br />
如果没有对应的 shell，则忽略此命令。<br />
切换后会通知 SHIORI 事件[OnShellChanged](../../shiori-event/boot-close-change/OnShellChanged.md)。

将 shell 名称设为 lastinstalled 时，会切换到最后安装的 ghost。但如果 SSP 曾经退出，则此功能无效。<br />
将 shell 名称设为 random 时，会随机切换。

在 SSP 2.4.74 及更高版本中，在 shell 名称后添加 --option=raise-event 后，会像通过菜单进行切换操作时一样通知[OnShellChanging](../../shiori-event/boot-close-change/OnShellChanging.md)。<br />
请注意，在这种情况下，也可以通过 balloon break（通常为双击）取消操作。<br />
未指定此选项时不会发出通知。

**対応:** SSP / CROW / Ninix

## 記述例

```sakurascript
masterシェルに切り替え。\![change,shell,master]
```

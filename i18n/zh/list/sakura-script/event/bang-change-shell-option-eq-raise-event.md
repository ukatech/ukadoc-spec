# `\![change,shell,シェル名(,--option=raise-event)]`

**カテゴリ:** 事件命令

切换到指定的 shell。<br />
如果不存在相应的 shell，则忽略此命令。<br />
切换后会通知 SHIORI 事件 [OnShellChanged](../../shiori-event/boot-close-change/OnShellChanged.md)。

将 shell 名称设为 lastinstalled 时，切换到最后安装的 ghost。但如果 SSP 已退出过一次，则无效。<br />
将 shell 名称设为 random 时，随机切换。

\[SSP 2.9.35\] 也可以指定 shell 的 [UUID](../../propertysystem/property-system/general-property/uuid.md) 来代替 shell 名称。

在 SSP 2.4.74 及更高版本中，在 shell 名称后指定 --option=raise-event 时，会像通过菜单切换时一样通知 [OnShellChanging](../../shiori-event/boot-close-change/OnShellChanging.md)。<br />
注意，此时也可以通过 balloon break（通常为双击）中止操作。<br />
不指定时则不会通知。

**対応:** SSP / CROW / Ninix

## 記述例

```sakurascript
masterシェルに切り替え。\![change,shell,master]
```

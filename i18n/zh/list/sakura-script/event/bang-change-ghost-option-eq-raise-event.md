# `\![change,ghost,ゴースト名(,--option=raise-event)]`

**カテゴリ:** 事件命令

切换到指定的 ghost。<br />
将 ghost 名称设为 random 时，随机切换（与 `\+` 相同）。<br />
设为 sequential 时，按顺序切换（与 `\_+` 相同）。<br />
执行时，如果不存在相应的 ghost，则忽略此命令。

将 ghost 名称设为 lastinstalled 时，切换到最后安装的 ghost。但如果 SSP 已退出过一次，则无效。<br />
将 ghost 名称设为 random 时，随机切换。

\[SSP 2.9.35\] 也可以指定 ghost 的 [UUID](../../propertysystem/property-system/general-property/uuid.md) 来代替 ghost 名称（避免混淆同名的 ghost）。

在 SSP 2.4.74 及更高版本中，在 ghost 名称后指定 --option=raise-event 时，会像通过菜单切换时一样通知 [OnGhostChanging](../../shiori-event/boot-close-change/OnGhostChanging.md)。<br />
注意，此时也可以通过 balloon break（通常为双击）中止操作。<br />
不指定时则不会通知。

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
Emily/Phase4.5に交代。\![change,ghost,Emily/Phase4.5]
```

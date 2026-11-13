# `\![call,ghost,ゴースト名(,--option=raise-event)]`

**カテゴリ:** 事件命令

调用由 ghost 名称指定的 ghost。<br />
将 ghost 名称设为 lastinstalled 时，调用最后安装的 ghost。<br />
将 ghost 名称设为 random 时，随机调用。<br />
\[SSP 2.9.35\] 也可以指定 ghost 的 [UUID](../../propertysystem/property-system/general-property/uuid.md) 来代替 ghost 名称（避免混淆同名的 ghost）。

在 SSP 2.4.74 及更高版本中，在 ghost 名称后指定 --option=raise-event 时，会像通过菜单切换时一样通知 [OnGhostCalling](../../shiori-event/boot-close-change/OnGhostCalling.md)。<br />
不指定时则不会通知。

**対応:** SSP / Ninix

## 記述例

```sakurascript
Emily/Phase4.5を呼び出す。\![call,ghost,Emily/Phase4.5]
```

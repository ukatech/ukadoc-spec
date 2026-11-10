# `\![call,ghost,ゴースト名(,--option=raise-event)]`

**カテゴリ:** 事件命令

调用指定名称的ghost。<br />
将ghost名称设为lastinstalled时，调用最后安装的ghost。<br />
将ghost名称设为random时，随机调用一个ghost。

在 SSP 2.4.74 及更高版本中，在ghost名称后添加--option=raise-event时，与通过菜单执行切换操作一样，会通知[OnGhostCalling](../../shiori-event/boot-close-change/OnGhostCalling.md)。<br />
未指定时不会通知。

**対応:** SSP / Ninix

## 記述例

```sakurascript
Emily/Phase4.5を呼び出す。\![call,ghost,Emily/Phase4.5]
```

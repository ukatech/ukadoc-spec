# `\![change,balloon,バルーン名]`

**カテゴリ:** 事件命令

切换到指定的 balloon。<br />
如果不存在相应的 balloon，则忽略此命令。<br />
切换后会通知 SHIORI 事件 [OnBalloonChange](../../shiori-event/boot-close-change/OnBalloonChange.md)。

将 balloon 名称设为 lastinstalled 时，切换到最后安装的 balloon。但如果 SSP 已退出过一次，则无效。<br />
将 balloon 名称设为 random 时，随机切换。

\[SSP 2.9.35\] 也可以指定 balloon 的 [UUID](../../propertysystem/property-system/general-property/uuid.md) 来代替 balloon 名称。

**対応:** SSP / Ninix

## 記述例

```sakurascript
SSPデフォルト+にバルーン変更。\![change,balloon,SSPデフォルト+]
```

# `\![change,balloon,バルーン名]`

**カテゴリ:** 事件命令

切换到指定的 balloon。<br />
如果没有对应的 balloon，则忽略此命令。<br />
切换后会通知 SHIORI 事件[OnBalloonChange](../../shiori-event/boot-close-change/OnBalloonChange.md)。

将 balloon 名称设为 lastinstalled 时，会切换到最后安装的 balloon。但如果 SSP 曾经退出，则此功能无效。<br />
将 balloon 名称设为 random 时，会随机切换。

**対応:** SSP / Ninix

## 記述例

```sakurascript
SSPデフォルト+にバルーン変更。\![change,balloon,SSPデフォルト+]
```

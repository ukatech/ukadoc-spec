# `\![change,balloon,バルーン名]`

**カテゴリ:** 事件指令

切換至該 balloon。<br />
若不存在相應的 balloon，則忽略。<br />
切換後會通知 SHIORI 事件 [OnBalloonChange](../../shiori-event/boot-close-change/OnBalloonChange.md)。

將 balloon 名稱設為 lastinstalled，即可切換至最後安裝的 balloon。但若曾結束 SSP，則此設定無效。<br />
將 balloon 名稱設為 random，即可隨機切換。

**対応:** SSP / Ninix

## 記述例

```sakurascript
SSPデフォルト+にバルーン変更。\![change,balloon,SSPデフォルト+]
```

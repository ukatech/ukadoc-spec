# `\![change,balloon,バルーン名]`

**カテゴリ:** 事件指令

切換至指定的 balloon。<br />
若找不到對應的 balloon，則忽略此指令。<br />
變更後會通知 SHIORI 事件 [OnBalloonChange](../../shiori-event/boot-close-change/OnBalloonChange.md)。

將 balloon 名稱設為 lastinstalled 時，切換至最後安裝的 balloon。但若 SSP 已經結束過一次，則無效。<br />
將 balloon 名稱設為 random 時，隨機切換。

\[SSP 2.9.35\] 也可指定 balloon 的 [UUID](../../propertysystem/property-system/general-property/uuid.md) 代替 balloon 名稱。

**対応:** SSP / Ninix

## 記述例

```sakurascript
SSPデフォルト+にバルーン変更。\![change,balloon,SSPデフォルト+]
```

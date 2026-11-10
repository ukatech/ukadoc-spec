# `\![change,balloon,バルーン名]`

**カテゴリ:** Event command

Switches to the specified balloon.<br />
If the specified balloon does not exist, this command is ignored.<br />
After the change, the SHIORI event [OnBalloonChange](../../shiori-event/boot-close-change/OnBalloonChange.md) is notified.

Setting the balloon name to lastinstalled switches to the last balloon installed. However, this is unavailable after SSP has been exited once.<br />
Setting the balloon name to random switches to a randomly selected balloon.

**対応:** SSP / Ninix

## 記述例

```sakurascript
SSPデフォルト+にバルーン変更。\![change,balloon,SSPデフォルト+]
```

# `\![bind,カテゴリ名,パーツ名,数値]`

**カテゴリ:** Surface command

Wear or remove dressup parts.<br />
For the numeric value, 1 means wear and 0 means remove.<br />
If the part name is left blank, the operation applies to the entire category.<br />
If the numeric value is left blank or omitted, the setting toggles ON/OFF as when using the menu.<br />
After the script runs, the SHIORI event OnDressupChanged is notified, followed by the SHIORI event OnNotifyDressupInfo.

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![bind,head,ribbon,1]本体側の着せ替えとして設定された、headカテゴリのribbonを装着。\1\![bind,arm,,0]相方側の着せ替えとして設定された、armカテゴリのパーツを全て解除。
```

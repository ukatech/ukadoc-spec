# `\![bind,カテゴリ名,パーツ名,数値]`

**カテゴリ:** Surface command

Dress or undress dressup parts.<br />
The numeric value is 1 to dress and 0 to undress.<br />
If the part name is empty, the operation applies to the entire category.<br />
If the numeric value is empty or omitted, it toggles ON/OFF as when using the menu.<br />
After the script runs, the SHIORI event OnDressupChanged is notified, followed by the SHIORI event OnNotifyDressupInfo.

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![bind,head,ribbon,1]本体側の着せ替えとして設定された、headカテゴリのribbonを装着。\1\![bind,arm,,0]相方側の着せ替えとして設定された、armカテゴリのパーツを全て解除。
```

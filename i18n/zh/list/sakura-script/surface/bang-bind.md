# `\![bind,カテゴリ名,パーツ名,数値]`

**カテゴリ:** Surface command

Put on or remove dressup parts.<br />
The numeric value is 1 to put on and 0 to remove.<br />
Leaving the part name blank performs the operation for the entire category.<br />
Leaving the numeric field blank or omitting it toggles ON/OFF, as with menu operations.<br />
After the script runs, the SHIORI event OnDressupChanged is notified, followed by the SHIORI event OnNotifyDressupInfo.

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![bind,head,ribbon,1]本体側の着せ替えとして設定された、headカテゴリのribbonを装着。\1\![bind,arm,,0]相方側の着せ替えとして設定された、armカテゴリのパーツを全て解除。
```

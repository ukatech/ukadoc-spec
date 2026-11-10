# `\![bind,カテゴリ名,パーツ名,数値]`

**カテゴリ:** surface 指令

穿上或脫下 dressup 零件。<br />
數值部分為 1 時穿上，為 0 時脫下。<br />
零件名稱留空時，會以類別為單位執行操作。<br />
數值欄留空或省略時，會像操作選單一樣切換 ON/OFF。<br />
執行指令後會通知 SHIORI 事件 OnDressupChanged，接著通知 SHIORI 事件 OnNotifyDressupInfo。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![bind,head,ribbon,1]本体側の着せ替えとして設定された、headカテゴリのribbonを装着。\1\![bind,arm,,0]相方側の着せ替えとして設定された、armカテゴリのパーツを全て解除。
```

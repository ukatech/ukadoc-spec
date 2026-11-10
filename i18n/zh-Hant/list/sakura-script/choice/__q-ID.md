# `\__q[ID,...]`

**カテゴリ:** 選項指令

將直到出現`\__q`為止的範圍設為選項。<br />
ID 規格與`\q`相同，包括以 On 或 script: 開頭的 ID 會受到特殊處理，以及 ID 引數的處理方式。<br />
執行後發生的 SHIORI Event 也相同。<br />
與`\q[]`標籤不同，此標籤也會自動換行。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\__q[OnTest,testreference]間にさくらスクリプトも挟める。\n改行、\_l[50,50]カーソル移動も可能で、画像を貼れば画像が選択肢になる。\__qこの例の場合、IDが「On」から始まっているため、選択時にOnTestイベントが発生し、reference0には「testreference」が格納されている。
```

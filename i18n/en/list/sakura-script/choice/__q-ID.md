# `\__q[ID,...]`

**カテゴリ:** Choice command

The range up to `\__q` becomes a choice.<br />
The ID specification is the same as for `\q`, including the special handling of IDs beginning with On or script:, and the handling of ID arguments.<br />
The SHIORI Event generated after execution is also the same.<br />
Unlike the `\q[]` tag, this command also inserts a line break automatically.

**対応:** SSP / Ninix

## 記述例

```sakurascript
\__q[OnTest,testreference]間にさくらスクリプトも挟める。\n改行、\_l[50,50]カーソル移動も可能で、画像を貼れば画像が選択肢になる。\__qこの例の場合、IDが「On」から始まっているため、選択時にOnTestイベントが発生し、reference0には「testreference」が格納されている。
```

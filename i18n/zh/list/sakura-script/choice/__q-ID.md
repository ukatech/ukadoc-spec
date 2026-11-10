# `\__q[ID,...]`

**カテゴリ:** 选项命令

将直到遇到`\__q`为止的范围设为选项。<br />
ID 规则与`\q`相同，包括以 On 或 script: 开头的 ID 会被特殊处理，以及 ID 参数的处理方式。<br />
执行后发生的 SHIORI Event 也相同。<br />
与`\q[]`标签不同，此命令也会自动换行。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\__q[OnTest,testreference]間にさくらスクリプトも挟める。\n改行、\_l[50,50]カーソル移動も可能で、画像を貼れば画像が選択肢になる。\__qこの例の場合、IDが「On」から始まっているため、選択時にOnTestイベントが発生し、reference0には「testreference」が格納されている。
```

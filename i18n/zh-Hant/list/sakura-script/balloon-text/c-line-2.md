# `\c[line,数値,開始位置]`

**カテゴリ:** balloon, text command

Clears the specified number of lines from the start position (line number) in the current scope. The start position is zero-based (0 for the first line, 1 for the second). The determination of which lines are cleared is the same as for `\c[line,数値]`.

**対応:** SSP

## 記述例

```sakurascript
トークを3行目から、\n1行削除。\nこの部分が\_l[,]削除される。\c[line,1,2]削除終了。
```

# `\c[line,数値,開始位置]`

**カテゴリ:** Balloon, text command

Clears the specified number of lines on the current scope, starting at the specified position (line number). The start position is zero-based (0 for the first line, 1 for the second). The criteria for which lines are cleared are the same as for `\c[line,数値]`.

**対応:** SSP

## 記述例

```sakurascript
トークを3行目から、\n1行削除。\nこの部分が\_l[,]削除される。\c[line,1,2]削除終了。
```

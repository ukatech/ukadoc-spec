# `\c[line,数値,開始位置]`

**カテゴリ:** balloon, text command

Clears the specified number of lines starting at the specified position (line number) in the current scope. The starting position is zero-based (the 1st line is 0, the 2nd is 1). The lines cleared are determined in the same way as with `\c[line,数値]`.

**対応:** SSP

## 記述例

```sakurascript
トークを3行目から、\n1行削除。\nこの部分が\_l[,]削除される。\c[line,1,2]削除終了。
```

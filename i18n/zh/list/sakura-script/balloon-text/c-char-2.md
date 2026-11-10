# `\c[char,数値,開始位置]`

**カテゴリ:** balloon, text command

Clears the specified number of characters starting at the specified position in the current scope. The starting position is zero-based (the 1st character is 0, the 2nd is 1). The characters cleared are determined in the same way as with `\c[char,数値]`.

**対応:** SSP

## 記述例

```sakurascript
トークの5文字目から、3文字削除\c[char,3,4]削除終了。
```

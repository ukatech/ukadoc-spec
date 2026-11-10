# `\c[char,数値,開始位置]`

**カテゴリ:** balloon, text command

Clears the specified number of characters from the specified position in the current scope. The start position is zero-based (0 for the first character, 1 for the second). The determination of which characters are cleared is the same as for `\c[char,数値]`.

**対応:** SSP

## 記述例

```sakurascript
トークの5文字目から、3文字削除\c[char,3,4]削除終了。
```

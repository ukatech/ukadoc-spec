# `\c[char,数値,開始位置]`

**カテゴリ:** Balloon, text command

Clears the specified number of characters on the current scope, starting at the specified position. The start position is zero-based (0 for the first character, 1 for the second). The criteria for which characters are cleared are the same as for `\c[char,数値]`.

**対応:** SSP

## 記述例

```sakurascript
トークの5文字目から、3文字削除\c[char,3,4]削除終了。
```

# `\c[char,数値]`

**カテゴリ:** balloon, text command

Clears the specified number of characters from the cursor position in the current scope. The characters to be cleared are determined by their order of appearance in the script, regardless of their position in the balloon. An image pasted with `\_b[ファイルパス,inline]` is treated as one character and is cleared.

**対応:** SSP

## 記述例

```sakurascript
トークを3文字削除\c[char,3]削除終了。
```

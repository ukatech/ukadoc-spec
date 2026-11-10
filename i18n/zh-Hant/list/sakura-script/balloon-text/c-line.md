# `\c[line,数値]`

**カテゴリ:** balloon, text command

Clears the specified number of lines from the balloon cursor position in the current scope.<br />
Content divided into “lines” by `\_l[x,y]`, `\n`, `\n[half]`, or `\n[パーセント]` is treated as lines. However, empty content divided by anything other than `\_l[x,y]`, such as `\n\n`, is not treated as a line.<br />
As with `\c[char,数値]`, the order of appearance in the script is used.

**対応:** SSP

## 記述例

```sakurascript
トークを1行削除。\nこの行が削除される。\c[line,1]削除終了。\nこの行は削除される。\n\n\n\n\n\c[line,1]削除終了。\nこの行は削除されない。\_l[0,0]\c[line,1]削除終了。
```

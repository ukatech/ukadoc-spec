# `\c[line,数値]`

**カテゴリ:** Balloon, text command

Clears the specified number of lines on the current scope, starting from the cursor position in the balloon.<br />
Text divided by `\_l[x,y]`, `\n`, `\n[half]`, or `\n[パーセント]` is treated as “lines.” However, divisions that contain no text, such as `\n\n` or divisions made by anything other than `\_l[x,y]`, are not treated as lines.<br />
As with `\c[char,数値]`, the order of appearance in the script is used.

**対応:** SSP

## 記述例

```sakurascript
トークを1行削除。\nこの行が削除される。\c[line,1]削除終了。\nこの行は削除される。\n\n\n\n\n\c[line,1]削除終了。\nこの行は削除されない。\_l[0,0]\c[line,1]削除終了。
```

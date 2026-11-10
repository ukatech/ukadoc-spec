# `\q[Title,script:内容 to execute]`

**カテゴリ:** Choice command

Displays a choice.<br />
After a selection, the content after script: is executed as Sakura Script.

**対応:** SSP

## 記述例

```sakurascript
\q[バルーンを閉じる,script:\e]\n入れ子も可能。\n\q[その１,"script:\q[その２,script:その３はない]"]
```

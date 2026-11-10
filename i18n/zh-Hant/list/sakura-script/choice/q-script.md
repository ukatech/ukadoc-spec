# `\q[タイトル,script:実行内容]`

**カテゴリ:** 選択肢コマンド

Displays choices.<br />
After selection, the content following script: is executed as Sakura Script.

**対応:** SSP

## 記述例

```sakurascript
\q[バルーンを閉じる,script:\e]\n入れ子も可能。\n\q[その１,"script:\q[その２,script:その３はない]"]
```

# `\q[タイトル,script:実行内容]`

**カテゴリ:** 选择项命令

显示选择项。<br />
选择后，将 script: 后的内容作为 Sakura Script 执行。

**対応:** SSP

## 記述例

```sakurascript
\q[バルーンを閉じる,script:\e]\n入れ子も可能。\n\q[その１,"script:\q[その２,script:その３はない]"]
```

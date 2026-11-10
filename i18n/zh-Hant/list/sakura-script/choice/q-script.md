# `\q[タイトル,script:実行内容]`

**カテゴリ:** 選項指令

顯示選項。<br />
選擇後，將 script: 後方的內容作為 Sakura Script 執行。

**対応:** SSP

## 記述例

```sakurascript
\q[バルーンを閉じる,script:\e]\n入れ子も可能。\n\q[その１,"script:\q[その２,script:その３はない]"]
```

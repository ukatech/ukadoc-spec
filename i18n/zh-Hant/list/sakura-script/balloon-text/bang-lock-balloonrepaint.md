# `\![lock,balloonrepaint]`

**カテゴリ:** balloon、文字指令

停止重繪 balloon，直到呼叫 `\![unlock,balloonrepaint]` 或腳本結束。<br />
此停止處理會在腳本結束時自動解除。<br />
但是，指定為 `\![lock,balloonrepaint,manual]` 時，會持續停止，直到明確解除鎖定\[2.5.16\]

**対応:** SSP

## 記述例

```sakurascript
\![lock,balloonrepaint]この文章はスクリプト実行が終わるまで表示されない。
```

# `\![lock,balloonrepaint]`

**カテゴリ:** 气球、文本命令

停止重绘气球，直到调用`\![unlock,balloonrepaint]`或脚本结束。<br />
此停止处理会在脚本结束时自动解除。<br />
但是，指定为`\![lock,balloonrepaint,manual]`时，会一直停止，直至显式解锁\[2.5.16\]

**対応:** SSP

## 記述例

```sakurascript
\![lock,balloonrepaint]この文章はスクリプト実行が終わるまで表示されない。
```

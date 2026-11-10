# `\![lock,balloonrepaint]`

**カテゴリ:** balloon, text command

Stop redrawing the balloon until `\![unlock,balloonrepaint]` is called or the script ends.<br />
This stop is automatically lifted when the script ends.<br />
However, specifying `\![lock,balloonrepaint,manual]` keeps redrawing stopped until explicitly unlocked. \[2.5.16\]

**対応:** SSP

## 記述例

```sakurascript
\![lock,balloonrepaint]この文章はスクリプト実行が終わるまで表示されない。
```

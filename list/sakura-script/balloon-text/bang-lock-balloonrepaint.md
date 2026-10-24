# `\![lock,balloonrepaint]`

**カテゴリ:** バルーン、テキストコマンド

`\![unlock,balloonrepaint]`が呼ばれるか、スクリプト終端までバルーンの再描画を停止する。<br />
この停止処理はスクリプト終端で自動的に解除される。<br />
ただし、`\![lock,balloonrepaint,manual]`と指定すると、明示的にunlockするまで停止される\[2.5.16\]

**対応:** SSP

## 記述例

```sakurascript
\![lock,balloonrepaint]この文章はスクリプト実行が終わるまで表示されない。
```

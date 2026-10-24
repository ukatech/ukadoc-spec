# `\![lock,repaint]`

**カテゴリ:** サーフェスコマンド

`\![unlock,repaint]`が呼ばれるまで再描画を停止する。<br />
この停止処理はスクリプト終端で自動的に解除される。<br />
ただし、`\![lock,repaint,manual]`と指定すると、明示的にunlockするまで停止される\[2.5.16\]

**対応:** Materia / SSP / Ninix

## 記述例

```sakurascript
\s[0]\i[500]サーフェス0番のアニメーション500番を再生開始。\![lock,repaint]ここで、アニメーションの描画を停止。
```

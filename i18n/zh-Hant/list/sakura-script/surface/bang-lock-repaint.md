# `\![lock,repaint]`

**カテゴリ:** surface 指令

停止重繪，直到呼叫 `\![unlock,repaint]` 為止。<br />
此停止處理會在指令碼結束時自動解除。<br />
但指定為 `\![lock,repaint,manual]` 時，會持續停止，直到明確解除鎖定為止 \[2.5.16\]

**対応:** Materia / SSP / Ninix

## 記述例

```sakurascript
\s[0]\i[500]サーフェス0番のアニメーション500番を再生開始。\![lock,repaint]ここで、アニメーションの描画を停止。
```

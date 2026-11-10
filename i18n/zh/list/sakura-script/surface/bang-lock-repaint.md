# `\![lock,repaint]`

**カテゴリ:** 表面命令

停止重绘，直到调用`\![unlock,repaint]`。<br />
此停止处理会在脚本结束时自动解除。<br />
但是，指定为`\![lock,repaint,manual]`时，直到明确调用unlock才会解除停止\[2.5.16\]

**対応:** Materia / SSP / Ninix

## 記述例

```sakurascript
\s[0]\i[500]サーフェス0番のアニメーション500番を再生開始。\![lock,repaint]ここで、アニメーションの描画を停止。
```

# `\![lock,repaint]`

**カテゴリ:** Surface command

Stop repainting until `\![unlock,repaint]` is called.<br />
This stop is automatically canceled at the end of the script.<br />
However, specifying `\![lock,repaint,manual]` keeps repainting stopped until it is explicitly unlocked\[2.5.16\]

**対応:** Materia / SSP / Ninix

## 記述例

```sakurascript
\s[0]\i[500]サーフェス0番のアニメーション500番を再生開始。\![lock,repaint]ここで、アニメーションの描画を停止。
```

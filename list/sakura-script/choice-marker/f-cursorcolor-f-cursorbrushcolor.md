# `\f[cursorcolor,色指定]`もしくは`\f[cursorbrushcolor,色指定]`

**カテゴリ:** 選択肢マーカー変更コマンド

選択中マーカーの矩形内の色を変更。`\f[cursormethod,描画方法]`の効果を受けて色が決まる点に注意。<br />
指定方法については[※下記参照](note-1.md#形状指定の方法)。

**対応:** SSP

## 記述例

```sakurascript
\f[cursorbrushcolor,red]\q[選択肢,OnTest]選択中の選択肢の形状がsquareの場合、背景色が赤色になる。
```

# `\f[cursorcolor,色指定]`或`\f[cursorbrushcolor,色指定]`

**カテゴリ:** 选项标记更改命令

更改选中标记矩形内的颜色。请注意，颜色会受`\f[cursormethod,描画方法]`的效果影响。<br />
指定方法请参见[※下文](note-1.md#形状指定の方法)。

**対応:** SSP

## 記述例

```sakurascript
\f[cursorbrushcolor,red]\q[選択肢,OnTest]選択中の選択肢の形状がsquareの場合、背景色が赤色になる。
```

# `\![enter,selectmode,モード(rect),左,上,右,下]\![enter,selectmode,モード(rect),当たり判定名]\![enter,selectmode,モード(rect)]`

**カテゴリ:** 未分类命令

启动选择模式。执行后会显示透明区域，拖动鼠标即可指定区域。<br />
执行后会触发 [OnSelectModeBegin](../../shiori-event/select-region-mode/OnSelectModeBegin.md)。另请参阅 OnSelectModeMouseUp、OnSelectModeMouseDown、OnSelectModeCancel 和 OnSelectModeComplete。<br />
目前只能指定表示矩形选择模式的 "rect"。省略时的处理方式也与指定 rect 相同。<br />
可以在模式之后指定选择区域的初始位置。可输入坐标，或输入要设为相同大小的碰撞判定名称。<br />
在此模式下不会重绘 surface。即使执行 Sakura Script（`\s[ID]`）或 dressup，绘制内容也不会改变，但更改会生效，并在执行 `\![leave,selectmode]` 时显示。

此模式会持续到 ghost 结束。

**対応:** SSP

## 記述例

```sakurascript
\![enter,selectmode,rect,head]セレクトモードを開始する。判定名headの範囲が初期選択されている。
```

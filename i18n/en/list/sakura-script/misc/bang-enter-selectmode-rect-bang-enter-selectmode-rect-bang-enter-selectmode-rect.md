# `\![enter,selectmode,モード(rect),左,上,右,下]\![enter,selectmode,モード(rect),当たり判定名]\![enter,selectmode,モード(rect)]`

**カテゴリ:** Uncategorized command

Starts selection mode. When executed, transparent areas are also displayed, and you can specify a region by dragging the mouse.<br />
After execution, [OnSelectModeBegin](../../shiori-event/select-region-mode/OnSelectModeBegin.md) is executed. See also OnSelectModeMouseUp, OnSelectModeMouseDown, OnSelectModeCancel, and OnSelectModeComplete.<br />
Currently, only "rect", which indicates rectangular selection mode, can be specified. If no mode is specified, it is treated as if rect were specified.<br />
You can specify the initial selection position after the mode. Enter coordinates or the name of a hit region set to the same size.<br />
The surface is not redrawn while this mode is active. Even if Sakura Script (`\s[ID]`) or dressup is applied, the display does not change, but the changes are applied and displayed when `\![leave,selectmode]` is executed.

This remains active until the ghost ends.

**対応:** SSP

## 記述例

```sakurascript
\![enter,selectmode,rect,head]セレクトモードを開始する。判定名headの範囲が初期選択されている。
```

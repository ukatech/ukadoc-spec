# `\![set,balloonalign,ID]`

**カテゴリ:** balloon, text command

Switch the balloon to the display direction specified by the ID below. The ID can be specified as follows.<br />
The values of [balloon.offsetx and balloon.offsety in the shell's descript.txt](../../../descript/shell/descript-txt/sakura.balloon.offsetx.md) and [balloon.offsetx and balloon.offsety in surfaces.txt](../../../descript/shell-surfaces/surface-brace/sakura.balloon.offsetx.md) are applied relative to the positions below. The default is none.

This remains in effect until the ghost exits.

- **left**: The balloon's upper-right corner touches the shell's upper-left coordinates.
- **center**: The balloon's bottom-center touches the shell's top-center coordinates.
- **top**: Same as center.
- **right**: The balloon's upper-left corner touches the shell's upper-right coordinates.
- **bottom**: The balloon's top-center touches the shell's bottom-center coordinates.
- **none**: Switches between left and right depending on the coordinates. After the shell is dragged, it switches if the balloon would be cut off.
- **anything else**: Same as none.

Different offsets can also be used for each direction. For left/right, offsetxl/offsetxr take priority; for center and top, offsetxc takes priority; for bottom, offsetxb takes priority (or offsetxc if offsetxb is not set). See [sakura.balloon.offsetx](../../../descript/shell/descript-txt/sakura.balloon.offsetx.md) for details.

**対応:** SSP

## 記述例

```sakurascript
\0\![set,balloonalign,top]本体側バルーンを、シェルの頭上に表示。\1\![set,balloonalign,right]相方側バルーンを、シェルの右側に表示。
```

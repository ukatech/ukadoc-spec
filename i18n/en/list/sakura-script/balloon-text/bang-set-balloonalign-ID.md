# `\![set,balloonalign,ID]`

**カテゴリ:** Balloon, text command

Switch the balloon to the display direction specified by the ID below. The ID can be specified as follows.<br />
The values of [balloon.offsetx and balloon.offsety in the shell's descript.txt](../../../descript/shell/descript-txt/sakura.balloon.offsetx.md) and [balloon.offsetx and balloon.offsety in surfaces.txt](../../../descript/shell-surfaces/surface-brace/sakura.balloon.offsetx.md) are applied relative to the positions below. The initial value is none.

This remains in effect until the ghost exits.

- **left**: The balloon's top-right corner aligns with the shell's top-left coordinates.
- **center**: The balloon's bottom-center aligns with the shell's top-center coordinates.
- **top**: Same as center.
- **right**: The balloon's top-left corner aligns with the shell's top-right coordinates.
- **bottom**: The balloon's top-center aligns with the shell's bottom-center coordinates.
- **none**: left and right switch depending on the coordinates. After the shell is dragged, the side switches if the balloon would be clipped.
- **Anything else**: Same as none.

Different offset values can also be used for each direction. For left/right, offsetxl/offsetxr take precedence; for center and top, offsetxc takes precedence; for bottom, offsetxb takes precedence (or offsetxc if offsetxb is not set). See [sakura.balloon.offsetx](../../../descript/shell/descript-txt/sakura.balloon.offsetx.md) for details.

**対応:** SSP

## 記述例

```sakurascript
\0\![set,balloonalign,top]本体側バルーンを、シェルの頭上に表示。\1\![set,balloonalign,right]相方側バルーンを、シェルの右側に表示。
```

# `\![set,balloonalign,ID]`

**カテゴリ:** 气球、文本命令

将气球切换到下列ID指定的显示方向。ID可按以下方式指定。<br />
以以下位置为基准，应用[shell的descript.txt中的balloon.offsetx和balloon.offsety值](../../../descript/shell/descript-txt/sakura.balloon.offsetx.md)以及[surfaces.txt中的balloon.offsetx和balloon.offsety值](../../../descript/shell-surfaces/surface-brace/sakura.balloon.offsetx.md)。初始值为none。

在ghost结束前一直有效。

- **left**: 气球右上角与shell左上角对齐。
- **center**: 气球下边中央与shell上边中央对齐。
- **top**: 与center相同。
- **right**: 气球左上角与shell右上角对齐。
- **bottom**: 气球上边中央与shell下边中央对齐。
- **none**: 根据坐标在left和right之间切换。shell拖动后，如果气球超出可见范围，则切换方向。
- **上述以外**: 与none相同。

也可以为不同方向使用不同的偏移值。left/right优先使用offsetxl/offsetxr，center・top优先使用offsetxc，bottom优先使用offsetxb（若不存在则使用offsetxc）。详情请参阅[sakura.balloon.offsetx](../../../descript/shell/descript-txt/sakura.balloon.offsetx.md)。

**対応:** SSP

## 記述例

```sakurascript
\0\![set,balloonalign,top]本体側バルーンを、シェルの頭上に表示。\1\![set,balloonalign,right]相方側バルーンを、シェルの右側に表示。
```

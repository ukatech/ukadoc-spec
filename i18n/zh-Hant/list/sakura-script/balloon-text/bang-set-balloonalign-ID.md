# `\![set,balloonalign,ID]`

**カテゴリ:** balloon、文字指令

將 balloon 切換為下列 ID 所指定的顯示方向。可定義以下 ID。<br />
以以下位置為基準，套用 [shell 的 descript.txt 中 balloon.offsetx 及 balloon.offsety 的值](../../../descript/shell/descript-txt/sakura.balloon.offsetx.md)、[surfaces.txt 中 balloon.offsetx 及 balloon.offsety 的值](../../../descript/shell-surfaces/surface-brace/sakura.balloon.offsetx.md)。初始值為 none。

持續有效直到 ghost 結束。

- **left**: shell 左上座標與 balloon 右上座標相接。
- **center**: shell 中央上方座標與 balloon 中央下方座標相接。
- **top**: 與 center 相同。
- **right**: shell 右上座標與 balloon 左上座標相接。
- **bottom**: shell 中央下方座標與 balloon 中央上方座標相接。
- **none**: 依座標切換 left 和 right。shell 拖曳移動後，如果 balloon 超出畫面，就會切換方向。
- **上述以外**: 與 none 相同。

也可以讓各方向使用不同的 offset 值。left/right 優先使用 offsetxl/offsetxr，center・top 優先使用 offsetxc，bottom 優先使用 offsetxb（若無則使用 offsetxc）。詳情請參閱 [sakura.balloon.offsetx](../../../descript/shell/descript-txt/sakura.balloon.offsetx.md)。

**対応:** SSP

## 記述例

```sakurascript
\0\![set,balloonalign,top]本体側バルーンを、シェルの頭上に表示。\1\![set,balloonalign,right]相方側バルーンを、シェルの右側に表示。
```

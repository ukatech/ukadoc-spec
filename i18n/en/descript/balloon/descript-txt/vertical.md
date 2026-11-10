# vertical,0/1

**カテゴリ:** descript.txt

If 1 is specified, text in this balloon is displayed in Japanese vertical writing (characters advance from top to bottom and lines advance from right to left).

When using vertical writing, the meaning of coordinate specifications in descript.txt changes as follows. Coordinates should still be specified relative to the top-left corner of the balloon image.

- origin.x … *right edge of the first column*. Columns advance from here toward the left. Usually this is not specified, and the validrect definition is used instead.
- origin.y … Starting position for character advancement (top edge of the first character). Usually this is not specified, and the validrect definition is used instead.
- validrect … Unchanged. The area in which text may be drawn.
- Specify the wrap position with [wordwrappoint.y](wordwrappoint.y.md). wordwrappoint.x is ignored.
- Specify the SSTP message display end position with [sstpmessage.yb](sstpmessage.yb.md). sstpmessage.xr is ignored.
- [number.y](number.y.md) (=number.yb) … *Bottom edge* of the counter value. The value extends upward from here. [number.x](number.x.md) (=number.xr) specifies the position of the column in which the value is placed.

Coordinates that should be measured from the right edge, such as origin.x and number.x, can be specified as negative values according to the rules for [\*1](../index.md#balloon設定) (for example, origin.x,-14 means 14 pixels from the right edge of the balloon image).

The vertical-writing variant of the specified font (with @ prefixed to the font name) is used automatically.<br />
If the specified font has no vertical-writing variant (such as a font file placed in the balloon folder or a Western font), it is automatically replaced with the vertical-writing variant of the environment's standard Gothic font.

Note also that the following settings work relative to the character advancement direction, rather than the “on-screen orientation.”

- `\f[align,～]` aligns characters within a column (left = top, right = bottom), while `\f[valign,～]` aligns them across the line thickness (top = right, bottom = left).
- arrow0 (scroll up) and arrow1 (scroll down) scroll right and left, respectively. The balloon must provide the images and their positions.
- Underlines (font.underline, `\f[underline,true]`, and anchor underlines) are drawn along the right side of a column.

One limitation is that the SSTP marker's sender display and the network update progress display are also drawn vertically. The input box (communicatebox) remains horizontal.

This can also be specified per balloon surface in [balloon(s/k)\*s.txt](../balloonsoption/index.md), but switching between vertical and horizontal writing for different surfaces in the same balloon will disrupt the layout of text that was displayed before the switch.

**既定値:** 0 (horizontal writing)

**対応:** SSP 2.8.80

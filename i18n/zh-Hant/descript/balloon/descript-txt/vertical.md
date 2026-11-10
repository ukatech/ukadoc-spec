# vertical,0/1

**カテゴリ:** descript.txt

If 1 is specified, the text in this balloon is displayed in Japanese vertical writing (characters flow from top to bottom, and lines flow from right to left).

With vertical writing, the meanings of coordinate specifications in descript.txt change as follows. Coordinates themselves should still be written with the top-left of the balloon image as the origin.

- origin.x … *right edge of the first column*. Columns proceed from here toward the left. This is usually omitted, leaving the position to the validrect definition.
- origin.y … The starting position for character flow (top edge of the first character). This is usually omitted, leaving the position to the validrect definition.
- validrect … No change. The area in which text may be drawn.
- Specify wrapping with [wordwrappoint.y](wordwrappoint.y.md). wordwrappoint.x is ignored.
- Specify the SSTP message display end position with [sstpmessage.yb](sstpmessage.yb.md). sstpmessage.xr is ignored.
- [number.y](number.y.md) (=number.yb) … The *bottom edge* of the counter value. The number extends upward from here. [number.x](number.x.md) (=number.xr) specifies the position of the column containing the number.

Coordinates for which you want to use the right edge as the reference, such as origin.x and number.x, can be specified as negative values according to the rules for [\*1](../index.md#balloon設定) (for example, origin.x,-14 means 14 pixels from the right edge of the balloon image).

The vertical-writing variant of the specified font (the font name prefixed with @) is used automatically.<br />
If the specified font has no vertical-writing variant (such as a font file placed in the balloon folder or a Western font), it is automatically replaced with the vertical-writing variant of the environment's default Gothic font.

Note that the following settings work based on the direction of character flow, rather than their “on-screen orientation.”

- `\f[align,～]` aligns characters within a column (left = top, right = bottom), while `\f[valign,～]` aligns across the line thickness (top = right, bottom = left).
- arrow0 (scroll up) and arrow1 (scroll down) mean scrolling right and left, respectively. Prepare the images and positions on the balloon side.
- Underlines (font.underline, `\f[underline,true]`, and anchor underlines) are drawn on the right side of the column.

As a limitation, the sender display for SSTP markers and the network update progress display are also drawn vertically. Input boxes (communicatebox) remain horizontal.

This can also be specified for each balloon surface using [balloon(s/k)\*s.txt](../balloonsoption/index.md), but switching between vertical and horizontal writing for different surfaces within the same balloon will disrupt the layout of text displayed before the switch.

**既定値:** 0 (horizontal writing)

**対応:** SSP 2.8.80

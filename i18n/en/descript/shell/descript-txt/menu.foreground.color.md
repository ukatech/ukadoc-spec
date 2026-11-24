# menu.foreground.color,color

**カテゴリ:** descript.txt

The background color of the selected item (the item under the cursor) in the owner draw menu. This color fills areas not covered by the selected background image ([menu.foreground.bitmap.filename](menu.foreground.bitmap.filename.md)), or the entire item if no image is specified.<br />
Specify the color using a color name (such as `red`), `#RRGGBB`, or `#RGB` (the `#` can be omitted).<br />
Red, green, and blue can also be specified separately by writing values from 0 to 255 in `menu.foreground.color.r` / `menu.foreground.color.g` / `menu.foreground.color.b`.

This can also be specified in the ghost's descript.txt. If specified in the shell's descript.txt, the shell's value takes precedence; otherwise, the ghost's value is used.

**既定値:** OS selected item (highlight) color

**対応:** SSP

# menu.background.color,color

**カテゴリ:** descript.txt

The background color of unselected items in the owner draw menu. This color fills areas not covered by the background image ([menu.background.bitmap.filename](menu.background.bitmap.filename.md)), or the entire item if no image is specified.<br />
Specify the color using a color name (such as `red`), `#RRGGBB`, or `#RGB` (the `#` can be omitted).<br />
Red, green, and blue can also be specified separately by writing values from 0 to 255 in `menu.background.color.r` / `menu.background.color.g` / `menu.background.color.b`.

This can also be specified in the ghost's descript.txt. If specified in the shell's descript.txt, the shell's value takes precedence; otherwise, the ghost's value is used.

**既定値:** OS menu color

**対応:** SSP

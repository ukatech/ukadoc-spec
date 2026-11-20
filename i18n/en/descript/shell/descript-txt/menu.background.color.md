# menu.background.color,color

**カテゴリ:** descript.txt

The background color of normal items in the owner draw menu. Areas not covered by the background image ([menu.background.bitmap.filename](menu.background.bitmap.filename.md)) are filled with this color (the entire item if no image is specified).<br />
Specify the color using a color name (such as `red`), `#RRGGBB`, or `#RGB` (the `#` may be omitted).<br />
Red, green, and blue can also be specified separately by writing values from 0 to 255 in `menu.background.color.r` / `menu.background.color.g` / `menu.background.color.b`.

This can also be specified in the ghost's descript.txt. If specified in the shell, the shell's value takes precedence; otherwise, the ghost's value is used.

**既定値:** The OS menu color

**対応:** SSP

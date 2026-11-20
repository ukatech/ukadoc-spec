# menu.sidebar.color,color

**カテゴリ:** descript.txt

The background color of the sidebar in the owner draw menu. This color fills the area not covered by the sidebar image ([menu.sidebar.bitmap.filename](menu.sidebar.bitmap.filename.md)). If there is no sidebar image and only [menu.sidebar.text](menu.sidebar.text.md) or [menu.sidebar.width](menu.sidebar.width.md) is specified, the entire sidebar is filled with this color.<br />
Specify the color using a color name (such as `red`), `#RRGGBB`, or `#RGB` (the `#` can be omitted).<br />
Red, green, and blue can also be specified separately by writing values from 0 to 255 in `menu.sidebar.color.r` / `menu.sidebar.color.g` / `menu.sidebar.color.b`.

This can also be specified in the ghost's descript.txt. If specified in the shell, the shell's value takes precedence; otherwise, the ghost's value is used.

**既定値:** The same color as [menu.foreground.color](menu.foreground.color.md)

**対応:** SSP

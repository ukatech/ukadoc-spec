# menu.sidebar.width,value

**カテゴリ:** descript.txt

The width of the sidebar in the owner draw menu, in pixels. A value of 0 is treated as unspecified.<br />
If a value larger than the sidebar image ([menu.sidebar.bitmap.filename](menu.sidebar.bitmap.filename.md)) is specified, the remaining area is filled with [menu.sidebar.color](menu.sidebar.color.md). If only this value is specified, with neither an image nor [menu.sidebar.text](menu.sidebar.text.md), a sidebar of that width is displayed using only the color.

This can also be specified in the ghost's descript.txt. If specified in the shell, the shell's value takes precedence; otherwise, the ghost's value is used.

**既定値:** The width of the sidebar image (or a width matching the text height if there is no image and only [menu.sidebar.text](menu.sidebar.text.md) is present)

**対応:** SSP

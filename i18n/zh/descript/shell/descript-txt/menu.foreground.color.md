# menu.foreground.color,颜色

**カテゴリ:** descript.txt

owner draw 菜单中，选中（光标所在）项的背景色。选中项的背景图像（[menu.foreground.bitmap.filename](menu.foreground.bitmap.filename.md)）未覆盖的部分（未指定图像时为整个项目）将填充此颜色。<br />
颜色可以用颜色名（如 `red`）、`#RRGGBB` 或 `#RGB` 指定（`#` 可以省略）。<br />
也可以在 `menu.foreground.color.r` / `menu.foreground.color.g` / `menu.foreground.color.b` 中填写 0～255 的数值，分别指定红、绿、蓝。

也可以写在 ghost 的 descript.txt 中。如果 shell 中有此设置，则优先使用 shell 的值；否则使用 ghost 的值。

**既定値:** OS 的选中项（高亮）颜色

**対応:** SSP

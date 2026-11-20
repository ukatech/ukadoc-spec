# menu.background.color,颜色

**カテゴリ:** descript.txt

owner draw 菜单中普通状态下菜单项的背景色。背景图像([menu.background.bitmap.filename](menu.background.bitmap.filename.md))未覆盖的部分（未指定图像时为整个菜单项）用此颜色填充。<br />
颜色可指定为颜色名（如 `red`）、`#RRGGBB` 或 `#RGB`（`#` 可省略）。<br />
也可以在 `menu.background.color.r` / `menu.background.color.g` / `menu.background.color.b` 中分别写入0～255的数值，指定红、绿、蓝分量。

也可写在 ghost 的 descript.txt 中。如果 shell 侧有设置，则优先使用 shell 侧的值；否则使用 ghost 侧的值。

**既定値:** OS 的菜单颜色

**対応:** SSP

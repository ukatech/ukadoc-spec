# menu.foreground.color,颜色

**カテゴリ:** descript.txt

owner draw 菜单中选中状态（光标所在）的项目背景色。选中状态的背景图像（[menu.foreground.bitmap.filename](menu.foreground.bitmap.filename.md)）未覆盖的部分（未指定图像时为整个项目）以此颜色填充。<br />
颜色可指定为颜色名称（如 `red`）、`#RRGGBB` 或 `#RGB`（可省略 `#`）。<br />
也可以在 `menu.foreground.color.r` / `menu.foreground.color.g` / `menu.foreground.color.b` 中填写 0～255 的数值，分别指定红、绿、蓝分量。

也可写入 ghost 侧的 descript.txt。如果 shell 侧已指定，则优先使用 shell 侧的值；否则使用 ghost 侧的值。

**既定値:** 操作系统的选中项目（高亮）颜色

**対応:** SSP

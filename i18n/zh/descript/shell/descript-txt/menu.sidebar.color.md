# menu.sidebar.color,颜色

**カテゴリ:** descript.txt

owner draw 菜单中侧边栏的背景色。侧边栏图像（[menu.sidebar.bitmap.filename](menu.sidebar.bitmap.filename.md)）未覆盖的部分以此颜色填充。如果没有侧边栏图像，只指定了 [menu.sidebar.text](menu.sidebar.text.md) 或 [menu.sidebar.width](menu.sidebar.width.md)，则整个侧边栏以此颜色填充。<br />
颜色可指定为颜色名称（如 `red`）、`#RRGGBB` 或 `#RGB`（可省略 `#`）。<br />
也可以在 `menu.sidebar.color.r` / `menu.sidebar.color.g` / `menu.sidebar.color.b` 中填写 0～255 的数值，分别指定红、绿、蓝分量。

也可写入 ghost 侧的 descript.txt。如果 shell 侧已指定，则优先使用 shell 侧的值；否则使用 ghost 侧的值。

**既定値:** 与 [menu.foreground.color](menu.foreground.color.md) 相同的颜色

**対応:** SSP

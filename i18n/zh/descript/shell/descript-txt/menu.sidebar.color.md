# menu.sidebar.color,颜色

**カテゴリ:** descript.txt

owner draw 菜单中侧边栏的背景色。侧边栏图像（[menu.sidebar.bitmap.filename](menu.sidebar.bitmap.filename.md)）未覆盖的部分将填充此颜色。如果没有侧边栏图像，仅指定了 [menu.sidebar.text](menu.sidebar.text.md) 或 [menu.sidebar.width](menu.sidebar.width.md)，则整个侧边栏填充此颜色。<br />
颜色可以用颜色名（如 `red`）、`#RRGGBB` 或 `#RGB` 指定（`#` 可以省略）。<br />
也可以在 `menu.sidebar.color.r` / `menu.sidebar.color.g` / `menu.sidebar.color.b` 中填写 0～255 的数值，分别指定红、绿、蓝。

也可以写在 ghost 的 descript.txt 中。如果 shell 中有此设置，则优先使用 shell 的值；否则使用 ghost 的值。

**既定値:** 与 [menu.foreground.color](menu.foreground.color.md) 相同的颜色

**対応:** SSP

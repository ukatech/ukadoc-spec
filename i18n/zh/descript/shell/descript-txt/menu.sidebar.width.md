# menu.sidebar.width,数值

**カテゴリ:** descript.txt

owner draw 菜单中侧边栏的宽度（像素）。0 与未指定的处理方式相同。<br />
如果指定的值大于侧边栏图像（[menu.sidebar.bitmap.filename](menu.sidebar.bitmap.filename.md)）的宽度，多余部分将用 [menu.sidebar.color](menu.sidebar.color.md) 填充。如果既没有图像也没有 [menu.sidebar.text](menu.sidebar.text.md)，只指定此值，则显示指定宽度的纯色侧边栏。

也可以写在 ghost 的 descript.txt 中。如果 shell 中有此设置，则优先使用 shell 的值；否则使用 ghost 的值。

**既定値:** 侧边栏图像的宽度（没有图像而仅有 [menu.sidebar.text](menu.sidebar.text.md) 时，宽度与文字高度相适应）

**対応:** SSP

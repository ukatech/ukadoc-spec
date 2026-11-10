# sakura.balloon.offsetx，坐标

**カテゴリ:** surface 块

仅对此 surface 生效的主体侧 balloon 位置 X 坐标。<br />
在offsetx / offsety后面附加一个表示方向的字符，可以根据 balloon 的显示位置使用不同的值（仅限 SSP）。

- **offsetx / offsety**: 不指定方向。在未填写下列项目时使用的默认值。
- **offsetxl / offsetyl**: balloon 显示在 shell 左侧时使用。
- **offsetxr / offsetyr**: balloon 显示在 shell 右侧时使用。
- **offsetxc / offsetyc**: balloon 显示在 shell 头顶或脚下时使用。适用于居中的两种情况。
- **offsetxb / offsetyb**: balloon 显示在 shell 脚下时使用。用于设置与头顶不同的值。

未设置offsetxb时使用offsetxc；若也未设置，则使用offsetx。未设置offsetxc / offsetxl / offsetxr时使用offsetx。X 坐标和 Y 坐标分别独立确定。<br />
此处填写的值优先于 shell 的[descript.txt](../../shell/descript-txt/sakura.balloon.offsetx.md)中填写的同名值。

符号方向与[descript.txt中的sakura.balloon.offsetx](../../shell/descript-txt/sakura.balloon.offsetx.md)相同。

**既定値:** 显示在左右时：使 balloon 的左右边缘与 surface 的右侧或左侧边缘对齐的位置<br />
显示在头顶或脚下时：surface 的中心

**対応:** Materia / SSP / CROW

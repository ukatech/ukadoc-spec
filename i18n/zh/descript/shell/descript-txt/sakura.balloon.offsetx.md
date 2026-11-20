# sakura.balloon.offsetx,坐标

**カテゴリ:** descript.txt

本体侧 balloon 位置的 X 坐标。<br />
在 offsetx / offsety 后附加一个表示方向的字符，可以根据 balloon 的显示位置使用不同的值（仅 SSP）。

- **offsetx / offsety**: 不指定方向。未设置以下项目时使用的默认值。
- **offsetxl / offsetyl**: 在 shell 左侧显示 balloon 时使用。
- **offsetxr / offsetyr**: 在 shell 右侧显示 balloon 时使用。
- **offsetxc / offsetyc**: 在 shell 头顶或脚下显示 balloon 时使用。这两种居中情况共用。
- **offsetxb / offsetyb**: 在 shell 脚下显示 balloon 时使用。当头顶和脚下需要使用不同的值时使用。

未设置时使用的值如下。X 坐标和 Y 坐标分别独立确定。

- **没有 offsetxb 时**: 按 offsetxc → offsetx 的顺序查找。
- **没有 offsetxc / offsetxl / offsetxr 时**: 使用 offsetx。

显示在哪个位置由 balloon 的 descript.txt 中的 [windowposition.x](../../balloon/descript-txt/windowposition.x.md)、shell 的 [sakura.balloon.alignment](sakura.balloon.alignment.md) 和 Sakura Script 的 [`\![set,balloonalign,ID]`](../../../list/sakura-script/balloon-text/bang-set-balloonalign-ID.md) 决定。

**注意正负号。**X 坐标的正方向在所有情况下都是靠近 shell 的方向，显示在左侧时向右为正，显示在右侧时**向左**为正（头顶和脚下时向右为正）。Y 坐标始终向下为正。<br />
但零点（基准）因方向而异。左右两侧的零点是 balloon 上边缘与 shell 图像上边缘对齐的位置；头顶的零点是 balloon 下边缘与 shell 图像上边缘相接的位置；脚下的零点是 balloon 上边缘与 shell 图像下边缘相接的位置。

也可以写在 ghost 的 descript.txt 中。如果 shell 侧有设置，则优先使用 shell 侧的值；否则使用 ghost 侧的值。

**既定値:** 无值

**対応:** Materia / SSP / CROW

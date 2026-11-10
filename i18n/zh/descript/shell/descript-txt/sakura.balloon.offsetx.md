# sakura.balloon.offsetx,坐标

**カテゴリ:** descript.txt

本体侧气泡位置的X坐标。<br />
在 offsetx / offsety 后附加一个表示方向的字符，可以根据气泡的显示位置使用不同的值（仅限SSP）。

- **offsetx / offsety**: 不指定方向。未指定下列设置时使用的默认值。
- **offsetxl / offsetyl**: 气泡显示在shell左侧时。
- **offsetxr / offsetyr**: 气泡显示在shell右侧时。
- **offsetxc / offsetyc**: 气泡显示在shell头顶或脚下时。用于两种居中对齐的情况。
- **offsetxb / offsetyb**: 气泡显示在shell脚下时。用于需要为头顶和脚下指定不同值的情况。

未指定时的取值方式如下。X坐标和Y坐标分别独立确定。

- **offsetxb 未设置时**: 按 offsetxc → offsetx 的顺序查找。
- **offsetxc / offsetxl / offsetxr 未设置时**: 使用 offsetx。

气泡显示在哪一侧，由气泡的descript.txt中的[windowposition.x](../../balloon/descript-txt/windowposition.x.md)、shell中的[sakura.balloon.alignment](sakura.balloon.alignment.md)以及Sakura Script的[`\![set,balloonalign,ID]`](../../../list/sakura-script/balloon-text/bang-set-balloonalign-ID.md)决定。

**注意符号。**X坐标的＋在所有情况下都表示朝shell靠近的方向，显示在左侧时为向右，显示在右侧时为**向左** (头顶和脚下时，向右为＋)。Y坐标的＋始终表示向下。<br />
但各方向的0位置（基准）不同。左右两侧时，气泡上端与shell图像上端对齐；头顶时，气泡下端与shell图像上端相接；脚下时，气泡上端与shell图像下端相接。

**既定値:** ghost的descript设置

**対応:** Materia / SSP / CROW

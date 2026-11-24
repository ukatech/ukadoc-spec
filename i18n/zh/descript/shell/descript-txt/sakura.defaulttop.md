# sakura.defaulttop,Y坐标

**カテゴリ:** descript.txt

本体侧（`\0`）默认位置的 Y 坐标。将角色窗口的上边缘置于此位置。<br />
值的格式和含义（单位、坐标系、负值、-- 的处理方式及失效条件）与 SHIORI 资源的 [sakura.defaulttop](../../../list/shiori-resource/ghost/sakura.defaulttop.md) 相同。负值表示距下边缘的间距。\[2.9.13\]<br />
仅在不沿上边缘或下边缘对齐的设置下有效，例如 [seriko.alignmenttodesktop](seriko.alignmenttodesktop.md) 为 free 时。<br />
优先级为 SHIORI 资源＞shell 侧的 descript.txt（本项）＞ghost 侧的 descript.txt。如果同一个 descript.txt 中也指定了 [sakura.defaulty](sakura.defaulty.md)，则优先使用后者。

也可写入 ghost 侧的 descript.txt。如果 shell 侧已指定，则优先使用 shell 侧的值；否则使用 ghost 侧的值。

**既定値:** 无值（本体侧置于工作区的下边缘）

**対応:** SSP

# sakura.defaultleft,X坐标

**カテゴリ:** descript.txt

本体侧（`\0`）默认位置的 X 坐标。将角色窗口的左边缘置于此位置。<br />
值的格式和含义（单位、坐标系、负值、-- 的处理方式及失效条件）与 SHIORI 资源的 [sakura.defaultleft](../../../list/shiori-resource/ghost/sakura.defaultleft.md) 相同。负值表示距右边缘的间距。\[2.9.13\]<br />
优先级为 SHIORI 资源＞shell 侧的 descript.txt（本项）＞ghost 侧的 descript.txt。如果同一个 descript.txt 中也指定了 [sakura.defaultx](sakura.defaultx.md)，则优先使用后者。

也可写入 ghost 侧的 descript.txt。如果 shell 侧已指定，则优先使用 shell 侧的值；否则使用 ghost 侧的值。

**既定値:** 无值（本体侧置于主显示器工作区的右下角）

**対応:** SSP

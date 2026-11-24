# sakura.defaultx,X坐标

**カテゴリ:** descript.txt

本体侧（`\0`）默认位置的 X 坐标。将 surface 的基准点（通常为 surface 的底部中央）置于此位置。\[2.9.13\]<br />
值的格式和含义（单位、坐标系、负值、-- 的处理方式及失效条件）与 SHIORI 资源的 [sakura.defaultx](../../../list/shiori-resource/ghost/sakura.defaultx.md) 相同。<br />
优先级为 SHIORI 资源＞shell 侧的 descript.txt（本项）＞ghost 侧的 descript.txt。<br />
如果同一个 descript.txt 中也指定了 [sakura.defaultleft](sakura.defaultleft.md)，则优先使用本项（defaultx）。

也可写入 ghost 侧的 descript.txt。如果 shell 侧已指定，则优先使用 shell 侧的值；否则使用 ghost 侧的值。

**既定値:** 无值（本体侧置于主显示器工作区的右下角）

**対応:** SSP

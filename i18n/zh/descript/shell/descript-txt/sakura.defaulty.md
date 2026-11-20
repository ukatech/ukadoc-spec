# sakura.defaulty,Y坐标

**カテゴリ:** descript.txt

本体侧（`\0`）默认位置的 Y 坐标。将 surface 的基准点（通常是 surface 的底部中央）放在此位置。\[2.9.13\]<br />
值的格式和含义（单位、坐标系、负值、-- 的处理方式及无效条件）与 SHIORI 资源的 [sakura.defaulty](../../../list/shiori-resource/ghost/sakura.defaulty.md) 相同。<br />
优先级为 SHIORI 资源＞shell 侧的 descript.txt（此项）＞ghost 侧的 descript.txt。<br />
如果同一 descript.txt 中也设置了 [sakura.defaulttop](sakura.defaulttop.md)，则优先使用此项（defaulty）。

也可以写在 ghost 的 descript.txt 中。如果 shell 侧有设置，则优先使用 shell 侧的值；否则使用 ghost 侧的值。

**既定値:** 无值（本体侧放在工作区域的下边缘）

**対応:** SSP

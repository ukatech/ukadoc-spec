# sakura.defaultx,X 坐标

**カテゴリ:** descript.txt

sakura 侧（`\0`）默认位置的 X 坐标。将 surface 的基准点（通常是 surface 的底部中央）置于此位置。\[2.9.13\]<br />
值的格式和含义（单位、坐标系、负值、-- 的处理方式、无效条件）与 SHIORI 资源的 [sakura.defaultx](../../../list/shiori-resource/ghost/sakura.defaultx.md) 相同。<br />
优先级为：SHIORI 资源＞[shell 侧的 descript.txt](../../shell/descript-txt/sakura.defaultx.md)＞ghost 侧的 descript.txt。<br />
如果同一个 descript.txt 中也写有 [sakura.defaultleft](sakura.defaultleft.md)，则此项（defaultx）优先。

**既定値:** 无值（sakura 侧会置于主显示器工作区的右下方）

**対応:** SSP

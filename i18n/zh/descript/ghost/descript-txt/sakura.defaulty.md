# sakura.defaulty,Y坐标

**カテゴリ:** descript.txt

主机侧(`\0`)默认位置的Y坐标。将 surface 的基准点（通常是 surface 的底部中央）置于此位置。\[2.9.13\]<br />
值的格式和含义（单位、坐标系、负值、--的处理方式、无效条件）与SHIORI资源的[sakura.defaulty](../../../list/shiori-resource/ghost/sakura.defaulty.md)相同。<br />
优先级为：SHIORI资源＞[shell侧的descript.txt](../../shell/descript-txt/sakura.defaulty.md)＞ghost侧的descript.txt。<br />
如果同一descript.txt中也写有[sakura.defaulttop](sakura.defaulttop.md)，则此项(defaulty)优先。

**既定値:** 无值（主机侧会置于工作区下端）

**対応:** SSP

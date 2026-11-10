# sakura.defaultx,X坐标

**カテゴリ:** descript.txt

本体侧(`\0`)默认位置的X坐标。将surface基准点（通常是surface的底部中央）放置在此位置。\[2.9.13\]<br />
值的格式和含义（单位、坐标系、负值、--的处理方式、失效条件）与SHIORI资源的[sakura.defaultx](../../../list/shiori-resource/ghost/sakura.defaultx.md)相同。<br />
优先级为SHIORI资源＞shell侧的descript.txt（本项）＞[ghost侧的descript.txt](../../ghost/descript-txt/sakura.defaultx.md)。<br />
如果同一个descript.txt中也写有[sakura.defaultleft](sakura.defaultleft.md)，则本项(defaultx)优先。

**既定値:** ghost的descript设置

**対応:** SSP

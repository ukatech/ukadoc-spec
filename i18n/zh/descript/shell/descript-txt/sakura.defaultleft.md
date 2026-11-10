# sakura.defaultleft,X坐标

**カテゴリ:** descript.txt

本体侧(`\0`)默认位置的X坐标。将角色窗口的左端放置在此位置。<br />
值的格式和含义（单位、坐标系、负值、--的处理方式、失效条件）与SHIORI资源的[sakura.defaultleft](../../../list/shiori-resource/ghost/sakura.defaultleft.md)相同。负值表示距右端的留白。\[2.9.13\]<br />
优先级为SHIORI资源＞shell侧的descript.txt（本项）＞[ghost侧的descript.txt](../../ghost/descript-txt/sakura.defaultleft.md)。如果同一个descript.txt中也写有[sakura.defaultx](sakura.defaultx.md)，则后者优先。

**既定値:** ghost的descript设置

**対応:** SSP

# sakura.defaulttop,Y坐标

**カテゴリ:** descript.txt

本体侧(`\0`)默认位置的Y坐标。将角色窗口的上端放置在此位置。<br />
值的格式和含义（单位、坐标系、负值、--的处理方式、失效条件）与SHIORI资源的[sakura.defaulttop](../../../list/shiori-resource/ghost/sakura.defaulttop.md)相同。负值表示距下端的留白。\[2.9.13\]<br />
仅当设置为不贴合上端/下端的位置时（例如[seriko.alignmenttodesktop](seriko.alignmenttodesktop.md)为free时）有效。<br />
优先级为SHIORI资源＞shell侧的descript.txt（本项）＞[ghost侧的descript.txt](../../ghost/descript-txt/sakura.defaulttop.md)。如果同一个descript.txt中也写有[sakura.defaulty](sakura.defaulty.md)，则后者优先。

**既定値:** ghost的descript设置

**対応:** SSP

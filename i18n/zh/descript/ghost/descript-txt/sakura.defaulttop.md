# sakura.defaulttop,Y坐标

**カテゴリ:** descript.txt

本体一侧（`\0`）默认位置的Y坐标。将角色窗口的上端放置在此位置。<br />
值的格式和含义（单位、坐标系、负值、--的处理方式、无效条件）与SHIORI资源中的[sakura.defaulttop](../../../list/shiori-resource/ghost/sakura.defaulttop.md)相同。负值表示距下端的边距。\[2.9.13\]<br />
仅当设置不沿上端/下端对齐时才有效，例如[seriko.alignmenttodesktop](seriko.alignmenttodesktop.md)为free时。<br />
优先级为：SHIORI资源＞[shell侧的descript.txt](../../shell/descript-txt/sakura.defaulttop.md)＞ghost侧的descript.txt。如果同一descript.txt中也写有[sakura.defaulty](sakura.defaulty.md)，则以后者为准。

**既定値:** 无值（本体一侧放置在工作区的下端）

**対応:** SSP

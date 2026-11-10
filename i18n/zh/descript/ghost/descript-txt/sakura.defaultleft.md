# sakura.defaultleft,X坐标

**カテゴリ:** descript.txt

本体一侧（`\0`）默认位置的X坐标。将角色窗口的左端放置在此位置。<br />
值的格式和含义（单位、坐标系、负值、--的处理方式、无效条件）与SHIORI资源中的[sakura.defaultleft](../../../list/shiori-resource/ghost/sakura.defaultleft.md)相同。负值表示距右端的边距。\[2.9.13\]<br />
优先级为：SHIORI资源＞[shell侧的descript.txt](../../shell/descript-txt/sakura.defaultleft.md)＞ghost侧的descript.txt。如果同一descript.txt中也写有[sakura.defaultx](sakura.defaultx.md)，则以后者为准。

**既定値:** 无值（本体一侧放置在主显示器工作区的右下角）

**対応:** SSP

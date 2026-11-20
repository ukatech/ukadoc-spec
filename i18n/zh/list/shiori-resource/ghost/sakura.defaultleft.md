# sakura.defaultleft

**カテゴリ:** ghost信息

主体侧（`\0`）默认位置的X坐标。将角色窗口的左边缘置于此位置。<br />
使用默认位置的场景，以及值的单位、坐标系和失效条件均与[sakura.defaultx](sakura.defaultx.md)相同。如果同时指定了[sakura.defaultx](sakura.defaultx.md)，则后者优先。<br />
负值表示从主显示器工作区域的右边缘到角色右边缘的距离。-0表示紧贴右边缘。可以不考虑surface的宽度，将其指定为距屏幕右边缘的余量。\[2.9.13\]<br />
连续使用两个-表示负坐标本身（--100表示X坐标-100）。\[2.9.13\]<br />
也可以在[ghost](../../../descript/shell/descript-txt/sakura.defaultleft.md)和[shell](../../../descript/shell/descript-txt/sakura.defaultleft.md)的descript.txt中填写相同项目。SHIORI资源的设置优先。

**対応:** Materia / SSP / CROW

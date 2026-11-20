# sakura.defaulttop,Y坐标

**カテゴリ:** descript.txt

本体侧（`\0`）默认位置的 Y 坐标。将角色窗口的上边缘放在此位置。<br />
值的格式和含义（单位、坐标系、负值、-- 的处理方式及无效条件）与 SHIORI 资源的 [sakura.defaulttop](../../../list/shiori-resource/ghost/sakura.defaulttop.md) 相同。负值表示距下边缘的间距。\[2.9.13\]<br />
仅在设置为不沿上边缘或下边缘排列时有效，例如 [seriko.alignmenttodesktop](seriko.alignmenttodesktop.md) 为 free 时。<br />
优先级为 SHIORI 资源＞shell 侧的 descript.txt（此项）＞ghost 侧的 descript.txt。如果同一 descript.txt 中也设置了 [sakura.defaulty](sakura.defaulty.md)，则优先使用该值。

也可以写在 ghost 的 descript.txt 中。如果 shell 侧有设置，则优先使用 shell 侧的值；否则使用 ghost 侧的值。

**既定値:** 无值（本体侧放在工作区域的下边缘）

**対応:** SSP

# asis

**カテゴリ:** surface 大括号 \> 绘制方法

与[overlay](overlay.md)相近，但叠加时会忽略*新建图层*的透明度（透明色，以及设置了pna或[seriko.use_self_alpha](../../../shell/descript-txt/seriko.use_self_alpha.md)时图像本身的alpha通道）。<br />
也可用于dressup和element。<br />
使用asis方法合成element合成的surface，并将其作为其他surface的动画部件时，显示效果未定义；但在Windows上，透明区域通常会显示为黑色（#000000），不受图像原有透明色的影响。

**対応:** SSP

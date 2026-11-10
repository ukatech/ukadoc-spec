# base

**カテゴリ:** surface 大括号 \> 绘制方法

用*新建图层*完全替换[基础surface](../caption_basesurface.md)。collision也会更新为该帧surface中定义的内容。<br />
叠加此方法的pattern，可以实现通过重绘整个surface来制作动画（也就是类似翻页动画的效果）。<br />
在指定此绘制方法的pattern定义中，XY坐标会被忽略。<br />
在dressup和element中，base方法只能用于第一个位置（element0、pattern0）。其他位置会被转换为overlay。

**対応:** Materia / SSP / CROW

# blend-multiply-fast

**カテゴリ:** surface混合 \> 绘制方法

根据*基础图层*的不透明度，以正片叠底合成方式叠加*新图层*。<br />
其行为与overlay-fast相同，外形不会改变，但不会覆盖当前表面，而是对其进行正片叠底合成处理。<br />
也可用于dressup和element。<br />
名称中的「fast」源于历史原因，并不表示处理速度快。<br />
建议在shell的descript.txt中设置[`seriko.use_self_alpha,full`](../../../shell/descript-txt/seriko.use_self_alpha.md)。

**対応:** SSP 2.8.36

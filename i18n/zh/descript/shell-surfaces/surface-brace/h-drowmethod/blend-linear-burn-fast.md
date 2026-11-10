# blend-linear-burn-fast

**カテゴリ:** surface混合 \> 绘制方法

根据*基底图层*的不透明度，将*新图层*以线性加深混合模式叠加。<br />
其行为与overlay-fast相同，外形不会改变，但不是覆盖，而是对当前surface执行线性加深混合处理。<br />
也可用于dressup和element。<br />
名称中的「fast」源于历史原因，并不表示处理速度快。<br />
建议在shell的descript.txt中设置[`seriko.use_self_alpha,full`](../../../shell/descript-txt/seriko.use_self_alpha.md)。

**対応:** SSP 2.8.40

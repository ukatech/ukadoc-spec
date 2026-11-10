# blend-lighten-fast

**カテゴリ:** surface混合 \> 绘制方法

根据*基底图层*的不透明度，以比较（变亮）合成的方式叠加*新图层*。<br />
其行为与overlay-fast相同，外形不会改变，但不会进行覆盖，而是对当前surface执行比较（变亮）合成处理。<br />
也可用于dressup和element。<br />
名称中的「fast」源自历史原因，并不代表处理速度快。<br />
建议在shell的descript.txt中设置[`seriko.use_self_alpha,full`](../../../shell/descript-txt/seriko.use_self_alpha.md)。

**対応:** SSP 2.8.40

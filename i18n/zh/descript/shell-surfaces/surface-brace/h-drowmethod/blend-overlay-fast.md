# blend-overlay-fast

**カテゴリ:** surface混合 \> 绘制方法

根据*基础图层*的不透明度，以叠加混合的方式覆盖*新图层*。<br />
其行为与overlay-fast相同，外形不会改变，但不是覆盖，而是对当前surface执行叠加混合处理。<br />
这与[overlay](overlay.md)方法无关，暗部使用正片叠底，亮部使用滤色混合。<br />
也可用于dressup和element。<br />
名称中的「fast」源于历史原因，处理速度并不快。<br />
建议在shell的descript.txt中设置[`seriko.use_self_alpha,full`](../../../shell/descript-txt/seriko.use_self_alpha.md)。

**対応:** SSP 2.8.36

# blend-add-glow-fast

**カテゴリ:** surface 大括号 \> 绘制方法

根据*基础图层*的不透明度，将*新建图层*以加色（发光）混合方式叠加。<br />
其行为与overlay-fast相同，不会改变外形，但会对当前surface执行加色（发光）混合，而不是覆盖。<br />
也可用于dressup和element。<br />
名称中的「fast」源于历史原因，并不表示处理速度更快。<br />
建议在shell的descript.txt中设置[`seriko.use_self_alpha,full`](../../../shell/descript-txt/seriko.use_self_alpha.md)。

**対応:** SSP 2.8.46

# blend-saturation-fast

**カテゴリ:** surface brace \> 绘制方法

根据*基础图层*的不透明度，将*新建图层*以饱和度合成的方式叠加。<br />
其行为与overlay-fast相同，轮廓不会改变，但会对当前サーフェス执行饱和度合成处理，而不是覆盖。<br />
也可用于dressup和element。<br />
名称中的「fast」源自历史原因，并不表示处理速度快。<br />
建议在shell的descript.txt中设置[`seriko.use_self_alpha,full`](../../../shell/descript-txt/seriko.use_self_alpha.md)。

**対応:** SSP 2.8.39

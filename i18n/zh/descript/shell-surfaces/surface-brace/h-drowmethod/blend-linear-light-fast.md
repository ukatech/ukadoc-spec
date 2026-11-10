# blend-linear-light-fast

**カテゴリ:** surface brace \> 绘制方法

根据*基础图层*的不透明度，将*新建图层*以线性光混合方式叠加。<br />
其行为与overlay-fast相同，外形不会改变，但不会覆盖当前サーフェス，而是对其执行线性光混合处理。<br />
也可用于着せ替え和element。<br />
名称中的「fast」源于历史原因，并不代表处理速度快。<br />
建议在shell的descript.txt中设置[`seriko.use_self_alpha,full`](../../../shell/descript-txt/seriko.use_self_alpha.md)。

**対応:** SSP 2.8.40

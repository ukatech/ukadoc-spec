# blend-subtract-fast

**カテゴリ:** surface花括号 \> 绘制方法

根据*基础图层*的不透明度，将*新建图层*以减去混合的方式叠加。<br />
行为与 overlay-fast 相同，外形不会改变，但会对当前 surface 执行减去混合，而不是覆盖。<br />
也可用于 dressup 和 element。<br />
名称中的“fast”源于历史原因，并不表示处理速度更快。<br />
建议在 shell 的 descript.txt 中设置[`seriko.use_self_alpha,full`](../../../shell/descript-txt/seriko.use_self_alpha.md)。

**対応:** SSP 2.8.40

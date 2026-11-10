# blend-lighter-color-fast

**カテゴリ:** surface brace \> 描画方法

根据*基础层*的不透明度，以颜色较亮者合成的方式叠加*新建层*。<br />
行为与overlay-fast相同，轮廓不会改变，但不会直接覆盖，而是对当前surface执行颜色较亮者合成处理。<br />
也可用于dressup和element。<br />
名称中的「fast」源于历史原因，并不表示处理速度快。<br />
建议在shell的descript.txt中设置[`seriko.use_self_alpha,full`](../../../shell/descript-txt/seriko.use_self_alpha.md)。

**対応:** SSP 2.8.40

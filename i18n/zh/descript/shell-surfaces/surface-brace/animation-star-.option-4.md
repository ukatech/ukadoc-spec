# animation\*.option,选项

**カテゴリ:** surface块

exclusive、background、shared-index选项可以同时指定，也可以用+分隔指定多个选项。例如：exclusive+background<br />
animation后面的\*部分为animationID（与animation\*.interval中的\*相同）。<br />
例如animation\*.option,exclusive+background,(1,3,5)这种写法只会影响*exclusive*。<br />
另外，对于interval为bind的动画，exclusive指定本身没有定义。

**既定値:** 无效果

**対応:** SSP

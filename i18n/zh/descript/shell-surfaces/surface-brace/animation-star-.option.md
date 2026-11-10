# animation\*.option,exclusive

**カテゴリ:** surface块

动画的排他运行选项。<br />
也就是说，指定exclusive选项的动画开始运行时，其他所有动画都会停止；在该动画结束前，也不会有其他动画开始运行。<br />
animation后面的\*部分为animationID（与animation\*.interval中的\*相同）。<br />
另外，对于interval为bind的动画，此指定没有定义。<br />
仅SSP支持通过animation\*.option,exclusive,(1,3,5)这种写法，仅对指定ID的动画进行排他控制。<br />
[旧定义](caption_seriko-redefine.md)：\*option,exclusive

**既定値:** 无效果

**対応:** Materia / SSP / CROW

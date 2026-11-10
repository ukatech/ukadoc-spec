# char\*.recommendsites

**カテゴリ:** ghost信息

`\p[*]`侧的推荐列表。<br />
值以<br />
项目名1\[字节值1\]url1\[字节值1\]横幅图像路径1\[字节值1\]选中时的对话脚本1\[字节值2\]项目名2\[字节值1\]...<br />
这种格式返回。<br />
不过，SHIORI可能会在内部进行格式转换，详情请参阅各SHIORI的说明。<br />
对话脚本部分不是单纯的字符串，而是Sakura Script。<br />
url部分可以使用以script:开头的描述来代替url，执行对应脚本（也可以使用[`\![raise]`](../../sakura-script/event/bang-raise-r0-r1-r2.md)等）。

**対応:** SSP

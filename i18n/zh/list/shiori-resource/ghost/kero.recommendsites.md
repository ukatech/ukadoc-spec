# kero.recommendsites

**カテゴリ:** ghost信息

搭档侧的推荐列表。<br />
值为<br />
项目名1\[字节值1\]url1\[字节值1\]横幅图片路径1\[字节值1\]选中时的对话脚本1\[字节值2\]项目名2\[字节值1\]...<br />
以此格式返回。<br />
不过，有时SHIORI会在内部完成该格式的转换，详情请参阅各SHIORI的说明。<br />
对话脚本部分不是普通字符串，而是Sakura Script。<br />
url部分可用以script:开头的内容代替url，这样即可执行该脚本（也可以使用[`\![raise]`](../../sakura-script/event/bang-raise-r0-r1-r2.md)等）。

**対応:** Materia / SSP / CROW / Ninix

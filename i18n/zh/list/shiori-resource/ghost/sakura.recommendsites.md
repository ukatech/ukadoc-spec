# sakura.recommendsites

**カテゴリ:** 幽灵信息

本体侧推荐列表。<br />
值为<br />
项目名称1\[字节值1\]url1\[字节值1\]横幅图像路径1\[字节值1\]选中时的对话脚本1\[字节值2\]项目名称2\[字节值1\]...<br />
这样的格式。<br />
不过，SHIORI 可能会在内部进行格式转换，详情请参阅各 SHIORI 的说明。<br />
对话脚本部分不是普通字符串，而是 Sakura Script。<br />
url 部分可用以 script: 开头的描述代替 url，以执行该脚本（也可以使用[`\![raise]`](../../sakura-script/event/bang-raise-r0-r1-r2.md)等）。

**対応:** Materia / SSP / CROW / Ninix

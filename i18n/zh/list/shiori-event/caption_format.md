# 本页的格式说明

本页介绍在SHIORI/3.0及3.1（SSP扩展定义）中发出的各个SHIORI Event ID。<br />
未列于此处的事件可能位于[SHIORI Resource](../shiori-resource/index.md)或[来自外部的SHIORI Event](../shiori-event-ex/index.md)页面。

如需了解SHIORI Event本身，请参阅「[补充：什么是SHIORI Event](../../memo/shiori-event.md)」页面。

## Reference列表

对于带有Reference的SHIORI Event，都会列出其Reference列表。<br />
如果Reference编号部分为「\*」，则表示Reference的数量不定。<br />
也就是说，由于该Reference处理的项目数量*会因运行环境而异，因此编号不定*；此外，这些数量不定的Reference中的内容*格式都相同*。<br />
即使在这种情况下，Reference仍遵循从0开始连续编号的原则。因此，例如，若Reference列表中只有编号为\*的项目，则会排列从0到不定编号、格式相同的Reference（数量根据运行环境而定）；若列表中有Reference2，且下一行是Reference\*，则会排列从3到不定编号、格式相同的Reference。

## \[NOTIFY\]标记说明

说明文字中标有*\[NOTIFY\]*的SHIORI Event通常通过NOTIFY命令发出。<br />
没有标记时，通常通过GET命令发出。

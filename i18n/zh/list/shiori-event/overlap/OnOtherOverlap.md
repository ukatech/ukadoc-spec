# OnOtherOverlap

**カテゴリ:** 屏幕外与重叠事件

包括其他角色在内的所有已启动角色（surface）窗口发生重叠时触发。是OnOverlap的全局版。<br />
重叠状态发生变化时会逐次通知，因此也可以通过适当处理检测到“不再重叠”。<br />
请注意，也会同时通知自身的信息。

- **Reference0**: Sakura名称/ID-Sakura名称/ID \[`\1`\] Sakura名称/ID-Sakura名称/ID \[`\1`\] Sakura名称/ID-Sakura名称/ID ...<br />
  \[`\1`\] 是字节值1<br />
  例：Emily/0-玛丽/1 \[`\1`\] 玛丽/0-所长/1
- **Reference1**: 使用与Reference0相同的格式，通知状态变化前的值（即上一次事件触发时的Reference0）。

**対応:** SSP / Ninix

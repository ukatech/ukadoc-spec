# OnOtherOffscreen

**カテゴリ:** 屏幕外与重叠事件

包括其他角色在内的角色（surface）窗口被挤到显示器（工作区域）外，或移出显示器（工作区域）时触发。即窗口超出屏幕边界。是OnOffscreen的全局版。<br />
超出屏幕边界的状态发生变化时会逐次通知，因此也可以通过适当处理检测到“恢复到屏幕内”。<br />
请注意，也会同时通知自身的信息。

- **Reference0**: Sakura名称/ID \[`\1`\] Sakura名称/ID \[`\1`\] Sakura名称/ID ...<br />
  \[`\1`\] 是字节值1<br />
  例：Emily/1 \[`\1`\] 所长/0
- **Reference1**: 使用与Reference0相同的格式，通知状态变化前的值（即上一次事件触发时的Reference0）。

**対応:** SSP / Ninix

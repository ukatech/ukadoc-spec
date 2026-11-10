# OnDressupChanged

**カテゴリ:** 启动・结束・切换事件

dressup切换时触发。<br />
可能会收到多次通知，此时最后一次OnDressupChanged为*\[GET\]*，其他为*\[NOTIFY\]*。<br />
另请参阅此事件之后触发的[OnNotifyDressupInfo](../notify/OnNotifyDressupInfo.md)。

**dressup标志的变更差异过多时（目前为100个元素），将跳过此通知。需要接收大量变更时，请使用OnNotifyDressupInfo。**

- **Reference0**: dressup目标角色的ID。
- **Reference1**: 部件名称。
- **Reference2**: 启用时为1，禁用时为0。
- **Reference3**: 部件类别名称。
- **Reference4**: 从脚本执行时为script，从菜单执行时为user \[2.5.90～\]

**対応:** SSP / Ninix

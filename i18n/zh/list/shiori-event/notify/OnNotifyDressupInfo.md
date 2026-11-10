# OnNotifyDressupInfo

**カテゴリ:** Notify 事件

通知 dressup 信息。<br />
仅在启动时以 *\[NOTIFY\]* 发送；如果是通过菜单切换等用户操作触发，则以 *\[GET\]* 发送。<br />
另请参阅此事件之前发生的 [OnDressupChanged](../boot-close-change/OnDressupChanged.md)。

- **Reference\***: 以下信息以字节值1分隔：\[角色ID、类别名称、部件名称、选项、启用1/禁用0、缩略图路径\]<br />
  选项可能有多个，以逗号分隔。<br />
  按 dressup 定义的数量重复。<br />
  如果 ghost 端处理与上次通知相比的启用/禁用状态差异，就可以掌握发生了哪些变化。

**対応:** SSP

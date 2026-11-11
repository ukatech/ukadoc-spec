# OnSpectrePlugin.ConfirmCalibration

**カテゴリ:** plugin“Spectre”

如果此 ghost 尚未“校准”，打开 plugin 菜单时会发生此事件。用户选择“重新校准”此 ghost 时也会发生此事件。<br />
返回特定响应后，即可完成握手，使 ghost 自动完成“校准”步骤。<br />
所需的响应是以下标签：`\![raiseplugin,Spectre,OnCustomCalibrationConfirm]`<br />
发送此标签时，应附带包含表情数据的 Reference。Reference 的写法与 OnSpectrePlugin.Surface 事件中收到的相同，顺序不限。<br />
*默认情况下，只发送 ghost 未提供的表情。* plugin 会假定列表中未列出的表情均存在。<br />
对于兼容表情较少的 ghost，可以使用选项反转此行为，使 plugin 只使用列表中列出的表情。<br />
对于没有任何兼容表情的 ghost，有一个专用的 Reference。<br />
*ghost 的 shell 无法准确表现的表情应列为此标签的 Reference*（使用反转行为时则应省略），因为 plugin 会将此信息用于自身目的。

- **--option=include**: 只使用列表中列出的 surface（反转行为）。
- **\_\_NO_EXPRESSIONS\_\_**: 不使用任何表情。必须作为 reference0 发送。

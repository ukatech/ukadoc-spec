# OnSpectrePlugin.ConfirmCalibration

**カテゴリ:** plugin“Spectre”

打开plugin菜单时，如果此ghost尚未“校准”，则发生此事件。用户选择“重新校准”此ghost时也会发生。<br />
返回特定响应即可完成握手，使ghost能够自动完成“校准”步骤。<br />
需要返回的响应是以下标签：`\![raiseplugin,Spectre,OnCustomCalibrationConfirm]`<br />
在此标签中发送包含表情数据的Reference。Reference的写法与OnSpectrePlugin.Surface事件中接收的相同，顺序不限。<br />
*默认情况下，只发送ghost不提供的表情。* plugin假定未列出的表情均存在。<br />
对于兼容表情较少的ghost，可以通过选项反转此行为，使plugin只使用列出的表情。<br />
对于完全没有兼容表情的ghost，提供了专用Reference。<br />
*ghost的shell无法准确表现的表情应作为此标签的Reference列出*（使用反转行为时则应省略），因为plugin会将此信息用于自身用途。

- **--option=include**: 只使用列出的surface（反转行为）。
- **\_\_NO_EXPRESSIONS\_\_**: 不使用任何表情。必须作为reference0发送。

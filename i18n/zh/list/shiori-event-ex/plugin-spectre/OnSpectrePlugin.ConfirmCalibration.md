# OnSpectrePlugin.ConfirmCalibration

**カテゴリ:** 插件“Spectre”

如果该ghost尚未经过“校准”，打开插件菜单时会触发。用户选择该ghost的“重新校准”时也会触发。<br />
如果返回特定响应，就会建立握手机制，使ghost能够自动完成“校准”步骤。<br />
所需的响应标签为：`\![raiseplugin,Spectre,OnCustomCalibrationConfirm]`<br />
发送时需在此标签中附上包含表情数据的Reference。Reference的写法与OnSpectrePlugin.Surface事件接收的内容相同，顺序不限。<br />
*默认情况下，只发送ghost不提供的表情。* 列表中未列出的表情均视为插件支持。<br />
对于支持表情较少的ghost，可以选择反转此行为，让插件只使用列表中列出的表情。<br />
对于完全不支持任何表情的ghost，也有专用的Reference。<br />
*请将ghost的shell无法准确呈现的表情列入此标签的Reference*（使用反转行为时除外）。插件会将此信息用于自身的用途。

- **--option=include**: 只使用列表中的surface（反转行为）。
- **\_\_NO_EXPRESSIONS\_\_**: 不使用任何表情。必须作为reference0发送。

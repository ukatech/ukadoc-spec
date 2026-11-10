# OnMenuExec

**カテゴリ:** PLUGIN Event

通过所有者绘制菜单执行插件时触发。<br />
建议进行某种响应。

- **Reference0**: 以字节值1分隔的、调用插件的 ghost 的`\0`之后各角色窗口的 HWND。<br />
  例如尚未构建时，可能为0。
- **Reference1**: 调用插件的 ghost 名称。
- **Reference2**: 调用插件的 ghost 当前的 shell 名称。
- **Reference3**: 调用插件的 ghost 的 ID（与通过 Owned SSTP 发送的 ID 相同）。
- **Reference4**: 调用插件的 ghost 的完整路径。

**対応:** SSP

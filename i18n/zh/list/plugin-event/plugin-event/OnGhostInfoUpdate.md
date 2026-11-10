# OnGhostInfoUpdate

**カテゴリ:** PLUGIN Event

ghost 信息更改时发生。<br />
加载时也可能发生。*\[NOTIFY\]*

- **Reference0**: 以字节值1分隔，发生更改的 ghost 的`\0`之后各角色窗口的 HWND。<br />
  在窗口尚未创建等情况下，值可能为0。
- **Reference1**: 发生更改的 ghost 名称。
- **Reference2**: 发生更改的 ghost 当前的 shell 名称。
- **Reference3**: 发生更改的 ghost 的 ID（与 Owned SSTP 发送的相同）。
- **Reference4**: 发生更改的 ghost 的完整路径。

**対応:** SSP

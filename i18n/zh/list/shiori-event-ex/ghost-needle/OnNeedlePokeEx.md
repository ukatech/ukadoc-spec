# OnNeedlePokeEx

**カテゴリ:** ghost「Needle」

当 Needle（通过重叠）“戳”另一个 ghost 时触发。此事件在 [OnNeedlePoke](OnNeedlePoke.md) 之前触发，是 OnNeedlePoke 的多 scope 版本，可用于高级处理。

- **Reference0**: 所有被戳的 scope 的 ID，以逗号分隔的数组。主角色为 0，副角色为 1，追加角色为 2 及之后的数字。
- **Reference1**: Needle 当前使用的 shell 的名称。
- **Reference2**: 当前 dressup 的列表。这是一个二维数组，各 dressup 之间以 0xFDEF 分隔，每个 dressup 的类别名和部件名以 0x01 分隔。（例："Color\[0x01\]Gray\[0xFDEF\]Bow\[0x01\]Pink"）

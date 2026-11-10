# ShioriEcho.CommandComplete

**カテゴリ:** 用于ghost开发的交互式exe「ghost-terminal」

用户按下命令行最右端的 \`→\` 时触发的事件

- **Reference0**: 终端收集到的命令
- **Reference1**: 在光标位置按下 \`→\` 时，命令的首字符位置（起始值为0）。
- **返回值（可选）：X-SSTP-PassThru-Command**: 将命令替换为此内容。<br />
  ghost可以在此事件中自动补全命令。
- **返回值（可选）：X-SSTP-PassThru-InsertIndex**: 将光标移动到此位置（未提供时保持不变）。

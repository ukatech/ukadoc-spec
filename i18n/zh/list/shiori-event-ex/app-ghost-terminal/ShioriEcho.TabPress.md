# ShioriEcho.TabPress

**カテゴリ:** 用于ghost开发的交互式exe「ghost-terminal」

按下Tab时触发的命令补全事件。

- **Reference0**: 终端收集到的命令。
- **Reference1**: 按下Tab时光标所在的命令首字符位置（起始值为0）。
- **Reference2**: 用户首次连续按下Tab的次数（起始值为0）。
- **Reference3**: 在这轮Tab补全中，首次按下Tab时光标所在的命令首字符位置（起始值为0）。
- **返回值（可选）：X-SSTP-PassThru-Command**: 将命令替换为此内容。
- **返回值（可选）：X-SSTP-PassThru-InsertIndex**: 将光标移动到此位置（未提供时保持不变）。
- **返回值（可选）：X-SSTP-PassThru-OldInsertIndex**: 将后续的 \`Reference3\` 更新为此内容，并在本轮Tab补全结束前保持有效（未提供时保持不变）。

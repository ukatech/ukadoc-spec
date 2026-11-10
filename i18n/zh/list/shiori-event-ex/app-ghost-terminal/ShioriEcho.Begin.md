# ShioriEcho.Begin

**カテゴリ:** 用于ghost开发的交互式exe「ghost-terminal」

此ghost启动时触发的ghost_terminal事件

- **Reference0**: 终端版本
- **Reference1**: 终端的会话类型<br />
  终端以 \`-s\` 开头时，值为 \`SakuraScript\`。<br />
  终端以 \`-c\` 开头时，值为 \`Command\`。<br />
  终端以通用模式启动时，值为 \`Common\`。
- **返回值：X-SSTP-PassThru-Tittle（可选）**: 设置终端标题
- **返回值：X-SSTP-PassThru-Icon（可选）**: 设置终端图标
- **返回值：X-SSTP-PassThru-SmallIcon（可选）**: 设置终端小图标<br />
  未设置时，与 \`X-SSTP-PassThru-Icon\` 相同
- **返回值：X-SSTP-PassThru-CustomLoginInfo（可选）**: 设置此项后，终端不会显示默认登录信息，而是显示此<br />
  此返回值会进行简单转义：<br />
  \- \``\n`\` 会转换为换行。<br />
  \- \``\t`\` 会转换为制表符。<br />
  \- \`\\\\\` 会转换为 \`\\\`。

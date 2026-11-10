# ShioriEcho.GetResult

**カテゴリ:** 用于ghost开发的交互式exe「ghost-terminal」

值结果事件的查询

可回复的标头 1：

- **返回值：X-SSTP-PassThru-Result**: 显示内容，然后继续获取下一条命令。
- **返回值（可选）：X-SSTP-PassThru-Type**: 附加信息：值类型

可回复的标头 2：

- **返回值：X-SSTP-PassThru-Special**: 显示内容，然后继续获取下一条命令。<br />
  此返回值会进行简单转义：<br />
  \- \``\n`\` 会转换为换行。<br />
  \- \``\t`\` 会转换为制表符。<br />
  \- \`\\\\\` 会转换为 \`\\\`。

可回复的标头 3：空

等待1秒后重新执行ShioriEcho.GetResult。

其他

- **返回值：X-SSTP-PassThru-Status**: 此返回值可以与上述返回值组合使用<br />
  若为 \`End\`，终端将退出。<br />
  若为 \`Continue\`，终端不会显示任何内容，并继续获取下一条命令。

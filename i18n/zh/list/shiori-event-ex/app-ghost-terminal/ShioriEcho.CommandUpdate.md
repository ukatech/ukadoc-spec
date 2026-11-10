# ShioriEcho.CommandUpdate

**カテゴリ:** 用于ghost开发的交互式exe「ghost-terminal」

命令更新时触发的事件

- **Reference0**: 终端收集到的命令
- **返回值（可选）：X-SSTP-PassThru-CommandForDisplay**: 将显示的命令替换为此内容。<br />
  ghost可以利用此事件实现密码输入时的掩码、普通朗读时的语法高亮等功能。

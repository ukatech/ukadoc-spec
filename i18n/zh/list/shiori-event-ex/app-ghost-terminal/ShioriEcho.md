# ShioriEcho

**カテゴリ:** 用于开发 ghost 的交互式 exe「Ghost Terminal」

输入命令后触发的事件

- **Reference0**: 在终端中收集的命令
- **返回值**: 如果未定义\`ShioriEcho.GetResult\`，可以在此返回\`ShioriEcho.GetResult\`支持的任意返回值。这些返回值会由终端正确处理（但是，如果未定义\`ShioriEcho.GetResult\`且未返回任何内容，返回值3会进入获取下一条命令的流程）。<br />
  如果已定义\`ShioriEcho.GetResult\`，则忽略此处的返回值（\*\*但是，sakura script 会正常执行\*\*）。

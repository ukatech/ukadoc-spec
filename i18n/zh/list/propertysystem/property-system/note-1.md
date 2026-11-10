# 补充说明

## ※SHIORI Status头

多个状态可能以逗号(,)分隔后返回，也可能返回空值

- **talking**：正在执行脚本（正在说话）。
- **passive**：处于passive模式（`\![enter,passivemode]`）。
- **induction**：处于induction模式（`\![enter,inductionmode]`）。
- **timecritical**：被`\t`标签锁定。
- **nouserbreak**：处于nouserbreak模式（`\![enter,nouserbreak]`）。
- **online**：处于在线状态（例如正在获取新闻标题数据、校准时间或进行自身的网络更新）。
- **choosing**：正在通过`\q`、`\__q`标签显示选项。
- **minimizing**：处于最小化状态（已变为任务栏托盘图标）。
- **opening(种类)**：输入窗口已展开。<br />
  种类部分会以斜杠分隔，列出当前打开的窗口：communicate、input、teach、textarea、dialog。<br />
  示例：opening(input/dialog)<br />
  ※从SSP 2.3.97开始使用斜杠。更早版本使用逗号分隔<br />
  ※textarea从SSP 2.9.10开始支持
- **balloon(信息)**：正在显示气球。<br />
  信息部分会列出当前显示的气球，格式为(角色ID)=(气球ID)。气球ID不区分左右（始终为偶数）。<br />
  示例：balloon(0=2/1=0)<br />
  ※从SSP 2.3.97开始使用斜杠。更早版本使用逗号分隔

※也可以通过以下方式获取各SHIORI的Status头。

- 华和梨……System.Request.Status条目
- YAYA……status变量中
- 里々……信息获取变量（Status）

# OnDisplayHandover

**カテゴリ:** OS状态事件

窗口跨屏移动时触发。*\[NOTIFY/其他GET\]*

- **Reference0**: init (位置初始化完成时) 或 update (初始化后的更新) 。<br />
  init会在启动后窗口位置确定时通知，但不一定早于OnBoot。
- **Reference1**: 主体为0，伴侣为1。在SSP/CROW中也可能为2及以上。
- **Reference2**: 移动前　左、上、右、下、位深、是否为主显示器(0/1)　init时为空<br />
  示例： 0,0,1600,900,32,1
- **Reference3**: 移动后　左、上、右、下、位深、是否为主显示器(0/1)

**対応:** SSP 2.4.09

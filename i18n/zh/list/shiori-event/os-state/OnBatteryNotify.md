# OnBatteryNotify

**カテゴリ:** OS 状态事件

通知剩余电量。仅在启动时通过 *\[NOTIFY\]* 通知，其他情况下使用 GET。

- **Reference0**: 剩余电量百分比。
- **Reference1**: 剩余时间。未知时为 -1。
- **Reference2**: offline（电池供电）、online（外接电源供电）、backup（UPS 等备用电源）之一。
- **Reference3**: 以逗号分隔的字符串，表示以下状态。示例：low,charging<br />
  high：电池电量为 2/3 以上<br />
  low：电池电量为 1/3 以下（也会触发 OnBatteryLow）<br />
  critical：电池电量为 5％ 以下（也会触发 OnBatteryCritical）<br />
  charging：电池正在充电（也会触发 OnBatteryChargingStart/Stop）<br />
  no_battery：电池已取出<br />
  power_saving：电池节能功能已开启（SSP 2.3.94 及之后/Windows 10 及之后）

在 Windows 7 之前的操作系统中，high/low 的判定标准可能不同。

**対応:** SSP

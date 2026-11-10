# OnBatteryNotify

**カテゴリ:** OS 狀態事件

通知剩餘電池電量。僅於啟動時以*\[NOTIFY\]*通知，其餘情況使用 GET。

- **Reference0**: 剩餘電量百分比。
- **Reference1**: 剩餘時間。不明時為 -1。
- **Reference2**: offline（電池供電）、online（電源供電）、backup（UPS 等備用電源）三者之一。
- **Reference3**: 以逗號分隔通知表示下列狀態的字串。範例： low,charging<br />
  high：電池電量達 2/3 以上<br />
  low：電池電量為 1/3 以下（也會觸發 OnBatteryLow）<br />
  critical：電池電量為 5％ 以下（也會觸發 OnBatteryCritical）<br />
  charging：電池正在充電（也會觸發 OnBatteryChargingStart/Stop）<br />
  no_battery：已取出電池<br />
  power_saving：電池節電功能已開啟（SSP 2.3.94 以後／Windows 10 以後）

Windows 7 之前的 OS，其 high/low 判定基準可能不同。

**対応:** SSP

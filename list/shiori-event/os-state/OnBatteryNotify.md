# OnBatteryNotify

**カテゴリ:** OS状態イベント

残りバッテリー量を通知。起動時のみ*\[NOTIFY\]*で通知され、他はGET。

- **Reference0**: 残りバッテリー％。
- **Reference1**: 残り時間。不明の場合は-1。
- **Reference2**: offline(バッテリー駆動)・online(電源供給中)・backup(UPSなど補助電源)　のいずれか。
- **Reference3**: 以下の状態を示す文字列をカンマ区切りで通知。例： low,charging<br />
  high：バッテリー残量が2/3以上<br />
  low：バッテリー残量が1/3以下 (OnBatteryLowも発生)<br />
  critical：バッテリー残量が5％以下 (OnBatteryCriticalも発生)<br />
  charging：バッテリーが充電中（OnBatteryChargingStart/Stopも発生）<br />
  no_battery：バッテリーが取り外されている<br />
  power_saving：バッテリー節約機能がON (SSP 2.3.94以降/Windows 10以降)

Windows 7より前のOSでは、high/lowの基準が異なることがある。

**対応:** SSP

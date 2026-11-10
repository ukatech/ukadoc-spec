# OnBatteryNotify

**カテゴリ:** OS state event

Notify the remaining battery level. Notified using *\[NOTIFY\]* only at startup; otherwise, use GET.

- **Reference0**: Remaining battery percentage.
- **Reference1**: Remaining time. -1 if unknown.
- **Reference2**: One of offline (running on battery), online (connected to power), or backup (auxiliary power such as a UPS).
- **Reference3**: A comma-separated string indicating the following states. Example: low,charging<br />
  high: Battery level is at least 2/3<br />
  low: Battery level is 1/3 or less (OnBatteryLow also occurs)<br />
  critical: Battery level is 5% or less (OnBatteryCritical also occurs)<br />
  charging: Battery is charging (OnBatteryChargingStart/Stop also occurs)<br />
  no_battery: Battery has been removed<br />
  power_saving: Battery saver is ON (SSP 2.3.94 and later/Windows 10 and later)

On operating systems earlier than Windows 7, the thresholds for high/low may differ.

**対応:** SSP

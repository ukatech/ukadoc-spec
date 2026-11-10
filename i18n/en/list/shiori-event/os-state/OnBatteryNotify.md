# OnBatteryNotify

**カテゴリ:** OS state event

Notifies the remaining battery level. Notified with *\[NOTIFY\]* only at startup; GET is used at other times.

- **Reference0**: Remaining battery percentage.
- **Reference1**: Remaining time. -1 if unknown.
- **Reference2**: One of offline (battery power), online (external power), or backup (auxiliary power such as a UPS).
- **Reference3**: A comma-separated string indicating the following states. Example: low,charging<br />
  high: Battery level is at least 2/3<br />
  low: Battery level is at most 1/3 (also triggers OnBatteryLow)<br />
  critical: Battery level is at most 5% (also triggers OnBatteryCritical)<br />
  charging: Battery is charging (also triggers OnBatteryChargingStart/Stop)<br />
  no_battery: Battery has been removed<br />
  power_saving: Battery saver is ON (SSP 2.3.94 and later / Windows 10 and later)

On operating systems earlier than Windows 7, the thresholds for high/low may differ.

**対応:** SSP

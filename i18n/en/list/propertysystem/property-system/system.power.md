# system.power.(key)

**カテゴリ:** Property System

Power and battery status. The following strings can be used for (key). If information cannot be retrieved, including on systems without a battery (such as desktop PCs), each value will be set to the value listed below for "when unavailable".

- **source**: Current power source: battery (running on battery), ac (connected to AC power/outlet), or ups (via a UPS). If unavailable, this is unknown.
- **battery.percent**: Battery charge (%; integer). If unavailable or the charge is unknown, this is -1.
- **battery.lifetime**: Remaining operating time on battery power (seconds). If unavailable or the remaining time is unknown, this is -1.
- **battery.flag**: Battery status flags, listed as comma-separated values. Possible values are high (charge sufficient), low (low charge), critical (critically low), charging (charging), no_battery (no battery), and power_saving (battery saver is enabled; Windows 10 and later only). If unavailable, this is an empty string.

**対応:** SSP 2.8.17

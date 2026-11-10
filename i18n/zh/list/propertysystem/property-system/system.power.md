# system.power.(キー)

**カテゴリ:** Property system

Power and battery status. The strings that can be used for (キー) are as follows. If the information cannot be obtained, including on systems without a battery such as desktop PCs, each value will be set to the value indicated below for "unavailable".

- **source**: Current power source: one of battery (battery-powered), ac (connected to AC power/outlet), or ups (via a UPS). If unavailable, the value is unknown.
- **battery.percent**: Remaining battery charge (%; integer). If unavailable or the remaining charge is unknown, the value is -1.
- **battery.lifetime**: Remaining operating time on battery power alone (seconds). If unavailable or the remaining time is unknown, the value is -1.
- **battery.flag**: Battery status flags. Lists applicable statuses separated by commas. Possible values are high (sufficient charge), low (low charge), critical (critically low charge), charging (charging), no_battery (no battery), and power_saving (battery saver enabled; Windows 10 and later only). If unavailable, an empty string.

**対応:** SSP 2.8.17

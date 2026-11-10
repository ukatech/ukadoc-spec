# OnBatteryLow

**カテゴリ:** OS state event

Occurs when the battery level becomes low (OnBatteryNotify Reference3 is low or lower).<br />
Note that the external app “Kinoko” has an event [with the same name](../../shiori-event-ex/app-kinoko/OnBatteryCritical-kinoko.md).<br />
Implemented for compatibility with “Kinoko”.

- **Reference0～**: Same as OnBatteryNotify. When Reference3 becomes low or lower, this event also occurs after OnBatteryNotify. If you have implemented appropriate handling for OnBatteryNotify, no handling for this event is needed.

**対応:** SSP

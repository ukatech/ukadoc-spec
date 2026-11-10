# OnBatteryLow

**カテゴリ:** OS state event

Occurs when the battery level becomes low (OnBatteryNotify Reference3 is low or lower).<br />
Note that an event with [the same name](../../shiori-event-ex/app-kinoko/OnBatteryCritical-kinoko.md) is also notified by the external application “Kinoko”.<br />
Implemented as a compatibility event for “Kinoko”.

- **Reference0～**: Same as OnBatteryNotify. If Reference3 becomes low or lower, this event also occurs after OnBatteryNotify, so no handling is needed here if appropriate handling is implemented for OnBatteryNotify.

**対応:** SSP

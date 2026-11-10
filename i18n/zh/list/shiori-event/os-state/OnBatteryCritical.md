# OnBatteryCritical

**カテゴリ:** OS 状态事件

电池电量极低时触发（OnBatteryNotify Reference3 为 critical 或更低）。<br />
请注意，外部应用“きのこ”通知的事件中有一个[同名事件](../../shiori-event-ex/app-kinoko/OnBatteryCritical-kinoko.md)。<br />
此事件作为与“きのこ”兼容的事件实现。

- **Reference0～**: 与 OnBatteryNotify 相同。Reference3 变为 critical 时，会在 OnBatteryNotify 触发后再触发此事件，因此如果已为 OnBatteryNotify 实现适当的处理，则无需处理此事件。

**対応:** SSP

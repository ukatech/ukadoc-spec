# OnBatteryCritical

**カテゴリ:** OS 狀態事件

電池電量極低（OnBatteryNotify Reference3 為 critical 或更低）時觸發。<br />
請注意，外部應用程式「きのこ」通知的事件中也有[同名事件](../../shiori-event-ex/app-kinoko/OnBatteryCritical-kinoko.md)。<br />
此事件是為了與「きのこ」相容而實作。

- **Reference0～**: 與 OnBatteryNotify 相同。Reference3 變為 critical 時，OnBatteryNotify 觸發後也會觸發此事件；若已為 OnBatteryNotify 實作適當處理，則不必處理此事件。

**対応:** SSP

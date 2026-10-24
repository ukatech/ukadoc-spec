# OnBatteryCritical

**カテゴリ:** OS状態イベント

バッテリー残量が極端に少なく(OnBatteryNotify Reference3がcritical以下)になった際に発生する。<br />
外部アプリ「きのこ」が通知するイベントに[同名の物](../../shiori-event-ex/app-kinoko/OnBatteryCritical-kinoko.md)があるので注意。<br />
「きのこ」との互換用イベントとして実装されている。

- **Reference0～**: OnBatteryNotifyと同じ。Reference3がcriticalになった場合、OnBatteryNotifyが発生後に本イベントも発生するので、OnBatteryNotifyに適切な処理を実装している場合こちらの対応は不要。

**対応:** SSP
